# Consultas oficiais por documento: dados abertos

**Toda consulta online, automatizada.**

Lista aberta das consultas que a [Hath Data](https://hathdata.com) faz em órgãos oficiais pelo documento da
empresa: certidões, situação cadastral, processos e listas oficiais. Cada prefeitura vem com a guia da cidade e as
páginas oficiais (gov.br, jus.br, leg.br) que sustentam cada regra.

[Página com busca e filtro](https://hathdata.github.io/consultas-oficiais/) · [Catálogo no site](https://hathdata.com/consultas) · [Guias por cidade](https://hathdata.com/guias)

| Arquivo | O que tem | Registros |
| --- | --- | --- |
| [`dados/consultas.json`](dados/consultas.json) | consulta, órgão, esfera, UFs, dado de entrada, situação e página | 1.067 |
| [`dados/prefeituras.json`](dados/prefeituras.json) | cidade, UF, documentos, guia, página de API e fontes oficiais | 123 (79 em produção, 21 estados) |
| [`dados/fontes-oficiais.json`](dados/fontes-oficiais.json) | página oficial citada e as guias que a citam | 997 |
| [`dados/paginas.json`](dados/paginas.json) | todas as páginas públicas do hathdata.com: título, tipo, data e consultas atendidas | 1.061 |

**Catálogo completo**, por esfera e órgão, com link para cada consulta: [`CATALOGO.md`](CATALOGO.md) e
[página com filtro](https://hathdata.github.io/consultas-oficiais/consultas.html). **Mapa do site**, página por página: [https://hathdata.github.io/consultas-oficiais/paginas.html](https://hathdata.github.io/consultas-oficiais/paginas.html).

Atualizado em 17/11/2026, todo dia, a partir de `https://hathdata.com/dados/abertos/`.

## Consultas por esfera

| Esfera | Consultas |
| --- | --- |
| Judiciário | 569 |
| Municipal | 226 |
| Federal | 155 |
| Estadual | 110 |
| Internacional | 7 |

## Páginas do site por tipo

| Tipo | Páginas |
| --- | --- |
| Consulta por órgão | 371 |
| Consulta: comarca do TJMG | 298 |
| Guia de cidade | 102 |
| Guia e página de produto | 98 |
| API de CND por cidade | 79 |
| CND estadual | 27 |
| Artigo | 25 |
| Integração RD Station CRM | 22 |
| Catálogo de consultas | 20 |
| Solução por público | 11 |
| Integração Omie | 7 |
| Home | 1 |

## Prefeituras em produção

A certidão municipal não tem regra nacional: cada prefeitura define o portal, a validade e o que pede. A guia de
cada cidade traz o passo a passo e a norma, com link para a fonte oficial.

| Cidade | UF | Documentos | Guia |
| --- | --- | --- | --- |
| Manaus | AM | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-manaus) |
| Feira de Santana | BA | Certidão Negativa de Débitos (empresa); Validação da Certidão de Débitos; Comprovante de Inscrição | [guia](https://hathdata.com/certidao-negativa-municipal-feira-de-santana) |
| Salvador | BA | Certidão Negativa de Débitos; NFS-e (Nota Fiscal Eletrônica de Serviços) | [guia](https://hathdata.com/certidao-negativa-municipal-salvador) |
| Fortaleza | CE | Certidão Negativa de Débitos; CPOM | [guia](https://hathdata.com/certidao-negativa-municipal-fortaleza) |
| Aracruz | ES | Certidão Negativa de Débitos (CNPJ) | [guia](https://hathdata.com/certidao-negativa-municipal-aracruz) |
| Goiânia | GO | Certidão Negativa de Débitos; Comprovante de Pagamento; Certidão de Baixa de Inscrição Mobiliária | [guia](https://hathdata.com/certidoes-prefeitura-de-goiania) |
| São Luís | MA | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-sao-luis) |
| Belo Horizonte | MG | Certidão Negativa de Débitos; Certidão de Quitação de IPTU e Taxas; Certidão de Quitação de ISS | [guia](https://hathdata.com/certidao-negativa-municipal-belo-horizonte) |
| Betim | MG | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-betim) |
| Contagem | MG | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-contagem) |
| Coqueiral | MG | Certidão de Débitos Municipais (CNPJ); Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-coqueiral) |
| Divinópolis | MG | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-divinopolis) |
| Montes Claros | MG | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-montes-claros) |
| Ribeirão das Neves | MG | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-ribeirao-das-neves) |
| Santana da Vargem | MG | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-santana-da-vargem) |
| Santana do Paraíso | MG | Certidão Negativa de Débitos (CNPJ); Certidão Negativa de Débitos (Inscrição Econômica); Alvará de Localização e Funcionamento | [guia](https://hathdata.com/certidao-negativa-municipal-santana-do-paraiso) |
| Três Pontas | MG | Certidão Negativa de Débitos; Autenticidade da CND | [guia](https://hathdata.com/certidao-negativa-municipal-tres-pontas) |
| Uberaba | MG | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-uberaba) |
| Uberlândia | MG | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-uberlandia) |
| Cuiabá | MT | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-cuiaba) |
| Ipiranga do Norte | MT | Certidão Negativa de Débitos (CNPJ); Certidão de Dados do Econômico; Alvará de Funcionamento | [guia](https://hathdata.com/certidao-negativa-municipal-ipiranga-do-norte) |
| Barcarena | PA | Certidão de Débitos de Tributos (CNPJ) | [guia](https://hathdata.com/certidao-negativa-municipal-barcarena) |
| Igarassu | PE | Certidão Negativa Mercantil; Validar Certidão Mercantil; Histórico de Certidões Mercantis | [guia](https://hathdata.com/certidao-negativa-municipal-igarassu) |
| Recife | PE | Certidão Negativa de Débitos; CPOM; NFS-e (Nota Fiscal Eletrônica de Serviços) | [guia](https://hathdata.com/certidoes-prefeitura-do-recife) |
| Cascavel | PR | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-cascavel) |
| Colombo | PR | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-colombo) |
| Curitiba | PR | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-curitiba) |
| Foz do Iguaçu | PR | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-foz-do-iguacu) |
| Guarapuava | PR | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-guarapuava) |
| Londrina | PR | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-londrina) |
| Maringá | PR | Certidão Negativa de Débitos (Contribuinte); Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-maringa) |
| Paranaguá | PR | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-paranagua) |
| Ponta Grossa | PR | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-ponta-grossa) |
| São José dos Pinhais | PR | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-sao-jose-dos-pinhais) |
| Campos dos Goytacazes | RJ | Certidão Negativa de Débitos (empresa); CND Imobiliária; Certidão de Quitação de ITBI | [guia](https://hathdata.com/certidao-negativa-municipal-campos-dos-goytacazes) |
| Duque de Caxias | RJ | Certidão Negativa de Débitos (CNPJ) | [guia](https://hathdata.com/certidao-negativa-municipal-duque-de-caxias) |
| Rio de Janeiro | RJ | NFS-e (Nota Fiscal Eletrônica de Serviços); Certidão de Situação Fiscal do ISS; Certidão de Dívida Ativa (PGM) | [guia](https://hathdata.com/certidao-negativa-municipal-rio-de-janeiro) |
| Seropédica | RJ | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-seropedica) |
| Natal | RN | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-natal) |
| Caxias do Sul | RS | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-caxias-do-sul) |
| Porto Alegre | RS | Certidão Negativa de Débitos; Comprovante de Inscrição do ISSQN | [guia](https://hathdata.com/certidao-negativa-municipal-porto-alegre) |
| São Leopoldo | RS | Certidão Negativa de Débito Geral; Certidão Negativa do Imóvel; Certidão Negativa de ITBI | [guia](https://hathdata.com/certidao-negativa-municipal-sao-leopoldo) |
| Balneário Camboriú | SC | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-balneario-camboriu) |
| Biguaçu | SC | Certidão Negativa de Débitos; Guias de ISS e Alvará | [guia](https://hathdata.com/certidao-negativa-municipal-biguacu) |
| Blumenau | SC | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-blumenau) |
| Brusque | SC | Certidão Negativa de Débitos; Certidão Negativa de Débitos do Imóvel; Autenticidade de Certidão Negativa | [guia](https://hathdata.com/certidao-negativa-municipal-brusque) |
| Criciúma | SC | Certidão Negativa de Débitos; Validação de Documentos | [guia](https://hathdata.com/certidao-negativa-municipal-criciuma) |
| Florianópolis | SC | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-florianopolis) |
| Garopaba | SC | Guias de ISS e Alvará; Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-garopaba) |
| Gaspar | SC | Certidão Negativa de Débito Geral | [guia](https://hathdata.com/certidao-negativa-municipal-gaspar) |
| Itajaí | SC | Certidão Negativa de Débitos; Consulta Validade CND | [guia](https://hathdata.com/certidao-negativa-municipal-itajai) |
| Itapema | SC | Certidão de Débito | [guia](https://hathdata.com/certidao-negativa-municipal-itapema) |
| Jaraguá do Sul | SC | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-jaragua-do-sul) |
| Joinville | SC | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-joinville) |
| Lages | SC | Certidão Negativa de Débitos; Validação de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-lages) |
| Palhoça | SC | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-palhoca) |
| São Francisco do Sul | SC | Certidão Negativa de Débitos (CNPJ); Autenticidade de Certidão | [guia](https://hathdata.com/certidao-negativa-municipal-sao-francisco-do-sul) |
| São José | SC | Certidão Negativa de Débitos; Guias de ISS e Taxas | [guia](https://hathdata.com/certidao-negativa-municipal-sao-jose) |
| Barueri | SP | Certidão de Débitos ISS/Taxas | [guia](https://hathdata.com/certidao-negativa-municipal-barueri) |
| Campinas | SP | Certidão Negativa de Débitos; CPOM | [guia](https://hathdata.com/certidao-negativa-municipal-campinas) |
| Catanduva | SP | CND por Inscrição Municipal; CND de Imóvel Urbano | [guia](https://hathdata.com/certidao-negativa-municipal-catanduva) |
| Cotia | SP | Certidão de Débitos Mobiliária | [guia](https://hathdata.com/certidao-negativa-municipal-cotia) |
| Franca | SP | Ficha da Situação Cadastral de Empresa; Rol Nominal Mobiliário; Certidão de Valor Venal | [guia](https://hathdata.com/certidao-negativa-municipal-franca) |
| Guarulhos | SP | Certidão Negativa de Débitos; Certidão de Cadastramento Mobiliário | [guia](https://hathdata.com/certidao-negativa-municipal-guarulhos) |
| Itaquaquecetuba | SP | Certidão Negativa da Empresa; Certidão Negativa de Imóvel; Certidão de Valor Venal | [guia](https://hathdata.com/certidao-negativa-municipal-itaquaquecetuba) |
| Itu | SP | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-itu) |
| Jundiaí | SP | Certidão Negativa de Débitos Municipais (CNPJ); Certidão Negativa de Débitos Mobiliários (ISSQN/Alvará/Multa); Certidão de Contribuinte Mobiliário | [guia](https://hathdata.com/certidao-negativa-municipal-jundiai) |
| Osasco | SP | Cadastro Mobiliário de Contribuinte (CMC); Certidão de Não-Inscrição | [guia](https://hathdata.com/certidao-negativa-municipal-osasco) |
| Praia Grande | SP | Certidão de Débitos Mobiliários; Autenticidade das Certidões | [guia](https://hathdata.com/certidao-negativa-municipal-praia-grande) |
| Ribeirão Preto | SP | Certidão de Situação Cadastral; Pesquisa de Certidões; Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-ribeirao-preto) |
| Santana de Parnaíba | SP | Certidão do Cadastro Mobiliário | [guia](https://hathdata.com/certidao-negativa-municipal-santana-de-parnaiba) |
| Santo André | SP | Certidão de Regularidade Fiscal Mobiliária e Imobiliária; Certidão de Débitos Mobiliária | [guia](https://hathdata.com/certidao-negativa-municipal-santo-andre) |
| Santos | SP | Certidão de Inexistência de Firma; Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-santos) |
| Sorocaba | SP | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-sorocaba) |
| Suzano | SP | Certidão de Débito | [guia](https://hathdata.com/certidao-negativa-municipal-suzano) |
| São Bernardo do Campo | SP | Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-sao-bernardo-do-campo) |
| São Caetano do Sul | SP | Certidão Negativa da Empresa; Certidão Negativa de Imóvel; Certidão de Valor Venal | [guia](https://hathdata.com/certidao-negativa-municipal-sao-caetano-do-sul) |
| São Paulo | SP | Dívida Ativa (CCM); AIT; AIT (Últimos 36 meses) | [guia](https://hathdata.com/certidao-negativa-municipal-sao-paulo) |
| Palmas | TO | Certidão de Situação Fiscal; Certidão Negativa de Débitos | [guia](https://hathdata.com/certidao-negativa-municipal-palmas) |

A lista completa, com as cidades sob demanda, está em [`dados/prefeituras.json`](dados/prefeituras.json) e na
[página do projeto](https://hathdata.github.io/consultas-oficiais/).

## Como usar

```bash
curl -s https://hathdata.com/dados/abertos/prefeituras.json | jq '.prefeituras[] | select(.uf == "MG") | .cidade'
```

```python
import pandas as pd, requests
dados = requests.get("https://hathdata.com/dados/abertos/consultas.json").json()
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

> Fonte: Hath Data, Consultas oficiais por documento (https://hathdata.com).

Há um [`CITATION.cff`](CITATION.cff) para gerar a citação pelo próprio GitHub.

## Sobre a Hath Data

A [Hath Data](https://hathdata.com) automatiza consultas em órgãos oficiais e entrega o PDF e os dados no ERP, no CRM ou por API,
com monitoramento. [Consultas](https://hathdata.com/consultas) · [API de CND](https://hathdata.com/api-cnd) ·
[Guias](https://hathdata.com/guias) · [LinkedIn](https://www.linkedin.com/company/hath-data/)
