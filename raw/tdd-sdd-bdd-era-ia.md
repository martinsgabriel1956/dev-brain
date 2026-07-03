# TDD, SDD e BDD na Era da IA

Se você tá querendo hospedar o seu site ou seu SaaS numa VPS ou hospedar um N8N ou OpenClaude, eu tô recomendando a HostGator, que é patrocinadora aqui do canal.

Vamos falar sobre TDD e SDD na era da IA. Chato ter que falar isso todo vídeo, mas qual que é a ideia aqui: ambas são metodologias, digamos assim, são técnicas que você pode usar para desenvolver suas aplicações, e a ideia aqui é a gente usar isso para melhorar a qualidade da nossa aplicação. É um negócio que, surpreendentemente, tem um viés bem comportamental humano aqui, e acho que, mais surpreendentemente ainda, esse viés comportamental humano funciona também com a IA. Vamos explicar aqui qual que é a ideia.

## TDD

Se você vive embaixo de uma pedra e nunca ouviu falar de TDD: é Test Driven Development, desenvolvimento orientado a testes. Tem três etapas no TDD, que é o seguinte:

1. Você vai pensar, conceber na sua cabeça: "eu quero uma função que, sei lá, some dois números" — só dando um exemplo. A primeira coisa que eu vou fazer é escrever um teste que falha.
2. A segunda coisa que eu vou fazer é escrever o mínimo de código pro teste passar.
3. A terceira coisa: refactor — refatorar, melhorar o código mantendo os testes passando.

Essa é a metodologia do TDD.

### Exemplo

Vamos tentar uma função melhor: uma função que concatena strings, `concat_string`, que recebe `s1` e `s2`.

Primeira coisa que eu escrevo dentro dessa função: nada, porque a primeira coisa que eu tenho que escrever é um teste. Então vamos escrever um teste que faz essa função falhar.

Eu estaria no meu ambiente de teste, no meu arquivo de teste, e escreveria algo tipo:

```
concat_string("hello", " word")
assert x == "hello word"
```

Escrevi um teste que falha, porque a minha `concat_string` não faz isso no momento. Agora vamos escrever o mínimo de código possível pro teste passar. Pra fazer isso a gente faria: `s1 + s2` — isso vai funcionar em Python. Fizemos o nosso teste passar.

### O que é importante falar sobre TDD

Isso não é tudo. A gente testou o happy path, mas eu tenho que me perguntar também: qual que é o comportamento quando eu passo, por exemplo, um número inteiro em vez de string? O que eu quero que aconteça — se eu quero que dê algum erro, eu escrevo um teste pra isso e valido que a função retornou um erro.

Nesse caso não consigo ter muita criatividade pra pensar em muitos edge cases, mas a ideia em TDD é você cobrir todos os possíveis casos excepcionais, e ir escrevendo código e refatorando: escreve teste, escreve código, refatora, escreve teste, escreve código, refatora. A ideia do TDD é que você primeiro escreve testes.

## SDD

Basicamente isso — SDD pode ser Spec Driven Development ou Schema Driven Development, um conceito parecido, mas SDD tem muita coisa aqui pra gente desempacotar.

Geralmente em SDD você vai escrever sobre uma boundary, um limite de um serviço. A gente pode imaginar esse limite, por exemplo, sendo uma REST API — a boundary, a membrana entre o seu frontend e o seu backend.

Uma das formas de se fazer Spec Driven Development é: antes desses dois lados começarem a escrever código, a gente escreve uma documentação da API. Você pode começar escrevendo API docs. Se você já trabalhou numa empresa, talvez já tenha feito isso meio sem querer — eu com certeza já fiz, eu não sabia que o nome era Spec Driven Development, mas meio que era, tipo, no início da sprint eu concordava com o frontend: "ó, eu preciso desses parâmetros, eu vou te devolver esse payload aqui" e o front falava "ok, beleza, fechou". Combinamos nesse spec, nesse contrato, e agora cada um desenvolve suas coisas.

