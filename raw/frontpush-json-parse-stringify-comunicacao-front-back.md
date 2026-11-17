# JSON: a linguagem unificada entre front-end e back-end, JSON.parse e JSON.stringify

Fala, pessoal, tudo certo com vocês? Vamos lá para mais uma aulinha de JavaScript, onde nós vamos começar no progredir do entendimento da linguagem, nós vamos começar a apresentar conceitos relacionados ao JavaScript assíncrono. São conceitos muitíssimo importantes para poder a gente progredir no estudo da linguagem, entender como é que se faz as requisições de back-end e front-end, e bem como para a gente entrar em qualquer framework que a gente vai estudar.

E como principal tópico que eu vou começar aqui a falar para vocês, eu vou falar sobre o JSON, e qual é o papel dele, por exemplo, na comunicação do back-end e do front-end. Mas antes, está bom que eu iria retomar um raciocínio com vocês.

## Front-end, back-end e a linguagem unificada

Vocês sabem muito bem que front-end e back-end são duas coisas distintas. O back-end é aquela parte do código onde faz as requisições, organização das regras de negócio para com o banco de dados, e o front-end é quem requisita ou passa os valores para o back-end conversar com o banco de dados e fazer toda essa troca de informações.

Calma que eu vou dar um exemplo. Vamos supor que você esteja lá acessando um e-commerce. Você vai perceber que lá na URL, nessa seção aqui, passa um monte de informações lá, inclusive, por exemplo, o ID do produto, a descrição do produto, qual é, por exemplo, o serial number do produto. Para quando eu abrir uma determinada página, ele requisite aquele produto específico para o back-end, o back-end pergunta, faz uma requisição para o banco de dados, traz todas essas informações e joga para o front-end na tela.

Assim como, por exemplo, quando eu estiver cadastrando algum tipo de usuário no front-end, eu pego as informações que você colocou naquele formulário, empacoto e mando para o back-end falar, cadastra esse usuário. Então é esse tipo de comunicação que existe.

Primeira coisa, ele é feito como? Por meio de uma API e por meio do quê? Por meio de arquivos de linguagem unificada a nascer, que é o JSON.

Como assim? Pense que, vamos supor que em todo o mundo seja obrigado todos a aprender inglês. Você concorda que se todo mundo aprender inglês, todos conseguem se comunicar, independente de qual país ele seja, a mesma coisa é o JSON nesse papel.

O JSON é uma linguagem de marcação, de objetos, vocês vão entender já por que eu vou detalhar isso aqui para vocês, que ela é unificada, ou seja, todas as linguagens entendem o formato JSON. Se todas entendem o formato JSON, é essa linguagem unificada que eu utilizo para poder trocar informações entre front-end e back-end, independente da linguagem.

Por mais que o nome seja JSON e o J seja de JavaScript, ele é uma linguagem unificada que pode ser utilizada em qualquer linguagem. Então, o front-end pode ser de uma tecnologia que não seja propriamente JavaScript, assim como o back-end pode ser Node, que é JavaScript, ou pode ser, por exemplo, PHP, independente da linguagem, eles vão entender o JSON, é assim que eu consigo fazer essa comunicação.

Um pequeno e importante de parênteses para a gente começar a entender os principais conceitos de JavaScript assíncrono.

E antes de eu partir para demonstrar para vocês como é que se dá um arquivo JSON, a definição dele chama-se JavaScript Object Notation, ou seja, uma anotação de objeto, e aí você que conhece como se dá um objeto, ele se assemelha muito em questão de organização, em questão de como eu o coloco e a gente vai verificar ele agora. Então, basicamente, é um formato de organização de dados composto por um conjunto de chave e valor, sempre vai ter isso, como se fosse um atributo e um determinado valor, tá bom? E vou aqui agora sumir da telinha e detalhar um pouco mais para vocês.

## Estrutura de um arquivo JSON

Eu estou construindo aqui, pessoal, simplesmente eu vim aqui e criei um arquivo chamado produto.json, ou JSON, seja lá como você preferir.

E agora eu vou começar a estruturar o meu arquivo JSON e vou mostrar para vocês, detalhando a estrutura de quais são as características que fazem desse arquivo um JSON para poder ele funcionar de fato e vai ser de suma importância para poder a gente depois transformar, destransformar e entender como a linguagem comunica por meio do JSON.

