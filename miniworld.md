# Minimundo — Exportacate

## 1. Contextualização

O **Exportacate** é um sistema de gestão para empresas exportadoras de abacate.
Ele acompanha todo o ciclo do produto: desde a colheita na fazenda, passando
pelo controle de qualidade, embalagem e embarque, até o pedido do cliente
importador no exterior e o respectivo pagamento.

A empresa trabalha com uma ou mais **fazendas parceiras**, cada uma organizada
em **pomares** de diferentes variedades de abacate (Hass, Fortuna, Breda etc.).
Periodicamente, cada pomar gera **lotes de colheita**, que são registrados com
data, quantidade colhida e variedade.

Antes de seguir para exportação, todo lote passa por uma **inspeção de
qualidade**, realizada por um inspetor da empresa. A inspeção classifica o
lote (tamanho, grau de maturação, percentual de defeitos) e define se ele é
**aprovado** ou **reprovado** para exportação. Lotes aprovados são organizados
em **embalagens** (caixas ou paletes), que por sua vez são agrupadas em um
**embarque** — um container vinculado a uma transportadora e a uma rota/navio,
com data de saída e data prevista de chegada.

Cada embarque atende a um **pedido** feito por um **cliente importador**
(empresa estrangeira), que especifica quantidade solicitada, preço acordado
e prazo de entrega. Para cada embarque são emitidos **documentos de
exportação** (certificado fitossanitário, invoice, nota fiscal), necessários
para a liberação alfandegária. Ao final do processo, é registrado o
**pagamento** do cliente referente ao pedido, controlando valor, data e
status (pendente, pago, atrasado).

O sistema também controla os **funcionários** envolvidos (inspetores,
responsáveis por embarque) e permite consultar o histórico de todo o processo
de um lote, do pomar até o pagamento do pedido correspondente.

## 2. Entidades

| # | Entidade              | Descrição                                                                 |
|---|------------------------|----------------------------------------------------------------------------|
| 1 | **Fazenda**            | Propriedade rural parceira. Nome, localização, produtor responsável.       |
| 2 | **Pomar**              | Área de cultivo dentro de uma fazenda. Variedade, área em hectares.        |
| 3 | **LoteColheita**       | Colheita registrada de um pomar. Data, quantidade (kg).                    |
| 4 | **InspecaoQualidade**  | Avaliação de um lote. Classificação, % de defeitos, resultado, inspetor.   |
| 5 | **Embalagem**          | Caixa/palete com lotes aprovados. Tipo, peso total.                       |
| 6 | **Embarque**           | Container de exportação. Data de saída, transportadora, status.           |
| 7 | **ClienteImportador**  | Empresa compradora no exterior. Nome, país, contato.                      |
| 8 | **Pedido**             | Solicitação de compra de um cliente. Quantidade, preço, prazo.             |
| 9 | **DocumentoExportacao**| Documento vinculado a um embarque. Tipo, número, data de emissão.         |
| 10| **Pagamento**          | Pagamento referente a um pedido. Valor, data, status.                      |
| 11| **Funcionario**        | Pessoa da empresa (inspetor, responsável de embarque). Nome, cargo.        |

> Mínimo de 8 classes exigido pelo trabalho: atendido (11 entidades).

## 3. Principais relacionamentos

- Uma **Fazenda** possui vários **Pomares** (1:N)
- Um **Pomar** gera vários **LotesColheita** (1:N)
- Um **LoteColheita** recebe uma **InspecaoQualidade** (1:1)
- Um **Funcionario** (inspetor) realiza várias **InspecaoQualidade** (1:N)
- Vários **LotesColheita** aprovados compõem uma **Embalagem** (N:N, via tabela associativa)
- Várias **Embalagens** compõem um **Embarque** (N:1)
- Um **Embarque** atende a um ou mais **Pedidos** (N:N, via tabela associativa)
- Um **Pedido** é feito por um **ClienteImportador** (N:1)
- Um **Embarque** possui vários **DocumentosExportacao** (1:N)
- Um **Pedido** possui um **Pagamento** (1:1)
- Um **Funcionario** é responsável por vários **Embarques** (1:N)
