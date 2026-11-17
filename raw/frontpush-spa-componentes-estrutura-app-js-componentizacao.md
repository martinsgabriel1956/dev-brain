# SPA: a estrutura SPA e a componentização

Opa, fala pessoal, tudo certo? Agora nós vamos continuar o que a gente já começou na aula passada, onde a gente conversou mais sobre o método de como é feito mais recentemente. A gente comparou o modelo tradicional de como acontece a comunicação do back-end e do front-end, quais são as vantagens de um com relação ao outro. E, nessa aula de agora, nós vamos falar, propriamente dito, de o que é uma estrutura SPA e a componentização e por que isso tudo conversa muito bem com o método que foi adotado. Então vamos lá.

## A estrutura SPA

A primeira coisa é uma aplicação que carrega uma única página HTML, por isso que é single, de único, de sozinho, traz essa ideia do inglês, page application. Então você vai carregar uma única página HTML e quaisquer interações com páginas subsequentes, as rotas que a gente cria, quando você clica o usuário é direcionado para uma determinada rota, não necessita outra requisição de outra página completa, diferentemente do que era, por exemplo, feito aqui no método tradicional, se eu requisitasse um ID de um produto 10, ele iria lá, requisitava para o banco de dados, ele traria essas informações, ele empacotava na HTML e devolvia tudo para você.

Se eu requisitasse um produto 12, ele iria fazer esse mesmo processo, consumir tudo de novo, sendo que o que muda de uma página para outra é somente a informação e eu consigo resolver esse problema, por exemplo, utilizando esse método aqui, porque ele me manda só a informação, então computacionalmente falando é bem mais barato ele me mandar só o que de fato muda.

## Componentização

E eu também tenho que pensar que todos os meus componentes da página não precisam ser recarregados, só aquele componente, aquele miolo que de fato vai mostrar o meu produto e aí eu fiz meio que um esquemático para poder já falar de um outro conceito que é a ideia de componentização, vocês vão perceber que eu tenho um componente maior chamado App.js e se ligam nesse nome, porque é com esse nome que a gente vai construir as próximas páginas do React, então lembre-se disso.

E aí, dentro desse componente maior, eu tenho componentes menores, onde eu posso ter um componente específico por header, um componente específico por sidebar, um componente específico por content e outro por footer.

Se eu for falar desse mesmo exemplo da KaBuM, do e-commerce que a gente está contextualizando aqui, quando eu clicasse em um novo produto, só iria mudar dois componentes, que é a sidebar carregando elementos e filtros específicos daquele produto e o próprio content, carregando as informações, a imagem, o preço, a descrição desse produto que eu pedi, sendo que o header e o footer eu não preciso mexer, então a página não é completamente recarregada, eu só carrego aqueles elementos que necessitam de fato da atualização.

Então, essa ideia de componentização, eu consigo organizar melhor o meu código, porque cada bloquinho desse vai ter o seu respectivo JavaScript, o seu respectivo HTML e o seu respectivo CSS, ou seja, cada componente não interfere na lógica um do outro, então eu posso muito bem tirar um, atualizar e plotar novamente, que ele não vai atrapalhar, porque ele está lá junto com os outros, porém ele tem um CSS próprio, uma estilização própria, ele tem uma estrutura de conteúdo própria, que é o HTML, e tem uma estrutura de lógica própria, que é o JavaScript, então isso faz com que eu tenha melhor performance, porque eu estou carregando somente o que é realmente necessário, e a gente consegue criar componentes que são encapsulados e que gerenciam o seu próprio estado.

Então eu consigo aninhar componentes, colocar um componente dentro do outro, posso criar quantos componentes eu quiser e criando o componente, eu posso muito bem utilizá-lo em outro lugar, por exemplo, se eu estiver criando um botão, ele sempre vai ter uma determinada ação na minha interface, então eu posso simplesmente passar um parâmetro para esse botão, como se ele fosse uma função, para onde é que você vai redirecionar quando clicar, ou então qual é a cor desse botão? Eu passo esses parâmetros para o componente e eu consigo muito bem renderizar ele em várias partes do meu código, da minha aplicação, eu estou reaproveitando aquele componente em várias partes, então consigo compartilhar, aninhar componentes e todo esse ecossistema, a gente consegue construir uma estrutura que detém várias vantagens.

## Um conceito liga com o outro

E um conceito sempre liga com o outro, então a gente consegue entender que a ideia de ser componentizado e as características dos componentes já torna possível o conceito de uma SPA e isso tudo só é possível porque o método de comunicação do back-end e do front-end é feito por meio de um JSON com API fornecendo múltiplos clientes, e aí eu não consigo desvencilhar um conceito do outro, necessariamente todos esses conceitos que eu apresentei para vocês ao longo dessas duas aulas de SPA conversam entre si e a gente de fato vai aplicar eles nas próximas aulas, mas é muito importante a gente entender o porquê da vantagem de a gente estar fazendo isso, do porquê a gente está fazendo e construindo dessa forma.

Pessoal, então falou e até a próxima.
