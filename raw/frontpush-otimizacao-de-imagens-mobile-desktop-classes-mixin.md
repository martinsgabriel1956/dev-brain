# Otimização de imagens, parte 2: imagem para mobile e para desktop

Opa, fala pessoal, sejam muito bem-vindos a mais uma aula aí da parte que a gente tá falando sobre hospedagem e tudo mais. Nessa aula de agora eu queria complementar algo que eu falei, que eu esqueci de falar na aula passada, que é falar um pouquinho sobre as imagens. Lembra que a gente falou das imagens, né?

Lendo aqui, pessoal, alguns tutoriais que, inclusive, eu já deixei eles disponíveis, né, na parte de otimização de websites lá no nosso querido Notion. Se você clicar aqui nesses artigos, eles têm algumas dicas. Esse aqui passa 11 dicas, 35 dicas, 8 e por aí vai, tá? E a gente vai até falar como ter mais performance nas animações, o que a gente pode mexer para poder conseguir uma melhor performance sem perder, ou então sem capar as animações. Vamos deixar essa aula mais para o final.

## Imagens de acordo com o tamanho do dispositivo

Mas, basicamente, o que eles falam? E o próprio Google, quando a gente abre aqui o Google Page Speeds, que a gente vai começar a trabalhar com ele, entender quais são os feedbacks que ele traz para a gente, ele fala muito sobre, por exemplo, disponibilize imagens que são de acordo com o tamanho do dispositivo.

Por exemplo, existem muitas imagens que o próprio Google vai perceber que a resolução dela é grande. Por exemplo, eu estou com uma determinada imagem que tem resolução, sei lá, horizontal de 1920 por 1080. Automaticamente, pelos padrões, o Google já entende que essa resolução é mais voltada para quando você acessa o website em um desktop, em um dispositivo de tela widescreen, ou seja, horizontal. Quando você coloca essa mesma imagem no mobile, ele pode reclamar. Por quê? Porque, segundo ele, você pode fazer essa otimização.

Você pode, por exemplo, carregar uma imagem em formato horizontal para o desktop e uma imagem em formato vertical para o mobile, que seja adaptado. E, consequentemente, com uma resolução menor, porque os celulares são telinhas menores, do quais você consegue economizar o tamanho da imagem nesse sentido. Então, é muito comum a gente abrir aqui no PageSpeed Insights do próprio Google, e ele vai reclamar disso, e ele pede para poder a gente fazer essa otimização.

Como que a gente pode fazer essa otimização? Como que a gente pode fazer essa troca se você quer realmente realizar esse passo? Nem sempre eu realizo esse passo, nem sempre dá para realizar esse passo, porque depende da imagem, às vezes é interessante, às vezes não, porque às vezes dá muito trabalho fazer essa transformação para todas as imagens, de fato. Mas, se a gente for seguir a regra, e se a gente for levar literalmente ao pé da letra essa regrinha, dá para a gente fazer da seguinte forma.

## Classes desktop e mobile

Primeiro, eu criei uma classe, essa aqui é uma forma, eu vou mostrar para vocês como que eu faço para poder fazer adaptações no nosso layout quando a gente quer... Ah, eu só quero que tal imagem apareça só no desktop, ou então eu quero que essa imagem só apareça no mobile, ou vice-versa. Ou então, ah, eu quero uma determinada estrutura de ordem no desktop e eu quero uma estrutura de ordem diferente no mobile. E aí eu utilizo desse artifício aqui para poder facilitar.

Então, literalmente eu crio uma classe, está vendo aqui, chamada desktop, onde eu aplico essa classe na tag que eu quero que ela apareça somente no desktop. E ele tem como breakpoint o tamanho S, que eu deixo aqui, o tamanho S mais ou menos em... contêiner S, 620 pixels. Então, cadê? S, não, é 960. Eu deixo aqui menos que o contêiner M. Então, quando ele chega em 960 pixels, ele já quebra para o modo mobile, segundo as nossas regrinhas dessa função do mixin de responsive que a gente faz no Sass.

Ah, se eu não sei o que você está falando, não entendi. Dá uma olhadinha nas aulas de Sass, que a gente fala sobre como os mixins podem ajudar na responsividade quando a gente está construindo um website. E aqui a gente está continuando essa ideia.

Então, basicamente, eu crio essa classe aqui, chamada desktop e mobile. Basicamente, eu aplico essa classe quando eu quero que aquele determinado elemento apareça somente no desktop, ou seja, eu dou include display none, ele vai simplesmente desaparecer. E no mobile, quando eu quero o contrário, ou seja, que ele desapareça no desktop e que ele somente apareça no mobile.

