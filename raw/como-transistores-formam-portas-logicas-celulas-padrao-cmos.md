# Como Transistores Formam Portas Lógicas (Células Padrão CMOS) — Branch Education

Dentro do seu computador existem dezenas de microchips com dezenas de bilhões de transistores. Você talvez saiba que esses transistores são a base de toda a tecnologia, são fabricados em fábricas que custam bilhões de dólares e têm apenas alguns nanômetros de tamanho. Mas o que você talvez não saiba é que essa rede de bilhões de transistores é, na verdade, organizada de forma muito parecida com blocos de Lego conectados juntos para montar um conjunto de Lego, como a Millennium Falcon de 7.541 peças.

Neste vídeo vamos explorar como os transistores dentro do seu computador são como blocos de Lego: como os transistores realmente são e como eles funcionam, lógica básica, e finalmente como 26 bilhões de transistores são organizados nas diferentes seções de um processador.

## Blocos de Lego e transistores: a analogia

Nessa analogia, vamos comparar um transistor a um único pino de um bloco de Lego. Sozinhos, nenhum dos dois faz muita coisa. No entanto, quando alguns transistores são conectados, eles formam uma **célula padrão** (standard cell), que é o bloco de construção fundamental de todo processador e GPU. Da mesma forma, vários pinos formam uma peça de Lego, que é o bloco de construção para todas as criações de Lego.

Por exemplo: dois transistores conectados juntos formam uma célula padrão inversora; quatro transistores conectados juntos formam uma porta NAND; e seis transistores formam uma porta OR. Há várias outras células padrão feitas ao conectar transistores, e da mesma forma existe uma grande variedade de peças de Lego com diferentes números de pinos e formatos.

## O inversor: a célula padrão mais simples

Antes de explorar células padrão mais complexas, primeiro é preciso entender como funciona uma das mais simples: o **inversor**, análogo a um bloco de Lego 1x2. Sua função é simplesmente receber uma entrada 1 e fornecer uma saída 0, ou vice-versa.

Essencialmente, células padrão como o inversor são a estrutura física real de uma porta lógica — é isso que se veria ao abrir e dar zoom em uma visão nanoscópica do processador de um smartphone.

Na parte inferior da célula padrão há dois transistores construídos sobre uma base de silício. Dentro de um transistor há três partes principais:

- **A porta (gate)**
- **O canal**
- **O dielétrico** — uma barreira que separa os dois e impede que a eletricidade passe

Além disso, em cada lado do canal e acima da porta há contatos metálicos conectados a vias verticais, usadas para entrada e saída de eletricidade para as partes correspondentes.

### Como o transistor funciona

Quando 1 V é aplicado à porta, a eletricidade consegue fluir pelo canal, conectando um lado do canal ao outro. Quando 0 V é aplicado à porta, a eletricidade não consegue fluir, resultando no isolamento elétrico dos dois lados do canal.

Analogia: pensar no canal e na porta como uma torneira de água com uma alavanca. Quando a alavanca é aberta, a água pode fluir; quando é fechada, a água para.

Esse transistor é chamado **FinFET tipo N** (devido ao seu formato semelhante a uma barbatana/"fin"). Quando 1 V é aplicado à porta, a eletricidade pode fluir através do canal.

Um segundo transistor, com o mesmo formato FinFET, funciona de maneira oposta — é o **transistor tipo P**: quando 1 V é aplicado ao gate, a eletricidade *não pode* fluir pelo canal; quando 0 V é aplicado, a eletricidade *pode* fluir. Usando a analogia da torneira: é como uma torneira defeituosa, onde a alavanca para baixo liga a água, e para desligar é preciso levantar a alavanca ativamente. O círculo no símbolo do gate do tipo P indica essa funcionalidade invertida.

### Combinando tipo N e tipo P

Ao conectar o gate dos dois transistores (N e P) em um único contato compartilhado, uma única tensão de entrada (1 V ou 0 V) controla ambos. Como os tipos N e P são opostos:

- Quando **0 V** é aplicado ao gate: o tipo P liga (conduz), o tipo N desliga.
- Quando **1 V** é aplicado ao gate: os dois trocam de estado — o tipo N liga, o tipo P desliga.

Em seguida, trazem-se os trilhos de energia e terra acima dos transistores: o trilho de energia fica em 1 V, o de terra em 0 V, e permanecem sempre nesses valores. Adicionam-se fios usando os pontos de contato, construindo vias verticais que conectam ambos os lados do transistor junto aos trilhos de energia — uma camada de fios chamada **interconexões locais**. Trilhos, vias e interconexões são fios de metais condutores (cobre, tungstênio ou alumínio) que conduzem eletricidade por caminhos intrincados.

