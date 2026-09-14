---
type: concept
title: "Ataque de Destilação vs. Ataque de Anomalia (Extração de Dados via LLM)"
aliases: ["ataque de destilação", "ataque de anomalia llm", "model extraction attack", "extração de dados via agente ia"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [seguranca, ia, destilacao, engenharia-reversa, agente-ia, deteccao-de-anomalia]
skill: tech-mentor-ai
status: stub
---

# Ataque de Destilação vs. Ataque de Anomalia (Extração de Dados via LLM)

Distinção entre dois objetivos diferentes de ataque contra uma LLM exposta publicamente, que são frequentemente confundidos sob o mesmo rótulo de "risco de destilação":

## Ataque de Destilação (comportamento do modelo)

Objetivo: extrair **como o modelo responde** — seu comportamento, padrões de treino — para treinar um modelo próprio mais barato que imita as respostas do alvo (destilação de conhecimento aplicada de forma não autorizada/adversarial). Caso público citado como emblemático: ataque atribuído à [[wiki/entities/alibaba|Alibaba]] contra a [[wiki/entities/openai|OpenAI]], usando cerca de 25 mil contas falsas e um volume muito alto de interações (número exato não confirmado nesta fonte — ver open question em [[wiki/sources/ia-nao-vai-substituir-desenvolvedor-2026-governanca-seguranca]]).

Esse tipo de ataque exige **escala** — muitas contas, muitas interações — porque o objetivo é reconstruir estatisticamente o comportamento geral do modelo.

## Ataque de Anomalia (extração de dados expostos ao agente)

Objetivo diferente e mais barato para o atacante: não destilar o modelo, mas **extrair dados que a empresa expôs para o agente** — conhecimento proprietário, regras de negócio, dados de contexto injetados via prompt/RAG. Para isso, o atacante não precisa de milhões de interações: **5-6 interações bem desenhadas** podem bastar para fazer [[wiki/concepts/engenharia-reversa|engenharia reversa]] do comportamento do agente e extrair informação que o modelo nunca deveria revelar.

Risco comum de má-percepção: como o caso público de referência (Alibaba/OpenAI) usa escala massiva, times de segurança tendem a achar que esse tipo de risco está distante da realidade de uma empresa comum — subestimando a variante de baixo volume focada em extração de dados, não em replicar o modelo.

## O Problema de Detecção

Segundo a fonte, hoje ainda é difícil para uma empresa perceber, na prática, que está sofrendo esse tipo de ataque através de uma LLM exposta via agente — não há, nesta fonte, um mecanismo de detecção descrito (ex.: rate limiting, análise de padrão de prompt, DLP na saída do agente). O nome usado pelo autor para esse processo de vigilância é "verificação de comportamento anômalo".

## Relação com outros conceitos

- [[wiki/concepts/engenharia-reversa]] — mecanismo usado no ataque de anomalia: reconstruir, a partir de poucas respostas, informação que o sistema não deveria revelar
- [[wiki/concepts/agent-containment]] — controle de superfície de exposição de um agente é a mitigação estrutural mais próxima para reduzir a superfície de extração de dados

## Key Sources

- [[wiki/sources/ia-nao-vai-substituir-desenvolvedor-2026-governanca-seguranca]] — origem da distinção entre os dois tipos de ataque e do caso Alibaba/OpenAI citado de memória
