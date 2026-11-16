# As propriedades @if e @else no Sass

Opa, olá, pessoal, tudo certo com vocês? Enfim, vamos dar continuidade às nossas aulas de fundamentos e recursos principais do Sass, onde a gente está estudando, aprofundando para poder saber como funciona. Na aula de hoje, nós vamos conhecer a propriedade do if, else e operadores, são estruturas encadeadas de programação.

Como o próprio nome já grita para quem conhece a linguagem de programação, esses comandos servem para criar estruturas encadeadas. Consequentemente, quando a gente sabe utilizar isso, dá mais elasticidade aos mixins, às funções que a gente cria. Então temos a capacidade de criar cenários diferentes de estilização.

## Sintaxe: um layout light e dark

Coloquei aqui um exemplo bem simples de sintaxe e aplicação. E vamos supor que a gente quer aplicar uma estrutura dark e uma light, onde basicamente a gente precisa fazer um toggle entre a cor de background e a cor de texto, de cor clara para cor escura, e aí a gente troca os dois.

Vamos supor que eu defina uma variável chamada layout, e se eu verificar que dentro dessa variável layout tem light, ou seja, o background-color, a variável do background-color é EF, EF, EF, ou seja, um branquinho, e o text-color é 10, 10, 10, ou seja, um escala de cinza. Caso contrário, o layout é dark.

Então, se eu quiser emendar mais estruturas, mais de duas, eu posso colocar else if e emendar mais uma estrutura. E, se eu não quiser, eu simplesmente fecho com else e está tudo certo. Vamos criar isso na prática e verificar como isso funciona.

## Na prática

Então vamos lá, pessoal, vamos tentar criar uma estrutura dark do nosso texto. Vamos criar uma estrutura if else, então vou abrir aqui, if, e vou criar uma variável chamada layout. Então vamos lá, layout, e, se dentro dessa variável está escrito light, é porque a minha estrutura, a minha página vai ser light.

E eu vou definir uma variável aqui dentro chamada bg-color, da forma que eu defini lá na sintaxe, ou seja, vou deixar em 10, 10, 10, não, é EF, EF, EF, porque a estrutura é light. E o text-color eu vou deixar hashtag 1A, 1A, 1A, ou 10, 10, 10, que é um cinza mais escuro.

E aí eu vou criar a minha estrutura else, onde, como só tem estrutura light e dark, só são duas opções, eu simplesmente poderia colocar aqui a estrutura else, e ela seria a mais indicada. Mas, se eu tiver mais de duas opções, eu posso emendar com outro if aqui, e mais uma vez definir o layout igual a dark. Então vamos deixar dessa forma aqui só para podermos entender.

E vamos definir isso aqui. Podemos definir vários mixins aqui dentro, pessoal, vocês que mandam, literalmente a sua criatividade e a sua capacidade de extrair o máximo desse recurso. Então vamos lá, simplesmente inverter esses carinhas aqui, então 10, 10, 10, e aqui coloca EF, EF, EF, para quando for dark.

E aí vou definir essa variável aqui em cima, layout. Então vamos defini-la como dark em um primeiro momento. Opa, é dois pontos. Então está aí, a minha estrutura vai ser dark.

Agora eu só preciso aplicar essas variáveis no lugar certo. Então, no body, eu vou colocar aqui bg-color, vou colocar no h1 text-color, a variável, vamos lá, text-color. Vou apagar isso aqui, e aqui também no botão vou apagar, vamos apagar esse botão aqui, vamos deixar só o texto e esse carinha aqui, e aqui colocamos text-color também. Então vamos apagar esse link.

Vamos ver como ficou agora: bg-color, undefined variable. Simplesmente, pessoal, é porque eu preciso defini-las primeiro sem ser na estrutura encadeada, por mais que seja o valor padrão. Depois ele pode simplesmente modificar. Então eu vou lá, deixo aqui a estrutura padrão, seto aqui fora da estrutura, que ele reclama quando precisar entrar. Então simplesmente eu copiei e colei aqui fora, e olha só, posso mudar para dark e para light, dark, light, dark, light.

Então, com essa estrutura de if else encadeada, eu consigo construir variáveis e cenários diferentes para poder trocar literalmente as cores do meu sistema, trocar de dark para light, ou então fazer alguma modificação, tanto de padding, de espaçamento. Isso aqui vinculado aos mixins é de um resultado incrível.

## No projeto do Nubank

Vou dar aqui mais alguns exemplos. Por exemplo, vou abrir aqui a aula do Nubank, onde eu tenho na parte de tipografia, vocês podem ir lá para ver, onde eu detalho isso aqui com mais ênfase. Mas a estrutura encadeada que eu fiz aqui na tipografia foi utilizando if else e mixins, vocês podem estar observando com mais detalhes lá no projeto.

Mas vou explicar para vocês uma aplicação. Eu criei um mixin de typefaces de tipografia, ou seja, typeface 1 é mais voltada para títulos, utilizando a font-family Sora, e a typeface 2 é voltada para corpo de texto, utilizando o font-family Source Sans Pro. E eu utilizo dois parâmetros, o tamanho e o dispositivo, sendo que o dispositivo padrão é desktop.

E eu simplesmente seto o tamanho do que eu quero, sendo que esse tamanho é pré-definido: ou ele é h1, ou h2, ou h3, ou h4, ou h5, sendo o h1 o maior deles e o h5 o menor deles. E os devices, ou é desktop ou é mobile. E eu seto essas características aqui no mixin e coloco uma estrutura encadeada aqui dentro, onde vai modificar o font-size e o line-height de acordo com a opção que colocar. E eu fiz essa estrutura tanto para typeface 1, tanto para typeface 2.

E, quando eu vou estabelecendo os h1, eu dou um include de typeface 1, porque h1 é de título. Então, portanto, h1, seto o tamanho h1 e desktop. E eu faço um outro mixin de responsividade, assim como aquele que eu tinha já citado na parte de mixins, falo para ele o tamanho, que é small, de um tamanho específico que eu coloquei, e também coloco typeface 1, só que agora tamanho mobile. E eu faço isso para todos, h1, h2, h3, h4, h5.

E isso facilita demais, porque basta eu modificar alguma coisa aqui que automaticamente toda a minha estrutura textual vai ser modificada automaticamente.

E a parte de responsividade, que aqui em layout eu criei esse mixin, onde eu entro com os tamanhos dos dispositivos, onde eu coloco xl, l, m, s e xs, meio que é do inglês, extra large, large, medium, small, extra small: aqui para resoluções acima de 1440, aqui entre 1140 e 1440, entre 960 e 1140, menor que 960 e menor que 540.

Então, olha só, mais uma vez eu criei um mixin com uma estrutura encadeada aqui dentro, utilizando o content. Então, desde que elas sejam combinadas, isso aqui é de um poder inimaginável. Eu demonstro com mais ênfase e mudou lá no projeto, então não deixe de conferir para você saber como eu implementei isso em projetos reais utilizando os recursos que acabamos de conhecer aqui.

No mais é isso. Não deixem de praticar isso aqui e criar as suas estruturas encadeadas com if else no Sass também, dando maior poder para ele. Então, só deixa eu voltar aqui, open folder, na nossa aulinha de Sass, e ver a forma de como ele está cuspindo o CSS bonitinho, já todo estilizado da forma que a gente precisa para o browser ler. Então, no mais é isso, pessoal, falou e até a próxima.
