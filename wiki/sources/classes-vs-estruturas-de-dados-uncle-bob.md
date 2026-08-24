---
type: source
title: "Classes vs. Estruturas de Dados (Uncle Bob, post original)"
aliases: ["classes vs data structures", "objects and data structures uncle bob", "classes versus data structures blog post"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_count: 0
tags: [clean-architecture, uncle-bob, data-structure, orm, dto, dependency-inversion, polimorfismo, expression-problem, arquitetura]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/classes-vs-estruturas-de-dados-uncle-bob.md
source_url: "https://blog.cleancoder.com/uncle-bob/2019/06/16/ObjectsAndDataStructures.html"
author: "Robert C. Martin (Uncle Bob)"
date_published: "2019-06-16"
date_ingested: 2026-08-23
---

## TL;DR

Post original do blog Clean Coder de Robert C. Martin, "Classes vs. Data Structures" (16/06/2019), escrito em formato de diálogo socrático. Define **objeto** = conjunto de funções que operam sobre dados implícitos/encapsulados, e **estrutura de dados** = conjunto de dados operados por funções implícitas/externas — como opostos exatos, não isomórficos. A partir daí deriva três oposições concretas entre classes e estruturas de dados: (1) visibilidade (funções explícitas + dados ocultos vs. dados explícitos + funções ocultas); (2) extensibilidade (classes facilitam adicionar tipos, dificultam adicionar funções; estruturas de dados fazem o oposto — problema hoje conhecido como *Expression Problem*); (3) direção da dependência de código-fonte (estruturas de dados com switch expõem quem chama a recompilação em cascata; classes com polimorfismo invertem essa dependência — Dependency Inversion). Esta fonte é o post primário citado, mas nunca lido diretamente, por [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — resolve as duas notas de verificação em aberto naquela fonte (título exato, URL, autoria).

## Key Claims

- **Objeto = conjunto de funções que operam sobre elementos de dados implícitos/encapsulados. Estrutura de dados = conjunto de elementos de dados operados por funções implícitas.** As duas definições são apresentadas como complementos exatos uma da outra — "encaixam como mão e luva". [confiança: fonte primária, citação direta]
- **DTOs e tabelas de banco de dados são estruturas de dados, não objetos.** Consequência direta: não existe "mapeamento" entre tabela e objeto, só **transferência de dados** — daí a crítica de que o nome *Object-Relational Mapper* é equivocado, já que não há objeto do lado relacional. Já registrado em [[wiki/concepts/objeto-vs-estrutura-de-dados]] a partir de uma fonte secundária (transcrição de vídeo); esta fonte confirma a formulação original.
- **Schema de banco de dados e modelo de objetos são moldados por forças diferentes.** O schema é um compromisso entre todas as aplicações que usam o banco; o modelo de objetos de cada aplicação é ajustado ao comportamento daquela aplicação específica. Isso é chamado historicamente de "impedância objeto-relacional" — mas Martin argumenta que não é bem uma "impedância", porque objeto e estrutura de dados não deveriam ser vistos como isomórficos (equivalentes) para começo de conversa.
- **Trade-off de extensibilidade (Expression Problem):** com um conjunto de classes polimórficas (ex.: `Square`, `Circle`, cada uma com sua própria implementação de `area`/`perimeter`), adicionar um **novo tipo** (`Triangle`) é fácil — só cria a nova classe — mas adicionar uma **nova função** (`center`) é difícil — precisa mudar toda classe existente. Com uma união discriminada (struct com type-code + funções com `switch`/`case` por tipo), o trade-off se inverte: adicionar uma nova função é fácil (só adiciona a função, com um caso a mais no switch de cada uma), mas adicionar um novo tipo é difícil (precisa editar o switch de cada função existente).
- **Direção da dependência de código-fonte também se inverte entre os dois modelos.** No modelo de união discriminada, o arquivo com o `switch` importa/depende de todas as implementações (`circleArea`, `squareArea`, `triangleArea`), e quem chama a função depende desse arquivo com o switch — logo uma mudança em qualquer implementação obriga recompilar (e redeployar) o arquivo do switch e todo mundo que o chama, em cascata. No modelo polimórfico, quem chama depende só da interface (`Shape`), e cada implementação (`Square`, `Circle`) também depende da interface — uma mudança numa implementação só exige recompilar/redeployar aquele arquivo específico. Martin nomeia esse segundo padrão de **Dependency Inversion**: os arquivos-fonte da implementação apontam na direção oposta à direção da chamada.
- **Resumo final do post (as três oposições):** (1) classes tornam funções visíveis e dados implícitos, estruturas de dados fazem o oposto; (2) classes facilitam adicionar tipos e dificultam adicionar funções, estruturas de dados fazem o oposto; (3) estruturas de dados expõem quem chama a recompilação/redeploy em cascata, classes isolam quem chama disso via Dependency Inversion.

## Entidades Mencionadas

- [[wiki/entities/uncle-bob]] — autor do post, referenciado indiretamente em [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] sem confirmação de título/URL até esta ingestão

## Conceitos Relacionados

- [[wiki/concepts/objeto-vs-estrutura-de-dados]] — página já existente sobre o mesmo tema (via fonte secundária); esta fonte primária adiciona o exemplo Square/Circle/Triangle e o argumento de direção de dependência que a transcrição de vídeo não cobria
- [[wiki/concepts/dependency-inversion-principle]] — o post usa "Dependency Inversion" no sentido específico de direção de dependência de código-fonte (implementação depende da interface, não o contrário); mesmo princípio, ângulo de explicação diferente (via `switch`/união discriminada vs. via injeção de dependência)
- [[wiki/concepts/expression-problem]] — página nova criada a partir desta fonte: o nome formal (na literatura de linguagens de programação) do trade-off "fácil adicionar tipo vs. fácil adicionar operação" que o post descreve sem nomear
- [[wiki/concepts/clean-architecture]] — este post é a base teórica citada (sem link direto) pelo diagrama de aplicação web já documentado nessa página
- [[wiki/concepts/mapper-pattern]] — a crítica ao nome ORM se conecta ao papel real do Data Mapper (transferência, não mapeamento)
- [[wiki/concepts/polimorfismo]] — mecanismo central do lado "objeto" da comparação (polimorfismo dinâmico vs. switch/union discriminada)
- [[wiki/concepts/acoplamento]] — a análise de direção de dependência de arquivo-fonte é uma instância concreta de acoplamento aferente/eferente

## Contradições e Tensões com a Wiki

Nenhuma contradição com o conteúdo já registrado. Esta fonte **resolve** as duas notas de verificação abertas em [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]]: o post existe em `blog.cleancoder.com`, se chama "Classes vs. Data Structures" (não "Objects and Data Structures" — esse é só o slug da URL), foi publicado em 16/06/2019, e a atribuição a Robert C. Martin está confirmada como correta. O conteúdo da transcrição de vídeo (definições de objeto/estrutura de dados, crítica ao ORM) é fiel ao post original — não há distorção. O post original vai além do que a transcrição cobria: adiciona o exemplo de formas geométricas com union discriminada, a formulação do trade-off de extensibilidade, e o argumento de direção de dependência/recompilação, nenhum dos quais aparecia na fonte secundária.

## Quotes Brutas Preservadas

> "An Object is a set of functions that operate upon implied data elements. A Data Structure is a set of data elements operated upon by implied functions."

> "There is no such thing as an Object Relational Mapper; because there is no mapping between database tables and objects... They transfer data between data structures."

> "Adding new functions to a set of classes is hard, you have to change each class. Adding new functions to a set of data structures is easy... Adding new types to a set of classes is easy... Adding new types to a set of data structures is hard, you have to change each function."

> "Data Structures expose callers to recompilation and redeployment. Classes isolate callers from recompilation and redeployment."

## Open Questions

Nenhuma. Esta ingestão fecha as duas questões em aberto que [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] havia registrado sobre este mesmo post.
