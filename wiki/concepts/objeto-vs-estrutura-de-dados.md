---
type: concept
title: "Objeto vs. Estrutura de Dados"
aliases: ["object vs data structure", "objetos e estruturas de dados", "data structure antithesis"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_count: 1
tags: [clean-architecture, uncle-bob, oop, encapsulamento, dto, orm]
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

## Relação com outros conceitos

- [[wiki/concepts/clean-architecture]] — onde a distinção é aplicada concretamente camada a camada
- [[wiki/concepts/mapper-pattern]] — o padrão que implementa a "transferência de dados" entre estrutura de dados (banco) e objeto (entidade de domínio)
- [[wiki/concepts/repository-pattern]] — abstrai exatamente essa transferência de dados de/para o banco
- [[wiki/concepts/ddd]] — entidades anêmicas são o sintoma de tratar um objeto como estrutura de dados por engano

## Key Sources

- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — post do blog de Uncle Bob (formato de diálogo) definindo objeto e estrutura de dados como conceitos opostos, e as duas implicações práticas (ORM, diagrama de Clean Architecture web)
