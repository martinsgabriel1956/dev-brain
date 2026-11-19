# Cache e CDN: CSS e JavaScript inline, incorporado e externo

Opa! Fala pessoal, sejam muito bem-vindos aí à nossa segunda aula de otimização, onde na primeira aula, justamente, a gente falou sobre a importância de a gente saber utilizar agora a aba Network, né, aqui no nosso console. Ele vai nos auxiliar e a gente entender muito dos processos de requisição que acontecem dentro das nossas aplicações, dos nossos websites. Quase que não sai.

Falei sobre o PageSpeed Insights do Google, que a gente vai utilizar ele como relatório para poder saber onde atacar as melhores otimizações e tudo mais. E falei na aula passada sobre a importância de você minificar e tentar colocar tudo em um arquivo só, principalmente CSS, se possível JavaScript, porque é mais barato, em questão de performance, em questão de requisição, você fazer poucos arquivos, até maiores, do que muitos arquivos menores, quando a gente está fazendo essa requisição, tá?

## Por que isso não se aplica ao web app

Por que que isso não se aplica, pessoal, ao Web App? Por que que isso não se aplica ao Web App? Você tem que lembrar o seguinte, o que o Web App faz? Que é um SPA. Qual que é a grande vantagem de um SPA, né? De ela ser reativa. O que que é ela ser reativa? Eu não precisar fazer o reload da minha página de uma forma inteira para poder atualizar algum componente. Vocês lembram disso? Lá da parte de React?

Então, basicamente, qual que era uma das defasagens do PHP? Da tecnologia do PHP. Ah, eu quero atualizar alguma coisa, eu tenho que colocar ou um botão para poder atualizar a página, para poder fazer essa atualização, ou eu tinha que forçar ele ir e voltar em uma determinada página para poder forçar o reload dessa página.

Hoje em dia, se o próprio componente percebeu que ele atualizou, que ele tem um novo valor para apresentar, ele próprio atualiza, segundo o Web App e os seus princípios de reatividade. Então, o que que ele faz? Ele tem uma virtual DOM, ele tem uma árvore de elementos de DOM virtual, compara e vê o que que mudou. Está sempre comparando e vendo. Ah, mudou isso aqui, então carrega só esse elemento em específico. Pelo fato do Web App carregar esse elemento em específico, faz com que ele próprio tenha esse tipo de otimização e a gente não precise se preocupar tanto.

Você pode ver que quando a gente utiliza o próprio styled-components, cada componente tem o seu respectivo CSS, não é? Então, o CSS, quando a gente constrói um Web App, ele tem várias tecnologias, ele tem vários recursos, que o CSS lá é quebrado. E o CSS quebrado lá é mais vantajoso. E aqui, quando a gente está falando de uma página normal em requisições, já é ao contrário. Entendeu? Então é bom a gente pontuar aí essa diferença antes da gente começar. Quer dizer, continuar. Beleza?

## Evite o CSS e JS incorporado e inline

Então, vamos voltar aqui para o nosso postzinho. A gente já falou sobre a minificação de arquivos CSS e JavaScript. Então, sempre quando você for... Ah, vou pegar aqui alguma biblioteca... Sempre vai ter a versão minificada e você prefira ela para poder, literalmente, diminuir o tamanho dessa requisição. Se vocês verem lá nas nossas aulinhas do Barba.js, que também já estão disponíveis, vocês podem ver que é um dos pontos que eles mais destacam nas features do programa, que já é uma biblioteca compactada que pesa 7K ou 9K. Então, é bem levinho.

Evite o CSS e JS incorporado e inline. Nossa, o que é isso? Vamos relembrar lá. Então, se a gente for aqui, pessoal, na nossa página HTML, lembre-se que tem como a gente fazer o CSS, a gente tem como escrever o CSS de três formas, né?

Primeira forma, como é que eu escrevo o CSS? Posso escrever ele inline. O que é inline? É, literalmente, eu vim aqui na tag, digitar style e colocar, por exemplo, background-color: red. Quando eu estou aplicando aqui um CSS, mas ele está sendo no modo inline, ele está sendo aplicado somente nesta tag e ele tem uma prioridade maior do que o CSS incorporado ou o vinculado, tá? Evite utilizar isso aqui.

Segundo ponto, qual que é o outro tipo de CSS? É justamente o incorporado, em que a gente cria aqui a tag style, a gente cria aqui uma tag style e coloca aqui type="text/css", correto? Então, quando a gente faz essa declaração aqui, a gente vai escrever o CSS aqui normal. Então, nós vamos pegar aqui, por exemplo, uma tag container e vamos escrever aqui, né? max-width: 1280 e a gente vai escrever aqui o nosso CSS normal. Também não indico fazer isso aqui, né?

