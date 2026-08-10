# Os Conceitos que Regem a Computação: Bits, Máquina de Turing e Complexidade

> Transcrição adaptada de vídeo. Limpeza de pontuação e correção de erros de transcrição automática (ex: "touring" → Turing, "bte" → byte, "shore" → XOR, "do na 100" → 2^100). Conteúdo técnico preservado. Segmento patrocinado (plataforma Brilliant) omitido por não ser conteúdo técnico.

A computação, assim como todas as outras áreas do conhecimento, é regida por conceitos fundamentais. Esses conceitos formam a base na qual se erguem as tecnologias e as linguagens de programação que dominam o cenário atual da tecnologia. Por exemplo, os algoritmos de criptografia utilizados pelos tokens JWT são construídos a partir desses conceitos, assim como os componentes do React. Para nos tornarmos profissionais mais completos e entendermos o panorama como um todo, é fundamental entender esses conceitos que formam a computação.

---

## Bits e Bytes

O sistema binário é o sistema utilizado para representar todas as informações dentro da computação, e por isso é de suma importância entender o que é esse sistema e como ele funciona.

**Bit** é a menor unidade de informação dentro da computação, e pode ter um valor de um ou zero — ligado ou desligado. O termo *bit* é uma abreviação de *binary digit* (dígito binário). O uso de apenas dois estados (zero ou um) simplifica o design dos componentes e dos circuitos eletrônicos. No hardware, esses dois estados podem ser representados por componentes eletrônicos de forma confiável, como por exemplo usando transistores: o estado ligado representa o número um e o desligado representa o número zero.

**Byte**, por outro lado, é a unidade de informação composta por 8 bits. Os bytes são usados para representar uma informação completa ou parte dela — por exemplo, caracteres como letras e números. A letra "A" pode ser representada por um byte específico em binário.

O que precisamos ter em mente é que os computadores usam apenas bits e bytes para representar todas as informações. Por exemplo, um documento de texto é armazenado no formato binário, onde cada byte representa uma letra; um conjunto de bytes pode representar uma palavra; e um conjunto desses conjuntos de bytes representa as frases dentro do documento.

O sistema binário também é muito eficiente para realizar o processamento desses dados. A lógica binária permite que os computadores realizem operações complexas de forma simples e rápida, porque, usando os operadores lógicos (como **AND**, **OR** e **XOR**), o computador consegue fazer operações em cima dos bytes para obter resultados. Assim, é possível representar uma soma somente com essas operações lógicas.

---

## A Máquina de Turing

Agora que entendemos como um computador pode compreender e armazenar informações através de zeros e uns, vamos entender a concepção primordial do que é um computador.

A **máquina de Turing** é um conceito teórico desenvolvido pelo matemático britânico Alan Turing em 1936. Essa máquina é considerada um dos modelos fundamentais para a teoria da computação e é frequentemente utilizada para saber o que pode ser computado ou não, e como isso pode ser computado.

Podemos imaginar a máquina de Turing como uma fita infinita dividida em células. Cada célula é capaz de armazenar um símbolo de um conjunto finito de símbolos (por exemplo, um zero ou um um). Além disso, há uma cabeça que passa sobre essa fita, com o poder de escrever uma informação numa célula ou ler o símbolo escrito naquela célula. Essa cabeça pode se mover ao longo da fita, tanto para a esquerda quanto para a direita, movendo-se para as células adjacentes.

O funcionamento da máquina é regido por um conjunto finito de regras chamado **tabela de transição**. A tabela de transição diz à máquina o que ela deve fazer de acordo com o símbolo lido na fita e o estado atual em que a máquina se encontra. Por exemplo: "se ler o valor zero, escreva o valor um e vá para a célula da direita"; ou "se ler o valor um, não faça nada e volte para a célula da esquerda". Essas regras determinam o novo símbolo a ser escrito, a direção para a qual a máquina deve se movimentar e o novo estado da máquina.

A beleza da máquina de Turing está na sua simplicidade e no poder que esse conceito teórico tem. Apesar de ser um modelo teórico simples, ela consegue representar qualquer algoritmo computacional — ou seja, tudo que pode ser computado num computador moderno hoje também pode ser computado numa máquina de Turing. Claro que teríamos uma tabela enorme com todas as possibilidades de transição e estados, além de uma fita gigante contendo todas as informações necessárias, mas não deixa de ser possível. Não existe nenhuma outra definição de computador mais completa que a máquina de Turing; apesar de simples, ela representa tudo que um computador consegue computar e é válida até hoje.

---

## Determinismo e Não-Determinismo

Agora entramos em conceitos que regem a complexidade dos algoritmos até hoje: o determinismo e o não-determinismo.

Uma **máquina de Turing determinística** é aquela na qual, para cada estado da máquina e para cada símbolo lido pela cabeça de leitura e escrita, existe no máximo uma ação possível. Em outras palavras, a tabela de transição possui uma única regra para cada combinação de estado e símbolo lido. O comportamento da máquina é totalmente previsível e determinístico: com a mesma entrada, sempre teremos a mesma saída.