A **entrada** é o fio que se conecta ao gate compartilhado; a **saída** se conecta ao fio de interconexão local ligado a um lado de cada um dos dois transistores.

### O que acontece com cada entrada

- **Entrada = 1 V**: o gate compartilhado liga o tipo N e desliga o tipo P. Com o tipo N ligado, a eletricidade flui: 0 V do trilho de terra viaja pelas interconexões locais, desce por uma via vertical, passa pelo canal do FinFET tipo N, sobe novamente por outra via, atravessa outra seção de interconexões locais e chega à saída. **Resultado: entrada 1 V → saída 0 V.** Ao mesmo tempo, o tipo P (controlado pela mesma entrada) está desligado, então essa seção do fio fica isolada.
- **Entrada = 0 V**: o oposto acontece — o tipo P liga, o barramento de 1 V é conectado através dos fios de interconexão local e vias, passa pelo canal do tipo P e sobe até a saída. **Resultado: entrada 0 V → saída 1 V.** O tipo N fica desligado e essa seção fica isolada.

Todos os espaços vazios entre os fios (que parecem estruturas tridimensionais flutuantes) são, na verdade, preenchidos com um material isolante chamado **dielétrico**.

Entender bem a função básica do inversor é fundamental para compreender células mais complicadas, como as portas NAND, OR e XOR.

## Detalhamento eletrônico do inversor

- **Símbolo e tabela lógica**: entrada 1 → saída 0, e vice-versa.
- **Esquema**: barramento de alimentação (1 V) acima, barramento de terra (0 V) abaixo; dois transistores simplificados — o de baixo do tipo N, o de cima do tipo P.
- As entradas dos dois gates estão conectadas juntas (na prática, costuma-se separá-las e rotular com o mesmo nome de entrada).
- A saída é posicionada no meio dos dois transistores.
- Quando 1 V é aplicado à entrada A, a saída é conectada ao trilho de aterramento (0 V). Quando 0 V é aplicado, a saída é conectada ao trilho de alimentação (1 V).

## Células padrão como blocos de Lego (continuação da analogia)

Existe uma grande variedade de células padrão construídas conectando diferentes quantidades de transistores usando as interconexões locais — assim como existe uma grande variedade de peças de Lego construídas conectando diferentes quantidades de pinos em várias configurações.

Se um pino de Lego é um transistor individual, e os blocos/peças de Lego são células padrão, o equivalente a um **conjunto de Lego** é uma **célula macro**. Por exemplo: 350 peças de Lego montam um Star Fighter; da mesma forma, aproximadamente **160 células padrão** conectadas formam uma célula macro capaz de somar dois números. Para conectar cada uma dessas 160 células padrão, usa-se uma camada superior de vias e fios verticais chamada **metal 1 (M1)**.

Ao dar zoom, encontram-se as células padrão individuais encaixadas entre várias fileiras dos trilhos de energia (1 V) e aterramento (0 V). Esse circuito usa uns e zeros binários: os números de entrada a serem somados são enviados usando 1 V ou 0 V em dois conjuntos de 32 fios, e a saída binária é transmitida por 33 fios.

Assim como existem milhares de conjuntos diferentes de Lego, há uma grande variedade de células macro diferentes, algumas contendo milhares de células padrão. Por exemplo, uma célula macro de **multiplicação de 32 bits** é construída a partir de **6.100 células padrão** — complexidade comparável ao conjunto LEGO Millennium Falcon, com cerca de 7.500 peças.

Células macro também são chamadas de módulos, blocos funcionais, unidades funcionais, ou simplesmente blocos/unidades.

### Hierarquia completa

Várias células macro são combinadas em um **núcleo IP**; vários núcleos IP são combinados em um **núcleo (core)** ou acelerador de hardware; esses elementos são combinados em um **chip completo** (processador), que fica dentro do encapsulamento montado na placa-mãe. Processadores modernos têm dezenas de bilhões de transistores.

Um transistor individual, ou uma célula padrão/porta lógica básica isolada, não é tão útil sozinha — mas quando dezenas de milhares de cientistas e engenheiros montam meticulosamente bilhões de células padrão e portas lógicas juntas (um "conjunto de Lego com bilhões de peças"), o resultado é um circuito integrado capaz de navegar na internet, reproduzir vídeos ou rodar jogos com gráficos avançados.

Processadores atuais usam cerca de **17 camadas metálicas** de fios conectados entre si para formar macrocélulas, núcleos IP, núcleos e outras seções do processador. No fundo, CPUs são apenas transistores e portas lógicas conectados usando quilômetros de fios.

## Portas lógicas mais complexas

### Porta NAND

