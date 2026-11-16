# Grids, parte 1: estrutura em colunas, Bootstrap, regra de oito pontos e responsividade

Opa, fala pessoal, vamos dar continuidade ao módulo de interface web, onde na aula de hoje nós vamos trabalhar os conceitos e aplicações de grids.

De antemão, eu já ressalto, já deixo aqui evidenciado a importância desse tópico, então não deixe de assistir às próximas aulas, porque elas estão assim completamente juntas com relação a esses conceitos, então muito do que eu falei em wireframes também se encaixa e você vai entender muito da disposição dos elementos depois de você estudar os grids, fora que ele ajuda demais os dois mundos que mais a gente está trabalhando, que é tanto a parte do designer, que vai precisar do alinhamento, da consistência, da organização dos elementos visuais, tanto na parte do desenvolvedor, que ele vai precisar depois conhecer um pouco mais sobre resoluções, breakpoints, distâncias, para conseguir a tão famigerada responsividade, para poder a gente ter interfaces que se adaptem a todo e qualquer tamanho de tela, todo e qualquer dispositivo.

Então, nessa primeira aula nós vamos trabalhar esses conceitos aqui, nas próximas aulas a gente vai aprofundar um pouco mais nos padrões que são utilizados hoje em dia, bem como informações mais técnicas e depois a gente vai implementar isso tanto no Figma, tanto no código, para poder exemplificar da melhor forma possível tudo que a gente está estudando, tudo que a gente está debatendo aqui.

## O que são grids

Primeira coisa, então, o que é? O que se trata dos grids? Então, os grids criam a estrutura básica, o esqueleto para o seu design, eles são colunas ou linhas, quando os elementos são colocados e alinhados.

Então, o grid, pessoal, nada mais é do que um padrão que foi criado para poder a gente conseguir os elementos fundamentais do design e, por exemplo, da responsividade. E quando eu estou falando de responsividade, quais são os pontos mais importantes? Eu conheci das resoluções, dos breakpoints, de eu ter distâncias padronizadas de forma que, se eu tenho um padrão, eu consigo adaptar ele em vários tamanhos de tela, ao passo que quais são os elementos importantes com relação ao design? É os elementos estarem alinhados, eles têm consistência de distância, é eles estarem e aparentarem organizados, porque isso traz uma sensação mais clean de limpeza, de apresentação dos elementos e tudo.

Então, os grids literalmente são colunas onde a gente organiza e ajuda tanto um mundo como o outro, tanto o mundo do design como o mundo do desenvolvimento.

Então, para poder não ficar só nas minhas palavras, eu vou mostrar alguns exemplos com base nos sites que eu já desenvolvi, por exemplo, na landing page do FrontPush. Se eu pegar a seção principal do meu site, se concentra nessa coluna grande que vai daqui até aqui, a gente percebe que esse bloco de conteúdo ocupa um determinado tamanho, enquanto esse bloco ocupa um outro tamanho, eles não são iguais, ao passo que aqui se repete da mesma forma, esse bloco é maior que esse.

Então, se eu for dividir, eu tenho aqui 12 colunas imaginárias, mais ou menos, esse aqui vai ocupar de sete a oito colunas, enquanto esse aqui vai ocupar de cinco a quatro colunas. E você percebe que todos são alinhados e seguem essa padronização.

E quando eu coloco, por exemplo, em modo de responsividade, eu vejo que a estrutura, quando ela parte para a estrutura de celular ou de tablet, você percebe que ele quebrou justamente naquele breakpoint e a gente começa a estudar os padrões para poder chegar aqui também e esse padrão também foi estabelecido na landing page aqui no design. Você percebe aqui, uma, duas, três, quatro, quatro colunas de cá e aqui oito colunas restantes de cá. Então, é esse tipo de estudo que a gente vai ter nas próximas aulas para a gente entender esses padrões.

Então, eles ajudam no alinhamento, na consistência do seu design, organizando aqueles elementos da interface que a gente conversou lá nos primeiros módulos que a gente, inclusive, tem um módulo só para poder tratar disso.

## Padrões: Bootstrap e regra de oito pontos

Como eu disse para vocês, os grids são padrões. Os dois mais utilizados, pessoal, é o Bootstrap, e a regra de oito pontos, com certeza eu já falei desses dois aqui para vocês, mesmo que de maneira indireta, eu já citei, vocês já viram essas imagens aqui.

