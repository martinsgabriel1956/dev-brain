---
type: source
title: "Seis Design Patterns Mais Usados na Prática"
aliases: ["6 design patterns mais usados", "seis padroes de design mais usados"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [design-patterns, creational, structural, behavioral, gof, observer, factory, singleton, decorator, strategy, adapter]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/seis-design-patterns-mais-usados-na-pratica.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-06
---

# Seis Design Patterns Mais Usados na Prática

Vídeo do YouTube (autoria não identificada na transcrição) que percorre os seis design patterns mais usados no mundo real, na experiência do autor, cada um introduzido por uma analogia do cotidiano: sino de inscrição do YouTube ([[wiki/concepts/observer-pattern]]), pedido de pizza ([[wiki/concepts/factory-pattern]]), elevador de prédio ([[wiki/concepts/singleton-pattern]]), filtros do Instagram ([[wiki/concepts/decorator-pattern]]), rotas do GPS ([[wiki/concepts/strategy-pattern]]) e adaptador de tomada de viagem ([[wiki/concepts/adapter-pattern]]).

## TL;DR

Seis dos 23 padrões do GoF (1994) cobrem a maioria dos casos reais de uso: [[wiki/concepts/observer-pattern|Observer]] (reagir a mudanças, ex.: `addEventListener`, `EventEmitter`, `useEffect`), [[wiki/concepts/factory-pattern|Factory]] (centralizar criação de objetos variável por contexto, ex.: `document.createElement`, factories de mock no Jest), [[wiki/concepts/singleton-pattern|Singleton]] (instância única, ex.: pool de conexão — com ressalva explícita de anti-pattern), [[wiki/concepts/decorator-pattern|Decorator]] (empilhar comportamento sem alterar o objeto original, ex.: decorators do TypeScript, `@Injectable`, `@Component`), [[wiki/concepts/strategy-pattern|Strategy]] (trocar algoritmo em runtime, ex.: middleware do Express, comparador do `Array.sort`) e [[wiki/concepts/adapter-pattern|Adapter]] (compatibilizar interfaces incompatíveis, ex.: ORMs como Prisma/TypeORM, troca de Axios por `fetch`). Os patterns compõem entre si (factory pode criar singleton; observer pode usar strategy; adapter pode envolver objeto de uma factory) e o alerta final é: não aplicar pattern sem um problema real por trás.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| `useEffect` do React segue o princípio do Observer | "Ele reage quando uma dependência muda" — analogia direta com `addEventListener`/`EventEmitter` | Médio — correta como analogia conceitual (reação a mudança de estado), mas o autor não detalha o mecanismo de dependency array do React |
| Singleton é "meio polêmico" / considerado anti-pattern por parte da comunidade | Justificativa dada: cria estado global, dificulta testes, esconde dependências | Alto — mesma ressalva já registrada em [[wiki/sources/sete-padroes-de-design-de-software]] ("glorified global variable") |
| Frameworks atuais implementam Singleton via container de DI em vez de "na mão" | Exemplo dado: o framework garante instância única sem acoplar o código | Alto — consistente com prática comum (ex.: escopo singleton em NestJS DI) |
| Decorators do TypeScript (`@`) seguem o mesmo princípio do Decorator Pattern GoF | Exemplos citados: `@Injectable` (Angular), `@Component` (NestJS) | Médio — tecnicamente os decorators de linguagem (metadata/anotação) são um mecanismo sintático diferente do Decorator estrutural GoF (wrapping de interface); a analogia funcional (adicionar comportamento sem alterar a classe original) procede, mas a mecânica não é idêntica |
| Adapter permite trocar biblioteca (Axios → `fetch`) sem tocar no resto do código | Exemplo dado: adapter implementa a mesma interface do Axios usando `fetch` por baixo | Alto — mesmo princípio já documentado em [[wiki/concepts/adapter-pattern]] via troca de lib de PDF (DomPDF → TCPDF) |
| ORMs (Prisma, TypeORM) e drivers de banco são exemplos de Adapter | "Eles traduzem chamadas genéricas pro protocolo específico de cada banco" | Alto — consistente com a definição estrutural do padrão |

## Estrutura dos Seis Patterns

| Pattern | Categoria GoF | Analogia usada | Problema que resolve |
|---|---|---|---|
| [[wiki/concepts/observer-pattern]] | Comportamental | Sino de inscrição do YouTube | Vários objetos precisam reagir à mesma mudança de estado |
| [[wiki/concepts/factory-pattern]] | Criacional | Pedido numa pizzaria | Criação de objeto variável por contexto, sem espalhar lógica de instanciação |
| [[wiki/concepts/singleton-pattern]] | Criacional | Elevador único do prédio | Garantir instância única com ponto de acesso global |
| [[wiki/concepts/decorator-pattern]] | Estrutural | Filtros empilhados do Instagram | Adicionar comportamento sem alterar o objeto original, de forma combinável |
| [[wiki/concepts/strategy-pattern]] | Comportamental | Opções de rota do GPS | Trocar algoritmo em tempo de execução sem `if/else` crescente |
| [[wiki/concepts/adapter-pattern]] | Estrutural | Adaptador de tomada de viagem | Compatibilizar interfaces que não foram desenhadas para trabalhar juntas |

## Interação Entre Patterns

O autor nota explicitamente que os patterns compõem entre si — não são escolhas mutuamente exclusivas:

- Uma **factory** pode criar **singletons** (a factory decide criar só na primeira chamada e retornar a mesma instância depois).
- Um **observer** pode usar **strategy** para decidir *como* notificar cada tipo de assinante.
- Um **adapter** pode envolver um objeto que foi criado por uma **factory**.

## Alerta Final

> "O ponto mais importante é não sair enfiando o design pattern em tudo. Eles existem para resolver problemas reais, e não é para deixar o código bonito. Se o problema não existe, os patterns também não precisam ser usados."

Mesmo princípio de cautela já presente em [[wiki/concepts/over-engineering]] e reforçado por [[wiki/sources/sete-padroes-de-design-de-software]] em relação ao Singleton especificamente.

## Conexões

- [[wiki/sources/sete-padroes-de-design-de-software]] — cobertura mais ampla (7 padrões, incluindo Builder), mesmo tom de ressalva sobre Singleton como "variável global glorificada"
- [[wiki/sources/design-pattern-observer]], [[wiki/sources/design-pattern-observer-codigo-fonte-tv]] — aprofundamento do Observer com pseudocódigo e implementação real
- [[wiki/sources/design-pattern-adapter]] — caso real (DomPDF → TCPDF) que ilustra com mais profundidade a mesma alegação sobre troca de biblioteca sem tocar na regra de negócio
- [[wiki/sources/design-pattern-strategy]], [[wiki/sources/design-pattern-facade]], [[wiki/sources/design-pattern-facade-renato-augusto]], [[wiki/sources/design-pattern-proxy]] — os outros padrões do "núcleo prático" já documentados na wiki

## Questões em Aberto

- Autoria e canal do vídeo não identificados na transcrição de áudio recebida — sem título, sem nome de apresentador, sem URL. Diferente de [[wiki/sources/sete-padroes-de-design-de-software]] (atribuído ao canal Forest), esta fonte não pôde ser atribuída com confiança.
- A equivalência entre decorators de linguagem do TypeScript (`@Injectable`, `@Component`) e o Decorator Pattern estrutural do GoF é tratada como direta pelo autor, mas a mecânica de implementação (metadata reflection vs. wrapping de interface em runtime) é distinta — vale uma nota de precisão técnica caso a wiki aprofunde essa comparação no futuro.
