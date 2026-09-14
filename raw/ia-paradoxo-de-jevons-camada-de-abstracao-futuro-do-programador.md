# IA, Paradoxo de Jevons e o Futuro da Profissão de Programador

Transcrição de vídeo/monólogo sem roteiro (autor não identificado no texto fornecido), em português. Colada diretamente pelo usuário no prompt, sem arquivo de origem preexistente em `raw/`. Sem tradução necessária.

---

E aí galera, beleza? Vamos falar sobre o assunto aqui do momento, que é IA. A gente não pode negar que é uma das maiores revoluções da história da computação. E hoje eu não quero falar muito sobre esse assunto mais do ponto de vista prático — eu tenho usado muito, já posso dizer que quase não tenho olhado mais pro código, e tenho usado muito o Cursor, que é uma ideia espetacular que eu tenho gostado muito, e mais recentemente também tô testando o Open Code com Open Router, com modelos abertos, para ficar um pouco mais barato, né. E também tenho usado várias skills no Cursor, que no caso são Cursor Rules, são regras, e posso falar mais sobre isso mais para frente. Mas hoje eu queria focar mais na questão econômica mesmo, do impacto da IA na nossa profissão de programadores, de desenvolvedores de software, de fato, né.

A gente pode dizer que é uma das coisas mais revolucionárias que aconteceram na história da tecnologia, na história da computação. Mas, de certa maneira, apesar de ser revolucionária, ela encaixa na história da computação — a história da computação é uma história de camadas de abstração sobre camadas de abstração. A gente começou com o hardware, e depois com linguagem de máquina escrita em binário, e depois a gente teve linguagem de montagem, assembly, que são apenas mnemônicos mesmo, que facilitam muito mais o uso do que usar binário. E depois, com o advento então do compilador, a gente começou a ter linguagens de alto nível, né, que começaram com Cobol, Fortran, e que hoje em dia, para nós, seriam linguagens de baixo nível — mas comparado com assembly são linguagens de alto nível, porque o código que você escreve já era muito mais próximo da linguagem natural comparado com binário e com assembly.

## O Paralelo com o Advento do Compilador

Um paralelo bem interessante que a gente pode fazer hoje é com o advento do compilador, porque, de fato, quando houve essa ideia de você escrever o código com uma linguagem mais próxima da linguagem natural, houve uma certa resistência. O pessoal mais "raiz", que desenvolvia usando assembly, torceram um pouco o nariz e, de fato, acharam que não era possível a gente escrever código de uma maneira mais próxima da linguagem natural, e achavam que o compilador, na verdade, ia atrapalhar — o código que era gerado pelo compilador, claro, ele traduzia o código de um programa usando linguagem de alto nível para o código binário de máquina que vai rodar na máquina, então, de certa maneira, ele tá gerando código, e uma das críticas é que esse código não era o mais otimizado possível, comparado com o código que seria gerado por um programador assembly.

Inclusive, uma curiosidade: eu tava vendo uma palestra do Kent Beck, e ele falou exatamente sobre isso — ele falou que o pai dele era um programador assembly, e quando apareceu o C, ele ficou um pouco assustado, porque a habilidade que ele tinha de programação em assembly — você tem que ficar alocando registradores, tem que saber do layout da memória — e aí, quando apareceu o C, ele teve que, de certa maneira, migrar, porque as habilidades que ele tinha perderam valor econômico.

Então a gente consegue até fazer um paralelo com hoje: de fato, a gente tá tendo uma crise de identidade, que o trabalho que a gente fazia há um ano perdeu o valor econômico, porque agora o código é gerado por IA. Então aquela habilidade de escrever código, de pensar em cada linha de código, de pensar no design mais baixo nível do código, foi embora — a gente não precisa mais dessa habilidade, porque as LLMs escrevem código muitas vezes melhor do que o código que a gente escreveria.