Então, esse aqui é o Bootstrap Grid System, onde ele estabelece grids em colunas para diferentes tipos de dispositivos e estabelece padrões de width, de comprimento para poder a gente conseguir essa padronização. E a regra dos oito pontos, que também é utilizada demais em sistemas de apps, tanto o Android como o iOS, eles gostam muito desse sisteminha aqui também.

Então, os dois meio que se complementam e são os dois mais utilizados hoje em dia, mas não se estranhe se você ver outros grids, mas que seguem essa mesma linha, esse mesmo conceito de criar essa estrutura básica, esse esqueleto para o nosso design. Então, vai ter variações, mas nós vamos trabalhar esses dois aqui como principal.

## Responsividade: fixo, fluido, adaptativo e responsivo

Um tópico que eu quero falar com vocês é sobre responsividade, porque com os grids a gente consegue conhecer mais sobre resoluções e breakpoints. A gente vai entender um pouco mais sobre esses conceitos.

[...] quando a gente está construindo elas, que é do tipo fixa, do tipo fluida, do tipo adaptativo e do tipo responsivo. Vou explicar para vocês a diferença entre eles.

### Fixo

Primeira coisa, o fixo é pouquíssimo comum hoje em dia, ele é mais voltado, por exemplo, para empresas, quando eu compro um determinado dispositivo na minha empresa e vai ser ele utilizado por vários e vários anos. Vamos supor que eu compro um iPad e eu vou para o meu time de desenvolvimento e o meu pessoal só vai usar o iPad para poder controlar tudo aqui dentro e você vai fazer um layout fixo para o iPad, porque é para uma tela só.

Então, vamos supor que você tenha um iPad para poder fazer o atendimento de uma pizzaria e fala assim, vai ser esse aqui durante muito tempo, eu comprei vários iPads e eu quero só um sistema para poder ficar mais barato. Não quero responsivo, porque a gente só vai utilizar um dispositivo e está tudo certo. E ele é projetado de maneira fixa e essa conversa aqui quanto à responsividade não faz tanto sentido.

Agora, a gente vai ver os três que são mais utilizados hoje em dia, o fluido, o adaptativo e o responsivo. Vamos entender.

### Fluido

Primeira coisa, a gente vai entender o que é fluido. O fluido, pessoal, eu vou dar exemplo aqui na prática com vocês. Presta atenção no tamanho do elemento. Está vendo aqui a minha logo? Ela está no tamanho. Agora, quando eu vou diminuindo, você vai perceber que quando chegar em determinada resolução, a minha imagem vai diminuir junto com a minha tela, olha só. Ela vai começar a diminuir, vai começar a espremer, está vendo? Então, conforme o tamanho da minha tela está diminuindo, a minha imagem também está diminuindo.

Isso aqui, quando a gente implementa no CSS, em questão de desenvolvimento, são widths definidos em porcentagem. Vamos supor que eu defini aqui um flexbox e eu pedi para essa imagem pegar 100% do elemento da caixa. Como a caixa está diminuindo, a minha imagem vai diminuir também.

Então, esse aqui é um tipo fluido, só que ele não pode ser aplicado de forma inteira porque vamos supor que eu mantenha fixo aqui, não vai quebrar. E vamos supor que eu continue diminuindo, diminuindo, diminuindo e diminuindo. Vai chegar um ponto que a minha tela vai ficar pequena, lógico que eu estou diminuindo. Esse bloco não iria quebrar, está vendo? Ele iria ficar um do lado do outro assim até eu esmagar os dois. A minha largura do texto aqui iria ficar muito pequena e eu não iria conseguir ler direito e a minha imagem também ficaria muito pequena.

Então, não dá para aplicar o sistema fluido na tela inteira, dá para aplicar em determinadas seções, em determinados breakpoints e aí não se preocupe que você vai entender isso. Com o passar das aulas e também quando você for assistir às aulas de desenvolvimento no script, a FIA.

Então, o fluido tem essa ideia, é quando os meus elementos são definidos com porcentagem com base na largura da tela e conforme eu diminuo, a minha imagem diminui junto. Só que, mais uma vez, se eu aplicar só isso, o meu layout fica pobre porque se eu for diminuir e ele vai seguir só essa linha, os meus elementos não vão quebrar para poder virar vertical e aí meio que vai ser um sistema responsivo porco e não chega a ser responsivo, é literalmente fluido.

### Adaptativo

O adaptativo encobre um pouco mais do fluido, então a gente meio que vai galgando degraus.

