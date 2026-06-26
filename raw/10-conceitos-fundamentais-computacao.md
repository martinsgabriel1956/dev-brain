# 10 Conceitos Fundamentais da Computação

> Transcrição adaptada de vídeo sobre os 10 conceitos base de tudo que existe em computação.

Tudo que existe na computação — de inteligência artificial a um simples print — se resume a 10 ideias fundamentais. Ideias que existem há décadas e não mudaram. Linguagens e frameworks mudam, mas esses conceitos não.

---

## #10 — Binário e Lógica Booleana

Tudo que o computador processa — texto, imagem, som — no fundo é uma sequência de zeros e uns. A letra "A" é uma sequência de zero e uns. Uma foto são milhões de números representando a cor de cada pixel.

Para manipular esses bits existem três operações: **AND**, **OR** e **NOT**. Parece simples, e é simples — mas combinando essas três operações dá para construir qualquer coisa: calculadoras, memória, processadores inteiros.

Cada circuito dentro do seu computador é uma combinação de portas lógicas. Mas ter dados em binário é só o começo. O que importa é como você organiza esses dados.

---

## #9 — Estruturas de Dados

Imagina que você tem 1000 nomes e precisa encontrar um específico:

- Em uma **lista**: você olha um por um — 1000 comparações no pior caso.
- Em uma **árvore binária de busca**: você divide pela metade a cada passo — 10 comparações no máximo.
- Em uma **hash table**: uma comparação direto no endereço certo.

Cada estrutura tem vantagens e desvantagens:

| Estrutura | Ponto forte |
|---|---|
| Array | Acesso rápido por índice |
| Lista encadeada | Inserção rápida no meio |
| Árvore | Busca rápida quando ordenado |
| Hash table | Busca em O(1) no caso médio |

A escolha da estrutura certa muda tudo no desempenho do seu código.

---

## #8 — Complexidade de Algoritmos (Big O)

O Big O responde uma pergunta: conforme os dados crescem, o que acontece com o tempo de execução?

| Notação | Crescimento |
|---|---|
| O(1) | Constante — não importa o tamanho |
| O(log n) | Logarítmico — busca binária |
| O(n) | Linear — dobrou os dados, dobrou o tempo |
| O(n²) | Quadrático — 100k elementos = 10 bilhões de operações |
| O(n!) | Fatorial — 20 elementos = mais de 2 quintilhões de operações |

O pior de todos é o O(n!) — aparece no **problema do caixeiro viajante** (qual a rota mais curta passando por todas as cidades?). Para resolver de verdade você teria que testar todas as combinações possíveis.

É por isso que a **busca binária** é tão poderosa: em vez de olhar um por um, ela divide pela metade a cada passo. 1 bilhão de elementos = apenas 30 comparações.

Saber Big O é saber prever se o seu código vai funcionar bem em produção ou travar com dados reais.

---

## #7 — Recursão

Recursão é quando uma função chama ela mesma para resolver um problema menor.

Exemplo — fatorial de 5:

```
fatorial(5) → fatorial(4) → fatorial(3) → fatorial(2) → fatorial(1) → retorna 1
```

Cada chamada entra na **pilha de execução**. Quando chega no caso base, começa a devolver os resultados de baixo para cima.

Toda recursão tem duas partes obrigatórias:

1. **Caso base** — o que faz a recursão parar. Sem ele: loop infinito.
2. **Caso recursivo** — onde o problema se divide em algo menor.

Recursão aparece em tudo: percorrer árvores, algoritmos de ordenação, fractais. Até o sistema de arquivos do seu computador é uma estrutura recursiva.

---

## #6 — Concorrência e Paralelismo

**Concorrência** é gerenciar várias tarefas ao mesmo tempo. **Paralelismo** é executar várias tarefas ao mesmo tempo. É uma diferença importante.

Analogia com cozinheiro:
- Um cozinheiro sozinho pode ser **concorrente**: coloca o arroz para cozinhar, corta a cebola enquanto espera, alterna entre tarefas — mas nunca faz dois movimentos no mesmo instante.
- Para fazer duas coisas ao mesmo tempo são necessários dois cozinheiros — isso é **paralelismo**.

O perigo mora nas **race conditions**: quando duas threads acessam o mesmo dado ao mesmo tempo.

Exemplo clássico: duas threads leem saldo de R$100, ambas subtraem R$50, ambas gravam R$50. O saldo deveria ser zero mas ficou R$50 — dinheiro apareceu do nada.

Mecanismos para lidar com isso: **locks**, **semáforos**, **mutexes** — e o famoso problema do **deadlock**.

---

