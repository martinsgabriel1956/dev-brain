Bom, pessoal, confesso que eu relutei bastante para fazer esse vídeo aqui, mas é algo que todo mundo me pergunta: como ler a documentação de uma determinada linguagem. E por que que eu relutei em fazer? Porque hoje em dia o pessoal tá usando muito inteligência artificial, então tu tem um retorno muito mais rápido utilizando ela. Mas a documentação não deixa de ser importante, assim como eu aprendi há muito tempo atrás a ler uma documentação bem escrita e bem feita. Eu quero mostrar isso aqui para vocês.

Mas antes eu quero falar do seguinte: as melhores documentações que vocês vão encontrar de qualquer linguagem de programação são feitas em inglês. Não tem jeito. Estudos para prova de certificação, documentações, questões — todas elas, o melhor conteúdo está em inglês. Então, se tu ainda não sabe inglês, domina o seu inglês e impulsione a sua carreira.

Bom, pessoal, antigamente a gente tinha os livros também, né, mas eu vou separar isso aqui em duas partes.

## Parte 1 — Os nomes das sessões (o padrão de toda documentação)

Tu vai ter que aprender os nomes das sessões, porque toda a documentação de qualquer linguagem já possui um padrão. Qual que seria esse padrão?

### Getting Started

A gente tem a sessão de **getting started**. A jogada aqui é que tu nunca pule essa parte. Ela serve para que tu consiga criar o teu primeiro projeto com aquela linguagem. Tu pode digitar a palavra-chave assim: "getting started Spring Boot", por exemplo, no Google, ou então "quick start", ou "quick start guide", ou "installation guide Spring Boot", ou tu pode procurar por "setup Spring Boot" — só que aí ele vai te mostrar mais o que tu precisa para estar utilizando o Spring. Então essas aqui são as palavras-chave. A ideia é que tu nunca pule essa parte do getting started.

### Tutorials

Dentro dos sites de cada linguagem existe uma outra sessão que é o **tutorials**. Aqui tu vai aprender basicamente o passo a passo da linguagem. Um exemplo: quero aprender string, tu vai direto pro tutorial que faz uso de strings.

### API Reference

A segunda etapa aqui, outra palavra-chave: tu vai ter o **API reference**. Ele não é um tutorial, mas é uma referência para tu se basear — que são basicamente as documentações da linguagem.

### Examples

E obviamente toda a linguagem possui os seus exemplos. Então você vai ter uma sessão só de **exemplo** (examples), com exemplos e tutoriais.

## Exemplo prático: documentação do Spring Boot

Quer ver? Eu vou mostrar isso na prática. Se eu pegar aqui e colocar "getting started spring boot" no Google, já aparece o quick start. Eu entro em getting started e já tem "building an [app]" — ele explica como buildar essa aplicação, e tem um código de exemplo: "create a simple web application", mostrando como fazer um Hello Controller, "create an application class", e como usar um command line runner para testar a aplicação.

Toda a documentação está em inglês — às vezes tu vai traduzir e não vai ficar tão bom assim. Eu recomendo que tu não pule isso, porque é importante para entender toda a sintaxe.

Na sessão **Learning**, tem o **Quickstart** (um pouco diferente, é um guia de quickstart): "start a new project", como criar um projeto no Spring Boot, como adicionar código, e um "try it" para rodar o primeiro projeto.

Embaixo, em Learning, você também tem os **Guides** — guias de estudo. Por exemplo, "building a RESTful web services", "consuming RESTful web services". Entrando em "building a RESTful web services", tem tudo: o que tu precisa, como completar o guia, como iniciar, como rodar os serviços ("run the services"). Se eu colocar "rest" no filtro, vêm todos os guias que têm REST. Se colocar outra palavra, vêm os guias daquele assunto.

Tem também os **cursos da própria plataforma**, homologados pela Spring Academy.

Na sessão de **Projects**, também tem tutoriais: Spring Integration, como usar o Spring AI (tutorial bem completo para quem quer se aprofundar em IA), Spring Cloud, Spring Data — o Spring Data JPA, que a gente utiliza muito, mostra um overview, um learning, um suporte e exemplos. Com isso tu consegue programar muita coisa. Tem link pro GitHub com exemplos atualizados (o exemplo que vi era de 5 meses atrás — bem atualizado).

