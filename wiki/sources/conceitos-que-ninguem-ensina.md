---
type: source
title: "Conceitos que Ninguém Ensina em Curso"
aliases: ["conceitos ninguem ensina", "back pressure", "thundering herd", "temporal coupling", "complexidade acidental"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/conceitos-que-ninguem-ensina.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [back-pressure, thundering-herd, temporal-coupling, accidental-complexity, essential-complexity, sistemas-distribuidos, fundamentos]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Quatro conceitos que separam devs que entendem o sistema dos que estão na esperança: (1) **Back Pressure** — produtor mais rápido que o consumidor; fix é desacelerar, bufferizar ou descartar deliberadamente. (2) **Thundering Herd** — cache expira e 10k requests batem no banco simultaneamente; fix é probabilistic early expiration + request coalescing. (3) **Temporal Coupling** — duas partes do sistema precisam de ordem específica mas nada no código impõe isso; fix é API impossível de chamar errado. (4) **Complexidade Acidental vs. Essencial** (Fred Brooks) — essencial é inerente ao problema; acidental é tudo que o time criou por acidente e chamou de tech debt.

## Key Claims

**Claim:** Back pressure ocorre quando o produtor é mais rápido que o consumidor — sem controle explícito, o sistema toma a decisão por você travando.
**Evidence:** Fila que cresce sem parar + memória subindo = back pressure não tratado. O fix correto é na fonte: desacelerar o produtor, bufferizar com limite máximo, ou descartar dados deliberadamente com política de prioridade. Deixar o sistema decidir por crash é o anti-padrão. Em Node.js streams: `readable.pipe(writable)` aplica back pressure automaticamente — `writable` sinaliza `drain` quando pronto para receber mais.
**Confidence:** alta

**Claim:** Thundering herd derruba bancos porque 10k requisições simultâneas batem no momento exato de expiração do cache.
**Evidence:** Cache expira → todos os callers detectam miss ao mesmo tempo → todos vão ao banco simultaneamente → banco passa de centenas para milhares de requests/segundo instantaneamente. Fixes: probabilistic early expiration (expirar levemente antes, de forma aleatória por caller, para que um único caller reconstrua enquanto outros ainda usam o cache válido); request coalescing (apenas um rebuilder, os outros aguardam o resultado). Cache stampede prevention é o nome do conjunto de técnicas.
**Confidence:** alta

**Claim:** Temporal coupling é quando a ordem de chamadas é implícita — vive em comentários ou na cabeça do dev original, e o erro resultante é completamente sem relação com a causa.
**Evidence:** `initialize()` antes de `process()`, abrir conexão antes de enviar dados. Quando alguém chama fora de ordem (e sempre chama), o erro é NullPointerException ou "connection refused" — não "você chamou na ordem errada". A solução de design é tornar a ordem impossível de violar: construtor que inicializa, builder pattern que força sequência, tipos que só existem após o passo anterior (`ConnectionBuilder` retorna `OpenConnection` que é o único parâmetro de `send()`).
**Confidence:** alta

**Claim:** A distinção essencial vs. acidental de Fred Brooks é o modelo mental mais útil para priorizar tech debt — complexidade essencial não pode ser removida, acidental deve ser.
**Evidence:** Pagamentos têm complexidade essencial: falhas de transação, retry, conciliação existem porque o problema é genuinamente difícil. Função de 400 linhas que faz 17 coisas é complexidade acidental: existe porque foi mais fácil adicionar do que refatorar. Diagnóstico: "essa complexidade existe porque o problema exige ou porque o time a criou?" Se a segunda resposta, é acidental e tem custo operacional crescente sem contrapartida de valor.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/back-pressure]]
- [[concepts/thundering-herd]]
- [[concepts/temporal-coupling]]
- [[concepts/accidental-complexity]]
- [[concepts/essential-complexity]]
- [[concepts/cache-stampede]]
- [[entities/fred-brooks]]

## Open Questions

- Back pressure em sistemas de mensageria (Kafka) — como o consumer lag se traduz em back pressure e quando escalar consumers vs desacelerar producers?
- Temporal coupling em microsserviços — service A deve existir antes de service B, mas Kubernetes não garante ordem de startup. Como resolver além de retry com backoff?
