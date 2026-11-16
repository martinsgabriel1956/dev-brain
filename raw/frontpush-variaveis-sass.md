# Variáveis no Sass

Olá, pessoal, tudo certo com vocês? Enfim, vamos dar continuidade aos fundamentos e principais recursos do Sass, onde, na aula de hoje, a gente vai conhecer um pouco de variáveis. Por mais que eu já tenha apresentado esse recurso nas aulas passadas de maneira indireta, vou dar um pouco mais de ênfase no poder que esse pequeno recurso, que aparenta ser pequeno, agiliza e dá maior produtividade no nosso CSS, na nossa programação CSS.

Então, variáveis, como o próprio nome já diz, permite a criação de variáveis: cores, componentes, propriedades do CSS e etc. Isso faz com que, primeiro, ajude na organização e na consistência no design. Então, isso tem importância infinita para quem quer ter maior fidelidade quando passar o layout para a codificação.

E também pode ser utilizado para propriedades de CSS, não só para cores, porque literalmente é um copia e cola. Então, o que estiver dentro dessa variável, se você copiar e colar no lugar certo no seu CSS, vai funcionar perfeitamente. Eu vou demonstrar isso aqui para vocês.

Então, como é que se declara uma variável no Sass? Simplesmente você define aqui um dólar, como se fosse em PHP, em PHP também utiliza o dólar para declaração de variáveis, você escreve a sua string, dois pontos, e aqui coloca o valor da variável. E, como eu disse para vocês, serve tanto para cores como também para outras propriedades, e eu vou demonstrar para vocês.

## Consistência e style guide

E, para que vocês entendam da maneira mais plena possível, eu preciso que vocês entendam um pouquinho de UI Design, e eu vou dar uma palinha aqui com o style guide. Por exemplo, nós temos aqui o Nubank, o style guide do Nubank. Ele tem toda uma documentação, e uma das coisas mais fundamentais no design é ter consistência.

O que significa ter consistência? É que a mesma cor é aplicada ao longo do meu projeto. Então, eu não posso, no meu projeto, por exemplo, pegar aqui um roxo, esse roxo que eu defini, eu defini esse roxo aqui como a minha cor. E aí, quando eu estiver colocando, eu esqueci a cor e eu faço uma determinada modificação aqui na matiz dela. Aí eu pego um roxo desse aqui, e eu começo a trabalhar com esse roxo. E aí, ao longo da minha interface, eu trabalho com tons diferentes de roxo.

Lembrando que esse aqui está na mesma matiz, é variação de cor, mas aqui eu estou modificando a matiz. Pode ver que a matiz dele, se eu vir aqui no modo HSB, está em 277. Esse aqui está em 286.

E aí, quando eu não tenho variáveis guardando esses valores, para que seja sempre a mesma cor sendo utilizada, ou o mesmo efeito, ou mesmo o box-shadow, para ter consistência ao longo do meu design, faz com que eu perca a qualidade. Eu perca na transição, na implementação do meu layout, que é meio que um pecado no design eu ficar fugindo da paleta de cores ou então da padronização que foi estabelecida aqui no style guide.

Você percebe que temos cores primárias, cores secundárias, cores auxiliares, cores brancas e pretas para composição de texto, cores em escala de cinza para poder estabelecer hierarquia textual, gradientes e tudo mais. Vocês vão perceber que, ao longo do meu style guide, está tudo documentado, as determinadas cores com seus hexadecimais.

Se eu estabelecer isso dentro de variáveis e só utilizar a variável, primeira coisa, se tiver alguma modificação, basta eu modificar a variável e ele vai modificar ao longo do meu documento inteiro. Vai facilitar a minha produtividade. E, assim como a gente faz com cores, a gente também pode aplicar em tipografia.

Como eu disse, também tem como aplicar as propriedades de CSS. Quando você clica em Inspect, você vai ver as características do CSS, como, por exemplo, font-family, que é a Montserrat, font-style, font-weight, que é o peso, o tipográfico, o tamanho, o line-height e etc. Tudo isso são variáveis que a gente pode também estar aplicando. E até aqui está errado, não é Montserrat, é Sora.

E você percebe que os tamanhos dos H1, dos títulos, dos corpos de texto do body, B1, B2, B3, ou então H1, H2, H3, são todos padronizados, tem características em cada um deles. Então, eu consigo estabelecer isso mais facilmente por meio de variáveis.

Da mesma maneira são botões. Vamos supor que, no meio do desenvolvimento, eu acredite que esse botão, o designer acabou de me mandar uma modificação, ou então você mesmo é o designer e fala assim: "eu achei esse box-shadow muito agressivo, então eu queria diminuir a opacidade dele". Então, você simplesmente vem aqui no box-shadow e modifica o opacity. Em vez de 0.8, você pode colocar 0.3, e etc., para poder modificar isso tudo por meio de variáveis.

## Demonstração: o botão

Sem mais delongas, vamos lá para demonstrar isso aqui para vocês. Por mais que esse recurso eu já tenha demonstrado de maneira indireta nas aulas passadas, eu vou aqui enfatizar. Então, estabeleça o branco, o preto, o cinza e etc. Posso colocar aqui hashtag 555 e ele vai modificar automaticamente para mim.

