# Criando o controller de usuários e o sistema de rotas

O nosso código já está funcionando, mas para escalar isso daqui, para começar a colocar muita coisa aqui dentro, não vai rolar por dois motivos. O primeiro deles é óbvio, né? Que nossas rotas, elas estão hoje... Cada nova rota que a gente for desenvolver, no caso, que a gente for criar aqui dentro, a gente vai ter que fazer essa condicional de URL e método. Então, assim, imagina como é que vai ficar esse negócio.

E o segundo problema é a regra de negócio. Hoje ela está toda aqui dentro. Então, beleza, aqui é uma coisa muito simples, né? Mas conforme isso aqui for crescendo, na hora de cadastrar um usuário, por exemplo, se a gente estivesse trabalhando com emails, a gente precisaria verificar se o email que o usuário está tentando, que a requisição está tentando cadastrar já não está inserido no banco de dados e tudo mais. Então, isso aqui vai ficando muito grande e insustentável.

## O controller

Então, a primeira coisa que a gente vai fazer é mover essa regra de negócio para dentro de um carinha chamado Controller. Então, eu vou criar uma pastinha chamada Controllers. E aqui dentro, eu vou ter o meu UserController.js. Beleza?

Então, um controlador é o responsável por armazenar toda a regra de negócio da nossa aplicação. Então, no caso aqui da nossa API, a gente vai ter um CRUD de usuários. O que é um CRUD? Então, CRUD são as operações de create, read, update e delete. Ou seja, criar um novo usuário, fazer o get, então pegar os dados de todos os usuários ou de um usuário específico a partir do ID, fazer o update em um usuário ou remover um usuário. Então, todas as funções que vão armazenar essas regras de negócio aqui, elas ficam dentro do nosso Controller. Beleza?

Então, eu vou começar fazendo o seguinte, module.exports. Vai ser um objeto, a gente vai trabalhar com classes a partir do próximo módulo. Mas para deixar as coisas um pouco mais simples, vamos de objeto aqui. E aí, eu vou ter o meu método listUsers, que é o método que vai fazer, como o nome já estava dizendo, listar todos os usuários.

Então, eu vou fazer o seguinte, eu vou recortar isso daqui, vou jogar aqui para dentro. Aqui dentro, eu vou receber o meu request e o meu response, que são esses aqui que a gente vai repassar ali para aquele método. E agora, a gente precisa importar o mock de usuários. Então, vou recortar esse require aqui, vou jogar ele aqui para cima. Vou salvar isso daqui, eu acho que é isso aí. Show de bola.

Então, agora aqui no meu index, eu vou dar um const userController, vai ser igual a require ./controllers/userController. Vou pegar esse meu userController e vou chamá-lo aqui embaixo. O meu método, no caso, listUsers, que está lá dentro daquele objeto. E aí, aqui para dentro, eu passo request e response.

Salvo isso daqui, vou executar node src/index.js, deu um errinho, ponto barra mocks. Ah, ok, porque a gente tem que voltar uma pasta, porque agora a gente está dentro de controllers. Então, paro o servidor, rodo ele de novo, e agora no meu browser, olha só, já está tudo funcionando. Então, o primeiro problema, que é esse da regra de negócio, a gente já resolveu.

## O arquivo de rotas

Agora, vamos resolver esse problema das rotas, que, como eu disse, cada nova rota que a gente fosse querer registrar aqui, a gente teria que duplicar essa condicional de if em request.url, método, enfim, então, ficou um negócio bem feio. O que eu vou começar fazendo aqui? Eu vou criar um novo arquivo chamado routes.js dentro de src. E aqui dentro, eu vou dar um module.exports em um array. E esse array vai ter vários objetos, e cada um desses objetos vai representar uma rota da nossa API. Olha só, que legal.

E aí, uma API, ela vai, os dois parâmetros, as duas propriedades. Fugiu a palavra, mas eu acho que propriedades fica legal. As duas propriedades que identificam uma rota, as duas principais, são o endpoint, então, por exemplo, barra users, e o método, para a gente identificar qual é a ação que a gente quer fazer em cima do recurso que foi identificado no endpoint. Então, basicamente, é isso aqui. Se a gente tivesse depois lá, se a gente tivesse não, a gente vai ter a nossa rota barra users do método post, vai ter também aqui o get para pegar o usuário por ID, enfim, mas daí depois a gente entra nisso.

