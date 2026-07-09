# 9 Algoritmos que Todo Programador Deveria Saber

E aí, meu nome é Forrest, bem-vindo de volta. Existem três tipos de algoritmos que você deveria conhecer como programador — na verdade, a gente vai passar por nove algoritmos neste vídeo: o que são, como funcionam, casos de uso reais, com exemplos de código e explicações. Mas todos eles se encaixam em três categorias:

- **Algoritmos de ordenação (sorting)** — usados para reorganizar elementos de uma lista ou array em uma certa ordem.
- **Algoritmos de busca (searching)** — usados para encontrar ou recuperar um elemento de uma estrutura de dados, ou para determinar sua existência e localização no conjunto de dados.
- **Algoritmos de grafo (graph)** — usados para resolver problemas relacionados à teoria dos grafos, onde os dados são representados como uma coleção de nós (ou vértices) conectados por arestas. Você provavelmente conhece isso na forma de árvores.

Assim como no vídeo sobre as quatro estruturas de dados fundamentais, quero dizer que tenho orgulho de você por ter clicado neste vídeo — isso não é o glamour de sonhar em ser engenheiro de software, isso é a parte suja, o trabalho que de fato te transforma em engenheiro de software.

## Por que esses algoritmos importam

Eles formam a base da resolução eficiente de problemas em ciência da computação. Estudá-los não só melhora habilidades de programação como aprofunda o raciocínio analítico, e são fundamentais para otimizar performance de software em uma ampla gama de aplicações do mundo real. É como a diferença entre construir algo com um martelo versus uma pinadeira pneumática (nail gun): os dois fazem o trabalho, mas a pinadeira é claramente mais eficiente na maioria dos projetos — só que às vezes o martelo é a escolha melhor, dependendo do escopo da tarefa. O mesmo vale para algoritmos: alguns são melhores para a maioria das tarefas, mas não para todas, e você precisa saber que essas alternativas existem para escolher a certa. Se você nunca soube que a pinadeira existia, boa sorte tentando construir a casa inteira só com o martelo.

## Algoritmos de Ordenação

Um algoritmo de ordenação é um método usado para reorganizar elementos de uma lista ou array em uma certa ordem — crescente, decrescente, ou até baseada em regras mais complexas. O propósito é organizar os dados de um jeito que facilite o uso, a busca, a análise e a exibição eficiente da informação. É como pegar um baralho embaralhado e querer colocá-lo em ordem.

Existem oito algoritmos de ordenação diferentes atuando sobre quatro condições iniciais diferentes — aleatório, quase ordenado, invertido e poucos valores únicos — e é uma representação bonita de como esses algoritmos são ótimos para ordenar algumas condições iniciais, mas ruins para outras. Vamos detalhar alguns deles:

### Bubble Sort

Ensinando programadores a não ordenar coisas desde os anos 1950, mas uma ótima representação de como algoritmos de ordenação funcionam. O Bubble Sort é um algoritmo simples que percorre o array repetidamente, elemento por elemento, comparando o elemento atual com o seguinte e trocando seus valores se o primeiro for maior que o segundo — repetindo esse processo até que o array esteja ordenado.

O código funciona assim: primeiro, determina o tamanho do array. O loop `for` externo representa cada passagem pelo array inteiro, enquanto o loop `for` interno itera sobre a parte ainda não ordenada do array, e o `if` compara elementos adjacentes, "borbulhando" o maior elemento até o topo. Daí vem o nome.

Tem complexidade de tempo médio e de pior caso de O(n²), o que significa que não é uma boa escolha para ordenar coisas.

### Insertion Sort

Na maioria das vezes um pouco melhor. O Insertion Sort é outro algoritmo simples que constrói o array final ordenado um elemento de cada vez. O código funciona assim: o loop `for` seleciona sequencialmente cada elemento do array, começando no índice 1 (o segundo elemento). Para cada elemento selecionado (a "chave"), o loop `while` compara essa chave com os elementos da parte já ordenada do array; enquanto a chave for menor que os elementos ordenados, esses elementos são deslocados para a direita para abrir espaço, até encontrar a posição correta para inserir a chave. Esse processo se repete até que cada elemento tenha sido posicionado corretamente.

Assim como o Bubble Sort, tem complexidade média e de pior caso de O(n²) — porém sua complexidade de melhor caso é O(n), o que o torna uma ótima escolha quando o conjunto de dados já está quase ordenado, mas uma escolha ruim quando o conjunto está invertido.

### Merge Sort

Agora vamos ver um dos algoritmos de ordenação mais eficientes. O Merge Sort é um algoritmo eficiente, estável, baseado em comparação, do tipo dividir-para-conquistar, e é recursivo. Ele divide o array de entrada em duas metades, chama a si mesmo recursivamente para cada metade (ordenando-as) e depois mescla as duas metades ordenadas.

