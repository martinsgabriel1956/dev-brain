---
type: entity
title: "Meta"
aliases: ["Facebook", "Meta Platforms"]
date_created: 2026-07-16
date_updated: 2026-11-17
source_count: 14
tags: [empresa, demissao, ai-washing, era-agentica, graphql, api-design, ci-cd, deploy]
skill: tech-mentor-ai
status: stub
---

# Meta

Big tech dona do Facebook, Instagram e WhatsApp. O CEO Mark Zuckerberg admitiu, em memorando interno, que a tecnologia de agentes de IA não progrediu tão rápido quanto esperado e que a empresa cometeu erros ao reestruturar equipes antecipando ganhos de produtividade por IA que ainda não se confirmaram — ver [[wiki/concepts/ai-washing]] e [[wiki/concepts/roi-de-ia]].

## O Memorando

> "Dada a complexidade dessas mudanças, cometemos erros e quase certamente cometeremos mais [...] não quero prometer demais, porque o mundo está mudando de maneiras que estão fora do nosso controle." — Mark Zuckerberg

Um exemplo concreto de erro citado: o assistente de recuperação de senha do Instagram, ao incorporar IA, passou a recitar senhas de usuários. Zuckerberg reiterou que a Meta não espera mais demissões em massa em toda a empresa neste ano — em contraste direto com a [[wiki/entities/microsoft]], que fez sua primeira grande onda de demissões dias antes.

## Criadora do GraphQL

A Meta (então Facebook) criou o [[wiki/concepts/graphql]], motivada pela necessidade de múltiplos frontends (mobile, web, iPad), evoluindo rapidamente, buscarem dados profundamente aninhados (usuário → post → comentário) sem multiplicar endpoints REST especializados por tela — e sem sofrer do problema de [[wiki/concepts/n-plus-one]] entre frontend e backend. Ver [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]].

## Deploy Contínuo em Escala Massiva (2017)

Antes de ser conhecida por IA, a Meta (então Facebook) já era referência em [[wiki/concepts/ci-cd]]: em 2017, migrou o deploy web de ~700 cherry-picks manuais/dia para push quase-contínuo direto da master, escalando via [[wiki/concepts/canary-release|rollout gradual]] (funcionários → 2% → 100%) e usando seu sistema interno de feature flag, o Gatekeeper, para desacoplar deploy de release (→ [[wiki/concepts/deploy-vs-release]]). Ver [[wiki/sources/rapid-release-at-massive-scale-facebook]].

## Facebook em japonês

Exemplo de Násser: com o Facebook em japonês, os ícones (caixa de entrada, sininho, engrenagem, lápis, escudo) ainda guiam o usuário ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Facebook denso

Na aula de espaçamento e linhas, o Facebook é o exemplo de interface densa: feed em cards, informações mais juntas dentro do card, linha de ponta a ponta separando conteúdo de interação ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]). Ver [[wiki/concepts/densidade-de-informacao]].

## Cores de marca

Na aula de paleta de Násser, Facebook (azul) e WhatsApp (verde) são exemplos de cor de base que "define o branding da marca" ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]). Ver [[wiki/concepts/identidade-visual]].

## Preto com um pingo de azul

Em aula de UI, o Facebook é exemplo de neutro tingido: "não é um preto totalmente sem saturação, ele tem um pingo de azul naquele preto, assim como um branco" ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]). Ver [[wiki/concepts/variacao-de-cores]].

## Key Sources

- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: React aula 03 do FrontPUSH: Facebook como criador do React
- [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]]
- [[wiki/sources/problema-n-mais-1-graphql-orm-solucoes]] — origem do GraphQL como resposta ao N+1/over-under-fetching
- [[wiki/sources/rapid-release-at-massive-scale-facebook]] — transição para deploy contínuo em escala (2017)
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — caso citado de segunda mão como ilustração didática de deploy vs. release
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — citada (sem detalhamento numérico) como uma das big techs estourando orçamento de engenharia de IA em 2026
- [[wiki/sources/historia-e-evolucao-das-apis-bernardo-lobato]] — criadora do [[wiki/concepts/graphql]], situado na linha do tempo dos anos 2010; também citada (então Facebook) como uma das pioneiras de API pública nos anos 2000
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — Explorar do Instagram: grid assimétrico e eixo de continuidade para feed infinito; Reels maiores como hierarquia
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — Facebook em japonês, navegável pelos ícones
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — Facebook denso organizado com cards e linhas
- [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]] — Facebook azul e WhatsApp verde como cor de branding
- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — preto e branco do Facebook tingidos de azul
- [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]] — FANG; rumor de codebase excelente

## Facebook como origem do React

Em [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]], a interface do Facebook (chat e curtidas atualizando sem recarregar) é a motivação do [[wiki/entities/react]], "criada pelo Facebook [...] por volta de 2013, 2014". O lançamento público foi em maio de 2013.

## Meta como empregadora (rumor)

Em [[wiki/sources/big-techs-salarios-vagas-processo-de-aplicacao]], parte da FANG; "dizem que a Meta tem uma codebase excelente", rumor que o autor pede para não tomar como recomendação.
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: o Facebook como quem "disponibiliza" o create-react-app
