---
type: source
title: "Monolito Modular: a etapa entre o MVP simples e a empresa madura"
aliases: ["monolito modular transicao", "modular monolith mvp empresa madura"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_count: 0
tags: [monolito-modular, monolito, microsservicos, hexagonal, ports-adapters, code-espaguete, arquitetura, migracao]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/monolito-modular-transicao-mvp-empresa-madura.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-10
---

# Monolito Modular: a etapa entre o MVP simples e a empresa madura

## TL;DR

Vídeo didático que apresenta o [[wiki/concepts/monolito-modular]] como a **etapa intermediária** entre um MVP simples (um [[wiki/concepts/monolito]] pequeno) e a maturidade que eventualmente exige [[wiki/concepts/microsservicos]]. A tese central: microsserviços resolvem o [[wiki/concepts/code-espaguete]] porque **impossibilitam** que um serviço chame funções de outro (a comunicação passa a ser via rede/API), mas essa mesma troca — chamada de função por chamada de rede — traz latência e overhead de DevOps que **não** são desejáveis quando o problema não é de hardware/escala. O monolito modular captura o pró que interessa (isolamento + fim do espaguete) sem os contras (comunicação via protocolo, DevOps complexo): um único artefato, um banco, um runtime, dividido em **módulos** que se comunicam por **contratos/interfaces** ([[wiki/concepts/hexagonal-architecture|Ports & Adapters]]) em vez de chamadas diretas. Bônus: como as interfaces já estão expostas, extrair um módulo para virar microsserviço depois é só trocar *como* ele se comunica (função → gRPC).

## Key Claims

**Claim:** Microsserviços eliminam o código espaguete por **impossibilidade estrutural**, não por disciplina.
**Evidence:** Um microsserviço não tem acesso às funções de outro; a comunicação só acontece via protocolos de rede (REST/GraphQL sobre HTTP, ou gRPC). Como um serviço não consegue chamar diretamente o outro, torna-se impossível o acoplamento em cadeia que gera o espaguete. "A troca foi substituir uma chamada de função por uma chamada via rede — isso algemou a gente."
**Confidence:** alta

**Claim:** A mesma troca que impede o espaguete é uma **desvantagem** quando o problema não é de hardware.
**Evidence:** Chamada via rede entre máquinas diferentes é muito mais lenta que chamada de função. Se cada serviço tem seu banco, um único request pode exigir consultar quatro bancos diferentes. Comunicação via protocolo só é vantagem quando há razão de hardware real (ex.: 20% da app é um cluster de IA que precisa de GPUs próprias, o resto cabe numa máquina pequena).
**Confidence:** alta

**Claim:** O pulo direto de monolito para microsserviços é doloroso para empresas **pequenas e médias**.
**Evidence:** Microsserviços pressupõem times autônomos (squads de ~6 por serviço) atuando como "empresas independentes". Numa empresa de 6 pessoas no total, cada pessoa teria que fazer o seu serviço, o seu DevOps e o seu banco — agir como uma empresa completa. Para empresas de 10-50 pessoas, carregar o monolito fica pesado ao mesmo tempo em que o overhead distribuído (logging distribuído, falhas distribuídas, latência) é caro demais.
**Confidence:** alta

**Claim:** Monolitos levam MVPs muito longe; migrar não é obrigatório.
**Evidence:** Pieter Levels, sozinho, mantém vários produtos — todos monolitos — faturando milhões/ano. Com ~1 milhão de usuários e produto simples, basta rodar o monolito em 3-4 máquinas com load balancer e réplica de banco. Sugerir microsserviços a ele seria idiotice.
**Confidence:** alta (o exemplo do Pieter Levels é ilustrativo/anedótico)

**Claim:** Monolito modular é um monolito — um artefato, um banco, um runtime — com módulos de fronteira explícita.
**Evidence:** Módulos não chamam funções uns dos outros; comunicam-se por **contratos/interfaces** (analogia com getters/setters de uma classe), definindo input e output. Isso garante separation of concerns e encapsulamento. Design pattern citado: Ports & Adapters / arquitetura hexagonal.
**Confidence:** alta

**Claim:** Modularizar antes facilita a extração futura para microsserviço.
**Evidence:** Se as interfaces já estão expostas, extrair um módulo (ex.: IA para GPUs próprias) é só trocar o transporte: antes chamada de função na interface, depois gRPC. "Não havia espaguete antes, não há espaguete agora — só um módulo que saiu do monolito e virou serviço." (Convergente com o aviso do skill: extrair *antes* de ter módulo bem definido → distributed monolith.)
**Confidence:** alta

## Entities

- **Pieter Levels** — exemplo de solo dev cujos produtos monolíticos faturam milhões (argumento "monolito basta").
- **Facebook / Uber / Google / iFood** — big techs que quebraram monolitos ou nasceram distribuídas.
- **Elixir** — citado pelo *hot code swap* como exceção ao "tem que fazer deploy de tudo de novo".
- **gRPC** — transporte usado ao extrair um módulo para microsserviço.

## Concepts

- [[wiki/concepts/monolito-modular]] — o conceito central.
- [[wiki/concepts/monolito]] — ponto de partida.
- [[wiki/concepts/microsservicos]] — destino eventual, com trade-offs.
- [[wiki/concepts/code-espaguete]] — o problema que dispara a discussão.
- [[wiki/concepts/hexagonal-architecture]] — Ports & Adapters como forma de comunicação entre módulos.
- [[wiki/concepts/contrato-de-api]] — "contrato" = interface exposta pelo módulo.
- [[wiki/concepts/separation-of-concerns]] e [[wiki/concepts/encapsulamento]] — o que os contratos garantem.
- [[wiki/concepts/database-per-service]] — banco por serviço (o vídeo tem ressalvas).
- [[wiki/concepts/escalabilidade-horizontal]] — rodar o monolito em N máquinas com LB e réplica.

## Open Questions / Contradictions

- O vídeo diz que microsserviços "impossibilitam" o espaguete. O skill e [[wiki/concepts/microsservicos]] apontam o **distributed monolith** como contraexemplo: microsserviços com fronteiras mal definidas reintroduzem acoplamento (deploys coordenados, banco compartilhado, chamadas síncronas em cadeia). Ou seja, a impossibilidade é estrutural para *chamadas de função*, mas não elimina acoplamento de outra natureza.
- "Cada serviço tem seu próprio banco" — o autor explicita que tem ressalvas ("deixe quieto"), alinhado com o debate registrado em [[wiki/concepts/database-per-service]].

## Raw quotes

> "A troca que a gente fez foi trocar uma chamada de função por uma chamada via rede — e isso algemou a gente, travou nossas mãos, preveniu que a gente transformasse o código numa sopa. Mas nem tudo são flores."

> "Pensa em getters e setters: você vai definir como os outros módulos podem interagir com o seu módulo, da mesma maneira que uma classe define como o mundo de fora interage com ela."

> "As interfaces já estavam expostas. Só o que eu preciso trocar é como se comunica: antes era uma chamada de função, agora é uma chamada via gRPC."
