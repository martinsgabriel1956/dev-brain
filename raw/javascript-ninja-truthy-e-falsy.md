# JavaScript Ninja: truthy e falsy

Olá, voltamos com a quarta aula do nosso curso JavaScript Ninja, e agora vamos falar dessa treta chamada [truthy e] falsy. Que quer esse negócio de falsy?

## O que é truthy e falsy

Então, sim, no JavaScript, quando você precisa avaliar um valor novamente, quando você precisa, quando você precisa testar alguma coisa, como if, por exemplo, o if, basicamente ele precisa de um valor booleano para verificar se ele tivesse um valor em torno de um valor booleano para verificar se ele entrou, ou falso pra ver se ele entrou naquela condição sine qua non. Se você me sai fora daquela instrução.

Então, basicamente, falou isso chama é falso. O seguinte: valor truthy é todo aquele valor que, booleanamente falando, digamos assim, sei que existe a palavra, ele é representado por true. E o falsy é o contrário: é todo um valor que, quando se converte para booleano, ele, e ele é representado por false.

Então vou dar um exemplo pra vocês aqui. Por exemplo, tínhamos como testar se um aqui é igual a letra B. Um número, na verdade, não é igual a letra B. Então ele vai retornar pra mim um valor, um valor falso.

Só que se eu testar pelo valor, por exemplo, ele vai me retornar um. Como eu, que eu sei, como eu faço pra saber se esse valor é um booleano ou não, se ele é verdadeiro ou falso? Novamente, fica indiferente: testa com o if.

Então, por exemplo, eu vou querer que uma variável de teste, tente fazer o teste aqui. Então eu tenho uma variável no teste desse tempo que Anna que verificar: if, está no teste vai receber [true]. Se isso for um senão, teste vai receber falso.

Então vou ver qualquer valor da variável teste: leva o teste, ou seja, na verdade ele, e ele é um valor verdadeiro.

Agora, por exemplo, vou testar uma 2.0: se ela for verdadeiro, 5.0, o rendimento do teste vai ser ótimo; se não, teste vai ser falso. E agora só o teste, na verdade, é falso. Ou seja, um zero, ele é um número também, comum, entendeu? Mais um, ele retorna, e ela retorna falso. Ou seja, isso é o perfil falso no JavaScript.

## Valores falsy

Então, basicamente, como eu sei quais são os valores de fora e quais são os valores apresentados por Fausto Silva, que retorna, booleanamente falando, false, false? E os valores falsos são definidos no nome, ou seja, não é número, do caso que ele ama, ele é um tipo de número, mas ele não é nulo, então ele é falso por escrito.

O número 0 está como a gente viu ali no exemplo. O número menos 0, que ele, JavaScript, eu posso usar o menos com o zero para dizer o que é um zero negativo; na verdade, era negativo igual a zero, então zero, menos 0. São Paulo é uma string vazia, tanto com aspas simples como com aspas duplas.

Então a gente fazendo o teste aqui vai ser verificado. Por exemplo, vai fazer um teste aqui: if, string vazia. Isso sempre que eu quiser testar somente um valor: string vazia, foi tudo muito bonito. Se não fosse assim vazio, o teste vai ser, vai ser falso.

Então aqui o valor do meu teste é falso, porque esse vazamento era falso.

Se eu testar aqui, por exemplo, por uma string já preenchida, ainda que seja com zero mesmo, mas é uma string preenchida. Então, se o banco deixe esse símbolo retorna true, se torna falso.

5 x 0. Falso.

Então, sim, e se o zero dentro de uma string, ele foi true, ele for um valor truthy, ele vai, então vai dizer que o teste vai ser. Se não, de ser falso. Tudo o que acontece?

Olha só: o zero, na verdade, dentro da string, ele não é a mesma coisa que um número zero. O tal número zero, ele, ele vai representar um valor falso, mas o zero dentro da lei vale tanto, ou seja, mais tinha preenchido, seja ela qual for. Pode ser Fernando aqui, por exemplo.

