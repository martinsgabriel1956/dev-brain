---
type: concept
title: "Hierarquia Visual"
aliases: ["visual hierarchy", "hierarquia de elementos", "padrão Z", "padrão F", "Z-pattern", "F-pattern"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [ui, ux, design, frontend, hierarquia-visual]
skill: tech-mentor-frontend
status: draft
---

# Hierarquia Visual

Ordem em que o olho do usuário percorre os elementos de uma tela, definida deliberadamente por meio de peso de fonte, tamanho, cor e posicionamento — não deixada ao acaso. O objetivo é que os elementos mais importantes chamem atenção primeiro, e os demais em ordem decrescente de importância.

## O problema de dois pontos focais

Se dois elementos (por exemplo, dois CTAs) têm o mesmo peso visual — mesmo tamanho, mesma cor chamativa, mesma fonte — o cérebro não sabe qual priorizar. Na prática, o usuário tende a escolher a ação mais fácil de executar, não a mais desejada pelo produto: um CTA de "ver conteúdo" (passivo, sem fricção) tende a roubar cliques de um CTA de "se inscrever" (ativo, com fricção de preencher um formulário), mesmo que o segundo seja o objetivo real da página.

## Padrões de leitura em tela

Além do peso visual dos elementos individuais, o **posicionamento relativo** segue padrões de escaneamento documentados:

- **Padrão Z**: usado em páginas com mais elementos e menos texto (apps, landing pages). O olho percorre da esquerda pra direita a partir do topo, desce em diagonal até a parte inferior esquerda, e finaliza a leitura da esquerda pra direita novamente — desenhando um Z.
- **Padrão F**: usado em páginas com muito texto (blogs, artigos). O usuário primeiro escaneia o conteúdo em formato de F (sem ler de fato) e só depois volta para ler o que interessou.

Escolher o padrão errado para o tipo de conteúdo — por exemplo, aplicar F numa tela com poucos elementos e um único objetivo de conversão — dilui o fluxo de atenção que a hierarquia visual tenta impor.

## Aplicação em prompts de geração de UI

Ao pedir para uma IA (ex.: UX Pilot, Cursor) gerar ou refatorar uma interface, é possível declarar a hierarquia explicitamente no prompt: qual elemento é o ponto focal primário (ex.: título com peso de fonte máximo), qual é o secundário (ex.: formulário), e garantir que a ação de CTA seja visualmente dominante sobre o resto — evitando CTAs concorrentes.

## Relação com outros conceitos

- [[wiki/concepts/lei-da-proximidade-gestalt]] — hierarquia define *o que* chama atenção primeiro; proximidade define *quais elementos são lidos como um grupo único*.
- [[wiki/concepts/affordance]] — hierarquia guia a atenção; affordance guia a ação depois que a atenção chegou lá.
- [[wiki/concepts/design-como-interacao]] — hierarquia é uma das camadas de design que vai além do "bonito", com efeito direto em conversão.

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
