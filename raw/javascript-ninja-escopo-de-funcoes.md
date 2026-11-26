# JavaScript Ninja: escopo de funções

Olá. Estamos com um curso JavaScript Ninja e o Fernando Daciuk aqui, e agora nós vamos continuar nossa [aula] normal depois de fazer a correção.

Algumas pessoas tiveram um pouco de dificuldade de fazer o exercício o insistiu o desafio 8, mas nós vamos voltar a fazer alguns exercícios para exercitar um pouco melhor o nosso... A nossa programação funcional está totalmente bem. Durante as aulas, durante as próximas aulas e durante os próximos desafios, a gente vai querer bastante coisa funcional pra gente treinar bastante esse tipo de programação, que a gente vai ver que vai ser bastante útil pra gente mais pra frente.

## Função dentro de função

Continuando falando de funções, como conversar um pouquinho sobre o escopo de funções. Então, [a] gente sabe que isso, uma função dentro de outra função, é permitido. Mas como fica o escopo dessa função? Como fica o escopo? Então vamos mostrar de uma forma prática, mais ou menos aqui, que eu estou... O que eu estou querendo dizer.

Exemplo: vou acessar aqui um arquivo minha a ponto de voltar para fazer algumas alterações, porque eu vou criar aqui uma função... ou criar uma função que está de uma função myFunction. E essa função, ela vai retornar a soma de dois números, por exemplo. Será que esses dois números, eles vão vir [de] uma função chamada sum. E essa a função, ela vai ser criada dentro da função, mas falando sobre o que eu vou fazer aqui, tenho mais dois exemplos. Não vou passar um número por parâmetro, só vou simplesmente executar essa função.

Eu estou fazendo isso aqui. Que eu fiz aqui: eu criei uma função chamada myFunction e dentro dela criei uma outra função, retornando 1 mais 2, o retorno da minha função principal, de minha função mãe, falando que vai ser essa função só invocada, que eu não dei o nome para ela. Agora sim não funciona.

Então eu dei o nome de uma função chamada sum. Retornei aqui 1 + 2 e fiz o retorno da sum invocado. Então, teoricamente, o resultado dessa função, quando é invocada, é para me retornar 3. Vamos ver se isso funciona. Então o console.log, para mostrar o nosso resultado no console, e vamos colocá-la, myFunction, e vamos executar ela. Ok.

Então vou mostrar que o conteúdo do arquivo que eu fiz. Então a função aqui é myFunction, dentro dela uma outra função, e o retorno vai ser a invocação dessa função. Quando eu executar, no meu ponto de vista, esse retorno vai ser 3. Ok. Ou seja, eu já sei que com isso a gente entende que é possível criar, então, uma função dentro de outra função. Eu consigo utilizar essa função ali dentro.

Agora, por exemplo, será que eu consigo utilizar a função sum fora da função myFunction? Eu vou mudar o mundo. Como descobriu isso? Eu conto JS aqui. Eu vou colocar no final do meu arquivo, mandar um console.log, que eu vou tentar executar a função sum. Funciona? Será que funciona? Então vou dar um pocket aqui pra você visualizar. Então eu só coloquei mais um console.log e tentei executar.

Olha só o que acontece quando eu executo esse cara aqui. Olha só, JavaScript: ele retorna o 3, que é o retorno da myFunction, como primeiro leitor aqui. Só que na hora de tentar retornar o sum, ele disse que sum is not found. Porque é que usuário define? Porque foi criado dentro da função.

[O] que a gente consegue entender com isso? Da mesma forma que variáveis, ela tem o escopo, e o escopo de uma variável, o escopo de função, as funções também criadas dentro de outras funções, o escopo dela é aquela função onde ela está dentro.

Então, basicamente, o que acontece é o seguinte: eu crio a função sum dentro de myFunction. Para eu externar essa função, ou analisar ela, ou usá-la fora, que eu precisaria ter criado essa função sum de fora de myFunction. Ou seja, a função sum, ela só existe enquanto myFunction existia. A partir do momento em que myFunction não existe mais, ou seja, ela já foi mencionada e não existe mais, eu não consigo acessar a função interna.

## Variáveis no escopo da função

Da mesma forma, se criar uma variável aqui dentro. 7. Eu, por exemplo, se eu criar aqui uma variável, vai o ano igual a 1 2 2. Se eu tentar acessar... não... a meu ver a função do santo consigo ver retornando.

É o que fiz aqui dentro: que eu criei duas variáveis, uma variável chamada number1 e uma variável chamada number2, e na variável sum eu retornei a soma dos valores dessas duas variáveis. Isso aqui funcionaria? Isso aqui funciona. Sim, funciona. Por que é que isso aqui funciona? Porque o escopo dessas variáveis aqui valem para toda essa função. Olha só que legal. Então essas variáveis, elas estão disponíveis dentro da função inteira, desde o início da década do início de dentro da função até o final dela. Essas variáveis, elas existem, inclusive se eu retornar aqui...

