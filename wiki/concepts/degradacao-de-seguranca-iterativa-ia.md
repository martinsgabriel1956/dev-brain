---
type: concept
title: "Degradação de Segurança em Geração Iterativa com IA"
aliases: ["security degradation iterative ai code generation", "degradação de segurança iterativa", "refinamento piora segurança"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 1
tags: [seguranca, ai-assisted-engineering, sast, code-review, vulnerabilidade, refinamento-iterativo]
skill: tech-mentor-ai
status: draft
---

# Degradação de Segurança em Geração Iterativa com IA

Achado contraintuitivo: pedir para uma IA **refinar/melhorar** um código repetidamente não melhora monotonicamente a segurança dele — pelo contrário, tende a piorar depois de poucas rodadas. Isso quebra a suposição implícita de que "mais iteração = mais qualidade", pelo menos na dimensão de segurança.

## O Achado

[[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] cita um paper (arXiv, "Security Degradation in Iterative AI Code Generation") que testou 400 amostras de código ao longo de 40 rodadas de refinamento, com 4 estratégias de prompt diferentes, medindo vulnerabilidades a cada passo via análise estática. Resultado: **+37,6% de vulnerabilidades críticas depois de apenas 5 interações**. Mesmo a estratégia de prompt que pedia explicitamente foco em segurança a cada rodada degradou depois de uma melhora inicial — não existe um prompt que blinde contra esse efeito.

Isso é diferente — mas complementar — do dado de base de que código gerado por IA já nasce com mais falhas de segurança que código humano (~2,77x, segundo CodeRabbit e Veracode, citados na mesma fonte): a degradação iterativa é um efeito *adicional*, que se acumula rodada a rodada em cima desse ponto de partida já mais vulnerável.

## Por que acontece (três mecanismos)

1. **Ausência de memória de contexto de segurança entre rodadas.** O modelo opera sobre o código presente, sem histórico explícito de qual vulnerabilidade foi introduzida ou corrigida em qual rodada anterior.
2. **Refactors deslocam a lógica de validação.** "Limpar" o código pode mover, remover silenciosamente ou alterar o comportamento de uma checagem de segurança, sem que isso seja visível na superfície do diff.
3. **Testes funcionais continuam passando.** A suíte de testes padrão cobre o happy path, não o edge case adversarial — então a regressão de segurança não é pega pelo próprio processo de verificação que os times já têm.

## Relação com outros conceitos

- [[wiki/concepts/degradacao-de-contexto]] — mecanismo próximo mas distinto: a degradação de contexto é sobre perda de atenção dentro de uma janela de contexto muito preenchida; a degradação de segurança iterativa pode ocorrer mesmo sem janela de contexto longa, pela simples falta de memória persistente de decisões de segurança entre rodadas de refinamento. A fonte não deixa claro se as 40 rodadas do paper ocorreram numa única sessão longa (o que aproximaria os dois mecanismos) ou em chamadas independentes — ver open question na página de source.
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] — este achado é evidência quantitativa concreta para o argumento mais geral de que código gerado por IA exige julgamento e revisão humana contínuos, não pontuais.
- [[wiki/concepts/sast]] — a mitigação proposta pela fonte depende de rodar SAST no *delta* a cada modificação, não só uma vez no fim.
- [[wiki/concepts/shift-left-testing]] — a recomendação de escrever testes de segurança antes de iterar é uma aplicação direta de shift-left à dimensão específica de refinamento assistido por IA.

## Mitigação Proposta (Processo)

A fonte propõe tratar security review como **checkpoint entre rodadas de iteração**, não como fase final:

1. SAST antes e depois de cada modificação, revisando o delta do relatório.
2. Limite explícito de número de iterações antes de forçar revisão manual (o paper sugere que 5 já é o suficiente para acumular dano significativo).
3. Testes de segurança escritos antes de iterar, como contrato.
4. Revisão de segurança feita em contexto/chat novo — sem o histórico de quem gerou o código — sob a hipótese de que um modelo "sem memória de autoria" tende a ser mais crítico.
5. Mudança de expectativa: cada rodada de refinamento tem custo (inclusive de segurança), não é melhoria estritamente monotônica.

## Key Sources

- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]]
