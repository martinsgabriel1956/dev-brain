# Flex-direction, flex-wrap e flex-flow: direção, quebra de linha e o princípio do responsivo

Então, pessoal, conforme eu disse na aula passada, a gente vai continuar aqui, de onde a gente parou: definir o display flex, ele vai se tornar um flex container e os seus filhos diretos se tornam flex itens. Entendeu isso aí, a gente consegue partir para as outras propriedades. E como tem algumas propriedades bem simples, eu vou tratar de mais algumas de uma vez nessa aula aqui para poder a gente otimizar a aula.

## Flex-direction

Com relação a essa propriedade flex-direction, ela está dizendo, literalmente, a direção dos flex-itens. Por padrão ela é row, que é linha, ou seja, quando eu defino o display flex, automaticamente o flex-direction já fica definido como linha.

Então, vamos lá. O que acontece? Eu vim aqui e vocês lembram quando eu deixei, deixa eu só comentar aqui, você lembra quando tinha só o item 2, 3 e 4? Quando eu deixei ele display block, ficou um embaixo do outro e ele completou em 100%. Aqui, quando eu deixei ele como display flex, automaticamente um ficou do lado do outro.

Então, se eu vir aqui no meu container e definir flex-direction como row, meio que não vai mudar nada, porque já é o padrão. Quando eu coloco row-reverse, como o próprio nome já diz, ele vai inverter a ordem dos itens.

Então, você percebe que é muito interessante de vocês literalmente irem testando. Faça esse mesmo exercício aqui, mas sem colar de mim, olhando a teoria e aplicando para vocês entenderem, porque é muito interessante de aprender flexbox fazendo, voltando na teoria.

## Flex-direction e responsividade

E a propriedade do flex-direction é extremamente utilizada, pelo menos por mim, é uma das formas que eu faço para poder conseguir uma boa responsividade. Você percebe que os elementos estão em linha, totalmente enfileirados, e depois eles ficam enfileirados em coluna. E é justamente isso que eu quero, e é deste princípio que parte a gente quebrar os blocos no sistema responsivo desktop.

Então, vamos supor que eu tenho três containers aqui, três itens aqui, e aí eu quero que, simplesmente, eles quebrem e fiquem em fileira por causa do mobile. Então, basta em um media query eu modificar: quando chegar em determinada resolução, troca para mim de flex-direction row para flex-direction column.

Então, vamos fazer essa opção aqui, vamos fazer esse aqui. Esse aqui está com o flex-direction row reverso, então eu posso muito bem aplicar o flex-direction column para ver como vai ficar. Olha aí, ele meio que volta a ser display-block. E eu posso colocar column-reverse, para ver, e olha só o que acontece, muito fácil.

## Media query

Vamos supor que eu quero fazer isso para um celular, e eu vou utilizar o do media query. Eu não sei o que é media query? É literalmente um recurso do CSS, onde eu consigo aplicar estilos para uma determinada faixa de resolução, e eu coloco esse limite utilizando o media query, onde eu coloco aqui media max-width, vamos supor 960 pixels.

E aí, eu vou colocar aqui dentro um estilo que eu quero que ele leia e sobrescreva o estilo que está antes, para quando chegar em 960 pixels, leia os estilos que estão aqui.

Então, eu vou pegar o container, não vou modificar absolutamente nada, só que eu vou mudar o nome da propriedade, eu acabei de esquecer, o flex-direction, vamos lá, estou ruim da cabeça já, flex-direction para column, column-normal. E aí, vamos ver como isso se dá na prática.

Olha só, está vendo a mudança? Então, olha só o princípio do sistema responsivo, a gente já está vendo aqui na prática como é que se aplica esse tipo de coisa. Ele quebrou exatamente do jeito que eu queria, quando ele atingiu 960 pixels. Se eu colocasse 720, ele vai demorar um pouquinho mais, tem, quebrou.

Então, é esse o princípio que a gente vai aplicar para poder construir sistemas responsivos, então superguarde essa propriedade aqui.

## Flex-wrap

O flex-wrap também é muito importante para poder construir sistemas responsivos e ele vai definir se os itens devem quebrar ou não.

Lembra quando a gente veio aqui e colocou vários itens? Então eu vou descomentar essa parte lá de trás, vou descomentar isso aqui para ficar vários itens, onde eles passam do meu container. Por que eles estão acontecendo isso? Porque eu não falei que era para eles quebrarem.

Por padrão, sempre vem flex-direction row, em linha, e por padrão sempre vem o flex-wrap como nowrap, ou seja, não quebre. Então, se eu deixar assim, ele não vai mudar exatamente nada, ele vai continuar do mesmo jeito que estava e ele vai criar uma barra de rolagem aqui, porque ele não vai quebrar o sistema.

## Max-width em vez de width

O meu container vai ficar responsivo, por quê? Porque eu defini o max-width, eu não defini um comprimento específico. É diferente de eu colocar width 700, totalmente diferente. Ele não vai mudar o tamanho dele, não vai mudar, ele vai entrar junto com a minha barra de rolagem.

Agora, se eu colocar o max-width, o que estou dizendo para ele? O máximo do container, o tamanho máximo que você vai alcançar é 700, e ele meio que ajusta, está vendo que ele está aqui ainda? Ele ajusta. Então é uma boa prática você utilizar o max-width, o min-width, o max-height e o min-height, se aplica também, é uma das propriedades. Então, percebe que a gente vai entendendo de responsividade ao passar as aulas.

## Wrap e wrap-reverse

Agora, se eu colocar o sistema wrap, percebe que ele quebra, agora ele quebrou, está vendo? Então, quando ele chega no limite do container e percebe que o conteúdo não consegue mais quebrar, percebe que o meu conteúdo é item 1, 2, 3 e 4. E como eu defini um padding de 20 pixels, ele vai até no limite e, quando chega no limite, ele vai lá e quebra. Olha só como é legal.

Então, muito importante também para poder a gente construir responsividade, quando eu quero que quebre elementos quando chega em determinado limite, e a gente vai estudar algumas outras propriedades para poder entender isso da melhor forma possível.

Então, basicamente, nowrap ele não vai quebrar, ele vai continuar mesmo atingindo o limite do container; o wrap vai quebrar; e o wrap inverso simplesmente vai quebrar da maneira contrária. Então, vamos fazer um pequeno exemplo: se eu colocar wrap inverso, vamos ver o que acontece.

Então, galera, você percebe que vocês precisam treinar isso aqui, não deixem eu fazendo sozinho e vocês ficam de boa. Então, pega isso aqui e faz isso também para poder a gente entender. Então, vamos lá, vamos continuar. Sempre, não deixe de ler, sempre leia a teoria aqui para poder a gente entender um pouco mais.

## Flex-flow

E por último, o flex-flow. O flex-flow, galera, vou deixar assim bem claro, meio que eu não utilizo muito, porque ele é simplesmente um atalho das propriedades flex-direction e flex-wrap. Então, eu prefiro utilizar flex-direction e flex-wrap. Flex-flow é simplesmente um jeito de utilizar os dois em uma linha só, mas é justamente os mesmos conceitos, se aplica exatamente as mesmas coisas.

Na próxima aula, a gente vai trabalhar sobre o Justify Content Center.
