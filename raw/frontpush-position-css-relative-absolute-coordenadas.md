# Position no CSS: relative no pai, absolute no filho e o sistema de coordenadas

Opa, fala pessoal, Násser aqui, sejam bem-vindos a mais uma aula de CSS, onde eu vou apresentar vocês mais um recurso, mais uma das propriedades que o CSS consegue fazer para a gente, beleza? Então, sem mais delongas, vamos lá.

## Position também é layout, mas não o comum

Como eu tinha falado para vocês, o CSS é uma linguagem de estilização e agora a gente descobriu que é uma linguagem de layout, então a gente consegue controlar o comportamento das caixas, dependendo do tamanho da nossa tela, para poder a gente construir o nosso layout, ter recursos como flexbox, grid layout e tudo mais, beleza? Uma nova forma da gente também construir layout é utilizando position, não é muito comum para poder a gente fazer layout assim, a gente utiliza mais outras convenções e vocês vão descobrir também o porquê, mas eu quero mostrar nesse aqui como é que funciona o position, tá bom? Então vamos lá, sem mais delongas, vamos lá.

## Container relative e item absolute

Vamos supor que eu tenho aqui o container e tenho um item dentro desse container, beleza? O container, a gente acabou de ver aqui, ele tem uma borda vermelha, eu vou colocar um padding aqui dentro de 8 pixels só para poder ficar espaçadinho, bonitinho, beleza? E nós temos aqui essa caixa, do qual, nessa caixa, eu quero definir um width para ela de, sei lá, 400 pixels, um max-width, é melhor, um max-width de 400 pixels nessa caixinha item que nós temos aqui, que ela tem uma borda verde.

Vamos supor que o elemento container eu defina ele como um position relative e esse aqui eu vou definir ele como um position absolute, olha só o que aconteceu, o que está acontecendo, como é que a gente consegue agora trabalhar com isso aí. Eu vou definir aqui no container, só para poder a gente entender melhor, um height de 400 pixels, melhor, 300.

E aí, pessoal, o que acontece? Você vai ver que se eu apagar o position relative do container, olha só o que acontece, teoricamente, a caixa perde a referência dela, nesse exemplo aqui não foi tão claro, mas eu vou deixar mais claro agora, vou apagar esse header aqui, nós temos aqui caixa, aparentemente não mudou absolutamente nada, mas, por exemplo, eu vou dar um padding-top aqui no container de 100 pixels, você está vendo que ele respeitou, ele deu o padding, por mais que ele esteja com o position absolute.

Mas, olha só, se eu vir aqui e colocar um top 0, olha só o que acontece, por mais que eu tenha dado um padding-top, que é um espaçamento no conteúdo interno do container, que o item é um filho do container, era para ele espaçar 100 pixels e ficar ali, mas como eu defini ele como position absolute e estabeleci para ele top 0, ele topou lá no meio, então isso aqui é uma outra propriedade de posicionamento, é um outro recurso de posicionamento do CSS, que eu vou explicar para vocês.

## Um sistema de coordenadas

Basicamente, pessoal, quando você define um elemento como position absolute, principalmente, ele fica flutuando, e ele sempre tem um relativo para quem ele olha, então é como se fosse um sistema de coordenadas, eu vou vir aqui para o Figma para poder demonstrar isso aqui para vocês.

O que é um sistema de coordenadas? Nada mais é, pessoal, do que um sistema XY, acredito que todo mundo viu isso aí na escola, então está aqui um sistema XY, do qual eu tenho aqui o eixo Y, deixa eu colocar aqui em um tamanho maior, aqui eu tenho o eixo Y, vou colocar em um tamanho bem grande, e aqui eu tenho o eixo X.

Quando a gente trabalha com o position, pessoal, ele fica flutuando meio que no eixo de coordenada, e ele sempre tem um elemento relativo, o elemento relativo, a gente sempre vai considerar ele como no ponto zero, ou seja, nesse ponto aqui, só que o pai do elemento tem que ser relativo para poder ele dar o eixo de referência que ele tem que se comportar.

## Sem pai relative, a referência é a janela

No caso, o que aconteceu? Eu defini o item como position absolute top zero, ele tem alguém como referência, como eu não coloquei o pai dele como referência, quem é que ele pega como referência? O body, ou seja, essa tag aqui vem por padrão como position relative, pode ver que ele topou lá no meio, então a própria tela tem como position relative. E vamos supor que esse aqui é o elemento que a gente está controlando, o elemento verde que a gente está controlando, quando eu dei position absolute top zero, ele topou bem aqui, top, ou seja, a distância do meu eixo que ele tem como referência, que é esse azul aqui, que no caso é a minha janela, ele deu um top zero.

