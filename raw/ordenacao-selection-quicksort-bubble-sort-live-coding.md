# Ordenação de Listas: Selection Sort, Quicksort e Bubble Sort (Live Coding)

Transcrição de um corte de live coding (canal de cortes, material extraído do canal principal "Fernanda Kiperdev", lives no 2º e 4º domingo do mês), com leitura de trechos do livro *Entendendo Algoritmos* (Aditya Bhargava). Já em português — sem tradução. Título original desconhecido; título descritivo derivado do conteúdo.

> **Nota de limpeza:** a transcrição automática corrompeu alguns termos, corrigidos por contexto: "arrei/arrey" → array; "ponto sorte" → `.sort`; "quicks sort/quissort" → Quicksort / `qsort`; "Bubl Sorte" → Bubble Sort; "Kishmor Kumar" → Kishore Kumar; "The Black Eyes" → provavelmente The Black Keys (exemplo do livro); "lenf" → `len`; "tray" → provável editor Trae; o trecho do quadro de tempos de execução para O(n!) ("1.27 x 10 né anos… 2559 anos") está truncado/incoerente na fala e foi mantido apenas de forma aproximada. Pontuação e pausas de fala foram reorganizadas em parágrafos; o conteúdo não foi alterado.

## Abertura: revisar algoritmos de ordenação

A ideia da live é revisar algoritmos de ordenação de listas. Na live anterior (domingo passado) o tema foi busca binária (pesquisa binária), o algoritmo usado para encontrar elementos numa lista já ordenada sem passar por todos os elementos. Com uma lista de 1 milhão de elementos ordenados, dá para aplicar busca binária e achar um item sem varrer tudo.

Agora a pergunta é: e se eu quero **ordenar** essa lista? Os elementos podem ser numéricos ou strings; a ordem crescente pode ser do menor para o maior número, ou alfabética (da letra A até o final do alfabeto). Com milhões de dados, como ordenar de maneira eficiente?

Muita gente vai pensar: "coloco no JavaScript, `lista.sort()`, já era". Não é bem assim. Primeiras perguntas:

- Qual algoritmo o `.sort` do JavaScript utiliza? E o `sort` do Python? (O Java também tem — não lembro de cabeça se o método está em `List` ou em `Array`.)
- Caso eu precise otimizar esse algoritmo padrão, como faço?

Isso mostra que os algoritmos que estamos aprendendo já vêm traduzidos em funções nativas das linguagens. Ao chamar essas funções, é preciso saber: qual algoritmo roda por trás? Qual a eficiência dele? Até que ponto ainda é eficiente? Certos algoritmos, mesmo recursivos, funcionam com 30 itens, mas com 500, 1000, 2000 ou 1 milhão de itens deixam de ser eficientes para o caso de uso — e aí, qual é o melhor algoritmo? É essa malícia, essa visão crítica, que a gente tem que desenvolver.

Vamos começar com a ordenação mais simples, a **ordenação por seleção**. Para acompanhar, é preciso ter compreendido arrays e listas e a notação Big O — arrays e listas já vimos; Big O eu vou explicando à medida que aparece, para quem não está familiarizado.

## Ordenação por seleção (Selection Sort)

Suponha uma lista de músicas no computador e, para cada artista, um contador de plays: Radiohead tocou 156 vezes, Kishore Kumar 141 vezes, The Black Keys 35 vezes. Você quer ordenar a lista de artistas do mais tocado (Radiohead) para o menos tocado, para categorizar seus artistas favoritos.

Uma maneira: pegar o artista mais tocado da lista e adicioná-lo a uma **nova lista**. Começo com uma lista nova, zerada, e faço um loop na lista inicial para encontrar o artista com maior número de plays; adiciono na nova lista em primeiro lugar. Depois repito o loop procurando o segundo artista mais tocado e adiciono em segundo lugar. Repito até terminar com uma lista nova ordenada.