Então existe um paralelo entre o que houve quando a gente começou com os compiladores, que davam a possibilidade da gente escrever um código mais próximo da linguagem natural e o compilador traduzia esse código em linguagem de máquina, com o que a gente tá fazendo com IA hoje — que é uma camada de abstração acima das linguagens de programação de alto nível, porque agora a gente descreve o que a gente quer usando linguagem natural, e a IA produz o código em linguagem de alto nível, automatizando boa parte do trabalho de implementação.

A Jean Sammet, programadora e uma das pioneiras em linguagens de programação, relata sobre essa resistência dos programadores quando a gente começou a escrever código usando linguagens de alto nível. E a própria Grace Hopper também, quando ela propôs a ideia do compilador, ela também sentiu essa resistência dos programadores "raiz".

Então a gente consegue fazer um paralelo entre essa camada de abstração que veio com as linguagens de programação de alto nível e o que está acontecendo hoje, que a gente consegue descrever os programas usando linguagem natural, e existe uma coisa abaixo que traduz essa coisa de mais alto nível para uma coisa de mais baixo nível. Ou seja, a gente adicionou uma outra camada de abstração: a gente descreve o programa em linguagem natural, a LLM transforma isso em código com linguagem de alto nível, e aí sim isso é compilado, e assim por diante — a gente vai baixando o nível até chegar na máquina.

## A Analogia Não É Perfeita: Natureza Estocástica da LLM

É claro que a analogia ela encaixa aqui, mas ela não é perfeita, porque as LLMs são estocásticas — ou seja, existe uma probabilidade que ocorre ali para escolher o próximo token. Essa probabilidade e essa natureza estocástica da LLM faz com que o código que é gerado não seja determinístico. Você escreve o mesmo prompt duas vezes, o código vai ser gerado de forma totalmente diferente, por conta dessa aleatoriedade que é inserida.

Basicamente, o mecanismo é bem simples: você tem um conjunto de tokens que é o contexto — são palavras, a gente pode entender assim — e ela tenta prever qual é a próxima palavra, o próximo token. Para fazer isso, ela tem esse modelo que foi treinado em código e também em texto, e aí ela consegue prever qual é o próximo token. Na verdade, para isso, como teria mais de uma possibilidade de palavra que vem depois de um conjunto de palavras — por exemplo, "meu nome é", talvez com maior frequência apareceu no treinamento a palavra "José", mas a palavra "João" também tem certa possibilidade de aparecer — então existe uma distribuição ali de possibilidade para cada token, e aí é como se fosse jogado um dado para escolher qual vai ser o próximo token. Então, com isso, existe uma certa aleatoriedade que faz com que a resposta da LLM não seja determinística.

Mas a gente pode fazer essa analogia no sentido de ser uma camada de abstração a mais, e também no sentido de ter provocado resistência na comunidade de desenvolvimento.

## A Pergunta Que Incomoda: A IA Vai Acabar com os Empregos de Tecnologia?

Agora vamos pra pergunta que incomoda, que é: será que a IA vai acabar com os empregos de tecnologia, ou acabar com a profissão de programador? Então a resposta é: talvez. A gente não sabe exatamente o que vai acontecer, as coisas estão mudando muito rápido hoje. Saiu o Astra, lá da OpenAI, e é muito impressionante essa ideia de você usar o modelo para controlar o seu computador — achei bem interessante isso daí, imagino que já havia coisa parecida, por exemplo, com a ideia do Open Claw, etc, mas, de fato, é muito impressionante a evolução dos modelos. A chave virou mais ou menos em dezembro do ano passado, que a gente começou a ter um modelo que, de fato, gerava código que era tão bom quanto ou até melhor do que o que a gente escreve.

Então tá muito difícil prever o que vai acontecer, mas eu queria trazer aqui algumas ideias de economia que o pessoal tem conversado — acho que vocês já ouviram um pouco sobre isso — mas que ajuda a gente a entender o impacto real da IA na nossa área de desenvolvimento de software.

## Paradoxo de Jevons

