# Injeção de SQL — Aula do Módulo de Segurança

> Transcrição de vídeo em português (aula de um curso, primeira aula do módulo de segurança). Texto corrido sem pontuação, reescrito como Markdown legível preservando o conteúdo e o tom da fala. Sem necessidade de tradução (fonte já em português).

E aí, galerinha, beleza? Aqui a gente tá na primeira aula do módulo de segurança. A gente vai falar sobre Injeção de SQL, o Sr. Jackson. Mas o que que é uma injeção de SQL? Basicamente aquele cara vacilão vai aproveitar da má estruturação do seu banco ou da sua entrada de dados na aplicação, e aí ele vai conseguir manipular os dados e trazer coisas que ele não deveria naquele instante.

Não entendi nada? Também não, por isso que a gente vai explicar de novo.

## O Que É

Vamos supor, vamos dar um exemplo: a gente tem um endpoint que deveria trazer produtos, e essa aplicação usa SQL — aquele tipo de entrada de dados. E aí o cara consegue colocar no filtro um trecho de SQL, e esse trecho vai concatenar com outra parte dessa query. Aí, ao invés de trazer só os produtos que o usuário deveria ver, o banco vai trazer tudo, ou de repente o cara manda um `DROP TABLE` ali — e se o usuário do banco não tem restrição do tipo de operação que pode fazer, isso dá um baita problema.

Basicamente é isso que é SQL Injection, mais ou menos.

## Como Isso É Aplicado na Prática

Como exemplo prático, vamos usar Express (Node.js) e o módulo `pg` (node-postgres) — sem usar nenhum ORM, conexão simples com o banco.

Tenho um endpoint que chama uma função. Ele recebe `name` e `email` via query string. Aí ele faz um `SELECT * FROM users WHERE name = ... AND email = ...` e retorna o resultado.

Já deixei um banco pronto, com uns 4 usuários. Vamos lá testar essa aplicação. Chamei o endpoint passando meu nome e meu e-mail — a aplicação retornou o usuário certinho, porque existe no banco um cara com esse nome e esse e-mail. Show de bola, beleza.

### A Vulnerabilidade

Só que a gente tem uma grande vulnerabilidade aqui. Imagino que, no lugar do nome e do e-mail, eu faça assim: no filtro, ao invés de passar um nome normal, eu passo algo tipo `' OR '1'='1`.

O que acontece? Ele trouxe **todos** os usuários. Por quê? Porque, na hora que ele pega esse valor e concatena com a query, ela fica assim:

```sql
SELECT * FROM users WHERE name = '' OR '1'='1' AND email = '' OR '1'='1'
```

Vamos imprimir isso com um `console.log` da query final pra gente entender exatamente o que aconteceu: ele monta um SQL que diz "traz todos os usuários onde o nome for igual a uma string vazia OU 1 igual a 1" — e isso **sempre** vai ser verdadeiro. Depois ele fez a mesma coisa com o e-mail, que também vira sempre verdadeiro. Como as duas condições são sempre verdadeiras (`OR`), o banco é "ignorante" — ele só executa o que a query pede — e traz todos os usuários.

Olha aí a primeira cagada que a gente tem na nossa aplicação: já existe uma grande vulnerabilidade porque a gente não tá tratando esse input. É difícil evitar isso? Não, é muito fácil. A gente vai ver agora como evitar que isso aconteça.

### Como Corrigir — Parâmetros / Placeholders

A primeira coisa que eu consigo fazer é fazer com que o `pg` receba um segundo parâmetro: um array. A primeira posição vai ser o `name`, a segunda o `email`, e no texto da query eu coloco `$1` e `$2` no lugar dos valores.

Testei de novo com o mesmo ataque (`' OR '1'='1'`) — a aplicação agora retorna nada, porque não existe usuário nenhum com esse nome literal. E se eu tentar voltar do jeito que funcionava antes — passar meu nome e meu e-mail de verdade — funciona certinho, retorna o usuário certo.

O que aconteceu? Basicamente, todo dado que está entrando deve ser **substituído** pelo que eu tô passando no array — o `$1` vira o `name`, o `$2` vira o `email`, e eles são tratados como **valor**, nunca como parte do comando SQL. Aí não existe mais aquele problema de injeção — os atacantes não vão conseguir mais isso.

Esse esquema no `pg` se chama **placeholders**. É muito fácil de aplicar.

### Outro Exemplo — Parâmetro de Rota

Outra dica: vamos supor que, no lugar de passar por query string, eu tenha um endpoint que lista usuários por parâmetro de rota — tipo `/users/:id`. Se eu simplesmente concatenar esse `id` direto na query sem tratar, dá pra fazer o mesmo ataque: no lugar de passar um ID normal, eu passo algo tipo `1 OR 1=1` — e de novo, como `1=1` é sempre verdadeiro, ele traz todos os usuários de novo, dessa vez através de um parâmetro de rota.

A lição se repete: nunca concatenar direto, sempre usar parâmetros/placeholders.

## Camada Adicional — Validação de Schema com Celebrate

Além de sempre parametrizar a query, dá pra colocar outra camada bem legal que trata isso ainda antes: uma biblioteca chamada **Celebrate**.

O Celebrate é basicamente um middleware que fica no meio, entre a entrada de dados da requisição e a resposta. Ele recebe os dados de quem tá fazendo a requisição (front-end ou outro client), verifica quais parâmetros podem entrar e quais tipos são esperados — por exemplo: "esse campo só pode ser esse tipo específico, só pode entrar número, ou só pode ter esse formato". Se vier algo diferente do formato esperado, ele já retorna erro antes mesmo de chegar na lógica da aplicação.

Para usar: importa-se o `celebrate` e as chaves do objeto (`Segments`), junto com o `Joi` — que trabalha junto com o Celebrate e é usado para descrever os schemas de validação.

Uso: coloca-se o middleware `celebrate(...)` entre a rota e o handler. Ele recebe um objeto onde a chave é o segmento que se quer validar (ex: `PARAMS`, para validar parâmetros de rota) e o valor é um schema Joi. No exemplo, testando o parâmetro `id`: `Joi.number()` — ou seja, esse campo tem que ser **obrigatoriamente** um número.

Testando de novo o ataque anterior (`1 OR 1=1`) no parâmetro de rota: agora a validação falha antes de chegar no banco, porque não foi mandado um número — a requisição já é rejeitada. Se eu passar só o número, volta a funcionar normalmente. Perfeito, show de bola.

## Conclusão

Era basicamente isso que eu queria mostrar nessa aula: como evitar SQL Injection. Repetindo — a gente **nunca** deve deixar a query da forma concatenada; sempre substituir por parâmetros/placeholders. Isso funciona com qualquer tecnologia: no Python (`psycopg2` e afins), no Java (JDBC com `PreparedStatement`), em qualquer linguagem/stack — o princípio é o mesmo.

Se você tá usando um ORM, ele nativamente já faz isso — parametriza os valores da mesma forma. Mas em queries mais complexas, às vezes você precisa escrever SQL na mão mesmo usando ORM, e aí tem que tomar muito cuidado pra não cair de novo nessa forma de concatenar texto puro. A ideia central: nunca deixar dessa forma concatenada — sempre usar parâmetros.

Se você gostou dessa dica, deixa um like, compartilha com a galera, comenta o que você já sabe sobre o assunto ou o que gostaria de ver na próxima aula do módulo de segurança. Valeu, até a próxima.