A gente vai ver que esse tipo de abordagem é muito comum quando você tem geradores de código, principalmente quando a gente fala aí do mercado digital, que isso aí eu vejo demais. Por isso que as páginas talvez elas fiquem muito lentas, porque, por exemplo, ah, eu quero fazer, eu quero vincular a minha página com o ActiveCampaign, que é uma ferramenta de email marketing, aí ele precisa me mandar um formulário e aí eu clico lá, gerar código. Quando ele gera o código, ele tem que gerar um código uniforme para você, ou seja, em uma página só. E aí o CSS e o JavaScript, ele vai vir incorporado ou vai vir inline.

E aí eu sempre digo que se você tiver o acúmulo muito disso na sua página, se você não fazer limpar literalmente isso daí, sua página pode ficar mais lenta por conta disso. Principalmente quando a gente fala de, sei lá, WordPress, PageBuilder, em que vai acumulando esse lixo de código e faz com que ele fique mais lento.

## O cache do navegador

Násser, por que não é vantajoso de fato? Porque, olha só, por padrão, os arquivos CSS e JS são armazenados em cache pelo browser do usuário. Ou seja, quando eu tenho um arquivo .js ou quando eu tenho um arquivo .css, que ele é feito por meio de um link, chamando pelo script ou pelo tag link, que é a forma que eu costumeiramente faço, é literalmente eu ter um script aqui, chamando um arquivo externo. Eu ter um link aqui, chamando um arquivo externo.

Eu consigo falar para o browser, a próxima vez que você visitar o meu site, pode guardar esse arquivo no seu cache, para poder ficar mais fácil. Você não precisa recarregar ele novamente. Então o próprio browser faz o download, ele deixa em cache esse seu arquivo para poder, quando a próxima vez que você for entrar, ele não precisar carregar mais esse arquivo. Então o próprio browser faz essa otimização.

Quando você utiliza CSS inline ou incorporado, ele não consegue fazer isso. Porque está na própria página do HTML. E a página do HTML é para conteúdo. Ou seja, o browser sempre vai ler de novo. Ele sempre vai ler de novo, sempre vai ler de novo. Então é interessante.

Você pode ver que isso aqui é tão verdade que às vezes você está em um determinado site, você modifica o .css dele, você sobe e quando você dá um F5, às vezes ele não funciona. Você tem que fazer um hard refresh para o browser carregar tudo de novo, de forma obrigatória. Para poder você verificar algumas features a mais que você implementou, de forma visual. Tá bom? Então é isso.

Terceiro ponto. Sempre otimize os PNGs e JPGs. Mas, além disso, eu vou falar sobre o WebP. Beleza? E aí para poder a gente deixar as aulas mais organizadinhas, eu vou falar disso aí na próxima aula.

## CDN ou arquivo local

Mas, para poder complementar essa aula aqui, falando sobre arquivos externos, é interessante eu falar sobre o famigerado CDN. Na C, eu tenho uma determinada biblioteca, por exemplo, a GSAP. Eu tenho aqui a GSAP, tá vendo? E, eu tô vendo que você tá fazendo o carregamento dela via CDN.

Então, se eu te expliquei esse lance de tipo: "Ah, Násser, se você falou pra mim que é bom você deixar arquivos JS ou JavaScript de forma local para poder o próprio browser armazenar em cache e disponibilizar isso de forma mais rápida porque, afinal, vai estar no cliente essa parada. Por que você colocou CDN aí no GSAP, no ScrollTrigger? Por que você não fez o download dessas duas bibliotecas e não colocou aí de forma local?", tá? Então, esse é um ponto muitíssimo interessante. Tá bom? Porque o que acontece? Vamos lá. Tem alguns pontos para poder a gente comentar sobre isso.

Primeira coisa, o fator atualização. Quando você tá com uma biblioteca do tipo GSAP, do tipo ScrollTrigger ela tá sempre tendo constantes atualizações. Concorda comigo? Já tá na 3.10.4 isso aqui quando eu fiz esse site. Se a gente for aqui no CDN então vamos abrir aqui, ó vamos colocar aqui CDN GSAP, só pra poder a gente ver. Pra eu conseguir provar isso aqui pra vocês. Olha só, já tá na 3.12.2 e aqui nós estamos na 3.10.4.

Então, é bom que as nossas bibliotecas elas sempre estejam atualizadas, concorda comigo? Porque tem uma uma comunidade muito grande, tem sempre pessoas trabalhando em cima daquilo ali, tem sempre atualizações que podem ser bem-vindas atualizações de performance, de novos recursos piriri para lá, por aí vai.

