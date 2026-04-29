---
date: 2026-04-08
tags: [tech-mentor, ia, mcp, model-context-protocol, tools, resources, prompts, sampling, a2a, oauth, streamable-http]
skill: tech-mentor-ai/references/ai/mcp.md
level: intermediário
---

# Model Context Protocol (MCP)

## Contexto

MCP é o protocolo padrão de fato para integração de ferramentas em LLMs desde 2025. Antes do MCP, cada integração era proprietária — function calling do OpenAI, plugins do ChatGPT, Gemini Functions. Código duplicado, sem reuso entre clientes. MCP define um contrato único que qualquer host e qualquer servidor pode implementar: o "USB-C das integrações de AI".

---

## Como Funciona

### Arquitetura

```
[Host / LLM Client]  ←──── MCP Protocol ────→  [MCP Server]
  Claude Desktop              JSON-RPC 2.0         Postgres
  VS Code Copilot             Streamable HTTP       GitHub
  App customizado             ou stdio              Filesystem
                                                    API interna
```

**Três papéis:**
- **Host:** o cliente que usa o LLM (Claude Desktop, VS Code, app customizado)
- **Client:** componente dentro do host que gerencia conexões MCP
- **Server:** serviço que expõe tools, resources e prompts

### Quatro primitivas

| Primitiva | Natureza | Quando usar |
|---|---|---|
| **Tools** | Ação / side effect — LLM decide quando chamar | Criar pedido, buscar dados, enviar e-mail |
| **Resources** | Leitura de dados — LLM ou user solicita explicitamente | Schema do banco, documentação, config |
| **Prompts** | Templates reutilizáveis com argumentos | Workflows frequentes com dados dinâmicos |
| **Sampling** | Server pede completion ao client | Server precisa do LLM do client para processar |

---

## Transporte

### stdio — processos locais

```
Host spawna o processo → stdin/stdout como canal
Latência zero, sem rede
Ideal para: ferramentas CLI, integração local (Claude Desktop, VS Code)
```

### Streamable HTTP — servidores remotos (padrão atual)

O SSE foi **deprecado em 2025** e substituído pelo Streamable HTTP. Usa HTTP normal com upgrade opcional para streaming — mais compatível com proxies e load balancers.

```
POST /mcp → envia e recebe na mesma conexão
           faz upgrade para SSE se resposta for longa
```

```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import express from "express";

const server = new McpServer({ name: "orders-mcp", version: "1.0.0" });
const app = express();

app.post("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: () => crypto.randomUUID() });
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});
```

---

## Tools

```typescript
import { z } from "zod";

server.tool(
  "search_products",
  "Search products by name, category or price range. Returns matching products with stock info. Does not support fuzzy search.",
  {
    query: z.string().describe("Search term (name or description)"),
    category: z.enum(["electronics", "clothing", "food"]).optional(),
    max_price: z.number().positive().optional().describe("Maximum price in BRL"),
    limit: z.number().int().min(1).max(50).default(10)
  },
  async ({ query, category, max_price, limit }) => {
    try {
      const products = await searchProducts({ query, category, max_price, limit });

      if (products.length === 0) {
        return { content: [{ type: "text", text: "No products found matching your criteria." }] };
      }

      const formatted = products
        .map(p => `- ${p.name} | R$${p.price} | Stock: ${p.stock} | ID: ${p.id}`)
        .join("\n");

      return { content: [{ type: "text", text: `Found ${products.length} products:\n${formatted}` }] };
    } catch (err) {
      // Retornar erro como dado — LLM consegue raciocinar sobre ele
      return { content: [{ type: "text", text: `Search failed: ${err.message}` }], isError: true };
    }
  }
);
```

**Regras para descriptions que o LLM usa bem:**
- Descreva quando usar E quando não usar
- Descreva o que retorna, não só o que recebe
- Inclua limitações: "Returns up to 50 results", "Does not support fuzzy search"
- Seja específico sobre o formato dos argumentos

