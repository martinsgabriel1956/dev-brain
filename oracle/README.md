# Oracle

MCP server que expõe busca RAG (Retrieval-Augmented Generation) sobre a wiki pessoal do `dev-brain`. Qualquer client MCP compatível com transporte HTTP (Claude Web, Claude Desktop, Claude Code, Cowork) pode se conectar e consultar o conteúdo ingerido, recebendo trechos relevantes com a fonte de origem para basear a resposta.

## Como funciona

1. Localmente, um script de ingestão lê os arquivos `.md` de `wiki/` e `raw/`, quebra o texto em chunks, gera embeddings via API da OpenAI e grava tudo em uma tabela vetorial no Turso (libSQL).
2. O servidor MCP expõe uma única tool, `search_wiki(query, top_k)`, que embeda a pergunta recebida e faz uma busca por similaridade de cosseno no Turso (via `vector_top_k`), retornando os trechos mais relevantes com a fonte.
3. Quem gera a resposta final em linguagem natural é a LLM do client que chamou a tool (Claude Web, Code, etc.) — o servidor não gera texto, só recupera contexto. É RAG puro, sem geração no lado do servidor.
4. O endpoint HTTP é protegido por um bearer token (`ORACLE_API_KEY`) — sem ele, todo request recebe 401.

## Decisões e motivações

| Decisão | Motivação |
|---|---|
| **Arquitetura: MCP server central** (em vez de conectar Claudes entre si) | Não existe comunicação Claude-para-Claude nativa entre superfícies diferentes (Web, Mobile, Code, Cowork). Um MCP server centraliza a lógica e o estado numa única fonte de verdade; cada client se conecta a ele de forma independente. |
| **Transporte HTTP** (`streamable-http`), não stdio | stdio só funciona para processos locais. Para Web e outras superfícies remotas acessarem o mesmo server, é necessário um endpoint HTTP público. |
| **Python** | Ecossistema de RAG/embeddings mais maduro que Node para esse tipo de pipeline (SDK oficial do MCP, `libsql-client`, `tiktoken`), e o projeto é greenfield — sem legado a considerar. |
| **Turso (libSQL) com vetor nativo** como banco | libSQL tem tipo `F32_BLOB` e índice `vector_top_k` (ANN) embutidos — dispensa um vector DB dedicado (Qdrant, Pinecone) ou um Postgres gerenciado só para pgvector. Tier free do Turso cobre confortavelmente o volume de uma wiki pessoal. |
| **OpenAI `text-embedding-3-small`** para embeddings, em vez de Voyage AI (recomendação oficial da Anthropic) | A Anthropic não tem modelo de embedding próprio — recomenda Voyage AI como parceira. Optou-se por manter o custo mínimo: `text-embedding-3-small` custa ~$0.02/1M tokens, e o volume de conteúdo pessoal (milhares de artigos) gira em torno de centavos de dólar no total. |
| **Ingestão local, sem CI** | Como o Turso já é um banco remoto, o script de ingestão local escreve direto nele — não há necessidade de esperar um push/CI para os dados "chegarem" ao banco. Simplifica o fluxo: roda-se `ingest.py` sob demanda após adicionar conteúdo novo. |
| **Deploy no Railway (plano Hobby, $5/mês)** | Alternativa ao Fly.io (que não tem mais tier gratuito permanente). O Hobby plan já inclui $5 de crédito de uso, suficiente para um servidor leve e majoritariamente ocioso como esse. |
| **Auth via bearer token estático**, não OAuth | Uso pessoal, um único "client" (você, em diferentes superfícies). Um token fixo comparado no header já corta acesso não autorizado ao endpoint público; OAuth completo seria complexidade sem benefício aqui. |
| **RAG puro (sem geração no servidor)** | O servidor só recupera e retorna contexto relevante; a resposta em linguagem natural é responsabilidade da LLM que chamou a tool. Mantém o server simples e desacoplado de qual modelo está consultando. |

### Trade-offs conhecidos

- **Mobile (app Claude) não tem suporte a MCP custom** no momento — essa superfície fica de fora do alcance do oráculo.
- **Token único e estático**, sem rotação ou escopo por client. Suficiente para uso pessoal; se mais gente precisar de acesso, migrar para um token por client ou OAuth.

## Estrutura do projeto

```
oracle/
  config.py       # variáveis de ambiente e parâmetros (modelo de embedding, chunking)
  db.py           # client Supabase: insert, delete, busca por similaridade
  chunking.py     # quebra de texto em chunks com overlap (tiktoken)
  ingest.py       # script de ingestão: wiki/ e raw/ -> embeddings -> Supabase
  server.py       # servidor MCP (FastMCP), tool search_wiki, transporte HTTP
  schema.sql      # schema Postgres/pgvector + função match_documents
  Dockerfile      # imagem para deploy (Railway/Fly.io)
  .env.example    # variáveis necessárias
```

## Setup

### 1. Banco de dados

Crie um banco no Turso (`turso db create oracle`) e rode o conteúdo de `schema.sql` nele (`turso db shell oracle < schema.sql`) para criar a tabela `documents` com a coluna vetorial e o índice `vector_top_k`.

### 2. Variáveis de ambiente

```bash
cp .env.example .env
```

Preencha:

- `OPENAI_API_KEY` — chave da API da OpenAI, usada para gerar embeddings.
- `TURSO_DATABASE_URL` — URL do banco (`turso db show oracle --url`).
- `TURSO_AUTH_TOKEN` — token de acesso ao banco (`turso db tokens create oracle`).
- `ORACLE_API_KEY` — token que você escolhe, usado para autenticar as chamadas ao endpoint MCP.

### 3. Instalar dependências

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install .
```

### 4. Ingerir conteúdo

```bash
python ingest.py --source all   # ou --source wiki / --source raw
```

Reingerir um arquivo já processado apaga os chunks antigos daquela fonte antes de gravar os novos — seguro rodar quantas vezes quiser.

### 5. Rodar o servidor

```bash
python server.py
```

Sobe em `0.0.0.0:8000` com transporte `streamable-http`.

## Deploy

O `Dockerfile` está pronto para build e deploy no Railway (plano Hobby) ou Render. Configure as mesmas variáveis de ambiente do `.env` como secrets da plataforma escolhida.

No client MCP (Claude Desktop/Code/Web), aponte para a URL pública do servidor e envie o header `Authorization: Bearer <ORACLE_API_KEY>`.

## Custo estimado

- **Embeddings (OpenAI):** ~$0.02 por 1M tokens — para milhares de artigos pessoais, o total fica na casa de centavos de dólar.
- **Banco (Turso):** grátis no tier free (500 bancos, 9GB de storage e 1B de reads/mês — bem acima do necessário para uma wiki pessoal).
- **Hosting (Railway Hobby):** $5/mês fixo, cobrindo o uso esperado de um servidor leve e majoritariamente ocioso.

## Próximos passos

- Avaliar suporte a MCP no app mobile quando/se disponível.
- Se o token único virar um problema (mais de um usuário/client), migrar para um token por client.
