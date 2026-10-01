---
type: concept
title: "Partição como pré-condição do CAP"
aliases: ["P é fixo no CAP", "tolerância a partição não é opcional", "CA não existe em sistema distribuído", "erro do triângulo CAP"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 2
tags: [system-design, cap-theorem, sistemas-distribuidos, particao-de-rede, entrevistas]
skill: tech-mentor-system-design
status: draft
---

# Partição como pré-condição do CAP

O [[wiki/concepts/cap-theorem]] costuma ser ensinado como um triângulo "escolha 2 de 3" (CP, CA, AP). Esta página registra a leitura mais precisa: **P não é uma das três cartas, é o que dá origem ao jogo**.

## Argumento

1. Num sistema distribuído, nós se comunicam por rede, e a rede pode falhar (ver [[wiki/concepts/falacias-da-computacao-distribuida]]).
2. **Partição** = falha de comunicação **entre os nós**. Não significa "ter muitos servidores".
3. Enquanto a rede está de pé, o sistema pode entregar C e A juntas; **não há dilema**.
4. Quando a partição acontece, o nó que não consegue falar com os outros precisa decidir: responder com o que tem (A, talvez desatualizado) ou recusar (C).
5. Logo o P é **o gatilho**; a escolha real é **C vs. A, condicionada à ocorrência de P**. Não dá para "escolher não ter P" num sistema distribuído.

## E o "CA"?

Só faz sentido num sistema de **nó único** (um servidor, um banco, sem replicação), onde não há rede interna para particionar. Ele não é distribuído, então o CAP não se aplica, e por isso não aparece em entrevista de system design. Materiais que classificam produtos como "CA" (ver [[wiki/sources/sgbd-conceitos-fundamentais-questoes-concurso]]) estão simplificando; ver a ressalva em [[wiki/concepts/cap-theorem]].

## Relação com outras páginas

- Custo no dia a dia, sem partição: [[wiki/concepts/pacelc]] (latência vs. consistência).
- Definição formal do lado A: [[wiki/concepts/disponibilidade-no-teorema-cap]].
- Escolha por serviço, não global: [[wiki/concepts/cap-por-servico]].

[external] O próprio Eric Brewer reconhece que "2 of 3" "was always misleading" e que o CAP proíbe apenas "perfect availability and consistency in the presence of partitions, which are rare" ([[wiki/entities/eric-brewer]]).

## Key sources

- [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]] — formulação "P é a pré-condição que ativa a escolha entre C e A"
- [[wiki/sources/cap-theorem]] — mesma conclusão ("CA só existe em single-node")
- [[wiki/sources/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato]] — mesma tese por outro caminho: P é intrínseco e não pode ser "desligado"
