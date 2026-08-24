---
type: source
title: "Xunit (Martin Fowler)"
aliases: ["xunit bliki", "história do junit", "origem do junit"]
date_created: 2026-07-19
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/xunit-martin-fowler.md
source_url: "https://martinfowler.com/bliki/Xunit.html"
author: "Martin Fowler"
date_published: 2006-01-17
date_ingested: 2026-07-19
source_count: 0
tags: [testes, tdd, junit, xunit, kent-beck, erich-gamma, historia, martin-fowler]
skill: tech-mentor-testing
status: stable
---

# Xunit (Martin Fowler)

## TL;DR

Bliki entry curto (mesma data do Test Double: 17 jan 2006) em que Fowler conta a origem da família de frameworks XUnit: nasceram como frameworks caseiros em Smalltalk que Kent Beck construía para si e clientes, viraram [[wiki/concepts/seedwork|Seedwork]] (cada time reconstrói o próprio, em vez de reusar um framework compartilhado), e só ganharam alcance global quando Kent Beck e Erich Gamma escreveram o JUnit num voo para a OOPSLA 1997 — a partir daí, "quase toda linguagem" ganhou um port.

## Key Claims

- **XUnit é o nome de família dado ao grupo de frameworks derivados de JUnit** — o primeiro a ficar amplamente conhecido. → [[wiki/entities/junit]]
- **A origem é anterior ao JUnit: Kent Beck já construía frameworks de teste caseiros em Smalltalk**, com foco em rodar testes rapidamente dentro do próprio IDE, num ciclo de edição-e-teste repetido a cada mudança. → [[wiki/entities/kent-beck]]
- **Não havia um framework único — Beck preferia que cada time construísse o seu próprio**, algo que levava poucas horas; isso é, na prática, o padrão que Fowler nomeia [[wiki/concepts/seedwork|Seedwork]] em outro bliki entry (framework mínimo que você modifica à vontade, em vez de estender de forma controlada).
- **O framework de Beck foi usado no projeto [[wiki/entities/c3-project|C3]]** (Chrysler Comprehensive Compensation), onde Ron Jeffries também foi apresentado a ele — C3 é o projeto de nascimento da Extreme Programming.
- **JUnit nasceu num voo de Zurique para a OOPSLA 1997 em Atlanta**, programado em par por Kent Beck e Erich Gamma, feito test-first. Fowler foi um dos primeiros usuários alfa e contribuiu de volta — inclusive é indiretamente responsável pela convenção de mensagem de assert vir como primeiro argumento, ao contrário da convenção Java usual de argumentos opcionais no fim.
- **Erich Gamma, coautor do JUnit, é um dos quatro autores do Gang of Four** (*Design Patterns*, 1994) — ver [[wiki/entities/gang-of-four]].
- **JUnit introduziu o indicador de progresso vermelho/verde** — inspirado em uma prática do time do C3 de colorir a janela de build inteira; JUnit formalizou isso como barra de progresso, criando vocabulário novo ("red bar", "green bar") que se espalhou pela indústria.
- **JUnit foi essencial para sustentar o crescimento de Extreme Programming e TDD** — sua simplicidade encorajou adoção; Fowler credita boa parte da mudança de atitude da indústria em relação a testes automatizados, na década anterior a 2006, à existência do JUnit.
- **Proliferação de ports**: Michael Feathers criou o CppUnit (provavelmente o primeiro port), seguido por ports para praticamente toda linguagem. Os ports variam de traduções literais até adaptações sofisticadas — NUnit 2.0 usou atributos de C# de forma elogiada por Anders Hejlsberg, influência que retornou ao Java na forma de annotations.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/kent-beck]] · [[wiki/entities/gang-of-four]] · [[wiki/entities/junit]] · [[wiki/entities/c3-project]]

## Concepts

[[wiki/concepts/tdd]] · [[wiki/concepts/seedwork]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/piramide-de-testes]]

## Conexão com o outro bliki entry da mesma data

Este artigo e [[wiki/sources/test-double-martin-fowler]] foram publicados no mesmo dia (17 jan 2006). O Test Double bliki abre citando que Gerard Meszaros "está escrevendo um livro para capturar padrões de uso dos vários frameworks Xunit" — ou seja, o próprio Fowler está usando o termo "Xunit" definido neste artigo para contextualizar o outro. As duas fontes são, na prática, um par: uma conta a origem técnica/histórica da família de frameworks, a outra cataloga o vocabulário de objetos de teste (Test Doubles) que surgiu ao redor deles.

## Open Questions

- Fowler cita ter contribuído mudanças para o JUnit original, incluindo (por implicação) a convenção de mensagem de assert como primeiro argumento — não há confirmação independente disso nesta wiki, só o relato em primeira pessoa do próprio bliki.
- ~~As páginas bliki [[wiki/concepts/seedwork|Seedwork]] e [[wiki/entities/c3-project|C3]] foram consultadas diretamente (via `curl` na fonte, não via WebFetch resumido) para calibrar os stubs criados nesta ingestão, mas não foram ingeridas como fontes primárias completas — citadas aqui como `[external]` com URL. Candidatas a ingestão própria no futuro se surgirem mais claims relevantes.~~ **Fechada em 2026-08-23**: ambas foram ingeridas como fontes primárias completas — [[wiki/sources/seedwork-martin-fowler]] e [[wiki/sources/c3-martin-fowler]].
- O relato da criação do red/green bar no C3 é anterior ao JUnit formalizar isso como barra de progresso — não há uma fonte terceira citada por Fowler para essa prática do time do C3, é memória pessoal dele.

## Raw Quotes

> "XUnit is the family name given to bunch of testing frameworks that have become widely known amongst software developers. The name is a derivation of JUnit, the first of these to be widely known."

> "JUnit was born on a flight from Zurich to the 1997 OOPSLA in Atlanta. Kent was flying with Erich Gamma, and what else were two geeks to do on a long flight but program?"

> "Kent wants people to control their own environment, so he liked to have each team build the framework themselves (it only took a couple of hours)... essentially it was really a Seedwork."

*(Tradução completa em `raw/xunit-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
