---
type: source
title: "Os 10 Princípios da Arquitetura Modular"
aliases: ["10 princípios da arquitetura modular", "monolito modular vs arquitetura modular"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/os-10-principios-arquitetura-modular-valdemar-neto.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-09-01
source_count: 0
tags: [monolito-modular, arquitetura-modular, microsservicos, monorepo, nx, modularizacao, ddd, backend, nestjs]
skill: tech-mentor-backend
status: stable
---

# Os 10 Princípios da Arquitetura Modular

## TL;DR

Vídeo de [[wiki/entities/valdemar-neto|Valdemar Neto]] (cofundador da [[wiki/entities/tech-leads-club|Tech Leads Club]], ex-Atlassian, ex-Totvs) que formaliza uma distinção terminológica não vista antes na wiki: **monolito modular** (um único deploy/app carregando todos os módulos, com `main.ts` alternativos permitindo rodar submódulos isolados) vs. **arquitetura modular** (múltiplos monolitos/apps, cada um compondo um subconjunto arbitrário de módulos a partir do mesmo codebase via monorepo). A arquitetura modular é apresentada como onde "realmente está a grande escala" — microsserviços não compõem (não cabem vários dentro de uma mesma app, pois vivem em codebases diferentes), enquanto módulos de domínio num monorepo podem ser recombinados infinitamente. O vídeo lista **10 princípios** nomeados e numerados para escalar arquiteturas modulares (limites bem definidos, componibilidade, independência, isolamento de estado, comunicação explícita, substituibilidade, deploy independente, escala independente, monitoramento/observabilidade, falhas isoladas), com demonstração concreta em NestJS/NX usando um sistema de streaming (estilo Netflix) com módulos billing/streaming/identity/shared-infra.

## Claims Principais

| Claim | Confiança |
|---|---|
| Distinção nova: **monolito modular** = um artefato/deploy carregando todos os módulos (mesmo permitindo `main.ts` alternativos para submódulos isolados); **arquitetura modular** = múltiplos monolitos/apps compondo módulos de domínio de formas arbitrárias a partir do mesmo codebase via monorepo | Alta — reformula com nomes próprios ("monolito modular" vs. "arquitetura modular") o mesmo mecanismo já documentado como [[wiki/concepts/composicao-de-modulos|module composition]] pela fonte [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]], mas cunha os termos de forma mais explícita e hierárquica |
| Microsserviços têm uma limitação estrutural que arquiteturas modulares não têm: **não compõem** — não é possível colocar vários microsserviços dentro de uma mesma app/processo, porque vivem em codebases/repositórios diferentes; módulos de domínio num monorepo podem ser compostos em "infinitas" combinações de apps | Alta — argumento novo e específico, não registrado antes desta forma em [[wiki/concepts/microsservicos]]; consistente com a tese geral já central da página (microsserviços resolvem complexidade local ao custo de complexidade global) |
| Dois motivos concretos para o retorno de monolitos modulares: (1) virtualização — hoje qualquer parte do código roda isolada em contêineres; (2) aprendizado com décadas de microsserviços — separação traz benefícios de design/coesão mas com custo alto de operação/carga cognitiva/gestão | Alta — reforça diretamente [[wiki/concepts/microsservicos]] (seção Custo-Benefício) com um ângulo histórico específico (antes só empresas grandes tinham ferramental; hoje qualquer um tem) |
| **10 princípios nomeados** para escalar arquitetura modular: limites bem definidos, componibilidade, independência, isolamento de estado, comunicação explícita, substituibilidade, deploy independente, escala independente, monitoramento/observabilidade, falhas isoladas | Alta — taxonomia própria do autor (parte de um livro em produção), mecanismos individuais (Ports & Adapters, database-per-module, façade/HTTP client, circuit breaker) já documentados em outras fontes da wiki sob nomes distintos |
| Comunicação explícita entre módulos usa **façade injetada** (classe que chama internamente um serviço de outro módulo) ou **HTTP client injetado via interface** (chamada REST para localhost) — nunca chamada direta de service para service | Alta — mecanismo concreto no código (NestJS), consistente com [[wiki/concepts/hexagonal-architecture|Ports & Adapters]] já documentado em [[wiki/concepts/monolito-modular]] |
| Limites do monolito modular clássico (aplicando os 10 princípios num único monolito): deploy independente é difícil (exige ferramental próprio), escala independente é difícil (mesmo processo/codebase, exige muito script customizado), falhas isoladas são difíceis (mesmo processo) — resolvidos migrando para monorepo com múltiplas apps (arquitetura modular) | Alta — mesma limitação de "redeploy cruzado" já documentada em [[wiki/concepts/monolito-modular]] (seção "Monolito é uma Escolha de Deploy"), agora generalizada para os três princípios mais difíceis de aplicar num monolito único |
| Ferramental de monorepo (NX no exemplo; cita também Bazel e Maven como alternativas usadas com Java) resolve as limitações acima ao permitir isolar deploy/escala/pipeline por módulo — "roda só o que mudou" | Alta — reforça `nx affected` já documentado em [[wiki/concepts/monorepo-backend]]; Bazel/Maven são menções novas nesta fonte (não documentadas antes na wiki como ferramental de monorepo) |
| No início de um sistema modular, na dúvida, criar módulos grandes e deixar a coesão interna aparecer antes de quebrar em módulos menores | Média-Alta — heurística prática nova nesta fonte, não documentada antes; alinhada ao espírito de "comece grande, extraia com necessidade real" já central em [[wiki/concepts/monolito-modular]] e [[wiki/concepts/monolith-first]] |

