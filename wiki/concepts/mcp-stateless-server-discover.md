---
type: concept
title: "MCP Stateless e Server Discover (Mudança de Spec 2026)"
aliases: ["mcp stateless", "server discover", "fim do handshake mcp", "cross-call state mcp", "handle mintado mcp"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [mcp, model-context-protocol, stateless, server-discover, handshake, streamable-http, serverless, anthropic]
skill: tech-mentor-ai
status: stub
---

# MCP Stateless e Server Discover (Mudança de Spec 2026)

## TL;DR

Mudança relatada na especificação core do [[wiki/concepts/model-context-protocol|MCP]]: o protocolo deixa de exigir handshake e sessão stateful, passando a ser stateless no núcleo — cada requisição (um POST simples) se descreve por completo sozinha. Um método `server discover`, obrigatório no servidor e opcional no cliente, substitui parte do papel do handshake antigo (anunciar versão, capabilities, identidade). Estado entre chamadas ("cross-call state") deixa de viver na sessão de transporte e vira um **handle opaco, assinado e mintado pelo servidor**, devolvido ao cliente e reenviado como argumento comum de tool na chamada seguinte.

## Por que a mudança importa

Antes, hospedar um MCP server exigia lidar com estado — Redis, sticky session, session store — porque o protocolo mantinha uma sessão viva entre client e server (ver a descrição pré-mudança em [[wiki/concepts/mcp-arquitetura]]). Isso dificultava (ou impedia) deploy serverless/edge, porque uma function efêmera não consegue manter conexão persistente com um cliente. Com o core stateless, servidores remotos MCP "efetivamente se tornam endpoints HTTP padrão, que escalam de forma limpa com carga enterprise" (citação do changelog da Anthropic, via [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]]) — viabilizando round robin comum num load balancer, sem infraestrutura de sessão dedicada.

## Handle Mintado — A Analogia da Comanda de Restaurante

O padrão para estado entre chamadas: o servidor gera ("minta") um handle opaco — como uma comanda numerada de restaurante — e devolve ao cliente. O cliente reenvia esse handle como um argumento comum de tool na próxima chamada. Qualquer instância do servidor pode processar essa chamada, porque o estado está na comanda, não na memória de quem atendeu antes. Isso desloca o estado da camada de transporte do protocolo para os dados — como um argumento qualquer.

**Implicação de segurança**: como a comanda passa pela mão do cliente, ela precisa ser assinada, garantindo três propriedades — quem é o dono, prazo de validade, e para que foi emitida (evitando reuso de uma comanda de checkout, por exemplo, para uma operação diferente como adicionar item ao carrinho).

## Multi-round Trip Requests — Interatividade sem Sessão Aberta

Mesmo sem handshake nem stream aberto, o servidor ainda pode pedir mais informação ao cliente: cliente chama com ID e parâmetros; servidor responde pedindo mais dados; cliente reenvia com os dados completos; servidor retorna resultado para aquele ID. Cada ida é um POST/request independente (IDs sequenciais, não a mesma conexão mantida aberta) — se algo falhar no meio do caminho, o cliente simplesmente faz retry, e esse retry pode cair em qualquer instância nova da função.

## Headers de Método e Recurso

Dois headers novos permitem que um proxy (Nginx, gateway, rate limiter) identifique método e recurso da requisição **sem abrir o body**. Antes, um proxy não sabia se um POST em `/mcp` pedia para listar tools (deveria levar milissegundos) ou para rodar uma tool com efeito colateral (ex.: autenticação OAuth, que pode levar segundos e exige rate limit mais restritivo). Com os headers, é possível aplicar políticas de rate limit diferentes por tipo de operação sem inspecionar o payload.

## Server Discover

Método obrigatório do lado do servidor (opcional do lado do cliente) que anuncia versão do protocolo suportada, capabilities e identidade do servidor. Uma versão incompatível ou ausente resulta em erro de versão retornado pelo servidor.

## Relação com Streamable HTTP e SSE

[[wiki/concepts/mcp-arquitetura]] já documenta a migração de SSE (deprecado) para Streamable HTTP como transporte atual do MCP, com sessão identificada via `sessionIdGenerator`/header `mcp-session-id`. A mudança descrita aqui vai além: não apenas troca o transporte, mas remove a exigência de sessão persistente do **core da especificação**, deixando Streamable HTTP (e qualquer mecanismo de sessão sobre ele) como opcional/adicional, não mais obrigatório pelo protocolo.

## Status de Verificação

Esta página está marcada como **stub**: baseada em uma única fonte de segunda mão (vídeo do YouTube), sem confirmação direta na spec oficial em `modelcontextprotocol.io`. Duas citações textuais do changelog da Anthropic foram preservadas na fonte, mas o mecanismo técnico completo (formato exato dos headers, algoritmo de assinatura do handle) não foi verificado contra documentação primária. Promover a `stable` requer cruzar com a especificação oficial.

## Key Sources

- [[wiki/sources/mcp-stateless-fim-do-handshake-server-discover-lucas-montano]]
