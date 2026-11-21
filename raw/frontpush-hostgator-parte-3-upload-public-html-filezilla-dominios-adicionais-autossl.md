# FrontPUSH: hospedagem na HostGator, parte 3 (upload, domínios adicionais e SSL)

Opa, fala pessoal, bem-vindos à terceira parte dessa aula prática, onde eu estou demonstrando como upar todos os meus websites por meio da HostGator, onde na aula passada eu dei meio que um panorama geral do cPanel, pelo menos eu passei pelos principais features que a gente precisa saber para poder upar esses websites.

Se eu não falei, pessoal, alguma coisa que vocês precisam aqui dentro, não hesitem em pesquisar, porque hoje em dia o cPanel vem com muita coisa instalada, muita coisa pronta, onde você só precisa de fato de alguns cliques para poder configurar ou fazer alguma coisa que você está precisando. Inclusive tem muitos tutoriais da própria HostGator e Hostinger, que têm blogs inteiros para poder falar de componentes específicos, de como instalar, como fazer, como instalar o WordPress e tudo mais. Enfim, vamos lá.

## A pasta public_html

Agora eu vou demonstrar para vocês, pessoal, como de fato você upa um site, onde você pega os seus arquivos, os diretórios do seu site que está local na sua máquina e passa para o servidor de fato, para quando você digitar www.frontpush.com.br, ele acessar a pasta certa que está lá os arquivos do seu website, beleza?

Então a primeira coisa que você precisa ir é clicar aqui em gerenciador de arquivos. No gerenciador de arquivos, você sempre vai procurar por essa pastinha aqui, que é a public-underline-html. É nessa pastinha que você sempre vai ter que colocar, sempre tudo vai ser direcionado para ela. Então ela é a pasta raiz de quando você acessa o seu domínio.

Então se você digitar www.nucfile.com.br, que é o meu domínio principal nesse caso aqui, quando eu der enter, ele vai entrar nessa página. Então o que tem nessa página? Tem de fato a página do meu portfólio. Então se você está vendo esse index.html aqui, você está vendo esse .svg, esse .src, esse .js, essa imagem e esse .css, são pastas do portfólio.

Ou seja, quando eu venho aqui e digito www.nucfile.com.br, você percebe que eu não digitei nenhuma barra para entrar em nenhuma pasta. Então eu estou entrando na pasta raiz e a pasta raiz é uma página estática.

## Por que o portfólio é estático

Ou seja, você percebeu que nela eu tenho um HTML. Essa página é inteiramente feita com HTML, CSS e JavaScript. Tem uma biblioteca em JavaScript, que é a GSAP, porém eu adicionei a página como um script, eu não utilizei nenhum npm, nem nada disso. Então ela está totalmente pura, é um website estático, porque ele não detém de nenhuma funcionalidade a mais.

Esse é o grande porquê que eu estava explicando desde aquela aula do que é um website estático e o que é um website dinâmico. A diferença de você upar uma aplicação web e você upar um website estático.

Para mim, esse portfólio, qual é a funcionalidade que eu preciso que ele tenha? Nenhuma. Eu só preciso que ele reúna os links do meu portfólio e apresente para mim. E com HTML, CSS e JavaScript, eu já consigo fazer isso. Então para que eu vou fazer uma aplicação web que vai me demandar bem mais trabalho de configuração de ambiente, de buildar a aplicação para poder ela funcionar, sendo que para essa aplicação eu não preciso disso.

Páginas de venda, por exemplo, para que eu vou precisar fazer uma aplicação super robusta sendo que uma página de vendas só precisa de texto, imagem e link. Texto, imagem e link você já consegue fazer só com HTML, CSS e JavaScript. Ah, tem algum modal e tudo mais, mas são funcionalidades muito simples que só com JavaScript puro você já consegue fazer. Então não há necessidade de você complicar o processo.

