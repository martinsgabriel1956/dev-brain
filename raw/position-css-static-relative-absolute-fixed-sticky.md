# Position no CSS: static, relative, absolute, fixed e sticky

Então, pessoal, agora nós vamos começar a parte do CSS básico, que é um CSS básico que muita gente não sabe e a gente vai tentar desvendar da melhor forma possível como é que funciona o tal do position.

É um tipo de posicionamento para poder a gente construir os layouts que as características dele podem nos ajudar a construir determinadas seções com funcionalidades legais que não utilize, por exemplo, apenas o flexbox ou o grid layout. Então, vamos entender de uma vez por todas o que significa esses carinhas aqui.

Com relação a isso, eu vou apagar tudo que a gente fez. Tem alguns links que eu também vou deixar para vocês entenderem como está aí, mas acredito que a minha explicação vai clarear o máximo possível, vou tentar.

## Preparando o exemplo

Primeira coisa, eu quero apagar tudo aqui, vamos lá, apagar tudo, tudo que a gente fez, tudo que a gente escreveu até agora. Vamos deixar aí.

Nós vamos criar aqui uma div, vamos lá. Então, nós vamos criar aqui uma section para poder ficar um pouco mais interessante na questão da semântica, onde o nome dela eu vou chamar, eu vou colocar nela uma classe chamada box, e aqui dentro eu vou criar um div com o nome de item, item 1, e eu vou colocar aqui item 2. Então, dois elementos para poder a gente estilizar e entender como é que se dá aqui o negócio.

Primeira coisa é que eu quero utilizar a box, então vamos lá. Vou utilizar aqui o body, vou forçar que a minha body tenha 100% de largura e 100% de viewport unit.

Olha, se eu não sei o que é viewport unit, isso aqui são unidades, já vou aproveitar aqui para explicar, são unidades com relação ao tamanho da tela. Deixa eu dar um background color aqui para vocês entenderem da melhor forma possível. Vamos lá, vamos lá.

O que eu estou dizendo? Olha, não tem a minha tag body, essa aqui, estilize ela para mim de forma que ela complete 100% na largura e 100% de viewport unit na altura. O que isso significa? Significa que 100% das unidades de altura da minha tela.

Por que surgiram essas medidas? Porque hoje em dia nós temos vários dispositivos e a gente quer construir interfaces responsivas. Eu posso muito bem colocar VW para poder ficar do tamanho da minha largura também, só que eu sei que não vão enxergar nada e eu vou colocar essas propriedades no box para vocês entenderem melhor, mas deixa cem VH porque ele vai estar sempre fullscreen na tela inteira.

Vamos lá, vamos aplicar aqui nessa box, vou aplicar uma borda de 5 pixels solid white para poder a gente enxergar. Vou definir um width de 500 pixels e um height de 500 pixels. Vamos enxergar o nosso quadradinho. Vamos começar a entender como ele funciona.

Eu vou aplicar um flexbox bem simples que vocês não precisam entender ainda para o que serve, a gente vai tratar isso só na seção de flexbox, mas eu vou deixar sempre esse quadrado alinhado ao centro. E o que eu faço? Eu aplico um display flex no meu body, então a minha seção quando eu aplico isso já se tornou um flex item, mas como só tem um não tem problema nenhum, vou dar um justify-content center para poder alinhar de maneira horizontal no center e dou um align-items center para poder centralizar na forma vertical e ele vai ficar sempre centralizado, independente do tamanho da tela.

E agora a gente vai começar a estilizar aquelas boxes, item 1, onde eu vou colocar também uma bordinha e um background-color neles, onde eu vou colocar uma caixinha de 100 pixels para poder a gente visualizar e a primeira caixinha eu vou dar um background-color red e a segunda caixinha eu vou dar um background-color purple. Um background blue, para a gente diferenciar as duas caixinhas.

## Position static

Então agora a gente vai começar a entender como é que funciona o position. Primeira coisa, vamos lá, se eu definir aqui um position static, vamos ver se muda alguma coisa, então position static, tanto em um como no outro. Não mudou exatamente nada, por quê? Porque o position static é o quê? É simplesmente quando o elemento é apresentado na hierarquia que ele é apresentado no documento, então meio que já é o padrão, então por isso que vocês não viram nenhuma modificação.

Esse position static já é padrão de todo e qualquer elemento quando você coloca, então cabe a nós ver as diferenças do fixed, do absolute, do relative e do sticky, que eu até esqueci de colocar aqui, mas eu vou complementar aqui na aula.