**Boas práticas de tool design:**
- Idempotência obrigatória para tools com efeitos colaterais
- Timeout de 30s para tools externas — retorne status parcial se necessário
- Erros como dados com `isError: true` — o LLM tenta alternativas quando vê o erro
- Escopo mínimo — uma tool específica por operação, nunca `query_database(sql)` livre

---

## Resources

Dados que o LLM pode ler sem invocar uma tool. Cacheable — não têm efeitos colaterais.

```typescript
import { ResourceTemplate } from "@modelcontextprotocol/sdk/server/mcp.js";

// Resource estático
server.resource(
  "api-schema",
  "openapi://schema",
  async uri => ({
    contents: [{
      uri: uri.toString(),
      text: await fs.readFile("./openapi.yaml", "utf8"),
      mimeType: "text/yaml"
    }]
  })
);

// Resource dinâmico com template URI
server.resource(
  "customer-profile",
  new ResourceTemplate("customer://{id}/profile", { list: undefined }),
  async (uri, { id }) => {
    const customer = await db.customers.findUnique({ where: { id } });
    return {
      contents: [{
        uri: uri.toString(),
        text: JSON.stringify(customer, null, 2),
        mimeType: "application/json"
      }]
    };
  }
);
```

---

## Prompts — Templates Reutilizáveis

```typescript
server.prompt(
  "analyze-order-issues",
  "Analyze patterns in failed orders for a given period",
  {
    start_date: z.string().describe("ISO 8601 date"),
    end_date: z.string().describe("ISO 8601 date"),
    group_by: z.enum(["reason", "product", "customer_region"]).default("reason")
  },
  async ({ start_date, end_date, group_by }) => {
    const data = await getFailedOrders(start_date, end_date, group_by);
    return {
      messages: [{
        role: "user",
        content: {
          type: "text",
          text: `Analyze the following failed order data and identify the top 3 actionable improvements:\n\n${JSON.stringify(data, null, 2)}`
        }
      }]
    };
  }
);
```

---

## Sampling — Server pede Completion ao Client

Primitiva menos conhecida: o servidor MCP pode pedir ao host que faça uma chamada LLM, sem ter acesso direto ao modelo.

```typescript
// Servidor solicita sampling ao client durante execução de uma tool
server.setRequestHandler(CallToolRequestSchema, async (request, extra) => {
  if (request.params.name === "analyze_data") {
    const data = await fetchData(request.params.arguments.query);

    // LLM do client processa os dados
    const llmResponse = await extra.requestSampling({
      messages: [{ role: "user", content: { type: "text", text: `Analyze: ${data}` } }],
      maxTokens: 1000
    });

    return { content: [{ type: "text", text: llmResponse.content.text }] };
  }
});
```

**Caso de uso:** servidor de análise que precisa do LLM para interpretar dados sem ter chave de API própria.

---

## MCP Client — Consumindo Servidores

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "node",
  args: ["./my-mcp-server.js"]
});

const client = new Client(
  { name: "my-client", version: "1.0.0" },
  { capabilities: { tools: {}, resources: {}, prompts: {} } }
);

await client.connect(transport);

// Listar tools disponíveis
const { tools } = await client.listTools();

// Chamar uma tool
const result = await client.callTool({
  name: "search_orders",
  arguments: { customerId: "cust_123", status: "pending" }
});
```

---

## MCP OAuth — Autenticação Segura

MCP tem spec oficial de autenticação baseada em OAuth 2.1 + PKCE.

```
Client → GET /.well-known/oauth-authorization-server → discovery
Client → POST /authorize (PKCE code_challenge)
User   → autentica no authorization server
Client → recebe authorization code
Client → POST /token → access_token
Client → Bearer token em todas as chamadas MCP
```

```typescript
import { OAuthClientProvider } from "@modelcontextprotocol/sdk/client/auth.js";

