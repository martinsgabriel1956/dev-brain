# FrontPUSH: hospedagem na HostGator, parte 1

Opa, fala pessoal, sejam bem-vindos à quarta aula, onde agora nós vamos de fato partir para a prática. Já que na última aula a gente viu as diferenças de como hospedar aplicações web para websites estáticos, agora nós vamos conhecer como eu fiz para poder hospedar todos os meus sites utilizando a HostGator nesse modelo mais tradicional, não quer dizer que ele é mais difícil, só é diferente, e aí você precisa adequar a tecnologia que você está escolhendo com a hospedagem, de forma que ela sempre seja mais fácil para poder você trabalhar.

Então eu vou mostrar na prática tudo como é que eu fiz, desde o domínio e tudo mais, enfim, sem mais delongas, vamos lá.

## Escolhendo o serviço e o plano

O primeiro passo que você precisa fazer é de fato escolher o serviço que você quer, seja a HostGator, seja a Hostinger, seja a Locaweb, todos esses serviços são de boas empresas, mas eu sempre procuro ir naquelas maiores, porque elas vão oferecer mais serviços por um preço menor.

Então quando você entra na HostGator, você vai poder ver os planos de hospedagem, tem a hospedagem P, o M e o Turbo. Eu assinei o Turbo, por quê? Porque era o único que tinha SSD na época, hoje até o plano P tem SSD, mas tem certificado SSL grátis, isso aqui é muito fácil de instalar, que é interessante para você ter o protocolo HTTPS no seu browser para poder garantir confiabilidade em tudo mais, mas tem mais poder de processamento, o Turbo, e aí eu fui lá e assinei esse plano aqui, também vou deixar no link da descrição a Hostinger, se você ver que tem mais vantagens para você, esteja totalmente à vontade, acredito que eles vão oferecer serviços muito parecidos um do outro, mas tem acesso Git, tem acesso a SSH, tem CDN, então eu acredito que a Hostinger tem sido um plano melhor que da HostGator, pelas vantagens que eu vi aqui, porém, contudo, entretanto, o meu plano aqui já está pago, então só quando terminar aqui que eu vou pensar em mudar, tá bom? Tem a GoDaddy, tem a Locaweb, enfim, dá uma olhada lá e aí decide.

## O e-mail técnico e o DNS da HostGator

Agora vamos para a parte mais técnica, por exemplo, quando eu de fato adquiri o serviço da HostGator, eles sempre enviam esse e-mail técnico aqui, onde ele vai falar qual foi o plano que eu adquiri, guarde este e-mail para futuras referências e tudo mais, e o primeiro ponto que é importante, eles passaram o quê? O DNS do seu plano de hospedagem são, eles me passaram o DNS deles.

Vocês lembram que eu falei para vocês que para poder fazer essa conversão de um nome para um IP, eu preciso de um servidor DNS e o servidor DNS é meio que um IP, onde você precisa apontar o servidor DNS para esse IP, para ele saber resolver quando você acessar o seu site. frontpush.com.br, você precisa apontar para os servidores de onde você contratou, ou seja, você precisa apontar o seu registro de domínio, que quem faz é a Registro.br, para o DNS da HostGator.

Ah, eu contratei agora da Hostinger, então você tem que ir lá no Registro.br e olha, agora aponta para esse outro servidor aqui, então é esse DNS que resolve, e aí eles me passaram o servidor DNS da HostGator, que é o quê? nspro34.hostgator.com.br, tem o master e o slave, são dois servidores DNS.

As outras informações técnicas, isso aqui é um e-mail que eu tirei print, pessoal, e só tampei os meus dados de acesso, mas olha só, para poder você acessar o cPanel, que é meio que o painel geral para você adicionar um novo domínio, instalar o certificado, instalar um banco de dados, ou então instalar o WordPress, tudo isso é por esse cPanel que a gente vai ver ele já já.

Então ele me trouxe as informações técnicas do servidor, o IP do servidor, de fato, e o usuário e a senha para poder eu acessar a minha conta no cPanel. Então essas informações aqui eles me enviam assim que eu contrato o serviço deles.

## O domínio na Registro.br

Uma outra coisa que eu quero mostrar para vocês, por exemplo, é o Registro.br. Lembre-se que a maioria das plataformas hoje em dia já oferecem o domínio grátis. Eu prefiro sempre pagar o meu domínio na Registro.br.

Então se você vir aqui no Google e colocar Registro.br, que é o órgão que registra todos os domínios do Brasil, quando você vir aqui, sei lá, www.creatorpush2.com.br, você vai ver que ele está disponível para poder a gente registrar aqui. Você vai ver que eu pago R$ 40 por um ano, R$ 76 por dois anos, R$ 185 por dois anos e aqui tem outros valores, onde você vai lá, paga e registra vinculando ao seu CPF ou o CNPJ.

E aí ele vai te dar todas as informações de titularidade, quais são os domínios que estão no meu nome. Então tenho o CreatorPUSH, tenho o FrontPUSH e tenho o meu nucfl.com.br. Então esses três estão vinculados à minha conta no meu CPF, então estão no meu domínio, esses domínios estão no meu domínio.

## Apontando o domínio para a HostGator

E aí eu tenho que indicar, na Registro.br, qual é o DNS do servidor que eu contratei, do serviço que eu contratei. Então eu fui lá, acessei a minha conta, vim aqui nos domínios e acessei essa informação aqui, DNS, ou seja, eu peguei esses carinhas aqui, nspro34.hostgator.com.br e o 35 e coloquei como servidores DNS de onde está registrado o meu domínio.

E eu fiz isso no caso porque eu fiz na Registro.br, porém esses registros da HostGator, esses serviços aliás, tanto da HostGator como da Hostinger, muitos deles já oferecem domínio gratuito de um ano, dois anos, onde na própria plataforma deles é feito isso, que a Registro.br faz. Na realidade, no background, ele já está fazendo isso com a Registro.br, só que ele pega esse serviço, deixa gratuito para oferecer mais uma vantagem para você contratar o serviço dele e não do outro, são apenas vantagens.

Então você opta para o que você quer fazer, mas sempre você vai precisar apontar, eu sou o DNS do domínio que eu comprei aqui, eu preciso apontar ele para o servidor onde está hospedado o meu site, no caso da HostGator. Mudei para Hostinger, eu venho aqui, alterar servidores DNS, agora eu vou copiar os dois DNS da Hostinger que eu mudei agora.

Demora algumas horas para ele fazer essa modificação, é rápido, ele sempre te manda um e-mail dizendo que está tudo ok e teoricamente agora é só você acessar a sua página e o seu cPanel, colocar os seus arquivos lá que já vai estar funcionando bonitinho, só que essa parte eu vou deixar em uma parte 2 para a gente complementar, beleza pessoal? Então falou e até a próxima.
