# Propriedade transform, parte 1: translate, scale, rotate, skew, matrix e perspectiva

Opa, fala pessoal, e aí nós vamos começar agora a parte de básico do CSS. É um básico diferente daquele que a gente viu na codificação front-end e é meio que aquele lá é um pré-requisito, se você não conhece nada de CSS, eu recomendo você começar por lá, onde aqui nós vamos dar uma focada nas propriedades que são mais voltadas para motion, então é transform, transition, opacity, position, animation, e aí sim a gente vai ter bagagem para poder começar as nossas animações, beleza?

Só quero deixar enfatizado que durante as aulas o nosso material de apoio é o W3C, para quem não conhece, esse é meio que um órgão de tudo que tem na web, esse é um órgão que regulamenta, então muito das propriedades lá, das regrinhas, de mais exemplos e de maiores explicações, não deixem de utilizar, de ver, de conferir o W3C. Eu sou desenvolvedor há um tempo já e mesmo assim não deixo de olhar esse material aqui sempre.

## As funções do transform

Então vamos lá, sem mais delongas, essa aula aqui a gente vai trabalhar um pouco da propriedade transform e como é que a gente consegue manipular os objetos, vou dar aqui uma explicação bem rápida na teoria, mas a maioria dela vai ser na prática, onde a gente vai demonstrar todas essas propriedades aqui e ver como é que a gente manipula objetos. Então elas meio que são autoexplicativas, mas é sempre legal demonstrar e vocês tentem executar a mesma coisa para vocês irem pegando a manha e entendendo como é que se dá o processo, certo?

Esse matrix e esse matrix 3D, ele meio que trata-se de um resumo das propriedades aqui de baixo. Então primeiro nós vamos ver cada um aqui de forma separada e depois a gente dá uma olhadinha no matrix 3D.

Em suma, translate, como o próprio nome já sugere, é quando você quer literalmente mover o objeto para o lado ou para o outro, para cima ou para baixo. Dá um translado dele, então ele mexe nos três eixos, inclusive no eixo Z, que a gente vai ver como é que a gente faz esse tipo de translado aqui.

Scale, como o próprio também nome já sugere, ele vai tratar do tamanho do objeto, então o objeto está lá no seu tamanho normal, tem como eu diminuir ele, tem como eu aumentar ele e também aumentar nas três coordenadas, tanto na X como na Y ou na Z. E aqui tem alguns comandos que são para tratar justamente cada um deles de forma separada.

Rotate também, para deduzir pelo nome, é quando eu quero rotacionar o objeto, o scale é quando eu quero deitar o objeto, esticar o objeto. Então eu deixo, por exemplo, a base fixa e a parte de cima eu translado de um lado para o outro, onde eu vou meio que deitando o objeto e eu estabeleço o ângulo que eu quero que isso aconteça.

E a perspectiva, para quem não sabe, a perspectiva é uma propriedade muito legal para poder a gente ver manipulação de elementos 3D no CSS, onde vocês sabem, nós temos aqui um ambiente 2D, nós temos a largura e a altura da nossa tela. Quando a gente quer simular algum elemento 3D, a gente tem que colocar a perspectiva, tem que colocar uma distância do eixo Z, de forma que a gente consiga manipular o objeto e dar essa noção para a pessoa.

## Preparando o código

Sem mais delongas, vamos aqui para o código, onde a gente vai tratar algumas coisinhas aqui, a gente vai entender algumas coisinhas, deixa eu apagar essa parte aqui, você primeiro me explica o que você fez.

Eu simplesmente criei um arquivo index.html, uma página HTML, fiz o link do CSS, utilizando a tag link. Mais uma vez, eu reitero, se você não entende o que eu fiz aqui, dá uma olhada na parte de básico, CSS, lá no ScriptFA, em codificação, que você vai entender.

E aqui eu fiz um arquivo Sass, como assim você não explicou o que é Sass, você tem que primeiro ensinar CSS. Então calma, eu estou utilizando apenas CSS, o Sass eu estou utilizando porque ele adiciona o WebKit nos meus comandos de forma automática e facilita a eu ter maior compatibilidade entre browsers. E muitas dessas vantagens eu conto lá no meu vídeo do YouTube de Sass, então com aquele vídeo introdutório você vai entender como é que funciona essa ferramenta, é um plugin que eu instalo aqui no VS Code.