Acho que vocês já ouviram falar no Paradoxo de Jevons. Não é um paradoxo per se, é mais uma observação contraintuitiva que esse inglês, William Jevons, percebeu num livro que ele escreveu sobre o consumo de carvão em 1865, chamado "The Coal Question". É bem interessante que ele observou — ele estava estudando as máquinas a vapor, e as primeiras máquinas a vapor não eram muito otimizadas, então, para você conseguir, por exemplo, que um trem a vapor andasse 1 km, você gastava muito carvão. E eles conseguiram construir máquinas a vapor mais otimizadas, que gastavam muito menos carvão para andar esse mesmo quilômetro.

E aí a expectativa é que, claro, você tá gastando menos carvão para andar o mesmo tanto, então o consumo de carvão vai cair. E aconteceu exatamente o contrário: como barateou, como a máquina ficou mais otimizada, então apareceram mais aplicações pra máquina, e mais trens foram colocados para rodar. Então, na verdade, aumentou o consumo, em vez de diminuir.

Claro, IA não pode ser comparada com carvão como um mesmo tipo de recurso, mas essa mesma ideia econômica — de você baratear um recurso e isso fazer com que, na verdade, você acabe gastando mais desse recurso — ela se aplica a outras coisas mais parecidas com tecnologia, mais parecidas com IA.

### Radiologia (Geoffrey Hinton)

Outro exemplo contraintuitivo desses aconteceu também na história, mais recentemente. Por exemplo, o Geoffrey Hinton, que é um dos papas da área de IA e, em particular, da área de deep learning, ele previu em 2016 que a profissão de radiologia — que é análise de imagens médicas — era uma profissão que ia acabar, por conta da melhoria da IA para fazer esse tipo de análise. E, na verdade, aconteceu o contrário: cresceu o número de radiologistas, por conta de baratear — uma parte dessa profissão foi automatizada, o que não quer dizer que toda a profissão foi automatizada e que não precisa mais de radiologista. Na verdade, como barateou, por exemplo, outras aplicações de análise de imagem médica ficaram mais baratas, então um hospital que não fazia esse tipo de análise passou a fazer. Então o que acontece é que aumenta o número de aplicações, então você precisa de mais gente — ou seja, isso gera mais demanda.

### Caixas Eletrônicos (ATM)

Outro exemplo bem significativo é o das ATMs, das Automated Teller Machines, ou caixa eletrônico, que, de fato, quando saiu o caixa eletrônico, pensava-se que ia diminuir o número de caixas humanos, porque a máquina ia fazer tudo. E, na verdade, também aconteceu o contrário: com o fato de você ter caixas eletrônicos, ficou mais barato abrir uma agência, então, com mais agências, precisa de mais gente, e inclusive caixas humanos — então, na verdade, aumentou o número de tellers, número de caixas, que eram necessários para trabalhar nessas agências novas.

Então uma tecnologia que automatizou muito o trabalho de caixa acabou aumentando a necessidade de caixas humanos, para fazer, talvez, outros tipos de atividades que não foram automatizadas.

### James Bessen

O James Bessen estudou esse fenômeno, e ele falou isso: que a automação não simplesmente eliminou a profissão, mas ela mudou a economia da atividade. Então a ideia é que o fato de você aumentar a produtividade não quer dizer que você vai ter menos emprego — pode acontecer, na verdade, o contrário, porque, como fica mais barato, acaba mudando a atividade economicamente, você precisa de mais gente.

### A Nuance: Nem Sempre Funciona Assim

Claro, tem uma nuance aqui: não quer dizer que, necessariamente, uma tecnologia nova que barateia uma atividade leva a mais demanda por profissionais dessa área. Aconteceu também na história um tipo de mecanização ou automação que, na verdade, diminuiu e enxugou o mercado — em particular, na revolução industrial, quando houve a mecanização do campo. Isso, de fato, causou um grande estrago e afetou muito os trabalhadores do campo.