Então, vamos supor, vocês vão entender um pouco mais isso, aqueles que já viram as aulas de flexbox, que quando eu estou definindo alguns itens, tem como eu colocar media query, ou seja, definir uma seção lá no CSS para ele ler quando chegar a determinada resolução. Então, eu vou lá no CSS e coloco, por exemplo, uma cláusula para ele começar a ler determinada folha de estilo quando ele estiver abaixo de 960 pixels, por exemplo, que a propósito isso é um breakpoint, é um valor de resolução onde eu falo para ele ler determinados estilos para poder aplicar a minha página.

Então, quando chegar em 960, vamos supor que ele começou a ler. Está vendo? Foi justamente nesse breakpoint que ele quebrou aqui, isso aqui é adaptativo. Então, quando ele chegou em determinado valor, ele leu uma folha de estilo onde ele mudou alguns elementos, você percebe que ele não está fluido, o que ele mudou de repente, está vendo? Ele mudou alguns tamanhos e aí isso aqui é adaptativo porque ele pega o valor da minha... Da minha tela e aí ele dá a folha de estilo com relação àquele breakpoint, está certo? E aí ele vai modificando conforme as telas.

Ele é bem mais... Esse modo adaptativo é mais otimizado. Por quê? Porque vamos supor que eu fiz alguma requisição e a minha tela é de 960 pixels, e tem essa resolução aqui próxima, eu vou mandar exatamente o estilo daquela tela, entendeu? Só que o adaptativo é específico para aquele estilo de tela, então se eu pegar alguma resolução alternativa, você vai ver que ele quebra, ele não funciona em outras resoluções, entendeu?

Então, o adaptativo é um pouco mais rápido porque é um para a tela e um pouco mais trabalhoso porque você tem que fazer vários estilos para várias telas, só que ele é mais rápido porque é um estilo só para cada tela, entendeu? Ele não carrega várias coisas, ele não analisa determinadas distâncias nesse sentido, ele é um pouco mais específico.

### Responsivo

Enquanto o responsivo engloba todos esses caras aqui, então ele meio que mistura o melhor de todos os mundos, por isso que esse meu site aqui é responsivo, você pode ver que ele tem características de fluido, que é nessa seção aqui, onde ele diminui junto com a minha tela, ele tem características de ser adaptativo, ou seja, quando chega em determinada resolução específica, ele coloca algum estilo a mais ou a menos para poder adaptar aquele tamanho de tela um pouco mais específico ou de uma seção para baixo e o agregar desses dois mundos é o responsivo, então ele é um pouco mais carregado, ele tem meio que todos esses modos operantes dentro de um só.

E isso nunca vai invalidar sempre você testar em vários tipos de dispositivos e a gente vai ver isso quando estiver construindo nossos projetos em todas as telas, a gente está testando como é que se comporta, por exemplo, em diferentes tipos de tela, em diferentes dispositivos porque hoje em dia a variação e a quantidade de dispositivos que tem é tão grande que você fazer o adaptativo é praticamente suicídio, você tem quantos modelos de Galaxy, você tem quantos modelos até de iPhone que são os mais padrões, você vê que tem variação entre eles, então hoje em dia o responsivo está sendo o queridinho mesmo para poder a gente projetar as nossas interfaces e a gente continua, aliás, essa conversa de sub-grids na próxima aula.

## Alinhamento e consistência

Mais uma vez enfatizando a questão do alinhamento da consistência, por que é tão importante, pessoal? Porque, por exemplo, aqui no wireframes, eu também vou citar isso na parte prática, você percebe que o meu conteúdo é alinhado aos grids, está vendo? Então, quando você coloca os grids, você vai ver que eles são todos alinhados, estou pegando seis colunas aqui e, por ser uma ilustração, eu estou deixando ela aqui de fora, mas é porque é o estilo dessa ilustração, mas olha só, é sempre alinhado, está vendo? As colunas do centro, sobra três para um lado, três para o outro, então olha só como é que isso facilita quando eu estou projetando. Certo?

Ah, quanto que tem de distância de um elemento para o outro? Ah, é uma coluna, então ajuda demais quando a gente estiver projetando e vai ter parte prática para vocês entenderem o tanto que isso aqui faz a diferença quanto à consistência, alinhamento e organização na questão do design e não deixe de olhar os websites [e] plugins para poder criar os grids que eu sempre deixo aqui no master file, então grids, também na parte prática a gente vai estar mexendo muito neles e conhecendo um pouco mais desse mundo, então essa aula foi um pouco mais introdutória para poder a gente entender os próximos conceitos, beleza galera? Até a próxima.
