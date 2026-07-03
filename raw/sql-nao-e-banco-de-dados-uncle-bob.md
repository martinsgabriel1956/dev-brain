# SQL não é Banco de Dados: A Confusão da Galera no Twitter

**Tema:** Diferença entre SQL (linguagem) e banco de dados; a polêmica do tweet do Uncle Bob sobre SQL
**Data de captura:** 2026-07-03

---

## Transcrição

Cara, é impressionante como tem muito dev que acha que SQL e banco de dados é a mesma coisa. Eu fiquei apavorado vendo o Twitter hoje, sério. Deixa eu mostrar para vocês aqui: primeiro eu acho que o [Uncle Bob] postou alguma coisa sobre... whatever, alguma coisa sobre Kelly no front-end, e aí ele falou: "Cara, eu acabei de saber que o Bob é anti-SQL" (risadas aqui). E aí o Bob falou o seguinte:

> SQL nunca foi pensado para ser usado em programas de computador. Era uma linguagem de console para impressão de relatórios. Incorporá-la em programas foi um dos erros mais graves da nossa indústria.

Incorporar SQL em programas foi o maior erro da nossa indústria — e aí o Uncle Bob falou: "Thanks Bob, obrigado Uncle Bob."

E eu achei o mais interessante, vendo mais preciso o reply do Uncle Bob — deixa eu ver se eu consigo acessar só o reply, eu acho que é aqui, né — é que a galera confunde as duas coisas. Tipo: como construir uma API que fala com a base de dados relacional sem SQL? Como fazer isso? A solução é eliminar o SQL dos sistemas inteiramente: *if there is no SQL, você não tem engine de SQL, e aí não vai ter SQL attacks.*

Eu acho que isso aqui é um trecho de algum post que o Uncle Bob fez, mas eu não li esse post. As pessoas perguntando: "O que tu usaria se não fosse o SQL? Então tu odeia/ama ORMs?" Outros falando assim: "Tá, então o quê, só arquivos? Porque tipo, se tu não usa SQL provavelmente tu vai usar só arquivos, né?"

SQL é tudo certo, não errado. E eu quero basicamente aqui explicar — porque eu não sei se alguém lá do Twitter vai ver, mas cara, se algum dia alguém te falar sobre isso, tu vai saber pelo menos explicar para essa pessoa.

## O que é SQL, afinal

Vamos começar pelo mais básico. Isso aqui vai cair na prova, tá, então anota aí: o que é SQL? SQL é uma linguagem — é isso, por isso que termina com "L" (cara, enfim, vocês falam "SQL" ou "sequel"): *Structured Query Language*.

Se dentro do teu código tu usa `SELECT * FROM table users WHERE ...` — não interessa o que tu vai fazer ali de WHERE — cara, se tu faz isso aqui, tu tá basicamente acoplando a tua aplicação ao banco. Isso viola os princípios de design limpo (Clean Code), porque tem a forma correta: a forma correta é basicamente tu abstrair completamente o teu código do banco de dados. Tem o controle versus abstrações, e aí a gente entra em vários rabbit holes de discussão.

## Quais são as alternativas

Tu poderia usar um **ORM** — muito usado, por exemplo, o Doctrine pro PHP ou o Hibernate pro Java. Tem diversos ORMs que tu pode utilizar, que por baixo dos panos vão rodar e criar as queries, os SQLs, tudo que tu precisar executar na tua base de dados relacional.

Mas tem outras formas também. Tu pode usar uma **DSL** (*domain specific language*) — no Kotlin tem várias linguagens que suportam isso: Java, TypeScript, Rust, Kotlin, todas suportam tu criar a tua DSL. Já existem formas de manipular objetos como se tu tivesse interagindo com a tua base de dados. Mas vale dizer que uma DSL, por exemplo, se tu pegar uma do Java como a jOOQ, ela provavelmente é um SQL wrapper — ela faz um wrap do teu SQL. Mesma coisa para um ORM: ele também vai ter internamente SQL. Tu vai escrever de forma declarativa, mas por baixo ele vai rodar um SQL para ti.

## A onda do "backend as a service"

Tem uma onda agora vindo das pessoas falando: "Cara, não faz query, usa aqui o Supabase da vida." Por sinal, a galera do Supabase criou uma publicidade muito bem pensada — o TJ retweetou aqui, ficou muito boa. (Esse vídeo não está sendo patrocinado pela Supabase, mas eu curti demais o que eles fizeram — entrando com quadro branco, foi sinistro. Supabase, justo essa.)

