# Configurando o ambiente: Git, Node.js, Yarn, VS Code e extensões

Opa, fala pessoal, sejam muito bem-vindos ao módulo de front-end, de código em si, onde essa aqui é a aula introdutória para poder a gente estabelecer o básico de HTML e CSS, mas também a gente configurar todo o ambiente antes da gente começar. Então, aqui tem as primeiras considerações que, assim, o pessoal sempre tem dúvida. Estou reunindo aqui as principais dúvidas para vocês terem a melhor experiência possível ao decorrer do curso. Então, nesse módulo nós vamos ver quais são as coisas que são interessantes da gente instalar, para que a gente está instalando, o que precisa instalar, o que não precisa, como configurar o ambiente e mais algumas considerações, enfim, vamos lá.

## Só HTML, CSS e JavaScript: basta um editor

Então, pessoal, o primeiro ponto que eu quero dizer para vocês é, se você está querendo, no primeiro momento, só mexer com HTML e CSS e JavaScript sem absolutamente nada de JavaScript, por exemplo, utilizando React ou outra biblioteca, você não precisa instalar absolutamente nada, somente um editor de código, que é o VSCode.

Por que isso acontece? Olha aqui, a gente está vendo o Chrome. Esse aqui é o Chrome. Então, pessoal, o Chrome, o Mozilla, o Safari, todo o browser, todo o navegador, ele entende três coisas, HTML, CSS e JavaScript. É lógico que tem uma diferençazinha de interpretação entre um e outro, principalmente no CSS, que tem técnicas para a gente fazer com que a interpretação seja mais uniforme possível, mas o browser sempre vai entender essas três.

E para você programar utilizando somente essas três, você não precisa instalar nada somente de um editor de código, mas, porém, contudo, entretanto, eu vou falar aqui todo o processo para vocês e vou explicar os pontos de por que precisa instalar isso, mas, às vezes, não é necessário para o que você está fazendo. Então, esse é o primeiro ponto.

## Git: Git for Windows e o terminal no Linux e no Mac

Eu vou minimizar aqui a minha tela para poder não atrapalhar vocês. A primeira coisa que eu quero instalar é o Git Bash. Então, se você vir aqui no Google, download Git Bash ou digite Git for Windows. Então, vamos lá, Git for Windows. Ah, Násser, o meu sistema operacional não é o Windows. Por que você está mostrando as coisas do Windows? Porque, pessoal, se você tem o sistema operacional do Linux, qualquer distribuição Linux ou o Mac, você instala o Git pelo próprio terminal.

Então, muito provavelmente, se você estiver em um Linux, você vai abrir o terminal, vai digitar lá sudo, se for uma distribuição Ubuntu, por exemplo, que já vem com o sudo instalado, ou uma distribuição do Debian. O sudo significa o que? Me torne super usuário por um tempo específico. Ou o su, que é um super user, por exemplo, no Debian. E é porque você precisa dessa patente no sistema para poder fazer essa instalação. Então, você vai colocar sudo ou su, apt ou apt-get, que são os gerenciadores de pacotes do Linux, install para instalar Git. Esse é o nome do pacote.

E eu aconselho vocês, se você tem o sistema operacional Linux, é só colocar no Google como instalar o Git no Linux. Vai ser o primeiro, senão o segundo link que você vai achar e você vai conseguir instalar o Git primeiro.

## O que é o Git e para que serve o versionamento

O que é o Git? Então, já aproveito aqui para poder mostrar para vocês o GitHub.com ou o GitLab.com, esses dois. Vamos lá. Olha só, caiu no GitHub do Yuri. Enfim, pessoal, o GitHub e o GitLab são repositórios online que a gente utiliza o Git para poder fazer o versionamento do nosso código.

O que é versionamento? Por que isso é necessário? Então, vamos lá por partes. Quando você está desenvolvendo o software, pessoal, você concorda comigo que você vai codar, você vai atualizar o sistema, se tiver algum bug, você vai atualizar de novo. Se tiver alguma nova feature, você vai atualizar de novo. E aí, em meio a esse tanto de atualizações, pode ser que, por exemplo, estou citando aqui uma situação hipotética, você suba essa nova atualização e ela esteja com bug se você não percebeu.

É interessante que se você subiu essa aplicação, você precisa retornar a versão antiga para ela se tornar estável de novo para você consertar o código.

