# JavaScript Ninja: métodos de objeto

Voltamos com a nossa terceira aula do curso JavaScript Ninja. Não foi nada daquilo que eu estava falando com você sobre propriedades de objeto, certo? Eu comecei a falar sobre propriedade [de] objeto, daqui a pouco já comecei a falar sobre, e sobre como atribuir função com uma variável, que isso tem a ver, na verdade, com objeto. Então vamos ver na prática o que isso tem a ver.

## Função atribuída a uma variável

Foi aqui que eu estava mostrando que funções, elas podem ser... elas podem ser atribuídos a variáveis. E eu vou mostrar para você mais uma coisa legal aqui. Estou, como estava mostrando, um posso de uma variável chamada Mayday, por exemplo, que ela pode ter uma função atribuída a ela. Ela vai retornar um valor... humano, vai fechar.

Foi um jogo que você chama viu mais vai, ele vai dizer que ela é uma função, e eu posso invocar ela usando o operador de invocação em função, que são os parênteses, abre e fecha, certo?

## Método

O que isso tem a ver, na verdade, com os objetos que eu estava falando? Porque só as propriedades do objeto, um objeto como você, ele pode ter... ele pode ter as propriedades, e a propriedade, ela vai receber o nome [e] um valor, e esse valor, ele pode ser um valor primitivo, como se viu, ou ele pode ser também um outro objeto.

Quando nós atribuímos a uma propriedade de um objeto uma função, nós chamamos essa propriedade de método.

## Reatribuir o objeto × notação de ponto

Então, basicamente, o que acontece: se eu tenho uma variável chamada objeto, eu vou querer uma variável aqui chamada objeto, ou melhor, porque ele é uma variável chamado pessoa. Vou pegar o mesmo exemplo que eu tinha colocado lá.

Vamos ver se que Fernando, ele vai ter uma idade, 30, ele vai ter uma altura, um ponto oitenta e cinco, e vai ter um peso, 85 quilos.

Só que essa, esse objeto pessoa, ele tem uma idade, ele tem um nome, ele tem uma altura e ele tem um peso, certo? Lembrando: se eu quiser acessar o nome dessa pessoa, pessoa ponto o nome, o acesso o valor do nome, está só aqui.

Esse objeto, essa pessoa, ele faz, ele... ele fala só isso, normalmente. Eu não sou idoso de você. Elas vão ser criadas com as nossas propriedades. Como eu faço para criar, então, o método, no caso? Como eu faço?

Então, para ter um método de um objeto, eu vou usar a pessoa, vou usar notação de objeto. Porque se eu atribuir novamente qualquer tipo de valor, vou mostrar, que eu tenho um objeto na pessoa. Eu quero atribuir uma nova propriedade. Se eu usar essa aqui de variável e atribuir novamente um valor aqui, por exemplo, sexo masculino, por exemplo, eu fizer isso, quando eu acessar a variável pessoa, eu perdi todas as minhas outras propriedades, porque eu atribui novamente um outro objeto. Um segundo objeto, que tem uma propriedade chamada sexo, que o valor de propriedade masculina, masculino.

Então, se eu quiser que ela, que um objeto já criado, ele tem outras propriedades, eu preciso usar a notação do ponto.

Então vamos lá: a pessoa vai receber um objeto aqui: nome Fernando, idade 30, altura 1 ponto 85. Isso porque eu nem sei o que o sexo masculino está.

Agora eu tenho uma pessoa com todas as minhas s... uma pessoa com todas, com todas as propriedades que eu queria definir. Se eu quiser definir, então, uma nova propriedade para essa pessoa, serei eu, por exemplo, pessoa ponto cor. Aí eu preciso utilizar essa notação aqui. Se eu atribui diretamente ao objeto pessoa, você me que todo ele. Eu vou pegar somente o... vou criar uma propriedade chamada cor e vou colocar aqui uma cor, caucasiano.

Agora, se eu acessar o meu de outra pessoa, eu tenho todas as minhas propriedades que eu tinha criado, inclusive a cor. Precisa acessar a pessoa ponto, ponto cor, vai aparecer que caucasiano.

