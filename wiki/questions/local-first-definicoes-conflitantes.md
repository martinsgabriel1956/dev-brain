---
type: question
title: "Local-First: duas fontes, dois significados incompatíveis"
aliases: ["local first definicoes conflitantes", "local-first ambiguo"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 2
tags: [local-first, offline-first, terminologia, contradiction, system-design]
skill: tech-mentor-system-design
status: draft
---

# Local-First: duas fontes, dois significados incompatíveis

A wiki tem duas fontes que usam o termo **"local-first"** para descrever arquiteturas completamente diferentes.

## Definição A — HMAC / dado efêmero sem storage no servidor

[[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]: o servidor **calcula** o dado (ex.: carrinho de compras com descontos), envia ao cliente com uma assinatura HMAC, e **nunca persiste** esse dado. O cliente guarda o payload localmente só para exibição; quando devolve ao servidor (ex.: no checkout), o servidor recalcula o HMAC para validar integridade — sem ter cópia salva para comparar. Aqui "local" significa "o único lugar onde o dado vive é o cliente, por economia de storage", mas **o servidor continua sendo a autoridade lógica** (ele que calculou o valor originalmente; o cliente não pode alterá-lo sem invalidar a assinatura).

## Definição B — canônica (Ink & Switch / Kleppmann): réplica primária com posse do usuário

[[wiki/sources/local-first-vs-offline-first]]: o dispositivo local é uma **réplica primária e autoritativa** — o usuário pode editar livremente, offline, e essa edição é válida por si só, sem precisar de aceite do servidor. O servidor é uma cópia secundária ("relay") usada para sincronização entre dispositivos, e pode cair sem impedir que as réplicas convirjam entre si (via LWW ou CRDT). Aqui "local" significa **posse real do dado pelo usuário** — se a empresa fechar, o arquivo continua seu.

## Por que são incompatíveis, não complementares

Na Definição A, o cliente **não tem autoridade** sobre o valor do dado — ele só o exibe e devolve intacto; qualquer alteração é detectada e rejeitada pelo HMAC. Na Definição B, o cliente **é** a autoridade — a edição local é definitiva e não depende de validação externa. Um sistema não pode ser as duas coisas ao mesmo tempo para o mesmo dado: ou o servidor valida contra alteração do cliente (A), ou o cliente tem liberdade de alterar sem essa validação (B).

A Definição B corresponde ao uso estabelecido do termo na literatura (Ink & Switch, "Local-first software", 2019; Martin Kleppmann). A Definição A parece ser um uso local/informal do termo pela fonte de entrevista, provavelmente por analogia superficial ("o dado vive no local, não no servidor") sem relação com a definição de posse/autoridade de réplica.

## Estado

Não resolvido por fusão — são conceitos diferentes que não deveriam compartilhar página. Ação tomada nesta ingestão: [[wiki/concepts/local-first]] foi revisado para apresentar a Definição B (canônica) como definição principal do conceito, com uma seção explícita marcando a Definição A como um uso divergente/específico do mesmo nome, cross-referenciada em vez de removida.

## Key Sources

- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]
- [[wiki/sources/local-first-vs-offline-first]]
