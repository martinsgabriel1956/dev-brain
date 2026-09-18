---
date: 2026-09-18
tags: [tech-mentor, ia, llms, transformers, self-attention, embeddings, tokenizacao, positional-encoding]
skill: tech-mentor-ai/references/ai/fundamentals.md
level: fundamento
---

# Self-Attention: o Mecanismo por Trás dos Transformers

## Contexto

Vídeo de uma série sobre desmistificar o funcionamento das LLMs para desenvolvedores. Este episódio explica o mecanismo de **self-attention**, apresentado como a virada de chave técnica que tornou modelos como ChatGPT e Claude eficientes na predição do próximo token. A narradora avisa explicitamente que domina o conceito e a intuição, mas não o cálculo matemático subjacente em profundidade — ela está estudando estatística/cálculo em paralelo.

---

## Pré-requisitos: Tokens e Embedding Vectors

Antes de entender attention, dois conceitos precisam estar claros:

### Tokens

Tokens são pedaços de uma palavra ou de uma frase — não são equivalentes a palavras inteiras. Exemplo: a frase "o banco aprovou o crédito" é quebrada em pedacinhos (tokens), e cada pedaço é traduzido para um número: o **ID daquele token no vocabulário** daquela LLM. O vocabulário é a lista completa de tokens que o modelo compreende, cada um com uma posição/ID fixo (ex.: "amor" = ID 1, "banana" = ID 2, "cachorro" = ID 3). A forma como a quebra em tokens acontece depende do modelo e do tokenizador usado — um token pode ser só a sílaba "cré" de "crédito", por exemplo.

### Embedding Vectors

Depois que o token vira um ID, esse ID por si só não carrega significado — só identifica a posição do token no vocabulário. O **embedding vector** é o que traduz esse ID em uma representação numérica do *significado* daquele token. Essa tradução vem de uma **matriz de embeddings** pronta ao final do treinamento do modelo: uma matriz que correlaciona cada ID de token a um vetor de números (ex.: `[0.22, 3, 5, ...]`).

**Como a matriz de embeddings é formada durante o treino:**

1. Todo token do vocabulário recebe um vetor de embedding **aleatório** no início do treinamento. O tamanho (length) desse vetor é definido previamente pelo time que constrói a LLM — ex.: GPT-2 usa vetores de 768 posições, mas poderia ser 15, 50, 1000 posições.
2. Durante o treinamento, o modelo é exposto a uma quantidade massiva de texto e vai plotando esses tokens num **mapa de padrões linguísticos multidimensional** — não um mapa de 2 eixos (X/Y), mas um espaço com centenas/milhares de dimensões.
3. O modelo ajusta os valores desse vetor iterativamente para capturar correlações: quais palavras aparecem juntas, qual a distância entre palavras opostas, etc.
4. Ao final do treino, cada token tem um vetor fixo que representa, com base em tudo que o modelo "leu", seu significado — mas ainda um significado **geral**, cobrindo todos os usos possíveis daquele token, não um significado específico ao contexto de uma frase.

**Demonstrações visuais citadas na fonte** (ferramentas externas, não geradas pela LLM em si):

- Guia intuitivo de embeddings do Hugging Face: mostra palavras plotadas por proximidade semântica — ex. "golden" no lado oposto de "owl" (coruja); "ocean" perto de "cobra" (cob).
- Embedding Projector do TensorFlow (Google): busca por palavra e mostra vizinhos no espaço multidimensional — ex. "Apple" tem como vizinhos "Macintosh", "Microsoft", "IBM"; "Isaac" tem como vizinhos "Isaac Newton", "Isaac Asimov" (implícito), "Abraham", "Jacob"; "tree" tem como vizinhos "forest", "leaf", "leaves", "plant", "flowers".

### O problema que embeddings sozinhos não resolvem: ambiguidade contextual

Uma palavra pode significar coisas diferentes dependendo do contexto. Exemplo central da fonte: a palavra **"banco"**.

- "O banco aprovou o crédito" → banco = instituição financeira.
- "A menina sentou no banco" → banco = objeto para sentar.

