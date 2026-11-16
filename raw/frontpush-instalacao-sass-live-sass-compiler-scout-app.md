# Instalação do Sass: Live Sass Compiler e Scout-App

Então, pessoal, vamos dar continuidade às nossas aulas de Sass, onde na aula de hoje eu vou falar para vocês duas formas de instalar o Sass no nosso computador.

A primeira forma é utilizando o próprio VS Code, o nosso editor que eu estou sempre utilizando aqui nas nossas aulas. Caso você queira aprender a como configurar inicialmente ou até instalar o Visual Studio Code, procure lá nas aulas introdutórias do próprio Script F, para você ter uma noção, e é o que eu vou utilizar.

"Ah, Násser, por que você vai utilizar no próprio VS Code?" Porque ele me traz a comodidade de já ter um plugin pronto que compile o Sass, e eu tenho tudo no próprio Visual Studio, então eu faço toda a gerência sem utilizar aplicativos externos, o que eu acho que facilita a minha vida.

Porém, teve alguns alunos que tiveram problemas com o plugin do Visual Studio Code, não estavam conseguindo rodar nas suas respectivas máquinas, e eu não sei exatamente o porquê, mas para poder resolver esse problema, eu também vou ensiná-los outros aplicativos, e um deles é o Scout-App. Ele é free e é multiplataforma, e por esses motivos eu escolhi ele para poder a gente estar aprendendo aqui.

## Linha de comando ou aplicativos

Então, sem mais delongas, vamos aqui no site do Sass. Esse aqui é o site do Sass, então olha só, "CSS with superpowers", o seu CSS com superpoderes, onde você pode vir aqui na parte de install e aprender um pouco mais das opções que o próprio CSS e o site dele dão de opções, tá bom?

Então, tem a opção de linha de comando, pessoal, e de aplicativos, aplicações. E aí o que acontece? Eu escolhi ensinar para vocês por meio de aplicativos, porque linha de comando talvez exija de vocês um conhecimento prévio maior, então você precisa saber um pouco de linha de comando de Linux, de fato, e depende se tem variações de se você está utilizando o Windows, ou o próprio Linux, ou o próprio Mac. Então isso fez com que a logística aqui fosse um pouquinho maior. Mas também não é nenhum bicho de sete cabeças fazer por linha de comando, mas com certeza é mais simples a gente partir para algum tipo de aplicação que tenha interface gráfica e facilite o nosso entendimento.

Então, olha só, nós temos o CodeKit, ele é pago para Mac, tem o Ghostlab, ele também é pago para Mac e Windows, o Hammer, o LiveReload e esses dois aqui, tá bom, pessoal? O Scout-App é free e open source, tem para Windows, Linux e Mac, então foi por isso que eu escolhi ele.

Mas também tem esse Prepros aqui, que também é uma opção interessante, que ele tem a opção, enquanto carrega aqui, de, por exemplo, você utilizar o recurso sem precisar pagar, mas ele sempre vai ter um pop-up falando assim, "pague", não sei o quê, entendeu? E por esse motivo eu escolhi o Scout-App, tá bom?

Então, olha só, quando ele abre aqui, "download free unlimited trial", então é available para Windows, Mac e Linux, então você também pode estar utilizando e testando esse aqui. E ele também tem suporte para Sass, para Less e para outros pré-processadores também, inclusive também tem algumas funções de JavaScript.

Mas aqui nós temos o Scout-App, onde nós vamos estar utilizando, para poder baixar, tá bom, pessoal? Eu já baixei, basta você vir aqui e selecionar a opção do seu sistema operacional, beleza?

## Live Sass Compiler no VS Code

Então, primeiro eu vou explicar como é feito no Visual Studio Code. Vou abrir aqui um novo arquivo de uma pastinha chamada SassAula, que eu já havia criado, onde nós vamos testar como roda o Sass direto no VS Code, que é a forma de como eu vou estar utilizando.

E aqui é muito simples, você basta vir aqui em extensions, em extensões ou plugins do próprio VS Code, e aí você vai procurar, pessoal, por esse plugin aqui, Live Sass Compiler, tá bom? Esse olhinho aqui. Então basta digitar Live Sass Compiler aqui, que você vai utilizar, que você vai achar, aliás, e aí instale e habilite esse carinha aqui.

Ele é muitíssimo importante e é uma das minhas plugins ou extensões do VS Code que eu não consigo viver sem, porque ele traz dois recursos muito interessantes. O primeiro recurso, pessoal, é que ele tem a opção de você abrir uma live, onde, quando você modifica o seu HTML e salva ele, automaticamente ele cria um servidorzinho em localhost, e aí, quando você salva, ele automaticamente modifica e atualiza o seu browser para você ver as modificações em tempo real, tá bom?

E ele também traz o recurso de ter o Sass e CSS Compiler. Então, por meio dele também tem essa opção, onde, para você habilitar e falar assim "pode compilar o Sass", vai ter um botãozinho com esse olhinho bem aqui, é onde você vai clicar nele, em Watch Sass, tá?

Antes de a gente começar, vamos criar uma paginazinha, sem mais delongas, um index.html, HTML5, deixa eu aumentar o zoom. E olha só, Open with Live Server: quando você instalar essa extensão, vai abrir essa opção para você, onde, pessoal, literalmente eu tenho a opção de abrir no browser por meio de um servidorzinho na porta 5500 em localhost e fazer as modificações. Então, se eu escrever qualquer coisa e simplesmente salvar, ele já aparece aqui automaticamente, tá bom?

