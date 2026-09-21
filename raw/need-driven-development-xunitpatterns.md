# Need-Driven Development

> Tradução para português do verbete de glossário **"need-driven development"**, do site xUnit Patterns.
> Fonte: http://xunitpatterns.com/need-driven%20development.html
> Autor: Gerard Meszaros | Copyright © 2003-2008
> Categoria original: Glossary
> Tradução feita para fins de estudo.

---

Uma variação do processo de **test-driven development** em que o código é escrito de fora para dentro (*outside in*) e todo o código dependente (*depended-on code*) é substituído por **Mock Objects** que verificam os **indirect outputs** esperados do código sendo escrito. Isso garante que as responsabilidades de cada unidade de software sejam bem compreendidas antes de serem codificadas, por meio da existência tanto de **unit tests** quanto de exemplos de uso real. A camada mais externa do software é escrita usando **storytest-driven development** e também deve ter exemplos de uso por clientes reais (por exemplo, uma interface de usuário acionando a **Service Facade** [CJ2EEP]), além dos **customer tests**.

## Termos relacionados

- **test-driven development** — processo do qual o need-driven development é uma variação.
- **Mock Object** — usado para substituir todo código dependente e verificar indirect outputs.
- **indirect output** — o que os Mock Objects verificam durante o processo.
- **unit test** — parte da evidência de que as responsabilidades de uma unidade são bem compreendidas.
- **storytest-driven development** — processo usado para escrever a camada mais externa do software.
- **Service Facade** — padrão citado como exemplo de interface acionada por clientes reais (referência: CJ2EEP).
- **customer test** — complementa os exemplos de uso real na camada mais externa.