Ou então você está trabalhando em times. Quando você trabalha em times, você precisa de uma organização. Vamos supor que eu vou subir um pedaço do código na aplicação, aí uma outra pessoa vai subir um outro pedaço de código de uma outra parte da aplicação e você percebe que precisa de algo para poder organizar isso, porque senão vai dar problema.

Então, o Git, pessoal, é justamente para isso. Quando a gente está estudando sobre programação, quando a gente está literalmente desenvolvendo algum tipo de código em maior grau de complexidade ou menor, mesmo que a gente esteja mexendo com HTML, que é uma linguagem de marcação e a gente vai falar sobre isso nos próximos tópicos, nas próximas aulas ou então o próprio CSS, é necessário o Git para poder você versionar o seu código, para poder você ter um controle de versão que é o Git sobre o seu código. Para caso tenha algum problema, você tenha mecanismos de como arrumar o problema da forma mais eficiente possível. Trabalhar em times nem se fala, é obrigatório você saber o Git.

Então, pessoal, a gente vai falar um pouquinho sobre o Git também nas próximas aulas, pelo menos o basicão para a gente entender o que é o quê, o que é uma branch, como é que sobe uma nova atualização, como é que desce, como é que reseta, enfim.

E aí, você que está no Windows, você precisa instalar isso utilizando o Git for Windows. E aí, por que eu falo para você instalar antes de, por exemplo, instalar o VS Code? Porque se você instalar antes, o VS Code já vai identificar de cara e você não precisa meio que adicionar o Git nele, por mais que seja fácil, mas é interessante você seguir esse fluxo.

## GitHub, GitLab e outros repositórios

E aí, existe o GitHub ou o GitLab, que são repositórios do qual você pode vincular o seu código. Tem outros repositórios online? Tem, tem o Bitbucket, tem um outro também que eu esqueci o nome agora, mas os principais GitHub e GitLab. E eu acredito que o GitHub está na frente. O GitHub já foi muito utilizado porque ele tinha melhores planos gratuitos, hoje em dia o GitHub está muito bom e todo dev que eu conheço, acredito que trabalha com GitHub, um ou outro, já vi trabalhando com o GitLab, todos têm a preferência para isso aqui. Então, é só você vir aqui, fazer a sua conta e tudo mais para poder você fazer o versionamento.

## Instalando o Git for Windows

Voltando ao Git for Windows, vamos lá, digite no Google Git for Windows, esse aqui vai ser o primeiro link, você vai baixar e instalar isso aqui. A instalação disso aqui, pessoal, literalmente vai instalar como se fosse um kernel, o que é kernel? Um núcleo do Linux de um sistema em Unix dentro do seu Windows e aí você vai ter acesso como se fosse a um Linux, só que no Windows, uma janelinha preta para poder você digitar alguns comandos, relaxa que eles não são complicados, eu vou mostrar para vocês e você tem como literalmente mexer como se estivesse no Linux no Windows e a instalação disso aqui é meio que next, next, next, sem problema nenhum.

Então, faça o download disso aqui, sempre vai ter lá um campo de nós recomendamos isso, você concorda, next, tá bom? Todas as configurações padrões que vêm na instalação do Git, vocês podem ter coisas lá que vocês não vão entender, você concorda, next. Então é isso, o primeiro ponto para vocês instalarem isso aqui, o Git.

## Node.js e a versão LTS

O segundo ponto para vocês instalarem, pessoal, é download Node.js para o Windows, por exemplo, e aí mais uma vez você vai vir aqui na página do Node e fazer a instalação da versão LTS, o que é versão LTS, o que é Node, não estou entendendo nada novamente, vamos lá.

Quando você está, pessoal, codando em JavaScript, que é uma linguagem de programação, e está utilizando ele no browser, eu falei lá no começo da aula que vocês não precisam instalar nada, que o próprio browser entende JavaScript, então até aí tudo bem, até aí tudo certo.

Porém, contudo, entretanto, vamos supor que você queira rodar um JavaScript fora do ambiente do browser, você não consegue, e aí você precisa do Node para poder instalar, para poder utilizar o JavaScript em outro lugar que não seja o browser, fora que o browser tem outra particularidade, o browser demora um pouco a atualizar, você vai perceber, ou então você já vai ouvir em algum lugar, que às vezes chega um recurso novo, seja o do CSS, seja o do JavaScript, e ele demora um tempo até o browser ter esse suporte.