Então, vamos lá, vou criar uma pastinha chamada CSS e aqui dentro eu vou criar um novo arquivo chamado style.scss, tá bom? Então, você percebe que ele já identificou esse arquivo como um arquivo Sass, tá bom, pessoal? Onde a gente pode simplesmente fazer a nossa programação por aqui.

Então eu posso estilizar primeiro tirando o padding, tiro o margin dos nossos elementos, a gente coloca o box-sizing border-box. A gente vem aqui e estiliza o body para que ele sempre tenha o tamanho da tela cheia, a gente coloca um background-color, hashtag, 0c, 0c, 0c, tá bom? E a gente pode também colocar um display flex, justify-content center, para todo e qualquer elemento ele sempre fique centralizado, e uma align-items center também. Além disso, eu quero estilizar o meu h1 com o color white, tá bom?

Então, quando eu salvo isso aqui, pessoal, você percebe que não aconteceu absolutamente nada. Por quê? Primeiro, eu não linquei e não gerei o arquivo CSS. Lembrando mais uma vez, o Sass não é compilado, ele não é lido pelo browser, ele é um meio de campo onde ele gera o CSS mais otimizado, onde a gente pode programar com as skills de Sass aqui dentro e ele já cospe o CSS devidamente otimizado, tá bom? E com as skills tudo estabelecido bem bonitinho, além de notificar quando tiver algum erro, tá bom, pessoal? Isso aqui é um outro detalhe muito interessante.

Então, para poder rodar, de fato, eu simplesmente vim aqui em Watch Sass e ele já está rodando. Você percebe que ele já gerou um CSS aqui, está vendo? Ele gerou dois arquivos: é um map, onde tem as configurações que você pode estar utilizando, vou falar dele posteriormente, mas olha só, ele gerou um CSS já otimizado com os traços webkit, com o traço ms, para poder melhorar a compatibilidade com browsers antigos.

E olha só o arquivo CSS puro que ele gerou, que é o arquivo que, de fato, nós vamos linkar no nosso arquivo, está vendo? Você percebe que é CSS, não é Sass, que a gente linka. E olha só, nós temos aqui ele estilizado, onde a gente pode escrever o nosso h1, "hello world com CSS ou Sass", vocês já entenderam aí. Então, já está devidamente funcionando aqui no nosso VS Code, tá bom?

## Scout-App

Agora, eu vou mostrar para vocês como se dá com o Scout-App. Basta você baixar e extrair, por exemplo, na sua pastinha. Eu coloquei aqui, WinScout-App, eu extraí na pasta C: do meu Windows, onde você pode extrair e abrir o seu arquivo, está bom?

Para poder utilizar ele e não ter conflito, eu vou parar aqui o plugin do próprio VS Code, vou fechar e vou excluir esses dois arquivos aqui, então, delete, para poder a gente fazer com o Scout-App, está bom?

SassAula, já selecionei, e tem sempre o input folder e output folder. Pode ser a mesma pasta, onde a pasta é o CSS, mas você pode muito bem ir lá no seu arquivo, criar uma pasta .scss e outra pasta só CSS, isso não impede você de nada. Então, posso muito bem vir aqui, criar uma pastinha chamada .scss, onde ele vai compilar o que tiver nesse carinha aqui e vai compilar o CSS aqui dentro. Também é uma forma de você estar se organizando.

Então, eu venho aqui, delete, ele até criou uma pastinha já personalizada para a gente. Então, eu venho aqui, new file, style.scss, ele já criou lá para mim, e eu seleciono: input folder, eu venho aqui no SassAula, CSS, e output folder, ele pegou automático, CSS aqui.

Então, ele já me dá as opções em desenvolvimento ou em produção, e ele me dá, pessoal, as opções de expandido ou, quando eu tiver em produção, em compressed. Ou seja, quando eu compilo ele, ele já tira os enters, as quebras de linha, os espaços, fazendo com que o seu CSS já seja cuspido de maneira otimizada com relação ao tamanho. Então, outra função muito legal.

Então, uma vez que você escolheu aqui, pessoal, basta você vir aqui e dar play. Deu play, ele já está rodando. Se você vir aqui no CSS, você vai perceber que ele já gerou um arquivo aqui, e basta você digitar aqui os mesmos comandos que a gente tinha feito.

Então, vem aqui: padding 0, margin 0, box-sizing border-box. Vamos abrir aqui, deixar ele aqui do lado para a gente estar acompanhando. A gente escreve aqui o body, vamos deixar aqui um width de 100%, um height de 100px, as mesmas configurações, background-color, hashtag 0c, 0c, 0c, e vamos colocar aqui o h1 com color white. Se eu salvar isso aqui, automaticamente ele compilou para mim, se ela perceber que o CSS que está sendo cuspido já está sendo feito também de maneira correta. Vamos lá, justify-content center, align-items center, já compilou tudo certinho também utilizando aqui.

Eu já quero ver a versão comprimida, compressed. Então, vocês vêm aqui, dá um pause, muda aqui para compressed, dá o play de novo, e olha só como ele cuspiu o arquivo CSS devidamente otimizado para você já colocar em produção. Isso aqui faz com que o arquivo fique bem menor, melhorando o tempo de requisição, porque tem um arquivo menor. Então, muito interessante para a gente estar utilizando, beleza, pessoal?

Então, essas aqui são as duas formas de a gente estar utilizando o Sass para a gente começar os nossos projetos, beleza? Então, falou, galera, até a próxima.