Um exemplo de profundidade da documentação: "various query methods" — como criar uma query (query creation), com os detalhes. Por exemplo, quero fazer uma consulta no banco que faça um `distinct`: dentro da interface do JPA, `findDistinctByLastnameAndFirstname` — ele faz um select com distinct no último nome e no primeiro nome. Isso é ouro na prática.

## Parte 2 — API Reference / JavaDoc (a documentação em si)

A parte dois é estudar pela **API reference** — no caso do Java, o **JavaDoc**. Dá pra digitar "JavaDoc 25" e entrar na página da versão. Lá em cima tem os packages, dá pra navegar por eles ou por todas as classes.

### Exemplo: a classe String

Entrando em String (S-T-R-I-N-G), carrega a classe. Ela herda de Object/Serializable — ou seja, dá pra enviar um dado de um front pra um back-end e deserializar esse objeto numa boa. Ela implementa Comparable. Tem um tutorialzinho de como usar (tudo em inglês — a tradução às vezes também não fica tão boa).

Embaixo tem os **construtores** da linguagem. Um construtor pode estar marcado como *deprecated* — ou seja, existe um construtor melhor em outra versão. Cada construtor tem sua descrição, por exemplo: "initializes a newly created String object so that it represents an empty character sequence" — cria uma variável do tipo String com uma sequência vazia.

Embaixo tem os **methods**, os métodos que dá pra usar dentro de uma String:

- `charAt` — retorna um `char`, o valor do caractere no índice especificado. Exemplo: pegar o caractere da posição 5 de um nome.
- `contains` — retorna um `boolean`: "returns true if and only if this string contains the specified sequence of char values".
- e assim por diante — a documentação detalha cada método.

### Vendo a documentação dentro da IDE

Essa mesma documentação do JavaDoc aparece dentro da ferramenta de desenvolvimento (IDE) — no caso, uma IDE da JetBrains. Ao criar uma variável `String name = "Mateus Leandro Ferreira"` e passar o mouse em cima, a IDE mostra a documentação inteira.

Se eu uso `name.contains("Leandro")`, ele busca se contém "Leandro" ali dentro. Apertando Ctrl e clicando em `contains`, entra direto na documentação/implementação do método: "returns true if and only if this string contains the specified sequence" — tipo de retorno `boolean`.

Internamente, `contains` usa `indexOf`. Dá pra usar diretamente `indexOf(...) >= 0` no lugar de `contains` — a IDE até sugere isso (em amarelinho, como um "melhor usar contains"), mas mostra que por baixo dos panos é a mesma coisa. Dá pra navegar mais fundo ainda e ver a implementação de `indexOf`, com explicação e código.

### Associando português → inglês

Quero transformar uma string em um vetor de pedaços: eu vou ter, dentro de String, o método `split`. A associação mental é: "quando eu vou transformar uma string em pedaços, eu vou cortar, então vou dar um split." A partir do momento que corto uma string em pedaços, tenho que ter um vetor.

O aprendizado na documentação funciona assim: tu associa a palavra em português para o inglês. "Quero em pedaços" → deve ter algum `split`. "Quero verificar se contém um caractere igual" → `contains`. "Quero verificar o tamanho" → `length`. "Será que tem algum método que me possibilita verificar se um texto é igual a outro?" → `equals`. Entrando em `equals`, dá pra ler a documentação e ver a implementação: "if this object is equal to the other", e assim por diante.

## Vale para qualquer linguagem

Documentação é tranquilo de trabalhar, e o padrão se repete: quero aprender Go, vai ter o "get started" do Go — comece por ele, não pule essa etapa. Quero trabalhar com Angular: "Angular getting started" → "getting started with Angular" → tutoriais para fazer. Toda linguagem é igual: tem as docs, tem tutorials (ex.: "your first Angular project", como fazer um Hello World).

## Fechamento

No meu tempo era só a API reference — a gente não usava tanto a internet, porque a API reference funciona offline (tu baixa o pacote de documentação). Usava-se muito o livro, e quando tinha internet, ia pro Stack Overflow ou pro GitHub. Hoje em dia tem um outro potencializador, que é a inteligência artificial: se tu quer saber como transformar uma string num vetor de strings, tu pode perguntar pro ChatGPT — só que, olhando a documentação, tu tem a possibilidade de entrar e ver como o método se comporta e como o pessoal da área faz isso.

Espero que vocês tenham gostado.
