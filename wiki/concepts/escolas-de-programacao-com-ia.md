---
type: concept
title: "As 5 Escolas de Programação com IA"
aliases: ["escolas de ia", "5 escolas de programacao com ia", "escolas de pensamento sobre ia para devs"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [vibe-coding, spec-driven-development, agentes-ia, autonomy-slider, harness, carreira]
skill: tech-mentor-ai
status: draft
---

# As 5 Escolas de Programação com IA

Taxonomia proposta em [[wiki/sources/cinco-escolas-programacao-com-ia]] para organizar as posições conflitantes da comunidade sobre como programar com IA, mapeadas ao longo do [[wiki/concepts/autonomy-slider|autonomy slider]] de [[wiki/entities/andrej-karpathy]].

## As Cinco Escolas

| # | Escola | Posição no slider | Ferramentas/Defensores citados |
|---|---|---|---|
| 1 | **Copiloto** — "você dirige" | Mínima autonomia | Cursor, GitHub Copilot |
| 2 | **Delegação total a agentes** | Alta autonomia | Claude Code, AMP ([[wiki/entities/thorsten-ball]]), [[wiki/entities/steve-yegge]] |
| 2b | *Variante:* Spec-Driven Development | Alta autonomia, com contrato prévio | [[wiki/entities/sean-grove]], [[wiki/concepts/spec-driven-development]] |
| 3 | **"Na unha"** — sem IA | Zero autonomia | [[wiki/entities/peter-naur]] (base teórica), quase sem defensores contemporâneos ativos |
| 4 | **O Loop** — sem supervisão | Máxima autonomia | Ralph Loop / "Half Wigun" ([[wiki/entities/geoffrey-huntley]]) |

*(Não há uma "Escola 5" nomeada isoladamente na fonte — o vídeo é titulado "5 escolas" contando a variante spec-driven como desdobramento da Escola 2, mas a tabela acima reflete os quatro polos claramente distintos descritos.)*

## A Tese Central: Nenhuma Escola é "A Certa"

O argumento organizador não é ranquear as escolas, mas mostrar que cada uma ocupa um ponto legítimo do mesmo eixo — e que **os próprios fundadores mudam de posição com o tempo**. Dois casos citados como prova: [[wiki/entities/dhh]] e [[wiki/entities/antirez]], que defendiam publicamente a Escola 3 ("na unha") e migraram para a Escola 2 (delegação total) em menos de 12 meses.

## Escola 3 é a "Órfã" da Taxonomia

A fonte observa que a Escola 3 — apesar de ser, na visão do autor, a mais teoricamente coerente (fundamentada em [[wiki/concepts/teoria-do-programa-naur]]) — está sendo abandonada: seu principal fundamento teórico ([[wiki/entities/peter-naur]]) morreu em 2016, antes do boom de LLMs agênticos, e seus defensores contemporâneos mais visíveis migraram de lado. Não há mais ninguém defendendo a posição "pura" de forma consistente e pública.

## Distinção Que Atravessa Todas as Escolas: Automatic Programming vs. Vibe Coding

Independentemente de qual escola um dev ocupa no slider, [[wiki/entities/antirez]] propõe (ao migrar da Escola 3 para a 2) uma distinção que vale para qualquer ponto do eixo:

- Usar um agente **com direção e critério de qualidade** — automatic programming, o código continua sendo seu.
- Aceitar o que a máquina produz **sem entender** — [[wiki/concepts/vibe-coding|vibe coding]], você vira "despachante de código".

Ou seja: a escola escolhida (quanto delegar) é ortogonal à disciplina aplicada (se você entende o que foi produzido). É possível fazer vibe coding na Escola 1 (aceitar toda sugestão do Copilot sem ler) e é possível fazer automatic programming na Escola 4 (loop sem supervisão em tempo real, mas com critérios de verificação e testes bem definidos que você entende).

## Relação com Outros Frameworks de Categorização de Adoção de IA

- [[wiki/concepts/niveis-adocao-ia-l0-l4]] — outra tentativa de categorizar posições de adoção de IA, em níveis discretos (L0 negacionista a L4+ fábrica) em vez de "escolas" com nomes próprios; os dois frameworks descrevem fenômenos sobrepostos com vocabulário diferente e sem terem sido cruzados diretamente por nenhuma fonte ainda.
- [[wiki/concepts/loop-engineering]] — a Escola 4 desta taxonomia é, na prática, o mesmo fenômeno já documentado em profundidade nesta wiki (Ralph Loop, quatro níveis oficiais de loop da Anthropic).

## Key Sources

- [[wiki/sources/cinco-escolas-programacao-com-ia]]
