#!/usr/bin/env python3
"""Atualiza o repositório a partir do hathdata.com e monta o README e a página (docs/index.html).

    python3 scripts/atualizar.py           # baixa os JSON de https://hathdata.com/dados/abertos/
    python3 scripts/atualizar.py --local   # só remonta README e página com os JSON de dados/

O hathdata.com é a fonte: este repositório só espelha e versiona. Roda todo dia no GitHub Actions.
"""
import html
import json
import sys
import urllib.request
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / 'dados'
SITE = 'https://hathdata.com'
REPO = 'https://github.com/hathdata/consultas-oficiais'
PAGES = 'https://hathdata.github.io/consultas-oficiais/'
ARQUIVOS = ['consultas.json', 'prefeituras.json', 'fontes-oficiais.json', 'paginas.json']
UTM = '?utm_source=github&utm_medium=dados-abertos&utm_campaign=consultas-oficiais'
ESFERAS = {'judiciario': 'Judiciário', 'municipal': 'Municipal', 'federal': 'Federal', 'estadual': 'Estadual', 'internacional': 'Internacional'}


def baixar():
    for arq in ARQUIVOS:
        req = urllib.request.Request(f'{SITE}/dados/abertos/{arq}', headers={'User-Agent': 'consultas-oficiais-sync'})
        with urllib.request.urlopen(req, timeout=60) as r:
            dado = json.loads(r.read().decode('utf-8'))
        if not dado.get('total'):
            raise SystemExit(f'{arq}: veio vazio, nada foi gravado')
        (DADOS / arq).write_text(json.dumps(dado, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def ler(arq):
    return json.loads((DADOS / arq).read_text(encoding='utf-8'))


def br(n):
    return f'{n:,}'.replace(',', '.')


def readme(c, p, f, pg):
    esferas = Counter(x['esfera'] for x in c['consultas'])
    prod = [x for x in p['prefeituras'] if x['situacao'] == 'em produção' and x['guia']]
    prod.sort(key=lambda x: (x['uf'], x['cidade']))
    linhas = '\n'.join(
        f"| {x['cidade']} | {x['uf']} | {'; '.join(x['documentos'][:3])} | [guia]({x['guia']}) |" for x in prod
    )
    tabela_tipos = '\n'.join(f'| {k[0].upper() + k[1:]} | {br(v)} |' for k, v in sorted(pg['tipos'].items(), key=lambda kv: -kv[1]))
    tabela_esfera = '\n'.join(f'| {ESFERAS.get(k, k)} | {br(v)} |' for k, v in esferas.most_common())
    return f"""# Consultas oficiais por CNPJ: dados abertos

**{c['slogan']}**

Lista aberta das consultas que a [Hath Data]({SITE}) faz em órgãos oficiais pelo CNPJ ou pela inscrição da
empresa: certidões, situação cadastral, processos e listas oficiais. Cada prefeitura vem com a guia da cidade e as
páginas oficiais (gov.br, jus.br, leg.br) que sustentam cada regra.

[Página com busca e filtro]({PAGES}) · [Catálogo no site]({SITE}/consultas) · [Guias por cidade]({SITE}/guias)

| Arquivo | O que tem | Registros |
| --- | --- | --- |
| [`dados/consultas.json`](dados/consultas.json) | consulta, órgão, esfera, UFs, dado de entrada, situação e página | {br(c['total'])} |
| [`dados/prefeituras.json`](dados/prefeituras.json) | cidade, UF, documentos, guia, página de API e fontes oficiais | {br(p['total'])} ({p['producao']} em produção, {p['estados']} estados) |
| [`dados/fontes-oficiais.json`](dados/fontes-oficiais.json) | página oficial citada e as guias que a citam | {br(f['total'])} |
| [`dados/paginas.json`](dados/paginas.json) | todas as páginas públicas do hathdata.com: título, tipo, data e consultas atendidas | {br(pg['total'])} |

**Catálogo completo**, por esfera e órgão, com link para cada consulta: [`CATALOGO.md`](CATALOGO.md) e
[página com filtro]({PAGES}consultas.html). **Mapa do site**, página por página: [{PAGES}paginas.html]({PAGES}paginas.html).

Atualizado em {c['geradoEm']}, todo dia, a partir de `{SITE}/dados/abertos/`.

## Consultas por esfera

| Esfera | Consultas |
| --- | --- |
{tabela_esfera}

## Páginas do site por tipo

| Tipo | Páginas |
| --- | --- |
{tabela_tipos}

## Prefeituras em produção

A certidão municipal não tem regra nacional: cada prefeitura define o portal, a validade e o que pede. A guia de
cada cidade traz o passo a passo e a norma, com link para a fonte oficial.

| Cidade | UF | Documentos | Guia |
| --- | --- | --- | --- |
{linhas}

A lista completa, com as cidades sob demanda, está em [`dados/prefeituras.json`](dados/prefeituras.json) e na
[página do projeto]({PAGES}).

## Como usar

```bash
curl -s {SITE}/dados/abertos/prefeituras.json | jq '.prefeituras[] | select(.uf == "MG") | .cidade'
```

```python
import pandas as pd, requests
dados = requests.get("{SITE}/dados/abertos/consultas.json").json()
df = pd.DataFrame(dados["consultas"])
df.groupby("esfera").size()
```

## Regras dos dados

- Só consultas feitas pelo **CNPJ** ou pela inscrição da empresa.
- Fonte só de domínio **oficial** (gov.br, jus.br, leg.br, mp.br). Nada de blog, fórum ou concorrente.
- Nenhum dado de contribuinte: a lista descreve as consultas, não o resultado delas.
- "Em produção" quer dizer que a consulta já roda no catálogo da Hath; "sob demanda" entra por mapeamento.

## Licença e citação

Dados sob [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR). Pode usar, inclusive comercialmente,
citando a fonte com link:

> Fonte: Hath Data, Consultas oficiais por CNPJ ({SITE}).

Há um [`CITATION.cff`](CITATION.cff) para gerar a citação pelo próprio GitHub.

## Sobre a Hath Data

A [Hath Data]({SITE}) automatiza consultas em órgãos oficiais e entrega o PDF e os dados no ERP, no CRM ou por API,
com monitoramento. [Consultas]({SITE}/consultas) · [API de CND]({SITE}/api-cnd) ·
[Guias]({SITE}/guias) · [LinkedIn](https://www.linkedin.com/company/hath-data/)
"""


def pagina(c, p, f):
    e = html.escape
    esferas = Counter(x['esfera'] for x in c['consultas'])
    linhas = []
    for x in sorted(p['prefeituras'], key=lambda x: (x['situacao'] != 'em produção', x['uf'], x['cidade'])):
        nome = f'<a href="{e(x["guia"] + UTM)}">{e(x["cidade"])}</a>' if x['guia'] else e(x['cidade'])
        api = f'<a href="{e(x["api"] + UTM)}">API</a>' if x['api'] else ''
        fontes = ' '.join(f'<a class="f" href="{e(s["url"])}" rel="noopener" title="{e(s["nome"])}">{i + 1}</a>' for i, s in enumerate(x['fontesOficiais'][:6]))
        linhas.append(
            f'<tr data-q="{e((x["cidade"] + " " + x["uf"]).lower())}"><td>{nome}</td><td>{e(x["uf"])}</td>'
            f'<td><span class="s{"p" if x["situacao"] == "em produção" else "d"}">{e(x["situacao"])}</span></td>'
            f'<td>{e("; ".join(x["documentos"][:3]))}</td><td>{api}</td><td>{fontes}</td></tr>'
        )
    ld = {
        '@context': 'https://schema.org',
        '@type': 'Dataset',
        'name': 'Consultas oficiais por CNPJ: dados abertos da Hath Data',
        'description': (
            f'{c["total"]} consultas a órgãos oficiais pelo CNPJ ou pela inscrição da empresa, {p["total"]} prefeituras '
            f'({p["producao"]} em produção, {p["estados"]} estados) com a guia de cada cidade e {f["total"]} páginas oficiais citadas.'
        ),
        'url': PAGES,
        'sameAs': REPO,
        'license': 'https://creativecommons.org/licenses/by/4.0/',
        'isAccessibleForFree': True,
        'inLanguage': 'pt-BR',
        'dateModified': c['geradoEm'],
        'spatialCoverage': {'@type': 'Country', 'name': 'Brasil'},
        'keywords': ['CND', 'certidão negativa municipal', 'consulta CNPJ', 'certidões', 'dados públicos', 'prefeituras'],
        'creator': {'@type': 'Organization', '@id': f'{SITE}/#organization', 'name': 'Hath Data', 'url': SITE},
        'distribution': [
            {'@type': 'DataDownload', 'encodingFormat': 'application/json', 'contentUrl': f'{SITE}/dados/abertos/{a}'} for a in ARQUIVOS
        ],
    }
    cards = ''.join(f'<div class="n"><b>{br(v)}</b><span>{e(ESFERAS.get(k, k))}</span></div>' for k, v in esferas.most_common())
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Consultas oficiais por CNPJ: dados abertos</title>
<meta name="description" content="{e(ld['description'])}">
<link rel="canonical" href="{PAGES}">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>
:root{{--tinta:#19232D;--cinza:#5c6b7d;--linha:#e3e8ef;--papel:#fff;--fundo:#f7f9fc;--azul:#2D6EDC;--roxo:#5A14A0;--ok:#0f7b4f;--dem:#8a5a00}}
@media (prefers-color-scheme:dark){{:root{{--tinta:#e8edf4;--cinza:#9aa8b8;--linha:#2a3442;--papel:#121821;--fundo:#0c1118;--azul:#6f9ff0;--roxo:#b38ae6;--ok:#4fd39a;--dem:#e2b34d}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--fundo);color:var(--tinta);font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}}
.w{{max-width:1080px;margin:0 auto;padding:32px 16px 64px}}
.rule{{height:5px;background:linear-gradient(90deg,#00DFEB,#2D6EDC 50%,#5A14A0)}}
.ey{{font:500 12px/1 ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--roxo)}}
h1{{font-size:clamp(28px,5vw,44px);line-height:1.08;letter-spacing:-.03em;margin:12px 0}}
h1 span{{background:linear-gradient(112deg,var(--azul),var(--roxo));-webkit-background-clip:text;background-clip:text;color:transparent}}
p.lead{{color:var(--cinza);max-width:720px}} a{{color:var(--azul)}}
.ns{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin:24px 0}}
.n{{background:var(--papel);border:1px solid var(--linha);border-radius:12px;padding:14px 16px}}.n b{{display:block;font-size:26px}}.n span{{color:var(--cinza);font-size:13px}}
input{{width:100%;padding:12px 14px;border:1px solid var(--linha);border-radius:10px;background:var(--papel);color:var(--tinta);font-size:16px;margin:8px 0 12px}}
.tb{{overflow-x:auto;background:var(--papel);border:1px solid var(--linha);border-radius:12px}}
table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{text-align:left;padding:10px 12px;border-bottom:1px solid var(--linha);vertical-align:top}}
th{{font-size:12px;color:var(--cinza);text-transform:uppercase;letter-spacing:.06em}}
.sp{{color:var(--ok);white-space:nowrap}}.sd{{color:var(--dem);white-space:nowrap}} a.f{{display:inline-block;min-width:20px;text-align:center;font-size:12px;border:1px solid var(--linha);border-radius:6px;margin:0 2px 2px 0;text-decoration:none}}
footer{{margin-top:40px;color:var(--cinza);font-size:14px}}
</style></head><body><div class="rule"></div><div class="w">
<div class="ey">Dados abertos · Hath Data</div>
<h1>Consultas oficiais por CNPJ, <span>em dados abertos.</span></h1>
<nav style="display:flex;flex-wrap:wrap;gap:8px 16px;margin:8px 0 20px"><a href="./">Prefeituras</a><a href="consultas.html">Catálogo de consultas ({br(c['total'])})</a><a href="paginas.html">Mapa do site</a><a href="{REPO}">GitHub</a></nav>
<p class="lead">{e(c['slogan'])} {br(c['total'])} consultas a órgãos oficiais pelo CNPJ ou pela inscrição da empresa,
{br(p['total'])} prefeituras com a guia de cada cidade e {br(f['total'])} páginas oficiais citadas. Atualizado em {e(c['geradoEm'])}.
Fonte: <a href="{SITE}/{UTM}">hathdata.com</a>. Código e histórico: <a href="{REPO}">GitHub</a>.</p>
<div class="ns">{cards}</div>
<h2>Prefeituras</h2>
<p class="lead">A certidão municipal não tem regra nacional. Cada guia traz o portal, a validade e a norma da cidade; os números
levam às páginas oficiais citadas.</p>
<input id="q" type="search" placeholder="Filtrar por cidade ou UF" aria-label="Filtrar por cidade ou UF">
<div class="tb"><table><thead><tr><th>Cidade</th><th>UF</th><th>Situação</th><th>Documentos</th><th>API</th><th>Fontes oficiais</th></tr></thead>
<tbody id="t">{''.join(linhas)}</tbody></table></div>
<h2>Arquivos</h2>
<ul>{''.join(f'<li><a href="{SITE}/dados/abertos/{a}">{a}</a> (<a href="{REPO}/blob/main/dados/{a}">no GitHub</a>)</li>' for a in ARQUIVOS)}</ul>
<p>Licença <a href="https://creativecommons.org/licenses/by/4.0/deed.pt_BR">CC BY 4.0</a>: use citando "Hath Data (hathdata.com)" com link.</p>
<footer><a href="{SITE}/{UTM}">Hath Data</a> · <a href="{SITE}/consultas{UTM}">Consultas</a> · <a href="{SITE}/guias{UTM}">Guias</a> ·
<a href="{SITE}/api-cnd{UTM}">API de CND</a> · <a href="https://www.linkedin.com/company/hath-data/">LinkedIn</a></footer>
</div>
<script>document.getElementById('q').addEventListener('input',function(){{var v=this.value.toLowerCase();document.querySelectorAll('#t tr').forEach(function(r){{r.style.display=r.dataset.q.indexOf(v)>-1?'':'none'}})}})</script>
</body></html>
"""


ESTILO = """<style>
:root{--tinta:#19232D;--cinza:#5c6b7d;--linha:#e3e8ef;--papel:#fff;--fundo:#f7f9fc;--azul:#2D6EDC;--roxo:#5A14A0;--ok:#0f7b4f;--dem:#8a5a00}
@media (prefers-color-scheme:dark){:root{--tinta:#e8edf4;--cinza:#9aa8b8;--linha:#2a3442;--papel:#121821;--fundo:#0c1118;--azul:#6f9ff0;--roxo:#b38ae6;--ok:#4fd39a;--dem:#e2b34d}}
*{box-sizing:border-box}body{margin:0;background:var(--fundo);color:var(--tinta);font:16px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
.w{max-width:1080px;margin:0 auto;padding:32px 16px 64px}.rule{height:5px;background:linear-gradient(90deg,#00DFEB,#2D6EDC 50%,#5A14A0)}
.ey{font:500 12px/1 ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--roxo)}
h1{font-size:clamp(26px,4.4vw,40px);line-height:1.1;letter-spacing:-.03em;margin:12px 0}h1 span{background:linear-gradient(112deg,var(--azul),var(--roxo));-webkit-background-clip:text;background-clip:text;color:transparent}
p.lead{color:var(--cinza);max-width:760px}a{color:var(--azul)}nav{display:flex;flex-wrap:wrap;gap:8px 16px;margin:8px 0 20px;font-size:15px}
.fx{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0 12px}.fx input{flex:1 1 260px}
input,select{padding:11px 13px;border:1px solid var(--linha);border-radius:10px;background:var(--papel);color:var(--tinta);font-size:16px}
.tb{overflow-x:auto;background:var(--papel);border:1px solid var(--linha);border-radius:12px}table{border-collapse:collapse;width:100%;font-size:14px}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--linha);vertical-align:top}th{font-size:12px;color:var(--cinza);text-transform:uppercase;letter-spacing:.06em}
.sp{color:var(--ok);white-space:nowrap}.sd{color:var(--dem);white-space:nowrap}.c{color:var(--cinza);font-size:13px}#n{color:var(--cinza);font-size:14px}
h2{margin-top:36px}footer{margin-top:40px;color:var(--cinza);font-size:14px}
</style>"""


def nav(e):
    return (f'<nav><a href="./">Prefeituras</a><a href="consultas.html">Catálogo de consultas</a><a href="paginas.html">Mapa do site</a>'
            f'<a href="{SITE}/{UTM}">hathdata.com</a><a href="{REPO}">GitHub</a></nav>')


def casca(titulo, descricao, url, corpo, ld=None):
    e = html.escape
    ldtag = f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>' if ld else ''
    return (f'<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{e(titulo)}</title><meta name="description" content="{e(descricao)}"><link rel="canonical" href="{url}">{ldtag}{ESTILO}</head>'
            f'<body><div class="rule"></div><div class="w">{corpo}<footer><a href="{SITE}/{UTM}">Hath Data</a> · Dados sob '
            f'<a href="https://creativecommons.org/licenses/by/4.0/deed.pt_BR">CC BY 4.0</a>, cite "Hath Data (hathdata.com)" com link.</footer></div></body></html>\n')


def pagina_consultas(c):
    e = html.escape
    linhas = []
    for x in sorted(c['consultas'], key=lambda x: (x['esfera'], x['orgao'], x['nome'])):
        nome = f'<a href="{e(x["pagina"] + UTM)}">{e(x["nome"])}</a>' if x['pagina'] else e(x['nome'])
        sit = 'sp' if x['situacao'] == 'em produção' else 'sd'
        linhas.append(f'<tr data-e="{e(x["esfera"])}" data-s="{sit}" data-q="{e((x["nome"] + " " + x["orgao"] + " " + " ".join(x["ufs"])).lower())}">'
                      f'<td>{nome}</td><td>{e(x["orgao"])}</td><td>{e(ESFERAS.get(x["esfera"], x["esfera"]))}</td><td>{e(", ".join(x["ufs"]) or "BR")}</td>'
                      f'<td class="c">{e(", ".join(x["entrada"]))}</td><td><span class="{sit}">{e(x["situacao"])}</span></td></tr>')
    opcoes = ''.join(f'<option value="{k}">{v}</option>' for k, v in ESFERAS.items())
    corpo = (f'<div class="ey">Dados abertos · Hath Data</div><h1>Catálogo de consultas oficiais, <span>completo.</span></h1>{nav(e)}'
             f'<p class="lead">{br(c["total"])} consultas a órgãos oficiais pelo CNPJ ou pela inscrição da empresa: '
             f'{br(sum(1 for x in c["consultas"] if x["situacao"] == "em produção"))} em produção e o restante sob demanda. '
             f'Cada nome leva à página da consulta no hathdata.com. Atualizado em {e(c["geradoEm"])}.</p>'
             f'<div class="fx"><input id="q" type="search" placeholder="Filtrar por consulta, órgão ou UF" aria-label="Filtrar">'
             f'<select id="es" aria-label="Esfera"><option value="">Todas as esferas</option>{opcoes}</select>'
             f'<select id="si" aria-label="Situação"><option value="">Toda situação</option><option value="sp">Em produção</option><option value="sd">Sob demanda</option></select></div>'
             f'<p id="n"></p><div class="tb"><table><thead><tr><th>Consulta</th><th>Órgão</th><th>Esfera</th><th>UF</th><th>Entrada</th><th>Situação</th></tr></thead>'
             f'<tbody id="t">{"".join(linhas)}</tbody></table></div>'
             '<script>var q=document.getElementById("q"),es=document.getElementById("es"),si=document.getElementById("si"),n=document.getElementById("n");'
             'function f(){var v=q.value.toLowerCase(),k=0;document.querySelectorAll("#t tr").forEach(function(r){var ok=r.dataset.q.indexOf(v)>-1&&(!es.value||r.dataset.e==es.value)&&(!si.value||r.dataset.s==si.value);r.style.display=ok?"":"none";if(ok)k++});n.textContent=k+" consultas"}'
             'q.oninput=es.onchange=si.onchange=f;f()</script>')
    ld = {'@context': 'https://schema.org', '@type': 'Dataset', 'name': 'Catálogo de consultas oficiais por CNPJ (Hath Data)',
          'description': f'{c["total"]} consultas a órgãos oficiais pelo CNPJ ou pela inscrição da empresa, com órgão, esfera, UF, dado de entrada e situação.',
          'url': PAGES + 'consultas.html', 'license': 'https://creativecommons.org/licenses/by/4.0/', 'isAccessibleForFree': True, 'inLanguage': 'pt-BR',
          'dateModified': c['geradoEm'], 'creator': {'@type': 'Organization', '@id': f'{SITE}/#organization', 'name': 'Hath Data', 'url': SITE},
          'distribution': [{'@type': 'DataDownload', 'encodingFormat': 'application/json', 'contentUrl': f'{SITE}/dados/abertos/consultas.json'}]}
    return casca('Catálogo de consultas oficiais por CNPJ', ld['description'], PAGES + 'consultas.html', corpo, ld)


def pagina_mapa(pg):
    e = html.escape
    grupos = {}
    for x in pg['paginas']:
        grupos.setdefault(x['tipo'], []).append(x)
    blocos = []
    for tipo, itens in sorted(grupos.items(), key=lambda kv: (kv[0] != 'guia de cidade', -len(kv[1]))):
        li = ''.join(f'<li><a href="{e(x["url"] + UTM)}">{e(x["titulo"] or x["url"])}</a>'
                     f'{" <span class=c>(" + br(len(x["consultas"])) + (" consulta)" if len(x["consultas"]) == 1 else " consultas)") + "</span>" if x["consultas"] else ""}</li>' for x in itens)
        blocos.append(f'<h2>{e(tipo[0].upper() + tipo[1:])} <span class="c">({br(len(itens))})</span></h2><ul>{li}</ul>')
    corpo = (f'<div class="ey">Dados abertos · Hath Data</div><h1>Mapa do hathdata.com, <span>página por página.</span></h1>{nav(e)}'
             f'<p class="lead">As {br(pg["total"])} páginas públicas do site, agrupadas por tipo, com as consultas que cada uma atende. '
             f'O mesmo conteúdo em <a href="{SITE}/dados/abertos/paginas.json">paginas.json</a>. Atualizado em {e(pg["geradoEm"])}.</p>{"".join(blocos)}')
    return casca('Mapa do hathdata.com: todas as páginas', f'As {pg["total"]} páginas públicas do hathdata.com, por tipo.', PAGES + 'paginas.html', corpo)


def catalogo_md(c):
    partes = [f'# Catálogo completo de consultas\n\n{br(c["total"])} consultas a órgãos oficiais pelo CNPJ ou pela inscrição da empresa, '
              f'por esfera e órgão. Atualizado em {c["geradoEm"]}. Fonte: [hathdata.com/consultas]({SITE}/consultas). '
              f'Com busca e filtro: [página do catálogo]({PAGES}consultas.html).\n']
    por = {}
    for x in c['consultas']:
        por.setdefault(x['esfera'], {}).setdefault(x['orgao'], []).append(x)
    for esf in sorted(por, key=lambda k: -sum(len(v) for v in por[k].values())):
        partes.append(f'\n## {ESFERAS.get(esf, esf)} ({br(sum(len(v) for v in por[esf].values()))})\n')
        for org in sorted(por[esf]):
            partes.append(f'\n### {org}\n\n| Consulta | UF | Entrada | Situação |\n| --- | --- | --- | --- |')
            for x in sorted(por[esf][org], key=lambda x: x['nome']):
                nome = f'[{x["nome"]}]({x["pagina"]})' if x['pagina'] else x['nome']
                partes.append(f'| {nome.replace("|", "/")} | {", ".join(x["ufs"]) or "BR"} | {", ".join(x["entrada"])} | {x["situacao"]} |')
    return '\n'.join(partes) + '\n'


def main():
    if '--local' not in sys.argv:
        baixar()
    c, p, f, pg = ler('consultas.json'), ler('prefeituras.json'), ler('fontes-oficiais.json'), ler('paginas.json')
    (RAIZ / 'README.md').write_text(readme(c, p, f, pg), encoding='utf-8')
    (RAIZ / 'CATALOGO.md').write_text(catalogo_md(c), encoding='utf-8')
    (RAIZ / 'docs' / 'index.html').write_text(pagina(c, p, f), encoding='utf-8')
    (RAIZ / 'docs' / 'consultas.html').write_text(pagina_consultas(c), encoding='utf-8')
    (RAIZ / 'docs' / 'paginas.html').write_text(pagina_mapa(pg), encoding='utf-8')
    print(f"ok: {c['total']} consultas, {p['total']} prefeituras, {f['total']} fontes, {pg['total']} páginas ({c['geradoEm']})")


if __name__ == '__main__':
    main()