Você pode ver que se eu vir aqui e colocar, por exemplo, no item, ao invés de top zero, 50px, ele distanciou 50px, se eu vir aqui e colocar left também 50px, ele distanciou para cá, 50px. Então, ele tem como referência isso aqui, o que eu fiz? Eu dei um top de 50px, ele distanciou aqui, essa distância aqui é 50px, aí ele foi lá e distanciou mais 50px aqui, e ele ficou bem aqui, entendeu?

## Pai relative, filho absolute

O que eu tenho que fazer? Eu tenho que saber onde está o relativo para poder definir como absoluto, eu posso definir o container como relative, aí ele vai estar olhando agora para o container, que é para o pai dele, então eu posso vir aqui, position relative, você vê que ele deu um espaçamento um pouquinho maior.

Se eu vir aqui e colocar, por exemplo, eu vou tirar isso aqui de novo, vou colocar um padding grande só para você sentir a diferença, de 40px, não, vou colocar um margin, é melhor, um margin de 40px, então olha lá, você pode ver que se eu der aqui, sei lá, 20px, ele não está importando para o pai, para o container, se eu colocar aqui 20px, ele está lá flutuando, porque eu não defini o pai como relative.

Quando eu venho aqui e defini como relative, olha lá, agora ele respeitou, agora ele está olhando para o pai, que é o container, antes ele estava olhando para janela, que é o relative, porque você não tinha definido, ele por padrão faz isso, e aí você viu que mudou, aí se eu colocar agora 50px aqui, agora ele está deslocando 50px com relação ao pai, com relação ao container vermelho aqui, tá?

## Quando usar: as bolinhas do FrontPUSH

Então, é esse o módulo de fazer posicionamento dentro do CSS, mas quando é que você utiliza isso? Por exemplo, aqui no front, você vai perceber que essas bolinhas aqui, elas modificando, indo para cá, indo para cá, eu simplesmente estabeleci para eles um top e um left, ou seja, em um primeiro momento, esteja com um top e um left de 50 e 50, depois vai para um top e um left de 80 e 80, depois vai para um top e um left de 30 e 30, aí ele ficou fazendo assim, ele meio que está livre no eixo de coordenadas, e aí eu consigo controlar melhor, com mais precisão, o posicionamento de algum elemento.

Isso é muito comum para você construir layout? Não, é mais para construir essas coisas mais exóticas assim, eu quero que isso aqui fique nesse elemento específico, eu quero que ele fique nessa distância específica de um outro elemento, você utiliza o position.

## top, left, right e bottom

Só saiba que tem um position, o left, o top, tem um right também, porque assim, eu sempre estou tomando como referência o top e o left, porque eu sempre vou ficar nesse quadrante aqui, mas vamos supor que eu sempre queira o meu elemento na parte direita, aí eu vou colocar right, ele vai colar aqui, como eu coloquei left, ele vai colar aqui, right ele vai colar para cá, se eu colocar bottom, ele vai colar para cá, vocês entenderam? Então, eu coloquei aqui no caso, 20, 50, se eu modificar isso aqui para bottom e isso aqui para right, olha lá para onde ele vai, minha tela está bem na frente, olha aí para onde ele vai, entendeu?

## Resumo: relative no pai, absolute no filho

Então, é questão de posicionamento dentro do eixo de coordenada, eu preciso dar um eixo para ele, eu preciso dar um relative, já que ele é absolute, então você precisa entender essa questão de pai e filho, position absolute e position relative, relative fica no pai, absolute fica no filho, se você não definir quem é o relative, ele sempre vai pegar como referência a própria janela, então para poder você ter controle, você define o pai como relative, o filho como absolute e ele vai ficar flutuando dentro desse pai relative e você consegue posicionar onde ele quer.

Reitero, isso aqui não é feito para fazer layout em si, quando você quer posicionar algum elemento específico, por exemplo, aqui no front, a outra seção onde eu utilizei isso foi, por exemplo, na minha descrição, essa parte aqui onde está vendo esse nzinho aqui, ele está específico em uma parte bem específica do meu posicionamento, ele está como position absolute, esse selo aqui também está como position absolute, mas o resto todo, eu utilizo o flexbox, que é o outro módulo, ou o grid layout, ou o grid system com o Sass, então é mais como curiosidade para vocês entenderem como funciona essa propriedade aqui do position, então falou, até a próxima.