O código funciona assim: a função de merge sort verifica se o array tem mais de um elemento (já que um único elemento já está ordenado por definição). Ela então divide o array em duas metades e chama a si mesma recursivamente para cada metade. Uma vez que as metades estão ordenadas, a função de merge pega essas duas metades ordenadas e as mescla em um único array ordenado, comparando os elementos de ambas as metades um a um e colocando o menor elemento no novo array, continuando até que todos os elementos estejam ordenados e mesclados.

O Merge Sort tem complexidade de tempo O(n log n) em todos os casos — porém requer espaço adicional para os arrays temporários usados no processo de merge, o que pode ser um problema em ambientes com restrição de memória. Já um algoritmo como o Quicksort, que quase sempre é tão bom quanto o Merge Sort, é um algoritmo *in-place* que requer muito pouca memória extra.

Existem muitos outros algoritmos de ordenação, como Selection Sort, Shell Sort, Heap Sort, e assim por diante. O algoritmo de ordenação que você usa depende do seu caso de uso, das capacidades do sistema e das características específicas dos dados com que você está lidando (tamanho, se já está parcialmente ordenado, etc). Algoritmos de ordenação são fundamentais em ciência da computação e usados em muitas aplicações reais, desde organizar arquivos em um computador até ordenar registros de banco de dados para recuperação fácil.

## Algoritmos de Busca

Um algoritmo de busca é um método usado para encontrar ou recuperar um elemento de uma estrutura de dados. O objetivo é determinar se um item existe no conjunto de dados e, frequentemente, determinar sua localização. É como abrir as páginas amarelas para procurar um número de telefone específico — só que você precisa fazer isso milhares de vezes, então é melhor que seu algoritmo de busca esteja correto.

### Linear Search (Busca Linear)

Uma forma de fazer isso é via um algoritmo de busca sequencial, como o Linear Search, que é exatamente o que o nome sugere: cada elemento é verificado em sequência até você encontrar o que procura ou a lista terminar. Se o elemento atual for igual ao que estamos procurando (X), ele é retornado.

A complexidade de tempo média e de pior caso é O(n), onde n é o número de elementos do array. Em outras palavras: se o elemento estiver no primeiro índice, essa é uma boa escolha de algoritmo de busca — mas se estiver no último índice, talvez não seja tão bom assim.

### Binary Search (Busca Binária)

Um algoritmo de busca por intervalo, como o Binary Search, é uma abordagem mais eficiente, assumindo que o conjunto de dados está ordenado. Ele funciona dividindo repetidamente o intervalo de busca ao meio. Voltando à analogia das páginas amarelas (que já estão em ordem alfabética, ou seja, já ordenadas): seria como abrir o livro direto na metade e, baseado no nome que você procura (digamos que comece com "T"), eliminar a primeira metade; então você pega a segunda metade, divide ela ao meio, verifica o elemento do meio, vê de que lado desse elemento do meio está o que você procura, elimina essa metade, e assim por diante, até encontrar o elemento ou concluir que ele não está na lista.

O código funciona assim: você passa o array ordenado e o elemento que está procurando para a função de busca binária. Inicializa os limites esquerdo e direito para representar o intervalo de busca atual. O loop `while` acessa o meio do intervalo de busca atual, compara o elemento do meio do array com o valor-alvo e, se não forem iguais, elimina a metade do array que não contém o alvo. Repete esse processo no restante do array até encontrar o alvo ou até o array não poder mais ser dividido, o que significa que o alvo não está lá.

A complexidade de tempo da busca binária é O(log n) nos casos médio e de pior caso, tornando-a significativamente mais rápida que a busca linear para arrays ordenados.

Existem muitos outros algoritmos de busca, como jump search, exponential search, Fibonacci search — ou você pode simplesmente usar uma busca em hash table e procurar a chave diretamente na hash table, com complexidade de tempo O(1) (embora isso nem sempre seja garantido). Busca é fundamental em tarefas como consultar bancos de dados, procurar algo nos seus arquivos, e muitas outras aplicações onde a recuperação rápida é crucial.

## Algoritmos de Grafo

Algoritmos de grafo são outro tipo de algoritmo que você deveria conhecer. São um conjunto de instruções usadas para resolver problemas relacionados à teoria dos grafos, onde os dados são representados como uma coleção de nós conectados por arestas. Assim como árvores, algoritmos de grafo são extremamente importantes para lidar com e analisar relações entre elementos, usados em inúmeras aplicações reais como redes de computadores, redes sociais e mapas de rotas de fato. Quando você digita um endereço no Google Maps e recebe direções, isso é um algoritmo de grafo em ação. Nesses casos, pense nos nós como interseções e nas arestas como as estradas.

### DFS — Depth-First Search (Busca em Profundidade)