## #5 — Compiladores e Interpretadores

Você escreve `let x = 10` e o computador entende zeros e uns. Quem faz essa tradução?

Um **compilador** passa por várias etapas:

1. **Análise léxica** — quebra o código em tokens (`let` = palavra reservada, `x` = identificador, `10` = número).
2. **Análise sintática** — monta uma árvore que representa a estrutura do código: a **AST** (Abstract Syntax Tree).
3. **Otimização e geração de código** — analisa a AST e gera o código de máquina mais eficiente.

Diferença entre compilador e interpretador:

- **Compilador**: traduz tudo de uma vez e gera um executável. Geralmente mais rápido.
- **Interpretador**: traduz e executa linha por linha. Geralmente mais flexível.
- **Meio-termo** (Java, C#): compilam para código intermediário que roda numa máquina virtual.

---

## #4 — Redes e Protocolos

Quando você acessa um site, seu computador manda uma mensagem pro servidor — atravessa cabos, roteadores, às vezes satélites — e chega em milissegundos. Os **protocolos** são as regras que definem como computadores se comunicam.

O modelo funciona em camadas:

| Camada | Responsabilidade |
|---|---|
| HTTP | O que dizer ("me dá a página inicial") |
| TCP | Garante que a mensagem chegue inteira; reenvia se perder pedaço |
| IP | Decide para onde mandar — endereço e rota |
| Física | Transmite os bits pelo cabo, Wi-Fi, fibra |

Cada camada empacota a mensagem com suas informações e passa para baixo. Do outro lado, cada camada desempacota e passa para cima. É como uma carta dentro de um envelope dentro de outro envelope.

---

## #3 — Banco de Dados

Variáveis morrem quando o programa fecha. O banco de dados é onde a informação sobrevive.

Uma query simples esconde decisões complexas: percorrer tudo, usar um índice, qual índice? Sem índice o banco lê todas as linhas. Com índice, pula direto nos dados certos — diferença entre 1 segundo e 1 milissegundo.

Bancos relacionais garantem as propriedades **ACID**:

| Propriedade | Significado |
|---|---|
| **Atomicidade** | Ou tudo acontece, ou nada acontece |
| **Consistência** | Dados sempre válidos antes e depois da transação |
| **Isolamento** | Transações concorrentes não interferem entre si |
| **Durabilidade** | Dados confirmados sobrevivem a falhas |

Sem essas garantias: dinheiro some, dados são corrompidos, sistemas quebram.

---

## #2 — Criptografia

Toda vez que você faz login, manda mensagem ou paga um boleto online, a criptografia está protegendo seus dados.

**Hashing**: transforma dados em uma impressão digital única e irreversível. A senha "123" vira uma sequência aleatória de caracteres — e não dá para voltar ao original. Por isso sites devem armazenar o *hash* da senha, nunca a senha em si.

**Criptografia simétrica**: usa a mesma chave para encriptar e decriptar. É rápida, mas tem um problema: como compartilhar a chave de forma segura?

**Criptografia assimétrica**: resolve isso com duas chaves:
- **Chave pública**: para encriptar — qualquer um pode ter.
- **Chave privada**: para decriptar — só você tem.

É assim que o **HTTPS** funciona: seu navegador usa a chave pública do servidor para encriptar, e só o servidor consegue decriptar com a chave privada.

---

## #1 — Abstração

Esse é o conceito mais importante da ciência da computação — e apareceu em todos os outros nove.

**Abstração é esconder a complexidade atrás de uma interface simples.**

Quando você dirige um carro, você gira o volante. Não precisa saber como a coluna de direção funciona, como o fluido hidráulico atua ou como as rodas recebem o comando. O volante é uma abstração.

Em programação é a mesma coisa: você chama `fetch()` para fazer uma requisição HTTP sem precisar saber como o TCP garante a entrega, como o IP roteia ou como os bits viram sinais elétricos.

Cada camada esconde a complexidade da anterior:

- Estruturas de dados abstraem como a memória organiza bits.
- Compiladores abstraem a tradução para código de máquina.
- Bancos de dados abstraem a persistência em disco.

Toda evolução em computação é uma nova camada de abstração:
- Assembly abstraiu o binário.
- C abstraiu o assembly.
- Python abstraiu o C.

Sem abstração, cada programa precisaria lidar com tudo — do transistor ao pixel. Com ela, você escreve `print("hello world")` e funciona.

---

## Conclusão

Esses são os 10 conceitos que são a base de tudo que existe em computação. Você não precisa decorar tudo hoje — mas se entender a essência de cada um, vai enxergar padrões em qualquer tecnologia nova que aparecer.