O embedding vector de "banco" carrega, dentro de si, sinais numéricos para *ambos* os significados possíveis — porque foi treinado sobre todos os usos do token no corpus. Ele não resolve sozinho qual significado se aplica à frase específica que foi dada como input. É exatamente esse problema que o mecanismo de self-attention resolve.

---

## Self-Attention

### Positional Encoding

Antes do cálculo de atenção em si, é adicionado a cada token um vetor extra chamado **positional encoding** (ou positional embedding), que representa a posição/ordem daquele token na frase de input. A ordem importa porque muda o significado da frase inteira — exemplo dado: "a mãe matou a filha" vs. "a filha matou a mãe" têm as mesmas palavras, significados opostos.

### Vetores Q (Query) e K (Key)

Para cada token, o mecanismo de self-attention gera dois novos vetores:

- **Vetor Q (Query):** representa o que aquele token está "buscando" — quais outras palavras são relevantes para ele.
- **Vetor K (Key):** representa o que cada token "oferece" para os outros.

A narradora é explícita que o cálculo matemático exato por trás da geração desses vetores não é coberto em profundidade no vídeo — o foco é conceitual.

### Cálculo do Attention Score

O vetor Q de um token é multiplicado pelo vetor K de outro token. Essa multiplicação de vetores gera uma matriz de **attention scores**: um valor numérico que representa o quanto um token é importante/relevante para outro token.

**Exemplo dado com a frase "o banco aprovou o crédito":**

- Importância de "banco" para "aprovou": ~40% (ilustrativo).
- Importância de "banco" para "crédito": ~60% (ilustrativo) — "crédito" adiciona bastante contexto ao significado de "banco".
- Importância de "o" para "banco": ~5% ou menos — artigo quase não muda o significado de "banco".

**Exemplo didático citado da literatura (frase clássica "the cat sat on the mat"):** uma matriz onde cada token é multiplicado por todos os outros tokens da frase, gerando scores como "mat"→"cat" = 2, "on"→"on" (mesmo token) = 1, "sat"→outro token = 0.5 — valores puramente ilustrativos para fins didáticos, não reais.

O resultado final dessa multiplicação de matrizes (Q × K) passa por uma função **softmax** para normalizar os scores.

### O output: vetor de significado + contexto

O resultado do mecanismo de self-attention é um **novo vetor para cada token**, que combina o significado semântico original (do embedding) com o contexto da frase específica em que aquele token apareceu. Com esse vetor enriquecido, o modelo consegue prever o próximo token com muito mais precisão — porque agora "entende" não só o que a palavra significa no dicionário, mas o que ela significa *naquela frase*.

---

## Arquitetura Transformer — visão geral do pipeline

1. **Input** → tokens.
2. Tokens → **input embeddings**.
3. Adição de **positional encoding**.
4. **Self-attention**: cálculo das matrizes Q e K, geração dos attention scores, normalização (softmax).
5. Geração do **output**: previsão das próximas palavras mais prováveis.
6. Normalização/decodificação final → output para o usuário.

## Significado histórico: "Attention Is All You Need" (2017)

O mecanismo de self-attention foi apresentado no paper **"Attention Is All You Need"**, publicado em 2017. Segundo a fonte, essa publicação foi a "faísca" que iniciou o avanço acelerado dos modelos generativos atuais — antes dele, os algoritmos existentes (que já usavam embedding vectors) tinham grande dificuldade em compreender contexto. A capacidade de compreender contexto via self-attention é apontada como a causa direta da qualidade das respostas que se observa hoje em modelos como ChatGPT e Claude.

## Limitações reconhecidas pela própria fonte

- A narradora reconhece abertamente que o cálculo matemático detalhado de Q, K, V e da função softmax fica fora do escopo do vídeo — ela não domina essa base de cálculo/estatística a fundo e está estudando o tema.
- Os números usados nos exemplos (40%, 60%, 5%; "mat"→"cat" = 2) são **ilustrativos/educacionais**, não valores reais extraídos de um modelo.
- O vídeo não cobre o vetor **V (Value)**, terceiro componente do mecanismo padrão de attention (Q, K, V) amplamente documentado na literatura — só menciona Q e K explicitamente.
