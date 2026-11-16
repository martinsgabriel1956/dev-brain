# Flex-shrink e flex: a redução dos itens e o atalho grow, shrink e basis

Opa, fala pessoal, nós vamos dar continuidade, agora a gente vai conversar um pouco sobre o flex-shrink. Basicamente, ele vai definir a capacidade de redução do item.

## O que é o flex-shrink

Lembra quando a gente estava executando essa parte da última aula sobre o flex-basis? A gente entendeu e a gente percebeu que os itens vão se ajustando, eles tendam a se ajustar para poder manter todas as regras que a gente estabeleceu lá, que é a regra de grow e a regra de basis.

Por padrão, o flex-shrink sempre vem denotado como um. Por ele ter um número, ele está falando que está positivo: eu permito que o item meio que diminua e permita a redução do tamanho do item para poder caber dentro do container e tentar satisfazer todas as particularidades que você aplicou, está certo?

Quando eu coloco o flex-shrink zero, ele fala o quê? Não, é para ficar fixo com o flex-basis que foi estabelecido, para manter esse valor fixo, pronto, acabou.

O flex-shrink, quando você aplica algum número, ele justamente vai permitir uma diminuição ainda maior e proporcional. Então, se eu colocar, por exemplo, um flex-shrink igual a quatro, ele vai permitir que quatro vezes ele diminua mais do que o flex-shrink um, então meio que é proporcional esses dois aqui.

## Por que é difícil perceber o flex-shrink

Para falar bem a verdade, pessoal, é muito difícil vocês perceberem a diferença do flex-shrink, e eu vou mostrar para vocês na prática o porquê, onde quase a gente não presta atenção nesse cara quando a gente está construindo layout. E eu vou colocar aqui uma situação bem adversa para vocês entenderem de fato se vai mudar ou não e para vocês verem que é bem difícil.

O flex-shrink vem com o padrão um, então se eu vir aqui e aplicar um, vai mudar praticamente nada ou absolutamente nada, ele vai se manter do mesmo jeito. Se eu colocar aqui 100 pixels, vou poder forçar ele quebrar mais de uma vez. Ele está permitindo: quando eu mudo aqui, ele está diminuindo, está permitindo que os itens sejam diminuídos para poder satisfazer todas as condições.

Se eu colocar no zero, vamos ver o que acontece, vamos na zero, vamos ver se muda alguma coisa, está vendo? Não mudou absolutamente nada. Fala assim: então o que está acontecendo? Vamos lá, vamos testar aqui o flex-shrink igual a cinco, por exemplo. Teoricamente ele tem que diminuir, só que ele vai permitir uma diminuição maior do que aquela que a gente tinha colocado. Então vamos colocar aqui 6, vamos ver se a gente consegue enxergar isso. Basicamente a gente não enxerga nada.

Qual foi a situação que eu enxerguei a influência do flex-shrink? Quando eu levei a situação mais para o extremo. Porque, como o container está em um tamanho ainda legal, ele não sentiu ainda essa necessidade de utilizar o flex-shrink para poder diminuir mais ainda, porque o termo, o tamanho que está vindo diminuindo já está satisfazendo as condições, e a diferença do flex-shrink 6 para o 1 é tão pequena que também você não percebe.

## Levando ao extremo

Eu vou exagerar aqui na colocação, vamos aumentar o flex-basis, fazer com que ele seja bem maior para poder ele quebrar, vamos tentar perceber alguma coisa diferente. Até agora não percebi nada de diferente. Vou colocar o 1 de volta, vamos ver se vai mudar alguma coisa. Para mim não mudou exatamente nada, mas o que acontece?

Eu vou extrapolar um pouco, vou vir aqui em inspecionar, nós vamos diminuir isso aqui ao máximo para poder a gente verificar, olha só o que está acontecendo. Quando a gente está chegando em um limite um pouco maior, você percebe que por agora está precisando quebrar esse conteúdo aqui, que antes não era necessário porque ele estava cabendo; ele está permitindo quebrar. Quando ele chega em um limite muito grande, ele não consegue mais diminuir os conteúdos aqui, justamente por ser um conteúdo contínuo. Olha só o que acontece, ele diminuiu ao máximo.

Se eu vir aqui no flex-shrink e colocar 7, vou colocar um valor maior, vou colocar 10, vamos ver se mudou alguma coisa, vamos ver se ele vai tentar quebrar mais alguma coisa. Justamente porque não tem mais como quebrar esse número aqui, por ele ser contínuo, ele não vai tentar quebrar essa informação, só se eu der enter no HTML. No CSS, eu percebo que não tem muita diferença. Ao passo que ele quebrou, quando ele pegou aqui nesse limite, ele meio que deu enter do 6, do 7, do 8. Então você percebe que é em situação muito atípica, por isso que quase você não vai perceber essa situação.

