# RAG com Spring AI: microagente de recomendação de passeios (Michele Brito)

> Transcrição de vídeo colada pelo usuário e limpa. Já estava em português (sem tradução). Corrigidos erros de reconhecimento de fala: "Rug/Raug/rag" → RAG; "Dunk Chin" → Danqi Chen; "Patrick Lis" → Patrick Lewis; "PG Vector Storp / Vector Storp" → `vector_store`; "Neon Te" → Neon; "Intelj" → IntelliJ; "Spring AI com o Gemini"; "topic K/top car" → top-K; "Badia de Westminster" → Abadia de Westminster; "Big Bang" → Big Ben; "Tamsa" → Tâmisa; "Galeria burguese" → Galleria Borghese; "aminagem BT cloud" → Gemini / GPT / Claude (leitura provável); "chatclient.prompt ... PC call" → `chatClient.prompt().user(...).call().content()`. Autora: Michele Brito (canal sobre microservices, IA, Java e Spring). Projeto de exemplo no GitHub (link na descrição do vídeo, não incluído aqui).

---

## Abertura

O que é a técnica RAG, tão usada em aplicações com IA? O vídeo explora conceitos, funcionamento e implementação em código com o projeto **Spring AI**.

## O que é RAG

RAG (geração aumentada por recuperação) conecta contexto ao raciocínio da IA com um pipeline de **três etapas**:

1. **Recuperação:** o sistema busca trechos relevantes em uma base externa, conforme a pergunta.
2. **Aumento:** os trechos recuperados são injetados no prompt, enriquecendo-o.
3. **Geração:** o prompt completo vai ao LLM, que responde de forma mais precisa e contextualizada.

## Por que usar RAG

Sem contexto relevante, a resposta do modelo tende a ser genérica, baseada só nos dados de treino, com contexto muito amplo, podendo até haver **alucinações**. Com RAG, a pergunta vai junto com um contexto específico, e a resposta fica mais precisa e aderente ao cenário.

## Histórico

- **2017:** o padrão "recuperar, então gerar" foi introduzido por **Danqi Chen** no artigo *Reading Wikipedia to Answer Open-Domain Questions*: o sistema recuperava as páginas da Wikipedia mais relevantes e o modelo as lia para gerar a resposta.
- **2020:** o termo **RAG** foi introduzido academicamente por **Patrick Lewis** no artigo *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks*, concluindo que acesso a informação relevante ajuda o modelo a gerar respostas mais precisas e reduz alucinações.
- **2023:** início do aumento do uso prático de RAG com LLMs, vector stores etc.

## Onde RAG entra numa arquitetura de microsserviços

RAG não é só "feature de chat". Cenário: arquitetura de microservices completa, com:

- **microsserviços de negócio:** order, payment, notification, products;
- **microsserviços de configuração / preocupações transversais:** config server, service registry;
- **microagentes:** aqui, um de **recomendação** e um de **detecção de fraude**. Atuam de forma inteligente na arquitetura: tomam decisões, otimizam fluxos. Nesses pontos se implementa RAG para buscar contexto, raciocinar, produzir resposta inteligente e agir.

Esses microagentes (nova camada de microservices) servem quando as decisões inteligentes seriam muito difíceis, ou impossíveis, de programar com `if`s, dado o número de possibilidades e regras. Com LLMs e RAG, agentes agem e otimizam o fluxo.

O caso do vídeo simula um **recomendador de passeios/tours** (como o app GetYourGuide).

## O microagente de recomendação: gatilho e pipeline

O agente é acionado pelos microsserviços **order** e **products**, de forma:

- **síncrona** (request HTTP), ou
- **assíncrona** (eventos), com menor acoplamento: o agente escuta canais de eventos e dispara o fluxo ao receber.

Pipeline: gatilho (evento ou HTTP) → núcleo RAG recupera contexto → integração com LLM gera resposta inteligente → o agente **age**, propagando a resposta para o restante da arquitetura (ex.: microserviço `notification`, que envia e-mail ou notificação ao usuário).

## Etapa 0: indexação (preparar a base vetorial)

RAG precisa de uma fonte externa com dados próprios. Primeiro se **prepara a indexação**: dados numa base vetorial, prontos para consulta **semântica**.

O que indexar no agente de recomendação:

- regras de negócio, políticas e regras pré-definidas;
- dados de produtos (catálogo);
- histórico de pedidos (orders), para limitar e personalizar o contexto enviado ao LLM.

Fluxo: a entrada chega (request ou evento) → **chunking** (quebra em trechos) → conversão do texto em **vetor (embedding)** com modelos de embedding comerciais (OpenAI, Gemini etc.) → gravação na base vetorial (**embedding store**): **pgvector** (extensão do PostgreSQL), Pinecone etc.

**Por que salvar vetores e não o texto?** A recuperação é semântica, não exata como uma query SQL. O retorno não é uma resposta exata, mas um trecho relevante à entrada que disparou o fluxo. Por isso o texto é convertido em vetor, para busca por **similaridade**.

## Indexação no código (Spring AI)

