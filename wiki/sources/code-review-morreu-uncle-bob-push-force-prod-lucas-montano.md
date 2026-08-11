---
type: source
title: "Code Review Morreu? Uncle Bob, Push Force pra Prod e Business × TI (Lucas Montano)"
aliases: ["code review morreu", "uncle bob não lê código lucas montano", "push force prod lucas montano"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [tech-mentor-ai, code-review, uncle-bob, quality-gate, agentes-ia, vibe-coding, bus-factor, harness-de-qualidade, push-to-prod, lucas-montano]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/code-review-morreu-uncle-bob-push-force-prod-lucas-montano.md
source_url:
author: Lucas Montano
date_published:
date_ingested: 2026-08-11
---

# Code Review Morreu? Uncle Bob, Push Force pra Prod e Business × TI (Lucas Montano)

## TL;DR

Vídeo de [[wiki/entities/lucas-montano]] sobre a repercussão do post de [[wiki/entities/uncle-bob]] afirmando que não lê mais nenhuma linha do código escrito por seus agentes — a produtividade só se aproveita submetendo o agente a restrições extremas (testes unitários, Gherkin, QA, métricas, mutation testing, cobertura). Montano se declara alinhado ("code review morreu quando começamos a produzir 10.000 linhas/dia") e revela sua própria prática de *push force* direto em produção via SSH+Claude Code na VPS. A tese central é uma **estratificação do code review por contexto organizacional**: em projeto solo, revisar cada linha da IA é red flag (sinal de pipeline sem quality gate); em time grande, review sobrevive não por desconfiança do código mas por **contexto** (arquitetura, padrões, requisitos) e pelo conflito estrutural entre *accountability* individual e *substituibilidade* que a empresa grande exige (ver [[wiki/concepts/bus-factor]]). Fecha com duas histórias-tese sobre o hype: o time comercial que vibe coda e "vira TI", e o Jira interno vibe-codado por um QA que foi revertido porque a manutenção consumia a capacidade do time.

## Key Claims

1. **Uncle Bob reafirma não ler nenhum código de seus agentes** — a "única maneira de aproveitar a produtividade deles" é submetê-los a restrições extremas (testes unitários, testes Gherkin, procedimentos de QA, métricas de qualidade, teste de mutação, cobertura) e confiar no que passa por todos os gates. Mesma posição já registrada em [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] e [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]], aqui via um post distinto (com treta pública com "Fernando" sobre estar *on call*).
2. **Uncle Bob programa desde o final dos anos 60** e enquadra o "não ler código" como decisão de quem tem muitos anos de plantão — ecoa "o direito de não ler código é conquistado, não copiado" de [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]]. Montano nota que os projetos no GitHub de Uncle Bob parecem *play projects* (ex.: "Missile Command dual platform"), o que baixa o risco de não ler código (nada crítico indo pra prod).
3. **Qualidade de código é mensurável, não subjetiva** — a defesa de Montano contra "o Senhor Código Limpo não se importa mais com qualidade": Uncle Bob "nunca falou sobre código, falou sobre *regras*" que se medem via quality gate no CD. Citação atribuída: *"Code quality still matters. It matters a lot. I verify it by using tools that measure."* Ver [[wiki/concepts/quality-gate]].
4. **O tempo economizado pela IA (~20x mais rápida) vai para escrever testes, não para revisar** — com 10.000 linhas geradas, não há como revisar tudo; a revisão linha a linha é substituída por unit/aceitação/QA. É o mesmo argumento de volume de [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] e do gargalo medido em [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]].
5. **Gergely Orosz observa o code review "desaparecendo"** — relata engenheiro sênior que revisava todo o código de IA e, após o lançamento do Fable, parou (exceto partes essenciais); "ainda não sei o que substituirá a revisão de código, pois algo precisa surgir no lugar dela". Montano discorda do "ainda não surgiu": os quality gates já são o substituto. Ver [[wiki/entities/gergely-orosz]].
6. **A revisão de código "morreu quando começamos a produzir 10.000 linhas/dia"** — tese explícita de Montano; a morte do review linha a linha é consequência mecânica do volume, não escolha ideológica.
7. **Montano faz *push force* direto em produção** — loga por SSH na VPS, roda [[wiki/entities/claude-code]] lá dentro e modifica direto em Prod (caso do SaaS Persoa); aceita downtime quando o custo de indisponibilidade é baixo. Contrasta com a disciplina de [[wiki/concepts/database-migration|migrations versionadas via PR]] documentada em [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — aqui é a prática oposta, assumida conscientemente para contexto de baixo risco.
8. **Em projeto solo, revisar cada linha da IA é uma red flag** — indica ausência de quality gate no pipeline; o *accountability* total já é do próprio dev, então o certo é pedir revisão à IA + testes E2E + orquestração de testes, não leitura linha a linha. Alinha com o [[wiki/concepts/harness-de-qualidade|harness de qualidade]] como substituto da leitura.
9. **Em time grande, o code review sobrevive por contexto, não por desconfiança** — Montano revisa PR no emprego para ter contexto de arquitetura, aderência a padrões do projeto e cobertura de requisitos, e testa localmente cada PR; o review vira "o QA dos próprios devs". Complementa a estratificação por [[wiki/concepts/matriz-risco-dificuldade-review-ia|risco × dificuldade]] de [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] com um eixo organizacional (porte da empresa).
10. **Accountability individual × substituibilidade é a tensão que decide o futuro do review** — responsabilizar cada dev pelo que coloca em prod funciona em empresa média, mas empresa grande recusa isso porque aumenta o [[wiki/concepts/bus-factor|bus factor]] e reduz substituibilidade; grande empresa quer processos, não heróis. Daí "várias verdades": review forte em time grande, opcional em time médio, dispensável em projeto solo.
11. **"TI não manda mais em TI; business manda em TI"** (Felipe Regazio, citado) — CEOs acham que a IA sabe mais de TI que o pessoal de TI; caso de uma empresa de 6 devs que demitiu metade porque o comercial vibe codou uma solução e o CEO se deslumbrou. Montano considera essas decisões equivocadas.
12. **Quem não é da área e vibe coda acaba virando TI** — sketch do freelancer ("você faz com IA e eu faço com IA, e a gente vê qual fica melhor") ilustra que software vibe-codado sempre precisa de melhorias; especializar o comercial em manter software é reinventar um time de TI. Só faz sentido substituir dev por IA quando o *supply* já está suprido (o gargalo virou vender, não produzir).
13. **A armadilha de manutenção do vibe code** — um QA (não-dev) vibe-codou um Jira interno melhor que Jira/Linear/Trello (março/2026); ~4 meses depois o time voltou ao Linear/Jira porque a manutenção da ferramenta interna consumia a capacidade de trabalho deles. Instância concreta dos limites de [[wiki/concepts/vibe-coding]] fora de MVP/protótipo.

## Entidades Mencionadas

- [[wiki/entities/lucas-montano]] — autor do vídeo; revela prática de push force em prod e a estratificação de review por porte de empresa.
- [[wiki/entities/uncle-bob]] — post que motiva o vídeo; treta pública com "Fernando"; anos-60 como origem da confiança no harness.
- [[wiki/entities/gergely-orosz]] — post sobre o code review "desaparecendo" e a pergunta em aberto do que o substitui.
- [[wiki/entities/hostinger]] — bloco patrocinado (plano KVM2, deploy de um clique de Claude Code/Codex CLI/N8N/Docker, cupom "Lucas Montano").
- [[wiki/entities/claude-code]] — ferramenta rodada por SSH direto na VPS para editar em produção.
- Fernando e Felipe Regazio — participantes da discussão no X (sem página própria; menções de Twitter).

## Conceitos Tocados

- [[wiki/concepts/code-review]]
- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/harness-de-qualidade]]
- [[wiki/concepts/teste-de-mutacao]]
- [[wiki/concepts/bus-factor]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/matriz-risco-dificuldade-review-ia]]
- [[wiki/concepts/paradoxo-da-aceleracao]]