const transport = new StreamableHTTPClientTransport(
  new URL("https://api.empresa.com/mcp"),
  {
    authProvider: new OAuthClientProvider({
      clientId: process.env.MCP_CLIENT_ID,
      redirectUrl: "http://localhost:3000/callback",
      scopes: ["mcp:read", "mcp:write"]
    })
  }
);
```

---

## MCP Roots — Escopo de Filesystem

Roots limitam quais diretórios o servidor MCP pode acessar. Segurança por design.

```typescript
// Servidor valida que paths estão dentro dos roots declarados pelo client
function isPathAllowed(path: string, roots: Root[]): boolean {
  return roots.some(root => path.startsWith(new URL(root.uri).pathname));
}

// Antes de qualquer operação no filesystem
const { roots } = await client.listRoots();
if (!isPathAllowed(requestedPath, roots)) {
  throw new Error(`Access to ${requestedPath} not allowed by client roots`);
}
```

---

## Multi-tenant — Isolamento por Sessão

```typescript
const sessions = new Map<string, UserContext>();

app.post("/mcp", async (req, res) => {
  const sessionId = req.headers["mcp-session-id"] as string;
  const userId = await validateToken(req.headers.authorization);

  if (!sessions.has(sessionId)) {
    sessions.set(sessionId, {
      userId,
      dbConnection: await createUserScopedDB(userId),
      permissions: await getUserPermissions(userId)
    });
  }

  const transport = new StreamableHTTPServerTransport({ sessionId });
  const server = createServerForSession(sessions.get(sessionId)!);
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
});
```

---

## A2A Protocol (Google) — Agent-to-Agent

Protocolo complementar ao MCP para comunicação entre agentes de diferentes stacks.

```
MCP:  Agent ←→ Tool / DB / File      (agente ↔ ferramentas)
A2A:  Agent A ←→ Agent B              (agente ↔ agente)
```

Cada agente A2A publica um `/.well-known/agent.json` descrevendo suas skills:

```json
{
  "name": "OrderAgent",
  "url": "https://agents.acme.com/order",
  "skills": [
    {
      "id": "create_order",
      "name": "Create Order",
      "description": "Creates a new purchase order. Requires product_id, quantity, customer_id.",
      "inputModes": ["application/json"],
      "outputModes": ["application/json"]
    }
  ],
  "authentication": { "schemes": ["Bearer"] },
  "capabilities": { "streaming": true }
}
```

**Lifecycle de uma task A2A:**
```
submitted → working → [input-required] → working → completed
                                                  ↘ failed | canceled
```

**Quando usar A2A vs chamada direta:**
```
A2A quando:
  Agentes são de stacks diferentes (Python ↔ TypeScript)
  Agente remoto é de outro time ou organização
  Descoberta dinâmica de capacidades (Agent Card)
  Auditoria e rate limiting por agente

Chamada direta quando:
  Agentes no mesmo processo ou serviço
  Performance crítica (A2A adiciona overhead HTTP)
  Prototipagem e desenvolvimento
```

**Status 2025/2026:** A2A em draft ativo com adoção crescente no ecossistema Google. MCP mais maduro e com maior adoção geral — ambos coexistirão.

---

## MCP vs Function Calling Direto

| Critério | MCP Server | Function Calling direto |
|---|---|---|
| Reuso | ✅ Qualquer host MCP | ❌ Acoplado ao provider |
| Deploy | ✅ Serviço independente | Código inline no app |
| Overhead | Latência de rede | Zero overhead |
| Segurança | Isolamento natural | Compartilha processo |

**Use MCP quando:** a mesma integração precisa funcionar em múltiplos clientes, ou ferramenta é um serviço independente entregue por um time de plataforma.

**Use function calling direto quando:** app único, sem reuso, latência crítica ou prototipagem.

---

## Conceitos Relacionados

[[agentes-core]] · [[agentes-orquestracao]] · [[structured-outputs-function-calling]] · [[ai-safety-engineering]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
