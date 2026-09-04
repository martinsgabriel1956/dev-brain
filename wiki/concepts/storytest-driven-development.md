---
type: concept
title: "Storytest-Driven Development"
aliases: ["storytest-driven development", "STDD"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 3
tags: [testes, tdd, xunit, bdd]
skill: tech-mentor-testing
status: stable
---

# Storytest-Driven Development

Variação do [[wiki/concepts/tdd|test-driven development]] que consiste em escrever (e geralmente automatizar) **customer tests** — testes da funcionalidade visível ao cliente, ver [[wiki/concepts/piramide-de-testes]] — antes do desenvolvimento da funcionalidade correspondente começar. O objetivo explícito não é apenas ter unidades corretas isoladamente, mas garantir que a integração das unidades verificadas pelos unit tests resulte num **todo utilizável** do ponto de vista de quem usa o sistema. É, na prática, o mesmo que praticar [[wiki/concepts/test-first-development|test-first development]] no nível de customer test em vez de unit test.

O termo foi cunhado por [[wiki/entities/joshua-kerievsky|Joshua Kerievsky]], como parte de sua metodologia [[wiki/concepts/industrial-xp|"Industrial XP" (IXP)]] — uma variação prática do [[wiki/concepts/extreme-programming|XP]] clássico.

## Key Sources

- [[wiki/sources/storytest-driven-development-xunitpatterns]] — **fonte primária dedicada**: define o termo diretamente, atribui a cunhagem a Joshua Kerievsky (Industrial XP)
- [[wiki/sources/test-driven-development-xunitpatterns]] — citado como "ver também", sem definição própria
- [[wiki/sources/test-first-development-xunitpatterns]] — não cita STDD diretamente, mas descreve a mesma prática por contraste (test-first no nível de customer test)
- [[wiki/sources/ixp-industrial-xp-xunitpatterns]] — fecha a lacuna de atribuição: fonte primária dedicada a Industrial XP e Joshua Kerievsky, antes só citados por contraste aqui
