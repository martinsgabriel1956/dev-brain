# CSS, classes e IDs: ligando o style.css, seletores de tag, classe e ID

Opa, fala pessoal, Násser aqui, sejam bem-vindos a mais uma aula do qual, na aula de hoje, nós vamos falar um pouquinho sobre CSS. Na aula passada, a gente falou sobre HTML, a gente vai continuar falando de HTML agora, porque agora tudo vai começar a misturar, mas a gente vai focar no CSS nas próximas aulas, beleza? Então, vou minimizar minha tela aqui, vamos começar.

## Estrutura do menu: header, nav, ul, li e links

Como eu tinha dito para vocês, pessoal, o HTML é literalmente para poder a gente organizar o conteúdo por meio de marcações. A gente delimita caixinhas e a gente vai organizando, dentro dessa outra caixinha tem isso, e a gente vai construindo a estrutura do nosso site assim, e eu vou começar a falar um pouquinho disso nessa aula e também vou falar de CSS, então vamos lá. Vamos supor que eu queira, nesse primeiro momento, dentro do meu body, dentro do corpo da minha página, eu queira criar um cabeçalho. Então, vou criar aqui um header, dentro desse header, eu quero uma barrinha de navegação, ou seja, onde tem os principais links, e é dentro disso que eu vou colocar, por exemplo, um menu, então vou colocar aqui um nav, uma barra de navegação. Dentro dessa barra de navegação, eu quero colocar uma lista de links, uma lista não ordenada de links, ou seja, eu vou colocar o ul, o ul é para criar uma lista.

A ul é uma lista não ordenada, ou seja, ou é um pontinho, ou é um quadradinho, que você vai ordenar os seus itens ali. Se você quiser, agora, ordenar por meio de número 1, ou então números romanos, ou então abcd, você vai colocar ol, só essa. Isso é tudo diferente, é diferença semântica de tags, que ela já vem com algumas pré-definições do próprio HTML, então não se preocupe, que você não precisa decorar tudo isso, dá para a gente modificar isso tudo depois, mas vamos lá.

O ul, por exemplo, e aí cada item se chama li, e olha só a escadinha que a gente está fazendo, a gente criou uma caixa chamada header, que é o nosso cabeçalho. Dentro do header, eu tenho uma barra de navegação, que é o nav, para poder fazer essa barra de navegação, eu vou criar uma lista, que é uma ul, e cada item da lista é um li, e cada item do li é um link, que a gente pode colocar assim, e eu vou colocar aqui, primeiro link, e aí eu posso colocar outros aqui, por exemplo, três links, primeiro link, segundo link, terceiro link, então vamos lá, terceiro link.

Salvei, ele automaticamente vai plotar aqui, então nós temos aqui, primeiro link, segundo link, terceiro link, vou dar aqui um zoom nessa página, só para poder a gente visualizar.

## HTML é estrutura, CSS é estilo

Então esse aqui é o nosso HTML, vocês percebem, pessoal, que o HTML sozinho dificulta a nossa vida, ele sozinho, como eu diria, é pobre visualmente, porque o HTML só serve para criar estrutura no nosso site, colocar conteúdo, é para isso que ele serve, então precisa de um segundo agente para poder deixar as coisas bonitas, para poder a gente estilizar isso, então o HTML é uma linguagem de marcação, não de programação, o CSS é uma linguagem de estilização, não de programação, é diferente também, só que ele tem bem mais recursos

## Criando o style.css e ligando pelo link

E agora a gente vai colocar o CSS nisso aqui, então dentro dessa minha pasta aqui, eu vou criar uma outra pasta chamada CSS, dentro dessa pasta CSS, eu vou criar um novo arquivo chamado style.css, automaticamente ele identificou ali como um CSS, e aí, pessoal, eu quero colocar cor na minha página, eu quero modificar isso aqui, fazer isso pelo HTML puro é possível, só que é muito complicado e muito limitado, então com o CSS é bem mais fácil.