Mas por baixo, continua sendo Postgres. Então mesmo se tu usa algo como *backend as a service* — pode ser também o Firebase — aí a gente entra em outra área, porque o Supabase vai usar por baixo o Postgres, então vai usar SQL. Tu pode chamar uma API, mas por baixo ele vai estar escrevendo SQL também.

Agora o Firebase (Firestore) seria um NoSQL — uma base de dados baseada em documentos, não relacional. Mas toda a discussão desse tweet é sobre base relacional, porque senão é absurdo discutir isso. Então para todo mundo que comentou lá sobre "base NoSQL": vocês estão perdendo totalmente a linha da conversa. A comparação não é sobre NoSQL versus base de dados relacional. Estava se falando da decisão de usar SQL na indústria em sistemas — uma linguagem que foi criada para ser usada no console, para imprimir relatórios. É isso.

Se a gente tá comparando algo que aconteceu lá atrás com SQL, a gente não tá querendo comparar com Firestore ou com MongoDB — é simplesmente idiota fazer isso, para de fazer isso. Não é sobre isso. A discussão é sobre o ato de escrever SQL nos programas. Porque, se não for isso, tu tem várias soluções: Firestore (baseado em documentos), MongoDB (também document-based), Redis, Datomic (que usa Datalog por baixo), Dgraph (que usa GraphQL) — diversas opções.

## O que é uma base de dados, de verdade

Mas o que eu quero falar aqui neste vídeo é voltar um pouco no SQL. Vamos lá: o que é SQL? Que tu acha que é SQL? Porque SQL não é a base de dados, tá, ok, entendemos isso. Então o que é SQL de fato?

Tem duas coisas que tu precisa entender sobre SQL, e para fazer isso nada mais óbvio que usar o exemplo do SQLite — uma base de dados, a melhor base de dados do mundo (SQLite, eu sei que "sqlite" em minúsculo agonia).

**Primeira coisa que uma base de dados deve fazer:** armazenar. Como é que uma base de dados armazena as coisas? Para quem odeia LeetCode — "para que eu vou inverter uma árvore binária" — olha só: uma base de dados vai usar *binary tree*. Também vai usar conceitos de páginas e de WAL (*write-ahead log*), que nada mais é do que logging, escrita de logs. Essa é a primeira coisa que uma base de dados tem que fazer. Se tu for criar uma base de dados, tu pode criar tudo que quiser — uma nova linguagem de programação, uma nova base de dados. Essa é a beleza da nossa área.

**Segunda coisa:** tu ter uma forma de se comunicar. O que seria isso? Tu vai ter que ter um SQL da vida — mas não precisaria ser. Tu vai ter que ter alguma forma de se comunicar, declarativa ou não.

**Depois:** tu vai ter uma forma de fazer um *planner* disso, de como tu vai executar, e então executar. Normalmente, na etapa dois de uma base relacional, a gente usa o nosso querido SQL. Se a gente quer parar de usar SQL — por exemplo, fazer um fork do SQLite — o nome teria que ser renomeado, porque não faria mais sentido chamar de SQLite.

## O desafio de criar seu próprio banco

Tu precisaria criar alguma coisa para interagir com uma B-tree, com documentos, ou qualquer formato de arquivo, ou páginas inteiras em CRUD raw mesmo. Tu teria que implementar uma forma de interagir com os dados — provavelmente em C ou em Rust — para criar esse teu *reader* e *parser* dessa nova coisa que tu vai chamar, que não é SQL.

Qual é o maior desafio se tu for aí e parar o final de semana para fazer isso? Não vai ser acessar os dados — mas basicamente tudo que a gente tem hoje, como *transaction logs*, indexação (indexing), tudo isso tu estaria reinventando.

Uma outra forma que eu achei divertida, que poderia solucionar esse problema, seria simplesmente substituir o *SQL parser* e a VM (*virtual machine*), e aí tu cria o que tu quiser. Tu pode usar uma DSL para isso — inventa aí a tua *domain specific language* do jeito que tu gosta de escrever. Sei lá, daqui a pouco é em português que tu vai escrever: "pesquisar usuários filtrando..." e por aí vai. Se divirta, pode fazer do jeito que tu quiser.

