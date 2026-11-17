# Modules JS: import, export, type module e export default

Opa, fala pessoal, tudo certo com vocês? Vamos lá para mais uma aula de JavaScript, onde na aula de hoje nós vamos ver os conceitos de modules JS.

Basicamente é um método muitíssimo importante de você entender para poder compreender como é que funciona, por exemplo, a dinâmica que acontece muitíssimo em frameworks, que basicamente é o conceito de importar e exportar arquivos JavaScript, onde suponha que você queira criar um arquivo só de string, de funções e tudo relacionado a string você vai colocar em um arquivo específico e outro só de números, isso aqui a gente só trata de funções de números. E aí eu quero utilizar os dois em um arquivo só, aí eu dou o export em cada um desses e dou o import nesse principal, onde eu posso utilizar todas as funções que eu tenho construído. Então é muitíssimo importante da gente entender esse conceito. No mais, vamos lá. Beleza pessoal?

## Por que separar em arquivos

Então, como eu já disse para vocês, é uma forma de exportar e importar módulos de código no JavaScript, tópico importantíssimo para a gente entender a dinâmica de frameworks.

Lembre-se pessoal que, por exemplo, nas aulas anteriores, quando a gente estava falando de funções, vamos supor que eu queria criar uma função de área retângulo. Então isso aqui é mais voltado para números ou então polígonos, onde eu coloco aqui return a vezes b e ele vai retornar para mim a [área] do retângulo.

E aí eu tinha feito, por exemplo, uma outra função chamada upperName, onde eu literalmente entro com uma string e ele vai me retornar a própria string, só que com a função upperCase, para poder ele me retornar o nome em caixa alta, com todas as letras maiúsculas.

E aí se eu fosse utilizar o meu código, eu colocaria console.log, chamaria a área do retângulo, vamos supor 2, 2, ele iria me retornar aqui 4 ou, por exemplo, eu poderia também colocar o upperName, em que eu colocaria aqui uma string chamada teste e ele voltaria para mim a mesma string, só que com as letras maiúsculas.

Vocês percebem que dessa forma ela não é muito organizada, em um mesmo arquivo eu estou tratando de funções que são respectivas ao retângulo, outra de string, então eu não consigo organizar da melhor forma o meu código. Então é interessante, por exemplo, eu ter um arquivo JavaScript que eu tinha criado aqui só para retângulo, onde a gente vai colocar todas as funções de retângulo aqui dentro e outro só para string, e aí eu consigo exportar essas duas e trazer aqui para dentro, então vamos fazer isso utilizando esse método.

## type="module" e o Live Server

Primeira coisa que a gente precisa saber para poder isso funcionar de fato é você colocar o atributo aqui chamado type="module", para poder ele funcionar dessa forma ele precisa ter essa característica aqui e além disso o seu código precisa estar rodando em um servidorzinho, então é muitíssimo importante que você se lembre de baixar e instalar o Live Server, que ele cria um servidorzinho para poder a gente rodar a nossa aplicação, que é chamado Live Reload, onde quando a gente salva, quando tem algum tipo de modificação ele automaticamente atualiza a nossa página e a gente consegue verificar as mudanças em tempo real, então é muitíssimo importante a gente ter isso para poder funcionar.

## export e import nomeados

No mais, eu criei o arquivo retângulo.js e a string.js, então dados dessas cláusulas para poder funcionar, vamos escrever as funções, vou recortar essa função aqui da retângulo e também vou fazer um function, por exemplo, perímetro retângulo, onde mais uma vez eu vou passar o lado A e o lado B como parâmetros e o return vai ser o quê? 2 vezes o lado A mais 2 vezes o lado B e ele vai me devolver o perímetro desse retângulo, vou até colocar entre parênteses para poder dar ênfase na multiplicação por mais que não seja necessário, então eu tenho duas funções aqui e eu vou colocar essa função upperName aqui dentro do string.

Então já coloquei essas duas e eu quero que esse meu aplicativo aqui leia esses dois arquivos e aí eu consigo utilizar essas funções aqui, vocês podem ver que se eu vir aqui em salvar, ele vai falar a referência erro, ou seja, a área retângulo não está definida, então ele bateu nessa função aqui, não achou ela definida em lugar nenhum e não está funcionando.

