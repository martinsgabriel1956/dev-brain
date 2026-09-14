---
type: source
title: "MCP Stateless: Fim do Handshake e Server Discover"
aliases: ["mcp stateless", "mcp fim do handshake", "server discover mcp", "mcp comanda de restaurante"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/mcp-stateless-fim-do-handshake-server-discover-lucas-montano.md
source_url: ""
author: "Lucas Montano (atribuição provável — auto-referência explícita no fechamento e cupom de patrocínio Hostinger nominal, mesmo padrão de fontes anteriores)"
date_published: ""
date_ingested: 2026-09-14
source_count: 0
tags: [mcp, model-context-protocol, stateless, server-discover, handshake, streamable-http, anthropic, hostinger]
skill: tech-mentor-ai
status: stable
---

## TL;DR

A Anthropic mudou a especificação core do MCP de stateful/bidirecional para **stateless no core** (mudança relatada como "da semana anterior" ao vídeo). O handshake que abria e mantinha uma sessão MCP acaba: cada POST agora se descreve sozinho via dois headers novos (método + recurso), um método `server discover` passa a ser obrigatório no servidor (opcional no cliente) para anunciar versão/capabilities/identidade, e estado entre chamadas ("cross-call state") passa a ser um **handle opaco assinado pelo servidor**, devolvido ao cliente e reenviado como argumento normal — não mais mantido em sessão no transporte. Isso permite deploy serverless/edge sem Redis/sticky session/session store, e round robin "burro" num load balancer comum.

## Key Claims

**Claim:** A especificação core do MCP deixou de exigir handshake/sessão stateful e passou a ser stateless, baseada em request/response simples.
**Evidence:** Citação direta do changelog da Anthropic (parafraseada na fonte): "remote MCP servers effectively become standard HTTP endpoints which scale cleanly with enterprise workloads" — não é mais necessário Redis, sticky session ou session store; tu pode implementar um round robin "burro" numa VPS sem infraestrutura adicional de sessão.
**Confidence:** média — a mudança de spec em si é relatada com citação textual do changelog, mas o vídeo não anexa link/PDF do changelog original nem data exata de publicação ("semana passada" em relação à data do vídeo, não confirmada). Nenhuma fonte primária foi lida diretamente nesta ingestão — tratar o mecanismo técnico específico como relato de segunda mão até confirmação com a spec oficial em `modelcontextprotocol.io`.

**Claim:** Estado entre chamadas ("cross-call state") agora é um handle opaco, assinado/mintado pelo servidor, passado como argumento comum de tool — não mais mantido implicitamente pelo transporte/sessão.
**Evidence:** Citação do changelog: "Servers that need cross-call state should use explicit, server-minted handles passed as ordinary tool arguments." A fonte usa a analogia da comanda de restaurante: o servidor "cunha" um número (o handle) e devolve ao cliente; qualquer instância do servidor (qualquer "garçom") pode atender a próxima chamada porque o estado está na comanda, não na memória de quem atendeu antes.
**Confidence:** alta quanto à citação textual do changelog; média quanto ao mecanismo criptográfico exato de assinatura (a fonte não detalha algoritmo, apenas os três atributos que precisam ser garantidos: dono, validade e propósito da emissão — mapeados na documentação oficial, segundo a fonte, à seção "server requirements" de "multi-round trip requests" em `modelcontextprotocol.io`, não conferida nesta ingestão).

**Claim:** Um novo método `server discover` passa a ser obrigatório do lado do servidor MCP (mas opcional do lado do cliente), anunciando versão, capabilities e identidade; versão incompatível retorna erro de versão.
**Evidence:** Descrito diretamente na fonte, sem trecho literal do changelog citado para essa parte específica (diferente das duas claims acima, que vêm com citação textual).
**Confidence:** média — sem citação textual direta do changelog para este método específico, ao contrário das duas claims anteriores.

**Claim:** Dois headers novos no MCP request permitem que proxies/gateways (Nginx, rate limiter) distingam método e recurso sem abrir o body da requisição, possibilitando rate limits diferentes por tipo de operação (ex.: listar tools vs. rodar uma tool de autenticação).
**Evidence:** Antes da mudança, um proxy não sabia se um POST em `/mcp` era um "list tools" (deveria levar milissegundos) ou uma chamada de tool com efeito colateral (ex.: autenticação OAuth), impedindo rate limits diferenciados por operação. Com os headers, essa distinção fica visível no nível de transporte.
**Confidence:** alta quanto ao problema descrito (plausível e coerente com a arquitetura de proxy reversa); média quanto ao nome/formato exato dos headers, que a fonte não cita literalmente.

**Claim:** MCP superou 400 milhões de downloads mensais do SDK (4× mais que no ano anterior) e o Claude (produto) tem 950 MCP servers listados.
**Evidence:** Citado como estatística no vídeo, sem link para relatório oficial da Anthropic.
**Confidence:** baixa quanto à precisão do número — não verificado contra fonte primária nesta ingestão. Tratar como não confirmado externamente, seguindo o padrão já registrado para outras estatísticas não verificadas citadas em vídeos na wiki (ver [[wiki/entities/anthropic]]).

**Claim:** Com a mudança stateless, um MCP server simples cabe num único arquivo, sem depender do MCP TypeScript SDK oficial.
**Evidence:** A fonte relata ter escrito o roteiro do vídeo antes de uma nova versão do SDK ter sido lançada, e que a simplicidade do protocolo (POST único, request/response) torna viável implementar o servidor "na mão".
**Confidence:** média — plausível dado o desenho descrito (request/response simples), mas não demonstrado com código na transcrição (o vídeo é falado, sem trechos de implementação colados nesta fonte).

## Entities & Concepts Touched

- [[wiki/concepts/model-context-protocol]]
- [[wiki/concepts/mcp-arquitetura]]
- [[wiki/concepts/mcp-server]]
- [[wiki/concepts/cli-vs-mcp]]
- [[wiki/concepts/mcp-stateless-server-discover]]
- [[wiki/entities/anthropic]]
- [[wiki/entities/lucas-montano]]
- [[wiki/entities/hostinger]]
- [[wiki/entities/claude-code]]

## Open Questions

- **Nenhuma fonte primária (changelog oficial da Anthropic ou spec atualizada em `modelcontextprotocol.io`) foi lida diretamente nesta ingestão** — todo o mecanismo técnico (headers exatos, algoritmo de assinatura do handle, formato do `server discover`) vem exclusivamente da narração do vídeo, com apenas duas citações textuais curtas do changelog. Fica em aberto: qual é a versão exata da spec que introduziu essa mudança, e se ela já está em `modelcontextprotocol.io/specification` no momento desta ingestão (2026-09-14).
- **Contradição/desatualização com páginas existentes da wiki:** [[wiki/concepts/cli-vs-mcp]] descreve descoberta de tools como "dinâmica via handshake" — essa premissa fica desatualizada se a mudança relatada aqui for confirmada (handshake deixa de ser parte obrigatória do protocolo). [[wiki/concepts/mcp-arquitetura]] também descreve "handshake entre host e servers registrados" como explicação do tempo de inicialização de harnesses — mesmo ponto de tensão. Ambas as páginas foram atualizadas nesta ingestão com uma seção específica sinalizando a mudança relatada nesta fonte, sem apagar o conteúdo anterior (que ainda descreve o modelo pré-mudança, relevante para servers MCP legados/stdio locais que a fonte não afirma que deixam de existir).
- **`references/ai/mcp.md` da skill `tech-mentor-ai` está desatualizada em relação a essa mudança** — o arquivo de referência documenta SSE deprecado em favor de Streamable HTTP (2025) e sessão via `sessionIdGenerator`/`mcp-session-id` como padrão atual, sem mencionar a remoção do handshake nem o `server discover`. Como a skill é read-only para o agente (invariante do repositório), isso não pode ser corrigido diretamente — registrado aqui como lacuna de calibração de domínio a considerar em uma futura atualização da skill pelo usuário.
- Autoria do vídeo (Lucas Montano) é inferida por convergência de sinais (auto-menção do canal no fechamento, cupom de patrocínio nominal "Lucas Montano" para Hostinger — mesmo padrão de [[wiki/sources/loop-engineering-guia-pratico-casos-reais-desastres-lucas-montano]] e [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]]), não por identificação nominal direta do canal na transcrição.
- Raw file não veio de um documento preexistente — o usuário colou a transcrição diretamente no prompt e pediu explicitamente para primeiro criar o Markdown em `raw/`, depois ingerir.

## Raw Quotes

> "A Anthropic tá matando o handshake do MCP. [...] o teu servidor remoto ele é só um post que roda em qualquer máquina."

> "Remote MCP servers effectively become standard HTTP endpoints which scale cleanly with enterprise workloads."

> "Servers that need cross-call state [should] use explicit, server-minted handles passed as ordinary tool arguments."

> "O estado agora tá na mão do cliente, ele não tá mais com o garçom — que no caso seria o teu MCP."
