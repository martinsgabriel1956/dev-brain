---
type: concept
title: "System Design por Nível de Senioridade"
aliases: ["system design junior pleno senior", "expectativas de system design por nível", "o que esperar de cada senioridade em arquitetura"]
date_created: 2026-07-27
date_updated: 2026-07-30
source_count: 3
tags: [system-design, carreira, senioridade, junior, pleno, senior, entrevistas]
skill: tech-mentor-system-design
status: draft
---

# System Design por Nível de Senioridade

**TL;DR:** o que se espera de [[wiki/concepts/entrevista-system-design|system design]] muda por nível de carreira, mas não da forma como as empresas costumam avaliar — a entrevista tende a cobrar sempre a compreensão do sistema completo (padrão popularizado pelo Google), enquanto no trabalho do dia a dia júnior e pleno raramente precisam dessa visão do todo. A progressão central é: júnior **soluciona e demonstra fundação**, pleno **resolve com racional prático**, sênior **otimiza e lidera a conversa sobre tradeoffs**.

## Por que essa distinção existe

Não há consenso entre empresas sobre a definição exata de júnior/pleno/sênior, então qualquer categorização de "o que esperar de cada nível" é necessariamente uma média, não uma regra. Ainda assim, um padrão recorrente aparece: existe uma diferença entre **como você é entrevistado** e **como você trabalha de fato**.

- **Entrevista:** cobra compreensão do todo (arquitetura, esquemas, tradeoffs, infra, API, escalabilidade, filas) em praticamente todos os níveis — herança do padrão de entrevista popularizado pelo Google e copiado amplamente.
- **Trabalho real:** júnior e pleno geralmente operam com visão rasa do todo + profundidade na parte específica que tocam (API, banco, infra). A compreensão do todo só se torna central a partir de sênior, tipicamente ao desenvolver uma feature nova ponta a ponta ou um sistema do zero para uma equipe — trabalho raramente delegado a júniors ou plenos.

## Progressão por nível

### Júnior — solucionar e demonstrar fundação

Compreensão básica de servidor/cliente, banco de dados, API, protocolo de comunicação (HTTP/RPC). Não precisa explicar tradeoffs a fundo — basta saber que a peça existe e resolve o problema ("vamos botar um banco aqui porque resolve"). Em entrevista, sistemas simples (encurtador de URL, jogo por turnos com 2 usuários) bastam; o resultado esperado é requisitos claros, fluxos de read/write, API e esquema simples, tradeoffs básicos e uma arquitetura de alto nível coerente.

### Pleno — resolver com racional prático

Além da base de júnior: workers, [[wiki/concepts/api-gateway|API Gateway]], [[wiki/concepts/load-balancer|load balancer]], tradeoffs SQL vs. NoSQL, Blob Store, [[wiki/concepts/cdn|CDN]] — com racional ligado a experiência real de ter usado essas peças, não apenas "sei que existe". Em entrevista, adiciona requisitos não funcionais, modelagem de API/esquema mais detalhada, algum nível de [[wiki/concepts/estimativas-back-of-envelope|estimativa]]/escalabilidade e identificação de gargalos/fault tolerance.

A linha entre pleno e sênior é descrita como cada vez mais borrada na prática de mercado — a progressão de um para o outro tende a ser rápida.

### Sênior — otimizar e liderar a conversa

Não se avalia mais se a peça básica é conhecida (isso já é dado) — se avalia se o candidato consegue usar essa base para escalar a milhões de usuários. Foco em tradeoffs: monolito vs. microsserviços, [[wiki/concepts/cap-theorem|teorema de CAP]], [[wiki/concepts/db-sharding|sharding]], [[wiki/concepts/cache|cache]] (ex.: cache-aside), reader replicas. Postura muda de reativa (responder ao que é perguntado) para proativa — o candidato lidera a conversa, pergunta e clarifica antes de desenhar.

### Sênior plus (tech lead / CTO / staff)

Desenvolver um sistema inteiro do zero para uma equipe trabalhar em cima — decidir SQL vs. NoSQL, serverless vs. servidor dedicado, [[wiki/concepts/microsservicos|monolito vs. microsserviços]] — e justificar cada decisão é tipicamente atribuição desse nível acima de sênior "puro".

[[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] descreve um eixo complementar (não de profundidade técnica, mas de escopo de responsabilidade) para diferenciar sênior de staff: sênior tende a olhar para o escopo do próprio produto, staff tende a olhar para a vertical inteira (múltiplos produtos/times) e como extrair valor máximo dali. A fonte usa isso para explicar por que a armadilha de escolher a solução mais complexa em vez da que resolve a causa raiz é especialmente comum nesse ponto da progressão — ver [[wiki/concepts/senior-vs-staff-visao-arquitetural]] para o detalhamento.

## Relação com outros conceitos

- [[wiki/concepts/entrevista-system-design]] — a estrutura de sessão (requisitos → capacidade → modelagem → desenho) que esta progressão por nível se aplica em cima
- [[wiki/concepts/estimativas-back-of-envelope]] — mais central e mais precisa quanto mais sênior
- [[wiki/concepts/cap-theorem]] — vocabulário esperado especificamente em nível sênior
- [[wiki/concepts/comparacao-na-carreira]] — falta de consenso sobre definições de nível é um tema recorrente na carreira dev, não exclusivo de system design
- [[wiki/concepts/senior-vs-staff-visao-arquitetural]] — eixo complementar (escopo de produto vs. escopo de vertical) para o nível sênior plus/staff
- [[wiki/concepts/causa-raiz]] e [[wiki/concepts/over-engineering]] — a armadilha de complexidade desnecessária associada ao nível sênior plus/staff nesta fonte

## Key Sources

- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — confirmação prática independente: o apresentador, ao desenhar um rascunho de entrevista, decide não aprofundar escalabilidade/RPS por considerar isso pergunta de senioridade mais alta — mesma gradação descrita nesta página, vinda de outra fonte/canal
- [[wiki/sources/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas]] — eixo complementar de sênior vs. staff baseado em escopo (produto vs. vertical), não profundidade técnica
