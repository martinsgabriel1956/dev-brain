---
type: source
title: "5 Princípios Que Me Mudaram Como Programador"
aliases: ["5 princípios que mudaram como programador", "boy scout rule programação", "faça a coisa mais simples que poderia funcionar"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 0
tags: [craftsmanship, principios, boy-scout-rule, yagni, otimizacao-prematura, extreme-programming, manutenibilidade]
skill: tech-mentor-leadership
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/5-principios-que-mudaram-como-programador.md"
source_url: ""
author: "desconhecido (vídeo YouTube, inglês)"
date_published: ""
date_ingested: "2026-07-09"
---

## TL;DR

Vídeo em inglês (traduzido) sobre por que devs ficam anos na área sem crescer: não internalizar princípios fundamentais de programação. Cobre cinco princípios práticos — Boy Scout Rule, evitar otimização prematura, escrever código para o mantenedor, YAGNI e "faça a coisa mais simples que poderia funcionar" (XP).

---

## Reivindicações Principais

**Claim:** A Boy Scout Rule (deixar o código um pouco mais limpo a cada mudança) é uma ferramenta contínua de combate à dívida técnica, popularizada por Uncle Bob.
**Evidência:** Exemplo dado — trocar um valor numa função e, ao perceber nomes de variável ruins, corrigi-los junto, mesmo não fazendo parte do escopo pedido.
**Confiança:** Alta — princípio amplamente citado na indústria (também presente em [[wiki/entities/uncle-bob]] e na literatura de Clean Code).

**Claim:** Otimização prematura desperdiça tempo em partes não-críticas do sistema; o problema não é otimizar, é otimizar sem saber o quê e quando.
**Evidência:** Citação de Donald Knuth ("premature optimization is the root of all evil"); exemplo de microsserviços para 100 usuários e cache para algo que não precisa.
**Confiança:** Alta — coincide integralmente com [[wiki/concepts/otimizacao-prematura]], já registrado na wiki via outra fonte.

**Claim:** Código deve ser escrito pensando em quem vai mantê-lo no futuro (inclusive o próprio autor), priorizando clareza sobre "só funcionar".
**Evidência:** Comparação entre duas implementações funcionalmente equivalentes, uma claramente mais legível — recomendação explícita de revisar isso antes de comitar código gerado por IA.
**Confiança:** Média — argumento qualitativo, sem exemplo de código incluído na transcrição original (removido na transcrição de áudio).

**Claim:** YAGNI — não construir hoje o que só *pode* ser necessário amanhã, porque a previsão raramente se confirma e a antecipação rouba tempo do que é necessário agora.
**Evidência:** Observação comportamental sobre devs que "predizem" necessidades futuras que nunca se concretizam.
**Confiança:** Alta — alinhado com [[wiki/concepts/yagni]], já bem documentado na wiki com origem em Kent Beck/XP.

**Claim:** "Faça a coisa mais simples que poderia possivelmente funcionar" — princípio da Extreme Programming: resolver com a solução mais simples válida agora, refatorando depois se necessário.
**Evidência:** Contraste com o hábito de tentar construir a solução "perfeita" desde o início, o que geralmente supercomplica o resultado.
**Confiança:** Alta — princípio clássico de XP (Kent Beck/Ward Cunningham), sobreposto mas distinto de [[wiki/concepts/kiss]].

---

## Os 5 Princípios

| # | Princípio | Ideia Central |
|---|---|---|
| 1 | Boy Scout Rule | Deixe o código um pouco mais limpo a cada mudança |
| 2 | Evite Otimização Prematura | Otimize o quê e quando importa, não tudo, sempre |
| 3 | Código para o Mantenedor | Escreva para quem vai entender e manter depois, não só para "funcionar" |
| 4 | YAGNI | Não construa o que você só *acha* que vai precisar |
| 5 | Faça a Coisa Mais Simples Que Poderia Funcionar | Resolva com a solução mais simples válida agora; refatore depois |

---

## Conceitos

- [[wiki/concepts/boy-scout-rule]]
- [[wiki/concepts/otimizacao-prematura]]
- [[wiki/concepts/codigo-para-o-mantenedor]]
- [[wiki/concepts/yagni]]
- [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]]
- [[wiki/concepts/kiss]]
- [[wiki/concepts/tech-debt-como-ferramenta]]

## Entidades

- [[wiki/entities/uncle-bob]]

## Questões em Aberto

- Autor do vídeo não identificado na transcrição (sem nome de canal, URL ou data).
- Transcrição é puramente falada (ASR), sem os exemplos de código mostrados na tela — o contraste de "código para o mantenedor" (duas implementações equivalentes) foi descrito mas não capturado literalmente.
- Autor menciona uma "segunda parte" com mais princípios — não ingerida (não publicada/disponível ainda).

## Raw Quotes

> "Leave the campground cleaner than you found it."

> "Premature optimization is the root of all evil." — citando Donald Knuth

> "You aren't going to need it."

> "Do the simplest thing that could possibly work."