## O ponto principal

O ponto que a gente quer chegar aqui: do que a gente tá falando naquela troca? Eu acho que se tratava simplesmente de tu não escrever SQL direto no teu código. Mas o que isso abre para nós? Na verdade, bota uma luz na superficialidade do conhecimento dos devs que estão no Twitter.

Tem muita coisa aqui que eu lembro da faculdade, muita coisa que eu lembro de quando eu tentei criar minha primeira base de dados — isso nunca fez... eu fortemente recomendo (vamos criar aqui a "rinha de base de dados"). Cara, é entender:

1. **Como as coisas são armazenadas** — falei da B-tree ali, mas tem coisas como um heap, várias estruturas que tu pode usar. Tem um conhecimento de LSM (*Log-Structured Merge-tree*), como se usa um LSM, que é uma outra estrutura de árvore. E para ti que odeia LeetCode: cara vê árvore em todo lugar, mas a questão é que tu acha que é inútil porque tu desconhece como as coisas funcionam por debaixo dos panos.

2. **Como tu vai modelar os teus dados** — aqui a gente entra tipo: vamos ter linhas (rows), documentos, grafos, chave-valor (um puta hash map, é isso que tu vai fazer, key-value). Como tu vai modelar os teus dados.

3. **Como tu vai se comunicar** — como vai ser a tua API. E a API aqui não é a tua requisição HTTP, eu tô falando de uma interface: qual vai ser a tua interface de acesso a esses dados que estão armazenados numa árvore e modelados de tal forma. Aqui entra o SQL, aqui entra uma DSL, e por que não até mesmo um HTTP. Com isso, para te interpretar, tu precisa ter um *query processor*, que vai basicamente interpretar o que tu criou de linguagem de comunicação com os teus dados.

4. **Transactions, indexação e otimização** — tu vai precisar de alguma forma criar as transactions; essa, na verdade, é a parte mais difícil ao substituir isso. Aqui a gente entra nas partes difíceis mesmo: como tu faz a indexação e a otimização. (E olha que eu nem tô falando de coisas como replicação, cache, autenticação e tudo mais.)

## Conclusão

Qual é o meu ponto principal desse vídeo? Simplesmente passar para vocês mais informação, e dizer que vocês têm que se aprofundar um pouco mais. O Twitter é ótimo, tá ligado, mas a gente precisa pegar o que tá sendo discutido lá e aproveitar. Tem muita coisa legal — tem até um blog post aqui, "Bob Tables: SQL is Demon Spawn, and No Self-Respecting Software Developer Should Ever Use It" — talvez seja esse o artigo que ele tava se referindo.

E aí a gente pode fazer comentários como este, que eu achei inteligente:

> "Eu acabei de ler a postagem do blog e não consigo imaginar que não seja satírica. Parece uma piada. Um GraphQL ou um ORM: tudo é uma abstração em cima de SQL, porque qualquer pessoa que estivesse propondo outra coisa estaria basicamente propondo reinventar uma roda que já foi testada e que é perfeita — como o SQLite."

É isso. Não esquece de se hidratar, e uma ótima sexta-feira.

---

## Notas de contexto (para ingestão na wiki)

- **Origem:** transcrição de vídeo/reação a uma thread do Twitter/X envolvendo Robert C. Martin ("Uncle Bob") e uma resposta atribuída a "Bob" sobre o uso de SQL em programas.
- **Temas centrais:** SQL como linguagem vs. banco de dados como sistema de armazenamento; ORMs; DSLs; arquitetura interna de bancos de dados relacionais (B-tree, WAL, query planner, parser, VM); comparação indevida entre SQL e NoSQL na discussão original; Supabase (backend-as-a-service sobre Postgres) vs. Firebase/Firestore (NoSQL documental).
- **Menções de produtos/tecnologias:** SQLite, Postgres, Supabase, Firebase/Firestore, MongoDB, Doctrine (PHP ORM), Hibernate (Java ORM), jOOQ (Java SQL DSL/wrapper), Datomic (Datalog), Dgraph (GraphQL sobre grafos).
- **Possível fonte do artigo citado:** "Bob Tables: SQL is Demon Spawn, and No Self-Respecting Software Developer Should Ever Use It" (blog post, não lido/confirmado pelo autor da transcrição).