## Open Questions

- Como as demais fontes sobre o mesmo tema, a transcrição **não cita URL nem data** dos posts de Uncle Bob, Gergely Orosz e Felipe Regazio — tratar citações textuais ("Code quality still matters...", frase sobre 20x) como reportadas, não verificadas contra a fonte primária. Mesma cautela já registrada em [[wiki/entities/uncle-bob]].
- Não fica claro se o post de Uncle Bob citado aqui é o mesmo das fontes anteriores ([[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]], [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]]) ou mais um post distinto na mesma janela — provavelmente um post posterior, dado o elemento novo (treta com "Fernando" sobre *on call*).
- As duas histórias-tese (empresa de 6 devs; Jira interno vibe-codado por QA) são relatos de segunda mão (mentoria no Stupid Button Club / rede social), sem verificação independente — tratar como anedota ilustrativa, não dado.
- A prática de *push force* direto em prod é apresentada como aceitável para contexto de baixo risco (SaaS pessoal, downtime tolerável); a própria wiki registra a disciplina oposta como padrão de indústria para código auditável ([[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]]) — contradição consciente, não erro.

## Raw Quotes

> "Minha estratégia atual é não ler nenhum código escrito por meus agentes. Essa é a única maneira de aproveitar a produtividade deles." — Uncle Bob (citado)

> "Code quality still matters. It matters a lot. I verify it by using tools that measure." — Uncle Bob (citado)

> "Ainda não sei o que substituirá a revisão de código, pois algo precisa surgir no lugar dela." — Gergely Orosz (citado)

> "A revisão de código morreu quando a gente começou a produzir 10.000 linhas de código por dia." — Lucas Montano

> "Se tu revisa cada linha que a IA está escrevendo, isso passa a ser uma red flag — significa que tu não colocou nenhum teste de qualidade no teu pipeline."

> "Uma grande empresa não quer isso, ela quer processos." (sobre accountability individual × substituibilidade)

> "TI não manda mais em TI. Business agora manda em TI, porque acha que a IA sabe mais de TI do que o pessoal de TI." — Felipe Regazio (citado)

> "Eles voltaram ao Linear/Jira porque a manutenção da ferramenta interna que desenvolveram com Vibe Code estava consumindo a capacidade de trabalho deles."
