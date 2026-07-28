---
type: source
title: "Connection Pooling — Pool vs. Polling, Vazamento de Conexão e Serverless"
aliases: ["pool vs polling", "client.release", "connection pooling serverless", "rds proxy lambda"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 0
tags: [connection-pooling, pgbouncer, rds-proxy, serverless, lambda, singleton, postgresql, banco-de-dados]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/connection-pooling-pool-vs-polling-serverless.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-28
---

# Connection Pooling — Pool vs. Polling, Vazamento de Conexão e Serverless

## TL;DR

Vídeo introdutório sobre connection pooling que cobre três ângulos pouco documentados na wiki até agora: (1) desambiguação *poll* (polling, pesquisa repetida) vs. *pool* (piscina de conexões); (2) o bug prático mais comum — instanciar a pool corretamente como singleton fora do handler de rota, mas esquecer `client.release()` num `finally`, vazando conexões da pool uma a uma até estourar; (3) o problema estrutural de connection pooling em ambientes serverless (Lambda não tem memória compartilhada entre invocações) e as soluções dependentes de plataforma — RDS Proxy (AWS), "attach database pool" (Vercel, lock-in de plataforma), suporte nativo de ORMs, e PgBouncer (citado com disclaimer explícito do autor de que nunca usou).

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| *Poll* (polling) e *pool* (piscina de conexões) são termos frequentemente confundidos por falantes de português | Observação didática do autor | Alta |
| Uma conexão por cliente funciona até ~20-30 usuários simultâneos, depois degrada | Experiência prática do autor | Média — número é estimativa qualitativa, não benchmark |
| Criar conexão é caro: handshake de rede, autenticação, processos em ambos os lados, TLS | Conhecimento consolidado de banco de dados | Alta |
| Em Node.js, um arquivo é um singleton — a pool deve ser instanciada fora da rota para ser reutilizada entre requests | Comportamento de módulos Node.js (`require`/`import` cacheado) | Alta |
| Esquecer `client.release()` vazando conexões aos poucos até esgotar a pool é um bug visto em produção pelo autor | Relato de experiência do autor | Média — anedota pessoal, sem fonte externa |
| `finally` (ou equivalente) é necessário para garantir release mesmo com erro na query | Padrão de tratamento de recursos | Alta |
| Lambda não tem memória compartilhada entre invocações — cada invocação é autossuficiente, inviabilizando pool "normal" no código de negócio | Modelo de execução serverless da AWS | Alta |
| RDS Proxy é uma das soluções mais usadas para pooling em Lambda na AWS | Prática de mercado citada pelo autor | Média — não checado contra a documentação oficial da AWS neste ingest |
| Vercel oferece "attach database pool" nas Vercel Functions como solução própria (lock-in de plataforma) | Citação da documentação da Vercel pelo autor | Média — não verificado diretamente na doc da Vercel |
| PgBouncer também funciona como proxy de pooling para serverless | Citado pelo autor com disclaimer explícito de nunca ter usado | Baixa — autor pede uso com cautela |

## Conceitos

- [[wiki/concepts/connection-pooling]] — já existe no index; conteúdo central desta fonte
- [[wiki/concepts/singleton-pattern]] — pool instanciada como singleton fora do handler de rota
- [[wiki/concepts/postgresql]] — banco de referência dos exemplos (`pg`/`Pool`/`client.release`)

## Key Sources

_Este é o documento primário._