Aqui complica um pouco porque eu dei o exemplo da API, que é um dos exemplos, não o único. A gente pode ter esse exemplo também em banco de dados, em eventos e mensagens. Eu consigo argumentar que se você modularizar o seu código, você consegue ter isso quase como uma interface mesmo, uma interface do código. Então quando a gente começa a generalizar demais o conceito de SDD, ele começa a abranger muita coisa — mas vamos tentar fechar ele um pouquinho.

Quando eu falo "olha, nessa empresa nós fazemos SDD, nós fazemos Spec Driven Development", o que é esperado, o que eu vou encontrar nessa empresa? Provavelmente vou encontrar que, no início de fazer um sistema, um pedaço de sistema, a gente vai ter uma OpenAPI spec — uma das coisas que a gente pode encontrar, também chamado de Swagger (eu nunca entendi qual a diferença entre OpenAPI e Swagger, acho que são a mesma coisa; enfim, uso os termos concomitantemente como se fossem a mesma coisa).

Você pode ter também os arquivos de Protobuf — quando você lida com protos e gRPC ou outros tipos de RPC, você tem um arquivo que meio que é um contrato que vai autogerar código em ambos os lados, vai gerar stubs tanto no produtor quanto no consumidor daquilo (se você não entendeu isso, assiste meu vídeo sobre gRPC). Você tem também o GraphQL, em que você pode ter o arquivo do esquema do GraphQL como sendo esse spec.

Geralmente tende a ser algo nessa linha.

## BDD

Uma coisa que eu não falei — eu vou até mudar o título desse vídeo, eu ia falar sobre TDD e SDD, mas vamos pro terceiro agora: BDD, que eu tenho honestamente menos experiência.

BDD é geralmente associado com um ferramental chamado Cucumber ou Gherkin, que é Behavior Driven Development, desenvolvimento orientado a comportamento. Essas ferramentas tentam descrever comportamento a nível de negócio, e a gente vai tentar validar que algo funciona, que algo segue a regra a nível de negócio, baseado numa descrição de comportamento.

Então você vai ter uma descrição tipo:

```
Feature: User registration

Scenario: Registro feito com sucesso
  Dado que eu tô na página de registro
  Quando eu envio um nome e um e-mail válidos
  Então a minha conta deve ser criada corretamente
```

Você tem essas três keywords: Given, When e Then. Isso é uma tentativa de juntar a nossa regra de negócio, e claro, aí você vai escrever uns testes em cima disso. Eu não vou entrar em detalhes porque não tenho prática com isso — se você quiser um vídeo sobre BDD, comenta aí, eu me comprometo a estudar e trazer esse vídeo. Não tenho prática nisso, então tô só levantando que existe, porque lembrei que existe.

A ideia por trás de BDD, e das poucas empresas que eu vi utilizando BDD, é tentar fazer uma ponte, linkar a regra de negócio com o código, e tentar ter um mecanismo para forçar que o código esteja aderente à regra de negócio. É basicamente isso.

## Por que esses conceitos são legais de entender

Primeiro, acho que quase todos os livros que você pega pra ler sobre engenharia de software vão dizer que essas práticas tendem a ser vistas como boas práticas — tendem a ser vistas como um aumento na velocidade e na qualidade do código, porque tende a ter menos regressão, menos retrabalho.

Pensa comigo: dev odeia escrever teste. E a IA também não gosta de escrever teste — se você não pedir, ela provavelmente não vai escrever. Então tanto dev quanto IA têm o mesmo probleminha, que é a gente não gosta de fazer teste. Tem até aqueles memes: os prós de escrever teste, todo mundo diz que é bom, todo mundo diz que poupa tempo, aumenta a confiança do código, a confiabilidade do código, e faz a equipe se mover mais rápido no longo prazo. Quais os contras de escrever testes? Eu não quero.

