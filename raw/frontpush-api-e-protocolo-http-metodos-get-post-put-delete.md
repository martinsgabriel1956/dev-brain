# API e protocolo HTTP: API pública, API do GitHub, HTTPS e os métodos GET, POST, PUT, DELETE e HEAD

Opa, olá pessoal, tudo certo? Sejam bem-vindos a mais uma aula de JavaScript, onde, na aula de hoje, vamos conversar um pouco sobre APIs e o protocolo HTTP. É uma aula mais conceitual, onde eu vou apresentar esses principais conceitos que são importantíssimos para podermos entender nas próximas aulas.

O que de fato é uma API, vou apresentar aqui de maneira bem didática o conceito e vocês vão entender esse conceito, que é um pouquinho abstrato, ao decorrer dos exemplos, das explicações que a gente for dando ao longo das próximas aulas, bem como o protocolo HTTP. Mas acho que é interessante eu detalhar alguns pontos aqui.

## O que é uma API

Primeira coisa, o que é uma API? Vocês perceberam que a gente está sempre tentando fazer uma requisição, ou seja, uma busca de informação do front-end para o back-end. O front-end constantemente precisa fazer esse tipo de requisição. E requisição nada mais é do que as informações de padronização que você precisa para poder realizar a comunicação e aí você faz por meio de uma API.

Sempre que você constrói, por exemplo, um back-end, você tem que sempre se perguntar como eu vou me comunicar? Ah, eu vou construir uma API. Essa API, de certa forma, reflete o banco de dados e tem como você acessar essas informações por meio de regrinhas, por meio de documentos que têm uma padronização, nós vamos ver ao decorrer, mas basicamente você acessa via URL, pode ter autenticação ou não.

Ou seja, você pode ser uma pessoa qualificada para acessar aquelas informações mediante uma chave, mediante uma senha onde ele faz essa verificação, essa autenticação, ou às vezes é uma API pública, simplesmente para você consultar determinada informação.

Por exemplo, existe uma API que tem como eu requisitar qual é o tempo em Brasília, por exemplo. Então, quais são as características que eu tenho que colocar na requisição, na URL para poder acessar diretamente o método, o objeto que eu quero, quais são, como eu tenho que colocar a informação Brasília dentro dessa URL para que ele me devolva o JSON com essas informações.

E eu já te falei, esse caso é, por exemplo, uma API pública, porque toda e qualquer pessoa pode fazer requisição, a esse website, sem precisar de uma senha para poder ter essas informações, mas tem outras APIs que não permitem isso.

## A API do GitHub e as Public APIs

E um exemplo, pessoal, eu vou estar utilizando aqui nas próximas aulas também para poder ilustrar, é a própria API do GitHub, que é muitíssimo utilizada nesses casos.

.users, e ele vai me trazer, justamente, um arquivo do tipo JSON, você já consegue identificar o padrão que é com algumas informações, ou seja, eu tenho um login, ele me traz a informação do meu login, ele me traz o ID do meu usuário, o node ID e outras informações do qual eu posso estar trazendo, fazendo essa requisição via HTTP, mas você percebe que é acessando essa API que é pública do GitHub.

Se você tiver curiosidade para poder conhecer todas as APIs do GitHub, é só colocar no Google Public APIs, por exemplo, vai ter uma descrição aqui, ele vai falar de todas as APIs que são públicas, uma descrição, se tem autenticação ou não, se tem o protocolo HTTPS ou não, se tem o CORS, o CORS eu vou explicar também, mas basicamente é quando você faz uma requisição dentro de uma outra requisição, se ele permite isso ou não, porque geralmente isso é bloqueado dos navegadores para poder evitar, por exemplo, que você execute um script dentro de um outro lugar, então é questão de segurança isso aí.

Mas basicamente essa é a ideia, você tem que entender que a API é a forma de como eu acesso a rede de comunicação daquele servidor para poder obter informações, por exemplo, de codificação, de chave, de estrutura para poder eu fazer algum cadastro, fazer algum tipo de requisição, um get, um post, um put, seja lá qual for o método que você estiver utilizando via HTTP.

## O protocolo HTTP e o HTTPS

Ah, você vai estar falando de HTTP, não estou entendendo nada, agora nós vamos lá, o protocolo HTTP, como eu escrevi aqui na sua tradução literal é Hypertext Transfer Protocol, ou seja, é um protocolo de transferência, é um protocolo simplesmente para você enviar e receber dados na web, como se fosse um canal, ele é utilizado para poder eu transferir arquivos, sendo que tem o HTTP e o HTTPS, o S vem de Security e é o mais amplamente utilizado justamente pela questão da segurança e quando não tem esse protocolo, quando não é utilizado esse protocolo, que tem algum tipo de criptografia, ele acusa no próprio browser como um cadeadinho aberto, ele avisa que a conexão não é segura e tudo mais, porque o protocolo de transferência não é criptografado, mas nós vamos fazer algumas requisições HTTP para poder entender como é o processo e o S é simplesmente porque tem uma criptografia em questão de segurança.

## Os métodos: GET, POST, PUT, DELETE e HEAD

E dentro do protocolo HTTP, nós temos alguns métodos que o get é a maioria deles e ele é o padrão, por que é o get? O get, se você traduzir de forma literal do inglês, ele vem de pegar a informação, requisitar a informação, então simplesmente é quando eu acesso uma determinada API em uma URL bem de acordo com a documentação daquela API, eu acesso a URL e ele me devolve alguma informação, no caso, o que eu fiz aqui? Eu acessei a API do GitHub, estou acessando os usuários do GitHub, e aí eu especifiquei qual é o usuário que eu quero, que no caso é o meu e ele me voltou as informações do meu usuário, então essa aqui foi uma requisição do tipo get, eu simplesmente peguei a informação.

Mas, por exemplo, tem requisições do qual a gente quer criar um novo usuário, o que acontece? Quando você faz o formulário no seu front-end, coloca lá nome, e-mail, endereço, você pega uma série de informações do usuário e você agora precisa enviar essas informações para o back-end falar cadastre essas informações no banco de dados, então o método, você não está mais pegando a informação, você está enviando uma informação, então é o método post quando você está criando, você tem que criar um novo registro e aí você tem que sinalizar qual é o método que você está utilizando, que no caso é de criar, de create, que sempre remete ao CRUD.

Um outro método é o put, onde você é exatamente parecido, exatamente não, ele é parecido com o método post, você vai atualizar a informação, então necessariamente você vai pegar um método get antes, vai pegar um determinado usuário, o ID do usuário é o ID, sei lá, 7, e aí o ID usuário 7 está pedindo para trocar o e-mail dele, ele trocou o de e-mail, veio aqui na plataforma, trocou o e-mail dele e está pedindo para poder atualizar, e aí você manda com o método put.

O método delete, como o próprio nome sugere, é quando você quer deletar alguma informação e o método head vem de puxar o cabeçalho, ele não é muito importante por agora, mas eu já deixo claro aqui que é a questão de quando você precisa dos metadados de alguma coisa, do cabeçalho de alguma coisa, então é quando você precisa descobrir algum tipo de informação inerente ao processo, inerente ao servidor. Entendo como metadados ou cabeçalhos que a gente vai ver nas próximas aulas, eu aplicando esses principais conceitos aqui.

Na próxima aula, se não me engano, nós vamos começar a falar de AJAX e vai ter a requisição HTTP para poder ilustrar tudo isso que eu estou falando aqui nesse vídeo, então falou, obrigado e até a próxima.