- Projeto **Spring Boot 4, Java 25**, Spring AI com **Gemini** (Google): starter do modelo de chat do Google e do **modelo de embedding** do Google; dependência do vector store **PGVector**.
- Um `VectorStoreRepository` com método `save` que recebe documentos e chama `vectorStore.add(...)`. `VectorStore` é abstração do Spring AI (suporte a API de vector store).
- Base: Postgres na plataforma **Neon**, com pgvector. A tabela `vector_store` (nome padrão do Spring AI) tem colunas: `id`, `content` (text), `metadata`, `embedding`.
- O tipo **`Document`** do Spring AI tem exatamente esses campos (id, content, metadata, embedding). No código se preenche:
  - **id:** o id recebido do microsserviço que salvou o produto;
  - **text:** o texto que será convertido em vetor, construído com atenção;
  - **metadata:** metadados importantes, usados depois **nos filtros** da busca por similaridade.
- Construção do texto: método isolado que devolve `String` em **linguagem natural**, próxima de uma possível pergunta enviada ao LLM, para que a busca por similaridade funcione (nome do produto, localização, categoria, descrição etc.).
- A conversão texto → embedding acontece **por baixo dos panos** durante o `add`: o Spring AI aciona o modelo de embedding, sem conversões manuais.

**Demo da indexação:** classe com catálogo de **21 tours** (Roma, Paris, Londres). É importante que o agente **recomende só passeios do catálogo** da plataforma e da **mesma localidade**. Um endpoint (mapeado no Postman) salva o catálogo e popula a base vetorial; um `select` no SQL Editor do Neon mostra 21 documentos com id, content, metadados e embedding.

Em produção, com eventos, o agente escuta: novo produto → indexa no catálogo; nova order → indexa no histórico do consumidor **e** dispara recomendação.

## O fluxo RAG em tempo de consulta

1. **Entrada → vetor:** o texto de entrada é convertido em embedding (também com modelo de embedding), porque a base guarda vetores.
2. **Recuperação:** consulta semântica na base, retornando os **top-K por similaridade**: trechos mais relevantes para aquele contexto e usuário.
3. **Aumento:** monta-se o prompt unindo a entrada que disparou o fluxo, o contexto recuperado e **regras e políticas** pré-definidas.
4. **Geração:** envia-se ao LLM (Gemini, GPT, Claude ou LLM local), que gera a resposta contextualizada, com menos chance de alucinação.
5. **Ação:** a resposta final vai ao usuário ou a outro microsserviço (ex.: `notification`).

## Recuperação, prompt e geração no código

No `RecommendationService`, o método que recebe `OrderCreatedDTO` (gatilho: nova order via HTTP ou evento) executa:

- **Recuperação:** duas buscas semânticas, ambas via `VectorStoreRepository`: (a) **tours do catálogo** e (b) **histórico do usuário** (compras anteriores). Cada busca recebe `query`, `topK` e um **filtro** (`FilterExpression`) construído a partir dos **metadados** gravados na indexação, e termina em `.build()` / `vectorStore.similaritySearch(...)`.
- **Query:** em **linguagem natural**, como uma pergunta no chat: "tours relacionados a <nome da order>" mais a **localização**, para trazer só opções da região. Isolada em método próprio.
- **topK:** fixo em **4** no exemplo; quanto maior a base, maior deve ser o conjunto, para não restringir demais.
- Retorno: lista de `Document`.
- **Aumento do prompt** (linhas 44–47): junta o `OrderCreatedDTO`, as duas listas de documentos (produtos e histórico) e, num método isolado, **regras/políticas**: recomendar só tours da mesma região; não recomendar tours que o cliente já comprou; etc. Resultado: uma `String` com o prompt completo.
- **Geração:** `chatClient.prompt().user(promptCompleto).call().content()`. O `ChatClient` do Spring AI abstrai a integração com vários LLMs; as chaves de API do modelo de chat e de embedding (Gemini) estão no `application`.

## Demo do resultado

1. **Order 1:** compra de visita guiada sem fila ao Coliseu (Roma). O agente (a) grava a order no vetor como `order history` do customer; (b) recomenda: tour sem filas à Galleria Borghese e tour pelas Catacumbas de Roma ("imersão histórica").
2. **Order 2:** o usuário compra as Catacumbas. Nova recomendação: Fórum Romano e Palatino (tour a pé) e tour gastronômico noturno.
3. **Order 3:** novo usuário (outro customer ID), passeio à Torre de Londres e Joias da Coroa. Sem histórico, o leque é mais aberto: Abadia de Westminster com Big Ben, cruzeiro pelo Tâmisa, tour gastronômico por mercado de Londres. Conforme o histórico cresce, as recomendações ficam mais ajustadas aos interesses.

Com apenas 21 itens o efeito é pequeno; com milhares de passeios e perfis (radical, histórico, romântico), o microagente mapeia catálogo e interesses e recomenda com precisão.

## Fechamento

Passamos pelas etapas do RAG: conversão de texto em vetores, busca por similaridade, enriquecimento do prompt e integração com LLM. Chamada para curtir e se inscrever no canal (conteúdos de microservices, IA, Java e Spring).
