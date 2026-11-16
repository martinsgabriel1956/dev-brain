# Classes e IDs no CSS

Então, galera, continuando aí, a gente já viu na aula passada como é que a gente aplica o CSS. Tem três formas e o mais utilizado, que a gente vai mais utilizar, esse externo, é literalmente quando a gente cria um arquivo .css e a gente faz o uso da tag link para poder linkar o nosso HTML ao CSS escolhido, quando a gente consegue escalar esse estilo e ter menos trabalho, menos retrabalho quando a gente estiver trabalhando com estilos.

Você vai ver que isso aqui é muito importante quando a gente está trabalhando com páginas, principalmente para poder a gente manter a organização e a consistência, beleza?

## Classe e ID: a diferença

Está certo, vamos supor então que a gente está aqui, vamos voltar aqui para o nosso código e agora a gente vai começar a falar um pouquinho sobre classes e IDs, que meio que são tags, se é que eu posso dizer assim. São tags para a gente criar os nossos próprios estilos e essas tags são amplamente utilizadas para poder a gente pegar um elemento específico, tratar um elemento específico. Então esse conceito aqui é de suma, suma, suma importância para vocês entenderem, porque a gente vai utilizar tanto em CSS como em JavaScript, que é meio que um gancho para poder a gente aplicar tudo e qualquer coisa, função, estilo, diversas coisas.

E a gente vai ver a diferença entre eles. Meio que eles funcionam de uma mesma forma, só que a semântica deles é diferente. O ID, pelo próprio nome, você consegue entender o quê? É uma tag que identifica aquela própria específica tag. É como se fosse o seu CPF: o seu CPF é só seu, não existe uma outra pessoa com seu CPF. Então o ID tem essa mesma intenção.

Qual é o seu ID? O seu ID é o seu CPF, o seu ID é o seu RG, o seu ID é o seu passaporte. Então eu consigo identificar quem é você pelo número do seu passaporte, pelo número do seu CPF e pelo número do seu RG. A tag ID carrega essa mesma semântica, então, por carregar essa semântica, eu tenho que aplicar apenas uma tag onde eu consigo identificar ela, certo?

Enquanto a classe, também a própria palavra já indica a semântica do negócio, que ela pode ser aplicada para várias tags. Então, se eu quero criar um estilo para aplicar em várias tags, eu crio uma classe; se eu quero uma ID de uma tag específica da página, eu vou colocar o ID. E para poder retomar ela, é sempre o jogo da velha ou cerquilha, e a classe é o ponto.

## Estilos por tag

Então vamos aqui demonstrar na prática como é que a gente aplica isso. Vamos criar aqui alguma hierarquia, então eu vou clicar aqui h1, onde eu vou colocar título. h1 é o título da minha página. O h2, eu vou criar aqui um h2, h2 eu vou colocar aqui como subtítulo. O h3 vai ser subsubtítulo. O parágrafo vai ser o meu corpo de texto, então vamos lá, corpo de texto. Beleza, acabei de criar aqui e já está funcionando.

Eu vou apagar esse estilo aqui e a gente vai ficar somente no estilo externo, para poder a gente editar e começar a se acostumar com esse estilo aqui. Calma que vocês vão entender por que eu fiz isso aqui. Primeiro eu tenho que explicar esse seletor aqui, o que ele significa, mas de antemão ele está dizendo que aplica a tudo, a todas as tags que existem lá. O asterisco aplica isso aqui, ou seja, eles vão iniciar com o margin zerado, com o padding zerado e a caixa no estilo border box. Esses conceitos aqui eu vou explicar nas próximas aulas, se acalmem, vamos um pouquinho mais com calma aqui.

Primeira coisa que eu quero aplicar: se é para tudo, eu posso aplicar um font-family, porque eu não gosto muito de fonte serifada, gosto sem serifa. Então eu venho aqui, sans-serif, para poder ela ficar retinha, beleza.

Primeira coisa que eu quero definir é por tags. Então eu posso muito bem aplicar estilos para h1, para h2, utilizando as próprias tags, h1, h2, h3, onde eu quero aplicar para o meu h1 a cor de maior contraste. Então vamos supor que eu aplique um branco. A cor de h2, ela também merece um destaque legal, mas eu vou colocar um cinza um pouquinho mais clarinho, CCC. Aqui no color ele está abaixo, então eu vou colocar um cinza um pouco mais escuro, então 555. h3, deixa eu ver aqui, deu errado, está aqui, porque não apliquei aqui a tag direito. h3 está aí. E aqui eu vou criar, aplicar no corpo de texto uma cor mais escura ainda, então vou colocar aqui por volta de hashtag 333, para poder a gente enxergar. Está aí, no escala de cinza.

## Classes para os botões

