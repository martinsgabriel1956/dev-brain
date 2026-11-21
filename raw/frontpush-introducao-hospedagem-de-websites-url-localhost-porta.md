# FrontPUSH: introdução ao módulo de hospedagem de websites

Opa, fala pessoal, sejam muito bem-vindos ao módulo de hospedagem de websites.

Esse módulo aqui, pessoal, é meio que um módulo bônus, porque eu vi a necessidade, muita gente sempre me pergunta de como eu hospedo os meus websites, como é o processo para fazer isso. E aí eu decidi fazer, nesse módulo aqui, um módulo reunindo as principais informações, que eu acredito que é muito interessante todo o desenvolvedor web front-end também saber.

## O que o módulo vai cobrir

Então nós vamos ver o método tradicional, que é aquele método onde a gente contrata um serviço como a HostGator, como a Hostinger e a gente hospeda o nosso website lá, a gente sobe as informações, contrata o domínio, vincula, instala certificado de SSL e tudo mais. Então eu vou mostrar na prática como eu fiz com os meus websites e também tem aquelas clouds, tanto gratuitas como as pagas, por exemplo, utilizando o próprio GitHub Pages, maneira bem simples de você hospedar o seu website, o próprio Netlify ou a Vercel também são muito bons. E ver como funciona também em plataformas maiores, como a Amazon, Microsoft Azure ou o Google Cloud. Então nós vamos citar e explicar as diferenças também.

Esse módulo aqui, pessoal, é um pouco mais introdutório, vou até diminuir aqui a minha câmera, onde nós vamos começar com conceitos iniciais e a gente vai avançando a cada aula, mas no primeiro momento a gente vai entender o que é hospedagem e por que é necessário a gente ter uma hospedagem.

Eu não sei se vocês já se perguntaram por que você não consegue upar, por exemplo, para a internet, um site que está direto no seu computador, sendo que está rodando no seu computador, por que ninguém consegue acessar? Então a gente precisa entender alguns conceitos de rede privada e rede pública para poder clarear isso na nossa mente. É lógico que a gente não vai descer muito nesses conceitos de rede, mas pelo menos alguns conceitos para poder deixar esse conhecimento bem embasado, eu vou falar aqui para vocês.

O que é domínio? Então a gente vai falar um pouquinho de DNS, como é que a gente registra um domínio, quais são os principais sites de hospedagem, do qual eu já citei agora há pouco, como colocar vários sites no mesmo servidor. Vocês vão ver que eu tenho o FrontPUSH, o CreatorPUSH e o meu portfólio tudo no mesmo servidor, só que com três domínios diferentes e aí vou mostrar para vocês na prática como eu fiz isso e como instalar certificados SSL, que é para poder a gente colocar o protocolo HTTPS quando a gente acessa os nossos websites, entre outras perguntas.

## O que é hospedagem

Então pessoal, basicamente o que é uma hospedagem? Ele é um serviço online que permite a publicação de um site ou aplicação web na internet e olha que tem diferença, viu? O website você upa ele e ele vai funcionar de uma determinada forma. A aplicação web necessita de mais configurações e eu também vou falar isso mais para frente, mas basicamente a gente precisa desse serviço online para poder hospedar o nosso website e olha só, vou dar um exemplo aqui na prática.

Por exemplo, eu estava aqui fazendo essa animação para a live do FrontPUSH. Se vocês observarem bem, lá na URL está escrito 127.0.0.1:5500/index.html. Então vocês já se perguntaram por que se eu acessar esse endereço de outro celular, por que eu não consigo acessar essa aplicação aqui? Por que ela não vai funcionar se eu digitar esse endereço em outro celular, por mais que esteja na rede da minha própria casa?

## As partes da URL

É agora que a gente vai entender já alguns conceitos aqui, vou sumir aqui da tela e já deixei esse esquemático aqui porque é interessante a gente frisar essas informações aqui.

Primeira coisa, pessoal, quando eu copiei e colei a URL, o HTTP se diz respeito ao protocolo que eu estou utilizando, no caso é o HTTP, que significa Hypertext Transfer Protocol, ou seja, é um protocolo de transferência de hipertexto, se você for traduzir.

O 127.0.0.1 está apontando para o host, ou seja, para a sua própria máquina. Esse 127.0.0.1 é a mesma coisa de você digitar localhost, então é o seu host local, é a sua própria máquina.

O dois pontos aqui, o número que vem em seguida é a porta, 5500. Mas por que quando eu estou acessando um site, eu não vejo :5500, eu não vejo a porta quando eu digito algum site? É porque quando você não vê nada aqui, é porque ele está na porta 80, a porta 80 é a porta padrão, e quando ela é a padrão, ela meio que não existe, então quando está assim, simplesmente localhost, é porque está sendo executado na porta 80. Quando não está sendo executado na porta 80, precisa especificar aqui qual é a porta.

E aí, quando eu passo aqui o barra, ele está na raiz do meu projeto, ou seja, isso aqui é um diretório, e dentro desse diretório, eu estou puxando esse arquivo aqui, que é o index.html. Mas mais uma vez, o index.html sempre é o arquivo padrão que está na raiz do seu projeto, em que não precisa dele ser escrito. Quando eu adiciono barra, automaticamente ele já vai puxar o index.html e o próprio browser faz isso.

Então, nós vamos voltar nesse conceito aqui, nessa URL, e aprofundar um pouco mais nisso nas próximas aulas.

## Os principais sites de hospedagem

E aí, só para poder enfatizar, pessoal, quais são os principais sites de hospedagem que a gente tem? Eu tenho o GitHub, o Netlify e a Heroku. Eles têm planos gratuitos para você hospedar nos seus websites e a gente também vai estar utilizando eles.

Então, você pode vir aqui no Netlify, esses links eu vou tentar deixar todos na descrição, para poder facilitar para vocês, e você pode vir aqui em pricing, você vai ver que tem aqui o plano starter, que é um plano básico para projetos pessoais, do qual você pode utilizar e, olha só, você pode buildar a sua aplicação sem precisar, por exemplo, entrar no servidor, propriamente dito, por meio de um FTP e puxar os seus arquivos. Você consegue colocar os arquivos direto pelo Git. A gente vai fazer esse processo tanto no Netlify, como no GitHub Pages, para vocês verem como isso aqui é muito fácil de upar. E com esse plano gratuito, você já consegue colocar a sua aplicação na internet.

Tem também a Heroku, que da mesmíssima forma tem aqui um plano gratuito, Free and Hobby, ou seja, são aplicativos não comerciais, são projetos pessoais que você pode estar upando e também é gratuito. O próprio GitHub Pages também tem essa possibilidade e também tem a Vercel, também é possível. Então são todas clouds, porém, eles têm planos gratuitos e planos pagos. Esses aí são os principais.

Tem também essas clouds que são de empresas gigantescas, como a Amazon, o Google ou a Microsoft Azure, onde eles são muito parecidos. Uma vez que você aprende um, você só precisa mexer um pouquinho na plataforma para poder aprender o outro.

E os sites mais tradicionais que eu tinha já falado para vocês, como, por exemplo, a Hostinger, a HostGator ou a Locaweb, que eu também já deixei aberto aqui, a gente vai conversar um pouco sobre os tipos de hospedagem, quais são as vantagens, quando eu indico um, quando eu indico o outro, como é que você faz para decidir qual é a hospedagem que você vai estar tratando no seu website.

Então, no mais é isso. Na próxima aula, a gente vai começar a aprofundar um pouco mais os conhecimentos que a gente acabou de citar aqui. Falou e até a próxima!
