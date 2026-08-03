# SLO, SLI e SLA — Exemplo com E-commerce

Nessa aula nós vamos falar sobre SLO, SLI e SLA. São itens bem importantes para você entender, principalmente ali na sua arquitetura.

O que acontece? Você tem que desenhar a sua arquitetura para atender a uma necessidade de um usuário. O que acontece é que, dependendo do software, da arquitetura que você tem, existem diferentes usuários.

Então você pode ser um e-commerce, né? Você tem lá um e-commerce, você tem usuários que compram aquele produto. Isso quer dizer que se o usuário — vamos dizer, o Douglas — vai lá comprar um produto nessa loja e ela está indisponível, tipo, ok, e eu não preciso saber quanto de SLA ela tem, né? Para mim tanto faz. O que acontece é que provavelmente eu não vou comprar nessa loja, vou comprar em outra. Eles vão perder dinheiro.

Então, internamente, o que acontece dentro do e-commerce? Vamos dizer, nesse problema que eu falei de indisponibilidade, que a indisponibilidade estava na verdade com um determinado time. Então vamos abrir aqui esse e-commerce. Vamos dizer que ele tinha duas aplicações, né? Tinha um banco de dados e tinha uma aplicação, para simplificar aqui. Sei que tá confuso o negócio, mas a aplicação conecta no banco de dados.

O que acontece é que internamente essa empresa tem uma definição de quanto disponível ela tem que estar, mas provavelmente não é uma SLA — porque ela vai estar... não, provavelmente é um SLO, porque está dentro da mesma empresa, existe um acordo entre as diferentes áreas. Uma área não vai pagar multa para outra, certo?

Então imagina a área de banco de dados: fez um problema e ela dizia "eu tenho que ficar 99,9% disponível para a aplicação". O que acontece é que ela não ficou. Isso vai gerar problemas internos, mas só isso.

Agora vamos imaginar um cenário diferente. Vamos imaginar aqui que esse banco de dados — nossa, bem hipotético — mas vamos dizer que é um banco de dados compartilhado, que existe uma outra empresa por trás, que vende um serviço de base de dados. E o que acontece? Essa aplicação está conectando nele. Então são empresas distintas.

O que acontece? Porque essa empresa aqui — vou colocar letras — essa empresa A e essa empresa B. Porque a empresa A contratou a B, provavelmente porque tem especialistas de banco de dados, então existe um contrato entre elas. Vamos supor, ela falou "eu tenho que ficar 99,9% disponível para você". É diferente. Não é mais um SLO. Estamos falando de um SLA.

Internamente, nas empresas, você tem os SLOs. Então, falando sobre os dois itens, é o quê? Um acordo de nível de serviço, que é um contrato explícito ou implícito, que detalha as consequências de não atender àquela porcentagem, né? Então, o que acontece se o SLO da empresa ali, que é o dado objetivo dele, não funciona? O SLA tá mais focado ali no nível de contrato. Quando a gente vai para o SLO, nós estamos falando da porcentagem de fato, mas não do contrato. Então, aqui geralmente é usado mais internamente nas empresas, uma área com a outra.

Tem um curso que eu falo sobre SRE, que é claro a base de tudo. Quando você fala de SRE, é extremamente importante para diversas coisas. Então aqui a gente tá falando que é um objetivo de nível de serviço. SLO é um target ou um intervalo, um valor, né? E ele desempenha um papel crucial para estabelecer as expectativas do que você pode esperar.

Legal. E aí nós temos o seguinte: o SLO é só uma porcentagem de alguma coisa. Você não concorda comigo? Que indisponibilidade... você precisa de uma métrica, certo? Um gráfico. Aí você precisa de um indicador, que é o SLI. O SLI é de fato a métrica que diz aquilo.

Então, vamos supor, ali você tem os HTTP, né? Então você fala: "olha, eu garanto que 98% dos HTTP vão ser 200". Sei lá. Então isso daqui é um SLA. Legal, internamente nós temos isso convertido, como eu falei aqui, para um SLO. E o SLO vai olhar para o quê? Para uma métrica.

Então imagina, você vai ter uma aplicação que os usuários conectam nela, certo? Se ela recebe HTTP 200, ou 300 qualquer coisa, ou 400 qualquer coisa, 500 qualquer coisa — enfim, né, 300 não ia ser, mas enfim, qualquer um desses — você precisa ter essas informações ligadas em uma métrica, né? Então vamos supor que aqui tem uma métrica, você ia ter que usar uma ferramenta de observabilidade e, dado essa métrica, você tem que ter o quê? Alarmes para o seu SLO, para os acordos de serviço que você tem. Então aqui dizendo que, se passar daquilo, ia ser um problema — olha só, passou. Enfim.

Então: SLI é a métrica, o SLO é a porcentagem, o SLA é a questão contratual.

Tá bom, pessoal, nem todo serviço faz sentido ter um SLA — naquele exemplo que eu dei. Só estendendo um pouquinho mais: eu conecto em um site para fazer uma compra, isso daqui não é um SLA. Eu não tenho um SLA com essa empresa, não tenho nenhum acordo. Eu estou comprando um produto, eu não posso reclamar.

Agora imagina que eu sou um lojista, né? E aí eu falo: eu vou escolher essa empresa aqui, esse website de venda, um e-commerce, por exemplo — nem sei se existe isso — e eu vou escolher para vender as minhas camisetas customizadas da minha marca, né? E aí eles me falam: "eu vou garantir para você que 99% do tempo seus produtos vão estar disponíveis". Se não tiver, isso é um problema, porque isso vai afetar. Então isso aqui é um SLA.

Tá bom, pessoal. Bom, isso é bem importante você saber. Espero que tenha ficado claro. Até o próximo vídeo. Valeu!
