---
type: source
title: "Objetos vs. Estruturas de Dados na Clean Architecture"
aliases: ["objetos vs estruturas de dados", "classes versus data structures uncle bob", "data structure clean architecture"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 0
tags: [clean-architecture, uncle-bob, data-structure, orm, dto, view-model, presenter, use-case, dependency-inversion, arquitetura]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/objetos-vs-estruturas-de-dados-clean-architecture.md
source_url: ""
author: "Não identificado no áudio — canal brasileiro de arquitetura de software/Clean Architecture (estilo e temática compatíveis com conteúdo educacional sobre Clean Architecture em português, mas atribuição não confirmada na transcrição)"
date_published: ""
date_ingested: 2026-07-24
---

## TL;DR

A distinção mais fundamental da Clean Architecture entre **objetos** (comportamento explícito, dados implícitos/encapsulados) e **estruturas de dados** (dados explícitos/públicos, funções implícitas/externas), a partir de um post do blog do Uncle Bob. Duas implicações práticas: (1) não existe mapeamento direto entre objetos e relações de banco de dados — só transferência de dados, o que torna o nome "Object-Relational Mapper" enganoso; (2) no diagrama de cenário típico de aplicação web do livro *Clean Architecture*, as caixas marcadas "DS" (Input Data, Output Data, ViewModel) são estruturas de dados puras usadas só para transportar dados entre camadas, enquanto Controller, Use Case, Entities e Presenter são objetos com comportamento, conectados por interfaces (Input/Output Boundary, Data Access) que fazem inversão de dependência.

## Key Claims

- **Objeto = conjunto de funções que operam sobre elementos de dados implícitos.** Dados encapsulados/privados, métodos públicos e explícitos. [confiança: atribuído por Uncle Bob a um post do próprio blog, conteúdo consistente com a literatura de Clean Code/Clean Architecture]
- **Estrutura de dados = conjunto de elementos de dados que são operados por funções implícitas.** Campos públicos/visíveis, funções que operam sobre eles ficam externas à estrutura (ex.: uma `struct` em C). Definição apresentada como o oposto exato da definição de objeto.
- **Não há mapeamento direto entre objetos e relações de banco de dados.** Tabelas contêm apenas dados estruturados (sem comportamento); um objeto contém dados **e** comportamento. O que existe entre banco e objeto é **transferência de dados**, não mapeamento — daí a sugestão (atribuída a Uncle Bob) de que "Object-Relational Mapper" é um nome equivocado; algo como "Relational Datastructure Mapper" seria mais preciso.
- **No diagrama de cenário típico de aplicação web (livro *Clean Architecture*), certas caixas são marcadas "DS"** (Data Structure) — Input Data, Output Data e ViewModel — indicando dados puros sem comportamento, usados só para atravessar camadas.
- **Fluxo completo descrito:** Web Server → Controller empacota Input Data (DS) → Input Boundary (interface/protocolo, inversão de dependência) → Use Case (objeto) orquestra Entities (objeto, comportamento de domínio) → Data Access interface + Data Mapper trazem dados do banco para as Entities → Use Case monta Output Data (DS, pode conter tipos de domínio como `Date` ou Value Objects de dinheiro) → Output Boundary (interface) → Presenter (objeto) reempacota em ViewModel (DS, só strings e flags) → View apenas despeja o ViewModel no HTML.
- **Interfaces de fronteira (Input Boundary, Output Boundary, Data Access) existem para inversão de dependência via polimorfismo** — o Use Case não depende do Controller nem do Presenter diretamente, ambos os lados dependem da mesma abstração. O vídeo usa o termo "protocolo" como sinônimo dessas interfaces.
- **View Model é sempre mais simples que Output Data.** Output Data pode carregar tipos de domínio (datas, Value Objects de dinheiro); o Presenter achata tudo isso em strings/flags simples antes de entregar à View — a View não deveria precisar formatar nada.

## Entidades Mencionadas

- [[wiki/entities/uncle-bob]] — autor do post de blog sobre classes vs. estruturas de dados e do livro *Clean Architecture*, fonte do diagrama de cenário web analisado

## Conceitos Relacionados

- [[wiki/concepts/clean-architecture]] — página nova, criada a partir desta fonte (hub central, antes só referenciado como link quebrado a partir de [[wiki/sources/presenters]])
- [[wiki/concepts/objeto-vs-estrutura-de-dados]] — página nova, o conceito central desta fonte
- [[wiki/concepts/mapper-pattern]] — a crítica ao nome "ORM" se conecta diretamente ao papel do Data Mapper já documentado
- [[wiki/concepts/repository-pattern]] — Data Access interface + Data Mapper é uma instância do mesmo padrão
- [[wiki/concepts/hexagonal-architecture]] — mesma regra de dependências apontando para dentro, vocabulário de Ports & Adapters equivalente a Input/Output Boundary
- [[wiki/concepts/adapter-pattern]] — interfaces de fronteira como mecanismo de inversão de dependência
- [[wiki/concepts/arquitetura-de-software]] — este vídeo é uma explicação concreta e detalhada de um dos livros já citados nessa página (*Clean Architecture*, Robert Martin)
- [[wiki/concepts/ddd]] — Value Objects mencionados como exemplo de tipo de domínio que aparece no Output Data e é achatado no ViewModel

## Contradições e Tensões com a Wiki

Nenhuma contradição encontrada. O conteúdo é altamente convergente com o que já está documentado: [[wiki/concepts/mapper-pattern]] já registra que "mapper é acoplado à camada/tecnologia, não ao domínio" e que a entidade de domínio permanece intocada ao trocar de ORM — esta fonte fornece a justificativa teórica de **por que** isso é assim (objetos ≠ estruturas de dados, logo não há mapeamento direto, só transferência). [[wiki/sources/presenters]] já descrevia o papel do Presenter/ViewModel do lado HTTP; esta fonte generaliza o mesmo padrão para o fluxo completo da Clean Architecture, incluindo o lado de entrada (Controller/Input Data) e persistência (Data Mapper), e fecha o link quebrado `[[concepts/clean-architecture]]` que essa fonte já citava sem a página existir.

## Quotes Brutas Preservadas

> "Objetos são um conjunto de funções que operam sobre elementos de dados implícitos, e a estrutura de dados é o oposto: um conjunto de elementos de dados que são operados por funções implícitas."

> "Não há mapeamento direto entre um objeto e uma relação do banco de dados... o que pode haver é uma transferência de dados."

> "As linhas de uma tabela no banco de dados não são nada mais do que dados estruturados — não há comportamento dentro do banco de dados."

> "A View fica bem simples, ela não faz quase nada, ela simplesmente joga os dados do ViewModel para uma página HTML."

## Open Questions

- **Autoria não confirmada.** A transcrição não menciona o nome do apresentador nem cita a URL exata do post do blog de Uncle Bob referenciado (só descreve o formato de diálogo do post). Não foi possível verificar o título exato do post nem confirmar a atribuição direta a Robert C. Martin a partir do áudio.
- **Nome exato do post do blog do Uncle Bob** não foi capturado com clareza na transcrição (áudio sugere algo como "Classes versus [Data Structures]"). Vale confirmar contra o blog real de Uncle Bob (`blog.cleancoder.com`) se for necessário citar como fonte primária.
