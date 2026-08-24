---
type: concept
title: "Tuple Space"
aliases: ["espaço de tuplas", "associative memory paradigm"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 1
tags: [sistemas-distribuidos, coordenacao, memoria-associativa, linda, javaspaces]
skill: tech-mentor-backend
status: stub
---

# Tuple Space

Repositório compartilhado de tuplas acessado concorrentemente: produtores publicam tuplas, consumidores as recuperam por **casamento de padrão** (não por endereço/chave exata). Implementa o paradigma de **memória associativa** para computação paralela/distribuída — também chamado de [[wiki/concepts/blackboard-metaphor|metáfora do quadro-negro]], uma forma de [[wiki/concepts/memoria-compartilhada-distribuida|memória compartilhada distribuída]].

Foi o embasamento teórico de [[wiki/concepts/linda-coordination-language|Linda]] (Yale, 1986). A implementação mais conhecida em produção é [[wiki/concepts/javaspaces|JavaSpaces]], e a generalização para objetos com comportamento é [[wiki/concepts/object-space|Object Space]].

## Por que importa

Desacopla produtor e consumidor tanto no **espaço** quanto no **tempo** — nenhum dos dois precisa conhecer o endereço do outro ou estar ativo simultaneamente. A retirada (take) de uma tupla do espaço é atômica e produz **exclusão mútua** sem precisar de um mecanismo de lock separado — ver [[wiki/concepts/distributed-lock|distributed lock]] para o contraste com locks explícitos (Redlock, advisory lock).

## Key sources

- [[wiki/sources/tuple-space-wikipedia]] — verbete da Wikipédia, definição canônica, origem em Linda, generalização Object Space, implementação JavaSpaces