## Position relative

Então vamos lá, vamos agora entender então o relative, vamos ver o que muda, opa, não mudou absolutamente nada, então vamos colocar aqui o relative aqui embaixo, beleza, não mudou nada também. O que acontece? O relative, ele tem como o próprio nome já denuncia isso, ele fala que é uma posição relativa, mas é uma posição relativa em relação a ele mesmo.

Vamos supor que está aqui o elemento em vermelho e vamos supor que tem um tracejado, então vou deixar aqui um elemento em vermelho, um border, um px, que é dashed para poder ficar pontilhado, white, então olha só, o meu quadradinho ficou pontilhado, imagine que ele vai continuar aqui e só a parte vermelha vai sair, imagine isso. Essa aqui é a posição original do item 1, concorda comigo?

Então o relative é sempre com relação à posição original e aí eu posso modificar essa posição com o top para a distância de cima, com o left para a distância da esquerda, com o bottom para a distância de baixo e o right para a distância à direita.

Então se eu colocar um top de 100 pixels, olha só o que vai acontecer, ele desceu justamente e ficou atrás do azul, então deixa eu baixar 200px, está aí, se eu baixar 250px, então ele está baixando com relação à essa posição original dele aqui. Você percebe que quando eu baixei 200px, ele ficou exatamente embaixo do outro quadradinho que está em média de 100px, então ele desceu 100px, 100px e parou justamente aqui. Então qual é a posição relativa que ele está fazendo? Com relação à posição original, ou seja, onde ele estava quando eu deixei top 0, 0, 0, então se eu deixar top 0, left 0, ele vai ficar exatamente onde ele está.

Se eu aplicar o left de 50px, ele vai afastar 50px com relação à sua posição original e eu posso também colocar a posição em porcentagem que vai ficar meio que responsivo, mas como a posição inicial é fixa porque está dentro de um quadrado que é fixo, ela vai ficar fixa, mas o porcentagem também é uma medida relativa, então esse é o lance do position relative.

É relativo à posição original dele, então é interessante a gente tratar desse carinha aqui, porque a gente pode fazer uma transição de estado, porque eu posso muito bem colocar aqui um valor negativo muito grande, vamos por menos mil pixels, meio que o nosso quadradinho vai sumir, porque ele vai passar aqui da tela, então ele está meio que aqui e você não está enxergando. E se eu colocar um estado de hover, ou então um clique para aparecer um menu, e aí eu vou lá e zero esse valor e ele volta para cá, eu colocando um transition, dá um efeito legal, que é o mesmo efeito que eu apliquei lá no meu menu mobile responsivo que eu fiz lá no meu canal do YouTube, se quiser dar uma olhada lá. Eu utilizo dessa artimanha aqui para poder fazer ele aparecer e desaparecer, eu utilizo do position.

## Position absolute

Por fim, vamos ver como é que funciona o position absolute, vamos lá ver agora o que acontece com o position absolute, para onde ele foi, enfim, meio que ele está aqui debaixo, o azul, então se eu dar um display none e fazer o item dois desaparecer, ele está bem aqui, mas por que o relative, que é o azul, ele subiu do nada só porque eu coloquei aqui absolute?

O que é o absolute? Ele está, a distância dele é medida com relação ao elemento pai e o elemento pai que é relative é o body, então se eu colocar, por exemplo, bottom zero, onde ele vai aparecer? Ele vai aparecer aqui na parte de fora, porque por padrão do HTML, sabe quem é o position relative? O pai dele é o body.

Então olha, eu coloquei aqui position relative, não mudou exatamente nada, agora pode ver que o próprio azul já desapareceu, dentro dessa tag é um elemento pai e eu vou torná-la relative, ou seja, eu dei uma nova posição para poder ele se realocar, então meio que agora a referência que eu tenho é essa minha caixa. Como eu coloquei bottom zero, ele está com a distância de bottom zero, se eu colocar agora right zero, você vai ver que ele vai colar na direita, o que agora ele está relacionado com relação, desculpe as minhas gafes, mas presta atenção no conteúdo, ele está tendo agora a div box como referência.

Então é assim que funciona o position absolute, ele sempre olha para o elemento pai que tem o position relative para poder definir essas distâncias, então da mesma forma você pode colocar top zero, vamos supor, left 100%, ele vai colar na parte de fora, porque sempre é essa parte que ele tem como relação, então é isso o position absolute.

