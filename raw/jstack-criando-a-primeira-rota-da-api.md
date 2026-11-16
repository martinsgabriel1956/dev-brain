# Criando a primeira rota da API

Vamos começar criando o primeiro endpoint aqui da nossa API, que vai ser o endpoint responsável por listar os usuários da aplicação.

## Lendo o método e a URL da request

Então aqui em cima eu vou primeiro colocar um console.log e aqui dentro desse meu console.log eu quero logar aqui no meu terminal algumas informações da request que está chegando no meu servidor. A primeira informação que eu quero pegar é o request method, ou seja, se é uma requisição do tipo get, post, put, delete, enfim, qual que é o método dessa requisição. E essa informação está dentro da variável request, que é a variável que a gente recebeu aqui em cima no atributo method, beleza? E o segundo dado que eu quero pegar é o endpoint, que também está dentro de request, mas agora no atributo URL.

Vou rodar aqui o meu servidor, então node src, vou atualizar aqui o meu browser e agora quando eu volto aqui no meu terminal, olha só, aqui embaixo eu já tenho o request method do tipo get, porque como eu já falei, quando a gente acessa o URL direto aqui do navegador, toda vez a requisição vai ser do tipo get e o endpoint barra é o endpoint padrão do HTTP quando a gente não informa nada, então se eu acessasse aqui barra users, aqui embaixo já está o endpoint barra users.

E se para você estiver aparecendo aí uma requisição do tipo get para o endpoint barra favicon.ico, pode ignorar, é uma requisição que o próprio navegador faz para tentar encontrar esse íconezinho que ele coloca aqui na aba, a gente só vai trabalhar com isso quando a gente entrar lá no módulo de frontend de React, beleza?

## GET /users

Muito bem, então eu vou começar fazendo o seguinte, vou criar aqui uma condicional, então se o meu request.url for igual igual igual a barra users, esse carinha aqui que eu estou mandando aqui embaixo, e o meu request.method for igual igual igual a get, seguindo lá os padrões do REST eu sei que essa URL aqui, que essa rota, ela precisa retornar uma lista de usuários, por quê? Porque o método HTTP é o get, ou seja, a gente está tentando obter informações e o meu endpoint, a minha URL é barra users e eu não estou passando nenhuma ID aqui identificando que eu quero buscar as informações de um usuário específico, eu só estou dizendo que eu quero obter usuários, e aí nesse cenário o cliente está esperando uma listagem de usuários.

Então eu vou fazer o seguinte, eu vou pegar esse response aqui, na verdade deixa eu copiar e deixar isso aqui comentado, vou colar aqui em cima, bom, vamos lá, vamos fazer umas alterações aqui, o primeiro, o status code aqui, primeiro o status code, a gente vai manter como 200 porque não tem regra de negócio, isso aqui sempre vai dar sucesso, só que agora a gente precisa mudar o content type, por quê? Porque o tipo de resposta que a gente vai mandar no nosso body não é mais HTML, como eu já falei lá na aula de REST a gente vai trabalhar com o JSON, e aí o content type para indicar que o corpo dessa resposta é JSON, é o application barra JSON, beleza?

## Dados mockados

E agora aqui dentro a gente manda o nosso array, a nossa lista de usuários, aqui a gente não vai trabalhar com banco de dados, a gente vai trabalhar com informações na memória, então o que eu vou fazer, aqui dentro de SRC eu vou criar uma pasta chamada mocks, mocks é um nome que a gente dá para quando a gente vai trabalhar com dados fake, que realmente não vão ser armazenados, enfim, não são dados reais da nossa aplicação, e aqui dentro eu vou criar um arquivo chamado users.js, vou dar um module.exports aqui em um array, e esse array vai ter vários objetos contendo id e name, vou triplicar isso aqui, então vou criar mais dois, então id2 vai ser Rose, id3 vai ser José, vou salvar isso daqui, posso fechar, e agora vou importar aqui dentro do meu index, então const users igual require ponto barra mocks barra users, show.

## JSON.stringify

Bom, só que eu não posso simplesmente chegar aqui no meu end e jogar aqui dentro esse meu array, por quê? Porque dentro do end a gente sempre precisa mandar uma string, então a gente precisa converter esse array em string, e para isso a gente tem uma funçãozinha aqui dentro do JavaScript, que é o JSON.stringify, daí a gente consegue converter array e objetos para strings no formato json, vou salvar isso aqui, posso parar o meu servidor, rodar de novo, e agora quando eu acessar aqui barra users, tá lá então o meu array, a minha listinha de usuários, e no meu caso aqui ele tá formatadinho desse jeito, todo bonitinho, eu posso minimizar aqui, maximizar, porque eu uso essa extensão aqui no meu Google Chrome, se você pesquisar ela no Google, você já vai achar, acho que é o primeiro, segundo link, você faz a instalação no teu Chrome e aí já vai estar funcionando aqui tudo certinho.

## Rota não encontrada: 404

Muito bem, só que agora a nossa API ela tem um problema, se eu tentar acessar aqui por exemplo, uma url que não existe, ele vai ficar carregando eternamente, por quê? Porque a gente não tá dizendo para o nosso servidor o que ele precisa fazer quando a url não for users, ou quando ela for users, mais o método não for get, então eu vou fazer o seguinte, vou recortar isso daqui, então deixa eu descomentar, recorto, jogo aqui para cima, o status code aqui vai ser o 404, porque a gente não encontrou a rota, a gente poderia fazer um tratamento diferente, por quê? Porque a gente tem um código HTTP, um status code específico para métodos não permitidos, ou seja, a rota users existe, mas se o usuário estivesse fazendo por exemplo, um post a gente teria o método específico lá, mas aqui não é muito relevante, a gente vai sempre retornar 404 mais para facilitar a nossa vida, beleza?

Então vou manter text/html, e aqui eu vou fazer aquele formatinho que o Express usa muito, que é o quê? Cannot, opa, Cannot, e aí eu retorno aqui o request.method e request.url, tá? Então vou parar o servidor, executo aqui de novo, e agora olha só, Cannot get barra, se eu tentar acessar aqui qualquer outra coisa, então Cannot get barra asd, beleza?

A gente vai refatorar isso daqui, tá? Vamos mover as rotas para um arquivo separado, até porque imagina agora se a gente fosse fazer o post aqui, enfim, se a gente tivesse outros endpoints, o rolo que não ia ser, ia ter que ficar fazendo um monte de else if aqui dentro, então a gente vai refatorar isso a partir da próxima aula.