E vamos supor que eu queira criar um botão. Então, eu vou criar um link com essa classe link, onde eu vou estilizar ele aqui. Vou vir aqui no body, vou colocar flex-direction column para poder esse link aparecer aqui embaixo. Então, posso criar aqui um botão. Está aí o botão. E vou utilizar essa classe de link aqui.

Vou dar um text-decoration none para poder tirar o sublinhado. Vou dar um font-size de 18 pixels. Vamos colocar um pouquinho mais, 24 pixels. Vou dar um color para ele, já utilizando a cor, as variáveis das cores. Então, posso colocar aqui branco, e ele vai ficar branco.

Vou criar aqui uma outra cor, o próprio roxo que acabamos de ver, do nosso projetinho do Nubank. Então, posso pegar esse roxo daqui, vou pegar esse hexadecimal, hashtag, vou colocar aqui para poder a gente estar utilizando ele. Vou colocar aqui background-color, um roxo.

Vamos dar um padding de 8 pixels em cima e embaixo, 16 de um lado e de outro. Beleza, vamos definir ele aqui como display inline-block, para poder virar o elemento de caixa, para poder eu otimizar ele. Vamos colocar aqui um pequeno border-radius de 16 pixels, não, de 8 pixels, aliás. Vamos colocar aqui uma margem, para poder não ficar colado lá no elemento, então eu posso colocar aqui um margin-top, um margin-top de 24 pixels.

Então, está aí o nosso pequeno botãozinho, pessoal. Vou dar aqui um padding um pouquinho maior, vamos colocar 16 e 24. Vamos colocar 12. Então, vamos lá, está aí o nosso botãozinho, já está tomando forma.

## Uma variável de sombra

E aí, eu posso colocar, por exemplo, propriedades de sombra. Então, vamos supor que eu tenha que colocar um elemento hover nesse link, onde ele cresça um box-shadow, indicando que isso é um elemento clicável, para poder melhorar a experiência do usuário.

Eu posso clicar muito bem aqui e criar um novo arquivo chamado shadows. shadows.scss, onde aqui eu posso criar uma variável chamada box-shadow purple, vou colocar agora em black, box-shadow purple, onde eu posso vir aqui no meu Figma, pegar essas características aqui desse botão. Está vendo que ele tem um box-shadow bem fraquinho? Mas eu vou criar um outro aqui utilizando o plugin Smooth Shadow. Vou mostrar para vocês.

Então, vou pegar aqui esse hexadecimal, vamos lá, e vou vir aqui nos plugins e vou vir no Smooth Shadow, vamos lá.

Então, pessoal, agora abriu, desculpe a demora, mas olha só: vou aplicar aqui nesse botão, colocar a cor roxinha. Esse aqui é um princípio também de design, que é sempre bom utilizar as sombras da mesma cor do elemento, está bom? Porque deixa as minhas sombras mais realistas.

Então, olha só, se a gente der um zoom aqui, se a gente der um zoom no elemento, vamos lá, deixa eu abrir aqui novamente, ele já criou um drop shadow aqui, bem fraquinho, está vendo? Onde a gente pode estar modificando aqui, vamos lá, aumentando ou diminuindo a quantidade de layers, está vendo? De camadas, literalmente. Posso modificar aqui o alpha, e aí eu vou deixar o alpha bem alto, só para vocês perceberem. Quando você quiser fazer algum tipo de modificação, o tanto que colocar em variáveis facilita. E vou aqui aumentar o blur, está vendo?

Então, vamos deixar essa estrutura aqui, bem exagerado mesmo, colocaria bem mais sutil em projetos reais. Está vendo? Box-shadow. Então eu simplesmente apago isso aqui e deixo somente as características. Então aqui, box-shadow purple.

Eu posso vir aqui no meu arquivo, vou dar um import desse arquivo chamado shadows, e aí eu posso aplicar essa variável aqui dentro do elemento hover. Então eu vim aqui dentro do elemento hover, vou aplicar um box-shadow, onde, na variável, eu vou colocar o nome dessa variável que eu criei, box-shadow purple, e apliquei.

Ele deu um pequeno errinho aqui. É porque eu coloquei o shadows sem o nosso querido underline aqui, para poder ele fazer tudo isso em um só, e aqui esses dois eu vou deletar, vamos lá, recycle bin. Então, olha só, o Sass também tem esse recurso de mostrar para nós os erros que a gente cometeu no meio do processo. Vou salvar aqui, já deu um sucesso, e olha só, quando eu aperto aqui, ele já está fazendo esse efeito.

Basta colocar aqui um transition, um transition de 0.5 segundos, para que essa transição seja suave. Então é isso, transition. Então está aí.

Agora, e quando eu quiser modificar? Que no caso eu faria uma sombra mais sutil, que foi esse o caso. Então, se eu vir aqui, eu quero deixar ela mais sutil, então vou diminuir o alpha, deixar ela bem de leve, talvez diminuir aqui, não, deixar o offset no mesmo lugar, e deixar ela bem mais leve, dessa forma aqui.

Eu basta vir aqui em Inspect, mais uma vez, eu copio essa seção aqui, Ctrl C, venho aqui no meus shadows e substituo aqui, substituo, salvo. E, quando eu vir aqui, você vai ver que a sombra está mais sutil. No preto aqui não ficou muito legal, mas eu queria demonstrar para vocês que é possível também aplicar em outras questões que não sejam somente a cor, tá bom? Também utilizando o recurso do import aqui, beleza, galera? Então, falou, até a próxima.
