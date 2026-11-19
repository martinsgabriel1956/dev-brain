# Introdução à otimização de páginas web e minificação de CSS e JavaScript

Opa! Fala pessoal, sejam muito bem-vindos aí a mais um módulo onde, no módulo de agora, nós vamos falar sobre otimização de páginas web. O que significa isso, Násser?

Então, basicamente, é como se eu fizesse a analogia de uma casa e a gente estivesse na fase de acabamento. A gente vai conferir os aspectos de carregamento da página, os posicionamentos do CSS, como é que a gente deve estruturar o CSS para poder ter o melhor carregamento possível, como é que a gente vai estruturar o JavaScript para poder a gente ter o melhor carregamento possível, quais são as diferenças de você carregar um web app e uma página normal, porque tem diferença de otimização nesses quesitos, como é que a gente faz a otimização de imagens, o que mais impacta na performance de uma página, como é que a gente estabelece carregamento sob demanda.

Consequentemente, quando a gente faz todos esses passos, a gente melhora o indexamento em motores de busca, como do Google, melhora o SEO, e a gente vai aprender, nesses próximos módulos, a poder analisar todos esses pontos.

Então, deixa eu compartilhar aqui a minha tela, para poder a gente começar. Em que, basicamente, pessoal, eu gostaria que vocês abrissem um Notion, um Notion do FrontPUSH 3.0, que nós já estamos em atualizações do FrontPUSH 3.0, e vocês vão vir aqui na parte de links úteis front-end, vocês vão procurar por otimização de websites, está aqui. Então, tem os sites para poder medir desempenho, e alguns artigos que eu já deixei abertos, para poder a gente estar analisando os principais pontos e explicando eles para vocês.

Para poder a gente também relembrar os velhos tempos, vocês lembram desse post aqui? Basicamente, nesse post, eu separei sete dicas para você melhorar a performance dos seus websites. Nós vamos citar essas sete dicas, num primeiro momento, mas eu vou aprofundar bem mais nessas questões, além de citar outros quesitos.

## Minifique arquivos CSS e JavaScript

Vamos lá. Minifique arquivos CSS e JavaScript. Minimização é o processo de remoção de caracteres desnecessários, tais como tabulações, espaços, comentários, códigos fontes, para poder reduzir o tamanho do arquivo, literalmente.

Então, pessoal, o que acontece? Eu vou abrir aqui uma página, que é uma página, por exemplo, que eu fiz recente, que é de uma empresa de energia solar. Eu fiz aqui, eu já praticamente entreguei, tá em nasausef.com.br.sosten

Vou aumentar aqui o zoom para vocês verem. Vocês podem ver que ela ficou com um desempenho muito interessante. Desempenho de 97%, acessibilidade de 90%, práticas recomendadas 95% e 100% SEO.

Então, é justamente isso que a gente vai bater na tecla, do que significam o FCP, o First Contentful Paint para o Google, o INP, o TTFB. A gente vai analisar, conforme for passando as aulas, tá? Eu vou dividir essas explicações em aulas específicas, para poder não ficar muito grande essa aula aqui.

Mas, basicamente, o Google vai melhor indexar a sua página de acordo com a experiência do usuário. Então, você pode ver aqui, relatório do UX, do Chrome, e tem a ver com o próprio desempenho da página, com aparecer o primeiro conteúdo, ele ser interagível nos primeiros segundos, não demorar muito. Tem boas práticas, tem a melhor indexação, para o Google, literalmente, conseguir copiar bem o seu site. Interessante a gente falar sobre isso, HTML semântico, mas vamos chegar lá, tá? E na parte do celular também, 92, 90, 95 e 100.

Mas, o que eu queria mostrar não é isso, pessoal. Basicamente, se você vir aqui, clicar com o botão direito e vir em Inspecionar, é interessante a gente vir aqui na aba de Network, tá? Quando você clicar aqui na aba de Network, nós vamos aprofundar bastante aqui nessa aba do console, para poder a gente descobrir algumas coisas, para poder a gente, literalmente, conseguir aprofundar um pouco mais. Eu vou até deixar aqui a tela completa, para poder melhorar aí a visualização de vocês.

Mas, basicamente, vocês podem ver que está sendo feito aqui um carregamento sobre demanda, tá vendo? 6, 7, png, tá vendo? E olha que eu não fiz todas as otimizações, tá bom?