Primeira coisa, eu tenho que dizer para o HTML onde está esse arquivo CSS para ele ler, então como é que eu faço isso? Por meio da tag link, já tem uma opção link CSS e não serve para linkar só CSS, tem a tag link com vários atributos, um dos atributos é linkar o arquivo CSS, então você vai lá e ele já está prontinho, você só precisa dizer o caminho, no caso é CSS barra style.css, porque eu criei uma pastinha, então você entende que quando o arquivo HTML está aqui nessa estrutura de pastas, ele enxerga uma pasta, o que tem dentro dessa pasta? Um outro arquivo.

Se eu tivesse que voltar a pasta ou então avançar em uma pasta, avançar em uma pasta vocês já viram, CSS barra style.css, se tivesse outra pasta, pasta barra, estrutura de diretórios normal, se eu tivesse que voltar uma pasta, se eu tivesse uma pasta lá dentro e quisesse voltar para anterior, voltar para anterior, eu fazia ponto, ponto, barra, pode ver aqui que ele achou os arquivos da área de trabalho, então como não está, está tudo certo, ou eu faço assim, CSS direto ou faço ponto, barra, que ele fala, esse diretório de agora é CSS, ele já encontrou, vocês percebem que o próprio VS Code, quando a gente digita ponto, barra, ele vai listar o que tem dentro dessa pasta, CSS, para enter duas vezes, então ele já achou esse arquivo, se eu vir aqui e salvar, ele vai linkar para mim.

Então vamos lá, agora a gente vai conhecer o que é o CSS, para que ele serve, nas próximas aulas a gente vai estudar mais específico sobre isso, quais são os seletores, quais são os principais comandos que a gente vai dar a CSS e mais uma vez, você não aprende tudo de uma vez, pessoal, eles aprendem com o decorrer do tempo, não tenha pressa nesse momento, esse momento é muito de descoberta Documentação, tá bom?

## Fundo, links e listas: os primeiros estilos

Então vamos lá, como é que eu faço no CSS, por exemplo, para mudar esse fundo, ele está branco, eu gosto de fundo dark, então o que eu faço? A tag que engloba tudo é a tag body, a minha página toda é feita dentro do body, então eu vou modificar ela, eu vou colocar um background-color e eu vou colocar uma cor em hexadecimal, por exemplo, vou colocar 0f, 0f, 0f, olha só ficou preto, então para vocês verem para que serve o CSS, eu queria uma outra cor, quero vermelho, quero azul, então serve simplesmente para isso, poder a gente definir aspectos visuais, mas não só visuais, vocês vão perceber o poder do CSS com o decorrer das aulas, então defini aqui o fundo.

Ah, mas eu quero mudar a cor dos links, a cor dos links está roxa, está sublinhado, eu não quero link sublinhado, então para poder tirar essa propriedade do link, eu faço text-decoration none, porque ele estava como underline, entendeu?

Então isso aqui já participa de uns resets que eu gosto de deixar dentro da página, porque isso aqui é tudo configuração padrão do HTML, Você pode ver que algumas coisas o próprio Google utiliza, por exemplo, o link ser azul quando você não visita e ele ser roxo quando você já tem visitado, isso é configuração padrão de HTML e você pode modificar isso via CSS, está bom?

Então, tirei aqui o sublinhado e eu quero ele na cor branca, então eu coloco aqui color, hashtag FFF, para ele ficar branco, porém a minha lista, que é a lista UL, ela está com uns pontinhos pretos aqui, eu não quero que apareça isso, ou seja, eu coloco list-style, ou seja, a forma de como você vai mostrar o estilo da lista como none.

Ele desapareceu, mas eu poderia muito bem colocar, por exemplo, eu quero um quadrado, um square, deixa eu voltar aqui para o branco, hashtag EEE, para poder mostrar para vocês aqui, está vendo que está um quadradinho, se você não colocar nada, se você vir aqui e comentar, ele fica uma bolinha.

