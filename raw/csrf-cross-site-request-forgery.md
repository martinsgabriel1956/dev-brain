# CSRF: Cross-Site Request Forgery

Hoje a gente vai falar um pouco sobre CSRF. O Cross-Site Request Forgery é um tipo de vulnerabilidade web onde um atacante, ele força requisições entre origens diferentes para alterar valores ou executar ações. A princípio, isso pode parecer meio confuso, mas vamos por etapas.

## Same-origin policy

Primeiro, a gente precisa entender a política que os navegadores usam para restringir a comunicação entre origens diferentes. Aí que entra o conceito da same origin policy. Por conta dessa política, as formas que uma origem pode interagir com outra diferente são limitadas. Uma origem é definida por protocolo, domínio e porta. Quando duas origens que não possuem os três atributos iguais tentam se comunicar, a política é aplicada.

Essa interação entre origens diferentes pode ser dividida em três cenários gerais. O cross-origin write, quando uma origem faz uma requisição para outra origem enviando algum tipo de dado, como a resposta de um formulário ou um redirect para outro site. Isso geralmente é permitido. O cross-origin embedding, que pode acontecer quando uma aplicação anexa uma imagem de outro domínio, referencia uma style sheet ou faz o uso de iframes, por exemplo, que também é permitido por padrão. E o cross origin read, que se dá quando uma origem tenta ler o conteúdo de outra origem, seja através da resposta de uma requisição ou de um embedding. E é aí que mora a maior restrição da same origin policy. Esse comportamento, por padrão, não é permitido, já que pode ser uma grande brecha de segurança.

## Cookies e sessão

Agora que a gente revisou como funciona a comunicação entre origens diferentes, falta relembrar mais um conceito: os cookies. Quando você faz login num site, como que ele te mantém autenticado para as próximas requisições? O fluxo é o seguinte: o cliente, ao fazer login, manda as credenciais dele pro servidor. O servidor valida elas e devolve cookies. Na próxima requisição, o navegador do cliente vai mandar esses cookies pro servidor de forma automática. É assim que uma sessão se mantém autenticada. Pra gente entender o fluxo do CSRF, é importante lembrar desse comportamento do navegador de enviar os cookies automaticamente. Isso vai ser importante mais para a frente.

## O cenário do banco

Depois de revisar todos esses conceitos, vamos pensar no seguinte cenário. Imagina que existe o site A, no nosso caso vai ser o site de um banco, onde ele possui uma tela de login normal. Nesse caso, a gente entra na conta do João e a gente consegue verificar alguma das funcionalidades do banco. No portal do nosso banco, a gente consegue ver o nosso saldo, a gente consegue realizar transferências para outras contas e a gente consegue ver o nosso extrato.

Agora imagina que um cliente recebeu no e-mail dele um link para um site B, que não tem relação nenhuma com o banco. Ao clicar no link, só é possível ver uma tela que diz o seguinte: "Cheque o seu saldo." Quando o cliente volta pro banco, recarrega a página e checa a conta dele, ele percebe que foi realizada uma transferência sem que ele soubesse. No nosso exemplo, para a conta de um atacante.

Pra gente entender como isso aconteceu, vamos dar uma olhada na aba de rede do nosso navegador. Aqui a gente consegue observar o que rolou por trás do ataque. Quando o cliente visitou o site, uma requisição foi feita, sem que ele soubesse, pro endpoint que realiza a transferência no banco, passando os dados do atacante como destino do pagamento.

Se a gente der uma olhada no código fonte do site do atacante, dá para ter uma noção melhor de como isso aconteceu sem que o cliente soubesse. Primeiro, o atacante criou um iframe e, dentro do contexto desse iframe, um formulário invisível com os dados da transferência. Depois, foi só implementar um script para fazer o envio do formulário assim que a janela do site fosse carregada. Assim, o ataque ocorreu sem que o cliente precisasse sequer interagir com o site. Só o ato de carregar a página foi suficiente para realizar a transferência.

E se você prestou atenção até aqui, você deve estar se perguntando: se existe a [same] origin policy, como que o site do atacante conseguiu interagir com o banco, se eles possuem origens diferentes? Aí que tá a magia do CSRF. Ele não quebra a política de same origin em nenhum momento. Tudo que o ataque precisava era que a vítima já tivesse logada no site. Assim, quando o script forçasse o envio da transferência, o navegador executaria a requisição carregando os cookies da sessão do cliente automaticamente. A interação não precisou ler a resposta do banco. Tudo que ela precisava era do cross-origin write. A requisição autenticada era o suficiente para executar a transferência.

Quando a gente for falar sobre os tipos de mitigação para essa vulnerabilidade, a gente vai conseguir entender melhor porque que essa implementação de transferência do banco não é segura. Mas antes, vamos pra parte prática.

## O laboratório

A descrição do laboratório diz que a função de atualizar o e-mail é vulnerável a CSRF. Para resolver o desafio, a gente precisa fazer o upload de um HTML em outro servidor que faça com que o usuário tenha o e-mail dele trocado. Logando na aplicação, já conseguimos identificar logo de cara a função de atualizar e-mail. Ao interceptar a requisição feita por essa função, vemos que é uma requisição do tipo post, que passa o valor do e-mail a ser trocado direto no body. Para trocar o e-mail, não precisa sequer saber o e-mail original, basta passar o valor desejado. Ao final, o usuário é redirecionado pro perfil com e-mail já trocado.

Na própria plataforma da PortSwigger, já é disponibilizado um servidor com outra origem para executar o exploit. Como nós já sabemos as informações necessárias para troca de e-mail, basta fazer o upload do script para executar a função automaticamente e entregar à vítima.

## Formas de proteção

Pra gente entender melhor o que poderia ter sido feito para impedir esse ataque, vamos dar uma olhada nas formas de proteção contra CSRF. A primeira seriam os CSRF Tokens, onde a aplicação no backend gera um valor único e totalmente imprevisível, compartilhando isso com o cliente. Toda vez que o usuário tentar fazer uma ação sensível, como o preenchimento do formulário de troca de e-mail ou a transferência, o cliente tem que mandar o token CSRF correto junto na requisição.

Se a gente for checar o código fonte do laboratório, vemos que não existe a presença de nenhum token do tipo. O formulário é enviado apenas com o valor do e-mail a ser substituído. Se fôssemos implementar essa proteção, seria algo desse tipo, com o valor do token sendo substituído pelo back end direto no front. Dessa forma, o atacante, quando fosse hospedar o script para fazer a requisição para explorar o CSRF, ia ter que adivinhar esse token, que é gerado aleatoriamente, o que dificultaria muito a exploração da vulnerabilidade.

Outra proteção envolve os cookies do cliente, mais especificamente o atributo de SameSite que os cookies podem possuir. Quando configurado de forma correta, com os valores lax ou strict, o SameSite pode impedir a exploração de CSRF, evitando que requisições críticas, como a troca de e-mail, sejam feitas de forma autenticada.

Essas são só duas das formas que uma aplicação pode usar para tentar evitar a exploração do CSRF. Na descrição do vídeo vão ter alguns links com mais formas e um pouco mais sobre a vulnerabilidade no geral. Muito obrigado pela atenção e bom estudo.