## Position fixed

Por fim, não, mas finalizando, vamos ver como é que funciona o position fixed. Então pelo próprio nome, o que a gente consegue deduzir do position fixed? É que ele é sempre fixo, deixa eu tirar o position relative dele, ele é fixo e depende, vamos supor que eu deixe ele top zero, olha só, hoje o meu português está maravilhoso, e ele sempre é com relação à sua tela, ele não está nem por position relative, está vendo? Eu coloquei o position relative no elemento pai, que é o box, e ele não veio para cá, ficou tipo fixo nesse elemento aqui, ele só olha para a sua tela, essa é a única referência do position fixed.

Então se eu colocar top zero, ele vai ficar fixo aqui por mais que eu tenha scroll no mouse, então deixa eu aumentar aqui a div box para 2000 de altura, olha só, criei um scroll e pasmem, eu estou rolando aqui, deixa eu colocar aqui algum texto só para vocês entenderem, vou colocar aqui Lorem Ipsum, não está aparecendo, cadê o texto, cadê o texto, Brasil, onde é que eu coloquei o texto, enfim, mas vocês conseguem entender, não sei por que está aparecendo o texto, mas o que acontece, independente do scroll, ele já está fixo bem aqui. Então o position fixed é muito utilizado para menus, e por mais que você role o scroll do mouse, ele se mantém fixo em alguma parte que você queira.

## Position sticky

Por fim, eu tenho o position sticky, que ele é muito legal, meio que é uma funcionalidade que antes só era implementada com o JavaScript e agora é possível de implementar só com o CSS. Vamos tentar fazer aqui algum exemplo para vocês entenderem, vamos supor que eu tenha uma tag nav, vou deixar aqui a tag nav, e dentro dessa tag nav eu quero fazer uma lista, e eu vou colocar alguns li, e eu coloquei ul porque eu quero uma lista não ordenada, só com pontinhos. Então vamos supor que eu estou construindo aqui um site, então aqui vem produtos, aqui na parte de baixo é sobre, e aqui contato, vamos lá, e aqui contato, está certo, vamos ver como ele se comporta agora.

Vou apagar esses dois itens aqui, e primeiro eu quero utilizar a minha ul, eu quero utilizar ela, e eu quero um background um pouco mais claro, eu coloco o CCC para eu enxergar, ele está bem aqui, deixa eu tirar esse position relative daqui, beleza, eu só vou tirar essa section, porque ela está me atrapalhando por causa do display flex, está aqui, está aí a minha lista. Deixa eu colocar um texto aqui muito grande só para poder a gente ter algum tipo de scroll, deixa eu mostrar para vocês, vamos lá, eu vou tirar esse display flex aqui para poder facilitar a minha vida, deixar ele em bloco mesmo, um debaixo do outro, e eu vou colocar esse parágrafo aqui.

Vamos estilizar ele de forma que ele tenha uma altura muito grande e ele seja fino, então coloque 1000 pixels, 2000 pixels de altura, coloque um width pequeno de 300 pixels, um border, um px, solid white, deixa eu enxergar ele, já criou um scroll, e vamos colocar um color, hashtag CCC para a gente enxergar o que está escrito, beleza, e aqui está o nosso menu. E olha só, eu vou dar um outro espaço de texto aqui em cima, com parágrafo eu vou dar com span, simplesmente para ter um espacinho ali em cima também, está vendo, tem um espaço aqui em cima.

E agora eu apliquei o position sticky nessa minha tag nav aqui, vou vir aqui, tag nav, e vou aplicar para ela um position sticky, sticky, e vou forçar que ela fique no top zero, vamos ver se mudou alguma coisa. Olha só, a princípio não mudou nada, nós temos aqui um texto aqui em cima, a propósito eu vou mudar para poder vocês enxergarem, span, com color, hashtag CCC para vocês entenderem, está aqui, olha só o que acontece. Então meio que quando eu quero deixar ele em position sticky, na parte de cima, e ele transita para o modo fixed, então olha só, quando eu vou descendo aqui o scroll, ele continua fixo, independente, então meio que ele faz a transição do position sticky para o position fixed.

Então isso aqui é uma aulinha para poder vocês entenderem um pouco mais, não deixem de ler e procurar mais referências, mas acredito que é uma boa explicação para vocês entenderem como é que se dá o processo, beleza, galera? Até a próxima.
