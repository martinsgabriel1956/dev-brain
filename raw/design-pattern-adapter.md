# Padrão de Projeto: Adapter — Renato Augusto

"Trocar todo o nosso código e não faz sentido — isso não é orientação a objetos, isso é programação procedural disfarçada de orientação a objetos."

Fala, pessoal! Renato Augusto aqui. No vídeo de hoje eu vou te mostrar tudo que tu precisa saber sobre o padrão de projeto Adapter e como ele se relaciona com o uso correto de orientação a objetos e também com o uso dos testes unitários. Então tu vai sair daqui programando muito melhor do que quando entrou, e vai sair com conhecimento extremamente avançado.

Antes da gente ir pra tela, eu tenho que deixar um aviso: toda essa nossa saga dos padrões de projeto, que a gente começou no primeiro vídeo do Strategy, é completamente agnóstica de linguagem de programação. Tu vai conseguir implementar tudo que eu ensino aqui na tua linguagem favorita, no teu framework favorito. Não se apegue à linguagem de programação — o conceito aqui é o que manda. Arquitetura é a arte de fazer a coisa certa.

## As duas analogias

**Trilho de trem e carro urbano.** A gente tem um trilho de trem e um carro urbano. A gente até consegue fazer um carro normal de rodovia andar sobre o trilho de um trem, mas não é o correto — é bem inviável. A gente precisa de um adaptador: algo que converta a interface de uso de um carro urbano para o trilho de um trem. Geralmente, quando interfaces de objetos são incompatíveis, a gente usa o Adapter.

**Tomadas (Refactoring Guru).** Imagina que tu tem o teu carregador de notebook, comprado aqui no Brasil, padrão de três pinos. Agora imagina que tu viajou pros Estados Unidos — lá o padrão de tomada é totalmente diferente. Tu não consegue encaixar a tua tomada de três pinos na tomada americana. O que tu precisa é de um adaptador, daqueles que fazem a conversão de três pinos para o padrão americano (ou vice-versa).

Tem gente que, na base da gambiarra, corta o fio, corta o plugue da tomada e deixa só as duas pontas do fio pra enfiar direto na tomada. Funciona, mas é a mesma coisa que pegar o carro e botar pra andar direto no trilho de trem — não vai dar muito certo. É exatamente pra isso que servem os padrões de projeto: a gente tem problemas específicos e soluções específicas. Padrão de projeto não é pra sair implementando feito um doido em tudo quanto é lugar — tem que ter o problema específico pra resolver com aquele padrão catalogado.

## O cenário: gerador de relatório de vendas

Vamos imaginar uma aplicação de vendas que a gente dá manutenção. Nesse módulo de vendas, a gente tem que rodar um script diariamente, responsável por gerar o relatório de vendas daquele dia. Esse script foi agendado no servidor, que se encarrega de rodá-lo todo dia.

O script chama uma classe `SalesReportGenerator` (gerador de relatório de vendas), que tem um método `generate`. Rodando esse código (via Docker, `php command.php`), ele gera o relatório em PDF.

### A classe `SalesReportGenerator`

Essa classe usa uma biblioteca externa de geração de PDF, o **DomPDF** (não é código proprietário). O fluxo dentro do método:

1. Chama `loadHtml()` passando o conteúdo (fictício aqui — na prática viria de uma query no banco, formatada em HTML).
2. Chama `setPaper()` passando o tamanho (A4) e a orientação (`landscape`).
3. Chama `render()`.
4. Monta o nome do arquivo pegando o timestamp atual concatenado com `.pdf`.
5. Chama a função nativa do PHP que cria o arquivo, passando o output do DomPDF e o filename.

### Onde está o problema

A classe `SalesReportGenerator` — uma classe de alto nível, de regra de negócio — está **altamente acoplada** ao DomPDF, uma biblioteca externa de baixo nível (detalhe de infraestrutura).