Sempre aplique esse hack aqui, onde o asterisco é um seletor, onde eu falo para ele aplicar para todas as tags HTML da minha página, onde eu falo para o quê? Tira o padding, tira o margin, porque tem alguns elementos, tem algumas tags do HTML que por padrão vem com o margin e com o padding e eu peço pra zerar tudo e o box-sizing eu aplico o border-box para poder ele ter como referência a borda e não o conteúdo.

Exemplifica para mim. Vamos supor que eu criei uma caixinha com a div chamada class-box e eu estou configurando com box-sizing e border-box. Olha só, se eu escrever aqui um conteúdo grande, olha só o que acontece, ele passa da minha caixa, porque eu estou falando para a caixa ter como referência a borda e eu estou falando para ele ter 100 pixels exatos. Se eu vir aqui e mudar para content-box, ele vai levar em consideração agora o conteúdo e aí quando eu adiciono, por exemplo, um padding, então 0, 20 pixels, mesmo que eu tenha estabelecido 100 para ficar fixo, ele vai permitir que o conteúdo se adeque ao conteúdo, então eu sempre deixo como border-box.

Então é só para explicar essa propriedade, para quem não sabe, eu apliquei um display flex para poder o meu filho, como eu apliquei no body, o meu filho direto dele é a minha class-box, então é esse elemento aqui onde eu só estou pedindo para ele centralizar de forma horizontal e centralizar de forma vertical, então vai ficar no centro para a gente entender como é que funciona essas propriedades.

## rotate

Enfim, sem mais delongas, está aqui a minha caixinha box onde a gente vai trabalhar essas propriedades transform de maneira bem tranquila para vocês entenderem e a gente começar os primeiros passos, vamos colocar aqui a propriedade transform e olha só, a maioria dela já está listada aqui, para poder a gente começar, eu vou começar aqui pelo rotate, onde eu simplesmente vou colocar um valor em graus, então para quem não sabe, em inglês a gente escreve degrees, é assim ou é assim, enfim, mas é graus em inglês e a gente coloca como deg.

Então vamos supor que eu coloque 50 deg, o meu quadradinho vai rotacionar com relação ao seu eixo principal aqui, então meio que o seu eixo, o seu ponto de ancoragem está no centro, se tivesse por exemplo aqui, ele iria virar assim, e aí na próxima aula, quando a gente for falar de propriedades do transform, a gente vai ver como é que a gente muda esse ponto de ancoragem dos elementos, mas por padrão quando você cria uma div, ele vem estabelecido no centro, então você rotaciona o objeto, vamos colocar aqui por exemplo 70 deg, ele rotacionou e aí ele vai até 360, então se eu colocar aqui 270, como está certinho no eixo, você não vai perceber, mas deixa eu aplicar aqui um linear gradiente para poder a gente ver de fato ele girando, porque com uma cor sólida você não sabe se ele girou ou não.

Então deixa eu vir aqui no Figma rapidinho, vou colocar um gradiente bem feio, o clássico blue-red, para poder a gente ver literalmente ele rotacionando, então 0 deg, a gente coloca 30 deg, ele vai rotacionando e pode colocar número negativo também, [menos] 30 deg ele simplesmente vai inverter o quadradinho, esse aqui é a propriedade rotate.

## translate

Tem a propriedade translate e a gente tem como utilizar x e y, que é essa translate aqui, onde a gente pode colocar aqui a informação x e y e a gente coloca em formato de pixels, então vamos supor que eu coloque 200 pixels aqui e 100 pixels no y, olha só, ele transladou 200 para cá, deixa eu transladar um pouco menos, 50 e 100, vamos ver, então ele transladou primeiro 50 para cá e depois 100 para baixo, porque é isso que vocês vão perceber.

Vamos colocar aqui o translate 3D, que ele já é x e y e z, você coloca as coordenadas, então vamos supor que eu queira só no x, então eu coloco 50 pixels 0, 0, ele sempre vai ter como referência a posição inicial dele e esse translate, pessoal, ele também é utilizado em layout, vamos supor que eu quero fazer um deslocamento bem pequenininho, na minha ilustração eu costumo fazer isso como se fosse um hack, quando eu estou projetando alguma coisa e ela o foge demais no flexbox, tem como eu forçar ele voltar para o lugar utilizando o translate.

