---
type: concept
title: "Projetar Duas Vezes (Design It Twice)"
aliases: ["design it twice", "design duas vezes"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [design, ousterhout, processo, decisao-tecnica]
skill: tech-mentor-backend
status: draft
---

# Projetar Duas Vezes (Design It Twice)

## TL;DR

Princípio de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 11): considerar pelo menos duas alternativas radicalmente diferentes antes de escolher uma interface ou implementação — mesmo quando a primeira ideia parece obviamente a certa. Comparar explicitamente os prós e contras de cada alternativa revela problemas que não aparecem ao avaliar uma única opção isoladamente, e frequentemente leva a uma terceira alternativa, melhor que as duas primeiras, construída a partir dos defeitos identificados em ambas.

## Exemplo recorrente do livro

A classe de texto de um editor GUI (usada em vários capítulos do livro) é o exemplo mais citado: comparar explicitamente uma interface *line-oriented* (métodos por linha inteira), uma *character-oriented* (inserir/deletar caractere a caractere) e uma *range-oriented* (inserir/deletar um intervalo arbitrário de caracteres, que pode cruzar linhas) lado a lado expõe que as duas primeiras forçam código adicional em quem usa a classe (dividir/juntar linhas, ou fazer loop caractere a caractere) — o que leva à terceira opção, superior às duas.

## Por que isso é difícil para gente inteligente

O autor nota que pessoas muito inteligentes tendem a resistir ao hábito: cresceram descobrindo que a primeira ideia já bastava para uma boa nota, então nunca desenvolveram o hábito de considerar uma segunda alternativa. Isso os torna mais lentos para chegar em designs realmente bons em problemas difíceis o suficiente — que é exatamente onde projetar duas vezes compensa mais. Custo típico: 1–2 horas para um módulo pequeno, insignificante frente às semanas de implementação que seguem.

## Onde aplicar

O princípio se aplica em múltiplos níveis: ao escolher a **interface** de um módulo (foco: facilidade de uso para quem chama), ao escolher sua **implementação** (foco: simplicidade e performance), e em decisões de nível mais alto, como decompor um sistema em módulos principais ou escolher funcionalidades de uma interface de usuário.

## Relação com outros conceitos

- [[wiki/concepts/decidir-o-que-importa]] — comparar alternativas explicitamente é uma das formas citadas no livro para descobrir o que realmente importa em uma decisão (ex.: ao escolher nome de variável, listar várias opções antes de escolher a mais informativa).
- [[wiki/concepts/tech-debt-como-ferramenta]] — projetar duas vezes é um dos investimentos proativos da programação estratégica (Cap. 3): gastar um pouco mais de tempo agora para produzir um design melhor.
- [[wiki/concepts/modulo-profundo]] — o exercício de comparar alternativas é o mecanismo prático mais citado no livro para chegar a interfaces mais profundas.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 11 completo
