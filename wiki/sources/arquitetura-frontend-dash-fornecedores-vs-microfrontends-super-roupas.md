---
type: source
title: "Super Roupas: Dash de Fornecedores vs. Microfrontends — Estudo de Caso de Arquitetura Frontend"
aliases: ["super roupas microfrontends", "dash de fornecedores bff", "senior vs staff arquitetura", "escalável para quê"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/arquitetura-frontend-dash-fornecedores-vs-microfrontends-super-roupas.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-30
source_count: 1
tags: [frontend, arquitetura, bff, microfrontends, over-engineering, causa-raiz, senioridade, system-design, api-composition]
skill: tech-mentor-frontend
status: stable
---

## TL;DR

Estudo de caso fictício (empresa "Super Roupas") ilustra um erro arquitetural comum: diante de 4 fornecedores com sistemas de gestão próprios e incompatíveis (dificultando saber quais roupas estão liberadas para venda), a solução "vendida" por um sênior inexperiente é unificar tudo num frontend só via [[wiki/concepts/microfrontends-parciais|microfrontends parciais]] orquestrados por um container/shell com comunicação por eventos — preservando polirrepo e CDs independentes para "reduzir acoplamento". O autor argumenta que essa solução ataca o sintoma errado: o problema real não é a experiência estar fragmentada, é a **falta de visibilidade de status/atraso** entre os 4 sistemas. A solução enxuta proposta é um frontend **somente leitura** (dashboard) alimentado por um [[wiki/concepts/bff-pattern|BFF]] que agrega dados dos 4 sistemas — sem tocar nos backends legados nem forçar unificação de produto. Estimativa qualitativa: a solução de microfrontends levaria 3+ meses com atrito de coordenação entre times e não resolveria a causa raiz; o dashboard/BFF é entregável em <2 meses por um time de 4 pessoas e já gera valor validável. A tese central é apresentada como o que diferencia, na prática, um sênior (foco no escopo do próprio produto) de um staff (foco em extrair valor máximo pela vertical): a tendência de confundir "solução mais complexa" com "solução mais madura/escalável", em vez de perguntar qual é a causa raiz do problema.

## Key Claims

**Claim:** A solução de microfrontends parciais (container/shell + módulos por rota para cada sistema de fornecedor + sidebar emitindo eventos) resolve o problema errado — ela endereça fragmentação de experiência, não a falta de visibilidade de status entre sistemas, que era o problema real relatado pela operação.
**Evidence:** A operação precisava consultar 4 sistemas diferentes para saber quais roupas desbloquear para venda, sem certeza se o produto chegaria a tempo. A proposta de unificação total exigiria reestruturar 4 interfaces heterogêneas (possivelmente com stacks divergentes — um serviço em MVC, outro hexagonal; um SQL, outro NoSQL) dentro de um único produto, com um BFF por trás e modelagem de entidades cruzada — descrito como "experiência muito custosa" mesmo focando só no front.
**Confidence:** média — é um relato/estudo de caso pedagógico com empresa fictícia, sem dados de produção reais; a estrutura do argumento (sintoma vs. causa raiz) é consistente com [[wiki/concepts/causa-raiz]], já documentada na wiki a partir de outra fonte independente.

**Claim:** Microfrontends parciais com comunicação via eventos reduzem acoplamento técnico entre equipes, mas não reduzem a complexidade de coordenação necessária para de fato resolver o problema de negócio — troca-se acoplamento de código por atrito organizacional (comunicação entre times, ausência de resolução na raiz).
**Evidence:** A solução do "sênior emotivo" é descrita com a justificativa técnica correta em isolamento (polirrepo, CDs independentes, baixo acoplamento via eventos), mas o autor estima mais de 3 meses de trabalho e "comunicação absurda entre times", sem de fato resolver o que a operação precisava saber (status/atraso por fornecedor).
**Confidence:** média — mesma fonte única, estimativa qualitativa sem benchmark; reforça e estende o levantamento de custos de microfrontends parciais já registrado em [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]], mas agora aplicado a um cenário de integração com sistemas de terceiros/fornecedores, não só entre módulos internos.

**Claim:** Um frontend somente leitura (dashboard) alimentado por um BFF que agrega os 4 sistemas de fornecedores resolve a causa raiz do problema (visibilidade de status/atraso) com fração do custo e do tempo da solução de unificação total — entregável em menos de 2 meses por um time de 4 pessoas.
**Evidence:** O dashboard permite drill-down por produto/fornecedor (produto A, B, C, D) extraindo métricas específicas de cada um, dando visibilidade direta sobre qual fornecedor mais atrasa — inclusive para decisões de negócio como cortar um fornecedor da lista. Nenhum sistema legado precisa ser alterado; o BFF só lê e agrega.
**Confidence:** média — proposta qualitativa e ilustrativa, não implementada/medida no material; consistente com o padrão de [[wiki/concepts/bff-pattern]] documentado na wiki (BFF como agregador que tira regra de negócio do frontend e reduz drasticamente o escopo de mudança nos serviços internos) e com [[wiki/concepts/api-composition]] (fan-out para múltiplos serviços).

**Claim:** A escolha recorrente pela solução arquitetural mais complexa em vez da mais direta para a causa raiz do problema é apresentada como diferença prática entre um sênior (foco no escopo/produto próprio) e um staff (foco em extrair valor máximo pela vertical/vários times) — mas a armadilha central (complexidade lida como maturidade/escalabilidade) é descrita como comum independente do nível.
**Evidence:** "É muito comum a gente ir para um caminho onde a gente acha que a solução mais complexa é a mais ideal, e não focar no problema que a gente quer resolver." O fechamento reforça isso como uma pergunta de reflexão: "escalável" é relativo — escalável para produto, para usuário, ou para times? — e a arquitetura deveria ser avaliada por resolver a causa raiz com o menor atrito, não por parecer madura/impressionante.
**Confidence:** baixa-média — é a tese de fechamento do autor, apresentada como heurística/reflexão pessoal, não como dado validado; complementa (sem contradizer) a distinção júnior/pleno/sênior já registrada em [[wiki/concepts/niveis-de-senioridade-system-design]], mas usa um eixo diferente (escopo do produto vs. escopo da vertical/staff) que essa página ainda não cobria.

## Entities & Concepts Touched

- [[wiki/concepts/over-engineering]]
- [[wiki/concepts/causa-raiz]]
- [[wiki/concepts/bff-pattern]]
- [[wiki/concepts/api-composition]]
- [[wiki/concepts/microfrontends-parciais]]
- [[wiki/concepts/microfrontend-baseado-em-rotas]]
- [[wiki/concepts/monolito-modular-frontend]]
- [[wiki/concepts/niveis-de-senioridade-system-design]]
- [[wiki/concepts/senior-vs-staff-visao-arquitetural]]

## Open Questions

- O material é um estudo de caso fictício/pedagógico — não há dados reais de produção (tempo de entrega real, custo de infra, número de fornecedores em produção) para validar as estimativas de "<2 meses" vs. "3+ meses". Registrado como limitação, não como benchmark.
- Não fica claro no material se a proposta de dashboard/BFF also endereça o outro problema citado de passagem (modelagem de entidades divergente entre os 4 sistemas de fornecedor — MVC vs. hexagonal, SQL vs. NoSQL) ou se isso continuaria sendo um problema não resolvido, só não crítico para o escopo do dashboard read-only.
- A distinção sênior (foco no produto) vs. staff (foco na vertical) é nova na wiki — só uma fonte cobre esse eixo específico; útil cruzar com uma futura fonte técnica sobre a progressão staff/principal engineer para decidir se vira página estável ou fica como stub.