Uma forma relativamente ineficiente de resolver isso seria usar o DFS (busca em profundidade). O DFS é exatamente o que o nome sugere: você vai o mais fundo possível em um único caminho, vê se funciona, e se não funcionar, volta (backtrack) e tenta outro. Basicamente, ele fica tentando diferentes rotas em cada interseção para ver se chega ao destino, verificando cada curva e estrada possível até chegar lá — não exatamente a melhor forma de fazer isso, mas é recursivo.

No código, a função de DFS recebe o grafo que precisa percorrer, o nó inicial, e os nós já visitados durante cada chamada recursiva. Em cada chamada, a função marca o nó atual como visitado e então explora iterativamente cada um dos vizinhos ainda não visitados desse nó; se um vizinho ainda não foi visitado, o processo continua recursivamente até que todos os nós alcançáveis a partir do ponto inicial tenham sido visitados.

A complexidade de tempo do DFS depende de como o grafo é representado: se for representado usando listas de adjacência, é uma complexidade de tempo; se for representado usando matriz de adjacência, é outra. Mas em termos de complexidade de espaço, na maioria dos casos o DFS tem complexidade O(V), onde V representa os vértices (também conhecidos como nós — os dois termos são intercambiáveis).

### BFS — Breadth-First Search (Busca em Largura)

Sempre que se fala de DFS, é preciso falar de BFS também, que também é exatamente o que o nome sugere: em vez de ir fundo em um único caminho como o DFS, o BFS se expande em largura, simultaneamente, camada por camada — lançando uma rede ampla a partir do ponto inicial e gradualmente expandindo essa rede.

Basicamente: se você está no meio de uma interseção com quatro opções (quatro estradas), você percorre as quatro até a próxima interseção, uma por vez — essa é a primeira camada. Se você ainda não chegou ao destino final em nenhuma dessas interseções (nós), você começa a próxima camada verificando todas as estradas (arestas) restantes a partir de cada uma dessas interseções onde você está agora — 12 nós simultaneamente, verificando todas as arestas até os próximos nós, até encontrar seu destino.

Como o BFS mantém registro dos caminhos percorridos, você consegue reconstruir a rota tomada, que será o caminho mais curto — mas apenas em termos do número de nós percorridos, não necessariamente em distância real. Ainda não é a melhor forma de resolver o problema, e tem a mesma complexidade de espaço e tempo do DFS.

### Algoritmo de Dijkstra

Em vez disso, usamos o algoritmo de Dijkstra — que é, literalmente, o algoritmo que o Google Maps usa (ou pelo menos uma versão modificada e aprimorada dele; depois eles também modificam e evoluem isso até o algoritmo A*, e então customizam ainda mais até chegar na versão proprietária deles, que funciona bem melhor que a do Apple Maps na maior parte do tempo).

O algoritmo de Dijkstra encontra o caminho mais curto entre um nó dado (chamado de "nó fonte") e todos os outros nós de um grafo. Mas não só isso: ele também usa os pesos das arestas (as estradas) para encontrar o caminho que minimiza o peso total, ou distância, entre o nó fonte e todos os outros nós. Em resumo, ele leva em conta a distância e o custo de cada estrada — algo parecido com considerar fatores como comprimento da via, condições de trânsito e limite de velocidade para determinar a rota mais rápida. Esse é o único dos três algoritmos de grafo aqui discutidos que de fato "pensa à frente", recalculando a melhor rota conforme você se move de nó em nó.

### Algoritmo A* (A-Star)

E claro, eu tinha que falar sobre o A*. O A* é um algoritmo de travessia e busca de caminho (pathfinding) usado em muitas áreas da ciência da computação, por sua completude, otimalidade e eficiência ótima. Assim como o algoritmo de Dijkstra, o A* é um algoritmo sofisticado usado para encontrar o caminho mais curto entre o ponto A e o ponto B. É, em linhas gerais, a mesma coisa, exceto que ele usa uma função heurística, dando prioridade a nós que aparentam ser "melhores" que os outros — ou seja, estimando o custo do nó atual até o destino em cada nó, priorizando nós que se acredita estarem mais próximos do objetivo, o que o torna mais eficiente. O algoritmo de Dijkstra não tem essa heurística.

## Fechamento

E existem muitos outros algoritmos que eu gostaria de discutir, como programação dinâmica (usando a sequência de Fibonacci ou o problema da mochila — dynamic programming, a propósito, é basicamente quebrar problemas em subproblemas menores), algoritmos de hashing para mapear dados de qualquer tamanho para dados de tamanho fixo de forma eficiente (esse é divertido), e muitos outros. Se você quiser ver mais conteúdo assim, me avisa — eu adoro esse assunto, eu só faria vídeo sobre isso se pudesse.

Se você curtiu, se inscreve, deixa um comentário e ativa o sininho pra saber quando eu subir o próximo vídeo sobre algoritmos. Eu sou o Forrest, até a próxima.
