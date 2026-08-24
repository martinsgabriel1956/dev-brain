---
type: concept
title: "Objeto vs. Estrutura de Dados"
aliases: ["object vs data structure", "objetos e estruturas de dados", "data structure antithesis"]
date_created: 2026-07-24
date_updated: 2026-08-23
source_count: 3
tags: [clean-architecture, uncle-bob, oop, encapsulamento, dto, orm, modelo-de-dominio-anemico, expression-problem, dependency-inversion]
skill: tech-mentor-backend
status: stable
---

# Objeto vs. Estrutura de Dados

Distinção fundamental de Uncle Bob (num post do seu blog, discutido em formato de diálogo) que trata **objeto** e **estrutura de dados** como conceitos opostos, não sobrepostos. A definição de um é literalmente o inverso da definição do outro.

## As duas definições

| | Objeto | Estrutura de Dados |
|---|---|---|
| **Definição** | Conjunto de **funções** que operam sobre elementos de dados **implícitos** | Conjunto de **elementos de dados** que são operados por funções **implícitas** |
| **Dados** | Encapsulados/privados (atributos, membros) | Expostos/públicos (campos) |
| **Funções** | Públicas e explícitas (métodos) — pertencem à própria classe | Externas — não pertencem à estrutura |
| **Exemplo** | Uma classe com getters/setters substituídos por comportamento real | Uma `struct` em C, um objeto JSON simples, um `Record`/`DTO` |

Uma forma simples de fixar: numa `struct`, todos os campos são completamente acessíveis de fora. Num objeto de verdade, os atributos **não** são acessíveis diretamente — o acesso é mediado por métodos que carregam comportamento.

## Por que a distinção importa

Não é purismo terminológico — a distinção tem consequências arquiteturais concretas:

### 1. Não existe mapeamento direto entre objetos e relações de banco de dados

Uma tabela de banco de dados contém **linhas**, e linhas são puramente estrutura de dados — campos sem comportamento. Um objeto contém dados **e** comportamento. Como os dois lados não são equivalentes, o que existe entre eles não é "mapeamento", é **transferência de dados**: você pega os valores que estão na estrutura de dados do banco e os copia para dentro de um objeto, que passa a ter esses valores mais tudo o que já definia como objeto (comportamento).

Essa é a base da crítica ao nome **Object-Relational Mapper (ORM)**: se o lado relacional é estrutura de dados pura, "objeto-relacional" descreve mal o que a ferramenta faz. Um nome mais preciso seria algo como *Relational Datastructure Mapper*. Ver [[wiki/concepts/mapper-pattern]] para o padrão de implementação que resolve esse problema de conversão entre camadas na prática.

### 2. Clean Architecture usa as duas coisas, em lugares diferentes e por razões diferentes

No diagrama de cenário típico de uma aplicação web (ver [[wiki/concepts/clean-architecture]]), estruturas de dados (`Input Data`, `Output Data`, `ViewModel`) são usadas exclusivamente **para transferir dados entre camadas** — não carregam lógica. Objetos (`Entities`, `Use Cases`, `Presenter`) carregam **comportamento e regra de negócio**. Confundir os dois papéis é um dos erros mais comuns em código que tenta seguir Clean Architecture: vazar lógica de negócio para dentro de um DTO/ViewModel, ou, no sentido inverso, tratar uma Entity como se fosse só um bag de dados (entidade anêmica — ver [[wiki/concepts/ddd]]).

## Trade-off de extensibilidade: fácil adicionar tipo vs. fácil adicionar operação

Confirmado pela fonte primária ([[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]], o post original de Uncle Bob, lido na íntegra): a oposição entre objeto e estrutura de dados não é só sobre visibilidade de dados/funções — ela também se manifesta como um trade-off de extensibilidade, hoje conhecido na literatura de linguagens de programação como [[wiki/concepts/expression-problem|Expression Problem]].

Exemplo do post: um conjunto de formas geométricas (`Square`, `Circle`) com operações `area` e `perimeter`.

