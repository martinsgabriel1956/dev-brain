---
type: concept
title: "Economia da Descoberta Automatizada de Vulnerabilidades"
aliases: ["custo por vulnerabilidade encontrada", "esteira de agentes de pentest", "triagem de falso positivo em pentest com ia"]
date_created: 2026-08-27
date_updated: 2026-08-27
source_count: 1
tags: [pentest, ai-red-teaming, economia-da-automacao, falsos-positivos, human-in-the-loop]
skill: tech-mentor-security
status: stub
---

# Economia da Descoberta Automatizada de Vulnerabilidades

Quando um pipeline de agentes de IA testa uma aplicação, ele explora combinações de parâmetros de forma exaustiva e sistemática, sem o custo marginal de paciência que limita um pentester humano (cuja hora é cara e cuja cobertura tende a ser amostral, não exaustiva). Isso derruba o **custo por vulnerabilidade encontrada** — e quando o custo de uma atividade despenca, o mercado dessa atividade muda.

## O trade-off: mais achados reais, mas também mais ruído

A mesma exaustividade que encontra falhas que humanos perdem (ex.: um [[wiki/concepts/idor|IDOR]] que passou por dois pentests manuais aprovados) também gera um volume alto de falsos positivos — alarmes apontando para problemas que não existem. [[wiki/sources/pipeline-agentes-ia-pentest-idor-critica-nao-substitui]] registra que os próprios autores do estudo citado admitem que **a validação humana virou o gargalo do processo**: cada falso positivo precisa de um humano para investigar e descartar. O fôlego do agente é infinito; o critério continua sendo escasso.

## Onde o valor migra

A conclusão prática é a mesma tese de [[wiki/concepts/engenheiro-vs-programador]] aplicada ao domínio de segurança ofensiva: o trabalho que ganha valor não é mais *executar* o teste (isso vira commodity, barato, delegável a uma esteira de agentes), mas **projetar a esteira** — escolher os agentes certos, definir os papéis de cada um, calibrar em que ponto o humano precisa validar, e decidir o que é sinal contra o que é ruído. Isso exige *mais* conhecimento de segurança para supervisionar bem, não menos — auditar um pipeline sem entender profundamente o domínio é, na formulação da fonte, "assinar um relatório no escuro".

## Relação com HITL

Este é um caso concreto do padrão geral documentado em [[wiki/concepts/human-in-the-loop]]: o agente não decide sozinho o que é achado real — o humano intervém no ponto de triagem/validação. A diferença em relação aos outros exemplos já registrados em HITL (checkpoints de erro composto, escape hatch por confiança) é que aqui o HITL não é opcional por design — ele é forçado pela taxa de falso positivo do próprio pipeline, o que o torna também um custo operacional a orçar, não só uma salvaguarda.

## Ver também

- [[wiki/concepts/idor]] — a falha concreta encontrada pelo pipeline no caso relatado
- [[wiki/concepts/apagao-de-seniors]] — tensão relacionada: se a execução vira barata, o risco de longo prazo é ninguém aprender a julgar

## Key Sources

- [[wiki/sources/pipeline-agentes-ia-pentest-idor-critica-nao-substitui]]
- [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] — mesmo fenômeno em escala maior: modelos especializados encontrando vulnerabilidades de décadas em software crítico (OpenBSD, FFmpeg, Linux)