## Entidades

- [[wiki/entities/valdemar-neto]] (novo) — autor, cofundador da Tech Leads Club, ex-Atlassian, ex-Totvs
- [[wiki/entities/tech-leads-club]] (novo) — empresa/comunidade cofundada pelo autor, oferece o curso "Aplicações Enterprise" citado na fonte

## Conceitos

- [[wiki/concepts/arquitetura-modular]] (novo) — distinção formal monolito modular vs. arquitetura modular, os 10 princípios
- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/composicao-de-modulos]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/monorepo-backend]]

## Open Questions

- Nomes de empresas mencionados no áudio ("Atlácia", "Totorks") foram normalizados para "Atlassian" e "Totvs" por proximidade fonética e plausibilidade (empresas de tecnologia reais, compatíveis com o perfil de "cofundador de Tech Leads Club" que ensina arquitetura de sistemas de grande porte) — não confirmado por fonte externa nesta ingestão.
- Livro "Os 10 Princípios da Arquitetura Modular" e curso "Aplicações Enterprise" (Tech Leads Club) são mencionados como trabalho em andamento/produto comercial — não verificados externamente, apenas registrados como contexto de autoria.
- Bazel e Maven são citados de passagem como ferramental de monorepo alternativo ao NX, sem exemplo prático demonstrado nesta fonte (só o exemplo NestJS/NX é mostrado em detalhe) — nenhuma página própria criada para eles nesta ingestão.

## Contradições com a Wiki Existente

Nenhuma contradição — forte reforço e formalização terminológica do que já estava documentado de forma mais dispersa. A principal contribuição é dar nomes explícitos e hierárquicos (monolito modular vs. arquitetura modular) a uma distinção que a wiki já tinha registrado em termos mais soltos (via [[wiki/concepts/composicao-de-modulos|module composition]], cunhado pela fonte anterior [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]]), e adicionar uma taxonomia numerada de 10 princípios que não existia antes na wiki. Vale notar: as duas fontes descrevem o **mesmo mecanismo técnico** (monorepo com módulos de domínio recombináveis em múltiplas apps) com nomes de conceito diferentes — "module composition" vs. "arquitetura modular" — tratado aqui como sinônimo, não como conceito novo e distinto.

## Citações Brutas Preservadas

> "A verdade é que monolitos modulares podem escalar tanto quanto microsserviços se forem bem estruturados."

> "A grande diferença de arquitetura modular para monolitos modulares é que numa arquitetura modular tu pode ter vários monolitos, várias maneiras de agrupar módulos [...] coisa que não é possível fazer com microsserviços, porque eles estão em codebases diferentes."

> "Qual que é o limite de microsserviços? Microsserviços não compõe, tu não consegue botar vários microsserviços dentro de uma mesma app."

> "Na dúvida, façam módulos bem grandes, deixem aparecer os agrupamentos internos, a coesão começar a aparecer, aí sim começa a criar módulos menores."

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/arquitetura-modular]]
- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/composicao-de-modulos]]
- [[wiki/concepts/monorepo-backend]]
- [[wiki/entities/valdemar-neto]]
- [[wiki/entities/tech-leads-club]]
