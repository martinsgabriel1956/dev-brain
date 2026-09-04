# Algoritmos de Ordenação: Bubble, Insertion, Selection, Merge, Quicksort e Heapsort

> Transcrição de aula/vídeo em português (autor não identificado), formatada e pontuada a partir de fala corrida sem pontuação. Correções de ASR (reconhecimento de fala) marcadas entre colchetes onde o termo técnico original estava incorreto ou distorcido — ex.: "boa sorte" → "bubble sort", "incesting sort" → "insertion sort", "mej sorte" / "medi" → "merge sort", "rip sort" / "rip" → "heap sort" / "heap".

## Bubble Sort

Vamos falar agora sobre os algoritmos de ordenação. O primeiro deles é o **Bubble Sort**, que é o algoritmo que percorre a lista realizando as trocas dos elementos adjacentes caso o elemento à direita seja menor.

Como assim, professor? Ele vai comparar de dois em dois elementos em um arranjo. Imagina um arranjo, uma estrutura de dados com cinco elementos — cinco números, por exemplo: `-2, 45, 0, 11, -9`.

Vamos focar nessa primeira linha, onde `i = 0` (primeira iteração). Ele vai comparar: -2 é menor que 45? Sim. Então ele vai manter essa posição — a ideia é sempre jogar o elemento maior para a direita. Como -2 é menor que 45, mantém. Aí ele vai para a segunda posição: estava comparando o primeiro elemento com o segundo, agora vai comparar o segundo elemento com o terceiro, onde `i = 1`.

Aí ele vai verificar: 45 é maior do que 0? Sim. Então ele vai jogar o 45 para a posição do 0 e o 0 para a posição do 45 — faz a inversão de posições desses elementos no arranjo. Se a gente olhar agora em `i = 2`, o 45 agora ocupa a terceira posição. Aí ele vai comparar agora o terceiro com o quarto: 45 é maior do que 11? Sim. Então faz uma nova troca.

A ideia é sempre passar o elemento maior para a direita com isso. Na primeira passada (primeira comparação de cada dupla de elementos nesse conjunto), ele já vai ter o maior elemento na última posição — no caso, 45 vai chegar lá.

Aí ele vai repetir todo esse processo. O resultado final da primeira iteração é: `-2, 0, 11, -9, 45`. Aí ele vai fazer tudo de novo: -2 é maior que 0? Não. Então não troca. 0 é maior do que 11? Ele vai comparar agora a segunda e a terceira posição — não, então mantém. Agora vai comparar a terceira e a quarta posição: 11 é maior do que -9? Sim, então realiza uma nova troca nesse arranjo. Aí ele vai comparar 11 é maior do que 45? Não, então mantém.

Ainda não está ordenado, porque ainda falta passar o -9 mais para trás — ou seja, ele vai percorrer isso várias vezes. O Bubble Sort percorre o array comparando de dois em dois; se o elemento for maior que o elemento à direita, ele troca as posições. A ordem final vai ser o arranjo ordenado: `-9, -2, 0, 11, 45`.

Só para constar: esse é um algoritmo lento, justamente pela quantidade de comparações que ele tem que realizar. A melhor situação possível para o uso desse algoritmo é o arranjo já ordenado, e o pior caso é o arranjo na ordem inversa.

## Insertion Sort

Uma outra opção de ordenação é o **Insertion Sort** (ordenação por inserção), e esse aqui é fácil de lembrar porque é semelhante à ordenação de cartas. Quem já jogou baralho, qualquer jogo de cartas em que você tem que ordenar os valores do menor para o maior, da esquerda para a direita, é a mesma ideia.

Como que a gente faz: a gente posiciona — vamos comparar primeiramente os dois. Recebeu 4 cartas, como aqui: `4, 2, 6, 0`. A gente vai comparar — imagina o ser humano olhando, a gente não consegue comparar tudo ao mesmo tempo, então vou olhar os dois primeiros. Vou ver: o primeiro, o 4, é maior do que o 2? Sim. Então eu vou passar o 2 para a posição do 4 — a primeira posição vai ficar `2, 4`.

