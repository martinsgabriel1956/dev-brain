# SGBD: Conceitos Fundamentais e Questões de Concurso

## O que é um SGBD

A sigla SGBD (ou "sistemas gerenciadores de bancos de dados") tem a ver com banco de dados. SGBD significa Sistema Gerenciador de Banco de Dados. Na prática, ele representa os programas utilizados para gerenciar a estrutura e as informações dos bancos de dados — está no próprio nome: ele gerencia o banco de dados, principalmente a estrutura e as próprias informações armazenadas ali.

As funções de um SGBD incluem:

- Transformar e apresentar os dados.
- Controlar o acesso de múltiplos usuários (multiusuário).
- Prover interfaces de comunicação para acesso ao banco de dados.

Os programas usados no SGBD também permitem a criação das estruturas de dados, a manutenção desses dados, o gerenciamento das transações efetuadas no banco, e por fim a extração de informações para realização de consultas, relatórios, análises, entre outros.

## Modelo conceitual

O SGBD funciona como um intermediário entre as aplicações e a base de dados. Ele gerencia uma coleção de dados inter-relacionados que estão na base de dados e uma coleção de programas para acesso a esse banco de dados. No meio do caminho entre as aplicações e a base de dados está o SGBD.

Outro termo importante nas provas de concurso é **visão** (view): é o conceito que permite que diferentes usuários compartilhem dados e recursos de processamento.

## SGBDR vs. SGBD NoSQL

Existem duas grandes subdivisões de SGBD:

- **SGBDR** — Sistema Gerenciador de Banco de Dados Relacional.
- **SGBD NoSQL** — Sistema Gerenciador de Banco de Dados não relacional.

### Banco de dados relacional (SGBDR)

É uma maneira intuitiva e direta de representar dados em tabelas. Nos bancos de dados relacionais:

- Cada linha da tabela é um **registro** (também chamado de tupla).
- As colunas da tabela contêm os **atributos** dos dados (também chamados de campos).
- Cada registro geralmente tem um valor para cada atributo.

A base do entendimento dos bancos relacionais é a manutenção de dados através de tabelas relacionadas entre si — por isso "banco de dados relacional": as tabelas se relacionam entre si através de suas linhas (registros) e colunas (atributos).

Exemplo: uma tabela "clientes" é formada por diversos campos (atributos/colunas) e por linhas (registros/tuplas), sendo nesses registros que os dados são de fato armazenados.

### SQL

Nos bancos de dados relacionais existe uma linguagem de consulta muito utilizada: a **linguagem SQL** (Structured Query Language / Linguagem de Consulta Estruturada). É um conjunto de comandos de manipulação de bancos de dados que permite criar, incluir, excluir, modificar e pesquisar informações nas tabelas de um banco relacional.

### Exemplos de SGBDR (relacionais)

- Microsoft SQL Server
- MySQL
- PostgreSQL
- Oracle Database
- Firebird
- Microsoft Access (pacote Office)
- LibreOffice Base (pacote LibreOffice)
- dBase (exemplo antigo)

### SGBD NoSQL (não relacionais)

O termo NoSQL representa um movimento que propõe novas estruturas de bancos de dados não relacionais.

Exemplos de SGBD NoSQL: MongoDB, Redis, Cassandra, Neo4j, Amazon DynamoDB, Apache HBase.

### Modelos de bancos de dados NoSQL

Existem quatro modelos principais de bancos de dados NoSQL:

1. **Orientado a chave-valor** — exemplos: DynamoDB, Redis, Riak, Memcached, Berkeley DB, LevelDB.
2. **Orientado a documentos** — exemplos: MongoDB (o mais proeminente), CouchBase, CouchDB, MarkLogic, RavenDB.
3. **Orientado a colunas** — exemplos: Cassandra, HBase, Hypertable.
4. **Orientado a grafos** — exemplos: AllegroGraph, ArangoDB, InfoGrid, Neo4j (destaque, muito utilizado atualmente), OrientDB/FlockDB, HyperGraphDB.

## Propriedades ACID (bancos relacionais)

Nos bancos de dados relacionais existe uma preocupação com as propriedades básicas da transação, conhecidas pela sigla **ACID**: Atomicidade, Consistência, Isolamento e Durabilidade.

- **Atomicidade**: a transação deve ter todas as suas operações executadas em caso de sucesso; em caso de falha, nenhum resultado das operações deve refletir sobre o banco de dados. Se ocorrer erro em uma transação, todo o conjunto de ações relacionado é desfeito até o retorno ao estado inicial, como se a transação nunca tivesse sido executada.
- **Consistência**: respeitar as regras de integridade dos dados. A execução de uma transação leva o banco de um estado consistente para outro estado consistente, mantendo sua integridade.
- **Isolamento**: evita que transações paralelas (concorrentes/simultâneas) interfiram umas nas outras — as operações parciais de uma transação não afetam as demais transações em execução.
- **Durabilidade**: persistência dos efeitos de uma transação em caso de sucesso, mesmo diante de quedas de energia, erros ou travamentos.

