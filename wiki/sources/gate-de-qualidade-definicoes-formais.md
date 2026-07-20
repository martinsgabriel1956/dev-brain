---
type: source
title: "Gate de Qualidade — Definições da Literatura"
aliases: ["gate de qualidade definições", "quality gate definições formais"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 0
tags: [tech-mentor-testing, quality-gate, criterios-de-qualidade, ciclo-de-vida-de-software, milestone]
skill: tech-mentor-testing
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/gate-de-qualidade-definicoes-formais.md
source_url: ""
author: "Professora Simone (sobrenome e curso/canal não identificados)"
date_published: ""
date_ingested: 2026-07-19
---

# Gate de Qualidade — Definições da Literatura

## TL;DR

Vídeo curto (aula) percorrendo três definições formais de **Quality Gate** citadas na literatura de engenharia de software: (1) uma definição baseada em checklist formal, aprovação/aceitação por gate e comunicação a stakeholders; (2) uma definição que enquadra gates como milestones/pontos de decisão com critérios pré-definidos focados em qualidade; e (3) a definição de **Schneider**, que trata o gate como ponto de verificação de um conjunto de critérios de qualidade que precisam ser atendidos para avançar de uma etapa a outra do ciclo de vida. A partir dessas três, a fonte consolida características estruturais do conceito: exige critérios de entrada e saída bem definidos, é disparado por **critérios, não por datas**, produz um resultado **binário** (aprovado/reprovado), pode ocorrer tanto no ciclo de desenvolvimento quanto no ciclo de teste, e múltiplos gates podem correr **em paralelo** (ex.: um gate de qualidade de código e um gate de quantidade/severidade de defeitos abertos, avaliados simultaneamente por desenvolvedores diferentes).

## Key Claims

1. **Não existe uma definição única e "mais correta" de Quality Gate na literatura** — a fonte é explícita sobre isso antes de apresentar as três definições, o que orienta a leitura: são visões complementares, não concorrentes.
2. **Definição 1 (autor não identificado com confiança na transcrição, soa como "Puxava")** — quality gates são listas de verificação formais usadas ao longo da vida de um projeto; em cada gate ocorre aprovação formal e aceitação; existe uma avaliação da qualidade e integridade do produto; as informações da avaliação são publicadas aos stakeholders corretos.
3. **Definição 2 (autor não identificado com confiança na transcrição, soa como "Adultos")** — quality gates são milestones e pontos de decisão com critérios pré-definidos e focados na qualidade.
4. **Definição 3 — Schneider** — um quality gate é um ponto de verificação onde um conjunto de critérios de qualidade pré-definidos deve ser atendido para que o processo avance de uma etapa para outra em seu ciclo de vida; nessa visão, o gate cumpre o papel de milestone através de regras que atendem a padrões de qualidade pré-definidos.
5. **Quality gate exige critérios de entrada e de saída definidos explicitamente** — sem esses critérios, não há como avaliar objetivamente se o gate foi ou não atingido.
6. **Gates podem existir tanto no ciclo de desenvolvimento quanto no ciclo de teste** — não é um conceito exclusivo de uma fase específica do processo de software.
7. **O critério de disparo de um gate é a satisfação de critérios, não uma data no calendário** — um quality gate é atingido quando os critérios definidos são cumpridos, independente de prazo.
8. **A avaliação em um quality gate é binária: aprovado ou reprovado** — não há estado intermediário; isso ocorre ao longo do ciclo de teste de software.
9. **Múltiplos quality gates podem rodar em paralelo, avaliados por pessoas diferentes** — exemplo dado na fonte: um desenvolvedor trabalha em um gate que avalia a qualidade do código, enquanto outro desenvolvedor trabalha em um gate distinto que avalia se a quantidade e a severidade dos defeitos abertos atendem ao critério de aprovação para produção. Os dois gates são independentes e simultâneos.

## Entidades Mencionadas

- Nenhuma entidade da wiki recebeu página própria a partir desta fonte — ver Open Questions sobre os dois autores não identificados com confiança e sobre a autora do vídeo (Professora Simone).

## Conceitos Tocados

- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/pipeline-de-qualidade]]

## Open Questions

- **Dois dos três autores citados não foram identificados com confiança** — a transcrição automática capturou os nomes como "Puxava" e "Adultos", que não correspondem a sobrenomes plausíveis de autores de engenharia de software; ambos foram mantidos literalmente no `raw/` e citados como "[nome incerto]" nesta página e em [[wiki/concepts/quality-gate]], sem criação de entidade própria, seguindo o mesmo precedente já registrado em [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] para nomes distorcidos por ASR (ex.: "Miture JS"/"mito").
- **"Schneider" é o único nome citado com clareza na transcrição**, mas sem nome completo, obra ou ano — não é possível confirmar com segurança se se refere a um autor específico e amplamente citado em engenharia de qualidade de software (ex.: Kurt Schneider) ou a outro "Schneider" do campo. Nenhuma entidade foi criada para evitar atribuição incorreta.
- **Autora do vídeo ("professora Simone") não recebeu página de entidade** — apenas o primeiro nome está disponível na transcrição, sem sobrenome, curso ou canal identificáveis; baixa relevância para justificar uma entidade própria com informação tão incompleta.
- Esta fonte é puramente conceitual/acadêmica (definições da literatura) — não traz exemplos práticos de ferramentas ou pipelines, o que a torna complementar (não sobreposta) a [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] e às fontes já citadas em [[wiki/concepts/pipeline-de-qualidade]], que cobrem o lado prático/ferramental do mesmo conceito.

## Raw Quotes

> "Ao longo dos anos, muitas definições sobre Gates de qualidade foram propostas, e não existe uma única mais correta ou definição de como ele deve ser estruturado."

> "[Schneider] comenta: ponto de verificação onde um conjunto de critérios de qualidade pré-definidos devem ser atendidos para seguir de uma etapa para outra em seu ciclo de vida."

> "Esses gates existem critérios para atingi-los, não necessariamente datas, e sim critérios — pontos de verificação que garantem que o software vai passar por todas as fases que são definidas."

> "Gates de qualidade são critérios binários: ou aprovados ou não aprovados."

> "Podemos ter um desenvolvedor que esteja trabalhando com o gate para atender a qualidade do código, enquanto tem um outro desenvolvedor que tá trabalhando com outro gate que determina se a quantidade de defeito e até mesmo a severidade dos defeitos que estão abertos atende o critério de aprovação desse código para produção."