Se fosse uma OL, que é uma lista ordenada, ele iria virar 123, então isso tudo você vai descobrindo com o tempo, não se preocupe com relação a isso, então vamos lá, só que eu quero sem lista, quero none, e aqui nós vamos voltar para o próximo de preto, um cinza escuro dessa forma aqui, e aqui nós vamos voltar para o UL, então é assim, pessoal, que eu vou estilizando.

## Tudo são caixinhas

Vamos supor que no meu link eu queira colocar um background, sei lá, vermelho, e vocês vão perceber que tudo são caixinhas, lembra do nosso header? Se você vir aqui no header e der uma borda nele para poder você enxergar onde está a caixinha do header, borda, dois pixels, solid green, olha só, ele criou uma caixinha com dois pixels de borda sólida, eu posso muito bem colocar uma borda que seja tracejada, que seja dashed, entendeu?

E todas essas personalizações você vai descobrindo com o tempo no CSS, até hoje tem personalizações do CSS que eu não conheço, mas existem algumas principais que a gente sempre vai estar tratando.

## Seletores de tag

Então vocês percebem que no CSS a gente utiliza seletores para poder a gente dizer onde a gente quer modificar, então o seletor é o próprio nome da tag, Ah, eu quero modificar a tag header, eu quero modificar a tag nav, eu venho aqui, nav, mais uma vez, eu vou dar um background-color pink para nav, olha lá, então eu vou o situando e esse exemplo aqui já vai ilustrar para vocês que tudo são caixinhas, tudo é div, então a sua capacidade está em você organizar essas caixinhas, essas divs, de forma que você entenda a estrutura e como você consegue modificar ela com o CSS.

E dentro desses seletores existem seletores que você mesmo pode criar, então a gente está vendo aqui que tem header, nav, mas vamos supor que você criou uma estrutura que ela tenha div ao invés de nav, então eu vou criar aqui, isso aqui vai contra o HTML semântico, mas só para eu explicar para vocês, vamos supor que eu tenho uma div aqui e uma div aqui, vai funcionar do mesmo jeito, ele vai perder a referência, por quê? Não existe mais header e não existe mais nav, só existe div, ele não encontrou esses seletores, como é que faz agora? Sendo que funciona, então se eu vir aqui em salvar, você vai ver que ele vai perder essa referência, ele não encontrou mais o seletor lá, o CSS, então como é que eu faço?

## Classe

Aí que vem a class e o id, esses conceitos aqui são primordiais para você entender as aulas de programação que virão, porque, por exemplo, eu posso muito bem dar uma label, uma etiqueta para essa tag, eu quero que essa tag seja identificada por essa classe, em que o nome da classe vai se chamar header e o nome da classe vai se chamar nav, então eu adicionei meio que uma label, uma etiqueta para poder identificar ela lá no CSS, mas é aí que está, eu consigo identificar não só no CSS, mas também no JavaScript, então vai servir para outras coisas, para poder eu elencar ali e puxar e manipular esses elementos.

Então pessoal, o header e o nav, agora eu consigo vir aqui no meu CSS e agora estilizar, só que para poder eu identificar uma classe, eu tenho que identificar ela com um ponto, então é .nav, se eu digitar aqui no .nav um background-color pink, vai funcionar, vou salvar aqui, vou salvar aqui, ficou pink de novo, se eu vir aqui e fazer .header e dar um background-color green dentro do class header, deixa eu ver aqui, acredito que ele não está indo porque ele não tem, deixa eu colocar aqui uma borda, um px solid blue, está aí, é porque eu precisei definir o tamanho dele, mas apareceu, vocês entenderam?

## ID

E tem a classe e tem o id, eu posso muito bem, ao invés de definir uma classe aqui, por exemplo, eu posso definir um id, sendo que eu vou colocar aqui nav-menu, o nome do meu id vai ser nav-menu e ao invés de chamar o header, o .nav, eu posso colocar hashtag nav-menu, porque quando é um id, eu chamo ele com hashtag, que é a cerquilha e quando é a classe, eu chamo com ponto, é assim que eu diferencio os dois, então se eu vir aqui e salvar, ele vai ficar exatamente igual, está vendo?