Ah, eu vou lá fazer o React, mas você já viu que como você está upando uma aplicação, você vai ter que buildar todo o ecossistema do React no servidor para poder isso funcionar. E para uma aplicação simples como essa, não há necessidade. Então por isso que essa página aqui eu fiz em website estático, eu não preciso dessas funcionalidades a mais. Tudo que eu quero é passar as informações das minhas principais redes para poder a pessoa entrar em contato comigo, passar o meu e-mail, me apresentar, colocar os principais links dos meus trabalhos e é isso.

E o bom é que o website estático vai ser bem leve, vai ser bem escalável. Então para a página de vendas é muito interessante que seja um website estático, porque ele não precisa carregar todo um ambiente para poder rodar. Ele está só em HTML e CSS e JavaScript e ele vai ser bem mais performático, o que página de venda é muito interessante que seja.

Então por isso que eu falo sempre para você avaliar qual é a aplicação que você está buildando, se é necessário mesmo ou não. Você pode ver que o meu portfólio é um website estático, já o FrontPUSH ele não é e eu vou explicar o porquê.

## Upload pelo gerenciador de arquivos

Então pessoal, para poder você passar a sua página para cá, basicamente você tem que vir aqui e clicar em carregar. Quando você clicar em carregar, ele vai abrir essa dialoga aqui, essa caixinha de diálogo para você pegar todos os arquivos que estão na sua página, no caso do seu portfólio, quer dizer, no meu caso, eu simplesmente peguei esses arquivos aqui, copiei e colei para lá. Ele vai fazer o upload desses arquivos aqui, então eu só selecionei e carreguei eles para cá.

Automaticamente, ele vai carregar todos os meus arquivos e quando eu digitar nucfl.com.br, ele vai cair nessa página. E como é que ele executa automaticamente? Quando ele ver index.html, por padrão, ele já vai executar o que tem nessa página index.html, que é a minha página única e principal, entendeu?

## Upload pelo FileZilla (FTP)

Você tem outra forma de você fazer isso? Tem. Utilizando, por exemplo, programas FTP, onde basicamente eu tenho o FileZilla, que é, inclusive, indicado pelo próprio pessoal do HostGator e um dos principais programas que tem, onde você basicamente vai entrar com três informações, qual é o IP do seu servidor, qual é o seu usuário e qual é a sua senha.

Lembre-se que o IP do servidor está bem aqui, 162.241.61.25, esse é o IP do seu servidor que você precisa colocar aqui, ele já está na conexão rápida que eu já inseri, então ele já está com o meu usuário, basta eu colocar a senha que ele vai automaticamente conectar.

Como você está conectando a um FTP, pode ser que apareça uma dialogue de segurança, por quê? Porque o FTP, digamos assim, em fins didáticos, não é criptografado, então ele vai abrir uma dialogue de segurança pedindo se pode confirmar, se você tem certeza e tudo mais, é só você clicar em sim. Se você quer algo criptografado, você tem que acessar, ele não envia FTP, mas envia SFTP, basicamente só muda isso, mas é o mesmo protocolo de transferência.

E olha só o que temos aqui, a pastinha public-underline-html, quando você entra nela, você está na mesma pastinha que estava no gerenciador de arquivos, é exatamente a mesma pasta. Deixa eu até dar um zoom aqui para poder facilitar a visualização de vocês.

O que eu fiz no FileZilla? Eu peguei os meus arquivos aqui, então eu posso vir aqui na minha área de trabalho, selecionar a pastinha NY, que é a pastinha do meu portfólio, que está em página estática, eu simplesmente selecionei esses arquivos, puxei e arrastei para cá, quando eu vou puxar e arrastar para cá, ele vai abrir uma dialogazinha de confirmação perguntando se você quer adicionar mesmo esses arquivos, quando você clicar em ok, ele vai fazer todo o upload desses arquivos, quando finalizar, o seu site já está hospedado. Se você puxar, eu quero substituir, você vai clicar em arrastar, ele vai identificar os arquivos que têm o mesmo nome e vai substituir.

## Projetos em subpastas

