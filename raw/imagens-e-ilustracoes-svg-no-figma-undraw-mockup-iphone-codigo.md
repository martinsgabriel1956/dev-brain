# Imagens e ilustrações: como funciona o SVG no Figma (unDraw, mockup de iPhone e o código do SVG)

Então, pessoal, mais uma aula sobre ilustrações, só que nessa aula a gente vai conversar um pouco mais de como funciona o SVG no Figma.

## Isometria nos wireframes

Então, vamos voltar aqui novamente, onde a gente tinha discutido um pouco sobre como construir essas imagens em perspectiva, em isometria, que, a propósito, eu utilizei aqui nos meus wireframes, então basicamente é fazer a mesma coisa que eu fiz ali, só que posicionando todos os elementos com algum gradiente linear embaixo, mas é utilizando aquele mesmo princípio, aplicando alguns efeitos de sombra com contraste legal e seleção de cores legal para poder construir esses wireframes aqui, da mesmíssima forma que eu fiz esse aqui, só que acredito que eu fiz esse aqui usando o skill-that, fechou?

## SVG do unDraw no Figma

Então, vamos voltar aqui e comentar um pouco sobre unDraw, lembra esse site aqui de ilustrações? Ele é muito legal porque tem como eu pegar essas ilustrações em modo de SVG, então eu consigo fazer o download via SVG, então eu venho aqui em mostrar na pasta, dessa mesma forma eu posso vir aqui, clicar e arrastar e trazer aqui para o Figma e a gente vai ver como é que trabalha ele.

Deixa eu baixar aqui algumas outras ilustrações que eu acredito que é legal da gente estar trabalhando, então vamos pôr essa ilustração aqui, download SVG, da mesma forma, mostrar na pasta.

E olha só gente, o tanto que ele é leve, vocês estão vendo aqui, 9KB, então é uma ilustração que eu considero legal para a gente aplicar e pesa apenas 9KB, então ele já vem embutido no modo frame, e o que é legal é justamente isso aqui, você percebe que é tudo editável, então quando você baixa em modo SVG, eu posso vir aqui e mudar totalmente a cor, posso vir aqui e colocar um roxo, então todos os elementos são editáveis, eu posso vir aqui, copiar, colar, está vendo?

Então essa é a grande vantagem de utilizar SVG, além de ser leve, você pode trazer aqui para o Figma e simplesmente editar tudo, ou então pegar apenas trechos para poder você formar as suas próprias ilustrações, então o unDraw é um site que eu gosto muito justamente por isso, ele oferece um download vasto de ilustrações, onde você pode mudar a cor e trazer aqui para o Figma.

## Construindo um mockup de iPhone com formas

E o grande pulo do gato, galera, é porque você percebe que isso aqui são todas formas, você concorda comigo? Isso aqui é uma forma, simplesmente ele veio e construiu essa ilustração, então a gente pode muito bem construir a nossa ilustração, por exemplo, eu tenho aqui na parte de style guide um iPhone de mockup, então se a gente copiar ele e colar, então Ctrl-C, Ctrl-V, foi só isso que eu fiz, e vir aqui e aplicar um preenchimento, vou colocar aqui o preenchimento meio padrão, 1A, só para a gente visualizar, você percebe que isso aqui é um conjunto de formas que eu consigo fazer no Figma, assim como essa ilustração.

Ora, então se eu construir uma ilustração aqui no Figma, eu vou conseguir exportar em SVG exatamente, e vai ficar exatamente dessa forma, então como é que eu fiz esse iPhone aqui? Literalmente eu fui lá, peguei algum mockup de alguém, ou então uma foto do próprio iPhone, então vamos supor que eu peguei essa foto aqui e desenhei um quadrado, então eu vim aqui, peguei as linhas de guia para poder me auxiliar, coloquei aqui e fui arrastando para poder me auxiliar, fui colocando, fui arrastando, e eu vim aqui e criei um retângulo, coloquei uma certa opacidade, olha só, de 20%, e aí sempre aperta em espaço para poder você navegar, galera, para quem não viu as aulas, vai acompanhando para vocês pegarem as skills, Ctrl-Mais, Ctrl-Menos para tirar o zoom, e aí eu venho aqui, clico e arrasto até a borda ficar mais ou menos do tamanho que eu quero, beleza, já comecei a construir o meu mockup.

