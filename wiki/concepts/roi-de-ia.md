---
type: concept
title: "ROI de IA"
aliases: ["retorno de ia", "ai roi", "valor da ia", "ia roi organizacional"]
date_created: 2026-05-31
date_updated: 2026-08-10
source_count: 3
tags: [roi-de-ia, ia-organizacional, llmops, token-economics, learning-gap-organizacional]
skill: tech-mentor-ai
status: stable
---

# ROI de IA

## TL;DR

O ganho individual de produtividade com IA é real e medido. O ganho no nível da empresa trava no caminho — por falta de redesenho de processo, governança e mudança de cultura. A pergunta certa não é "a IA funciona?" (funciona), mas "o valor que ela gera supera o custo total e está sendo capturado por quem paga a conta?"

## Os Números

| Fonte | Dado |
|-------|------|
| Writer (2.400 respondentes) | 29% veem ROI / 71% não veem |
| Mercer (12.000 respondentes) | 27% atingiram expectativa — número **caindo** ano a ano |
| MIT (critério rigoroso) | **5%** com impacto real medido na balança |
| Google DORA | 8 meses para o investimento começar a dar retorno; 34% no primeiro ano se atravessar a fase |

O gap entre 29% (Writer) e 5% (MIT) não é contradição — medem com critérios diferentes. O MIT exige impacto na balança da empresa; a Writer mede percepção de executivos.

## O Ganho Individual Existe

- **97%** dos executivos relatam benefício *individual*
- Superusers economizam **9 horas/semana** — mais de um dia útil
- São **5x mais produtivos**

O problema: ganho no nível da pessoa não sobe automaticamente para a empresa.

## Por que o Valor Vaza no Caminho

```
Dev mais produtivo
    ↓
Entrega mais código
    ↓
Mas o processo de entrega não mudou (review, deploy, rollout)
    ↓
Ou a empresa não redesenhou onde alocar esse tempo liberado
    ↓
Ganho individual → não vira receita nem redução de custo real
```

**Diagnóstico do MIT:** o problema não é a qualidade do modelo. É o [[learning-gap-organizacional]] — a integração e a maturidade da organização onde a IA vai trabalhar.

## O que Gera ROI de Verdade

1. **Redesenho de processo** — não apenas "dar IA para os devs"
2. **Governança** — quem decide o que automatizar, com quais critérios
3. **Mudança de cultura** — equipe que usa IA para crescer, não para se manter
4. **Harness de qualidade** — testes, cobertura, arquitetura clara para a IA amplificar

> *"A maioria das empresas está tentando colher o fruto sem plantar a árvore."*

## O que Não Gera ROI

- Comprar licença + esperar mágica → [[ai-washing]]
- Demitir atribuindo à IA → Gartner mostra zero correlação entre demissão e ROI
- Pressionar deadline sem mudar processo → [[aprendizado-passivo]] organizacional

## Linha do Tempo Realista (Google DORA)

```
Mês 0–8:   investimento em treinamento, remoção de gargalos, débito técnico
           → desaceleração temporária
Mês 8+:    retorno começa a aparecer
Ano 1:     até 34% de retorno possível — se atravessar a fase
```

## Relação com [[era-agentica]]

Na era agêntica, o custo por dev explodiu ($200–2.000+/mês). ROI positivo exige que o valor gerado pelo agente supere esse custo — o que só acontece com processo e governança adequados.

## Previsão Gartner: Custo de Codificação Supera Salário Médio até 2028

A [[wiki/entities/gartner]] projeta que o custo de codificação com IA vai superar o salário médio de um desenvolvedor até **2028**. O motivo apontado não é a tecnologia em si, mas a falta de disciplina de consumo de tokens — que não surge da escolha do desenvolvedor, já que devs tendem a otimizar velocidade e conveniência em vez de eficiência de custo. Sem visibilidade institucional clara do uso de tokens, a organização arrisca estourar orçamento e perder a capacidade de rastrear resultado de custo versus valor — o oposto exato do que o [[wiki/concepts/capital-de-tokens|capital de tokens]] exigiria se fosse tratado com o mesmo rigor de medição do capital humano.

## Quantificação do Vazamento: 93% de adoção, 10% de ganho (Faros AI)

[[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] dá um número concreto para o "valor que vaza no caminho" descrito acima: 93% de adoção de IA entre devs, mas só **10% de ganho de produtividade organizacional** — mesmo com devs individualmente fazendo +21% de tarefas e ~2x de PRs. O ponto de vazamento identificado é específico: o processo de entrega (a revisão) não mudou, então o ganho individual esbarra no gargalo de code review (+91% no tempo de review). É a versão de engenharia interna do mesmo "ganho individual que não sobe para a empresa" — ver [[wiki/concepts/paradoxo-da-aceleracao]].

## Key Sources

- [[wiki/sources/ia-custo-roi-bolha-ou-realidade]]
- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]] — previsão Gartner 2028 e o conceito de capital de tokens
- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] — 93% adoção vs. 10% de ganho organizacional; o vazamento localizado no gargalo de code review