Então 50 e aí vocês vão perceber que para a direita o eixo x é positivo, para a esquerda o eixo x é negativo, só que aqui o eixo y é invertido, não é como a gente vê lá na escola, se eu colocar 50 pixels você vai ver que ele vai descer ao invés de subir, então quando eu quero colocar ele lá para cima o eixo x ou o eixo y é negativo, ele é invertido nesse sentido, mas também é invertido entre aspas, ele é invertido com relação ao sistema de coordenadas atual que a gente utiliza, porque tudo na física depende do referencial.

E o eixo z, se eu colocar aqui 50 pixels você não vai descobrir nada, não vai ver nada de diferente porque é o eixo que está saindo da tela, então ele meio que se aproximou de você, mas só que como a tela é 2D você não percebeu e a gente precisa utilizar a propriedade de perspectiva para você ver isso de fato mudando, então você pode utilizar o translate 3D ou então simplesmente o translate x, 200 pixels, onde ele vai mudar somente na x, ou então somente na y, ou então somente na z, vai fazer o translado dos objetos.

Isso aqui é uma coisa muito simples, mas que eu utilizo em várias animações minhas, então um exemplo pessoal, essa setinha aqui eu simplesmente defini ponto de translate, então aqui ela está no determinado translate e eu vim aqui, coloquei um eixo x e eixo y e aí eu pedi para ela ficar transitando com a velocidade diferente entre esses pontos, eu utilizei translate, por exemplo, essas animações aqui onde eu passo o mouse e a bolinha e esses links, eles aumentam, é simplesmente um translate no eixo y, que ele vai lá, sobe e depois desce, eu utilizo justamente ele, para vocês irem conhecendo.

## scale

Já falei de rotate, já falei de translate, vamos ver aqui, vamos falar do scale, vamos lá, o scale, como o próprio nome já diz, ele vai tratar da escala, então se eu colocar 1,2, ele vai dar 20% de aumento com relação ao tamanho original, se eu colocar 2, ele vai dar 100% de aumento, está certo?

Então é como se fosse aplicar desconto, quando você quer aplicar desconto em um número, você faz 1 menos a taxa, quando você quer dar aumento, você faz 1 mais a taxa, então se eu quero dar aumento de 50%, é 1,5, se eu quero fazer o decréscimo de 30%, eu faço 0,7 e por aí vai.

E quando eu aplico o scale, ele faz o quê? No eixo x, no eixo y e no eixo z, tem como eu fazer também essa alteração só no eixo x, então ele meio que vai ficar achatadinho, ou então só no eixo y, está certo?

O que mais? O rotate, eu já falei sobre o ângulo, esse rotate 3D, tudo que é remetido ao 3D assim, é quando a gente aplica perspectiva, que já já vou falar para vocês, para poder a gente visualizar, e o resto, quando não tem, ele aplica somente no 2D, está vendo? O scale, o translate, o rotate, certo?

## skew e várias funções ao mesmo tempo

E agora vamos ver um pouquinho da skew, como é que se dá? Skew, da mesma forma, tem o x e o y, está vendo? E quando eu aplico a skew, vamos supor que eu quero no eixo x e eu coloco 20 deg, você vai ver que ele vai entortar só no eixo x, se eu colocar menos 20 deg, ele vai entortar só no eixo x, se eu quiser que faça no eixo y, vamos ver aqui a diferença, ele entortou no eixo y, se eu colocar 20, colocar aqui 50, exagerar um pouquinho, está aí, e se eu quiser fazer nos dois, é só fazer assim, pessoal, eixo x, aí eu faço 50 também, 50 deg, ele vai esticar mais ainda, onde eu estou mexendo nas duas propriedades, se eu colocar apenas skew, vamos ver o que acontece, então não deixem de treinar, pessoal, não deixem de treinar.

E tem como aplicar muitas propriedades ao mesmo tempo, é só você dar um espaço, vir aqui, rotate, 45 deg, ele vai rodar, 45, tem como aumentar o scale, tem como aumentar o scale só no x, quero que eu aumente tudo, o scale é 1,5, tem como você aplicar todas essas propriedades aqui ao mesmo tempo.