Então, cada rota, como eu disse, vai ser um objeto aqui dentro. E aí, além dessas duas propriedades de identificação da rota, eu vou passar uma terceira chamada handler, que é, basicamente, a função que eu quero executar toda vez que essa rota for chamada. Simples assim, bem facinho, né? E aí, qual que é a função que a gente quer executar? É a função aqui do UserController listUsers.

Joia? Então, eu vou recortar, eita, vai, aqui, eu vou recortar esse require aqui que estava dentro do index, vou jogar ele aqui para dentro, e aqui dentro do meu handler eu passo userController.listUsers. E, preste atenção, eu não estou executando a função, tá? Eu só estou passando a referência da função aqui. Então, depois a gente vai executar o método handler, né? Então, seria mais ou menos como se a gente pegasse aqui o nosso array, a array é maravilhoso, né? O nosso array de rotas. Então, routes, zero, ponto handler, e aí eu executo, passando lá o request, response, que é o que ele precisa para funcionar, beleza? Então, por isso que a gente não executa aqui dentro.

## Encontrando a rota com find

Muito bem, então, eu vou salvar isso aqui, e agora, voltando aqui para o index, eu vou começar importando esse meu arquivo de rotas, então, require routes, e aqui embaixo, agora é o seguinte, ó, eu vou comentar tudo isso aqui, e a gente vai fazer o seguinte, eu vou criar uma constante chamada route, e aí, dentro do meu array de rotas, né? Então, routes, que a gente importou aqui em cima, eu vou fazer um ponto find para procurar um elemento dentro da minha lista, né? Dentro do meu array, do meu vetor de rotas.

E aí, aqui dentro, a gente passa uma função, essa função, ela recebe aqui, qual é a rota que ele está iterando no momento, vou chamar de routeObject, então, o que eu quero dizer com isso? Vamos só duplicar aqui para ficar um pouquinho mais claro. Ele vai fazer uma iteração, passando item por item de dentro do nosso array, e quando ele estiver iterando em cima desse item, o valor desse meu routeObject vai ser as propriedades desse meu item aqui, beleza? Dessa posição do meu array.

E aí, o que eu quero fazer? Eu quero verificar se o route, ponto, aliás, routeObject, endpoint for igual, igual, igual ao meu request.url, opa, aqui saiu com R maiúsculo, vamos ver se não importou nada, não. Ah, joia, então, volta para minúsculo. Então, se o endpoint da rota que ele está iterando no momento for igual ao request.url que está chegando na minha requisição e o routeObject, então, routeObject ponto, qual que é o nome? method for igual, igual, igual ao request.method, quer dizer que essa rota aqui, ela existe, né? A rota que o usuário está tentando bater, a gente registrou aqui dentro do nosso array de rotas.

Então, o que eu vou fazer? Então, se route, se essa rota existir, eu vou pegar o route.handler, como eu disse, e vou executar passando request e response. Response, facinho, né? E aí, se ele não encontrar, aí o que ele vai fazer? Ele retorna aqui esse 404 que a gente já tinha. Então, deixa eu jogar ele para cá, show.

Então, salvo isso aqui agora e olha só que legal, eu vou parar o meu servidor, vou executar de novo, está rodando, não quebrou nada. E agora, quando eu atualizo aqui dentro, olha só, ele continua funcionando.

E agora, se a gente quiser registrar uma nova rota, a gente só precisa duplicar isso aqui, eu vou colocar aqui, por exemplo, produtos. E aí, ele vai chamar aqui também listUser. Então, hoje, se eu acessar aqui barra produtos, barra produtos, ele não funciona, né? O cannot get ali. Aí, eu vou salvar, paro o servidor, executo de novo e agora, olha só, produtos, está funcionando. Fica muito mais fácil, né? E a gente não precisa mais ficar fazendo aquele mundaréu de if else.
