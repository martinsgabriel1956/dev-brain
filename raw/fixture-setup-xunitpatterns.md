# Fixture Setup

> Tradução para português do verbete de glossário **"fixture setup"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/fixture%20setup.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Antes que a lógica desejada do **sistema sob teste (SUT — system under test)** possa ser exercitada, as precondições do teste precisam ser configuradas. Coletivamente, todos os objetos (e seu estado) são chamados de **test fixture** (ou **test context**), e a fase do teste que os configura é chamada de **fixture setup**.

## Termos relacionados

- **SUT** (system under test) — o sistema sob teste, cuja lógica só pode ser exercitada após a fixture setup estar completa.
- **test fixture** (ou **test context**) — o conjunto de objetos e seu estado que constitui as precondições do teste; é o que a fixture setup configura.
- **Four-Phase Test** — estrutura de teste em quatro fases (fixture setup, exercise SUT, result verification, fixture teardown) da qual a fixture setup é a primeira fase.
