---
type: concept
title: "Limites da API de Busca de Código do GitHub"
aliases: ["github code search", "search code api", "indexação de busca do github"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 1
tags: [github, secret-scanning, indexacao, api, security]
skill: tech-mentor-security
status: stub
---

# Limites da API de Busca de Código do GitHub

A rota de busca de código do GitHub (`search code`, parte da REST API de Search) não consulta o estado atual de todos os repositórios em tempo real — ela consulta um **índice**, construído de forma assíncrona e com atraso em relação ao momento real de um push.

## Limites Relevantes

- **Indexação não-instantânea e priorizada.** Milhões de repositórios recebem commits todos os dias; o indexador não processa tudo imediatamente e prioriza. Repositórios pequenos, de um único autor, tendem a ficar para trás na fila — e são justamente os que mais vazam secrets por descuido.
- **Teto de 1000 resultados por consulta**, mesmo quando existem dezenas de milhares de repositórios compatíveis com os termos de busca.
- **Ordenação só por `indexed`** (há quanto tempo o arquivo foi indexado) — não existe ordenação por data de commit/push. [external: confirmado na documentação oficial do GitHub REST API — Search code, consultada em 2026-10-01]
- **Rate limit mais restrito que outras buscas:** 10 requisições por minuto para código (autenticado), contra 30/min para outras buscas. [external]
- **Só o branch padrão é considerado**, e apenas arquivos abaixo de um limite de tamanho (384 KB). [external]
- **Até ~4000 repositórios** retornados a partir dos filtros de uma query ampla — buscas muito genéricas não cobrem todo o GitHub. [external]

## Implicação para Secret Scanning (ofensivo e defensivo)

Uma busca ingênua por prefixo de chave (ex.: `sk_live`) tende a devolver repositórios antigos, já bem indexados e irrelevantes para o que acabou de vazar — não o commit mais recente, que é onde uma secret tem maior chance de ainda estar ativa. Do lado defensivo, isso também significa que confiar apenas na busca pública do GitHub para saber se uma credencial da própria empresa vazou é insuficiente: o [[wiki/concepts/secret-scanning]] corporativo (GitHub Advanced Security, push protection) opera sobre o próprio repositório no momento do push, não depende desse índice de busca global.

## Key Sources

- [[wiki/sources/secrets-vazadas-no-github-conceitos-e-riscos]] — introduz o conceito a partir da observação de que busca por prefixo de chave é ineficiente para achar vazamentos recentes
