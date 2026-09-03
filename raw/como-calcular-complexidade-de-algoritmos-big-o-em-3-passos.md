# Como calcular complexidade de algoritmos (Big-O) em 3 passos

> Transcrição de vídeo do canal do usuário sobre análise de complexidade de tempo (notação Big-O), limpa e formatada a partir do texto bruto gerado por transcrição automática. Nenhuma tradução foi necessária (conteúdo original em português).

## Introdução

O vídeo abre perguntando ao público: você já codificou uma solução para um problema (de trabalho ou de faculdade) e não sabia dizer se ela era rápida o suficiente? Ou passou por um processo seletivo, escreveu um código e o entrevistador perguntou "qual a complexidade desse código?" e você não soube responder? Já ouviu falar de Big-O mas nunca entendeu de fato o que é, ou pesquisou sobre o assunto e só encontrou fórmulas matemáticas que não ajudaram?

A promessa do vídeo: ensinar a calcular a complexidade de tempo de cerca de 90% dos códigos que você escrever, seguindo apenas três passos.

## Por que medir tempo de execução com um cronômetro não funciva

Pode existir mais de uma forma de resolver o mesmo problema, e uma solução pode ser melhor que outra em tempo de execução. Uma abordagem ingênua seria cronometrar quanto tempo o código leva para rodar (ex: "demorou 10 segundos", "demorou 2 minutos"). Isso não funciona bem na prática porque:

- O tempo depende da máquina onde o código roda (processadores diferentes têm desempenho diferente).
- O código pode ser testado com uma entrada "de sorte" que roda rápido, mas em outro cenário (não testado) pode ser muito mais lento.

## O que é complexidade de algoritmos

Complexidade de algoritmos é uma forma de analisar a quantidade de passos/iterações que o código leva para executar do início ao fim, considerando o **pior caso possível** (o cenário em que o algoritmo levaria mais tempo para ser executado).

A notação mais usada para descrever complexidade de tempo é a **notação Big-O** (O grande), que descreve o crescimento do tempo de execução de um algoritmo em função do tamanho da entrada.

### Complexidades comuns (da melhor para a pior)

- **O(1)** — constante: independente do tamanho da entrada, o algoritmo sempre executa no mesmo tempo.
- **O(log n)** — logarítmica.
- **O(n)** — linear.
- **O(n log n)**.
- **O(n²)** — quadrática.
- **O(n³)** — cúbica.
- **O(2ⁿ)** — exponencial.
- **O(n!)** — fatorial.

Quanto maior a entrada, mais rápido cresce o tempo de execução de complexidades piores (ex: O(n²) cresce muito mais rápido que O(n) conforme n aumenta).

### Ordem de grandeza prática

Como referência de bolso: em um segundo, um computador consegue executar aproximadamente entre 10⁷ e 10⁸ operações/passos (isso varia conforme o tipo de operação). Esse número serve para estimar se uma solução é viável dentro de um limite de tempo.

**Exemplo:** se um problema tem entrada de tamanho 10⁶ e o limite de execução é 1 segundo, mas a solução encontrada tem complexidade O(n²), o número de operações seria (10⁶)² = 10¹². Isso é muito maior que 10⁸ operações/segundo, então essa solução não rodaria a tempo. Uma solução O(n) para a mesma entrada faria apenas 10⁶ passos, o que é viável.

## Os 3 passos para calcular a complexidade de um código

1. **Levar em consideração apenas as repetições do código** (loops).
2. **Verificar a complexidade das funções/métodos próprios da linguagem** usados no código (ex: `size()`, `sort()`, `find()`), pois elas também custam tempo.
3. **Ignorar constantes e usar apenas o termo de maior grau** da expressão final.

Esses passos são aplicados a vários exemplos de código (ilustrados em C++ com `std::vector`) ao longo do vídeo.

## Exemplos trabalhados

### Exemplo 1 — busca linear em um vetor

Código que recebe um `vector` e um valor `x`, percorre o vetor procurando `x`, retorna `true` se encontrar e `false` caso contrário.

- **Passo 1:** há um único laço (`for`) que repete `tamanho` vezes, onde `tamanho` é o tamanho do vetor de entrada → O(n).
- **Passo 2:** o código usa `vector::size()`. Consultando a documentação (cppreference), a complexidade de `size()` é **constante O(1)**. Comparações e retornos também são O(1).
- **Passo 3:** como o único termo não constante é o laço, a complexidade final é **O(n)**.

O vídeo destaca que, para descobrir a complexidade de funções/métodos nativos de uma linguagem (como `size()`), pode-se consultar a documentação oficial — no exemplo, o site **cppreference.com**, buscando a página do container (`vector`), a função de interesse (`size`) e a seção "Complexity".

