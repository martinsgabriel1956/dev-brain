---
type: concept
title: "Requisição e Resposta"
aliases: ["request-response", "ciclo de requisição", "request/response cycle"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [http, backend, api, requisicao, resposta, status-code]
skill: tech-mentor-backend
status: stub
---

# Requisição e Resposta

O idioma básico de todo backend: um cliente envia uma **requisição**, o servidor processa e devolve uma **resposta**. Toda a arquitetura de um sistema — [[wiki/concepts/contrato-de-api]], autenticação, cache, filas — existe para decidir o que acontece entre essas duas pontas.

## Anatomia da Requisição

- **Método** — GET (buscar), POST (criar), PUT/PATCH (atualizar), DELETE (remover)
- **Rota** — ex. `/api/orders`
- **Headers** — metadados: token, idioma, tipo de conteúdo
- **Body** — corpo da mensagem (nem toda requisição tem)

## Anatomia da Resposta

O **status code** comunica o resultado:

| Faixa | Significado | Exemplo |
|---|---|---|
| 2xx | Sucesso | 200 OK |
| 4xx | Erro do cliente | 401 não autenticado, 404 não encontrado |
| 5xx | Erro do servidor | 500 erro interno |

## Relação com outros conceitos

- [[wiki/concepts/contrato-de-api]] — formaliza o formato de requisição/resposta entre cliente e servidor
- [[wiki/concepts/autenticacao-e-autorizacao]] — geralmente viaja como header na requisição
- [[wiki/concepts/observabilidade]] — cada requisição é o evento mais granular que logs, métricas e traces observam

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