Vamos pensar como engenheiros de computação e avaliar quanto tempo isso demora. O tempo de execução O(n) significa que você precisa passar por todos os elementos da lista uma vez. O `n` é o `len` da lista — o número de itens. Esse `n` é muito usado nas notações de complexidade (a notação Big O). Dizer O(n) significa que a complexidade aumenta proporcionalmente ao número de itens: com 100 itens, leva o tempo de percorrer 100 itens; com 200, o dobro. Para encontrar o artista com maior número de plays você verifica cada item da lista — O(n).

Para criar a nova lista ordenada, essa mesma operação (percorrer todos os itens e selecionar o de maior número de plays) precisa ser feita **n vezes**: com n itens, o loop pela lista é repetido n vezes. No final é n × n — é como um `for` dentro de outro `for`. Sempre que há um loop `for` dentro de outro loop `for`, a complexidade é O(n²): o `for` externo vai do índice zero ao último; para cada item, o `for` interno percorre de novo todos os itens. Equivale a multiplicar n por n. Portanto, a ordenação por seleção tem complexidade O(n²).

Algoritmos de ordenação são muito úteis: dá para ordenar nomes numa agenda telefônica, datas de viagem, e-mails, números de processo, a posição de uma pessoa numa lista — qualquer coisa que possa ser ordenada.

### "Mas eu verifico menos elementos a cada vez…"

Talvez você esteja pensando: conforme passo pela lista e encontro o próximo maior, acabo checando menos elementos a cada loop — então o tempo de execução ainda é O(n²)? Boa pergunta, e a resposta tem a ver com a notação Big O (o livro detalha no capítulo seguinte). Você está certo em não precisar verificar n elementos toda vez: verifica n, depois n − 1, n − 2, n − 3… Na média, verifica uma lista com metade dos elementos: o tempo seria O(n × ½ × n). Mas **constantes como ½ são ignoradas na notação Big O**. Isso é muito importante — quem fez computação e estudou algoritmos e estruturas de dados vai lembrar. Sempre que há uma constante atrelada à função que calcula o tempo de execução, as constantes são cortadas.

Por quê? Porque a constante é irrelevante para casos gigantescos. Exemplo: se n fosse 500 milhões, n × n é um número gigantesco, com vários zeros no final. Dividir por dois (250 milhões) diminui, mas não muda a ordem de grandeza — continua gigantesco. Quando falamos de números em escala, qualquer constante "não faz cosquinha" na análise de eficiência de tempo. Essa função matemática é para analisar tempo de execução de um algoritmo em escala, não para casos com 100 ou 50 elementos — nesses, sinceramente, não importa qual algoritmo você escolhe, o tempo vai ser mais ou menos o mesmo. A diferença começa a "gritar" na casa dos milhões de itens.

Há raras exceções: com um algoritmo O(n²), ou com um algoritmo recursivo, chegar a 100 ou 200 chamadas recursivas já começa a ficar feio e lento. Mas em listas, a diferença só aparece na casa de 100.000, 200.000, 500.000 elementos — com 100, 200 ou 400 números não faz muita diferença.

A ordenação por seleção é um bom algoritmo, mas não é muito rápido. O **Quicksort** é um algoritmo de ordenação mais rápido, com tempo de execução O(n log n) — visto adiante (capítulo 4 do livro).

## Quicksort

Depois da ordenação por seleção (o algoritmo mais básico), passamos ao Quicksort: um algoritmo de **dividir para conquistar**, de que já demos uma palhinha na última live, e muito mais eficiente. Depois passamos ao Bubble Sort.

A estratégia do Quicksort é **recursão de maneira inteligente**: ele não fica fazendo recursões infinitas; faz recursão para ir quebrando a lista em listas menores até chegar ao caso base. Chegando ao fundo da recursão, ele começa a retornar e voltar ao topo, ordenando a lista.

