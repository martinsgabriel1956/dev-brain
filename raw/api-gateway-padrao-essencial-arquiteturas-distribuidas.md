# API Gateway: Padrão Essencial em Arquiteturas Distribuídas

Transcrição de vídeo do canal de Bernardo Lobato sobre o padrão API Gateway.

## Introdução — o problema

Sua aplicação se integra com dezenas de outros serviços ou APIs. Só de tentar lembrar que porta precisa ficar aberta e para quem, você já fica perdido. Precisa disponibilizar só um endpoint externamente, mas não encontrou nenhuma maneira interessante de fazer isso e acabou tendo que disponibilizar a API inteira. Já recebeu de retorno um JSON de 10 MB quando tudo que você precisava era um ID de usuário e um nome. Esse vídeo é para você.

Hoje vamos falar de API Gateway, um padrão essencial quando estamos falando de arquiteturas distribuídas. Se você acha que já sabe tudo sobre API Gateway, fica até o final do vídeo — deve ter um ou dois pontos que você provavelmente não sabe.

Olá, dev, eu sou Bernardo Lobato, e hoje vamos falar sobre esse padrão muitas vezes desconhecido, muitas vezes negligenciado, mas que cumpre um papel fundamental na arquitetura do seu sistema.

## O problema ilustrado

Antes de entrar nos detalhes e ver as melhores aplicações, vamos imaginar um problema: uma aplicação mobile em que um usuário precisa simplesmente logar no sistema e trazer na tela uma lista dos seus pedidos e pagamentos.

1. O usuário chama um endpoint de login, que traz algumas informações básicas do usuário.
2. Depois ele chama outro endpoint para trazer suas informações pessoais — aqui já temos um objeto maior sendo armazenado.
3. Na sequência, um novo endpoint para trazer os pedidos daquele usuário — todos os dados dos pedidos são trazidos nesse endpoint.
4. Por fim, um último endpoint para listar todos os pagamentos de todos os pedidos daquele usuário.

Pare para pensar no monte de informação inútil que está sendo trafegada pela rede nesse contexto. Agora imagine a latência e a velocidade de carregamento dessa tela. Imaginou? Agora pense tudo isso num 3G sendo acessado de uma região bem remota.

Agora imagine que você quer subir uma nova instância da sua API para lidar melhor com a escalabilidade. Do jeito que está configurado, como o frontend vai saber qual o endereço da nova API que ele deve chamar? Ele provavelmente vai continuar chamando o serviço antigo, e a nova API não vai adiantar de nada. E isso só piora se você tiver chamando múltiplos serviços.

## A solução: um componente intermediário

A partir de agora, vamos criar um componente novo dentro da arquitetura que vai funcionar como um intermediário entre a aplicação mobile e os serviços. Esse componente recebe todas as solicitações do usuário e as redireciona aos endpoints específicos. Agora temos um componente novo e podemos escalar a API.

Isso resolveu o problema dos endpoints e das chamadas, mas e a latência e a quantidade enorme de dados que não serve para o contexto do mobile? E a orquestração desses endpoints — como montar um objeto mais aderente para o mobile?

A solução para esses problemas é a utilização de um **API Gateway**, que pode ser tão simples quanto rotear as requisições entre o aplicativo mobile e os respectivos serviços, assim como ter várias funções de borda como autenticação, autorização, cache, log, etc.

## O que é formalmente um API Gateway

Um API Gateway é um componente centralizado dentro da arquitetura que funciona como o único ponto de entrada do mundo exterior para a aplicação. Esse componente pode ser responsável por:

- **Roteamento** dos endpoints do client para os diversos serviços e APIs dentro da arquitetura.
- **Autenticação e autorização** do usuário que está se conectando através do serviço.
- **Mapeamento de payloads** — por exemplo, se você tem uma API em REST e precisa conectar com outra API que funciona com gRPC ou GraphQL ou outra tecnologia, o API Gateway pode ser o componente que faz essa transformação dos dados de um padrão como JSON, por exemplo, para outro padrão como gRPC.
- Outras funções como **cache, log, rate limit**, etc., se isso for o que a arquitetura pedir.

O componente-chave aqui é a **flexibilidade**: o cliente só conhece um endpoint, então ele só vai acessar esse componente, e esse componente acaba cuidando de toda essa infraestrutura dentro do sistema.

## API Composition

Voltando ao problema, já vimos que o API Gateway resolve o problema de múltiplos endpoints. Agora precisamos tratar de outros problemas, como centralização e merge de informações. Para isso, conhecemos um novo pattern chamado **API Composition**.

Um API Composition tem como componente principal um elemento chamado **API Composer**, que pode chamar e orquestrar endpoints em várias APIs diferentes e devolver tudo como um único resultado — descartando informações desnecessárias naquele contexto, ou até adicionando informações úteis para aquela etapa da utilização do sistema. Com isso, resolvemos o problema das múltiplas requisições e da orquestração de serviços, além de conseguir lapidar o objeto de retorno para deixá-lo mais aderente ao que o cliente está esperando na ponta.

## Edge functions (funções de borda)

Já entendido o potencial desse componente, vamos falar um pouco do que chamamos de **edge functions** ou funções de borda — funções que é comum atrelar ao comportamento do API Gateway, como autenticação, autorização, cache, rate limit, etc.

O que precisa ficar claro é que, apesar de podermos nos beneficiar (e muito) acoplando essas funcionalidades dentro do API Gateway, precisamos tomar muito cuidado ao utilizar essas funções de borda. Se ficarmos usando e abusando a torto e a direito, o API Gateway pode se tornar um **gargalo** — e isso é tudo que não queremos. O API Gateway precisa ser rápido, precisa ser eficiente. Portanto, se vamos usar essas funções de borda dentro do API Gateway, precisamos usar com consciência, sabendo do real impacto que isso pode trazer para o projeto.