## matrix

E esse matrix, vou falar primeiro desse aqui, porque o trade dele é um pouquinho mais complicado, vocês viram lá, meio que o transform matrix é desse jeito aqui, quando você quiser aplicar, que quase você não vai aplicar, porque não é muito intuitivo, são mais ferramentas que utilizam o matrix para poder colocar, o scale no x, a segunda propriedade é o skew y, a terceira propriedade é o skew x, a quarta propriedade é o scale y, porque já foi o x, então o scale y, aqui translate x e aqui translate y, essas aqui são as propriedades do matrix.

Mas é só se você quiser resumir todas essas propriedades aqui no matrix, aí você utiliza, mas eu, sendo bem sincero, não é muito intuitivo, eu não utilizo muito, mas é bom para a gente entender o que acontece quando você bater o olho nessa propriedade matrix, em algum objeto SVG, você já fala, ele está aplicando a propriedade transform, e tem como eu transformar um em outro. É só uma fórmula de resumir essas propriedades.

## Perspectiva e 3D

E agora nós vamos entender um pouco como funciona o 3D, eu vou agora adicionar um pouquinho de perspectiva, para poder explicar e para a aula não ficar muito longa, eu vou aplicar aqui um rotate x, vamos supor, ele vai virar apenas no eixo x, vocês percebem isso? Ele vai rotacionar o objeto apenas no eixo x.

Então, vamos colocar aqui 30deg para ver o que acontece, olha só, não mudou praticamente nada, vamos ver aqui, 0deg para ver como está, olha, mudou, então ele meio que diminuiu, então se eu colocar aqui 50deg, olha só, ele só diminuiu, então é como se eu colocasse o scale no x de 0,7, vamos ver, aliás, é no y, estou no y, então se eu aplicar no y de 0,7, ou aplicar um rotate x de 50deg, olha só, meio que tem o mesmo efeito, está vendo?

Mas por que isso nasce? O que acontece? Eu vim aqui no meu console, vou clicar aqui na div box, para poder a gente alterar por aqui, eu vou colocar aqui e vou mudar nas setas direcionais, olha só o que acontece, está vendo? Eu estou aumentando e diminuindo o rotate e olha só o que está acontecendo, por que isso está acontecendo? Ele está girando, só que pelo fato de não ter perspectiva, você não está entendendo muito bem, e como é que a gente aplica o perspectiva?

A gente nunca aplica na div que a gente está olhando, por que? Perspectiva depende de quão longe está um objeto do outro, isso se aplica ao nosso olho, por exemplo, se eu pegar o seu celular, você pega o seu celular e fica girando ele na sua frente, se você girar ele muito perto, você vai ver que a perspectiva é 1. Se você girar ele longe, você vai ver que a perspectiva é outra, talvez a variação pela distância é diferente, então eu sempre aplico a perspectiva no elemento pai, naquele que engloba o elemento que eu quero ver, a perspectiva, no caso é o body, então eu já deixei aqui preparado, perspectiva, vou deixar em 400 pixels e agora a gente vai ver o que acontece, olha só.

Se eu vir aqui agora no nosso rotate e mudar, que eu mudo pela seta direcional, para cima e para baixo, olha só qual é o efeito agora, eles percebem que como eu adicionei perspectiva, agora parece realmente que ele está rotacionando, por que? Essa parte que teoricamente está mais longe, ela está menor, então dá a ideia de que ele literalmente está fazendo um flip 3D, e é assim que a gente consegue rotacionar os elementos em 3D, utilizando essa propriedade de perspectiva, e a gente vai trabalhar um pouco mais também nas próximas aulas, junto com as outras propriedades de transform.

Então isso aqui é meio que um primeiro apelativo para vocês entenderem como se dá, tentem fazer esse exercício, modifiquem aqui a perspectiva para mais, para menos, para ver o que acontece, porque a perspectiva menor se adequa ao tamanho do objeto, então eu diminui aqui, ficou mais próximo do tamanho dele e eu percebi que a distância de aumento foi aumentar, certo?

Então está aí para vocês já irem testando e descobrindo, beleza galera? Até a próxima aula.
