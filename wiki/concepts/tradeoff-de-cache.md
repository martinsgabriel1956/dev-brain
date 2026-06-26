---
type: concept
title: "Tradeoff de Cache"
aliases: ["custo de cache", "complexidade de cache", "cache complexity"]
date_created: 2026-06-26
date_updated: 2026-06-26
source_count: 1
tags: [cache, tradeoff, arquitetura, decisao, backend]
skill: tech-mentor-backend
status: stable
---

# Tradeoff de Cache

## TL;DR

Adicionar [[cache]] sempre aumenta a complexidade do sistema. O ganho de performance precisa superar o custo de manter mais uma tecnologia, uma estratégia de sincronismo e um vetor de inconsistência.

## O Que Você Ganha

- Latência de resposta muito menor para dados frequentes
- Redução de carga no banco de dados
- Capacidade de absorver picos de tráfego sem escalar o banco

## O Que Você Paga

- **Complexidade extra** — a aplicação precisa coordenar leitura de cache + banco
- **Sincronismo** — quem invalida o cache quando o dado muda no banco?
- **Consistência eventual** — entre a atualização no banco e a expiração do cache, os dados divergem
- **Mais uma tecnologia** — [[redis]] é mais uma dependência para operar, versionar e monitorar
- **Debug mais difícil** — um bug pode vir do cache (dado stale) ou do banco

## O Problema Mais Difícil do Cache

> "Existem apenas duas coisas difíceis em Ciência da Computação: invalidação de cache e nomear coisas." — Phil Karlton

Saber **quando invalidar** é mais difícil que implementar o cache em si.

## Estratégias de Invalidação

| Estratégia | Como | Risco |
|---|---|---|
| TTL fixo | Expira após N segundos | Dado stale até expirar |
| Invalidação por evento | Deleta chave quando dado muda | Exige coordenação entre serviços |
| Write-through | Atualiza cache junto com banco | Latência de escrita |
| Invalidação por tag | Grupo de chaves invalidado junto | Mapeamento de tags a manter |

## Quando NÃO Adicionar Cache

- Dados financeiros onde 1 centavo de inconsistência é inaceitável
- Sistemas onde a complexidade operacional já é alta
- Tráfego baixo onde o banco não é gargalo
- Dados com volatilidade alta (TTL seria tão curto que o cache não ajuda)

## Key Sources

- [[wiki/sources/como-arquitetar-com-cache-e-redis]]