## BFF — Backend for Frontend

Uma breve menção a um tipo de API Gateway que nos últimos tempos ficou muito popularizado: o **BFF**, ou Backend For Frontend (também pode ser conhecido como "Best Friends Forever").

Um BFF é um tipo específico de API Gateway. Ele diz que, basicamente, cada frontend deve ter seu próprio backend. Como o próprio nome já diz, essa abordagem gera vários serviços, cada um com sua particularidade. Por exemplo:

- Um app mobile pode utilizar recursos que são mais interessantes para essa questão do mobile.
- Um frontend de administração (web) pode utilizar recursos mais aderentes para a administração do sistema, que não necessariamente têm a ver com os serviços mobile.
- Mesmo um app mais simples, voltado para o usuário final na web, pode usar recursos que só são interessantes para ele e não são interessantes para os outros componentes da arquitetura.

Essa abordagem pode parecer exagerada e acabar inflando a arquitetura desnecessariamente — e em alguns pontos é sim desnecessário. Mas em outros pontos é bem interessante, principalmente no sentido de tirar praticamente 100% das regras de negócio do frontend, o que é extremamente desejável nesse modelo de desenvolvimento.

Outro ponto fundamental — talvez o mais importante dessa abordagem — é que cada BFF vai trazer exclusivamente somente os dados que aquele frontend precisa. Temos muita flexibilidade e eficiência com essa conexão, principalmente quando os serviços aos quais o BFF vai se conectar são serviços legados ou são gerenciados por outro time, e não temos tanta flexibilidade para mexer neles quanto temos para mexer no frontend e no BFF.

Muitas vezes a implementação do BFF é feita pelos próprios desenvolvedores frontend — eles sabem melhor do que ninguém as necessidades que precisam ser absorvidas através do BFF.

Essa abordagem do BFF precisa ser extremamente enxuta e bem otimizada, senão ela vai acabar se tornando um complicador dentro da arquitetura — mais um projeto que vamos precisar ficar dando manutenção, e ninguém quer isso. Um bom BFF é aquele que às vezes até esquecemos que existe, que precisamos mexer tão pouco — a não ser quando precisamos de uma adequação de um novo endpoint, de um envelopamento de um dado, enfim. O ideal é que mexamos nele muito pouco e que ele consuma muito pouca infraestrutura também.

## Benefícios de utilizar API Gateway

- **Centralização do acesso** às APIs/serviços — o principal ponto.
- **Redução de acoplamento** entre os clientes e os serviços — é possível evoluir os serviços sem prejudicar o cliente na ponta, sem ter que ficar atualizando ele o tempo inteiro, sem ter que fazer breaking change.
- **Melhor segurança dos serviços**, pois detalhes internos ficam escondidos — o serviço não fica disponibilizado para o mundo externo, só o API Gateway fica, e ele é extremamente limitado.

## Desafios ao adotar um API Gateway

**1. Single point of failure.** O API Gateway acaba se tornando um ponto único de falha — se ele cair, a arquitetura inteira cai. É preciso pensar em:
- Escalabilidade horizontal, para evitar que o serviço fique 100% fora do ar.
- Balanceamento de carga, com várias instâncias do API Gateway no ar.
- Observabilidade.

A chave aqui é: **redundância, balanceamento e observabilidade**.

**2. Gateway mal configurado vira gargalo.** Se você acha que o API Gateway é bala de prata e começa a pendurar nele autenticação, autorização, cache, acesso a dados, CDN e mais um monte de coisa, isso traz consequências muito complicadas para o projeto. Procure deixar o API Gateway o mais leve e enxuto possível, para ganhar eficiência e não se tornar mais um gargalo na aplicação.

**3. Equilibrar simplicidade e complexidade excessiva.** Se você tem um componente que já faz essas funções de borda, por que não utilizá-lo? Não se trata de não poder usar, mas de usar com responsabilidade — sem transformar a arquitetura num gargalo por causa disso. Estude o sistema, estude as regras, e coloque as funções de borda nos lugares mais apropriados. No geral, o uso do API Gateway, assim como vários outros conceitos, exige maturidade e responsabilidade, para não tomar decisões arbitrárias a torto e a direito e no processo prejudicar a arquitetura.

## Tecnologias de mercado

- **Kong** — projeto open source pensado para ser utilizado com microsserviços; muito leve e extensível; compatível para uso multicloud com vários provedores de cloud.
- **NGINX** — muito famoso como servidor web e proxy, que também pode ser adaptado para funcionar como API Gateway.
- **Traefik** — muito utilizado em ambientes com Kubernetes e Docker; basicamente um proxy reverso que também pode ser usado como API Gateway.
- **Spring Cloud Gateway** — evolução do Zuul, o antigo API Gateway da Netflix; foca em soluções com Spring e o ecossistema Spring.

Um ponto importante é evitar ao máximo ficar dependente de tecnologias, principalmente se são proprietárias e se isso de alguma maneira impede o sistema de crescer e evoluir.

Também existe a possibilidade de implementar o próprio API Gateway dentro da arquitetura. Diferente de outros componentes já discutidos em outros vídeos, o API Gateway é um componente para o qual normalmente recomendaria uma implementação própria, principalmente por ser uma implementação relativamente simples — hoje já existem diversos frameworks, independente da linguagem, que ajudam a implementar esse componente e as funções de borda, para se ter maior controle dentro da arquitetura.

## Fechamento

Esse é o primeiro vídeo de uma série sobre padrões de integração de aplicações — vem muita coisa boa por aí. O autor recomenda dois vídeos complementares sobre comunicação assíncrona e comunicação síncrona entre sistemas, que formam a base para entender comunicação entre componentes de arquitetura.