- **Como objetos** (cada forma é uma classe com [[wiki/concepts/polimorfismo|polimorfismo]] dinâmico): adicionar um novo **tipo** (`Triangle`) é fácil — só cria a classe nova, nada existente muda. Adicionar uma nova **operação** (`center`) é difícil — precisa editar todas as classes existentes.
- **Como estruturas de dados** (união discriminada com type-code + funções com `switch`): o oposto exato. Adicionar uma nova **operação** é fácil — só cria a função nova. Adicionar um novo **tipo** é difícil — precisa editar o `switch` de cada função existente.

Regra prática: se o eixo de mudança esperado é "vou adicionar tipos com frequência", prefira classes; se é "vou adicionar operações com frequência", prefira estruturas de dados.

## Direção da dependência de código-fonte (Dependency Inversion)

Ainda segundo [[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]], existe uma terceira oposição, sobre a direção das dependências entre arquivos-fonte:

- **União discriminada + switch**: o arquivo com o `switch` depende de (importa) cada implementação específica (`circleArea`, `squareArea`, ...), e quem chama a operação depende desse arquivo com o switch. Uma mudança em qualquer implementação obriga recompilar/redeployar o arquivo do switch e, em cascata, todo mundo que o chama.
- **Polimorfismo com interface**: quem chama depende só da interface (`Shape`), e cada implementação também depende dessa mesma interface — não de quem chama. Uma mudança numa implementação exige recompilar/redeployar só aquele arquivo. As dependências apontam na direção **oposta** à direção da chamada.

Esse segundo padrão é o que Martin chama de **Dependency Inversion** neste post — o mesmo nome usado em [[wiki/concepts/dependency-inversion-principle]], mas descrito aqui a partir do ângulo de recompilação/redeploy em vez do ângulo usual de injeção de dependência.

## Relação com outros conceitos

- [[wiki/concepts/clean-architecture]] — onde a distinção é aplicada concretamente camada a camada
- [[wiki/concepts/mapper-pattern]] — o padrão que implementa a "transferência de dados" entre estrutura de dados (banco) e objeto (entidade de domínio)
- [[wiki/concepts/repository-pattern]] — abstrai exatamente essa transferência de dados de/para o banco
- [[wiki/concepts/ddd]] — entidades anêmicas são o sintoma de tratar um objeto como estrutura de dados por engano
- [[wiki/concepts/modelo-de-dominio-anemico]] — o anti-padrão nomeado: dados sem comportamento, um objeto que é na verdade uma estrutura de dados disfarçada
- [[wiki/concepts/encapsulamento]] — a fronteira que transforma uma estrutura de dados (atributos públicos) num objeto de verdade (atributos privados + comportamento que protege invariantes)

## Active Record aplicado a entidades de domínio é incompatível com Clean Architecture

[[wiki/sources/arquitetura-limpa-na-pratica]] leva a crítica ao ORM um passo além: usar o padrão **Active Record** (a entidade conhece como persistir a si mesma) diretamente numa entidade de domínio é descrito como impossível dentro da Clean Architecture, porque a própria definição do padrão mistura código de persistência com regra de negócio do domínio, violando a Regra de Dependência. O autor considera aceitável usar Active Record em estruturas de dados (DTOs) na camada externa, onde não há regra de negócio para proteger.

## Key Sources

- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — transcrição de vídeo sobre o post do blog de Uncle Bob, e as duas implicações práticas (ORM, diagrama de Clean Architecture web)
- [[wiki/sources/classes-vs-estruturas-de-dados-uncle-bob]] — post original do blog de Uncle Bob (fonte primária, lido na íntegra): confirma as definições, e adiciona o trade-off de extensibilidade (Expression Problem) e o argumento de direção de dependência (Dependency Inversion)
- [[wiki/sources/arquitetura-limpa-na-pratica]] — extensão da crítica ao ORM: por que Active Record aplicado a entidades de domínio viola a Regra de Dependência