Aí agora eu vou analisar o terceiro elemento também: então eu tenho `2, 4, 6` — mantém, né, o 6 é maior do que o 4 e do que o 2, então mantém na posição dele. Ok, aí agora eu vou analisar o quarto elemento, que é aqui, no caso, o 0. O 0 é o menor desses três, sim, então eu vou passar ele lá para a primeira posição. Vai ficar `0, 2, 4, 6`.

É como se você tivesse ordenando um conjunto de cartas que acabou de receber num jogo. Primeiro analisa os dois primeiros, depois junto com o terceiro, depois junto com o quarto, e já posiciona. Por exemplo, se no lugar do 0 eu tivesse o 3 — ao invés de pegar esse quarto elemento e jogar para a primeira posição, ele ia jogar para a segunda, porque eu ia ter `2, 3, 4, 6`.

## Selection Sort

**Selection Sort**: esse é um outro algoritmo de ordenação que passa o menor valor para a primeira posição, o segundo menor para a segunda posição, e assim sucessivamente.

Diferentemente do Insertion Sort, que começa a comparação agregando um valor de cada vez (primeiro analisa os dois primeiros, depois os três, depois os quatro), no Selection Sort ele já compara o arranjo todo de uma vez. Tenho aqui o arranjo no estado inicial com os números `7, 4, 5, 9, 8, 2, 1`. No Selection Sort ele já vê qual é o menor desse arranjo e joga para a primeira posição — o menor vai para a primeira posição. Fixa o 1 ali, agora está fixo.

Aí a gente vai para o segundo arranjo (o restante). Ele vai comparar e descobrir qual é o segundo menor valor — o 2. Aí ele já coloca na segunda posição. Logo abaixo, ele vai localizar o terceiro menor valor — o 4 — e joga na terceira posição. Depois vai achar o quarto menor valor — o 5 — e joga na quarta posição, e assim sucessivamente até ter o arranjo ordenado.

## Merge Sort

Vamos agora ao **Merge Sort** (do inglês *merge*, mesclar). Como que ele funciona: ele divide recursivamente o arranjo ao meio em outros dois arranjos, até restarem elementos únicos, para depois combinar — fazer o que a gente chama de *merge* (mesclagem) — dos resultados. Ou seja, ele segue aquele paradigma de dividir para conquistar.

Vamos ver um exemplo: olhando aqui o primeiro arranjo, `6, 5, 12, 10, 9, 1`. Primeira coisa: divide ao meio. Ficam dois subarranjos. Aí cada subarranjo desse também vai ser dividido: ele jogou do lado esquerdo o 6 individualmente, e jogou `5, 12` para um subarranjo. Se fossem quatro elementos, ele criaria dois subarranjos com dois elementos, mas como são só três, ele jogou o da esquerda sozinho e trouxe os dois da direita (5 e 12) para um outro subarranjo.

Do lado direito, o mesmo processo: `10, 9, 1` foram separados — o 10 ficou sozinho (primeiro elemento), e o segundo e o terceiro elemento (9 e 1) vieram juntos e também foram divididos. Ele divide até ficar só um elemento — divide tudo, separa tudo, depois começa o processo de mesclagem.

Na mesclagem, ele já ordena, colocando o menor à esquerda e o maior à direita: 5 é menor que 12? Sim, então mantém — fica `5, 12`. Seguindo a subida da árvore à esquerda, mescla o 6 com o `5, 12` já ordenados: verifica e mescla esses três elementos, fica `5, 6, 12`.

Seguindo a subida da árvore à direita, mesma coisa: `10, 9, 1` foram separados — o 9 trocou de posição com o 1 naquele primeiro *merge* à direita (viram `1, 9`). Na hora de mesclar o 10 com `1, 9`, houve mudança de novo, ficou `1, 9, 10`. Observe que sempre que se mescla um novo subarranjo, ele já vem ordenado.

