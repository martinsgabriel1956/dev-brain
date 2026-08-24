---
type: source
title: "C3 (Martin Fowler)"
aliases: ["c3 bliki", "chrysler comprehensive compensation", "origem da extreme programming"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/c3-martin-fowler.md
source_url: "https://martinfowler.com/bliki/C3.html"
author: "Martin Fowler"
date_published: 2004-08-03
date_ingested: 2026-08-23
source_count: 0
tags: [extreme-programming, kent-beck, historia, xp, folclore]
skill: tech-mentor-testing
status: stable
---

# C3 (Martin Fowler)

## TL;DR

Bliki entry curto em que Fowler conta a história do projeto Chrysler Comprehensive Compensation (C3): consolidação de sistemas legados de folha de pagamento em COBOL, onde Fowler participou como consultor desde 1993. O desenvolvimento em Smalltalk começou em 1995, mas foi reiniciado em 1996 sob liderança de [[wiki/entities/kent-beck]] — reinício que consolidou as práticas hoje conhecidas como Extreme Programming. O sistema entrou em produção em 1997 (~10 mil funcionários), mas novo desenvolvimento parou em 1999 e a folha voltou ao COBOL original. Fowler encerra observando que faltam análises confiáveis do projeto (a Wikipedia inclusive erra) e que outros projetos, não o C3, sustentaram a evolução da XP depois de seu fim.

## Key Claims

- **C3 é o nome curto de "Chrysler Comprehensive Compensation"**, projeto para consolidar múltiplos sistemas legados de folha de pagamento COBOL da Chrysler numa única aplicação.
- **Fowler participou como consultor a partir de 1993** — anterior ao início do desenvolvimento em si.
- **Desenvolvimento em Smalltalk começou em 1995 e teve problemas de estabilidade**, levando a um recomeço em 1996 sob liderança de [[wiki/entities/kent-beck]] — esse recomeço é o evento que incorporou as práticas que se tornariam a Extreme Programming. → [[wiki/entities/c3-project]]
- **O sistema entrou em produção em 1997**, processando compensação de aproximadamente dez mil funcionários.
- **Novo desenvolvimento cessou em 1999**; o projeto teve a ambição de cobrir toda a folha da Chrysler, mas não chegou lá. O sistema em produção foi revertido para a infraestrutura COBOL original, com apenas um subconjunto de funcionários permanecendo no sistema novo. Havia planos (não confirmados como executados) de migrar para um ERP.
- **"XP não é garantia de sucesso"** — Fowler enquadra o encerramento do C3 como prova disso: o sucesso inicial do C3 inspirou a XP e ajudou a difundi-la, mas foram *outros* projetos que sustentaram a evolução da metodologia depois que o C3 propriamente dito encerrou.
- **Relatos externos sobre o C3, incluindo a Wikipedia, são incorretos ou incompletos** segundo Fowler — ele atribui isso à falta de análise vinda de quem participou em tempo integral da equipe, e nota que fontes externas costumam se basear em referências pouco claras.
- **Vários membros da equipe do C3 seguiram para outros projetos de XP**, um dos quais ficou conhecido por manter um "VeryLowDefectProject" (projeto com taxa de defeitos muito baixa).

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/kent-beck]] · [[wiki/entities/c3-project]]

## Concepts

[[wiki/concepts/extreme-programming]] · [[wiki/concepts/tdd]] · [[wiki/concepts/yagni]] · [[wiki/concepts/seedwork]]

## Conexão com xunit-martin-fowler

[[wiki/sources/xunit-martin-fowler]] já mencionava o C3 de passagem (framework de testes caseiro de Beck usado no projeto, prática do time de colorir a janela de build em vermelho/verde). Esta fonte é o relato dedicado de Fowler sobre o próprio projeto, publicado quase dois anos e meio antes (ago/2004 vs. jan/2006) — o stub [[wiki/entities/c3-project]], criado durante aquela ingestão a partir de consulta direta (não uma ingestão própria), agora ganha fonte primária formal.

## Open Questions

- Fowler não detalha quais práticas específicas foram "incorporadas" no recomeço de 1996 além de afirmar que se tornaram a XP — o detalhamento das 12 práticas originais da XP (planning game, pair programming, TDD, refactoring contínuo, etc.) não vem desta fonte.
- Não fica claro se os planos de migração para um sistema ERP mencionados no fim do artigo chegaram a ser executados — Fowler não confirma.
- ~~O time e o projeto específico que alcançou reconhecimento como "VeryLowDefectProject" não são nomeados~~ — **resolvido**: [[wiki/sources/very-low-defect-project-martin-fowler]] (fonte primária de Fowler, publicada sete meses antes desta, em jan/2004) identifica o projeto como o software de portal na Chrysler de ex-colegas do C3, com exatamente um bug registrado em 2002. Pessoas e empresa cliente continuam não nomeadas.
- Assim como em [[wiki/sources/xunit-martin-fowler]], Fowler reafirma aqui que a página da Wikipedia sobre o C3 é enganosa — nenhuma dessas fontes deve ser usada nesta wiki sem verificação adicional.

## Raw Quotes

*(Tradução completa em `raw/c3-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