Mas, o mais interessante é a gente vir aqui, marcar essa caixinha de Disable Cache e dar um F5, tá? Quando a gente faz isso, nós vamos conseguir simular como se fosse um site aberto pela primeira vez. O que significa isso? Ele ser aberto pela primeira vez? Que ele, literalmente, teve que carregar todos os arquivos que estavam indexados, para poder o site funcionar de maneira completa, né?

Vocês podem ver que os primeiros arquivos que a gente tem aqui, são os arquivos de CSS, os arquivos de JavaScript, que a gente, literalmente, coloca ali no header, no cabeçalho da nossa página, para poder ele carregar.

E aí, pessoal, tem aqui Size, tá vendo aqui? Size e Tempo. Então, é só a gente levar em consideração a própria física do negócio. Dá para a gente fazer aqui um pequeno paralelo da física. Cara, se eu estou carregando algo que é menos pesado, o tempo para poder fazer esse processo vai ser melhor. De eu carregá-lo de um lugar para o outro vai ser mais fácil.

Então, de forma bem intuitiva, quando a gente vem aqui e minifica os seus arquivos CSS e JavaScript, basta você vir aqui no próprio Google, tá vendo? Eu vim aqui no Google, coloquei minificar CSS e JavaScript, por exemplo. Vai aparecer diversos sites, você pode utilizar um interessante, que ele, literalmente, vai pegar o nosso arquivo aqui, CSS, cadê? Esse style.css aqui, vocês vão perceber que ele é cheio de espaços. Então, cheio de espaços.

Esses espaços aqui, quando a gente fala com relação ao arquivo, se a gente tirar todos esses espaços e deixar tudo em uma linha só, o nosso arquivo vai diminuir de tamanho. Isso vale tanto para o JavaScript como para o CSS.

De forma nenhuma, essa prática é válida quando você ainda está com o site em produção. Quer dizer, quando você está com o site ainda em desenvolvimento, quando ele ainda não foi para a produção. Então, quando você está programando, de fato, é interessante que você não faça isso, porque a leitura fica muito ruim, né? Quem é que aguenta ficar editando CSS em uma linha só?

E tem o artifício do Sass, que você pode, literalmente, utilizar o Sass, assim, normalmente, com todos os espaçamentos, todas as tabulações que a gente faz para poder entender o código da melhor forma possível, mas ele sempre cospe esse CSS de forma única. E a gente já vai falar por que a gente utiliza o CSS de forma única também, tá?

E aí, se você pegar só esse CSS aqui e minificar ele tanto, isso para o JavaScript, poxa, já vai melhorar aí o tamanho dos arquivos, tá?

## Web app e página normal

Segundo ponto que eu quero comentar, Násser, é porque utilizar, por exemplo, o CSS em uma página única, ela é melhor para o carregamento da página, para a otimização de performance da página.

E aí, o que eu tenho para falar para vocês? Existem diferenças do web app para uma página normal. Por que eu vou focar mais na página normal? Porque quando a gente fala da página normal, a gente tem que fazer mais otimizações do que em um web app.

O próprio web app, um React da vida, um Vue.js, como ele faz a Single Page Application, a SPA, ele que monta aquilo ali, ele que faz a virtual DOM, ele que compara o que mudou da virtual DOM para DOM, e aí ele modifica somente o necessário, ele próprio faz muita otimização de performance. Então, meio que a gente não precisa se preocupar.

Quando a gente está construindo aqui uma página, web assim, HTML, CSS, JavaScript, padrãozinho, para poder funcionar como uma landing page, a gente tem que se preocupar com mais coisas. Por isso que eu vou focar mais nisso, porque no web app você vai ter que se preocupar menos. Nem tudo que eu vou falar aqui vai se aplicar, e aí eu vou pontuando.

## Um arquivo maior em vez de vários pequenos

Mas, quando a gente está fazendo uma determinada requisição, deixa eu voltar para cá, vocês podem ver que a requisição do site, ela não é feita de maneira, como se diz, paralela. Todos os arquivos não são carregados de uma só vez.

Quando o browser faz o carregamento da sua página, primeiro, ele já tem a inteligência para poder carregar a sua página sem quebrar. O que é carregar a sua página sem quebrar? Ele vai dar prioridade para o style.css, para o JavaScript, para poder já carregar a forma do seu site bonitinho. Para não carregar aquele site todo quebrado, e aí ele vai montando conforme você vai mexendo nele. Então, ele tenta montar isso da melhor forma possível.