Exemplo informal de lista com 10, 15 e 33: divido 10 e 15 numa lista e 33 na outra; 10 e 15 são só dois elementos — o segundo é maior que o primeiro? Se não for, inverto a posição. Volto no caso de recursão e retorno para cima; tenho duas listas ordenadas e faço o *merge* numa lista única. *(Nota: durante a fala, o apresentador primeiro diz que o caso base é "de zero a um elemento", corrige-se para "um ou dois elementos", e depois, lendo o livro, o caso base é apresentado corretamente como array vazio ou com um elemento — ver "Livro" abaixo.)*

### Leitura do livro

O Quicksort é um algoritmo de ordenação muito mais rápido que a ordenação por seleção, e muito utilizado na prática. Por exemplo, a biblioteca padrão da linguagem C tem uma função chamada `qsort`, que é a implementação do Quicksort. Ele utiliza a estratégia de dividir para conquistar.

Vamos usar o Quicksort para ordenar um array. Qual é o array mais simples que um algoritmo de ordenação pode ordenar? Alguns arrays nem precisam ser ordenados: um array vazio ou com um elemento é o mais fácil — não há nada para fazer. Então arrays vazios ou com apenas um elemento serão o **caso base** da recursão: quando a recursão para, você pode apenas retornar esses arrays como estão. Escrevendo a função: `def quicksort(array)`: se `len(array) < 2`, retorna o array. Esse é o caso base, onde a recursão para.

Um array com dois elementos também é simples: confiro se o primeiro é menor que o segundo; caso contrário, troco de lugar (swap). Agora um array com três elementos. Lembre-se de que você está usando dividir para conquistar: quebre o array até chegar ao caso base. A lógica do Quicksort:

1. Primeiro você escolhe um elemento do array. Esse elemento é chamado de **pivô** (falaremos depois sobre como escolher um bom pivô; nesse momento vamos usar o primeiro item do array).
2. Encontre os elementos menores que o pivô e os elementos maiores que o pivô. Isso é chamado de **particionamento**. Você tem um subarray com todos os números menores que o pivô, o pivô, e um subarray com todos os números maiores que o pivô. Os dois subarrays não estão ordenados — apenas particionados.
3. Se os subarrays estivessem ordenados, a ordenação do array completo seria simples: `array_esquerdo + pivô + array_direito` dá um array ordenado.

Como ordenar os subarrays? O caso base do Quicksort já consegue ordenar arrays de dois elementos e arrays vazios; então, se você aplicar o Quicksort em ambos os subarrays e combinar os resultados, terá um array ordenado. Isso funciona com **qualquer pivô**: suponha que você escolha 15 como pivô de [10, 15, 33]; ambos os subarrays contêm apenas um elemento, e você já sabe ordenar isso. Logo, já sabe ordenar um array de três elementos: escolhe um pivô, particiona em dois subarrays (menores e maiores que o pivô) e executa o Quicksort em cada um.

Com quatro elementos (ex.: [33, 10, 15, 7]): escolhendo 33 como pivô, 10, 15 e 7 vão para um único subarray e o subarray dos maiores fica vazio. O subarray da esquerda tem três elementos — então executo o Quicksort de novo: escolho um pivô (10, por exemplo), particiono em [7] e [15], que já são casos base. Aplico isso recursivamente a todos os subarrays até chegar a subarrays de zero ou um item; a partir daí vou retornando os resultados, até o primeiro caso onde tenho dois subarrays e o pivô: encaixo o subarray de um lado, o outro do outro lado, e o pivô no meio.

### Por que O(n log n) e não O(n²) ou exponencial?

A cada recursão o array diminui — é dividido ao meio, literalmente. Isso é um comportamento padrão de logaritmo: a cada execução o número de elementos que preciso passar é cada vez menor. E por que o `n`? Porque em cada nível é preciso um `for` sobre todos os elementos para separar os maiores e os menores que o pivô, o que é uma execução nos n elementos. Então tenho n (trabalho por nível) × log n (número de níveis de recursão) = O(n log n).