O SDD também vai nos dar uma velocidade interessante, porque eu tenho certeza que se você trabalhou na área antes de 2024 (depois, tudo foi pro caos, mas enfim) — você com certeza teve a experiência de que você fez algo no backend, a outra pessoa fez algo no frontend, aí você falou "ah, no final a gente encaixa as coisas", e aí você viu que não encaixava, o Lego não encaixou bonitinho — o que poderia ter sido resolvido se houvesse literalmente 3 minutos de comunicação sobre como vai ser a API, qual é o contrato que a gente tá combinando.

## Aplicando isso com IA

Essas são boas práticas, você pode implementá-las, e você pode inclusive obrigar a IA a fazer elas. Olha aqui comigo: quando você estiver no seu projetinho, você pode ter, por exemplo, um arquivo `.md`, um `CLAUDE.md`, um `AGENTS.md`, uma skill — eu não ligo, isso em algum momento vira um prompt explicando como se faz o desenvolvimento, porque hoje em dia você provavelmente vai utilizar um harness, tipo Claude Code, e o Claude Code consegue rodar testes. Então você vai obrigar o Claude Code a fazer TDD.

Isso funciona pra IA? Surpreendentemente, parece que sim. Eu não tenho dados suficientes pra afirmar categoricamente, mas eu consigo dizer que parece que TDD e SDD aumentam a chance da IA fazer algo que funciona e que tá de acordo com a sua intenção. Você obriga a IA a escrever testes que você dá uma olhada por cima, e a escrever um esquema que você vai dar uma olhada por cima — a chance de você pegar os erros antes deles acontecerem, e a chance de você e a IA chegarem num consentimento de "eu acho que a IA realmente entendeu a minha intenção aqui", eu tenho visto que essa chance parece aumentar.

Enfim, você consegue ter um prompt que fala: "olha, a gente faz SDD, você tem que fazer tal coisa; a gente faz TDD, você tem que fazer tal coisa" — você explica pra IA qual é o ferramental a usar, quais as tools ali, tipo qual comando da codebase utilizar pra fazer isso. Aí você pode ter uma skill, enfim, você entendeu a pegada.

E dentro do seu codebase, pras APIs, você pode ter o YAML da OpenAPI ou o Swagger descrevendo os PDFs, descrevendo os esquemas, esse tipo de coisa — escreve os endpoints, os payloads, o esquema esperado. E aí você pode ter, por exemplo, a nossa função de concatenar strings e um teste pra garantir que as strings são concatenadas. Essa sintaxe é específica desse tipo de teste que eu tô utilizando — você pode escolher a ferramenta que quiser pra fazer testes.

Das que eu conheço: você tem o pytest, que era bem popular, Python; também tem um que é unittest, acho que é assim que se escreve. Você tem Jest, que era muito popular, mas parece que o pessoal tem preferido Vitest por algum motivo, eu não sei sinceramente. Ferramenta de teste eu honestamente não me importo muito, é tudo tão parecido que qualquer uma funciona na minha opinião. Essas duas de cima são de Python, essas duas de baixo são de Node — pra mim não faz a menor diferença, pode escolher qualquer uma.

Acho que testes são boa prática, acho que é algo legal de se fazer, e algo legal de forçar a sua IA a fazer também. E lembra de proibir ela de deletar os testes quando eles não passarem, porque aí ela vai fazer isso: ela vai pegar os seus testes, tipo, ela vai implementar uma feature, vai ver que "uau, a minha feature não funcionou", mas "se eu deletar esse teste aqui, aí vai passar" — vai fazer essa, não é muito bacana.

## Fechamento

Ficamos por aqui. Sinto que esse vídeo foi mais simples que o normal, mas enfim, ficamos por aqui. O que você quer que eu evolua desse assunto? Quer ver na prática eu brincando com uma IA mandando ela seguir TDD? Pode ser um vídeo legal.
