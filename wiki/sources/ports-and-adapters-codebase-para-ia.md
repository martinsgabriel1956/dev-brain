---
type: source
title: "Ports and Adapters — Codebase Preparada para IA"
aliases: ["hexagonal ia", "codebase ia qualidade", "ports adapters antes depois"]
date_created: 2026-05-04
date_updated: 2026-05-04
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ports-and-adapters-codebase-para-ia.md
source_url: null
author: "Galego"
date_published: null
date_ingested: 2026-05-04
source_count: 0
tags: [hexagonal-architecture, ports-adapters, codebase-quality, ia-engineering, acoplamento, refactoring]
skill: tech-mentor-backend
status: stable
---

# Ports and Adapters — Codebase Preparada para IA

## TL;DR

A qualidade do código que a IA vai interagir importa mais do que o prompt, o modelo ou a ferramenta. As mesmas técnicas de manutenibilidade que sempre funcionaram para humanos são as que tornam o código mais legível para IA. O vídeo demonstra isso com um exemplo antes/depois usando Ports and Adapters num blog simples (users, posts, comments).

---

## Key Claims

### Claim 1 — Codebase ruim prejudica IA mais do que prompt ruim
**Evidence:** Tentar refatorar código legado complexo com IA produz resultados piores do que ter uma codebase bem estruturada desde o início.
**Source:** Galego, vídeo canal
**Confidence:** alto — alinhado com Navigation Paradox (paper) e Addy Osmani

### Claim 2 — God class com forte acoplamento cria cascata de quebras
**Evidence:** No exemplo, mudar a estrutura interna de `User` quebra lógica de posts E de comments — três lugares afetados por uma única mudança.
**Source:** demonstração de código
**Confidence:** alto — consequência direta de ausência de encapsulamento

### Claim 3 — Ports and Adapters permite substituição sem quebrar o resto
**Evidence:** Migrar de armazenamento in-memory para Clerk (serviço externo) = criar um novo adapter que implementa a mesma interface + trocar uma linha no `index.ts`. O resto não muda.
**Source:** demonstração de código
**Confidence:** alto

### Claim 4 — Mais linhas de código e mais arquivos é a troca correta acima de certo tamanho
**Evidence:** Para 200 linhas, god class funciona. Para 20.000 linhas e 4 colaboradores, ports and adapters é claramente superior. O overhead se paga.
**Source:** Galego, vídeo canal
**Confidence:** alto — consenso da indústria

---

## Conceitos Centrais

- [[concepts/hexagonal-architecture]] — Ports & Adapters: o padrão e seus componentes
- [[concepts/codebase-legibilidade-ia]] — legibilidade para humanos = legibilidade para IA
- [[concepts/acoplamento]] — o inimigo central; forte acoplamento congela o código
- [[concepts/adapter-pattern]] — implementação concreta de um port
- [[concepts/single-responsibility-principle]] — cada módulo com uma razão para mudar

---

## Antes vs Depois — Estrutura

**Antes (god class, `index.ts` único):**
```
index.ts — 238 linhas
└── Classe App
    ├── banco de dados embutido
    ├── inicialização de users/posts/comments
    ├── routing com if/else por método HTTP + path
    ├── validação de e-mail inline (loop, não função)
    └── regras de negócio misturadas com infra
```

**Depois (ports and adapters):**
```
src/
├── domain/          — tipos e regras de domínio
├── repositories/    — ports (interfaces/contratos)
├── adapters/        — implementações concretas
├── services/        — regras de negócio
├── router/          — rotas por serviço
└── index.ts         — instanciação e injeção
```

---

## Por Que Isso Importa Para IA

| Cenário | God Class | Ports & Adapters |
|---|---|---|
| "Altere como usuários são criados" | IA precisa entender 20k linhas de contexto misturado | IA abre `user.service.ts` + `user.adapter.ts` |
| "Troque o banco de dados de users" | IA vai quebrar posts e comments sem perceber | IA cria novo adapter, troca uma linha no index |
| "Adicione busca por e-mail" | IA duplica o loop inline | IA adiciona método ao UserRepository |
| Contexto necessário por tarefa | Alto (tudo está interconectado) | Baixo (contexto localizado por módulo) |

---

## Discussão: Repository vs Service em Dependências Cruzadas

`PostService` usa `userRepository` diretamente (não `UserService`):

- **Adequado para** sistemas que não vão evoluir para microsserviços
- **Prefira chamar o `UserService`** se a evolução para microsserviços for esperada — evita que PostService saiba que existe um repositório de usuário

---

## Discussão: Regras de Negócio no Service vs Domain

O autor coloca validações no `UserService`. O argumento DDD puro seria colocar no domínio. Para uma codebase que veio de god class, o service já é uma melhoria substancial — refinar para domínio é o próximo passo incremental.

> "Eu não gosto de começar com uma função por arquivo. Gosto de ir incrementando depois."

---

## Quando NÃO Aplicar

- MVPs com < 300 linhas e uma pessoa: god class é adequada
- O overhead compensa quando: projeto vai crescer, partes podem ser substituídas, múltiplos colaboradores

---

## Conexões com o Wiki

- [[sources/hexagonal-architecture]] — referência técnica aprofundada do padrão (Alistair Cockburn, driving/driven ports, in-memory adapters)
- [[sources/clean-architecture-ia-custo-real]] — custo em tokens de arquitetura horizontal com IA
- [[sources/navigation-paradox-2026]] — agente perde arquivos críticos em arquitetura por camada
- [[sources/acoplamento-abstracao-estado]] — acoplamento como lente de design

---

## Open Questions

- Ports and adapters + IA: existe um tamanho de módulo "ideal" para que o agente consiga trabalhar sem precisar abrir outros módulos?
- Como medir o ROI do refactor em termos de qualidade de resposta do agente?
