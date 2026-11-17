# JavaScript assíncrono: síncrono × assíncrono, exemplos e vantagens

Opa, olá pessoal, sejam bem-vindos para mais uma aula de JavaScript, onde nós vamos conhecer agora alguns conceitos do JavaScript assíncrono. Por que ele é tão importante nesse lance de requisição?

Se você não assistiu a aula de JSON, eu recomendo fortemente você voltar, porque os conceitos que eu apresento lá, muitos deles serão reaproveitados aqui para podermos entender o mundo das requisições de como um front-end comunica com o back-end e etc.

## Síncrono e assíncrono

Então, basicamente, pessoal, para eu explicar para vocês o que é o JavaScript assíncrono, é interessante eu explicar primeiro o que é o JavaScript síncrono. A palavra síncrono vem de sincronia, que denota a ideia de ordem, então é literalmente quando você executa uma tarefa e depois outra tarefa e depois outra tarefa, ou seja, quando termina a primeira, a primeira, eu executo a segunda, quando termina a segunda, eu executo a terceira, então tem uma certa ordem para as tarefas serem executadas.

O assíncrono vem justamente de uma ideia de que quando acontece algum evento, eu faço ele rodar uma outra tarefa de maneira assíncrona dessa ordem, então ela independe dessa ordem para poder acontecer.

E um exemplo disso é, por exemplo, quando eu faço uma requisição e eu quero cadastrar algo dessa requisição no banco de dados, então eu vou lá, faço uma requisição via URL por meio do protocolo HTTP, se você não entender, calma que eu vou explicar nas próximas aulas, e ele me devolve um JSON. Dentro desse JSON, eu posso fazer uma outra tarefa para poder transformar ele em um objeto, quando ele transformar esse objeto, eu pego uma característica específica e, por exemplo, cadastro no banco de dados.

Você viu que foi uma série de tarefas que acontecem de maneira assíncrona, simplesmente quando eu faço uma requisição que não necessariamente está dentro de uma ordem estabelecida dentro do nosso código do JavaScript.

Por isso que eu escrevi aqui, depende das tasks de tarefas que rodam no fundo da aplicação, que o seu JavaScript vai estar rodando o síncrono bonitinho e você pode fazer o assíncrono no fundo, então meio que vai dar essa ideia de processamento paralelo, traz a ideia de processos que são rodados paralelos.

## Exemplos e vantagens

E os exemplos que a gente tem de JavaScript assíncrono que a gente vai utilizar e ver os conceitos nessa parte aqui é, por exemplo, o AJAX, Axios, Promises, o que são promessas, o Fetch, Async, Await, então nós vamos conhecer esses métodos que ilustram o JavaScript assíncrono.

E quais são as vantagens? Carregar seção, por exemplo, sem precisar recarregar a página inteira. Vamos supor que você está lá construindo um e-commerce e você já carregou lá no seu cliente toda a página web e vamos supor que você clica simplesmente para carregar o miolo daquela página, só um produto, para que eu vou clicar e fazer de maneira síncrona para poder carregar todos os itens mais uma vez sendo que eu só quero recarregar uma seção do site, entendeu?

Então isso economiza recursos, é interessante eu trabalhar com o JavaScript assíncrono simplesmente fazendo uma requisição e ainda consegue fazer ele de maneira paralela, então eu consigo otimizar a minha aplicação utilizando o JavaScript assíncrono.

Então eu tenho maior controle de quando iniciar alguma função mediante essas particularidades do JavaScript assíncrono, então nós vamos começar a ver essas propriedades para poder entender nas próximas aulas em conjunto com o JSON, comunicação e tudo mais que é muito interessante da gente estar aprendendo.