E o que acontece? Vamos supor que eu quero aplicar em um link, então eu vou criar aqui um link, onde eu vou fazer aqui um botão de call to action, então button. E aí eu quero que esse link eu possa aplicar em vários pontos do meu site, vários pontos do meu site. Então, para ele, eu vou criar uma classe para poder estilizar, porque você concorda comigo que a minha página pode ter vários links. Então, se eu fizer aqui e estilizar a tag de link, vamos supor que eu coloque o text-decoration none, e deixe a color hashtag FFF, branco também, está aqui o meu link, está vendo, no button. Mas eu tenho diversos links na minha página: eu tenho link de botão, eu tenho link que é só sublinhado. Então como é que eu vou fazer essa distinção?

Aí eu vou criar uma classe para o meu botão, chamada btn. Isso aqui é qualquer nome, é tipo uma tag, uma flag que você anuncia para o sistema. Então poderia muito bem colocar "esse aqui é meu botão", só que sem acento e sem espaço, porque quando você coloca espaço, ele identifica que isso aqui é outra classe. Então meio que eu posso aplicar btn, e se eu quiser aplicar outra classe, para deixar ele verde, eu coloco assim, btn-green, e eu vou emendando um monte de classes aqui. Então não pode dar espaço: sempre a classe, faça tudo minúsculo, sem espaço, para poder funcionar.

Então eu vou criar o estilo do btn aqui, vamos lá, .btn. A gente sabe que, se vocês não sabem, fique sabendo, o link sempre vem como display inline. O que significa isso, Násser? O display inline é toda e qualquer propriedade que é de texto, que não é de caixa. Aí vocês vão entender um pouco mais quando a gente for falar de box model, então até lá se acalme. Então display block, a gente vai tratar disso aí. Aí eu deixo ele como display block para poder virar uma caixinha, e eu vou colocar uma borda, uma borda de dois pixels, solid red, só para eu ver se está funcionando no meu btn.

Deixa eu salvar aqui, está aí, então está começando a funcionar, está vendo? Então eu estou aplicando o estilo a esse botão. E vamos supor que eu quero criar um link secundário. Lembra lá no meu, na parte de UI, quem sabe, eu tenho sempre um botão primário e um botão secundário. Então vamos supor que eu queira aplicar aqui btn-secondary, e aqui btn-primary, e eu vou aplicar essas duas classes.

Eu venho aqui, faço btn-primary, onde geralmente esse carinha aqui tem um background-color, onde eu posso aplicar o meu verdinho, 5f36a. Consequentemente a cor dele tem que ser 1a, para poder causar um contraste legal. A gente está começando a entender. A gente vai fixar o tamanho dele, então eu vou colocar um width de 320 pixels e um height de 50 pixels, 56 pixels, para poder ilustrar isso. Para poder deixar ele totalmente alinhado, vamos colocar um text-align center, para poder o texto ficar devidamente alinhado. Calma que a gente vai estilizar. Vamos colocar uma bordinha, border-radius de 16 pixels.

E agora eu vou começar a estilizar o meu outro botão, que é o botão secundário, então btn-secondary, onde eu vou aplicar justamente as mesmas cores, só que o background-color dele, eu quero que ele seja transparente e que a cor dele seja branca, para poder a gente enxergar. Então ele está mais ou menos da mesma estrutura, só que a borda dele, eu quero ele com uma borda para poder enxergar o contorno do botão, então 2px solid 5fe360, que é o verde que eu utilizo nos meus projetos.

Então você percebe que eu estou criando um estilo, e aí eu utilizo a class, e aí eu posso aplicar para várias tags lá embaixo. Vamos supor que eu tenha outro botão lá embaixo, outro botão lá embaixo, outro botão lá embaixo: eu só copio e colo, ele sai replicando para mim. E se eu mudar em um lugar, vamos supor que eu mude para vermelho, vai ficar bem bizarro, é só para poder ilustrar, olha só, ele aplicou justamente para todos. Então é essa ideia que eu quero passar para vocês.

## ID para um botão específico

E essa mesmíssima ideia você aplica ao ID, só que o ID você não aplica a class, você vai aplicar assim: ID é igual o quê? Botão btn-checkout, que é um botão maior. Então você quer dar mais ênfase e fazer esse botão aqui diferente, ele é específico, porque você quer ativar algum tipo de função. Aí você vai lá, aplica um ID, vem aqui e, ao invés de aplicar class, coloca aqui btn-checkout. Como ele é um checkout, ele vai ter mais ou menos as mesmas características, só que ele vai ser maior, então eu vou deixar ele com 520, e aqui é 120, então o tamanho dele vai ser maior, e a cor dele também vai ser azul. Então olha só, ele meio que aplicou o estilo aqui do meu botão exagerado, para vocês entenderem.

E eu não posso aplicar outra tag com esse ID, porque esse ID identifica justamente esse botão. Se você colocar um ID, vai dar conflito e pode prejudicar o funcionamento do seu site. Está vendo que ele não vai ter erro, porque o HTML e o CSS são linguagens onde o browser interpreta o que você digitou, então é o que ele está interpretando, mas ele não dá nenhum warning. Talvez no console, quando você abrir, então vem aqui em inspecionar, talvez ele dê algum erro, mas como não tem nenhuma função atrelada, ele não vai apresentar exatamente nada.

Beleza, galera, então falou, até a próxima.