### Quadro de tempos de execução (do livro)

Os tempos do quadro são estimativas para um caso em que se executam **10 operações por segundo** — apenas ilustrativos, não regra, porque hardware, quantidade de processos rodando, linguagem, processador (Intel ou AMD) etc. interferem. Na realidade o computador executa muito mais que 10 operações por segundo; o quadro serve só para mostrar quão diferentes são os tempos de execução. Para um array de tamanho 1000:

| Complexidade | Tempo estimado (a 10 ops/s) | Algoritmo de exemplo |
|---|---|---|
| O(log n) | 1 segundo | busca binária |
| O(n) | 100 segundos | busca simples |
| O(n log n) | ~996 segundos | Quicksort |
| O(n²) | ~27 horas | ordenação por seleção |
| O(n!) | astronomicamente grande (anos) | caixeiro-viajante |

O livro menciona também o **Merge Sort**, com tempo de execução O(n log n), muito mais rápido que a ordenação por seleção.

### Pior caso e caso médio

O Quicksort é um caso complicado: no pior caso, o tempo de execução é O(n²) — tão lento quanto a ordenação por seleção — mas é o pior caso possível; no caso médio, é O(n log n). O que é pior caso e caso médio? O pior caso é o pior cenário possível para o algoritmo (na fala: o array completamente invertido, obrigando a quebrar todos os subarrays e a fazer swap de todos os números); o melhor caso é aquele em que já está quase tudo ordenado e é preciso fazer um único swap. Muito se fala em pior caso, melhor caso e caso médio ao analisar a complexidade de tempo dos algoritmos.

## Bubble Sort

Agora o Bubble Sort. (O apresentador abre o Geeks for Geeks, "Bubble Sort Implementation", copia o código para um arquivo `bubblesort.js` e pega também um exemplo de Quicksort para comparar.)

O Quicksort chama a si mesmo — isso é **recursão** — e além disso faz a partição: divide o array em subarrays, e a cada nova chamada passa um array menor do que recebeu (um dos subarrays que particionou). Já o Bubble Sort funciona com **um `for` dentro de um `for`**: um loop entre todos os elementos do array, mais outro loop entre todos os elementos; salva uma variável temporária e faz o swap dos elementos caso um seja maior que o outro; repete até passar por todos os elementos. Na página do Geeks for Geeks há uma imagem dos swaps, elemento por elemento, até ficarem ordenados.

Na análise de complexidade do Bubble Sort: o **melhor caso é O(n)**, o **pior caso é O(n²)** — que se aproxima muito do pior caso do Quicksort. Então, apesar da eficiência do Quicksort em alguns casos, se por algum motivo o array que ele recebe não facilita a vida do algoritmo, ele terá o mesmo tempo de execução do Bubble Sort, um algoritmo mais simples que ordena com um loop dentro do outro.

Devemos sempre olhar para o *worst case scenario*. O Quicksort é considerado O(n log n) porque o pior caso acontece só em casos muito esdrúxulos, e dá para otimizar um pouco: quando se seleciona o pivô da maneira mais eficiente, consegue-se garantir eficiência O(n log n). Se eu pegasse o elemento do meio e o array já estivesse ordenado, também consigo garantir isso. A eficiência do Quicksort está muito atrelada à **escolha do pivô**: pode ser o primeiro elemento do array, o do meio, o último ou um elemento aleatório — dependendo de qual pivô escolher, isso pode impactar o tempo de execução.

## Encerramento

Esse quadro foi retirado do live coding que acontece todo segundo e quarto domingo do mês no canal principal Fernanda Kiperdev, com conteúdos aprofundados sobre programação e tecnologia. Se gostou, deixe o like, inscreva-se no canal de cortes e acompanhe a live ao vivo no canal principal.
