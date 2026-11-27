---
type: concept
title: "Sensible Defaults / Paved Road"
aliases: ["sensible defaults", "paved road", "estrada pavimentada", "padroes sensatos", "golden path"]
date_created: 2026-08-12
date_updated: 2026-11-27
source_count: 3
tags: [platform-engineering, sensible-defaults, paved-road, golden-path, autonomia, netflix]
skill: tech-mentor-infra
status: draft
---

# Sensible Defaults / Paved Road

## TL;DR

Mecanismo que uma [[plataforma-digital]] usa para reconciliar **autonomia** e **consolidação** sem recorrer a mandato: oferecer **padrões sensatos** (*sensible defaults*) que o time pode adotar de imediato — e opcionalmente sobrescrever. A adoção é por atração, não por imposição. A [[wiki/entities/netflix]] chama isso de **paved road** (estrada pavimentada).

## O problema que resolve

Dois extremos, ambos ruins ([[wiki/sources/talk-about-platforms-evan-bottcher]]):
- **mandato central** ("build for reuse" obrigatório) → gera [[backlog-coupling]] e infra travada;
- **autonomia total** → elimina o acoplamento mas cria **arrasto por diversificação tecnológica** (cada time reinventa a stack, ilustrado pelo Cloud Native Landscape lotado).

Sensible defaults é o meio-termo: o caminho padrão já vem pronto e bom, mas ninguém é obrigado a segui-lo.

## Paved road (Netflix)

Modelo citado por Bottcher: os times **não são obrigados** a usar o ferramental centralizado, mas se saírem da estrada pavimentada assumem **todos os custos** de manter a alternativa. O incentivo econômico empurra naturalmente para a plataforma — sem mandato.

## Tornar o caminho certo o mais fácil

Princípio (formalizado depois como **golden path** em IDPs `[skill: tech-mentor-infra]`, `references/platform-engineering.md`): o caminho recomendado deve ser o mais fácil de seguir — irresistível, não obrigatório. Se o time precisa "hackear" o default para fazer algo razoável, o default está errado.

## Relacionados

- [[plataforma-como-produto]] — adoção voluntária como teste de qualidade da plataforma
- [[backlog-coupling]] / [[autonomia-tecnica]] — os dois extremos que isto equilibra
- [[you-build-it-you-run-it]] — quem opera o que sai da estrada

## O mesmo princípio no nível da API (Ousterhout)

[[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] (5.7) aplica a ideia a uma classe: a biblioteca HTTP deve preencher sozinha a versão da resposta e o cabeçalho `Date`. Valores padrão tornam o caso comum o mais simples possível e são ocultação parcial: o usuário normal nem sabe que o item existe, e o raro que precisa troca por um método específico. "As melhores funcionalidades são aquelas que você obtém sem sequer saber que existem." O red flag do lado oposto é a superexposição ([[wiki/concepts/red-flags-de-design]]). A analogia com a paved road é da wiki: lá o default é uma escolha de ferramenta, aqui um valor de parâmetro.

## Padrão razoável para parâmetros de configuração (cap. 8)

[[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] (8.2) volta ao valor padrão: quando um [[wiki/concepts/parametro-de-configuracao]] é inevitável, ele deve ter um padrão razoável, para que o usuário só precise mexer "em condições excepcionais". Antes disso vem a pergunta se o parâmetro precisa existir: se o módulo calcula um valor melhor que o usuário, não exporte. Ver [[wiki/concepts/puxar-complexidade-para-baixo]].

## Key sources

- [[wiki/sources/talk-about-platforms-evan-bottcher]] — Evan Bottcher, *What I Talk About When I Talk About Platforms* (2018)
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]] — valores padrão em APIs como ocultação parcial (5.7)
- [[wiki/sources/filosofia-do-design-de-software-cap-08-puxe-a-complexidade-para-baixo]] — 8.2: padrões razoáveis para parâmetros de configuração que não puderam ser eliminados