Então é assim que eu faço, porém, quando eu quero agora adicionar, como se diz, um novo domínio, por exemplo, eu tenho o CreatorPUSH e eu tenho o FrontPUSH, por enquanto, eu só ensinei para vocês o NUCFI, porque aí eu coloco na pasta raiz e está tudo certo, mas se eu quiser adicionar novos projetos aqui dentro, você tem que entender, pessoal, que tudo são pastinhas, tudo são diretórios, então o seu site é um diretório, se você colocar um novo diretório lá dentro, basta você acessar barra Nubank, por exemplo, digitar NUCFI.com.br barra Nubank, você vai ver que ele vai acessar um outro diretório, que é o projeto do Nubank, do qual, da mesmíssima forma, eu só criei uma pasta aqui dentro chamada Nubank, está bem aqui, Nubank, eu vou acessar aqui, porque está em um zoom maior, está aqui uma pastinha chamada Nubank, eu só criei uma nova pasta aqui dentro e joguei todos os meus arquivos da página estática do Nubank aqui dentro e funcionou perfeitamente, da mesmíssima forma, eu fiz para o Spider-Man, então se eu vir aqui NUCFI.com.br barra Spider-Man, ele vai cair nessa página aqui, que é um diretório diferente, mas que aqui no cPanel, eu simplesmente criei uma pasta, e da mesmíssima forma, eu joguei os arquivos para lá do Spider-Man, do projeto do Spider-Man, da mesma forma, porém, contudo, entretanto, eu estou utilizando o mesmo domínio, eu estou utilizando NUCFI barra Spider-Man, barra Nubank, agora eu quero acessar dessa mesma forma, só que de um domínio diferente e o que eu preciso fazer?

## Domínios adicionais

Eu preciso primeiro registrar um novo domínio, então eu tenho lá registrado o domínio do FrontPUSH e o domínio do CreatorPUSH e eles apontam também para esse mesmo servidor DNS, mesmíssima coisa, só que agora eu preciso vir aqui no cPanel e adicionar esses novos domínios e dizer para esse domínio, olha, quando você receber esse domínio como requisição, eu quero que você direcione ele para uma outra pasta, que não seja a pasta raiz, ou seja, eu venho aqui em domínios adicionais, nesse domínio adicional, você vai perceber que eu tenho dois domínios aqui que já estão criados, que no caso é o do CreatorPUSH e o do FrontPUSH, o que eu falei para ele?

Olha, ao invés de você entrar diretamente na página public_html, que lá é onde está o meu de portfólio, você vai entrar na pasta public_html, barra frontpush, ou seja, quando eu digitar agora frontpush.com.br, ao invés de ele entrar na pasta raiz, ele vai na pasta raiz e vai procurar uma pasta chamada frontpush e lá dentro ele vai executar, então basicamente eu coloquei aqui, frontpush.com.br, ele não vai deixar adicionar porque já existe um nome com esse domínio e ao invés de colocar o diretório aqui frontpush.com.br, eu vou colocar barra public, barra frontpush e eu lá no meu gerenciador de arquivos, eu vou criar uma pasta chamada frontpush, entendeu?

E aí eu vou lá e adiciono, como aqui já está feito, só vou gerenciar aqui o redirecionamento, eu vou voltar aqui, ver aqui em domínio, por exemplo, domínios, isso, está bem aqui, vou clicar em gerenciar para você ver, então olha só, ele já está criado, está bom? Então ele tem que entrar nessa pastinha aqui, public_html/creatorpush e aí você vai lá e adiciona esse novo domínio e ele vai criar para você automaticamente, está bom?

E aí quando eu acessar www.creatorpush.com.br, ele vai cair na pastinha creatorpush, que é essa aqui, que também tem uma página estática aqui dentro, porém, como eu disse para vocês, o FrontPUSH não é uma página estática, ele é uma aplicação web em PHP, só que você pode perceber que está agora index.php.

## Por que o FrontPUSH é em PHP

