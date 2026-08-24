---
type: entity
title: "C3 (Chrysler Comprehensive Compensation Project)"
aliases: ["C3", "Chrysler Comprehensive Compensation", "projeto de nascimento da XP"]
date_created: 2026-07-19
date_updated: 2026-08-23
source_count: 3
tags: [extreme-programming, kent-beck, historia, xp]
skill: tech-mentor-testing
status: stable
---

# C3 (Chrysler Comprehensive Compensation Project)

Projeto de consolidação de sistemas legados de folha de pagamento COBOL na Chrysler. [[wiki/entities/martin-fowler]] participou como consultor a partir de 1993; o desenvolvimento em Smalltalk começou em 1995, teve problemas de estabilidade e foi reiniciado sob liderança de [[wiki/entities/kent-beck]] em 1996 — esse recomeço é conhecido como o "projeto de nascimento" da [[wiki/concepts/extreme-programming|Extreme Programming]]. Foi ali que as práticas que se tornariam conhecidas como XP foram reunidas pela primeira vez de forma coesa (embora Beck já usasse abordagens parecidas em projetos anteriores). Ron Jeffries também foi apresentado ao framework de testes de Beck durante o C3.

## Linha do tempo

- **1993** — Fowler entra como consultor.
- **1995** — início do desenvolvimento em Smalltalk; problemas de estabilidade.
- **1996** — recomeço sob liderança de Kent Beck; consolidação das práticas da XP.
- **1997** — sistema entra em produção, processando compensação de ~10 mil funcionários.
- **1999** — novo desenvolvimento cessa; sistema em produção é revertido, em parte, para a infraestrutura COBOL original.

## Sucesso inicial não sustentou o projeto — nem era necessário para sustentar a XP

Segundo [[wiki/sources/c3-martin-fowler]], o C3 nunca chegou a cobrir toda a folha de pagamento da Chrysler como planejado, e o desenvolvimento novo parou em 1999 — mas o sucesso inicial do projeto (1997) já havia sido suficiente para inspirar e difundir a XP. Fowler usa esse desfecho como argumento explícito de que "XP não é garantia de sucesso": foram *outros* projetos, não o C3, que sustentaram a evolução da metodologia depois de seu encerramento. Vários ex-membros da equipe do C3 seguiram para esses projetos seguintes, um dos quais alcançou reconhecimento por manter um [[wiki/concepts/very-low-defect-project|VeryLowDefectProject]].

## Ex-membros do C3 e o software de portal na Chrysler (2002)

[[wiki/sources/very-low-defect-project-martin-fowler]] (jan/2004, publicado sete meses *antes* do relato dedicado ao C3) nomeia esse projeto seguinte, embora sem nomear pessoas: "vários dos meus velhos amigos do C3" construíram software de portal na Chrysler e, partindo de um defeito por mês, registraram **exatamente um bug em todo o ano de 2002** — enquanto lançavam uma nova versão a cada uma ou duas semanas. É o caso concreto por trás da menção lateral em [[wiki/sources/c3-martin-fowler]], e reforça a tese acima com um contraste direto: o C3 original não sustentou seu próprio sucesso, mas parte de sua equipe produziu, em outro projeto, um dos resultados de qualidade mais fortes já atribuídos à XP.

## Relevância para esta wiki

O framework de testes caseiro em Smalltalk que Beck usava no C3 — um exemplo de [[wiki/concepts/seedwork|Seedwork]] — é o antecessor direto do [[wiki/entities/junit]], criado por Beck e Erich Gamma em 1997. O time do C3 também tinha o hábito de colorir a janela de build inteira de vermelho/verde conforme os testes passavam ou falhavam — prática que o JUnit formalizaria como a barra de progresso red/green bar.

## Nota sobre confiabilidade de fontes externas

Fowler nota, tanto em [[wiki/sources/xunit-martin-fowler]] quanto em [[wiki/sources/c3-martin-fowler]], que a página da Wikipedia sobre o C3 é enganosa e baseada em fontes pouco claras — segundo ele, análise confiável do projeto deveria vir de quem participou em tempo integral da equipe, o que raramente aconteceu. Não usar a Wikipedia como referência sobre o C3 sem verificação adicional.

## Ver também

- [[wiki/entities/kent-beck]]
- [[wiki/entities/junit]]
- [[wiki/concepts/seedwork]]
- [[wiki/concepts/extreme-programming]]

## Key Sources

- [[wiki/sources/xunit-martin-fowler]]
- [[wiki/sources/c3-martin-fowler]] — fonte primária dedicada ao projeto: linha do tempo completa, desfecho e a tese de que "XP não é garantia de sucesso"
- [[wiki/sources/very-low-defect-project-martin-fowler]] — nomeia (sem nomes próprios) o projeto seguinte de ex-membros do C3: software de portal na Chrysler, exatamente um bug em 2002