## Teorema CAP (bancos NoSQL)

O Teorema CAP foi proposto no ano 2000 pelo pesquisador Eric Brewer. Consiste em um conjunto de requisitos para sistemas distribuídos, tipicamente NoSQL:

- **C — Consistência (Consistency)**: todos os nós do sistema devem conter os mesmos dados, garantindo que diferentes usuários terão a mesma visão do estado dos dados — ou seja, todos os servidores de um cluster terão cópias consistentes dos dados. (Não tem o mesmo significado da consistência do ACID, que trata da não violação de regras do banco.)
- **A — Disponibilidade (Availability)**: o sistema deve sempre responder a uma requisição, mesmo que não esteja consistente.
- **P — Tolerância a partição (Partition Tolerance)**: o sistema continuará em operação mesmo que algum servidor do cluster venha a falhar.

Segundo Brewer, é teoricamente impossível que um sistema atenda simultaneamente os três requisitos — só é possível manter dois ao mesmo tempo:

- Um SGBDR e o Neo4j (NoSQL) mantêm **CA** (consistência e disponibilidade), abrindo mão da tolerância a partição.
- MongoDB, BigTable, HBase, Redis e Memcached mantêm **CP** (consistência e tolerância a partição), abrindo mão de parte da disponibilidade.
- CouchDB, DynamoDB, SimpleDB e Cassandra mantêm **AP** (disponibilidade e tolerância a partição), abrindo mão de parte da consistência.

Se for preciso garantir consistência e disponibilidade para uma aplicação, é necessário abrir mão da tolerância a partição — pois não há garantia de alta consistência dos dados se a aplicação precisar estar sempre disponível.

## Questões de concurso sobre SGBD

**Questão 1.** O conjunto de programas responsável pelo gerenciamento de uma base de dados e que, entre outras funções, suporta uma linguagem de consulta, gera relatórios e disponibiliza uma interface para que os seus clientes possam incluir, alterar ou consultar dados é chamado de:
**Gabarito: SGBD** (Sistema Gerenciador de Banco de Dados).

**Questão 2.** Assinale a alternativa que NÃO corresponde a um sistema gerenciador de banco de dados: (a) MySQL; (b) Oracle; (c) Microsoft SQL Server; (d) Firebird; (e) Firefox.
**Gabarito: letra (e) — Firefox**, que é um navegador (browser), não um SGBD.

**Questão 3.** Quais dos sistemas gerenciadores de bancos de dados abaixo constituem SGBDs NoSQL? 1) Oracle Database; 2) MongoDB; 3) Neo4j; 4) MySQL.
**Gabarito: apenas as afirmativas 2 e 3** — Oracle Database e MySQL são SGBDR (relacionais); MongoDB e Neo4j são NoSQL (não relacionais).

## O que as bancas responderam como certo

**CESPE/CEBRASPE** — sobre funções de um SGBD, foi dado como certo: "transformar e apresentar dados, controlar o acesso de multiusuário, prover interfaces de comunicação com o banco de dados".

**CESPE/CEBRASPE** — sobre atomicidade: "conforme o princípio da atomicidade, caso ocorra erro em uma determinada transação, todo o conjunto de ações a ela relacionado será desfeito até o retorno ao estado inicial, como se a transação nunca tivesse sido executada". Dado como certo.

**NC-UFPR** — sobre propriedades ACID: "o isolamento resolve os efeitos decorrentes da execução de transações concorrentes (simultâneas), em que cada transação é executada de forma que as operações parciais das demais transações não afetem as transações atuais". Dado como certo.

**NC-UFPR** — sobre o objetivo principal de um SGBD: "armazenar e recuperar os dados de forma conveniente e eficiente". Dado como certo.

**KIAC** — sobre o conceito de visão: "nos sistemas gerenciadores de bancos de dados (SGBDs), o conceito que permite que diferentes usuários compartilhem dados e recursos de processamento é conhecido como visão". Dado como certo.

**IBADE do Pará** — sobre a definição de SGBD: "trata-se de um sistema de software de uso geral que facilita o processo de definição, construção, manipulação e compartilhamento de banco de dados". Dado como certo.

**Instituto AOCP** — sobre SGBDs NoSQL e seus modelos estruturais, foi dado como certo o pareamento: Cassandra → orientado a colunas; Neo4j → orientado a grafos; MongoDB → orientado a documentos; Redis → orientado a chave-valor.
