---
date: 2026-04-08
tags: [tech-mentor, ia, agentes, memory, working-memory, episodic, semantic, procedural, letta, memgpt, mem0, zep, entity-memory, memory-poisoning]
skill: tech-mentor-ai/references/ai/agent-memory.md
level: avançado
---

# Memória de Agentes

## Contexto

Sem memória persistente, cada sessão começa do zero — inviável para assistentes reais. Agentes LLM têm um problema fundamental: o contexto da janela é volátil, finito e caro. Arquiteturas de memória resolvem isso externalizando, comprimindo e recuperando informação de forma seletiva. O objetivo não é "lembrar tudo" — é injetar no contexto exatamente o que é relevante para a task atual.

---

## Como Funciona

### Hierarquia de Memória

```
In-context (working memory)   → System prompt + conversa recente
                                Acesso instantâneo, custo O(n), perdido ao fim da sessão

Recall memory (episódica)     → Histórico de interações em vector store
                                Busca semântica, custo de retrieval, persiste entre sessões

Archival memory (long-term)   → Fatos, preferências, entidades, capacidade ilimitada
                                Mais lenta, mais barata, estruturada
```

---

## Taxonomia Completa

| Tipo | Análogo técnico | O que armazena | Latência |
|---|---|---|---|
| **Working memory** | Janela de contexto | Conversa atual, tool results, raciocínio ativo | Zero |
| **Episódica** | Log + retrieval semântico | "O que aconteceu nessa sessão/tarefa?" | Baixa |
| **Semântica** | Knowledge base vetorial ou grafo | Fatos, documentos, entidades, relacionamentos | Baixa |
| **Procedural** | System prompt + few-shot examples | "Como executar tarefas recorrentes?" | Zero |
| **Prospectiva** | Planner externo | Lembretes, próximos steps planejados | Baixa |

---

## Working Memory — In-Context

Tudo que está na janela de contexto ativa. Zero latência, mas:
- Custo cresce linearmente com tokens
- Perdido ao fim da sessão
- Attention é O(n²) — contexto grande = latência alta

**Context Compression** — antes de encher o contexto, o agente resume mensagens antigas:
```python
# Sistema monitora utilização do contexto
# Quando ultrapassa 80%, comprime as mensagens mais antigas
if context_utilization > 0.80:
    summary = await llm.summarize(old_messages)
    context = [SystemMessage(f"Resumo da conversa: {summary}")] + recent_messages[-8:]
```

Ferramentas como Letta/MemGPT gerenciam isso automaticamente com paginação de contexto.

---

## Memória Episódica

Armazena eventos passados — sessões anteriores, histórico de conversas, outcomes de ações.

```python
# Indexação: após cada turno
async def store_episode(turn: ConversationTurn, user_id: str, session_id: str):
    embedding = await embed(f"{turn.user_message}\n{turn.agent_response}")
    await vector_store.upsert(
        embedding=embedding,
        metadata={
            "user_id": user_id,
            "session_id": session_id,
            "timestamp": datetime.utcnow().isoformat(),
            "summary": await llm.summarize(turn)  # resumo para retrieval
        }
    )

# Retrieval: no início de cada sessão
async def recall_relevant(current_context: str, user_id: str, top_k=5) -> list[str]:
    query_embedding = await embed(current_context)
    episodes = await vector_store.search(
        embedding=query_embedding,
        top_k=top_k,
        filter={"user_id": user_id}  # isolamento por usuário
    )
    return [ep.metadata["summary"] for ep in episodes]
```

**O que constitui um "episódio"? Trade-offs:**

| Granularidade | Vantagem | Desvantagem |
|---|---|---|
| Por mensagem | Recall preciso | Caro para indexar e buscar |
| Por turno | Balanceado | Pode perder contexto fino |
| Por tarefa completa | Barato | Perde detalhes |
| Por chunk semântico | Eficiente | Requer semantic chunker |

---

## Memória Semântica

Conhecimento factual sobre entidades, relacionamentos e domínio. Não é "o que aconteceu" — é "o que é verdade".

**Entity Memory** — manter um caderno de entidades que o agente atualiza após cada interação:

```python
# Após cada turno, extrai entidades mencionadas
async def update_entity_memory(turn: str, memory_store):
    entities = await llm.extract_entities(turn)
    # Output esperado: [{id, name, type, facts: [...]}]

    for entity in entities:
        existing = await memory_store.get(entity["id"])
        merged = merge_entity(existing, entity)  # combina fatos novos com existentes
        await memory_store.upsert(entity["id"], merged)

# Exemplo de entidade armazenada
{
    "id": "user_gabriel",
    "name": "Gabriel",
    "type": "user",
    "facts": [
        "Prefere respostas técnicas diretas",
        "Stack principal: Node.js + TypeScript",
        "Estudando IA para Engenharia de Software"
    ],
    "updated_at": "2026-04-08T10:00:00Z"
}
```

**Backends por caso de uso:**

| Backend | Melhor para |
|---|---|
| pgvector | Apps que já usam Postgres, escala moderada |
| Qdrant | Alta escala, filtros complexos, multi-tenant |
| Redis (módulo vector) | Memória episódica de curto prazo, baixa latência |
| Neo4j / FalkorDB | Relações complexas entre entidades, multi-hop reasoning |
| SQLite + embedding | Agentes locais, desenvolvimento |

---

## Memória Procedural

Como realizar tarefas. Implementada como:

1. **System prompt persistente** — persona, estilo de resposta, regras de comportamento
2. **Few-shot examples dinâmicos** — recuperados por similaridade com a task atual
3. **Tool descriptions** — ensinam o agente como e quando usar ferramentas

**Dynamic Few-Shot Selection** — mais eficiente que exemplos fixos quando o banco é grande:
```python
async def build_prompt_with_examples(user_input: str, example_store) -> str:
    # Busca exemplos mais similares ao input atual
    input_embedding = await embed(user_input)
    relevant_examples = await example_store.search(input_embedding, top_k=3)

    # Injeta exemplos relevantes antes do input
    few_shot_block = format_examples(relevant_examples)
    return f"{few_shot_block}\n\nNow handle: {user_input}"
```

---

## Arquitetura de Referência — Letta (MemGPT)

```
┌──────────────────────────────────────────────┐
│              Janela de Contexto               │
│  [System Prompt] [Working Memory] [Messages]  │
│                    ↕ (paginação automática)   │
├──────────────────────────────────────────────┤
│              External Memory                  │
│  ┌────────────┐   ┌────────────┐             │
│  │  Archival   │   │  Episodic  │             │
│  │ (vetorial)  │   │  (events)  │             │
│  └────────────┘   └────────────┘             │
└──────────────────────────────────────────────┘
```

O agente usa tools para ler e escrever na external memory — a decisão de quando acessar é do próprio LLM:

```python
from letta import create_client

client = create_client()

agent_state = client.create_agent(
    name="assistant",
    memory=ChatMemory(
        human="Gabriel é um dev fullstack estudando IA para arquitetura de software",
        persona="Sou um assistente técnico que lembra de conversas anteriores e adapta minhas respostas ao perfil do usuário"
    ),
)

# A memória é atualizada automaticamente pelo agente
# Quando o contexto enche, o agente arquiva o que não é crítico
response = client.send_message(
    agent_id=agent_state.id,
    role="user",
    message="Qual era aquele problema de performance que discutimos semana passada?"
    # Agente busca na memória arquivada e traz contexto relevante
)
```

**Tools de memória expostas ao agente Letta:**
```python
memory_search(query: str) -> list[str]    # busca na archival memory
memory_insert(content: str) -> None       # salva novo fato
memory_replace(old: str, new: str) -> None  # atualiza fato existente
```

---

## Mem0 — Hierárquica com Auto-Summarization

```python
from mem0 import Memory

memory = Memory()

# Adicionar memória
memory.add(
    messages=[{"role": "user", "content": "Prefiro código em TypeScript com strict mode"}],
    user_id="gabriel"
)

# Buscar memórias relevantes
relevant = memory.search(
    query="Como devo formatar o código?",
    user_id="gabriel"
)
# → ["Prefiro código em TypeScript com strict mode", ...]

# Mem0 auto-sumariza e deduplica periodicamente
# Para manter a memória limpa sem intervenção manual
```

---

## Zep — Managed Memory com Grafos de Conhecimento

Zep é um serviço gerenciado de memória com grafo de conhecimento sobre as conversas — extrai entidades e relações automaticamente.

```python
from zep_python import ZepClient, Message

zep = ZepClient(api_key=ZEP_API_KEY)

# Adicionar mensagem à sessão
await zep.memory.aadd_memory(
    session_id=session_id,
    messages=[Message(role="user", content="Tenho um problema no meu serviço de pagamento")]
)

# Buscar contexto relevante (Zep extrai entidades e relações automaticamente)
memory = await zep.memory.aget_memory(session_id)
# memory.context já contém resumo + fatos extraídos + entidades

# Busca semântica no histórico
results = await zep.memory.asearch_memory(
    session_id=session_id,
    text="problemas de pagamento anteriores",
    limit=5
)
```