## Can I use e o suporte dos browsers

É por isso que, por exemplo, a gente usa o Can I use, o Can I use literalmente vai listar quais são as propriedades que já chegaram aos browsers, em qual versão chegou, se tem alguma versão desse recurso que, por exemplo, não está estável, alguma coisa ele vai falar, por exemplo, a propriedade transform do CSS, que a gente utiliza muito, você vai perceber que ele vai listar CSS3 2D transforms, ele vai listar todos os navegadores que têm o suporte para esse recurso aqui, mas eu vejo que um recurso que não está muito disponível em todos.

Voltamos pessoal, foi mal, teve um pequeno corte aqui, o meu celular despertou, mas enfim, voltando, tem um recurso que não é muito aceito por todos os browsers, que, por exemplo, o backdrop-filter, o que é esse backdrop-filter? É uma propriedade que a gente utiliza no CSS para poder dar aquele efeito de vidro desfocado, para vocês perceberem, alguns efeitos que eu implementei na própria página do FrontPUSH não estão disponíveis, por exemplo, no Mozilla Firefox, se você abrir nele, mas no Chrome ele já vai funcionar, então ele traz justamente esses recursos, vocês vão perceber que no Firefox está vendo que está vermelho aqui, ou seja, versão 98, versão 99 não é suportada por padrão, mas você pode habilitar.

Ele tem a opção de você habilitar isso e ele te passa aqui as informações de como você pode habilitar esse recurso, deixa eu dar um zoom aqui, dentro do Firefox, mas você vai ver que no Chrome ele está suportado, no Safari ele está suportado, no Opera, mesma coisa, então é só no Opera Mini e alguns browsers aqui, Firefox principalmente, ele não vem suportado, e o que é browser, do browser, enfim, ele vai mostrar para você os recursos, então já é um parêntese aqui nessa aula.

Mas o que eu estou querendo mostrar para vocês é que quando eu quero rodar o JavaScript fora do ambiente do browser e, além disso, que ele seja um pouco mais recente, a gente precisa do Node, a gente precisa do Node para poder instalar pacotes, por exemplo, utilizando o React, biblioteca.

Então vem aqui, baixa a versão LTS, por que é LTS? A LTS, pessoal, nesse ambiente de pacotes open source e tudo mais, ele é aquela sigla onde você literalmente tem uma estabilidade maior, meio que tem a versão mais atual, mas pode conter bugs e tem a versão LTS, que é aquela que é mais estável, então eu sempre recomendo vocês baixarem essa aqui.

A maioria dos sistemas de vocês vão ser 64 bits, acho dificilmente ser 32 bits, só venha aqui, faça a instalação e a mesma coisa, é bem next, next, next e ponto.

Uma outra coisa que é interessante a gente instalar antes para quem for programar em React, então eu reitero aqui, se você for utilizar alguma biblioteca, você precisa do Node, mas só for estudar HTML, CSS e JavaScript, só precisa do VS Code.

## Yarn

Uma outra coisa que é interessante é você instalar o yarn, vamos lá, yarn for windows, então a instalação dele é um outro pacote de instalação, vocês vão perceber que quando a gente entrar em React, se eu preciso de tal pacote, você vai digitar npm install alguma coisa, ou então yarn add alguma coisa, algum pacote, então para você instalar esses pacotes, é legal você ter também aqui a instalação do yarn no seu PC e aí uma vez que você instalou o Git, o Node e o yarn, você já está preparado para utilizar tudo que tem disponível no curso, você não precisa instalar nada mais que isso.

## VS Code

Mas agora nós precisamos do VS Code, então para quem não sabe, o VS Code é um editor de código, então é muitíssimo utilizado, a grande maioria do pessoal vai utilizar isso aqui e eu inclusive recomendo que você utilize o VS Code, tanto pela compatibilidade da gente estar trabalhando aqui no curso, às vezes tem algum recurso que, por exemplo, é de um plugin que está no VS Code e às vezes em editor, editor você não vai conseguir, então isso aqui literalmente fica a seu critério, mas eu recomendo fortemente você utilizar o VS Code, mais uma vez, tem a versão dele para Windows, para Linux, para Mac, para você fazer essa instalação, beleza?

