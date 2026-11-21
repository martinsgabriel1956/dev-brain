# FrontPUSH: o que é IP e o que é DNS

Opa, fala pessoal, tudo certo? Enfim, sejam muito bem-vindos à segunda aula do módulo de hospedagem de websites, onde na aula de hoje nós vamos conversar um pouco sobre o que é o IP e o que é o DNS.

Então, esses conceitos aqui, pessoal, eu não vou aprofundar muito, vai ser bem superficial, mas eu acredito que seja importante para poder, quando a gente estiver acessando, quando eu estiver ensinando o método mais tradicional de hospedagem de websites, é interessante que a gente entenda desses conceitos aqui.

## O que é o IP

Então, basicamente, o que é o IP? O IP é um protocolo. Assim como na internet eu tenho nada mais do que um conglomerado de computadores e eles precisam se comunicar, eu preciso estabelecer regras de comunicação e é isso que os protocolos fazem. E o protocolo de internet nada mais faz do que identificar o seu dispositivo na internet.

Então, assim como você, pessoa, detém de um CPF que identifica você no mundo, no Brasil, você também, na internet, o computador precisa da mesma coisa, ele precisa de um IP para poder identificá-lo na internet, para quando você estiver, por exemplo, mandando um pacote, ah, eu requisitei um pacote, estou mandando o pacote na internet, eu preciso saber para quem eu estou mandando e aí eu consigo identificar isso com o IP.

## IPv4 e IPv6

Então, basicamente, como é que eu faço e eu até copiei aqui as configurações aqui do meu computador, ele vai falar a velocidade da conexão e eu tenho o endereço IPv6 e o endereço IPv4, como vocês podem bem ver aqui.

Ah, Násser, qual é a diferença entre o IPv6 e o IPv4? Na maioria das vezes eu só vejo o IPv4, a gente não utiliza o IPv6. O que acontece, pessoal? Basicamente, o IPv4 tem quatro grupos, como vocês podem bem ver, com 32 bits, enquanto o IPv6 são oito grupos que constituem 128 bits de endereçamento.

E aí, basicamente, por que existe o IPv6? É porque tem uma coisa chamada internet das coisas. Na internet das coisas, não só smartphones e computadores ou notebooks terão acesso à internet, mas também todo e qualquer dispositivo também vai estar conectado à internet, geladeiras, lâmpadas inteligentes, casas inteligentes, vai haver uma inserção de dispositivos na internet muito grande, do qual o IPv4, esse grupo de endereçamentos vai ser insuficiente para tanto dispositivo. Então, é literalmente muito dispositivo para pouco endereço, você não vai conseguir endereçar todos eles. E por isso surgiu a necessidade do IPv6 com 128 bits de endereçamento, mas a gente sempre está utilizando o IPv4 normalmente.

## Acessando o site de outro celular

Então vamos lá, pessoal, vamos voltar. Eu também tenho o servidor DNS, que no caso é o 192.168.1.154, o endereço IPv4 do meu computador é 192.168.1.92.

E aí, pessoal, o que é interessante, eu quero deixar claro para vocês do porquê que, por exemplo, eu não consigo acessar de um outro celular esse website que está rolando. Como é que eu faço para poder acessar esse website de um outro celular?

Primeira coisa, eu preciso especificar o host. Então, no caso, se eu digitar localhost, ele vai estar apontando para ele mesmo, então não faz sentido. O que eu tenho que digitar em outro celular para poder acessar essa aplicação aqui? Primeira coisa, eu preciso digitar o meu IP, o host que eu quero acessar. Então eu vou digitar aqui 192.168.1.92 e na porta 5500.

Se eu digitar agora esse endereço aqui em outro celular para poder verificar essa aplicação, ele vai rodar, mas tem outro porém, ele precisa estar na mesma rede. Então um dispositivo só vai enxergar o outro quando ele está na mesma rede. E no caso, essa rede aqui é privada.

## Rede privada e rede pública

Násser, como assim? Existe rede privada e rede pública? Exatamente.

Para você estar na internet de fato e visível para toda essa rede de computadores, você precisa ter um IP público e o IP público é fixo, porque senão quando você acessa, por exemplo, o Google, se eu vir aqui e digitar, por exemplo, o CMD, o prompt de comando, e dar um ping em www.google.com.br, você vai ver que ele me dá um endereço de IP.

Mesma coisa se eu der um ping, por exemplo, no FrontPUSH, então frontpush.com.br. Você vai ver que ele está disparando nesse IP aqui, 162.241.61.29. Esse aqui é o IP do servidor em que está hospedado o meu website e está pingando lá, mas ele é um IP fixo e público, enquanto o 192.168 é uma rede privada.

Você vai perceber que na sua casa, se você verificar o seu IP, provavelmente ele pode ser igual ao meu, mas ele está em uma rede privada. Quando você faz alguma coisa na internet, ele faz a demodulação de uma rede privada para uma rede pública, por isso que você consegue acessar a internet, mas para poder acessar da sua mesma casa, você precisa estar na mesma rede, ou seja, conectado no mesmo Wi-Fi para você acessar isso aqui. Se você estiver em um Wi-Fi diferente, ele também não vai conseguir enxergar.

Então é interessante a gente saber o porquê que a gente precisa de um IP público, porque senão a gente não consegue, de fato, hospedar na internet. As outras pessoas que estão em outras redes privadas não vão conseguir achar o nosso website.

## O que é o DNS

E o que é o DNS? O DNS nada mais é do que ele converte nomes de domínio em endereço de IP. Como eu mostrei aqui para vocês no prompt de comando, vocês vão ver que quando eu dei um ping no frontpush.com.br, eu digitei um nome que é frontpush.com.br e ele vinculou esse nome a um IP.

Por que eu preciso do DNS? Porque é bem mais fácil eu lembrar de um nome do que lembrar de um IP. Se vocês não sabem, eu consigo acessar o meu site digitando 162.241.61.29, mas é bem mais difícil eu lembrar desse número do que sempre lembrar do nome FrontPUSH.

Então o DNS converte esse nome de domínio em endereço de IP para que os navegadores possam carregar os recursos da internet. Então quando você vai lá e digita um domínio, ele sempre é vinculado a um número de IP, que é o servidor que está com a sua página lá e você consegue acessar ele por meio do protocolo HTTP para mostrar no browser a sua página web.

## Registro.br

E aí o órgão para poder a gente registrar o domínio no Brasil é a Registro.br, do qual eu vou abrir bem aqui. Então basicamente esse aqui é o site, pessoal. Para você registrar domínios no Brasil, sempre vem aqui na Registro.br.

Então você pode ver que se você digitar aqui www.frontpush.com.br, você vai ver que não está mais disponível porque já está registrado no meu nome e ele dá outras sugestões de domínios diferentes com esse mesmo FrontPUSH, só que sem a nomenclatura .com, .app, .art, .blog.

Então você pode vir aqui e registrar o seu nome para deixar fixo apontando para um IP, que é o servidor que você pode hospedar em qualquer lugar, da mesma forma aqui o creatorpush.com.br, ele também já está registrado. Então olha só, o Násser também, o Creator aqui também e o FrontPUSH também. Todos eles estão no mesmo servidor que é na HostGator que eu vou estar explicando para vocês nas próximas aulas, mas basicamente é isso que eu queria falar para vocês, o que é DNS e o que é o IP para poder a gente conseguir prosseguir.

Então falou e até a próxima.
