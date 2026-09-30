---
type: concept
title: "Versionamento de Prompt"
aliases: ["prompt versioning", "versionar prompts", "reprodutibilidade de prompt"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [prompt-versioning, llmops, reprodutibilidade, rastreabilidade]
skill: tech-mentor-ai
status: draft
---

# Versionamento de Prompt

Prática de registrar cada versão de um prompt de agente de forma que se possa **rastrear** o que mudou e **reproduzir** o comportamento de uma versão antiga. Motivação da fonte: prompts colados em bloco de notas perdem o *porquê* da mudança e viram lixo ([[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]).

## Ideia central

- **Prompt é código**: uma palavra a mais ("muito gentil") pode mudar a resposta, então merece o mesmo cuidado.
- **Objetivo é reprodutibilidade**: poder "voltar no tempo" para a versão 1 e obter a mesma execução. Isso só é possível se as variáveis do entorno (modelo, temperatura, provedor) forem guardadas junto — ver [[wiki/concepts/metadados-de-prompt]].
- **Não é versionar string**: versiona-se o ecossistema do prompt (texto + metadados + motivo).
- **Quatro pilares** (segundo a fonte): rastreamento de metadados, [[wiki/concepts/versionamento-semantico-de-prompt]], saber a versão ativa ([[wiki/concepts/prompt-registry-local]]) e [[wiki/concepts/rollback-de-prompt]].

## O que versionar NÃO faz

Versionar dá controle, **não qualidade**: se o prompt melhora depende das instruções, da estrutura e das tools. Para medir, é preciso [[wiki/concepts/teste-de-regressao-de-prompt]] sobre um [[wiki/concepts/golden-dataset]]. Ver também o gate de CI/CD em [[wiki/concepts/prompt-engineering]].

## Limites da reprodutibilidade

Mesmo com tudo registrado, o output pode variar (não determinismo do LLM, modelo atualizado pelo provedor sob o mesmo ID). Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]. `[external]` a fonte não trata seed nem snapshot de modelo.

## Relação com outros conceitos

- [[wiki/concepts/llmops]] — prompt versioning é parte do ciclo operacional
- [[wiki/concepts/llm-evals-testing]] — a validação de cada versão
- [[wiki/concepts/hyperparameters-llm]] — temperatura é uma das variáveis a registrar
- [[wiki/concepts/feature-flag]] — mecanismo análogo de ativar/desativar versões sem redeploy

## Key sources

- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]]