Beleza. Então, se você atribui novamente um outro objeto pra uma pessoa, você vai perder tudo o que você tinha até então. Novas atribuições, sempre utilizando essa notação aqui: o nome do objeto, ponto, o nome da propriedade, é igual, o valor que você quer passar. E na hora da criação do objeto, utilizando as chaves: da propriedade, dois pontos, no valor; de propriedade, dois pontos, o valor; da propriedade, dois pontos, o valor, certo? Sempre separando as propriedades por vírgula e atribuindo a ela utilizando o sinal de dois pontos. Beleza.

## Método andar

Eu estava falando, estava falando sobre os métodos do objeto. E os métodos do objeto, ele podem ser, basicamente, ações que eu vou atribuir a essa pessoa. Então, por exemplo, eu quero fazer essa pessoa, da pessoa ponto andar. Isso vai ser um método.

Então eu... eu queria uma função aqui, mas eu vou retribuir para colocar um valor aqui, pessoal a ponto onde você mandar a pessoa andar. Eu vou retornar, por exemplo, "estou andando". Como faço pra pessoa?

Então aqui eu tenho todas as minhas propriedades, e tenho mais a minha, o meu método andar aqui. Como faço para evocar o momento? Não anda mesmo em cima da variável: pessoa andar. Só que o executivo é simétrico, ou seja, um bloco ensinou o método utilizando a notação de abre e fecha parênteses, tá. E isso vai dizer que a pessoa está andando.

## Método aniversário

Estávamos falando uma coisa um pouco mais útil. Então, com relação a isso, está numa coisa um pouco mais útil. Com relação a isso, vamos fazer com que essa pessoa, ela, ela faça o aniversário, cara de escola. Faça aniversário: a idade dela venha, venha a aumentar. Minha mãe me subiu maduro com meu nome, e a gente faz isso.

Pensei que se fosse essa pessoa ponto idade, eu vou poder acessar o valor de 30, que é a idade dessa pessoa. Que você tem que acontece?

Eu vou criar um método chamado aniversário, que vai ser uma fantochada. E esse método, ele vai fazer o que ele é... ele não vai retornar nada, na verdade, mas ele vai fazer com que a idade dessa pessoa aumente um ano. Como é que eu vou fazer isso? Como o acesso à idade dessa pessoa: pessoa ponto idade, mais mais. Adicionar mais um, mais um valor na idade dessa pessoa.

Então, se você sabe a vida da pessoa, que eu tenho uma idade de 30 anos, sem invocar a pessoa ponto aniversário. Vou evocar essa função aqui: que vai acontecer? Não retorno nada, certo? Porque a minha função não retorna nada. Mas... mas se eu acessar agora obrigando a pessoa a só idade, que aconteceu com ela? Você mesmo: a função de aniversário aqui, ela incrementa um ano na idade.

Você lembra que o operador, o operador binário mais mais, ele vai incrementar o valor e vai automaticamente atribuir aquele valor? É exatamente o que acontece com o nosso objeto.

## Método nome completo

Então, por exemplo, se eu quiser adicionar um sobrenome por Fernando Pessoa, minha pessoa, eu posso adicionar pessoa de sobrenome igual Daciuk, por exemplo, que o meu objeto pessoal agora tem um sobrenome também.

Agora eu posso querer um método chamado nome completo. Eu vou criar uma função com ele, e eu vou retornar o que... eu não vou modificar nada. Simplesmente vou retornar pessoa ponto o nome, mais um espaço, mais pessoal ou ponto do sobrenome. Assim que venceu meu, meu método. Então agora eu tenho em pessoa... tenho um método chamado o nome completo, e esse método, um nome completo, que ele vai retornar o nome completo da pessoa. Realmente funciona: a pessoa ponto um nome completo me retornou Fernando Daciuk.

Então é basicamente dessa forma quem vai trabalhar com objetos JavaScript. Está em fazer fase, vai fazer mais alguns exercícios. Eu vou mostrar para você mais algumas, mas algumas coisas legais que a gente pode fazer também com objetos, mais no próximo vídeo, que você já deu um tempo. Então, até o próximo.