Export na frente das funções e agora eu consigo dar o import e aí eu consigo estabelecer, por exemplo, o nome das funções, ou seja, área retângulo, o VS Code já é inteligente que ele já leu o arquivo, já conseguiu identificar para mim que existe essa função área retângulo lá dentro e quando eu aperto enter, ele já completa para mim e eu coloco from e aí o caminho do arquivo, no caso, como está no mesmo diretório, eu faço ponto barra e aí eu seleciono o retângulo.js, então olha só, área retângulo, estou chamando ele aqui, ele já vai funcionar e vai me devolver quatro, por exemplo.

Agora ele deu erro no upperName, onde eu vou fazer exatamente a mesma coisa no upperName, então vamos lá, está funcionando, agora, por exemplo, se eu for utilizar o perímetro, você vai ver que ele também não está definido, porque eu não chamei ele aqui, então para poder chamar mais funções, eu preciso colocar aqui perímetro retângulo para poder ele funcionar e agora está funcionando perfeitamente, está bom?

## Exportando um objeto

As funções, isso me obriga, por exemplo, que eu saiba exatamente o nome da função, concorda comigo? Se eu tivesse, por exemplo, uma biblioteca gigantesca, a gente está falando de retângulo.js, que só tem duas funções, a string.js só tem uma função, então eu consigo muito bem vir aqui nesses arquivos, abrir eles e ver qual é o nome da função para poder chamar aqui, agora vamos supor que você esteja com uma biblioteca gigantesca, isso aqui é praticamente impossível, você não vai adivinhar o nome da função, então é muito comum que essas exportações aqui sejam feitas por objetos.

Então eu posso criar, por exemplo, aqui um objeto chamado const retângulo, onde eu vou criar um objeto, como é que eu crio um objeto? Eu declaro abrindo e fechando chaves, onde, pessoal, eu simplesmente vou chamar essas funções aqui, então eu vou declarar aqui a área retângulo, e vou chamar aqui a perímetro retângulo, são duas funções e aí eu estou construindo um objeto com essas duas funções aqui, e em vez de dar o export nessas funções, eu venho aqui e dou um export do retângulo, vamos lá, retângulo, um export do próprio retângulo, e aí eu vou exportar ele como default.

Ah, Násser, para que você está exportando ele como default? Porque vocês vão ver já já, agora, ao invés de fazer isso com as funções, eu consigo fazer diretamente com o objeto, então eu posso declarar aqui retângulo, está vendo que ele está chamando o objeto e aqui eu vou declarar o objeto, retângulo.perímetro, então vamos ver se funciona, está devolvendo o 8, e aí eu posso colocar, por exemplo, area, e agora ele está devolvendo 4, certinho, está vendo, gente?

Então, esse método aqui justamente vai facilitar a gente organizar, ter vários arquivos sendo exportados, sendo importados, e essa é a dinâmica que é importante a gente entender.

## Por que default

E uma outra coisa que eu não expliquei é a questão do default, por que eu coloquei, por exemplo, default aqui? Vocês vão perceber, pessoal, que às vezes eu não vou saber exatamente o nome do objeto, que está sendo exportado, então importado, vocês podem ver que eu coloquei aqui retângulo, que é exatamente o nome do objeto aqui, porém, contudo, entretanto, vamos supor que essa biblioteca aqui seja gigantesca, e eu não saiba exatamente qual é o nome do objeto lá, mas eu sei qual é, por exemplo, a dinâmica do que se trata esse objeto, e aí eu vou dar um nome para ele, e aí eu vou dar um nome totalmente aleatório, teste, e se eu chamar esse mesmo teste aqui, ele vai funcionar do mesmo jeito, tanto a area como o perímetro, 8, por que?

Porque eu exportei ele como default, ou seja, quando eu faço o export e o import dessa biblioteca aqui, automaticamente ele vai trazer sempre esse, por mais que eu não tenha declarado o nome exato dele.

É lógico que você não vai colocar teste, colocar nomes aleatórios para poder chamar, é bom que você tenha semântica no seu código, então se você for colocar retângulo, rectangle, se eu posso colocar muito bem em inglês, rectangle, chamar que ele vai funcionar perfeitamente, tá bom pessoal?

Então, é isso aí, modularização de código JavaScript, até a próxima.