Por outro lado, a **máquina de Turing não-determinística** é uma generalização do modelo determinístico, onde para cada estado e cada símbolo lido pode haver várias ações possíveis. A tabela de transição pode ter várias regras para a mesma combinação de estado e símbolo. Num modelo não-determinístico, a máquina pode escolher entre todas as transições disponíveis e seguir caminhos diferentes; se pelo menos um desses caminhos levar a um estado de aceitação, a máquina retorna que aceita a entrada (ou seja, encontra um resultado).

Esses conceitos são importantes porque permitem explorar diferentes modelos de computação e entender os limites e capacidades da máquina de Turing — ou seja, dos algoritmos atuais. Algumas classes de problemas são solucionáveis por máquinas de Turing determinísticas (como as máquinas que temos hoje). Outras classes requerem o poder adicional do não-determinismo para serem solucionadas de maneira eficiente. Os nossos computadores de hoje não funcionam como máquinas de Turing não-determinísticas, mas já existem estudos sobre isso — por exemplo, os computadores quânticos.

Além disso, o estudo de máquinas de Turing não-determinísticas é fundamental para a teoria da complexidade computacional, especialmente na classificação entre diferentes classes de complexidade, porque existe uma certa classe de problemas que só seria solucionável em tempo razoável utilizando máquinas de Turing não-determinísticas.

---

## Complexidade Computacional

A complexidade computacional é algo inerente à profissão de programador. Podemos não enxergar essa complexidade, mas ela nos acompanha em todos os algoritmos que escrevemos ao longo da carreira. Existe uma certa classe de problemas que não conseguem ser solucionados por computadores em tempo viável, ou que exigiriam tanto recurso de máquina e memória que se torna inviável executá-los. Como programadores e solucionadores de problemas, precisamos reconhecer quando topamos com um problema desses e saber lidar com ele — por exemplo, utilizando uma solução razoável (não perfeita, mas suficiente para desenvolver o produto).

A complexidade computacional é uma área dentro da teoria da computação que estuda a eficiência dos algoritmos em termos de **tempo** e de **espaço** — porque ambos são medidas finitas (não temos tempo infinito nem memória infinita). Tempo é quanto o algoritmo leva para finalizar sua execução; espaço é quanta memória o algoritmo utiliza durante a execução.

### Notação Big O

Um dos conceitos mais importantes e populares dentro da complexidade computacional é a **notação Big O** (*Big O notation*). A notação Big O descreve o comportamento assintótico de uma função — uma forma de medir como a função que representa o tempo de execução de um algoritmo se comporta à medida que o tamanho da entrada tende ao infinito. É muito utilizada para representar a complexidade de tempo ou de espaço de um algoritmo.

Não podemos medir a complexidade de tempo em segundos, porque isso varia muito conforme a máquina, os processos em execução naquele momento e até condições externas. Precisamos de uma forma de medir a complexidade do algoritmo desconsiderando essas variáveis incontroláveis, levando em consideração apenas a complexidade do algoritmo em si — e é aí que entra a notação Big O.

**O(n²) — complexidade quadrática:** o tempo de execução cresce proporcionalmente ao quadrado do tamanho da entrada. Se a entrada é 1, leva 1 unidade de tempo; se a entrada é 100, leva 10.000 unidades; se a entrada é 1.000, leva 1.000.000 de unidades.

**O(n) — complexidade linear:** o tempo cresce proporcionalmente ao tamanho da entrada, de um para um. Entrada 1 → 1 unidade; entrada 100 → 100 unidades; entrada 1.000 → 1.000 unidades. Muito mais eficiente que O(n²).

**O(2ⁿ) — complexidade exponencial:** o tempo de execução dobra a cada aumento de uma unidade no tamanho da entrada. Entrada 1 → 2 unidades; entrada 10 → 1.024 unidades; entrada 100 → 2¹⁰⁰ unidades (um número tão grande que é praticamente incompreensível e inviável de ser aguardado por um ser humano).

### Complexidade e Criptografia

A partir do princípio dos algoritmos com complexidade exponencial é que os algoritmos de criptografia são cuidadosamente escolhidos para garantir a segurança dos dados. Para quebrar uma criptografia e obter as informações contidas naquele hash, seria necessário executar algoritmos de complexidade exponencial — praticamente inviáveis de executar nas máquinas que temos hoje.

Com uma chave criptográfica pequena, com poucos caracteres e um número reduzido de possibilidades, talvez fosse possível quebrar a criptografia em tempo razoável. Mas, à medida que aumentamos o tamanho da chave e adicionamos mais possibilidades (letras, números, caracteres especiais, maiúsculas e minúsculas), mais difícil fica quebrá-la, porque o tamanho da entrada do algoritmo cresce e, sendo a complexidade exponencial, o tempo de execução dispara.

Na prática, o tempo necessário para descriptografar os dados aumenta exponencialmente à medida que o tamanho da chave aumenta. Assim, mesmo com o avanço da tecnologia e dos recursos computacionais, torna-se praticamente impossível quebrar as criptografias atuais sem ter a chave utilizada para criptografar os dados.