## A ordem de instalação

Então siga, pessoal, esse fluxo aqui, acredito que não vai dar problema em nada, se tiver algum problema, só dá um Google, então coloca aqui nos comentários que a gente vai resolver, então siga esse fluxo, se eu quero logo instalar tudo, não quero mais mexer com isso, quero configurar tudo, instala o Git, instala o Node, instala o yarn, depois o VS Code. Beleza?

## Extensões do VS Code

Uma vez que você tem instalado isso, pessoal, nessa ordem, agora eu vou mostrar para vocês aqui dentro de como é que a gente instala as outras coisas que são interessantes para poder a gente ganhar produtividade ou então personalizar o seu VS Code, está bom? Então as extensões que eu acredito que são as mais importantes, eu vou falar aqui para vocês. Então vamos lá, VS Code icons, vou passar aqui por todas as extensões do meu VS Code. Quando você faz a instalação, é só você vir aqui nesse quadradinho, extensions ou plugins do seu VS Code, então a gente vai instalar algumas coisas que a comunidade desenvolve, que ganha em produtividade que facilita o seu fluxo de trabalho e eu vou explicar aqui alguns pontos importantes.

O VS Code icons, literalmente estética, não tem esses íconezinhos que quando a gente cria uma página aparece aqui, o símbolo do JavaScript, o símbolo do Sass, o símbolo do HTML, é literalmente para isso e aí eu instalei, vim aqui, digitei aqui no marketplace, nas extensões, VS Code icons, ele vai aparecer, está bom?

Uma outra coisa, Thunder Client, está bom? Esse Thunder Client aqui, pessoal, ele é meio que um testador para poder, quando a gente abrir uma API, para poder a gente consumir dados de uma API, para a gente testar a API, fazer requisições, subir para ver se está funcionando tudo certo, primeiro, antes da gente ir para o código, o Thunder Client é uma ótima opção. Tem o Postman, só que aí você precisa instalar, eu acredito que é bem mais fácil o Thunder Client, inclusive eu ensino o Thunder Client lá na seção de React, então você já pode deixar instalado também, esses aqui não.

O Prettier - Code formatter também é muito interessante você instalar, quando você está digitando o código ali, você pode ser que você não tabule, não organize o seu código, ele vai organizar para você ao salvar, então muito interessante, tem algumas coisas que eu não vou falar nessa primeira aula, porque não faz sentido, porque vocês nem sabem de programação ainda, alguns aqui, então eu deixo para falar um pouquinho depois.

## Live Server e o auto reloading

O que é muitíssimo importante é o Live Server, esse aqui fala, gente, por favor, instale esse plugin, instale essa extensão, por quê? Isso aqui vai nos dar a propriedade de auto reloading, para quem não sabe, quando a gente está, por exemplo, programando, deixa eu abrir aqui com o Live Server, ele vai fazer um servidorzinho para poder rodar a nossa aplicação, então isso já é um ponto positivo, por mais que seja um servidor simples de HTML, CSS e JavaScript, tem alguns recursos que só funcionam quando são rodados em servidor, que é diferente de você ir lá, clicar no seu arquivo HTML duas vezes e ele abrir no seu browser, você rodar ali no servidor, tem alguns recursos que só funcionam com o servidor, no momento eu vou deixar assim, e o Live Server já cria esse servidor para a gente, e além de criar esse servidor, ele, assim que a gente, por exemplo, modifica alguma coisa no nosso site, modifica alguma coisa no nosso site, a gente sempre precisa vir aqui e dar F5.

Então a gente modificou alguma coisa no nosso HTML, no nosso CSS, no nosso JavaScript, quase que não sai, eu preciso voltar no navegador, onde está aberto, e apertar F5 para poder atualizar, com o Live Server, só de eu salvar, ele já atualiza para mim, então, se eu vir aqui, por exemplo, dar um enter no meu arquivo, eu modifiquei o meu arquivo, se eu der um Ctrl S utilizando o Live Server, você viu que automaticamente ele fez o auto reloading, é uma propriedade que, por exemplo, quando a gente está utilizando o React, também a gente consegue, mas aqui, para poder fazer os nossos testes, a gente ter mais produtividade, a gente já consegue só salvando, ele já recarrega para nós e a gente já consegue ver em tempo real aquela modificação, e as aulas serão meio que nessa pegada, então, Live Server é muitíssimo importante.

