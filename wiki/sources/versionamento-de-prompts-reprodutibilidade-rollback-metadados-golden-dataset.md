---
type: source
title: "Versionamento de Prompts: Reprodutibilidade, Metadados, Versionamento Semântico e Rollback Instantâneo"
aliases: []
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 0
tags: [prompt-versioning, llmops, reprodutibilidade, rollback, metadados, golden-dataset, regressao-de-prompt, agentes-ia, openrouter]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset.md
source_url: ""
author: "Não identificado (dev que constrói um assistente financeiro com agentes; repositório 'prompt manager')"
date_published: ""
date_ingested: 2026-09-30
---

## TL;DR

Vídeo PT-BR de um dev que largava versões de prompt esquecidas num bloco de notas e perdia o *porquê* de cada mudança. A solução foi **versionar o ecossistema do prompt**, não só a string: prompt + modelo + provedor + temperatura + autor + data + motivo da mudança ([[wiki/concepts/metadados-de-prompt]]). Sustenta-se em quatro pilares: rastreamento de metadados, [[wiki/concepts/versionamento-semantico-de-prompt]] (major/minor/correção), saber a versão ativa e [[wiki/concepts/rollback-de-prompt]] com um clique. O objetivo é a reprodutibilidade ([[wiki/concepts/versionamento-de-prompt]]). Ressalva: versionar **não melhora** a qualidade; para medir se uma versão é melhor, o autor aponta testes unitários/integração e [[wiki/concepts/teste-de-regressao-de-prompt]] sobre um [[wiki/concepts/golden-dataset]] (vídeo futuro). Demo com interface web local e um `metadata.json` que aponta a versão ativa, lido por um loader que monta o agente ([[wiki/concepts/prompt-registry-local]]).

## Key Claims

1. **Prompt esquecido em bloco de notas perde valor porque se perde o porquê da mudança.** O problema não é guardar o texto, é guardar a razão. *Evidência: relato pessoal.* → [[wiki/concepts/versionamento-de-prompt]]
2. **Uma palavra pode mudar o comportamento** ("assistente gentil" vs. "assistente muito gentil"), logo prompt merece o mesmo rigor que código. *Evidência: exemplo hipotético, sem medição.* → [[wiki/concepts/versionamento-de-prompt]], [[wiki/concepts/prompt-engineering]]
3. **Objetivo = reprodutibilidade**: voltar à versão 1 e obter a mesma execução, o que exige registrar as variáveis do entorno (modelo, temperatura), não só o texto. → [[wiki/concepts/versionamento-de-prompt]], [[wiki/concepts/metadados-de-prompt]]
4. **"Versionar prompt não é versionar string."** Versiona-se o ecossistema: variáveis + metadados (autor, temperatura, modelo, provedor, data, motivo). → [[wiki/concepts/metadados-de-prompt]]
5. **Versionamento semântico** distingue mudança *major* (reestrutura quase todo o prompt), *minor* (comportamento provavelmente igual) e correção simples. → [[wiki/concepts/versionamento-semantico-de-prompt]]
6. **É preciso saber sempre qual versão está ativa**, porque cada agente terá várias. → [[wiki/concepts/prompt-registry-local]]
7. **Rollback instantâneo** por um clique (ativar/depreciar versão): 2.0 falhou em produção, volta-se à 1.2.1. → [[wiki/concepts/rollback-de-prompt]]
8. **Versionar ≠ melhorar.** Qualidade depende das instruções, da estrutura e também das tools. → [[wiki/concepts/versionamento-de-prompt]]
9. **Avaliação**: testes unitários, de integração e golden test; regressão compara versão A vs. B (ex.: 1 vs. 1.2) contra respostas esperadas do golden dataset. *Evidência: só descrito, sem demo (vídeo futuro).* → [[wiki/concepts/teste-de-regressao-de-prompt]], [[wiki/concepts/golden-dataset]], [[wiki/concepts/llm-evals-testing]]
10. **Implementação demonstrada**: UI web local (criar à esquerda, gerenciar à direita); `metadata.json` guarda a versão ativa de cada prompt; cada versão é um JSON; diretório definido por variável de `.env`; *prompt loader* + *agent builder* leem o metadata (com refresh controlado) e criam o agente com prompt, modelo e temperatura da versão ativa. Modelos escolhidos por ID do OpenRouter, com presets; campo de "esforço" quando o modelo suporta. → [[wiki/concepts/prompt-registry-local]], [[wiki/entities/openrouter]]

## Entidades

- [[wiki/entities/openrouter]] — origem dos IDs de modelo no seletor da UI
- [[wiki/entities/google]] — Gemini como modelo de exemplo nos metadados

## Conceitos

- [[wiki/concepts/versionamento-de-prompt]]
- [[wiki/concepts/metadados-de-prompt]]
- [[wiki/concepts/versionamento-semantico-de-prompt]]
- [[wiki/concepts/rollback-de-prompt]]
- [[wiki/concepts/golden-dataset]]
- [[wiki/concepts/teste-de-regressao-de-prompt]]
- [[wiki/concepts/prompt-registry-local]]
- Já existentes tocados: [[wiki/concepts/prompt-engineering]], [[wiki/concepts/llm-evals-testing]], [[wiki/concepts/evals-llm]], [[wiki/concepts/llmops]], [[wiki/concepts/system-prompt-arquitetura]], [[wiki/concepts/hyperparameters-llm]], [[wiki/concepts/agente-ia]], [[wiki/concepts/determinismo-vs-probabilismo-em-ia]], [[wiki/concepts/drift-detection]], [[wiki/concepts/ci-cd]], [[wiki/concepts/feature-flag]], [[wiki/concepts/api-versioning]]

## Open Questions / Ressalvas

- **Reprodutibilidade parcial.** Registrar prompt+modelo+temperatura não garante o mesmo output: o próprio provedor pode atualizar o modelo sob o mesmo ID, e temperatura 0 não é determinismo estrito em todos os provedores `[external, não verificado aqui]`. A fonte não trata seed nem *model pinning* por snapshot. Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]].
- **Versionamento fica fora do ciclo de teste.** O autor separa versionar (controle) de testar (qualidade) e adia o segundo; sem gate de eval, o rollback é reativo (descobre-se em produção). Ver [[wiki/concepts/prompt-engineering]] (seção "Versionamento de Prompt Não É Só Git").
- **Escopo do controle.** Não fica claro se mudanças de *tools*, schema de saída ou RAG entram na versão; o autor só cita tools como fator de qualidade.
- **Alternativa Git.** A fonte usa arquivos JSON + `metadata.json` num registro próprio e não compara com Git/PR nem com registries prontos (LangSmith Hub, Langfuse Prompt Management) `[skill: tech-mentor-ai]`.
- **Regra de semver não definida.** O autor não diz o que qualifica major vs. minor; é julgamento do autor, não critério verificável.
- **Concorrência do refresh.** "Certo controle de tempo e atualização" do loader não é detalhado (TTL? *polling*?).
- Repositório "prompt manager" e o vídeo/workflow citados não foram acessados; nada aqui foi verificado no código.
- Sem contradição com a wiki; complementa e concretiza o ponto de [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] (versionamento como artefato com gate em CI/CD) e de [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] (evals por mudança de prompt).

## Citações que valem guardar

> "Versionar o prompt não significa versionar string."

> "Vamos tratar os nossos prompts com o mesmo respeito e o mesmo cuidado que a gente trata os nossos códigos."

> "O version não significa que as respostas vão melhorar."