E você pode ver que ele pega uma determinada demanda, é como se ele fosse um caminhãozinho, tá bom, pessoal? De forma didática e um pouco mais palpável para vocês entenderem, quando um browser está carregando, ele tem, por exemplo, um limite de carga. É como se fosse um caminhão. Ah, o meu caminhão aqui, para poder fazer a primeira ida e a primeira volta dessas requisições, nesse pacote, ele só cabe, sei lá, 10 requisições. Estou chutando aqui um exemplo. Dessas 10 requisições, ah, vamos supor que eu terminei uma, sobrou uma vaga, ele faz outra. Sobrou uma vaga, ele faz outra.

Se eu vim aqui e, por exemplo, dar um refresh novamente, você vai ver... Deixa eu dar aqui o refresh. Olha só, você viu? Está certo que está sendo rápido, porque tem algumas coisas bem leves que ele carrega muito rápido, mas ele carrega uma coisa, depois vai outra, depois vai outra, e aí você tem aqui meio que a linha do tempo de como ele carrega isso, tá?

Então, você vai perceber que ele esperou primeiro esses aqui, depois veio esses, e aí ele vai meio que dando uma linha do tempo. Você está vendo que esses aqui, ícone build, SVG, eles vieram depois no tempo, você está vendo? Esse aqui, eles estão bem coladinhos nessa parte, e aqui eles estão mais afastados, tá?

E aí, pelo fato dessa característica, pelo browser ter essa característica de primeiro fazer a requisição desses primeiros, acredite em mim, eu já fiz alguns testes, é mais barato para o browser ele ter um arquivo um pouco maior, entendeu? E ele fazer uma requisição do que fazer várias requisições de arquivos pequenos.

Por que eu falo isso? Porque, por exemplo, quando a gente está aqui no nosso querido Sass, você pode ver que a gente tem um arquivo para acordeon, um arquivo para animações, um arquivo para backgrounds, um arquivo para botões, e assim vai, para tipografia, para layout. Então, para a nossa organização, é maravilhoso a gente ter vários arquivos CSS. Um só para layout, um só para tipografia, um só para cores, um só para botões, e assim vai. Porque para poder a gente se localizar quando a gente está desenvolvendo, fica mais fácil.

E por que eu sempre falo para a gente montar todos esses arquivos menores dentro de um style só, e aí ele cospe tudo em um style só? Justamente por esse objetivo. Então, a gente já estava fazendo otimização de CSS desde o começo, e vocês não percebiam.

É por esse motivo que, por exemplo, se você for lá no Bootstrap, se você vir aqui, Bootstrap, vamos lá, www.google.com.br, se a gente for lá em Bootstrap 5, Bootstrap 5, você vai ver que quando a gente vem aqui em introduction e download, você vai ver que, olha só, compilado e minificado CSS bundles. Compilado e minificado JavaScript plugins.

E quando você faz, você vincula o Bootstrap na sua página, quando você faz a vinculação do seu Bootstrap na sua página, olha só que interessante, ele vai como um único arquivo Bootstrap minificado. Ou seja, essa estratégia, ela é utilizada pelos maiores Bootstrap, pelo poptwin e tudo mais, é um único arquivo bootstrap.js e um único arquivo bootstrap.css, com tudo lá dentro.

Por quê? Para a otimização, é mais barato para o browser eu ter um arquivo maior de, por exemplo, vamos chutar aqui, eu ter, por exemplo, um arquivo de 50K, tudo junto em um arquivo só, do que eu ter 5 arquivos de 10K sendo carregados. Então, para a otimização, ele lê mais rápido, ele lê tudo de uma vez, ele lê todo o seu conteúdo ali da sua página de uma vez e evita, melhora a experiência do usuário, porque ele carregou tudo de uma vez naquele arquivo.

Então, evite ao máximo ter muitos arquivos soltos. Quantos arquivos JavaScript você tem solto aí? Você está vendo aqui que está carregando o Swiper, o minificado também, está carregando o SVGInject, está carregando o GSAP, está carregando o ScrollTrigger e está carregando o app.js. Está vendo? Então, são 1, 2, 3, 4, 5, 6, 6, 6 arquivos JavaScript e 2 arquivos CSS. Um que vem do Google, que é a tipografia, e outro que são os locais.

Ah, Násser, quando é que eu devo utilizar CDN ou arquivo local? O que é melhor para mim? Isso a gente vai ver na próxima aula, tá? Nessa primeira aula, eu só queria explicar, dar a introdução e já começar a falar sobre como minificar esses arquivos e o porquê que isso é interessante para performance. Beleza, pessoal? Então, falou e até a próxima.