---

## Memory Sharing em Multi-Agente

| Abordagem | Isolamento | Complexidade | Quando usar |
|---|---|---|---|
| **Shared Vector Store** | Baixo | Baixa | Agentes colaborativos do mesmo domínio |
| **Memory Namespacing** | Alto | Média | Multi-tenant, agentes especializados |
| **Memory Broker Agent** | Muito alto | Alta | Auditoria, controle de acesso granular |

```python
# Namespacing: {agent_id}/{user_id}/memory_type
namespace = f"{agent_id}/{user_id}/episodic"
await vector_store.upsert(embedding, metadata, namespace=namespace)

# Compartilhamento explícito: agente lê memória de outro via tool
async def read_shared_memory(source_agent_id: str, query: str) -> list[str]:
    # Tool que permite acesso controlado à memória de outro agente
    namespace = f"{source_agent_id}/shared"
    return await vector_store.search(embed(query), namespace=namespace)
```

---

## Problemas Comuns

### Memory Poisoning

Se o agente escreve na memória com base em input não confiável (resultado de tool de página web, e-mail), um atacante pode injetar instruções maliciosas na memória de longo prazo.

```python
# ❌ Inseguro — escreve diretamente o output de tool na memória
memory.insert(tool_output)

# ✅ Seguro — sanitiza e separa fatos de instruções
def safe_memory_insert(content: str):
    sanitized = sanitize_content(content)  # remove padrões de injection
    if is_instruction_like(sanitized):
        log_security_event("Potential memory injection blocked", content)
        return
    memory.insert(sanitized)
```

### Memory Drift

Ao longo de muitas sessões, a memória acumula fatos desatualizados ou contraditórios.

```python
# Estratégia: TTL + compressão periódica
# Fatos episódicos com TTL de 90 dias
# A cada semana, rodar job de deduplicação e sumarização
async def memory_maintenance_job():
    old_entries = await memory_store.find_older_than(days=90)
    if len(old_entries) > 100:
        summary = await llm.summarize_facts(old_entries)
        await memory_store.delete_batch(old_entries)
        await memory_store.insert(summary, metadata={"type": "compressed_history"})
```

### Retrieval Miss

Memória existe mas não é recuperada porque a query semântica não casa com o texto armazenado.

**Mitigações:**
- Hybrid search (BM25 + vetorial) para combinar recall léxico e semântico
- Metadata filters — filtrar por `user_id`, `session_id`, `entity_type`
- Múltiplos embeddings por entrada (embedding do fato + embedding da query que o gerou)
- Reescrita de query antes de buscar

### Custo de Escrita

Escrever na memória a cada turno é caro em tokens e latência.

```python
# Estratégia: escrita lazy em batch
class LazyMemoryWriter:
    def __init__(self, batch_size=5):
        self.buffer = []
        self.batch_size = batch_size

    async def add(self, turn: ConversationTurn):
        self.buffer.append(turn)
        if len(self.buffer) >= self.batch_size:
            await self.flush()

    async def flush(self):
        # Extrai entidades e fatos de todos os turns de uma vez
        facts = await llm.extract_facts_batch(self.buffer)
        await memory_store.upsert_batch(facts)
        self.buffer.clear()
```

---

## Quando Usar / Quando Evitar

**Working memory (in-context) resolve quando:** sessão curta, task única, usuário não espera continuidade entre sessões.

**Episódica quando:** assistente pessoal, suporte ao cliente que lembra interações anteriores, agentes de longa duração.

**Semântica quando:** agente precisa de conhecimento factual sobre o domínio ou sobre o usuário que cresce ao longo do tempo.

**Procedural quando:** o agente deve aprender com exemplos positivos acumulados em produção.

**Não implemente memória quando:** task é stateless, custo de retrieval não compensa, dados do usuário não podem ser armazenados (LGPD/GDPR sem consent adequado).

---

## Conceitos Relacionados

[[agentes-core]] · [[agentes-orquestracao]] · [[rag-retrieval]] · [[context-engineering]] · [[ai-safety-engineering]]

---
*Fonte: tech-mentor skill · tech-mentor-ai · 2026-04-08*