Executa a lógica de AND seguida de NOT. Na analogia do Lego, seria equivalente a um bloco 2x2. Construída com **quatro transistores**: dois do tipo P em paralelo acima, dois do tipo N em série abaixo. As duas entradas são conectadas a um dos terminais de cada porta dos transistores; a saída fica no meio dos canais.

- Para a saída ser **0**, ambas as entradas precisam ser **1** (ligando ambos os N-type, criando caminho do trilho de terra até a saída).
- Para a saída ser **1**, é necessário que um ou ambos os transistores P-type estejam ligados (criando caminho do trilho de energia até a saída).

Detalhamento físico:
- Os dois transistores tipo P estão em **paralelo**: um lado de cada um conectado ao trilho de energia, saída conectada no meio. Quando um ou ambos ligam (o que ocorre quando 0 é aplicado a qualquer entrada), o trilho de 1 V se conecta à saída. Entrada (0,0), (0,1) ou (1,0) resulta em saída 1.
- Os dois transistores tipo N estão em **série**: trilho de terra conectado a um lado de ambos, saída no lado oposto. Para que 0 V passe, **ambos** precisam estar ligados — o que ocorre quando ambas as entradas são 1. Entrada (1,1) resulta em saída 0.

Observação: em macrocélulas (como a de adição), os trilhos de energia e terra são alternados entre células padrão vizinhas — metade tem energia acima e terra abaixo, a outra metade o inverso. Para acomodar isso, a célula padrão é fisicamente invertida (P embaixo, N em cima), mas funciona da mesma forma.

### Porta AND

Combinação de uma porta NAND com um inversor acoplado na saída. Quando as duas entradas são 1, a saída (após NAND + inversão) também é 1; se uma ou ambas as entradas forem 0, a saída é 0.

### Portas NOR e OR

Usam configuração muito semelhante à NAND: uma porta **NOR** é como uma NAND, mas com dois transistores tipo P em **série** e os do tipo N em **paralelo** (inversão da topologia NAND). Uma porta **OR** é uma NOR com um inversor adicionado na saída.

### Portas XOR e XNOR

Mais complicadas — exigem um total de **10 transistores** cada, pois a lógica precisa considerar apenas uma das entradas ativada (não ambas, nem nenhuma). A porta XNOR é semelhante à XOR, apenas com os transistores tipo N e tipo P em série/paralelo invertidos entre si.

Pergunta em aberto levantada no próprio vídeo: como construir uma porta AND com três entradas, ou uma porta OR exclusivo (XOR) com quatro entradas?

## CMOS e observações técnicas finais

1. **CMOS**: esse tipo de circuito é chamado de **semicondutor de óxido metálico complementar (Complementary Metal-Oxide-Semiconductor)**, devido aos dois tipos de transistores (N e P) que funcionam de forma oposta. Circuitos CMOS têm alta tolerância a ruído e baixo consumo de energia, porque um dos pares de transistores está sempre desligado e, se projetados corretamente, nunca há um caminho direto entre o trilho de 1 V e o trilho de terra.

2. **Velocidade física real**: embora a explicação de como um inversor funciona leve minutos, fisicamente a operação leva apenas alguns **picossegundos** (10⁻¹² segundos) entre a mudança de entrada e a mudança correspondente na saída. Cada célula padrão leva alguns picossegundos para completar sua lógica; a célula macro de multiplicação (6.000+ células padrão) leva cerca de **150 a 200 picossegundos** entre a entrada chegar e todas as células completarem sua lógica.

3. **Complexidade real dos transistores**: a maioria dos FinFETs é construída a partir de múltiplas "barbatanas" (fins) para melhorar as características elétricas. Nos circuitos CMOS, os transistores tipo P ficam em cima e os tipo N embaixo (fisicamente).

4. **Crédito**: agradecimento a Mat Venn, do canal "Zero to ASIC Course", por ajudar a obter os layouts precisos de células padrão usados no vídeo. Ele também administra o serviço **Tiny Tapeout**, que permite fabricar um circuito integrado próprio.

## Nota sobre produção do vídeo

O criador (canal Branch Education) menciona que este roteiro passou por quase 54 revisões e, em seis ocasiões, trechos inteiros foram descartados e o roteiro foi reestruturado — inicialmente o vídeo tentava também explicar como portas lógicas realizam operações matemáticas (multiplicação), mas essa parte foi movida para um vídeo separado, focando este vídeo apenas no design de células padrão.

---

*Fonte: transcrição de vídeo do canal Branch Education (YouTube), sobre design de transistores, células padrão e portas lógicas em circuitos CMOS. Conteúdo já em português brasileiro, sem necessidade de tradução.*