É lógico que a gente tem que fazer aquele teste, aquele famigerado teste e eu nunca pego, por exemplo, a versão beta eu já pego uma versão ali que tá nem muito desatualizada, nem a última que saiu, pra poder a gente ter uma certa estabilidade, porque pode acontecer mas, a questão é se você for atualizar a sua determinada aplicação pra poder eu trocar a versão aqui do GSAP e colocar uma versão mais nova, o que eu tenho que fazer? A gente só trocar o link. É só eu trocar aqui o nome de 3.10.4 pra 3.12.2. Então é muito mais fácil fazer uma atualização desse biblioteca. Agora, se eu for baixar, eu tenho que ir lá copiar, ir no arquivo substituir, subir pra lá. Primeiro ponto, esse é o primeiro ponto facilidade na atualização.

Segundo ponto, quando você vai carregar o site pela primeira vez pra pessoa é interessantíssimo que nessa primeira vez, ele seja muito bem otimizado. Por que, Násser? Porque, o que acontece? Esse cache, ele é interessante? É! Ele é interessante, mas o CDN, ele funciona como se fosse servidores que eles podem ter uma localização geográfica, que pra carregar pro seu usuário é mais rápido ele sair de um servidor que está perto dele, do que sair do seu servidor que está lá em São Paulo, por exemplo.

Vamos supor. Vamos supor aqui, vamos colocar nome nos bois pra poder vocês entenderem. Vamos supor que uma pessoa do Acre, nada contra os acreanos. Acho que não é acreano, né? Enfim, uma pessoa que mora no Acre, ela fez uma requisição lá do seu site. O seu site ele está lá em São Paulo, concorda comigo? E aí, é lógico que quando você faz uma determinada requisição leva um tempo pra poder essa requisição ser completada, pra poder literalmente fazer o download do arquivo de São Paulo pro Acre. Mas vamos supor que existe um servidor CDN lá no Pará. Ok? Lá no Pará. E aí o que dura mais? Eu fazer um download de um arquivo de São Paulo ou do Pará? É do Pará, né?

Mas você não pode estar pensando só em nível Brasil. Você não pode estar pensando só em nível Brasil. Porque o CDN ele é mundial. Você entendeu? Então vamos supor que outra pessoa lá do outro lado do mundo, quando você pega a relação de requisições quando uma pessoa que está fora do seu país faz uma requisição existem mais endereços e mais lugares que ela tem que percorrer. Muito mais. Entendeu?

Então quando a gente fala de algumas requisições que estão perto aqui, talvez até faça sentido você colocar em cache, colocar de forma local. Mas pra poder você estar meio que blindado de qualquer pessoa acessar de qualquer lugar e ter um desempenho muito parecido porque o CDN ele pode disponibilizar pra pessoa esse arquivo no servidor mais próximo a ela de forma geográfica, meio que fica elas por elas. Entendeu?

Então o que eu faço? Eu literalmente deixo... É... Em cache, literalmente o arquivo que eu fiz porque que eu digitei não tem como. E deixo essas bibliotecas assim... no CDN. É... Porque meio que fica elas por elas. E às vezes o CDN fica até melhor... Então CDN ela conhece mais efetivo quando a gente fala de forma generalizada. Talvez uma pessoa aqui do lado que esteja no Brasil, então que esteja perto, pode até fazer diferença para ela, entendeu? Mas quando a gente fala de, sei lá, homogeneidade com relação a acesso em qualquer tipo de lugar, em qualquer inóspito lugar, o CDN é bem interessante também, tá? Porque ele vai fazer a requisição desse arquivo aqui nos servidores deles, fechou?

Outra coisa que você pode ter vantagem no CDN, vocês concordam comigo que o CDN, por ser um site extremamente famoso e utilizado para poder hospedar muitas bibliotecas desse tipo, ele tem espelhamento de banco de dados, ele tem recorrência, se cair um servidor tem outro, eles têm espelhamento, então, qualquer tipo de palcd, vocês podem ter certeza que esse link aqui não cai, já do seu servidor lá, dependendo, se caiu já era, entendeu?

Então, pessoal, ele é um pouquinho mais confiável nesse sentido, então você pode ver que existem vantagens e desvantagens, você tem que colocar aí na balança, mas é assim que eu costumo fazer quando a gente fala com relação ao CDN, beleza?

Então é isso, pessoal, vamos deixar aqui para comentar sobre performance um pouquinho mais na próxima aula, que eu vou explicando mais alguns pontos para vocês, e até a próxima.