- Se os mantenedores do DomPDF mudarem a assinatura dos métodos (por exemplo, `render` virar `generate`), a classe de negócio precisa mudar junto. Isso fere o **Single Responsibility Principle (SRP)** do SOLID: a classe tem mais de um motivo para mudar — se o conteúdo do relatório mudar, ou se a forma de chamar o DomPDF mudar.
- Toda vez que se dá um `new` dentro do código, distanciando-se de uma abstração e aproximando-se de uma classe concreta, gera-se acoplamento. Não é preciso eliminar acoplamento 100% (isso não existe), mas o ideal é programar para abstrações/interfaces, não para implementações concretas.
- **Testabilidade:** como testar unitariamente o método `generate` sem chamar de fato o DomPDF? Não tem como mockar ou substituir por uma classe fake, porque a instância concreta (`new DomPdf(...)`) está criada direto dentro do método.

Uma classe de alto nível (que lida com regra de negócio) não pode ficar vinculada e sabendo demais dos detalhes de uma classe de muito baixo nível (como gerar um PDF, quais métodos chamar em qual ordem). Isso não é orientação a objetos — é programação procedural disfarçada de orientação a objetos. É exatamente o exemplo do fio cortado direto na tomada, ou do carro andando direto sobre o trilho do trem: funciona, mas não é o certo.

## Resolvendo com o Adapter

### 1. Criar a interface

Criar uma interface `PdfAdapter` com um método `generate`, que não retorna nada (só salva o arquivo), recebendo uma string `fileName` e uma string `content`.

### 2. Criar o adaptador concreto

Criar uma classe `DomPdfAdapter` que implementa `PdfAdapter`. Dentro do método `generate`, ela envelopa todo o comportamento específico do DomPDF (`loadHtml`, `setPaper`, `render`, `file_put_contents`) que antes estava solto dentro da classe de negócio.

### 3. Modificar a classe de negócio

`SalesReportGenerator` passa a ter um construtor que recebe a interface `PdfAdapter` (programando para abstração, não para implementação concreta) e guarda numa propriedade privada. O método `generate` da classe de negócio passa a apenas montar o `fileName` e o `content`, e delegar para `this->pdfAdapter->generate(fileName, content)`. A classe de negócio não sabe mais qual biblioteca está por trás, nem os detalhes de como o PDF é montado.

### 4. Instanciar no ponto de entrada

No script (`Command`), em vez de a classe de negócio instanciar o DomPDF diretamente, o `Command` instancia `new DomPdfAdapter()` e injeta essa instância no construtor de `SalesReportGenerator`.

A interface `PdfAdapter` funciona como a "tomada": quem tem que se adaptar a ela são as implementações concretas, não a classe de negócio. Se o DomPDF deixar de existir ou de ser mantido, a solução não é reescrever a classe de negócio — é puxar outra biblioteca, criar um novo adaptador que implemente a mesma interface, e trocar apenas a instância injetada no `Command`.

### Trocando de biblioteca sem tocar na regra de negócio

Para provar o ponto, o vídeo demonstra a troca do DomPDF pelo **TCPDF** (outra biblioteca de PDF, com uma interface de uso bem diferente: `writeHTML`, `setFont`, etc., em vez de `loadHtml`/`setPaper`/`render`). Cria-se uma nova classe `TcpdfAdapter implements PdfAdapter`, que encapsula essa API diferente atrás do mesmo contrato `generate(fileName, content)`.

No `Command`, a única mudança necessária é trocar `new DomPdfAdapter()` por `new TcpdfAdapter()`. A classe `SalesReportGenerator` não muda uma linha — rodando o comando de novo, o relatório é gerado normalmente (com um layout ligeiramente diferente, produto da lib diferente por trás).

## Por que isso importa

- Classes de alto nível (regra de negócio) devem depender sempre de abstrações, nunca de implementações concretas — isso as torna estáveis diante de mudanças em bibliotecas externas ou detalhes de infraestrutura.
- Classes de baixo nível e bibliotecas externas é que devem se adaptar ao código de domínio — nunca o contrário.
- Com o Adapter em vigor, o código fica testável: dá pra criar um objeto fake que implementa `PdfAdapter` e passar para o construtor de `SalesReportGenerator`, testando a orquestração sem gerar PDF de verdade.
- Regra prática: toda vez que uma classe de alto nível (regra de negócio) estiver diretamente acoplada, via `new`, a uma classe de muito baixo nível (detalhe de infraestrutura/biblioteca externa), esse é o sinal para aplicar o Adapter.

Padrão de projeto não é para aplicar em tudo indiscriminadamente — é solução catalogada para um problema específico: interfaces incompatíveis entre uma classe de alto nível e uma dependência de baixo nível/externa.