## Live Sass Compiler e o que é um pré-processador

Antes de você estar instalando, o Live Sass Compiler, isso aqui, pessoal, eu vou deixar um pouco para poder explicar para vocês lá na parte de Sass, para quem não sabe o que é Sass, não vou deixar essa aula muito gigantesca, mas o Sass é um pré-processador do CSS, o que é um pré-processador?

Para quem não sabe, o CSS é uma linguagem de estilo, é uma linguagem de estilização, é uma linguagem de layout, e aí ele não tem muitos recursos de otimização voltados à programação, então são voltados à programação.

Vamos supor que no CSS eu queira colocar, por exemplo, um if else, se isso acontecer, acontece isso no código, se não, acontece isso no código, então eu crio uma estrutura condicional no CSS nativo, não consigo fazer isso, e aí, se eu conseguisse fazer isso, a minha produtividade ia aumentar, porque eu ia conseguir programar, por mais simples que seja, uma estrutura de condições dentro do CSS, e isso já nos dá infinitas possibilidades, estou citando um exemplo.

Então o Sass adiciona propriedades de programação, se é que eu posso dizer assim de forma didática, dentro do nosso CSS, ele não modifica o CSS em nada, a gente programa o CSS do mesmo jeito que a gente faria se fosse no puro, mas ele adiciona algumas coisinhas a mais que facilitam o nosso workflow, e para essa aqui não ser uma aula pesada, eu explico mais sobre como ter essa extensão para poder rodar o Sass, é simplesmente um programinha que a gente instala com um clique, a gente vem aqui, clique, instalou, ele vai instalar a extensão de Sass, e aí a gente vai conseguir utilizar esse recurso, somente isso.

Se você tiver mais curiosidades, vai lá na aula de Sass, que a gente trata isso aqui de maneira bem mais enfática.

## Outras extensões e temas

HTML Snippets, Material Theme, Color Highlight, esse Color Highlight é literalmente quando você digitar um hexadecimal dentro do seu VS Code, ele vai colocar a cor ali, então vamos supor que eu coloque hashtag FFF, que é o branco, quando eu digitar hashtag FFF, ele vai identificar que aquilo ali é um hexadecimal e já vai pintar aquilo ali de branco, isso aí facilita também.

Enfim, tem o One Dark Theme, que literalmente, pessoal, é para poder personalizar o meu VS Code, você vai ver que quando você instalar o seu VS Code, ele não vai estar nesse tema que está sendo apresentado para vocês, vai estar em outro tema, e se eu quero mudar as cores, isso e aquilo, então só procura por temas, se você digitar themes dark aqui dentro, você vai achar uma infinidade, tem o material theme e o One Dark Theme, a extensão que eu utilizo aqui, se você vir em color theme, não sei se está dando para enxergar, mas é o Community Material Theme, então você já sabe o que é o material theme, Ocean High Contrast, é esse o tema que eu utilizo dentro do meu VS Code.

## Git Bash como terminal padrão no VS Code

Para poder a gente, por exemplo, abrir o terminal, uma vez que você instalou o git, lá o git bash, você vai vir em terminal, new terminal, então você vai ter condições de mexer no seu terminal aqui, eu instalei depois, não segui exatamente o fluxo que eu tinha me falado, instalei depois, o meu VS Code não está identificando o terminal do git bash que a gente instalou lá atrás, que isso aqui é o git bash, você vai ter que vir nesse mais aqui e adicionar o git bash como default, ele vai abrir todos os bashes que podem ser instalados, por exemplo, eu tenho o próprio PowerShell que é do Windows, o JavaScript debug terminal, o Ubuntu 20.04 instalado em WSL e aí na maioria das vezes eu deixo o git bash aqui como default e ele vai abrir essa linha de comando aqui para mim, do qual a gente vai trabalhar só quando for nas partes de programação mesmo, como React ou qualquer outra biblioteca.

## Encerramento

Beleza pessoal, então não mais é isso, essa aqui é a aula introdutória, tomara que ela tenha sido leve para a gente começar, aguarde aí as próximas aulas para a gente continuar o curso, falou pessoal, até a próxima.
