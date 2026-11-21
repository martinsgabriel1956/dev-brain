# FrontPUSH: hospedagem na HostGator, parte 2 (o cPanel)

Opa, fala pessoal, sejam bem-vindos à parte 2 da parte prática, onde eu estou demonstrando como eu fiz para poder upar todos os meus sites aqui na HostGator.

## Recapitulando a parte 1

Rapidamente, eu vou recapitular o que eu fiz nessa primeira parte. Basicamente, você precisa escolher o seu serviço. No caso, na época, eu escolhi a HostGator. Quando você escolher o seu plano, fizer a sua conta e pagar, eles vão te enviar um e-mail muito similar a esse aqui, com essas principais informações de acesso. As principais informações são qual é o plano que você adquiriu, qual é o seu principal domínio, quais são os endereços DNS, qual é o seu usuário e a sua senha para poder você acessar o painel ou principal de recursos, que a gente vai mexer daqui a pouco para poder colocar os nossos arquivos e os websites.

Segunda parte é a parte do Registro.br, onde você de fato registra o seu domínio. Como eu tinha dito, para esses serviços, muitos deles oferecem domínios grátis, ou seja, você não precisa pagar novamente no Registro.br, mas eu, Násser, prefiro deixar separado, porque quando eu vou modificar alguma coisa, eu vou modificar direto pelo Registro.br. Ah, troquei, não quero mais a HostGator, venho aqui e altero o DNS para apontar para os servidores da Hostinger.

No caso, como eu estou na HostGator, está apontando para o DNS do HostGator, porque um precisa combinar com o outro. Não adianta nada eu digitar www.frontpush.com.br e ele não apontar para os servidores do HostGator, que é onde está o meu site. Então, essa parte é importante.

## Acessando o cPanel

Recapitulado isso, agora eu preciso acessar o meu cPanel e eu vou mostrar os principais recursos. Para poder você acessar o cPanel, você vai precisar desse usuário e dessa senha. No caso, como eu faço para acessar? Você vai entrar no seu domínio principal, no caso é nusefale.com.br barra cPanel. Quando você digitar enter, ele vai ser redirecionado para uma página para você entrar com o seu usuário e com a sua senha. Uma vez que eu já entrei, ele vai entrar nessa parte aqui, você vai digitar o seu usuário e sua senha.

Esse aqui, pessoal, é o cPanel. Ele detém todas as principais funções que você precisa fazer no seu website.

## Banco de dados

Ah, Násser, eu quero adicionar um banco de dados. Olha só, banco de dados. Ele já vem com o phpMyAdmin instalado. Para quem não sabe, o phpMyAdmin é um programinha que facilita eu criar banco de dados com uma interface gráfica, sem precisar utilizar terminal e isso tudo. Já utilizei muito ele.

Ah, Násser, eu quero criar de fato um banco de dados. Você vai vir aqui em banco de dados MySQL. Você percebe que esses recursos já estão instalados aqui. Se você fosse pegar, por exemplo, um servidor cru, você teria que instalar tudo isso na mão. Para quem conhece um pouco de Linux, você teria que entrar no terminal e dar um `sudo apt-get install mysql-server`. Ele vai instalar o banco de dados do MySQL e etc. Você vai perceber que tem muitos recursos aqui dentro que já estão instalados, que já estão prontos nesse serviço.

## Arquivos e FTP

Aqui é a parte de banco de dados. Aqui é a parte de arquivos. Ah, Násser, quando eu clicar em gerenciador de arquivos, ele vai abrir essa pastinha. Essa pastinha aqui é a minha pasta do meu usuário no servidor deles. Então, basicamente, é aqui que eu vou colocar as minhas páginas web. Eu coloco todas aqui dentro e vou demonstrar para vocês. A gente simplesmente acessa isso aqui, clica e arrasta, copia a nossa pastinha da nossa aplicação web para aqui para dentro, que já vai funcionar.

Uso do disco, tem outras informações e tem conta FTP. Basicamente, o que é um FTP? O FTP, pessoal, é um protocolo de transferência de arquivos. Então, quando você quer passar a sua aplicação web, que está naquela pastinha que você construiu, para aqui para dentro você precisa transferir esse arquivo. E aí você precisa utilizar o protocolo FTP. Então, basicamente, você está criando uma conta FTP para poder fazer isso, ou você pode puxar daqui diretamente. Não tem problema nenhum. Também vou mostrar como é que faz isso na prática.

Tem controle de Git, muito do CP, pessoal. Fuce, descubra. Estou aqui mostrando os principais recursos.

Ah, eu quero ver o uso do disco. Então, você pode ver aqui que eu utilizei na public_html, que é onde a gente coloca os nossos websites, 80 MB. Então já está cheio 80 MB aí.

## Domínios

