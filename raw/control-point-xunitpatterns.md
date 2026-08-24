# Control Point

> Tradução para português do verbete de glossário **"control point"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/control%20point.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Um **control point** (ponto de controle) é a forma como o teste pede ao **sistema sob teste (SUT — system under test)** para fazer algo por ele. Isso pode ser para fins de configurar ou desmontar a fixture (fixture setup/teardown), ou pode ser usado durante a fase de **exercise SUT** do teste. É um tipo de **interaction point** (ponto de interação).

Alguns control points são fornecidos estritamente para os testes; eles não devem ser usados pelo **production code** (código de produção), porque contornam a validação de entrada ou interrompem o ciclo de vida normal do SUT ou de algum objeto do qual ele depende.

## Termos relacionados

- **SUT** (system under test) — o sistema sob teste.
- **interaction point** — categoria mais ampla à qual o control point pertence.
- **exercise SUT** — fase do teste em que o SUT é acionado através de um control point.
- **production code** — código de produção; não deve depender de control points exclusivos de teste, pois eles bypassam validação de entrada e ciclo de vida normal.
