# FrontPUSH: website estático vs. aplicação web

Opa, fala pessoal, tudo certo? Sejam bem-vindos à terceira aula, onde, na aula de hoje, nós vamos ver as diferenças entre aplicações web e website estático e o quão importante é conhecer isso e as funcionalidades daquilo que você está querendo implementar para você definir qual é o melhor jeito de você hospedar aquele determinado website, aquela determinada aplicação web, tá?

Então, essa aula, pessoal, é importantíssima porque o pessoal sempre me pergunta, Násser, por que você não utilizou nenhuma biblioteca ou framework no FrontPUSH? Por que você não utilizou, sei lá, ReactJS quando você upou o seu site? Por que isso? E é com essa aula aqui que você vai entender um pouco mais, beleza?

## Website estático

Então, primeira coisa, pessoal, o website estático. Vamos voltar um pouquinho lá no conceito. O que é um website estático? É basicamente um website que é construído com HTML, CSS e JavaScript.

É um website denominado estático porque ele não consegue construir funcionalidades complexas. Por exemplo, se você pegar lá um website com HTML e CSS e JavaScript que tem to-do list, você vai ver que se você apertar F5, toda a informação é apagada porque você construiu aquilo ali dentro de um array. Você não armazenou aquilo ali dentro de um banco de dados. Você pode muito bem utilizar, por exemplo, local storage de uma aplicação e tudo mais, mas se dar um limpar, você perdeu todas as informações.

Então, você não consegue criar funcionalidades muito complexas, nem navegação entre páginas dinâmicas e complexas, como, por exemplo, utilizando um ReactJS ou outra linguagem, outra tecnologia, com um website estático.

E aí, por que você não precisa instalar nem configurar nada quando você usa um website estático? Porque é o que o browser entende. A única coisa que ele entende é HTML, HTML, CSS e JavaScript. Então, como ele só está construído com base nisso, você não precisa instalar nem configurar nada que ele já vai rodar diretamente. Então, é bem fácil. Basta você copiar e colar um website estático em uma determinada pasta e acessar essa pasta no seu servidor que ela vai rodar.

## Aplicação web

Agora, quando eu falo de aplicação web, é quando você está construindo aplicações que detêm de uma funcionalidade, ou seja, detêm de um back-end, detêm de um front-end, detêm de uma API, detêm de funcionalidades que exigem um banco de dados e é tudo mais complexo. Então, nessas aplicações, você vai precisar instalar, você vai precisar configurar alguma coisa a mais para poder funcionar, para poder a sua aplicação de fato rodar.

## PHP e Apache no XAMPP

Por exemplo, o PHP precisa do Apache para rodar. Vou dar aqui um pequeno exemplo para vocês.

Se eu vir aqui e acessar localhost barra frontpush e der um enter, você vai ver que ele não achou, está vendo? Então, eu vou digitar HTTP://localhost barra frontpush, ou seja, eu estou acessando a minha própria máquina no localhost, no protocolo HTTP e eu estou indo na pasta raiz do FrontPUSH, ou seja, é para aparecer a minha aplicação e ela está aqui.

Quando eu digito isso aqui, ele vai ficar carregando, carregando e vai dizer que não é possível acessar esse site, porque o FrontPUSH é uma aplicação que está desenvolvida em PHP, ele não é um website estático, ele está em PHP e o website, o browser não entende PHP, ele precisa de um servidor Apache para poder rodar e por isso que eu tenho instalado o XAMPP.

O XAMPP tem aqui um servidorzinho abaixo, Apache, um serviço Apache, tem o serviço de MySQL, do FileZilla, do Mercury, do Tomcat, mas para poder rodar o PHP, eu só preciso do Apache, então se eu vir aqui e dar um start, eu startei o servidor do Apache na porta 80 e na porta 443, ou seja, está rodando o Apache nessas portas, então uma vez que ele está instalado e rodando nessa porta, se eu vir aqui e der um F5 novamente, agora sim a minha aplicação vai rodar, está vendo?

Então o FrontPUSH é uma aplicação que está rodando em PHP, se você não instalar e configurar o Apache na porta que você está acessando, a aplicação simplesmente não vai rodar. E isso acontece da mesmíssima forma quando você faz a hospedagem de uma aplicação web em um servidor, por exemplo, ele precisa ter o Apache já instalado, entendeu?

## ReactJS e MySQL

Então, da mesmíssima forma acontece, por exemplo, com o ReactJS. O ReactJS, se não me engano, para poder rodar, eu estava rodando no localhost na porta 3000, é isso? Se eu vir aqui, que é a aplicação do blog que a gente está fazendo lá no módulo de React, digitar localhost 3000 e, por exemplo, dar um Enter aqui, você vai ver que ele vai ficar rodando, vai ficar rodando e não vai achar, por quê? Porque ele é uma aplicação web que necessita de configurações, necessita de um build, que é a construção do ambiente para poder essa aplicação rodar na porta 3000, que passa para o browser ler o que está naquela porta.

Então, pessoal, o ReactJS precisa da configuração do ambiente, eu preciso também de um banco de dados, de um MySQL. Você precisa instalar o MySQL, você precisa configurar o MySQL, você precisa criar a sua base de dados, as suas tabelas, você precisa criar o usuário do banco de dados para conectar com a sua aplicação, isso eu já estou falando de back-end, mas é só para vocês entenderem que quando a gente fala de uma aplicação web, você precisa de um pouco mais desse poder de configuração.

É lógico que quando ele é construído de maneira inteligente, se você apertar um build e já estabelecer, ele já constrói tudo para você automático, mas no final das contas, no background do negócio, você sempre vai precisar configurar alguma coisa. Então, na maioria das vezes, você vai precisar de um acesso ao terminal para poder configurar essas aplicações, ou, por exemplo, utilizando o PHP, que é um pouco mais simples, só precisa do servidor Apache para rodar e está tudo certo.

## Na hospedagem

Muitos servidores, como, por exemplo, o HostGator ou o Hostinger já vem com a pasta instalada, você nem precisa fazer nada, porque ele já está instalado, configurado na porta 80, entendeu?

Então, na próxima aula, eu vou mostrar para vocês como eu fiz isso, tanto para o CreatorPUSH, que o CreatorPUSH é um website estático, eu vou mostrar para vocês como eu upei esse website estático para o servidor e também vou mostrar como eu fiz isso com o PHP lá na HostGator, também falando sobre os domínios e tudo mais, depois eu vou fazer essa mesma coisa, só que utilizando o GitHub Pages, só dando um preview das próximas aulas. Beleza, pessoal? Então, falou e até a próxima!