Então, vamos supor que eu tenha uma determinada... Vamos supor que, sei lá, vou inventar aqui. Eu tenho um menu que ele é desktop e eu tenho um menu que ele é mobile. Então, quando eu estiver entrando em um computador de resolução horizontal maior que 960 pixels, eu quero que apareça, por exemplo, um div.menu desktop. E aí eu vou fazer toda a estilização com base nesse menu desktop. Então, aqui eu vou colocar um monte de coisa, parará, parará, parará, parará. Vou programar aqui dentro. Ah, eu quero que ele apareça somente no desktop. Então, eu faço assim, desktop. Vou lá e adiciono essa classe.

E aí eu tenho aqui um div.menu mobile. Da mesma forma, eu vou programar as coisas aqui dentro. Então, eu vou programar, programar, programar. Ah, eu quero que ele apareça somente no mobile. E aí eu venho aqui, mobile. Tá bom, pessoal?

Então, essa é uma forma que, aplicando essas classes, é uma solução genérica que dá pra fazer não só com imagens, mas também com qualquer coisa, qualquer coisa que eu estiver programando aqui.

Então, vamos supor que eu tenha uma imagem que está aqui dentro e ela está dentro lá do SVG, da pasta SVG, e que eu tenha uma imagem, sei lá, imagem drone, só que desktop. 1.jpg. E aí eu quero que essa mesma imagem seja adaptada. E aí o nome dela é mobile, por exemplo. Então, eu salvo duas imagens, uma com o caráter mais retangular, mais horizontal, e outra com o formato mais vertical. E aí eu salvo duas imagens diferentes e eu posso carregá-las dessa maneira aqui. Fazendo essa distinção por meio dessa classe.

Essa é uma solução genérica. Dá pra fazer com imagem, dá pra fazer com programação, dá pra fazer com menu, dá pra fazer com mil coisas. Tudo que estiver aqui dentro vai aparecer ou desaparecer conforme você queira.

## O mixin responsive

E a outra forma é literalmente da gente ir fazendo um mixin. Então, da mesma forma que a gente coloca aqui um responsive, vamos supor que a gente está fazendo um menu. A gente está fazendo um menu e a gente escreve aqui menu. Aqui, essa parte, ela vai ser a programação. Essa parte vai ser a programação do desktop. Tá certo?

Ah, eu quero fazer a programação específica sem mudar essa classe. Então, a gente aplica o responsive do tamanho S e aí a gente vai programar o que aqui dentro? Essa parte vai ser a programação. Vamos tirar a programação, o termo programação. Vamos colocar estilização. É melhor para poder não confundir o pessoal. Estilização do desktop e aqui vai ser a estilização do mobile.

E aqui você carrega a imagem que é do mobile e aqui em cima você carrega a imagem que é do desktop. Então, tem essas duas principais formas aí que no fundo elas são iguais, mas daquela outra forma a gente consegue generalizar para outras coisas. Então, basicamente é isso.

Eu esqueci de comentar essa parte de imagens na aula passada que, porventura, o Google reclama. Ele fala, ele consegue identificar o tamanho das imagens e falar essa imagem está mais casada ali com o desktop. Então, você está carregando uma imagem de desktop no mobile. Então, essa imagem está muito pesada para o mobile.

Às vezes você simplesmente diminui, redimensiona aquela imagem, só que ela continua pesando a mesma coisa que aquela imagem grande e que você poderia literalmente diminuir, diminuindo a resolução daquela imagem, consequentemente diminuindo o peso daquela imagem.

Então, você vai ver que muitas coisas que o Google reclama naquele PageSpeed Insights, que na próxima aula a gente vai dar uma olhada mais minuciosa do que é cada ponto, de como a gente tentar arrumar e melhorar os pontos que ele indica para a gente, muitas delas são imagens, de fato. São imagens.

Por isso que eu tinha mencionado na aula anterior que se você dominar o campo de imagens ali, se você fizer o dever de casa das imagens, eu acredito que 70% já está feito. Tem todos os outros pormenores aqui que a gente vai comentar sobre SEO, sobre práticas, sobre indexação, sobre as animações, sobre performance, sobre frames dentro de uma página que a gente está executando, que também levam em consideração a experiência do usuário. Mas com relação à performance, carregar mais rápido as imagens, elas realmente têm um papel muito grande nesse quesito. Beleza, pessoal? Falou e até a próxima aula!
