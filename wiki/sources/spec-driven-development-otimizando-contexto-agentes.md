---
type: source
title: "Spec-Driven Development: Otimizando o Contexto para Agentes de Código"
aliases: ["SPC driven development", "TLC Spec Driven", "spec driven contexto"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/spec-driven-development-otimizando-contexto-agentes.md
source_url: ""
author: "Provavelmente Valdemar Neto (Tech Leads Club) — não confirmado por nome na fala, inferido por menção ao workshop e à skill TLC Spec Driven"
date_published: null
date_ingested: 2026-08-03
source_count: 0
tags: [spec-driven, rpi-workflow, context-engineering, subagentes, janela-de-contexto, ia-para-devs, harness]
skill: tech-mentor-ai
status: stable
---

# Spec-Driven Development: Otimizando o Contexto para Agentes de Código

## TL;DR

Transcrição de vídeo (autor provavelmente [[wiki/entities/valdemar-neto]], Tech Leads Club — não confirmado por nome na fala) que amarra explicitamente dois padrões já documentados na wiki — [[wiki/concepts/rpi-workflow|RPI]] e [[wiki/concepts/spec-driven-development|Spec-Driven Development]] — como a mesma resposta a um único problema: janelas de contexto maiores aumentam a chance de alucinação, então o objetivo é manter o uso próximo de ~200k tokens mesmo em mudanças grandes (exemplo dado: feature de recomendações tocando ~90 arquivos). A fonte detalha, com exemplo prático de uma skill chamada "TLC Spec Driven", os quatro artefatos do fluxo — spec (specify), design (opcional), tasks (breakdown com dependências e paralelizável vs. sequencial) e execução — e mostra a fase de execução usando **quatro subagentes em paralelo**, cada um cobrindo um subconjunto de tasks, além de um arquivo de **"estado"** que registra decisões tomadas pelo agente durante a implementação para permitir continuidade entre sessões/janelas de contexto.

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Quanto maior a proporção da janela de contexto ocupada, maior a chance de alucinação — daí a recomendação prática de manter o uso em torno de ~200k tokens mesmo com janelas de até 1M disponíveis | Afirmação direta do autor, alinhada com o que já está documentado em [[wiki/concepts/janela-de-contexto]] e [[wiki/concepts/dumb-zone]] | Média-alta — é uma heurística de campo, não uma medição formal citada na fonte |
| Um plano único (ex.: `/plan` a partir de um PRD grande) não é adequado para projetos que tocam dezenas de arquivos, porque a funcionalidade de "plano" das ferramentas atuais é desenhada para uma tarefa bem definida, não para decompor um projeto inteiro em ordem de dependência e paralelismo | Comparação direta entre pedir um plano a partir de um PRD grande vs. usar spec-driven com breakdown de tasks | Alta — consistente com a distinção já registrada em [[wiki/concepts/spec-driven-development]] entre "tarefas menores → Plan Mode" e "features complexas → SDD" |
| A fase de research deve ser salva em Markdown antes de prosseguir para não obrigar a fase de implementação a herdar uma janela de contexto já poluída pela pesquisa | Explicação do fluxo Research → Plan → Implement, incluindo a ressalva de que implementar a partir da janela de research "não dá" para mudanças de 90 arquivos | Alta — mesma tese central de [[wiki/concepts/memoria-de-longo-prazo-ia]] |
| Cada task no breakdown deve conter: o que fazer, onde fazer, o que reusar, de quais tasks é pré-requisito, e uma definition of done — o suficiente para o agente executar sem precisar repetir a fase de research | Estrutura de tasks descrita e mostrada em captura de tela (não visível na transcrição, mas descrita verbalmente) | Alta — consistente com o formato de task já descrito em [[wiki/concepts/tech-spec]] |
| Na execução, o agente identifica autonomamente quais tasks do breakdown podem rodar em paralelo e despacha múltiplos subagentes (4, no exemplo) simultaneamente, cada um resolvendo um subconjunto de tasks | Relato de execução real de um projeto, com prompt explícito incentivando uso de subagentes | Alta — reforça o "Padrão Orquestrador" e o disparo automático de subagentes já documentados em [[wiki/concepts/subagentes]] |
| Um projeto spec-driven gera, além da spec/design/tasks, um artefato de "estado" que registra decisões importantes tomadas durante a implementação, permitindo abrir uma nova janela de contexto e retomar o trabalho de onde parou, inclusive fatiando o projeto em múltiplos PRs | Explicação do autor sobre o propósito do arquivo de estado | Média-alta — o mecanismo é plausível e alinhado com [[wiki/concepts/memoria-de-longo-prazo-ia]], mas a fonte não mostra o conteúdo real do arquivo, só descreve seu papel |
| A fase de planejamento e a fase de implementação devem rodar em janelas de contexto separadas (nova sessão/`/clear` entre elas) | Prática aplicada no exemplo do autor — pesquisa/planejamento numa janela, implementação em outra, explicitamente justificada como reforço de um princípio já usado em vídeos anteriores do mesmo autor | Alta — idêntico ao passo "Limpeza de Contexto" já documentado em [[wiki/concepts/spec-driven-development]] |

## Conceitos Abordados

- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/rpi-workflow]]
- [[wiki/concepts/janela-de-contexto]]
- [[wiki/concepts/subagentes]]
- [[wiki/concepts/memoria-de-longo-prazo-ia]]
- [[wiki/concepts/prd-product-requirements-document]]
- [[wiki/concepts/tech-spec]]
- [[wiki/concepts/worktree-paralelismo]]

