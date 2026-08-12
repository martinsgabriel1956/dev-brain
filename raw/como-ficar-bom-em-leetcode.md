# Como ficar bom em LeetCode

> Transcrição de vídeo (pt-BR), limpa e organizada. Canal de programação com foco em Python.

## Antes do "como", o "porquê"

Antes de entender **como** ficar bom em LeetCode, primeiro é preciso entender **por que** você quer ficar bom nisso. Se você clicou no vídeo, provavelmente já tem algum motivo em mente. Os três principais motivos, na minha opinião:

1. **Passar em entrevistas.** É o motivo principal e não há nada de errado com ele — de fato vai te ajudar bastante.
2. **A ideia de que LeetCode está ligado a "lógica de programação".** É um termo vago que não significa muita coisa, e muita gente discorda, mas faz certo sentido: os problemas estilo LeetCode estão na classe dos problemas mais difíceis de resolver em computação. A lógica que você aprende às vezes é abstrata — você não vai ficar bom em *programação do dia a dia* fazendo LeetCode (resolver "tal browser não suporta tal coisa", erro de CORS etc. não tem nada a ver com LeetCode). Mas ajuda tangencialmente com alguns tipos de problema específicos e dá **fluência na linguagem**, o que facilita consertar outros problemas.
3. **Interesse genuíno em estruturas de dados e algoritmos.** Perfeitamente válido.

## Passo 1 — Escolher uma linguagem

Escolha **uma** linguagem e, de preferência, use só ela para LeetCode. Não precisa ser a que você usa no trabalho — dependendo dela, recomendo até que **não** seja.

Prefira uma linguagem com **pouco boilerplate**, rápida para fazer coisas simples:

- **Python** (minha recomendação): a mais rápida para prototipar coisas simples estilo LeetCode. Tipagem fraca (`a = 0` sem declarar tipos), poucos imports/módulos. LeetCode é essencialmente prototipar um algoritmo e testá-lo várias vezes — Python brilha nisso.
- **Go**: também rápido de escrever, parecido com Python em certos aspectos. Boa alternativa.
- **JavaScript**: boa opção também, apesar de alguns comportamentos estranhos (que raramente aparecem nesses problemas).

**O que evitar (a menos que você já seja muito bom nelas):** Rust, Haskell. Aprender LeetCode é um *skill set* diferente de aprender uma linguagem complexa. Fazendo as duas coisas ao mesmo tempo, você briga mais com a linguagem e menos com o problema — o aprendizado dos algoritmos fica mais lento. Faça uma coisa de cada vez. (Se você já tem 10 anos de Java e nunca viu Python, aí sim faça em Java.)

Numa entrevista, Python é mais rápido; Rust te obriga a "chapar" tudo e acaba mais lento e desafiador.

## Passo 2 — Entender as estruturas de dados mais comuns

Não precisa estudar todas antes de começar — dá pra ir num modelo iterativo (estuda uma, faz exercícios dela, passa pra próxima). Lista das que valem a pena:

- **Array**
- **Linked list**
- **Queue** (fila)
- **Stack** (pilha)
- **Binary tree** (árvore binária)
- **Hash map**
- **Graph** (grafo)

Quase todo problema de LeetCode cai em uma (ou algumas) dessas. Estruturas como **B-tree** ou **heap** são mais raras — não vale focar tanto nelas, principalmente no começo.

Junto disso, aprenda **Big O** — é obrigatório para ficar bom em LeetCode. (Ponto final. Tenho um vídeo no canal sobre isso.)

### Onde estudar

- Google + GeeksforGeeks (ou similares) para a explicação de cada estrutura.
- Se você fala inglês: **Frontend Masters** tem o curso gratuito do **ThePrimeagen**, muito bom — ensina a implementar árvore binária, por exemplo.
- Livro **"Entendendo Algoritmos"** (*Grokking Algorithms*), muito recomendado.

**Dica chave:** **implemente** cada estrutura por conta própria (uma árvore binária, uma linked list etc.). Isso fixa o entendimento.

## Passo 3 — Identificar os padrões de problema

Depois de entender e implementar uma estrutura, identifique os **padrões** mais comuns dela.

Exemplo com **binary tree**: quase tudo se resolve com **DFS** (depth-first search) ou **BFS** (breadth-first search). Estude os dois.

No LeetCode: filtre por `binary tree`. Ordene por **acceptance rate** (taxa de aceitação alta costuma indicar problema intuitivo, não necessariamente fácil) ou de **Easy → Hard**, e vá resolvendo.

### Exemplo prático

Abri um problema de **binary search tree** (BST). Se você não conhece o termo, **pesquise** e volte. Uma BST é uma árvore ordenada para busca: todos os nós à direita de um valor são maiores; à esquerda, menores — recursivamente.

O problema: dados dois inteiros `low` e `high`, retornar a soma de todos os nós entre eles (inclusivo). Entendi o problema, mas não sei resolver na hora → tento por **no máximo ~10 minutos**. Se não vier uma solução clara, vou em **Solutions**, escolho minha linguagem (Python) e vejo a solução mais votada/visualizada (costumam ser boas). Ela explica: aqui usa-se uma **DFS** (como eu disse, a maioria de binary tree cai em DFS ou BFS).

## Passo 4 — Não fique quebrando a cabeça

Se você **não sabe** resolver um problema, você **não sabe** — talvez nunca tenha visto aquele algoritmo. Não há nada a aprender ficando 3 horas batendo cabeça.

Deu ~5–10 minutos e não enxergou nem o início de uma solução? **Esqueça.** Abra as *submissions*, olhe o código, tente entender **linha por linha** e **reescreva** (não copie e cole — reescrevendo você presta mais atenção no que acontece). Assim você aprende a implementação (ex.: uma DFS).

Depois volte à lista, ache **outro** problema do mesmo padrão (ex.: outro DFS, como *Sum Root to Leaf Numbers*) e resolva. Depois de 2, 3, 4 problemas de DFS, começa a ficar fácil e você passa a **reconhecer** quando o enunciado pede DFS.

## Padrões principais para focar

- **BFS / DFS** — extremamente comuns.
- **Sliding window** (janela deslizante).
- **Backtracking**.
- **Dynamic programming** — comece pelo Fibonacci em DP.
- **Hash map** — resolve quase tudo.
- **Two pointer** — cai muito, muito, muito. Provavelmente o **primeiro** em que focar.

## Resumo do método (o loop)

1. Entenda uma estrutura de dados (ex.: binary tree).
2. Entenda os algoritmos dela (ex.: DFS).
3. Repita vários exercícios desse padrão no LeetCode até **reconhecer** quando o enunciado o pede.
4. Volte ao passo 1 com a próxima estrutura (ex.: Array → sliding window).
5. Repita.

É assim que você fica bom em LeetCode: **bastante repetição**, sem segredo. E não fique quebrando a cabeça — se não entendeu, olhe a solução, entenda-a e vá para o próximo exercício.