### Exemplo 2 — dois `for`s aninhados, mesmo tamanho

Uma função recebe um `vector`, obtém o tamanho (constante), e tem dois laços `for` aninhados, ambos indo de 0 até `tamanho`, com comparações simples dentro (constantes).

- Laço externo: O(n). Laço interno: O(n). Como estão aninhados, multiplicam-se: **O(n) × O(n) = O(n²)**.
- Comparações internas são O(1) e são ignoradas.
- Complexidade final: **O(n²)**.

### Exemplo 3 — múltiplos `for`s sequenciais e aninhados (mistos)

Código com quatro laços: um `for` de 0 até `tamanho` (O(n)); outro `for` também até `tamanho` (O(n)); dois `for`s aninhados um dentro do outro fazendo operações, seguidos de mais um `for` simples até `tamanho` (O(n)).

- Multiplicando os dois `for`s aninhados: O(n) × O(n) = O(n²) — isso domina sobre o que vem depois.
- Somando os `for`s simples restantes: O(n²) + O(n) + O(n) = O(n²) + 2·O(n).
- **Passo 3** (ignorar constantes, manter o termo de maior grau): a constante "2" é descartada; entre O(n²) e O(n), o termo de maior grau é O(n²).
- Complexidade final: **O(n²)**.

### Exemplo 4 — dois `for`s independentes com tamanhos diferentes

Código com dois `for`s, cada um percorrendo um vetor diferente: um vai até `tamanho` (do vetor `v`, chamado de `n`) e o outro vai até `tamanho2` (de um vetor `w`, chamado de `m`). Como os tamanhos são variáveis independentes, não se pode dizer que ambos são O(n).

- Laço 1: O(n). Laço 2: O(m).
- Não há aninhamento entre eles (são sequenciais/independentes), e cada corpo de laço só tem operações constantes.
- Como são termos independentes multiplicados dentro de contextos diferentes (no exemplo dado, o resultado final combina os dois em um único termo multiplicativo), a complexidade final apresentada é **O(n·m)** — um único termo, já que não há um "+" separando termos distintos nesse caso.

### Exemplo 5 — menor idade repetida, via contagem (versão 1)

Código que recebe um `vector` de idades e verifica se a menor idade aparece pelo menos duas vezes:

1. Encontra a menor idade percorrendo o vetor uma vez (um `for`).
2. Percorre o vetor novamente contando quantas vezes a menor idade aparece; se o contador for maior que 1, retorna `true`.

- Dois laços sequenciais, cada um O(n): **O(n) + O(n) = 2·O(n)**.
- Uso de `size()` (constante), ignorado.
- **Passo 3:** descarta a constante "2" → complexidade final **O(n)**.

### Exemplo 6 — menor idade repetida, via ordenação (versão 2)

Código que faz a mesma coisa (verificar se a menor idade se repete), mas de forma "aparentemente" mais simples: ordena o vetor (`sort`) e depois compara a posição 0 com a posição 1; se forem iguais, a menor idade está repetida.

- À primeira vista parece mais rápido por ter menos linhas e nenhum laço explícito escrito no código — mas essa impressão é enganosa.
- **Passo 1:** não há laços explícitos escritos pelo programador.
- **Passo 2:** o código usa `sort()`. Consultando a documentação (cppreference), a complexidade de `sort()` é aproximadamente **O(n log n)**, onde n é o tamanho do vetor.
- Complexidade final: **O(n log n)**.
- **Conclusão do exemplo:** mesmo fazendo exatamente a mesma coisa, essa versão é **pior** que a versão anterior (O(n log n) > O(n)), porque a forma como `sort()` é implementada internamente pela linguagem tem custo maior do que dois laços lineares. Isso mostra que "código menor" ou "com menos linhas" não é sinônimo de "código mais rápido" — é preciso avaliar a complexidade real, inclusive de funções da biblioteca padrão.

### Exemplo 7 — busca em estrutura ordenada (`count`)

Código que recebe um valor `x` e um `vector` (ou estrutura similar, ex.: um `set`), e usa o método `.count(x)`.

- **Passo 1:** não há laço explícito.
- **Passo 2:** a complexidade de `count()` (no contexto do exemplo, uma estrutura ordenada/associativa) é **O(log n)**, conforme documentação.
- Complexidade final: **O(log n)**.

## Conclusão

O vídeo encerra reforçando que os 3 passos (achar repetições → checar complexidade de funções nativas usadas → ignorar constantes e manter o termo de maior grau) permitem calcular a complexidade de tempo da grande maioria dos algoritmos encontrados no dia a dia. Convida a audiência a se inscrever no canal e comentar dúvidas ou algoritmos específicos cuja complexidade não conseguiram calcular, para discussão nos comentários.
