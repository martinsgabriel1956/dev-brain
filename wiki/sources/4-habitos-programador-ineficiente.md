---
type: source
title: "4 Habits That Make You an Inefficient Developer"
aliases: ["4 hábitos programador ineficiente", "inefficient developer habits", "dano better programming"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_file: /home/nemomartins/Documentos/new/dev-study/raw/4-habitos-programador-ineficiente.md
source_url: https://medium.com/better-programming/4-habits-that-make-you-an-inefficient-developer-f4384c4b9df5
author: "Dano"
date_published: 2026-04-22
date_ingested: 2026-04-29
source_count: 0
tags: [carreira, hábitos, craftsmanship, testes, commits, definição-de-pronto, liderança, produtividade]
skill: tech-mentor-leadership
status: stable
---

# 4 Habits That Make You an Inefficient Developer

> "You are not a bad programmer. You may have the habits of a bad programmer."

Distinção fundamental entre **ser** e **estar**: identidade é fixa, hábitos são mutáveis. Esse framing remove a paralisia e abre espaço para ação deliberada.

Ver também: [[wiki/sources/habitos-ruins-de-programador]] (ingest anterior do mesmo conteúdo, sem URL, via transcrição PT-BR)

## TL;DR

4 hábitos que destroem a eficiência de devs — dizer sim pra tudo, definição fraca de "pronto", não testar o próprio código, e commits gigantes — todos corrigíveis com consciência e prática.

## Os 4 Hábitos

| # | Hábito | Conceito central |
|---|---|---|
| 1 | Dizer sim para tudo | Promise debt, dependência, inibição de líderes |
| 2 | Definição de "pronto" incorreta | Legibilidade, docs, code review no lugar errado |
| 3 | Não testar o próprio código | Happy path exclusivo, testes automatizados |
| 4 | Commits gigantes | Unidade funcional: código + teste no mesmo commit |

## Claims Principais

**Hábito 1 — Dizer Sim Para Tudo**
- Ajudar todos parece louvável, mas uma promessa é uma dívida — accumular sem controle estoura o tempo e derruba produtividade por interrupções constantes.
- Efeito colateral grave: pessoas ficam "viciadas" na sua opinião, param de assumir risco próprio e novos líderes não emergem.
- Contramedida: deixar a pessoa agir primeiro, depois dar feedback — ela assume 100% do risco e 100% do retorno, o que é mais poderoso para o crescimento dela.
- Calibrar sempre: nível de senioridade ≠ nível de risco. Júnior com acesso ao banco de produção não deve responder "pode rodar esse UPDATE sem WHERE?" sozinho.
- Citação: *"When you say yes to others, make sure you are not saying no to yourself."* — Paulo Coelho

**Hábito 2 — Definição de "Pronto" Incorreta**
- Codar é apenas uma das muitas tarefas de um programador.
- "Pronto" real exige: código legível por outros, documentação atualizada, review focado em regra de negócio (não só estilo), e caminhos de erro testados.
- Código que outro dev não consegue entender facilmente = evidência de que precisa refatorar = ainda não está pronto.

**Hábito 3 — Não Testar o Próprio Código**
- Testar só o happy path é tão inútil quanto concordar com a própria opinião.
- Deve-se garantir comportamento em: sucesso, erro esperado, edge cases.
- Marco de maturidade: ser enganado pelo próprio teste — sinal de que os testes têm dentes.

**Hábito 4 — Commits Gigantes**
- Pull requests gigantes ninguém quer revisar e ninguém sabe quando terminam.
- Antipadrão frequente: commit 1 quebra um teste, commit 2 corrige — dois commits sem coesão.
- Regra: no mesmo commit, vai a alteração do código E a alteração do teste que a valida. Uma unidade funcional, não um diário.

## Conceitos Abordados

- [[concepts/dizer-sim-para-tudo]]
- [[concepts/definicao-de-pronto]]
- [[concepts/testar-proprio-codigo]]
- [[concepts/atomic-commits]]

## Quotes Relevantes

> "A promise is a debt. Be very careful not to accumulate debts in an uncontrolled way."

> "Testing only the happy path is as pointless as agreeing with your own opinion."

> "Make each commit a functional unit of change, not a diary entry."

## Questões Abertas

- Qual o threshold prático para dizer não? O artigo diz "calibrar por senioridade" mas não dá critérios objetivos.
- Como medir se commits estão atômicos o suficiente? Existe heurística além de "code + test together"?
