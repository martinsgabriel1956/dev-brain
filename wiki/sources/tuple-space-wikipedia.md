---
type: source
title: "Tuple Space (Wikipédia)"
aliases: ["espaço de tuplas", "tuple space wikipedia", "object space"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 0
tags: [tuple-space, linda, javaspaces, sistemas-distribuidos, coordenacao, memoria-associativa, blackboard, space-based-architecture]
skill: tech-mentor-backend
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tuple-space-wikipedia.md
source_url: https://en.wikipedia.org/wiki/Tuple_space
author: "Wikipédia (colaborativo, CC BY-SA)"
date_published:
date_ingested: 2026-08-21
---

# Tuple Space (Wikipédia)

## TL;DR

Verbete da Wikipédia (traduzido para pt-BR em `raw/`) sobre **[[wiki/concepts/tuple-space|tuple space]]**: um repositório compartilhado de tuplas, acessado concorrentemente por produtores (que escrevem) e consumidores (que leem/retiram por casamento de padrão) — a "metáfora do quadro-negro" ([[wiki/concepts/blackboard-metaphor|blackboard metaphor]]), uma forma de [[wiki/concepts/memoria-compartilhada-distribuida|memória compartilhada distribuída]]. Foi o embasamento teórico de **[[wiki/concepts/linda-coordination-language|Linda]]**, linguagem de coordenação criada por [[wiki/entities/david-gelernter|David Gelernter]] e [[wiki/entities/nicholas-carriero|Nicholas Carriero]] em Yale (1986). O verbete detalha a generalização **[[wiki/concepts/object-space|Object Space]]** (objetos passivos, exclusão mútua embutida via remoção-no-acesso) e sua implementação mais conhecida, **[[wiki/concepts/javaspaces|JavaSpaces]]** (parte da tecnologia Jini da Sun, comercialmente nichada em financeiro/telco, usando o padrão **[[wiki/concepts/master-worker-pattern|Master-Worker]]**), com um exemplo de código completo (write/read/take).

## Key claims

1. **Tuple space = memória associativa compartilhada e concorrente.** "Fornece um repositório de tuplas que pode ser acessado concorrentemente. Produtores postam dados como tuplas no espaço, e consumidores recuperam dados que casam com um certo padrão." Equivalente à "metáfora do quadro-negro" e uma forma de [[wiki/concepts/memoria-compartilhada-distribuida|memória compartilhada distribuída]]. *Evidência:* parágrafo de abertura.
2. **Origem teórica em Linda (Yale, 1986).** Tuple spaces foram "o embasamento teórico da linguagem Linda", desenvolvida por [[wiki/entities/david-gelernter|David Gelernter]] e [[wiki/entities/nicholas-carriero|Nicholas Carriero]]. Implementações existem para Java, Lisp, Lua, Prolog, Python, Ruby, Smalltalk, Tcl e .NET. *Evidência:* verbete.
3. **Object Spaces generaliza para objetos com comportamento — mas passivos enquanto no espaço.** Um provedor encapsula um serviço como objeto e o deposita no espaço; o objeto é registrado num Object Directory e localizável por *properties lookup*; um processo pode **bloquear esperando** um objeto aparecer. Objetos são **passivos** no espaço — métodos só podem ser invocados após o processo **recuperar o objeto para memória local**. *Evidência:* seção Object Spaces.
4. **Exclusão mútua é inerente ao modelo, não um mecanismo à parte.** "Uma vez que um objeto é acessado, ele é removido do Object Space e substituído somente após ser liberado. Nenhum outro processo pode acessar um objeto enquanto ele está sendo usado por um." A retirada (take) da tupla/objeto do espaço *é* o lock — não há primitiva de lock separada. *Evidência:* seção Object Spaces, último parágrafo.
5. **JavaSpaces: implementação Java, parte do Jini, nicho financeiro/telco.** Serviço de "troca e coordenação de objetos distribuído"; peers coordenam-se compartilhando estado. Escalabilidade via processamento paralelo; armazenamento confiável via **replicação distribuída**, mas o foco é baixa latência/alta performance, não cache confiável. JavaSpaces "não foi um sucesso comercial" como parte do Jini, mas sobrevive como tecnologia de nicho. Bill Joy (cofundador da Sun): o sonho de sistemas distribuídos exigiria "um salto quântico de pensamento". *Evidência:* seção JavaSpaces.
6. **Padrão dominante em JavaSpaces: Master-Worker.** "O Master distribui unidades de trabalho para o 'espaço', que são lidas, processadas e escritas de volta pelos workers." Ambientes típicos têm múltiplos espaços, masters e workers genéricos — desacoplamento espacial e temporal entre produtor e consumidor de trabalho. *Evidência:* seção JavaSpaces.
7. **API mínima de três operações: write / read / take.** O exemplo de código mostra `space.write(entry, null, Lease.FOREVER)` (publica, com lease/TTL), `space.read(...)` (lê sem remover) e `space.take(...)` (lê e remove — a operação que produz exclusão mútua). *Evidência:* bloco de código Java do verbete (Server/Client).

## Entidades

- [[wiki/entities/david-gelernter|David Gelernter]] — criador de Linda e do paradigma Object Spaces, Yale, anos 1980.
- [[wiki/entities/nicholas-carriero|Nicholas Carriero]] — coautor de Linda com Gelernter (Yale, 1986).
- [[wiki/entities/ken-arnold|Ken Arnold]] — engenheiro líder do JavaSpaces na Sun Microsystems.
- [[wiki/entities/bill-joy|Bill Joy]] — cofundador da Sun, citado sobre a ambição do modelo de sistemas distribuídos do Jini/JavaSpaces.

## Conceitos

[[wiki/concepts/tuple-space]] · [[wiki/concepts/linda-coordination-language]] · [[wiki/concepts/object-space]] · [[wiki/concepts/javaspaces]] · [[wiki/concepts/master-worker-pattern]] · [[wiki/concepts/memoria-compartilhada-distribuida]] · [[wiki/concepts/blackboard-metaphor]] · [[wiki/concepts/space-based-architecture]]

## Open questions / contradições contra o wiki

- **Skill `tech-mentor-backend` não cobre tuple spaces / modelo Linda.** O índice de `references/` da skill (distributed-systems.md, distributed-locking.md, brokers-comparison.md etc.) não tem entrada dedicada a espaços de coordenação/paradigma Linda — provável lacuna de referência a preencher futuramente, já que o padrão é o ancestral direto de [[wiki/concepts/space-based-architecture|space-based architecture]], hoje citado só de passagem em outras fontes da wiki.
- **Fronteira com [[wiki/concepts/distributed-lock|distributed lock]] em aberto.** O verbete afirma que a retirada (take) de uma tupla/objeto do espaço já provê exclusão mútua "de graça", sem lock explícito — vale contrastar formalmente com os mecanismos de [[wiki/concepts/distributed-lock|distributed lock]] (Redlock, advisory lock) já documentados na wiki: são a mesma garantia (mútua exclusão distribuída) obtida por primitivas radicalmente diferentes (remoção atômica vs. lease/lock explícito).
- **Verbete é curto e datado** (a maioria das fontes secundárias citadas é de 1999–2009); não cobre desenvolvimentos mais recentes de space-based architecture (ex.: GigaSpaces, Hazelcast) nem comparação direta com filas/streams modernos (Kafka, Redis Streams) — comparação fica registrada como lacuna, não como afirmação da fonte.

## Citações preservadas

> "A tuple space implements the associative memory paradigm for parallel/distributed computing. [...] This is also known as the 'blackboard metaphor' and may be thought of as a form of distributed shared memory."

> "Once an object is accessed, it is removed from the Object Space and replaced only after release. No other process can access an object while it is being used by one process."

> "[This] distributed systems dream would take 'a quantum leap in thinking.'" — Bill Joy
