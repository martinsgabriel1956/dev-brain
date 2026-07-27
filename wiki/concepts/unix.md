---
type: concept
title: "Unix"
aliases: ["UNIX"]
date_created: 2026-07-20
date_updated: 2026-07-27
source_count: 2
tags: [sistema-operacional, unix, servidor, cs-fundamentals, comunidade, open-source]
skill: cs-fundamentals
status: stub
---

# Unix

Um dos sistemas operacionais mais antigos, desenvolvido no final dos anos 60 pela AT&T como sistema multitarefa e multiusuário, voltado a servidores e computação de alto nível. Deu origem a muitos sistemas modernos, incluindo o [[wiki/concepts/linux]] (clone independente) e o [[wiki/concepts/bsd]] (descendente direto do código-fonte).

## Uso

Raramente usado por consumidores comuns — domínio de grandes corporações, bancos e centros de pesquisa. Exemplo citado: serviços nacionais de meteorologia usam sistemas baseados em Unix para processar grandes volumes de dados.

## Desvantagem

Licenciamento comercial caro — para uma empresa de 250 funcionários, o custo pode ultrapassar a casa das centenas de milhares de dólares.

## Origem como Subproduto e o Senso de Comunidade

Segundo [[wiki/sources/a-insanidade-de-ser-um-programador-hoje]], o Unix nasceu como subproduto: [[wiki/entities/ken-thompson]] queria um ambiente melhor para rodar o próprio jogo, *Space Travel*, na AT&T, e criou o Unix no processo. Depois de criado, não guardou para si — o sistema foi absorvido pela comunidade, que construiu em cima dele ao longo de décadas (incluindo os descendentes já documentados nesta página, [[wiki/concepts/linux]] e [[wiki/concepts/bsd]]). O mesmo Thompson criou o `grep` (busca recursiva de padrão de texto em arquivos) originalmente como comando privado seu, antes de virar ferramenta pública padrão. A fonte usa esse histórico como exemplo do que considera um traço raro da área de programação: pessoas compartilharem trabalho sem cobrar, permitindo que outras construam em cima — o mesmo padrão por trás do ecossistema moderno de bibliotecas open source.

## Key Sources

- [[wiki/sources/8-sistemas-operacionais-explicados]] — panorama comparativo de propósito e mercado
- [[wiki/sources/a-insanidade-de-ser-um-programador-hoje]] — origem do Unix como subproduto do jogo *Space Travel* de Ken Thompson; `grep` como exemplo de ferramenta privada que virou pública; senso de comunidade da área