Por que eu utilizei PHP no FrontPUSH e nas outras eu utilizei um website estático, só HTML e CSS? Porque na página do FrontPUSH eu tenho, por exemplo, outras páginas dentro dela que eu preciso de uma navegação dentro do site, você vai perceber que no FrontPUSH, se você vir aqui, www.frontpush.com.br, ele tem uma página de cadastro, então ele vem aqui, entrar para a lista de espera, você vai perceber que ele entra em outra página e como eu preciso dessa navegação, eu falei, cara, eu vou fazer uma aplicação web, mas eu não vou fazer uma aplicação web em React que vai me demandar bem mais configurações para algo muito simples, porque eu só quero uma rota diferente aqui dentro, para fazer uma rota em React, eu tenho que configurar todo um ecossistema, com PHP é bem mais fácil, então eu fui pela facilidade e falei, não, vou fazer em PHP, já me atende super bem e além disso, como eu disse para vocês, no cPanel, nesses domínios como na HostGator, na Hostinger, ele já vem com o PHP já todo instalado, porque ele já vem preparado para o WordPress, que também é em PHP, então eu não preciso instalar uma parte, nem configurar nada disso, ele já vem configurado certinho, então para poder eu rodar o PHP, o procedimento é exatamente o mesmo que uma página estática, parece que está tudo igual, mas ele é uma aplicação, então eu simplesmente vim aqui, copiei e colei o diretório do FrontPUSH para essa pastinha que eu fiz aqui e aí funciona perfeitamente bem direto, não precisei configurar absolutamente nada, mas é porque a HostGator já deixa pré-configurado e instalado o Apache nesse servidor, então não se engane e tenha em mente essa particularidade.

Então, basicamente é isso, pessoal, eu venho aqui, adiciono um domínio adicional, redirecionando para uma pasta em específico que eu mesmo crio lá no gerenciador de arquivos vinculado a um novo domínio, então é assim que eu consigo ter vários sites, só que na mesma pastinha, vocês viram, eu tenho, por exemplo, o site do Nubank, só que eu não tenho um domínio específico para o Nubank, então eu entro em barra Nubank, barra Spider-Man, só que para o FrontPUSH e para o CreatorPUSH, eu criei um novo domínio e eles direcionam diretamente para cá, basta só configurar aqui.

## Certificado SSL com AutoSSL

E por último, antes de eu encerrar de fato essa aula e todo esse tutorial, eu vim aqui em certificado SSL, está bom, pessoal? Certificado SSL utilizando a HostGator pelo cPanel, que é um processo muito fácil, porque ele já vem na interface gráfica, você só precisa clicar e confirmar, basicamente é isso, quando você clicar e confirmar, ele vai te gerar uma chave, a chave padrão para o seu SSL barra TLS certificado, então você sempre vai pedir para ele utilizar esse certificado aqui.

Quando você tiver esse certificado já instalado, que é com poucos cliques que você consegue fazer isso, você vem aqui em status do certificado SSL barra TLS, automaticamente todos os seus domínios vão aparecer aqui, todos os seus domínios, aqueles em que o AutoSSL não foi instalado, vai ficar vermelho, aqui como ele já instalou em todos, estão todos verdinhos, então todos já estão com o certificado SSL instalado em cada site e quando você entrar ele já vai ser HTTPS, quando ele ficar vermelho é porque não está instalado e ele faz isso de maneira automática e para poder você instalar o certificado que você acabou de adicionar lá do outro lado, basta você selecionar aqui todos os domínios e executar AutoSSL, automaticamente ele vai instalar o certificado em todos esses domínios, em todas essas pastas para quando você acessar o seu website ele ter o HTTPS, entendeu?

Para vocês verem, o processo é totalmente por interface gráfica utilizando o cPanel, se eu fosse fazer por linha de comando eu teria que pegar um certificado e instalar ele manualmente, mas na maioria das interfaces hoje em dia tanto o cloud como o cPanel, que é a maneira mais tradicional de hospedar websites, é tudo feito de maneira fácil e rápida como eu mostrei aqui para vocês. Beleza?

Então acredito que é isso pessoal, acredito que eu dei um panorama geral aqui de como eu hospedei as minhas páginas e se tiver mais alguma dúvida deixa aqui também, falou pessoal e até a próxima.
