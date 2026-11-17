# Axios: encapsulamento do XMLHttpRequest, CDN e axios.get com then

Opa, fala pessoal, tudo certo? Enfim, vamos lá para mais uma aula de JavaScript, onde nós vamos agora conversar sobre Axios, mais um tijolinho dos conceitos importantes para poder a gente continuar progredindo nesse estudo, enfim, vamos lá.

## O que é o Axios

Basicamente, o Axios, a gente vai fazer exatamente a mesma coisa que a gente tem feito, vocês podem ver que desde lá da aula de AJAX, a gente está sempre tratando do mesmo assunto, só que a gente está refinando a forma de como a gente faz a requisição. A gente está entendendo o que é uma requisição, como é que ele volta, o que ele precisa verificar, quais são as formas de a gente conseguir sucesso, o que a gente pode fazer quando dá sucesso, quando dá errado e tudo mais.

E o Axios, simplesmente, é um encapsulamento do XML HTTP request, ou seja, ele vai fazer exatamente a mesma coisa que a gente fez na aula passada, só que de maneira bem mais enxuta.

## Instalação via CDN

Entendo como é instalar, o exemplo, a API do Axios e várias características que você pode vir aqui.

Então, para poder a gente instalar ele, você pode instalar aqui via npm, yarn, só que como a gente ainda não configurou o nosso ambiente de desenvolvimento, por exemplo, eu prefiro fazer isso quando eu estou literalmente utilizando algum tipo de framework, a gente pode utilizar o código via CDN.

Ah, Násser, não estou entendendo o que você está dizendo. Basicamente, pessoal, é o código em si do Axios, a gente está passando esse código para o nosso navegador ler para quando a gente utilizar os métodos do Axios dentro do nosso JavaScript, sendo que ele tem que ser declarado primeiro, está vendo? É para poder a gente utilizar aqui, dá tudo certo, beleza?

## axios.get e then

Então vamos lá, vou literalmente apagar a promise, porque a Axios, como a gente viu aqui na descrição, ele já é baseado aqui em HTTP request e já é uma promise, está vendo? Ou seja, ele já suporta uma API de promise.

Então vamos lá, olha só como é fácil, pessoal. Olha só o tamanho da parafernália, então eu vou até deixar selecionado aqui, essa parte, vou comentar aqui, e olha só o tamanho da parafernália para poder a gente executar essa coisa.

Se a gente vir aqui e definir simplesmente o Axios e utilizar o .get, a gente pode passar a nossa URL diretamente por aqui, vamos lá, diretamente por aqui. Essa parte aqui, GitHub, para ficar GitHub certinho, onde eu posso aplicar o .then direto nela, porque ela já é uma promise e eu já estou passando qual é o método e já estou passando a URL, então toda aquela parafernália que eu fiz antes simplesmente se resume a isso aqui, onde eu estou definindo o Axios com o método .get, sendo que eu poderia muito bem colocar aqui o método .put, método .delete, método .post, só que no caso é o .get mesmo.

Se eu quisesse colocar um outro parâmetro aqui, eu colocaria ele aqui, mas no caso não é necessário, nós vamos explorar ele um pouquinho depois, mas eu já consigo utilizar o sistema de promise que ele aceita, a API, ou seja, eu já consigo fazer o .then e o .get, então simplesmente ele vai funcionar da mesmíssima forma que a gente estabeleceu antes, ele já tem todos os tratamentos.

## A resposta mais completa

Se eu vir aqui em salvar, ele já me voltou esse objeto aqui e, inclusive, ele me voltou o objeto mais completo ainda, porque ele me voltou o config, está vendo, se eu abrir aqui, config, antes ele só me voltava a data, lembra disso? O cache control, ou seja, meio que são as configurações de metadata e o próprio request, está vendo?

Então ele me volta um objeto mais completo ainda que o próprio XHTML HTTP request, então além dele me voltar mais informações, ser mais completo, ele é mais enxuto em questão de código, em questão de verbosidade de código, onde você consegue fazer exatamente a mesma coisa que a gente fazia, só que de forma mais direta, dinâmica e voltando com mais informações, então muito interessante a gente estar utilizando o Axios em conformidade com as promises e poder usufruir dessas funcionalidades. No mais é isso, até a próxima.