Fausto. Ele vai retornar true. Por quê? Porque uma string com valor, ela é igual outro. Então diferente. Se defende e se fala de fortuna. Se não vencer, false, false. Ok.

O null também é a mesma coisa. O null é um valor falso. Então se ele foi, eu fiz o teste bem ser. Se não, o teste vai ser falso. A ONU também é falsa.

Agora, por exemplo, um objeto. Tem lá um objeto vazio, por exemplo. Eu vou testar se ele foi até o fim do teste. Caso contrário, se o teste vai ser falso. Você pode ver que o objeto vazio.

Aí o array também. A mesma coisa. Teste, sim; teste, falso. Então array também, acho que você pode ver.

Na Arena. Ora, se ele foi, no final o teste vai ser falso. Então na Arena também é falso.

Ok, então, basicamente, eu pode ver que a gente testou a falha de novo, na Arena. Aí sim, no Vazião, o zero. Quer testar o menos zero também? Vamos verificar. Pelo menos zero, o que menos 0. Também é falso.

Qualquer outro valor, por exemplo, 2. O valor do modelo true é true.

Ah, e também esqueci de colocar aqui o valor false. false também apresentado como falso, dá um valor falso, né. Obviamente ele é falso. Esqueci de colocar aqui, mas o valor falso também é falso.

Beleza, então esses são os valores falsos. Quais são os valores [truthy]? São todos os outros. Então qualquer outro valor que seja diferente de ano e fale, de 0, menos 0 e string vazia, tanto com aspas simples ou com aspas duplas, é o false. Qualquer um desses valores, ele vai ser falso. Fora isso, todos os outros valores são [truthy]. Beleza, então algo bem simples, ainda é facinho de verificar.

## Dupla negação (!!)

E tem uma forma de [a] gente descobrir como a representação booleana de um valor sem utilizar o if, que são utilizar duas vezes o sinal de sinal de exclamação.

Então, por exemplo, vamos ver como é que funciona. A gente viu aqui operar o operador, o navio de informação, ele nega o valor. Então, por exemplo, se eu tenho um valor alto, ele vai se tornar falso, certo? Se eu tenho o valor que o valor não é verdadeiro, ele vai converter no valor booleano, certo, e vai fazer isso, é o contrário, então você vai ser falso. Se ele era falso, ele vai ser true.

Ok, pra saber exatamente o valor booleano, que assim, um, 1, 1 único, um único sinal de exclamação, ele converte para booleano, inverte valores. Então, basicamente, a ideia de usar dois sinais de booleano é aquilo que ele faz: e converte para booleano, inverte o valor, ele comete um mudando de nome em vez de o valor de novo.

Então o true vai se, com duas vezes, o banco usa, era falso. E o 2, true; Fernando, e true. A string vazia aqui: ele inverteu o valor, artigo vazia, false. Se está a string com aspas duplas vazia, também é false. false, false, false, obviamente. Ok, eu tenho 8 1 8 0 dentro da historinha: true, tá.

Então, basicamente, esse formato que você é, que você pode utilizar para testar novamente o JavaScript, que ele já faz conversão de tipo. Vai, vai ver mais pra frente sobre a conversão de tipos também, está, mas basicamente, e essa é a forma mais fácil, mais prática de você descobrir um valor é truthy ou falsy no JavaScript.

Que você quer, assim, que você consegue testar o JavaScript, novamente ele faz essa, essa, essa conversão automaticamente, você não precisa fazer manualmente. Dificilmente você vai precisar, novamente, mas se por acaso você precisar, essa é a forma mais prática: que você usa um if, ou você pode usar essa representação com um dois exclamação. Da mentira mais pra frente qual vai ser o uso disso, quando o cliente vai poder usa isso, se é realmente interessante utilizar esse formato. A gente vai verificar isso mais pra frente.

Beleza, então era isso que eu tinha para falar sobre truthy e falsy como você. E agora vai conversar um pouco sobre o condicional ternário, mais incentivo, vai falar no próximo vídeo. Valeu, até.
