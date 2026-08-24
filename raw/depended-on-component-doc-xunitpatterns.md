# Depended-On Component (DOC)

> Tradução para português do verbete de glossário **"depended-on component (DOC)"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/DOC.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Uma classe individual ou um componente de granularidade grossa do qual o **sistema sob teste (SUT — system under test)** depende. A dependência costuma ser de delegação via chamadas de método. Em automação de testes, o DOC é de interesse principalmente porque precisamos ser capazes de examinar e controlar suas interações com o SUT para obter cobertura de teste completa.

## Termos relacionados

- **SUT** (system under test) — o sistema sob teste; nunca é o que se substitui por um double.
- **Test Double** — padrão usado para substituir o DOC real por um "equivalente específico para teste" quando examinar/controlar a interação real não é viável.
- **indirect input** — valor que o SUT recebe de um DOC.
- **indirect output** — chamada ou efeito que o SUT dispara sobre um DOC.