Agora, se eu vir aqui e colocar flex-shrink 0, ou seja, não diminua, mantenha esse 300 pixels forever, vamos ver o que acontece. Agora eu entendi: você percebe que agora que o meu container mantém lá, só que o flex-basis está mantido, os 300 pixels estão mantidos.

Como é difícil você encontrar até mesmo tela de celular a 320 pixels, por isso que a gente não percebe muito como é que funciona essa particularidade. Na maioria das vezes, o flex-shrink vai ficar igual a 1 e você nem vai perceber, mas é legal a gente estar estudando aqui e trocando experiências nesse sentido para poder a gente entender um pouco mais da tecnologia e desse recurso.

## O atalho flex

Aproveitando, o flex, ele é até legal porque de cara é o que eu mais utilizo. É lógico que eu utilizo o flex-basis para poder enfatizar determinada propriedade, mas eu utilizo muito do flex, que é meio que um atalho das propriedades flex-grow, flex-shrink e flex-basis, isso em um comando só.

Basicamente é sempre o quê? A ordem é o grow, o shrink e o basis, e esse aqui é o valor padrão, ele sempre vem setado como flex 0 1 auto. E o próprio W3C fala que é legal definir o flex dessa forma, utilizando essa propriedade, porque ela é inteligente, então meio que é mais difícil você errar quando você utiliza o flex total.

## Flex: 1

Então, basicamente, se eu quiser aplicar essa mesma coisa aqui, o que eu vou fazer? Se eu definir flex igual a 1, como ele vai ficar? Vamos lá, se eu definir o flex igual a 1, olha só o que ele vai virar, como fica a configuração? É como se eu colocasse flex-grow igual a 1, é como se eu colocasse flex-shrink igual a 1, ou seja, ele permite, flex-shrink igual a 1, e o flex-basis igual a 0.

Lembra o que faz o flex-basis? O flex-grow a gente sabe que é com relação a crescer, então eu meio que apliquei isso aqui a todos, então está tudo certo. Flex-shrink, na maioria das vezes, não vai fazer muita diferença, então a gente tem que sempre observar para o grow e para o basis. O basis, lembra que ele tem o valor padrão de flex-basis auto, onde ele não está importando, ele não está nem aí, é com relação ao tamanho. O flex-basis meio que vai tentar deixar todos os mais iguais possíveis. Você percebe que, mesmo com o conteúdo estando aqui diferente, eles estão muito parecidos uns dos outros, mesmo estando com o grow aqui diferente. Quando você define o flex igual a 1, ele vai meio que aplicar essas propriedades aqui.

## A fórmula 1, 1, 300

E quando eu quero um flex parecido com o que estava da vez passada: vamos deixar o flex-grow igual a 1, vamos deixar o flex-shrink igual a 1, vamos colocar, por exemplo, auto, está aí, automático, que ele não está nem em deixar tudo padronizado, ele ajusta com relação ao conteúdo e está tudo certo. Eu posso colocar 1, 1, 0, onde ele vai se tornar exatamente da mesma forma, e, por exemplo, colocar 300 pixels, que é a forma que estava anteriormente.

Então essa de cara é a tipa fórmula que eu mais utilizo, é sempre 1, 1, 300, e quando eu quero aplicar algum flex-grow diferente, eu vou lá e aplico de forma inline ou aplicando alguma classe para poder fazer com que ele cresça mais do que o outro. Então isso aqui é um belo atalho e ele facilita de fato a nossa vida.

Se eu for colocar, por exemplo, um flex-grow igual a 2, a gente falou do exemplo do 1, se eu for colocar flex-grow igual a 2, o que isso aqui reflete? Vamos ver o que acontece. Quando eu defino o flex-grow igual a 2, ele mantém exatamente as mesmas coisas quando você deixa ele flex-grow igual a 1, só que a diferença é que o flex-grow fica igual a 2. Então, quando eu mudo aqui, ele sempre mantém o shrink de 1, sempre mantém o shrink, o basis de 0, e aí ele muda apenas o grow.

Então eu sempre utilizo, na maioria das vezes, 1, 1 e o flex-basis, porque eu gosto do flex-basis para poder a gente ter um melhor controle dos nossos flex-itens, beleza, galera? Até a próxima.