## Comentários

Exatamente igual, se eu quero comentar essa parte aqui do meu CSS, o que é um comentário? É literalmente quando você quer apagar alguma coisa da interpretação ali, mas você ainda quer deixar ali caso você precise usar ou então adicionar algum tipo de comentário, esse trecho no código faz isso e isso, você quer explicar o seu código, inclusive, recomendo demais, principalmente na parte de lógica, então quando você salva isso aqui, ele perdeu a referência, mas quando você vir aqui, salvou, ele conseguiu a referência de novo.

## Classe x ID: a diferença semântica

Então tem duas formas de eu referenciar além dos seletores padrões do HTML, que é criando classes e ids, só que tem uma diferença semântica entre eles, que é muitíssimo importante, o id, como o próprio nome já diz, é um identificador, então da mesma forma que você não pode ter dois CPFs ou que não existe uma outra pessoa com seu CPF, não existe uma outra pessoa com o mesmo número de banco, não existe uma outra pessoa com o mesmo número de RG que o seu, você é único, você precisa ser identificado, da mesma forma é aqui, existe essa diferença dinâmica, eu não posso colocar em outra tag o id nav-menu, você pode, mas a interpretação vai estar errada, a semântica vai estar errada, pode quebrar o seu código, pode dar algum problema ali, porque às vezes eu peguei esse id por meio de um JavaScript, por meio de um CSS e apliquei em uma tag só, vamos supor que você vai lá e adicione um id em outra tag, como é que ele vai saber qual é a tag que ele vai aplicar agora? Ele pode pegar pela ordem e ainda funcionar, mas por exemplo você colocou ele lá em cima, ele pegou uma ordem diferente, vai dar problema de semântica, então você vai utilizar o id para aquela tag específica, é só essa tag que tem no meu documento inteiro.

## Uma classe para vários links

Já o class você pode aplicar em várias, então vamos supor que eu crie uma class de link, no meu menu eles vão ter a mesma formatação, aí você aplica uma classe, qual é o nome da classe? nav-link, por exemplo, e ainda vou explicar como nomear essas classes, bons padrões para poder a gente nomear essas classes, então vamos lá, class-link, eu vou aplicar classe-link nos três links e agora eu vou estilizar, então eu vou vir aqui, .nav-link, a cor dele seja preto, então hashtag 000, olha só, automaticamente todos os links vão ficar pretos, se eu vir aqui e apagar essa classe do terceiro link, apaga e salvei, ele voltou a ser branco.

Então o que a gente percebe? Que a classe está no nível acima do seletor, então você pode ver que eu defini todos os links, eles são brancos, ele vai respeitar a classe, então a classe está em uma hierarquia maior que o seletor, vocês estão pegando aí, vocês percebem que eu coloquei aqui que o background-color de um link é vermelho, mas quando eu aplicar o nav-link o background vai ser branco, então hashtag FFF, olha lá, por mais que ele seja link, ele está pegando as configurações que eu estabeleci no nav-link, ao invés de colocar as configurações do link normal.

## Encerramento

Então a gente está começando a aprender que o CSS é uma linguagem de estilização, eu vou modificar o CSS, a estrutura visual, a estrutura de layout do meu site por meio do CSS, vocês vão ver o quão poderoso é o CSS, eu nem comecei a falar dos recursos dele aqui, mas nesse primeiro momento a gente precisa entender como é que eu faço esse link da tag que eu criei no HTML com o CSS lá, por meio de seletores, e tem diversos seletores, vai ter uma aula só sobre seletores, mas nesse primeiro momento eu queria mostrar que são os seletores padrões, que são as tags e class e id, que é assim que a gente consegue elencar e selecionar qual é a tag específica que a gente quer mexer, e tudo mais, então nessa primeira aula eu vou deixar isso e a gente vai seguir nas próximas aulas, até a próxima.