Por fim, ele mescla os dois subarranjos resultantes, já ordenados, e fica `1, 5, 6, 9, 10, 12`. Então, lembre: *merge* = mesclar. Só de saber a tradução da palavra já ajuda a resolver a questão em prova/concurso. Ele segue o paradigma de dividir para depois mesclar (conquistar), resultando no array ordenado.

## Quicksort

**Quicksort** também utiliza a abordagem de dividir para conquistar — vai separando em outros subarranjos. Só que ele faz o seguinte: tenho um arranjo qualquer, uma sequência de valores. Ele vai escolher um ponto de referência, que a gente chama de **pivô**. Imagina, digamos, o valor 5.

Aí ele vai separar em dois subarranjos: no da esquerda, ele vai posicionar os elementos que são **menores** que o pivô escolhido; na direita, ele vai posicionar os elementos que são **maiores**. Imagina esse primeiro exemplo: `6, 5, 12, 10, 9, 1`. Ele poderia escolher um pivô qualquer, digamos o número 5. Aí ele ia criar dois subarranjos: no subarranjo da esquerda, os elementos menores que 5 — nesse caso, só o 1. No subarranjo da direita, os outros elementos maiores que 5: `6, 9, 10, 12`.

Aí ele vai fazendo isso de novo — o Quicksort repete o processo nesses subarranjos: escolhe desse subarranjo um novo ponto de referência e divide de novo, jogando os menores para a esquerda e os maiores para a direita.

Qual seria o pior caso no uso desse algoritmo? Quando os pivôs escolhidos são sempre os extremos (o maior ou o menor valor do arranjo) — porque aí não muda muito: se você escolhe o maior valor, já tem no subarranjo à esquerda todos os menores valores (sem nenhum maior), então não vai ter um segundo subarranjo do outro lado — a divisão fica desbalanceada.

## Heapsort

Outro algoritmo é o **Heapsort**, e "heap" vem do uso de uma estrutura *heap*. O que é uma estrutura heap? É como se fosse um vetor — para quem não é da área técnica, um conjunto de valores, uma lista de valores quaisquer, que podem estar ordenados ou não. É uma estrutura de dados auxiliar, tal como uma lista encadeada ou uma fila.

O Heapsort tem a presença da árvore binária, mas utiliza também essa estrutura auxiliar chamada heap. Ele tem um passo a passo para execução: primeiramente, criar um **Max Heap** para todos os elementos — "Max" aqui significa descobrir qual é o maior elemento ali da árvore. Ele vai retirar a raiz (que é o maior elemento) e depois vai rebalancear a árvore.

Vamos entender: no primeiro passo (primeira figura), ele está comparando o 1 com o 12. Precisa fazer o Max Heap — jogar o maior valor para a raiz. O 12 é maior do que o 1? Sim, então ele joga o 12 para a posição 0 e o 1 fica na posição 1. Descendo para baixo, ele compara agora o 1 com o 6 (posição 1 com a posição 4): o 6 é maior que o 1? Sim, então ele joga o 1 para a posição do 6 e o 6 para a posição do 1.

A ideia é sempre ter o maior valor na raiz. Não entendi, professor? Olha aqui: analisando `5, 1, 6` — isso é uma árvore, `5, 1, 6`. Qual é a raiz dessa subárvore? A posição do 1. Qual é o maior elemento desses três? O 6. Então o 6 tem que vir para a raiz — fica `6, 5, 1`. É sempre nessa ordem: no caso, o 9 é menor do que o 10, então tá certo o 10 ficar acima do 9; e o 10 é menor do que o 12, então também está certo. Sempre a raiz tem que ser maior do que os elementos filhos — elemento pai (a raiz) tem que ser maior que os elementos filhos, para cada subarranjo. É assim que o Heapsort funciona: tem a árvore binária, mas com o auxílio de uma estrutura auxiliar (o heap).