Ah, Násser, eu quero adicionar um novo domínio. Também vou mostrar que antes só foi o nucf-ali, que foi o meu primeiro. Depois eu registrei o FrontPUSH lá no Registro.br, adicionei ele aqui. Depois eu fui lá, adicionei o CreatorPUSH, adicionei ele aqui de novo. Também vou demonstrar para vocês, eu só vim aqui e adicionei ele.

## Métricas e contas de e-mail

As métricas, eles também dão informações de métricas e você pode também criar contas de e-mail. Você vai perceber que quando você cria uma conta no Google, qual é o domínio do seu e-mail? É o que? Fulano de tal, arroba, gmail.com. Esse Gmail é o domínio do Google e ele sempre vai estar presente no seu e-mail porque ele está no domínio do Google.

Mas como você comprou o seu próprio domínio, agora você pode ter um e-mail na sua conta. Então, no caso, qual é o meu domínio? nucf-ali.com.br. Então, eu posso criar qualquer nome, sei lá, fulano de tal, arroba, nucf-ali.com.br. Ou então, eu posso criar um contato, arroba, frontpush.com.br. E eu vou lá, crio uma conta de e-mail chamada contato vinculado a esse domínio que eu acabei de registrar e ele me dá essas contas de e-mail grátis para eu dar para o pessoal e eu consiga agora um e-mail no meu domínio, que é um e-mail um pouco mais profissional, não é utilizando o Google, não é utilizando o Yahoo e vai. Então, você cria também isso por aqui.

## Largura de banda

Tem métricas de relatório de erros, largura de banda, relatório de acesso do seu website, tudo você vê por aqui também.

É interessante você sempre observar que se você comprar um serviço, um plano de hospedagem que tem a largura de banda baixa e o seu site tem muito acesso, isso vai comer a largura de banda e meio que ele vai travar o acesso do seu site. É difícil isso acontecer, mas antigamente, onde a largura de banda era algo mais caro, conforme vai passando o tempo, essas coisas vão ficando mais baratas, já chegou de vez que eu acessei tanto o meu site que comeu toda a largura de banda e eu tinha que pagar mais porque já tinha comido tudo. Hoje é mais difícil.

## SSH, segurança e certificado SSL

Acesso SSH, para quem não sabe, o acesso SSH é quando você vai acessar diretamente essa pastinha aqui, só que via terminal. Você faz um acesso remoto utilizando o comando do SSH no Linux. Você consegue, por linha de comando no terminal, acessar aquela pastinha ali.

Tem bloqueador de IP e aqui é onde a gente instala o certificado SSL, que é para a gente ter o protocolo HTTPS grátis na nossa plataforma e eles disponibilizam esse certificado SSL de forma gratuita, só com alguns cliques. Você consegue criar e instalar esse certificado SSL, que eu também vou demonstrar nessa aula que eu só estou passando aqui pelo cPanel.

Gerenciador de tokens, status do certificado. Você vai ver que eu instalei esse certificado para todos os domínios, tanto o Creator, está vendo aqui, tanto o FrontPUSH quanto o NUCFL e ele faz esse certificado tanto para e-mail, tanto para o protocolo HTTPS, que quando eu entro aparece o cadeadinho de forma que ele está protegido.

## PHP e WordPress

As outras ferramentas que estão instaladas aqui. Muitas coisas do PHP já vêm pré-instaladas, pessoal, porque esses servidores, esse serviço de hospedagem, eles vêm muito preparados para o WordPress. O pessoal sempre utiliza muito o WordPress vinculado a esses serviços.

Então, eu sempre trabalho com WordPress, o que isso indica para mim? Serviços como o da HostGator, como o da Hostinger, que já vem com tudo isso preparado, com tudo isso instalado, com poucos cliques você consegue fazer assim muita coisa sem precisar pegar em absolutamente nada de código ou linha de comando. Então, a tecnologia que eu estou mexendo é o PHP, eu indico, você está utilizando esses serviços aqui que já vem pronto em muita coisa.

Então, gerenciar aplicações, para você instalar novas aplicações dentro do seu servidor também com poucos cliques, versão do PHP, instalar o WordPress, enfim, e tem bem mais funcionalidades aqui do cPanel, mas as principais eu diria que é o gerenciador de arquivos, banco de dados, se você tiver, ou phpMyAdmin, os domínios e o certificado SSL, beleza pessoal?

Então, esse aqui é o cPanel, é a parte principal, é o painel principal de recursos quando você contrata um serviço de hospedagem e agora nas próximas aulas eu vou demonstrar na prática como eu fiz para adicionar um novo domínio, quando você registra e instalar o certificado de SSL e passar o website, o CreatorPUSH e o FrontPUSH, para poder executar dentro do serviço aqui, beleza pessoal? Então, falou e até a próxima.
