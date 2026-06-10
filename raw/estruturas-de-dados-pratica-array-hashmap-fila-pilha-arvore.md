# Estruturas de Dados na Prática — Array, Hashmap, Fila, Pilha e Árvore

**Fonte:** Transcrição de vídeo (YouTube)  
**Autor:** desconhecido (canal parceiro da Rocket City)  
**Data de publicação:** desconhecida  
**Idioma original:** Português (Brasil)

---

## Introdução

Toda vez que você escreve código, você está tomando decisões que vão definir se o seu sistema vai ser:

- Rápido ou lento
- Flexível ou frágil
- Fácil de manter ou impossível de entender

A maioria dos devs toma essa decisão sem nem perceber que está tomando. Estamos falando de **estrutura de dados** — não o conceito teórico da faculdade, mas a escolha prática de como você organiza as informações do seu sistema e o que isso significa para tudo que vem depois.

> A escolha errada em um sistema pequeno pode até passar despercebida. A escolha errada em um sistema com mais de 1.000 usuários vai parar o sistema.

---

## Array

### O que é

Pense numa fila de pessoas esperando para entrar em um show. Cada pessoa tem uma posição. A contagem começa em **zero** — a primeira pessoa está na posição 0, a segunda na posição 1, e assim por diante.

O array é uma **coleção ordenada** onde cada elemento tem sua posição (**índice**). O acesso por índice é praticamente instantâneo — você não precisa procurar, você sabe exatamente onde o elemento está.

### Ponto forte

```
array[9] → acessa a 10ª posição diretamente
```

Acesso por posição em tempo constante — O(1).

### Ponto fraco

Inserir ou remover elementos **no meio** é caro. Se você remove o elemento da posição 3 de um array com 100 elementos, todos os elementos das posições 4 a 99 precisam ser deslocados uma posição. Com 10 elementos, imperceptível. Com 1 milhão, lento.

### Quando usar

- A ordem importa e você acessa elementos por posição
- Você vai iterar por todos os elementos em sequência
- O tamanho da coleção é previsível e relativamente fixo

### Quando não usar

- Você precisa buscar elementos por atributo (ex.: por e-mail)
- Você insere e remove elementos no meio com frequência

---

## Hashmap

### O que é

Pense em um dicionário: você não procura palavra por palavra desde o início. Você vai direto à letra que te interessa e busca a partir dali.

O hashmap funciona assim — em vez de posição numérica, você acessa os dados através de uma **chave**. A chave pode ser qualquer coisa: um e-mail, um ID, um nome.

### Por que é mais rápido para busca

No array, para buscar um usuário pelo e-mail, você teria que percorrer cada elemento um por um. Com 10 usuários é rápido; com 1 milhão, é lento.

No hashmap, você vai direto na chave. **Não importa se há 10 ou 1 milhão de registros** — o tempo de busca é praticamente o mesmo: O(1).

### Quando usar

- Você precisa buscar por um identificador (ID, e-mail, nome)
- Você precisa verificar se algo existe de forma rápida
- Você quer associar uma chave a um valor

### Quando não usar

- A ordem dos elementos importa
- Você precisa de um intervalo de valores (ex.: todos os usuários com ID entre 100 e 200)

---

## Fila (Queue)

### O que é

A fila é exatamente o que o nome diz: o **primeiro que entra é o primeiro que sai** (FIFO — First In, First Out).

Analogia: mensagens que chegam no celular — as enviadas primeiro chegam primeiro.

### Onde aparece na prática

- Filas de jobs (processamento em background)
- Filas de mensagens (Kafka, RabbitMQ, SQS)
- Filas de impressão

### Quando usar

Quando você precisa processar coisas **em ordem** de chegada.

---

## Pilha (Stack)

### O que é

O oposto da fila: o **último que entra é o primeiro que sai** (LIFO — Last In, First Out).

Analogia: uma pilha de pratos. Você coloca um prato em cima e ele é o primeiro a ser retirado. Nunca vai buscar o prato do fundo.

### Onde aparece na prática

- **Ctrl+Z no editor de código**: a última modificação é a primeira a ser desfeita — exatamente o comportamento de uma pilha
- Call stack de execução de funções
- Histórico de navegação (botão "voltar")

### Quando usar

Quando o elemento **mais recente** tem prioridade de processamento.

---

## Árvore (Tree)

### O que é

Provavelmente você usa todos os dias sem perceber. O **sistema de arquivos do seu computador** é uma árvore clássica: uma pasta-raiz contém subpastas, que contêm arquivos.

A ideia central: cada elemento é um **nó**. Cada nó pode ter filhos. Cada filho pode ter filhos. Isso cria uma **hierarquia natural**.

### Por que é poderosa para buscas

Um banco de dados que usa árvore internamente para indexar dados consegue encontrar um registro entre **bilhões** em questão de milissegundos. A razão: a árvore permite **eliminar metade das possibilidades em cada etapa** da busca (busca binária).

### Onde aparece na prática (sem você construir do zero)

- **Bancos de dados**: índices B-tree (PostgreSQL, MySQL)
- **Sistema de arquivos**: hierarquia de pastas
- **Parsers de código**: AST (Abstract Syntax Tree)

Entender árvores te ajuda a entender o comportamento desses sistemas.

### Quando usar

- Os dados têm hierarquia natural (categorias, comentários aninhados, menus)
- Você precisa de busca eficiente em grandes volumes
- Você está modelando relacionamentos pai-filho

### Quando não usar

- Os dados são planos e simples — array ou hashmap resolvem com menos complexidade

---

## As Três Perguntas para Escolher a Estrutura Certa

```
1. Você acessa o dado por POSIÇÃO ou por IDENTIFICADOR?
   → Posição: Array
   → Identificador: Hashmap

2. A ORDEM de processamento importa?
   → Primeiro que chegou processa primeiro: Fila
   → O mais recente tem prioridade: Pilha

3. Os dados têm HIERARQUIA NATURAL?
   → Sim: Árvore
   → Não: Array ou Hashmap já resolvem
```

A maioria dos problemas do dia a dia cabe dentro dessas três perguntas.

---

## Tabela Resumo

| Estrutura | Acesso | Busca por atributo | Inserção/Remoção no meio | Hierarquia |
|---|---|---|---|---|
| **Array** | O(1) por índice | O(n) | O(n) | Não |
| **Hashmap** | O(1) por chave | O(1) por chave | O(1) | Não |
| **Fila** | Primeiro elemento | — | O(1) nas extremidades | Não |
| **Pilha** | Último elemento | — | O(1) no topo | Não |
| **Árvore** | O(log n) | O(log n) | O(log n) | Sim |

---

## Próximo Passo

O vídeo anuncia uma continuação sobre **Big O notation** — entender o "porquê" por trás das diferenças de performance: por que o hashmap é mais rápido que o array em uma busca, o que define a velocidade de uma operação, e como pensar em performance não como otimização tardia, mas como consequência natural das suas escolhas de estrutura de dados.