Mas a minha expectativa é que, de fato, a IA não vai diminuir ou acabar com a profissão de tecnologia, de desenvolvedor de software — na verdade, eu acho que ela vai precisar de mais gente. O DHH foi recentemente no Lex Fridman, e ele fala sobre isso, e foi lá que eu vi essa história do caixa eletrônico, que eu achei muito significativo, e me parece um caso análogo.

## A Crise de Identidade e o Lado Bom

E aí, é claro, pessoal, a gente não pode negar que houve uma mudança muito drástica na nossa atividade. De certa maneira, a gente tá com uma crise de identidade, em particular quem se identificava com a atividade de escrever código, porque, de fato, a gente vai parar de escrever código, a não ser em situações muito excepcionais. Então muita gente tá, de certa forma, de luto, e eu também me incomodei um pouco com essa questão, porque, de fato, impactou muito a maneira da gente trabalhar.

Por outro lado, existe um lado muito bom disso: que facilitou muito a gente construir coisas. Então, se você gosta de construir coisas, na verdade, a IA nos empolga muito mais. E isso aconteceu, por exemplo, com o DHH, que acabou construindo uma distribuição do Linux, que é o Omakub, e ele disse que nunca teve tanto prazer em desenvolver software, né, em trabalhar com computadores.

Uma coisa parecida aconteceu com o Kent Beck — aliás, o Kent Beck também fez um tweet que ficou muito famoso, em que ele falou isso: "O valor econômico de 90% das minhas habilidades praticamente despencou. Já os 10% restantes ficaram 1000 vezes mais valiosos."

## O Que Continua Valendo: Princípios, Julgamento e Qualidades Humanas

Então a gente percebe isso: que conhecimento de princípios de desenvolvimento de software, de engenharia de software, de ciência da computação — que são aqueles princípios que eu sempre prezei, preguei aqui no canal — eles continuam sendo importantes. Conhecimento de arquitetura de software, de infraestrutura, de boas práticas de engenharia de software, porque, afinal de contas, a gente tá guiando a LLM, e as LLMs acabam sendo multiplicadoras: se você sabe muito de engenharia de software, você, de fato, fica muitas vezes mais produtivo. E o contrário também ocorre: quem sabe pouco ou tem ideias erradas, na verdade, a IA multiplica a bagunça.

Então é isso — eu acho que a gente não tem motivo para ficar pessimista, a gente tem motivo para ficar otimista, sendo realistas, né, pensando que, de fato, existe uma alteração muito forte que tá acontecendo no nosso mercado, na indústria de desenvolvimento de software — acredito que em todas as indústrias, na verdade — mas me parece que o futuro ainda é muito promissor para tecnologia.

Eu acho que ficou valendo mais ainda essas qualidades: por exemplo, a habilidade de comunicação, e essas virtudes tão importantes, que são a constância, a resiliência, a força de vontade — tudo isso ainda vai impactar muito, e vai impactar mais, eu acho, porque o conhecimento técnico de programação em si, isso, como o Kent Beck falou, perdeu o valor. Mas essas outras coisas — conhecimento de mais alto nível de gerir software, desenvolvimento de software, de tecnologia em geral, e habilidades e qualidades humanas — na verdade, aumentaram de valor.

## Conclusão

Então é isso, né — eu te convido a se aprofundar mais nesses assuntos, no Paradoxo de Jevons, em vários pontos na história em que isso ocorreu, de você diminuir o custo de um recurso e, na verdade, isso fazer com que esse recurso fosse mais utilizado. Eu acho que isso vai acontecer com IA, porque muitas ideias que custavam muito caro agora custam mais barato — isso quer dizer que mais pessoas vão construir software, e quanto mais software a gente constrói, mais pessoas a gente vai precisar para manter esse software.

Então, como eu disse, eu acho que o futuro é promissor. Espero que vocês tenham curtido, fiquem com Deus, e até o próximo vídeo.