Aí eu vim aqui, agora eu quero a parte de dentro, vou fazer só até essa parte para vocês entenderem, venho aqui com as linhas guia da régua, caso você queira ativar a régua, se eu não me engano, só vir aqui em procurar por window, preference, enfim, eu vou achar aqui direitinho e eu falo para vocês onde ativa essa régua, caso no de vocês não venha ativo.

Aí eu venho, traço mais uma vez um retângulo, coloco nele uma certa opacidade, coloco de 20% para poder enxergar, mais uma vez eu arrasto até ele ficar desse jeito, e aí eu preciso fazer esse recorte, concorda comigo? Para poder fazer esse recorte, eu posso muito bem vir aqui com um retângulo também, fazer nessa parte assim, de forma que eu também aplique uma opacidade para poder enxergar ele, pelas setas direcionais eu ajusto para ficar do tamanho certinho, e eu posso muito bem fazer um border-radius para poder mais ou menos ficar do mesmo tamanho, está vendo? Então eu não vou fazer aqui com perfeição só para vocês entenderem, mas meio que o meu mockup já vai tomando forma, está vendo?

E como é que eu faço para poder recortar essa parte aqui? Eu seleciono esse elemento, deixa eu deixar em 100% de novo, 100%, 100%, eu seleciono esse elemento com o shift, segura shift, seleciona esse elemento, continua pressionando shift, selecionei os dois, e aí eu venho aqui no modo de combinar, e aí tem como subtrair, pegar interseção, no caso eu estou querendo subtrair, e aí eu vou construindo o meu mockup.

## Exportando em SVG

E aí você vai perceber que construindo o seu mockup, deixa eu tirar aqui as linhas guia, para você voltar e arrastar para o mesmo lugar, quando você constrói o seu mockup, que isso aqui dá um trabalhinho, dá até um trabalhinho, fica aí de exercício para vocês desenvolverem as habilidades, você pode vir aqui, clicar no frame e clicar em export, e aí vai ter a opção de você exportar em SVG, eu vou dar o nome de mockup-iphone, mockup-iphone, quase que não foi, mockup-iphone, então eu tenho aqui a opção de exportar, e eu escolho a opção SVG, quando eu exportar, eu vou exportar aqui na minha área de trabalho mesmo, e aí vamos ver o resultado.

Se eu clicar duas vezes, ele vai abrir no browser, vai abrir aqui, como se fosse uma internet, você percebe que ele é um SVG, se eu clicar em propriedades, olha só, ele pesa apenas 2KB, e o tamanho diz 4KB, então é muito, muito leve, e você tem uma ilustração de qualidade, e que é muito, muito fiel, além de você ter resolução infinita.

## A estrutura do SVG em código

E aí nós vamos agora verificar como se dá a estrutura de um SVG, em questão de tags HTML, então eu vou abrir aqui com o VS Code, e eu vou dar um zoom para vocês visualizarem direito, você percebe que é só código, está vendo?

Então ele aplica filtros, isso aqui a gente vai estudar com maior veemência no curso de Motion, mas você percebe que aqui ele tem a parte de definições, que meio que estabelece o linear gradiente que a gente tem lá dentro, eu vou dar aqui uma tabulação para vocês enxergarem, ele aplica filtros para poder conseguir aquela cor, ele aplica filtros em SVG, então todos esses aqui são filtros em SVG, inclusive filtros de sombra, onde é tudo configurado via código, e aqui é aquele gradiente laranja, onde tem aqui a cor laranja e outra cor laranja, e aí ele dá um ID, que é o paint-linear, e aplica esse paint-linear nos caminhos, que são os círculos, os retângulos e os outros caminhos que a gente definiu lá com o Figma, e aqui define o preenchimento deles também em hexadecimal.

Então eu vou estudar com mais veemência e dar maiores detalhes de como se estrutura um SVG, lá no curso de Motion, mas aqui ele é tudo estabelecido por código, por isso que é leve, e por ser estabelecido por código e ter tags HTML, que é um SVG, eu posso muito bem manipular eles via CSS, então meio que a magia do Motion surgiu daqui, então não vou dar muitos detalhes porque isso aqui é do curso de Motion, mas dá para perceber o poder do SVG e das ilustrações nesse modo, beleza galera? Até a próxima.
