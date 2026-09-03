# Oracle

MCP server que expõe busca RAG (Retrieval-Augmented Generation) sobre a wiki pessoal do `dev-brain`. Qualquer client MCP compatível com transporte HTTP (Claude Web, Claude Desktop, Claude Code, Cowork) pode se conectar e consultar o conteúdo ingerido, recebendo trechos relevantes com a fonte de origem para basear a resposta.

## Como funciona

1. Localmente, um script de ingestão lê os arquivos `.md` de `wiki/` e `raw/`, quebra o texto em chunks, gera embeddings via API da OpenAI e grava tudo em uma tabela vetorial no Supabase (pgvector).
2. O servidor MCP expõe uma única tool, `search_wiki(query, top_k)`, que embeda a pergunta recebida e faz uma busca por similaridade de cosseno no Supabase, retornando os trechos mais relevantes com a fonte.
3. Quem gera a resposta final em linguagem natural é a LLM do client que chamou a tool (Claude Web, Code, etc.) — o servidor não gera texto, só recupera contexto. É RAG puro, sem geração no lado do servidor.

## Decisões e motivações

| Decisão | Motivação |
|---|---|
| **Arquitetura: MCP server central** (em vez de conectar Claudes entre si) | Não existe comunicação Claude-para-Claude nativa entre superfícies diferentes (Web, Mobile, Code, Cowork). Um MCP server centraliza a lógica e o estado numa única fonte de verdade; cada client se conecta a ele de forma independente. |
| **Transporte HTTP** (`streamable-http`), não stdio | stdio só funciona para processos locais. Para Web e outras superfícies remotas acessarem o mesmo server, é necessário um endpoint HTTP público. |
| **Python** | Ecossistema de RAG/embeddings mais maduro que Node para esse tipo de pipeline (SDK oficial do MCP, `supabase-py`, `tiktoken`), e o projeto é greenfield — sem legado a considerar. |
| **Supabase + pgvector** como banco vetorial | Bundla Postgres + busca vetorial + auth em um único serviço gerenciado, com tier gratuito que comporta ~50–80 mil vetores (1536 dims). Evita rodar um vector DB dedicado (Qdrant, Pinecone) só para esse volume pessoal. |
| **OpenAI `text-embedding-3-small`** para embeddings, em vez de Voyage AI (recomendação oficial da Anthropic) | A Anthropic não tem modelo de embedding próprio — recomenda Voyage AI como parceira. Optou-se por manter o custo mínimo: `text-embedding-3-small` custa ~$0.02/1M tokens, e o volume de conteúdo pessoal (milhares de artigos) gira em torno de centavos de dólar no total. |
| **Ingestão local, sem CI** | Como o Supabase já é um banco remoto, o script de ingestão local escreve direto nele — não há necessidade de esperar um push/CI para os dados "chegarem" ao banco. Simplifica o fluxo: roda-se `ingest.py` sob demanda após adicionar conteúdo novo. |
| **Deploy no Railway (plano Hobby, $5/mês)** | Alternativa ao Fly.io (que não tem mais tier gratuito permanente). O Hobby plan já inclui $5 de crédito de uso, suficiente para um servidor leve e majoritariamente ocioso como esse. |
| **Conexão Railway → Supabase via Supavisor (pooler)**, não conexão direta | O Supabase usa IPv6 por padrão na conexão direta, e o Railway tem problemas conhecidos de conectividade IPv6 (`ENETUNREACH`). A connection string do pooler é IPv4-compatible e evita o problema. |
| **RAG puro (sem geração no servidor)** | O servidor só recupera e retorna contexto relevante; a resposta em linguagem natural é responsabilidade da LLM que chamou a tool. Mantém o server simples e desacoplado de qual modelo está consultando. |

### Trade-offs conhecidos

- **Supabase free tier pausa após 7 dias de inatividade.** Se o servidor precisar responder de forma imprevisível a qualquer momento, o plano Pro ($25/mês) remove essa pausa. Por ora, aceito o risco do tier gratuito.
- **Mobile (app Claude) não tem suporte a MCP custom** no momento — essa superfície fica de fora do alcance do oráculo.
- **Sem auth implementada ainda.** Como o transporte é HTTP público, autenticação (API key ou OAuth) é um requisito antes de expor o server publicamente — ainda não implementado neste esqueleto.

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

No SQL Editor do projeto Supabase, rode o conteúdo de `schema.sql` para criar a extensão `vector`, a tabela `documents` e a função `match_documents`.

### 2. Variáveis de ambiente

```bash
cp .env.example .env
```

Preencha:

- `OPENAI_API_KEY` — chave da API da OpenAI, usada para gerar embeddings.
- `SUPABASE_URL` — connection string do projeto (usar o pooler/Supavisor quando fizer deploy no Railway).
- `SUPABASE_SERVICE_KEY` — service role key do Supabase (necessária para escrever na tabela via `db.py`).

### 3. Instalar dependências

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install mcp openai supabase python-dotenv tiktoken
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

O `Dockerfile` está pronto para build e deploy no Railway (plano Hobby) ou Fly.io. Configure as mesmas variáveis de ambiente do `.env` como secrets da plataforma escolhida, e aponte `SUPABASE_URL` para a connection string do pooler (Supavisor) do Supabase.

## Custo estimado

- **Embeddings (OpenAI):** ~$0.02 por 1M tokens — para milhares de artigos pessoais, o total fica na casa de centavos de dólar.
- **Banco (Supabase):** grátis no tier free (com o trade-off da pausa por inatividade) ou $25/mês no Pro.
- **Hosting (Railway Hobby):** $5/mês fixo, cobrindo o uso esperado de um servidor leve e majoritariamente ocioso.

## Próximos passos

- Implementar autenticação no endpoint HTTP (API key por client).
- Decidir entre manter Supabase free (aceitando pausas) ou migrar para Pro.
- Avaliar suporte a MCP no app mobile quando/se disponível.