Um exemplo: eu tenho essas duas variáveis. Estão disponíveis aqui dentro, dentro do escopo da minha função myFunction, e a função sum, ela está disponível dentro da função, da função sum. Eu consigo acessar valores dessas duas variáveis. Também não consigo acessar porque ele está dentro de myFunction.

Então, o sum aqui, a gente vai ver mais para frente o que é isso. A sum está fazendo o papel de uma coisa que é uma coisa, é uma função que ela consegue acessar parâmetros externos a ela. Então eu não consigo acessar de um show aqui. Eu não conseguiria acessar um valor, por exemplo. Mas se eu consigo acessar essas variáveis que estão aqui fora. Então aqui a gente viu que essa questão de escopo, ela realmente... ela realmente funciona.

## O posicionamento importa?

Agora, será que o posicionamento das minhas, nas minhas variáveis, ou da minha função, contém alguma coisa? Como assim, você diz, o posicionamento? Vamos verificar aqui. Você sabe que Mark brilha, e vou fazer o seguinte: eu vou deletar aqui essas duas linhas. Eu vou criar ainda dentro da função... Olha só, eu não sei se você lembra o que eu falei aquela vez sobre ela, sobre variáveis, mas olha só o que acontece aqui. Eu crio uma variável aqui, passar uma, vai passar dois.

As variáveis estão dentro da função, certa? E a função soma, ela está sendo criada antes. Ela está sendo criada antes dessas, dessas variáveis, que se tornam o que são. Isso aqui vai funcionar? Vamos ver o que isso aqui vai retornar. Você chama aquilo noite, e ele vai continuar retornando 3. Por que retorna 3? Por que, quando que ele retorna 3, se eu tenho aqui uma função, eu crio as minhas variáveis aquilo depois, depois de chamar essa função aqui, é que eu estou fazendo uma oitava edição. Eu publiquei. Isso aqui funciona.

Então isso funciona pelo seguinte: quando eu crio minha função, eu crio minha função sum, quando é a vez que ele passa por aqui, ele simplesmente verifica que essa função aqui existe, mas ele não executa. Então você ainda não sabe se o número ou ainda existem. Está aí que acontece: eu declaro que as minhas variáveis, não, declarei as minhas variáveis, passei valores, agora elas têm valores, e logo depois eu faço a invocação da função sum. Como eu não fiz o retorno da função que no final chamei ela depois, então ele vai, como foi declarado o Mamberti, ou ele vai continuar enxergando o nome, eu não tive aqui, porque a hora que ele foi executado é aí que ele vai tentar ver se tu tem algum, tem algum valor. Certo?

Então, o que é que consegue isso? Por enquanto, é algo, algo bastante simples, algo bastante comum, está acontecendo. Então eu queria que eu crio uma função. Então você viu que, independente de onde declarei as minhas variáveis, eu criando uma função, no caso, se eu crio uma função geral, que nesse caso o que eu crio a função sum dentro de myFunction, eu consegui acessar os valores de Ana, independente da posição que eles foram criados, contanto que ela seja invocada somente depois que esses valores fossem criados. Está?

## Função depois do return

Agora, promoveu um outro exemplo, um pouco diferente do que acontece aqui. Você sabe que o meu único ponto JS está... E agora, se eu fizer o seguinte, você sabe que o Banco de Fomento pode morrer. Se eu pegar essa função de estado e eu colocar ela depois de oito anos, você acha que vai acontecer nesse caso? Olha só: eu estou criando as variáveis aqui, declarando as minhas duas variáveis no meio do ano. Então, aumentar aqui para ficar um pouco melhor de visualizar.

Então, por exemplo, eu estou aqui criando as minhas variáveis o ano meio, e eu estou fazendo o retorno edição. E você sabe, a gente já viu que tudo que acontece depois do return o JavaScript simplesmente ignora. E agora, depois, eu entendo, eu estou criando a minha função sambista retornando na mesma noite. Isso aqui será que funciona? O que você acha? Que vai funcionar? Você acha que não vai pressionar? Vamos experimentar para ver. A gente tem que tentar naquela linguagem até descobrir as coisas que acontecem com ela.

Então aqui tem um retorno, retorno, retorno. Teoricamente, o que aqui deveriam... deveria fazer isso, que deveria retornar undefined, porque o teoricamente ainda não existe. Estou retornando a ele. Eu estou criando o meu sum depois do meu retorno. Mas, para nossa surpresa, olha só o que acontece: eu consigo executar me normalmente a função. Que imagino que acontece? Que magia é essa? Por que é que eu consigo retornar o sum ainda depois de, sabendo que depois do return não acontece mais nada na função, JavaScript simplesmente ignora, e sabe aquela função? Porque o que é que magia é essa? E o que é que acontece pra que isso realmente vai funcionar?

Na verdade, o que acontece é algo chamado hoisting, que é o hoisting. A gente vai ver no próximo vídeo. Valeu.
