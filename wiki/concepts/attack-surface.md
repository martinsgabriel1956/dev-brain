---
type: concept
title: "Attack Surface (Superfície de Ataque)"
aliases: ["attack surface", "superfície de ataque", "minimização de superfície", "surface minimization"]
date_created: 2026-06-05
date_updated: 2026-06-05
source_count: 1
tags: [attack-surface, security, arquitetura-seguranca, defense-in-depth, gatekeeper]
skill: tech-mentor-security
status: stable
---

# Attack Surface (Superfície de Ataque)

Conjunto de todos os pontos de entrada que um atacante pode explorar para comprometer um sistema. Quanto maior a superfície, maior o risco — porque mais lugares precisam estar corretos simultaneamente.

## Componentes da Superfície

- Endpoints de API expostos publicamente
- Portas abertas em servidores/containers
- Serviços internos acessíveis de fora (erro de configuração)
- Dependências de terceiros com acesso privilegiado
- Interfaces de administração expostas na internet
- Tokens/credenciais de escopo excessivo

## Redução de Superfície

A pergunta que guia a redução: **"Por que isso precisa estar acessível?"**

- [[concepts/gatekeeper-pattern]] — centraliza todo acesso externo, eliminando portas espalhadas
- [[concepts/valet-key-pattern]] — credenciais de escopo mínimo limitam o impacto de vazamentos
- Desabilitar endpoints não usados
- APIs internas em rede privada, sem exposição pública
- Documentação de API (Swagger/OpenAPI) com autenticação em produção

## Relação com Defense in Depth

[[concepts/defense-in-depth]] e minimização de superfície são complementares: a superfície define quanto você tem para defender; a defesa em profundidade define quantas camadas cobrem cada ponto.

## Exemplos Concretos de Superfície

**URLs públicas de S3 sem autenticação**
"Ninguém vai adivinhar o UUID" não é segurança: URLs aparecem em histórico do browser, histórico do roteador, caches de rede. URLs não são tratadas como dados sensíveis nativamente. Recursos sensíveis no S3 sempre precisam de autenticação.

**IDs sequenciais em endpoints**
`/api/imagens/123` com ID sequencial permite varredura trivial: 124, 125, 126… A pessoa varre todos os registros sem autenticação. Use IDs não-sequenciais (UUID) e autentique o acesso.

**Outputs como vetores**
Não só inputs: logs com dados sensíveis, tempo de resposta variável, tamanho de respostas de erro — tudo pode vazar informação. Ver [[timing-attack]].

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — exemplos: inputs do usuário, S3 público, IDs sequenciais, outputs e timing como vetores
