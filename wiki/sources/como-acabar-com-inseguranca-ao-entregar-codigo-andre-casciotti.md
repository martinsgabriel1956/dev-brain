---
type: source
title: "Como acabar com a insegurança ao entregar código (André Casciotti)"
aliases: ["insegurança ao entregar código", "o certo é um combinado", "3 dicas contra insegurança do dev"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-acabar-com-inseguranca-ao-entregar-codigo-andre-casciotti.md
source_url: ""
author: "André Casciotti"
date_published: ""
date_ingested: 2026-10-09
source_count: 1
tags: [carreira, inseguranca, requisitos, testes, decisao, pressa, tech-debt, testing]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Vídeo do quadro "Próximo Nível" de [[wiki/entities/andre-casciotti]]. Tese: a insegurança do dev ao entregar ([[wiki/concepts/inseguranca-na-entrega]]) vem da **falta de clareza** — foco no "como" em vez do "o quê/porquê/quando" — e da diferença entre "funcionar" para o dev (sem exception) e para o usuário ([[wiki/concepts/funcionar-e-resolver-problema]]). Três antídotos: (1) descobrir **o que é o certo**, que é um **combinado formalizado** com o usuário ([[wiki/concepts/o-certo-e-um-combinado]]); (2) criar o hábito de **testar** com roteiro escrito ([[wiki/concepts/plano-de-testes-escrito]], [[wiki/concepts/testar-proprio-codigo]]); (3) fazer **escolhas conscientes** sob pressão — contexto, aceitar o cenário, reportar o risco, melhorar na próxima ([[wiki/concepts/escolhas-conscientes-sob-pressao]]).

## Key Claims

**Claim:** Insegurança é normal em toda a carreira; só é prejudicial se **constante**.
**Evidence:** experiência do autor; ambiente instável. **Confidence:** média (opinião).

**Claim:** "Funcionar" para o dev = sem exception/crash/mensagem de sucesso; para o usuário = **resolver o problema dele**, e não travar é pré-requisito óbvio. O conflito gera bronca ("chinelada") e, daí, insegurança.
**Evidence:** analogias com celular, jogo online, troca de app de finanças. **Confidence:** média-alta. Ver [[wiki/concepts/funcionar-e-resolver-problema]].

**Claim:** Devs aprendem a **seguir ordens e reclamar** do usuário; sem saber o que é certo, entregam com insegurança ou excesso de confiança.
**Evidence:** relato de formação (faculdade/cursos/primeiro emprego). **Confidence:** média (generalização anedótica).

**Claim:** "O certo" não é verdade absoluta, é um **combinado** entre a necessidade do usuário e o entendimento do dev; deve ser feito com curiosidade (perguntar porquês), desenho/material visual e **formalização** (não "no boca a boca"), porque na empresa quem puder tirar o seu da reta tira.
**Evidence:** analogia do arquiteto/decorador. **Confidence:** média-alta; coerente com [[wiki/concepts/comunicacao-tecnica]] e [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]. Ver [[wiki/concepts/o-certo-e-um-combinado]].

**Claim:** Teste é a primeira coisa descartada na correria — logo, na prática "não é importante" para o dev; a raiz é que **ninguém ensina a testar** (testar virou "apertar botão"). Testar de verdade = **validar o certo**.
**Evidence:** relatos de dúvidas de seguidores; analogia piloto/simulador. **Confidence:** média; bate com [[wiki/concepts/developers-not-writing-tests]].

**Claim:** Testar remove a insegurança: ao falhar em produção você sabe qual cenário **não** testou e o acrescenta ao plano; quem nunca testa "sempre deixa de testar alguma coisa".
**Evidence:** experiência do autor (13 anos "rateando" com testes por não saber o que era o certo). **Confidence:** média. [external] Testes só cobrem cenários pensados — ver ressalva em [[wiki/concepts/testar-proprio-codigo]].

**Claim:** Hábito de testar = (a) saber o certo, (b) **escrever roteiro/plano de testes**, (c) **executar**; manual serve para começar, automatizar depois.
**Evidence:** analogia do manual de eletrônico. **Confidence:** média. Ver [[wiki/concepts/plano-de-testes-escrito]].

**Claim:** Pressa → gambiarra → problema em produção → insegurança. Escolha consciente: saber o contexto (urgência/criticidade), aceitar o cenário sem brigar, **reportar o risco** para dividi-lo, e melhorar na próxima ("a pior coisa é cometer o mesmo erro duas vezes").
**Evidence:** experiência do autor. **Confidence:** média-alta; alinha com [[wiki/concepts/melhor-possivel-com-o-tempo-disponivel]] e [[wiki/concepts/tech-debt]] (dívida consciente). Ver [[wiki/concepts/escolhas-conscientes-sob-pressao]].

**Claim:** Insegurança = falta de clareza (foco no como, não no o quê/porquê/quando); técnicas estão em análise de requisitos, testes unitários e arquitetura.
**Evidence:** conclusão do vídeo (promove o curso do autor). **Confidence:** média; ressalva comercial.

## Entities

[[wiki/entities/andre-casciotti]] (canal Próximo Nível / curso "Dev que Resolve").

## Concepts

Novos: [[wiki/concepts/inseguranca-na-entrega]], [[wiki/concepts/o-certo-e-um-combinado]], [[wiki/concepts/plano-de-testes-escrito]], [[wiki/concepts/escolhas-conscientes-sob-pressao]], [[wiki/concepts/funcionar-e-resolver-problema]].
Existentes: [[wiki/concepts/testar-proprio-codigo]], [[wiki/concepts/developers-not-writing-tests]], [[wiki/concepts/entender-contexto-da-demanda]], [[wiki/concepts/melhor-possivel-com-o-tempo-disponivel]], [[wiki/concepts/medo-do-prazo-vs-medo-do-bug]], [[wiki/concepts/confianca-profissional-dev]], [[wiki/concepts/sindrome-do-impostor]], [[wiki/concepts/tech-debt]], [[wiki/concepts/definicao-de-pronto]], [[wiki/concepts/comunicacao-tecnica]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]], [[wiki/concepts/foco-no-que-esta-ao-seu-alcance]].

## Open Questions

- "Formalizar" como? Sem ferramenta/artefato concreto (ata, ticket, critérios de aceite, BDD) — lacuna prática.
- Tensão com [[wiki/concepts/melhor-possivel-com-o-tempo-disponivel]]: "aceitar e entregar" vs. "melhorar na próxima" — sem critério de quando a dívida consciente vira inaceitável.
- Evidência só anedótica; nenhuma pesquisa sobre insegurança/testes citada.
- Parte 2 prometida sobre insegurança técnica.

## Quotes

> "O certo é um combinado daquilo que o seu usuário precisa com aquilo que você, como dev, entendeu que precisa ser feito."

> "Você pode deixar de entregar, mas não deixa de testar. Isso não acontece."

> "Pressa gera gambiarra e gambiarra gera problema… e problema gera insegurança."

> "A pior coisa que tem é você cometer o mesmo erro duas vezes."