Basicamente, você pode abrir um colchete, lembre-se que essa anotação é muito parecida com arrays e eu posso colocar, por exemplo, objetos aqui dentro, lembrando que objeto é sempre com chaves. Já que o nome desse JSON é produto, eu vou colocar, por exemplo, características de produto e cada objeto desse aqui é a descrição de um produto. Então, posso colocar, por exemplo, ID, mas as características ou então o conjunto de chaves do JSON sempre tem que ser colocado por chaves duplas, não funciona aspa simples e vocês vão ver que ele dá erro.

Então, eu coloco aqui ID, coloco dois pontos e, por exemplo, ID de número um, porque é o meu primeiro produto, vírgula, coloco, por exemplo, o nome do produto, aí eu posso colocar aqui, já que é um string, mais uma vez, não funciona com aspas duplas, então eu posso colocar Notebook Dell, vírgula, posso colocar, por exemplo, o modelo é gamer e, por exemplo, quantidade, eu posso colocar aqui, sei lá, tem cinco no estoque.

Primeira coisa, pessoal, que eu preciso explicar para vocês, as propriedades, mais uma vez, precisam ser em aspas duplas, se colocar em aspas simples, vai dar erro, se eu colocar aqui aspas simples, já viu que o próprio VS Code já mostra que está dando erro, que tem alguma coisa errada nesse arquivo JSON, então precisa ser aspas duplas. Da mesmíssima forma, se o seu conteúdo for uma string, está vendo, por mais que aqui seja uma string, onde eu esteja atribuindo o Notebook Dell a variável ou a chave nome, não pode também.

Outra coisa, o último item da descrição do seu objeto, se é que eu posso dizer assim, dentro do JSON, ele nunca pode ter vírgula, ou seja, o último item não pode ter vírgula, outra coisa.

E eu posso colocar n objetos aqui, então eu posso, digito vírgula, para poder separar um objeto do outro e eu posso colocar dois, aí eu posso colocar Notebook Acer, modelo gamer, quantidade, 10. E aqui eu posso colocar as descrições que eu quiser, seja uma configuração de input, uma configuração de socket, de API, tudo você pode descrever dessa forma aqui.

## Valores: número, string, booleano, objeto e array

E além disso, eu também gostaria de mostrar para vocês quais são os valores que você pode passar. Como a gente viu aqui, valores numéricos, como a gente viu aqui valores de string, mas você pode muito bem colocar também valores booleanos, então eu posso colocar se ele tem USB-C, que é o novo padrão que está vindo, onde eu posso colocar true ou false, então ele também aceita valores booleanos.

Além disso, ele também pode carregar um objeto dentro do outro, a gente vê que é muito comum esse tipo de conceito, então eu posso definir aqui um objeto, que é uma característica desse produto, e aí eu simplesmente faço dois pontos e coloco outras características aqui, onde eu posso colocar o endereço do CNPJ, então do fabricante, ou então características do fabricante, eu posso colocar assim, fabricante, e como isso aqui é um objeto, eu estou abrindo chaves, eu posso colocar características, sei lá, cidade de onde o fabricante está falando, e aí eu coloco aqui Brasília, posso colocar, por exemplo, país, sempre com aspas duplas, país, eu coloco Brasil, então você vai perceber que eu posso colocar valores booleanos, valores numéricos, valores de string, valores de objeto e também colocar arrays, então eu posso transformar isso aqui também em uma array.

Como é que eu faço? Simplesmente, vou só copiar e colar aqui, fabricante 2, para poder diferenciar aqui, porque você viu que ele deu um warning, quando eu tenho a mesma característica, e agora eu vou colocar colchetes, para poder indicar que isso aqui é um array e não um objeto, e colocar fabricante 2, tirei a vírgula, então está aí, eu consigo estabelecer todas essas características aqui dentro, só que aqui, como é um objeto, eu tenho que simplesmente passar o valor, então não funciona esse negócio de eu ter um atributo e um valor, o array é direto no valor, um array de valores, então o primeiro lugar está Brasília e Brasil, isso aqui é só porque eu não tive um exemplo melhor para dar, só para poder demonstrar as características de um JSON, de quais informações eu consigo colocar aqui dentro.

