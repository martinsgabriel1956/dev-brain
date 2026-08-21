# Indirect Input

> Tradução para português do verbete de glossário **"indirect input"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/Indirect%20Input.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Quando o comportamento do **sistema sob teste (SUT — system under test)** é afetado pelos valores retornados por outro componente cujos serviços ele utiliza, chamamos esses valores de **indirect inputs** ("entradas indiretas") do SUT.

*Indirect inputs* podem ser:

- valores de retorno reais de funções;
- parâmetros atualizados (de saída/out) de procedimentos ou subrotinas; e
- quaisquer erros ou exceções levantados pelo **componente do qual se depende (DOC — depended-on component)**.

Testar o comportamento do SUT com *indirect inputs* exige o **ponto de controle** apropriado na "parte de trás" (back side) do SUT. Frequentemente usamos um **Test Stub** para injetar os *indirect inputs* no SUT.

## Termos relacionados

- **SUT** (system under test) — o sistema sob teste.
- **DOC** (depended-on component) — o componente do qual o SUT depende.
- **control point** — ponto de controle usado para manipular o comportamento do SUT durante o teste.
- **Test Stub** — padrão de Test Double usado para fornecer *indirect inputs* controlados ao SUT.
- **direct input** — contraparte de *indirect input*: entradas fornecidas diretamente ao SUT (ex.: parâmetros de chamada).