## Entidades Abordadas

- [[wiki/entities/valdemar-neto]]

## Observações / Contradições

Nenhuma contradição com o que já está registrado na wiki — esta fonte funciona como uma **segunda confirmação em campo**, com exemplo concreto (feature de recomendações, ~90 arquivos, 4 subagentes em paralelo), do mesmo modelo mental já sintetizado em [[wiki/concepts/rpi-workflow]] (que cita explicitamente a relação entre RPI e SDD como "mesma família, foco diferente") e em [[wiki/concepts/spec-driven-development]]. O ponto novo mais concreto é o artefato de **"estado"** como registro de decisões pós-implementação para continuidade entre janelas — distinto de "memória de longo prazo" (que salva o *research*, antes da implementação): aqui o que é salvo são decisões tomadas *durante* a implementação. Vale registrar como nuance, não contradição.

A skill demonstrada ("TLC Spec Driven", atribuída à Tech Leads Club e a "Felipe Rodrigues") e o "Spec Kit do GitHub" são citados como duas implementações concretas do mesmo padrão — nenhuma das duas tem página própria na wiki; ambas mencionadas aqui como ferramentas, não como entidades centrais da fonte.

## Atualização Posterior: Benchmark de Granularidade de Subagentes

[[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]], ingerida depois, refina o Cenário 4/Execute descrito acima ("quatro subagentes em paralelo a partir do breakdown de tasks"): um benchmark de campo posterior, sobre a mesma skill TLC Spec Driven, mostra que a quantidade de subagentes usada na execução importa tanto quanto decidir se paraleliza — um subagente por task piora tempo, custo e qualidade ao mesmo tempo frente a não usar subagente nenhum, enquanto agrupar tasks relacionadas em poucos subagentes coesos (3, no caso testado) iguala ou supera o desempenho de um agente único. A skill teria evoluído de granularidade por task para agrupamento por fase como resultado direto desse achado.

## Perguntas Abertas

- Autor não confirmado por nome completo/canal na transcrição fornecida — atribuição a Valdemar Neto é inferência por contexto (menção ao workshop "Desenvolvimento Assistido por IA Avançado" e à skill "TLC Spec Driven" da Tech Leads Club, mesma organização já registrada na página de Valdemar Neto).
- A fonte não detalha o formato exato do arquivo de "estado" (schema, onde fica, como é atualizado) — fica em aberto comparar com o mecanismo real de memória de longo prazo já documentado.

## Raw Quotes

> "O que separa um resultado mais ou menos que tu tem um sistema completo e funcional é o contexto que tu dá."

> "Quanto maior a janela de contexto, mais chance de alucinar tem."

> "A gente termina a fase de research, salva tudo que a gente aprendeu em arquivos Markdown — assim a gente pode pegar esses arquivos Markdown, que já tem todo o resultado da pesquisa, e começar a desenvolver em cima deles, sem precisar gastar mais tokens pesquisando no futuro."

> "Isso aqui é que nem um plano — tem todo o contexto que a IA precisa para escrever esse bloco de código, ela não precisa fazer uma nova pesquisa."

> "O estado vai guardando decisões importantes que o agente criou durante a implementação [...] a gente pode simplesmente abrir outra janela, começar o projeto da onde tava, dizer 'continua o projeto tal', e ele vai funcionar."
