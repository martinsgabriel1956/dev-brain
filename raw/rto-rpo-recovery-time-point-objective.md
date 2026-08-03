Nessa aula vamos falar de outros termos que são extremamente importantes quando você está definindo sua arquitetura.

Um pouco mais focado na questão da resiliência, disponibilidade que você vai ter e a confiabilidade. Quando eu falei da confiabilidade, um dos princípios está lá dentro, que é o RTO e o RPO. O que acontece aqui é bem focado em desastres. Imagina quando algo acontece de errado? A sua aplicação ali cai. Ela fica indisponível? O que que você vai fazer?

Existem dois indicadores. Um se chama RTO, de Recovery Time Objective, ou seja, o tempo de recuperação que você vai ter. Então, quanto tempo você leva para restaurar aquele serviço? Guarda isso daí, a gente já volta aqui.

E aí nós temos o RPO, que é o Recovery Point Objective — ponto de recuperação. Imagine do backup que você tem. Isso quer dizer o seguinte, pessoal: primeiro imagina, você tem uma aplicação, né? Se essa aplicação caiu, independente se é monolito ou qualquer outra coisa, essa aplicação está indisponível. Quanto tempo você leva para subir ela de novo? O RTO está baseado no seu tempo de recuperação.

Isso é muito importante porque tem arquiteturas em que o tempo de recuperação, se você escolher um padrão ali, é quase impossível você atender em menos de 1h, por exemplo. Isso é extremamente importante, tá pessoal? Imagina, você fala "eu tenho duas horas". Certo? Legal, mas esse é um site de vendas que você vende ali 1.000 dólares por minuto. Quanto dinheiro você não vai perder em duas horas? Então, esse é um número que você tem que ter para pensar na arquitetura que você vai ter. Entendeu? Não tem como não ter esse número.

E outro ponto muito importante: se sua aplicação caiu, explodiu, não sei o que aconteceu, você estragou ela de um jeito tão feio que você tem que recuperar ela inteira — seja o banco de dados inteiro — o que acontece? O seu backup, o ponto de recuperação, é de que horas então? Imagina se agora é meio-dia que deu o problema. O último backup foi das 10h. Você perdeu duas horas de dados.

Isso, para um sistema... vamos pensar num sistema financeiro, que precisa ter todos os dados, é impossível. Não tem como você perder duas horas e não saber quem transferiu, quem não transferiu, e tal. Então não é cabível.

Agora imagina um site de vendas. Claro, as vendas têm que estar lá registradas, todas as vendas que você fez, não pode perder nenhum dado. Imagina: eu vou lá no site, compro uma camiseta, ou compro um remédio, e aí eu acho que vai chegar, passa três dias, não chega, e eu preciso do remédio. Eu vou ver e minha compra simplesmente sumiu. Imagina, é impossível. Então é o negócio que vai definir isso agora.

Existem outros casos. Por exemplo, eu tenho um microsserviço dentro do meu e-commerce em que as pessoas vão lá e registram produtos para vender. Às vezes, vamos supor, eu poderia perder duas horas de todos os meus registros que foram adicionados no site para venda. Isso iria afetar o negócio, mas às vezes eu posso comportar isso.

Então você tem que saber qual é o RTO e o RPO da sua aplicação para saber qual é a arquitetura na qual você precisa implementar, qual o padrão que você precisa implementar, qual vai ser o design dela. Isso é extremamente importante.

Bom pessoal, conceito base extremamente importante para o restante do treinamento. Valeu! Até o próximo vídeo!