Então basicamente é isso, eu vou diminuir para deixar bem simples, vou deixar só essas características aqui, para poder falar um pouco mais agora de como a gente consegue manipular o JSON dentro do próprio JavaScript e mostrar que tem um objeto chamado JSON aqui dentro, onde nós temos dois métodos principais que a gente está sempre utilizando.

## O objeto JSON: parse e stringify

Então, vamos lá, o objeto é simplesmente JSON em maiúsculo, onde nós temos duas funções, dois métodos principais para poder a gente manipular o JSON, que vocês vão ver em muitos lugares, o primeiro método é o parse, o que esse método faz, vou colocar aqui uma descrição, basicamente ele transforma o texto, isso aqui é uma string, por mais que ela tenha um formato e tudo mais, isso aqui é como se fosse uma string, então ele transforma o texto JSON em objeto, então eu quero transformar isso em um objeto manipulável para poder acessar os atributos, adicionar métodos, enfim, eu quero transformar isso em um objeto, então eu utilizo o parse e tem o JSON.stringify, que é justamente ao contrário, é quando eu quero transformar um objeto que eu tenho aqui dentro do JavaScript, eu construí um objeto em JavaScript e eu quero transformar esse objeto em JSON, deixa eu fechar aqui, em um arquivo JSON, então nós vamos utilizar essas principais aqui e eu vou demonstrar para vocês, deixa eu comentar.

Então pessoal, primeira coisa, eu quero, por exemplo, criar uma constante chamada JSON, onde eu vou pegar o texto desse JSON aqui que eu acabei de criar e transformar ele em objeto, então eu faço JSON.parse e eu vou passar a string aqui dentro, uma string de JSON, então simplesmente eu vou pegar isso aqui, vou dar um Ctrl C, um Ctrl V, é muito importante que ele esteja na linha, em uma linha, ele não vai pegar essas quebras de linha aqui, então a gente pode fazer assim, vamos lá, para poder ficar em uma linha, você pode ver que ele parou agora o erro, então ele precisa que ele seja nesse formato aqui, vamos dar aqui um ponto e vírgula e continuar.

Então se eu simplesmente vir aqui e der um console.log do JSON que a gente acabou de ver aqui, vamos ver o que ele devolve para a gente, olha só, ele já devolveu um objeto bonitinho, com a id 1, modelo gamer, nome, Notebook Dell, quantidade 5 e olha só, objeto, então ele já transformou essa string aqui de JSON em um objeto.

Nas próximas aulas eu vou mostrar para vocês, assim que eu apresentar o que é API e requisição HTTP, que tem como fazer essa requisição aqui via HTTP, porque a gente não vai utilizar esse método aqui, copiando e colando, porque geralmente os arquivos JSON são muito grandes, então eu fiz ele pequeno só para vocês entenderem.

Então a gente já viu aqui que tem como ele justamente fazer essa mudança e eu posso muito bem agora fazer o contrário, agora eu quero definir um objeto, então eu estou construindo aqui um objeto em JavaScript, a gente sabe como é que a gente constrói, simplesmente abre e fecha chaves, e aí eu posso colocar um determinado objeto, sei lá, caneta, quais são os atributos de uma caneta, então eu posso colocar aqui cor, onde eu coloco azul, opa, azul, cor azul, posso colocar formato, o formato da caneta é triangular, a pegada dela, sei lá, tamanho, eu posso colocar, não, tipo, posso colocar assim, tipo é uma caneta de desenho, estou só inventando aqui, beleza pessoal?

Então esse aqui é um objeto e vamos supor que eu queira transformar esse objeto em linguagem JSON e eu vou utilizar o método stringify, então eu posso criar aqui uma constante chamada string JSON, onde o que eu vou fazer? Eu vou pegar aqui o objeto JSON, que já existe, isso aqui é nativo do JavaScript, ele tem um monte de métodos e tudo mais, só que esses dois são os principais, então stringify, onde eu vou pegar o objeto caneta e simplesmente vou dar um console.log no string, essa é a string que eu acabei de construir, string JSON, vou comentar esse outro console aqui só para poder a gente ver o que acontece, então olha só, ele acabou de transformar em uma string JSON, e plotou aqui no console.

Então basicamente é isso que eu tenho para falar sobre JSON, nas próximas aulas a gente vai construir outros conceitos em cima disso e por enquanto é isso, beleza pessoal? Então falou e até a próxima.
