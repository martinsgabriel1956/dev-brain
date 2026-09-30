---
type: concept
title: "Determinismo vs. Probabilismo em IA"
aliases: ["ferramenta certa para a tarefa ia", "analise semantica vs analise deterministica", "llm como juiz determinístico"]
date_created: 2026-07-27
date_updated: 2026-09-30
source_count: 3
tags: [determinismo, robustez-de-sistemas, tokenizacao, era-agentica, harness-de-qualidade]
skill: tech-mentor-ai
status: draft
---

# Determinismo vs. Probabilismo em IA

Distinção entre tarefas que toleram variação de resposta para o mesmo input (interpretação, resumo, análise semântica) e tarefas que exigem o mesmo output, sempre, para o mesmo input (cálculo de juros, validação de regra de negócio, folha de pagamento). LLMs são bons na primeira categoria e estruturalmente inadequados para a segunda, porque não leem conteúdo linha a linha — tokenizam e geram resposta por probabilidade (ver [[wiki/concepts/tokenizacao]]).

## A Falha Concreta que Expõe o Problema

[[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] documenta um caso de teste: um "validador inteligente" de tarefas de COBOL via LLM aprovava programas com variável não definida e reprovava programas corretos, de forma inconsistente entre execuções e entre modelos (ChatGPT, Claude, Gemini deram o mesmo diagnóstico ao ser questionados). Nenhum dos três conseguia nem identificar de forma confiável se um programa fonte estava em free format ou fixed format — uma checagem sintática trivial para um parser determinístico, mas sujeita a erro para um modelo que opera sobre probabilidade de tokens.

## Por Que Sistemas Corporativos Não Toleram Isso

Sistemas que calculam juros, impostos ou salário precisam gerar o mesmo output para o mesmo input hoje, amanhã e daqui a 5 anos — sem espaço para "quase certo". É por isso que são construídos com regras rígidas e comportamento previsível, não com julgamento de modelo. Ver [[wiki/concepts/robustez-de-sistemas]].

## Relação com Harness e Pipeline de Qualidade

O mesmo princípio já estava implícito em [[wiki/concepts/harness-de-qualidade]] e [[wiki/concepts/pipeline-de-qualidade]]: a IA gera, mas quem decide passa/não-passa é uma pipeline determinística, não o julgamento do modelo. [[wiki/concepts/rubrica-de-verificacao]] resolve o mesmo problema em contexto de agentes — o limite de tentativas de follow-up é definido por quem constrói o sistema, não pela LLM. A ferramenta certa para uma tarefa determinística continua sendo software tradicional (regras, parsers, pipelines); a IA entra como camada de interpretação sobre o resultado, não como substituta do processamento lógico.

## A Analogia da Ferramenta Errada

Usar um LLM para validação determinística é como usar um carro de corrida para arar um campo, ou uma chave de fenda para pregar um prego: o problema não é a ferramenta, é a tarefa que se espera dela.

## Aplicação à Esteira de CI/CD

[[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] aplica a distinção à esteira: código gera ações determinísticas e LLM gera saídas indeterminadas; por isso a execução de testes/gates/linters não deve depender de LLM, e a LLM entra na construção ou em verificações periódicas. Ver [[wiki/concepts/ia-na-esteira-ci-cd]].

## Reprodutibilidade de Prompt

[[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] busca "reproduzir exatamente" o comportamento de uma versão antiga registrando prompt, modelo e temperatura. Como o LLM é probabilístico, isso reduz mas não elimina a variação `[inferência]`; ver [[wiki/concepts/versionamento-de-prompt]].

## Key Sources

- [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]]
- [[wiki/sources/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes]] — determinismo aplicado à execução da esteira
- [[wiki/sources/versionamento-de-prompts-reprodutibilidade-rollback-metadados-golden-dataset]] — reprodutibilidade de prompt e seus limites
