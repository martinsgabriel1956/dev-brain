# Por Que Vale a Pena Estudar Microsserviços (Mesmo Que Você Nunca Vá Usar em Produção)

> Transcrição de vídeo em português, colada pelo usuário no chat e reorganizada em seções/parágrafos para leitura (removidas repetições e hesitações de fala; conteúdo não traduzido — já em português). Autor identificado no próprio texto: Bernardo Lobato.

## Abertura

Tipos da vibe code, devs performáticos, porque você precisaria estudar microsserviços? É possível que você nunca trabalhe com esse estilo em sua forma mais completa durante toda a sua carreira. Então por que investir o seu tempo nisso? É o que eu pretendo te explicar aqui com esse vídeo.

Olá dev, eu sou Bernardo Lobato e hoje vamos bater um papo um pouco mais subjetivo, e também falar um pouco mais sobre carreira e aprendizado — mas de uma maneira leve, fazendo algumas provocações e reflexões. Eu quero falar da importância que o aprendizado de microsserviços traz na sua carreira, e no impacto que um estudo desses pode ter se levado a sério no longo prazo.

## O Problema do Conteúdo Raso

Hoje temos uma infinidade de posts no LinkedIn, vídeos aqui mesmo no YouTube e outros conteúdos — alguns voltados para IA, outros voltados para os padrões de system design que você precisa conhecer — mas vejo pouca ou nenhuma profundidade em muitos desses conteúdos, que acabam trazendo simplesmente uma salada de letrinhas e esquemas gráficos que nada conversam com quem já não tenha aquele conteúdo absorvido, internalizado. Um catálogo nada prático que não aumenta de verdade o seu repertório técnico.

Só que hoje em dia o problema vai além de conteúdos rasos e de estudos unicamente para entrevistas de emprego. O uso de ferramentas de IA para facilitar a codificação e a definição de arquiteturas de sistemas complexos muitas vezes pode mascarar um problema que pode vir a se tornar gigante: a falta de vivência daqueles que são responsáveis pela entrega e pelos respectivos projetos.

Uma arquitetura complexa de um sistema complexo não deve ser feita no automático, sem uma dose de subjetividade daquele que é o responsável por ela. Requisitos arquiteturais como segurança, manutenibilidade, escalabilidade, disponibilidade, portabilidade e outros requisitos de qualidade são essenciais em todos os projetos de grande porte que almejam se manter relevantes no decorrer do tempo e à prova de futuro.

## Por Que Microsserviços

É aqui que eu vou começar a falar sobre o estudo dos microsserviços, porque estudar esse modelo arquitetural é provavelmente o jeito mais rápido de aprender dezenas de conceitos avançados de arquitetura — e eu vou te mostrar agora exatamente por quê.

Microsserviços têm raízes em conceitos de arquitetura orientada a serviços, lá do início dos anos 2000, mas são um estilo arquitetural que acabou ganhando muita popularidade por volta de 2014, naquele famoso artigo do Martin Fowler e James Lewis (link na descrição). Foi mesmo nessa época que o estilo acabou tomando de assalto a indústria de desenvolvimento. Durante muito tempo virou hype, e qualquer solução nova em times "da moda" sempre acabava passando — nem que fosse por um estudo da viabilidade dos microsserviços, uma "pokezinha" que seja — muitas vezes sem saber direito como aquele estilo funcionava corretamente.

### O que é o estilo

Basicamente, nesse estilo arquitetural, ao invés de construir uma aplicação única e monolítica que concentra todas as funcionalidades no mesmo processo e banco de dados, você divide o sistema em vários serviços pequenos e independentes, cada um responsável por uma parte específica do negócio — por exemplo, um serviço de pagamentos, um serviço de usuário e um serviço de notificações.

Cada microsserviço:
- Roda de forma isolada.
- Tem seu próprio banco de dados, se bem implementado.
- Pode ser desenvolvido, implantado e escalado independentemente dos outros.
- Se comunica com os demais através de APIs — REST, RPC ou mensageria assíncrona (filas e eventos).

### Benefícios e custos

Benefícios: escalabilidade seletiva (você só escala o serviço que precisa, não a aplicação inteira), times menores, mais enxutos e mais autônomos trabalhando em paralelo, e maior resiliência (a falha de um serviço não necessariamente derruba o sistema inteiro).

Em troca, introduz uma complexidade operacional bem maior: consistência de dados distribuída, latência de rede entre serviços, observabilidade (rastrear o que acontece entre múltiplos serviços), orquestração de deploy, e uma série de padrões de resiliência — circuit breaker, retry, timeout etc. — tudo isso para lidar com falhas que simplesmente não existiam quando tudo rodava dentro de uma única aplicação, um único processo.

(Autor cita ter um vídeo anterior no canal com mais detalhes sobre microsserviços, linkado na descrição.)

## Por Que Virou Hype: Uma Breve Análise de Mercado

Já que é tão complexo assim, como pode ter virado padrão e gerado tanto hype? A ascensão desse modelo arquitetural caminhou lado a lado com a ascensão da própria computação em nuvem.

Antes da nuvem, montar e manter dezenas de serviços dependentes, cada um com sua própria infraestrutura, era operacionalmente inviável para a maioria das empresas — exigia hardware próprio, provisionamento manual, mão de obra especializada e um custo de manutenção muitas vezes proibitivo. Com a chegada e popularização de provedores como AWS e Google Cloud, e de tecnologias como contêineres e orquestradores como Docker ou Kubernetes, esse custo caiu drasticamente. Ficou barato e rápido provisionar, escalar e derrubar serviços sob demanda — e foi essa infraestrutura elástica e self-service que destravou os microsserviços na prática, dando viabilidade em escala.

Além disso, a ascensão do movimento e da cultura de DevOps, e a ideia de times autônomos, vinham bastante ao encontro do que representava esse estilo arquitetural de uma maneira mais filosófica. E tem mais um ponto: a fadiga de sistemas monolíticos em grandes empresas tradicionais — burocracia para subir uma nova versão, demora para atualizar tecnologias, testes manuais e outras dificuldades comuns para quem já trabalhava com esse tipo de sistema. Mais uma coisa que os microsserviços acabavam combatendo por tabela.

Com tudo isso, tornou-se comum usar microsserviços na sua startup só para dizer que estava em dia com o que o mercado estava utilizando, que estava "modernizando" a aplicação, mesmo sem uma necessidade real. Desenvolvedores buscavam criar quaisquer projetos, por mais simples que fossem, nesse modelo, já desde o início, como forma de se destacar na multidão. Um belíssimo efeito manada.

## A Tese do Vídeo: O Hype Passou, o Aprendizado Fica

À primeira vista, pelo jeito que venho falando, pode parecer que sou contra esse estilo — não sou, não sou hater. Defendendo minha tese aqui do vídeo: todo esse hype dos microsserviços já passou. Hoje, mais de 10 anos depois do início da popularização desse modelo, é comum que se tomem decisões com mais pé no chão, em vez de simplesmente começar já criando N microsserviços sem pesar os prós e os contras.

Mas eu realmente acho que uma coisa que deve sobreviver a toda essa fase, todo esse hype, é o aprendizado que o estudo desse estilo proporciona ao desenvolvedor que está disposto a se aventurar em toda essa complexidade a mais.

Um tópico macro bem definido nos permite organizar o estudo de maneira muito mais padronizada — livros, cursos e outros materiais que acabam trabalhando esses conceitos complexos de maneira meio que unificada, com propósito bem definido. Em outras palavras: microsserviços nos permitem aprender, de maneira amarrada, conceitos avançados e aparentemente dispersos que, se estudados individualmente, poderiam nunca se tornar motivadores ou relevantes no seu dia a dia como desenvolvedor — ou levariam muito mais tempo até que você conseguisse dedicar atenção a esse aprendizado.

Todo esse estudo combinado acaba servindo como uma espécie de cola que une vários aspectos diferentes de arquitetura de sistemas ou system design — principalmente conceitos centrais e complexos de sistemas distribuídos, de APIs e de segurança.

Atualmente eu não vejo microsserviço somente como um estilo arquitetural — eu gosto de entendê-lo como um guia de aprendizado para o desenvolvimento moderno, principalmente para quem vai trabalhar com a parte de internet ou de aplicativos. Mesmo que para muitos funcione apenas como uma pincelada em cada subtópico, acaba servindo também como base para correr atrás de outros conceitos e continuar expandindo o seu repertório técnico através de material mais avançado e mais aprofundado.

Isso acaba te libertando — paradoxalmente — permitindo, com um repertório arquitetural maior e mais completo, adotar com muito mais propriedade os conceitos e ferramentas que esse estudo de microsserviços te trouxe, mesmo que não usem sua totalidade, mesmo que todo o seu sistema não precise seguir rigorosamente esse modelo, sem precisar criar os tais microsserviços de maneira rigorosa com todas as regrinhas que dizem respeito a eles.

## Relato Pessoal do Autor

Isso tudo eu falo bastante por experiência própria. Durante quase 10 anos eu fiquei trabalhando na mesma empresa com monólitos legados — sistemas legados Java e PHP, um pouco de cada, dependendo da época ou do que precisava mexer. Sistemas bem tradicionais, do jeitinho que a maioria de nós, "macaco velho", está acostumada, querendo ou não.

Nesse cenário a gente acaba meio que se tornando refém do próprio parque tecnológico da empresa e dos seus sistemas, se tornando em alguns níveis alheio completamente ao mercado e ao que está acontecendo de novo lá fora. Quando eu precisei sair desse lugar e confrontar o que estava acontecendo no mundo real, eu me vi simplesmente fora do mercado — uma série de letrinhas novas na sopa que a gente está acostumado, e eu não fazia ideia de por onde recomeçar. As primeiras entrevistas foram mais inseguras, com aquela sensação de estar sempre um passo atrás, de ter ficado para trás tecnicamente sem nem perceber.

Mas eu já tinha uma bagagem um pouco mais da parte da universidade e da pós-graduação, com sistemas distribuídos, e por sorte foi bem no comecinho desse hype dos microsserviços. Tomei esse hype como o meu norte e centralizei os estudos a partir daí. Em poucas semanas estudando de forma mais organizada e estruturada, acabei destravando uma quantidade de conceitos que eu nunca imaginei que precisaria um dia fora do âmbito acadêmico: sistemas distribuídos, observabilidade, resiliência, segurança — tudo isso vinha de brinde junto com o estudo dos microsserviços. E foi exatamente esse repertório que me trouxe de volta pro mercado. Ter um eixo central de estudo acabou puxando o resto de todos esses conceitos.

## Onde os Conceitos de Microsserviços se Aplicam Fora de Microsserviços

Para tentar ilustrar os argumentos em relação à importância desse estudo pro dia a dia de desenvolvedor que quer se aprimorar, seguem alguns pontos que fazem parte do uso do modelo de microsserviços, mas que podem ser utilizados em diversos outros contextos e projetos no dia a dia do desenvolvimento:

1. **Separação de responsabilidades / bounded context** — mesmo dentro de um monólito, você aprende a desenhar módulos com fronteiras claras, evitando aquele espaguete onde tudo depende de tudo.
2. **Design de APIs e contratos** — pensar em versionamento de API, retrocompatibilidade, contratos bem definidos entre módulos; algo que se aplica até entre times do mesmo backend.
3. **Padrões de resiliência** — circuit breaker, retry, timeout não são exclusividade de sistemas distribuídos; fazem sentido em qualquer chamada de API externa, seja de terceiros, um banco de dados, um serviço de pagamento, mesmo dentro de uma aplicação única, de um backend único.
4. **Observabilidade** — a necessidade de rastrear erros e comportamentos em múltiplos serviços ensina disciplina de log estruturado e métricas, que pode ser observada como melhoria em monólitos.
5. **Consistência de dados e transações** — entender consistência eventual e o saga pattern ajuda a lidar melhor com cenários de concorrência e integração, mesmo num único banco de dados.
6. **Comunicação assíncrona** — aprender sobre filas e eventos ensina quando desacoplar processos, como envio de e-mail ou geração de relatório, fora do fluxo principal da aplicação.
7. **Cultura de times autônomos** — entender a filosofia por trás de squads independentes ajuda a pensar em organização de times e propriedade de código, mesmo sem arquitetura distribuída.

## Reaproveitando Peças Prontas do Ecossistema de Microsserviços

E não para só na teoria — dá para aproveitar literalmente peças prontas desse mundo, mesmo num projeto que não é microsserviços de verdade. O autor cita que, sempre que começa um novo projeto, já tem alguns microsserviços "na manga" — como por exemplo um serviço de autenticação e autorização como o Keycloak, que já reúne em si próprio todos os requisitos necessários para lidar com autenticação e autorização (inclusive autenticação federada), garantindo que o time não invista tempo a mais nesses requisitos que já possuem frentes amplamente estabelecidas de código livre, abertamente utilizáveis.

## Conclusão: Vale a Pena Estudar, Mesmo Sem Usar

É por isso que, quando alguém pergunta se vale a pena estudar microsserviços mesmo que a empresa não use no dia a dia, a resposta é sempre a mesma: vale, e muito. Porque o que você ganha é muito mais do que só um estilo arquitetural a mais para o catálogo — você ganha repertório, que hoje em dia é fundamental para quem desenvolve ou pretende desenvolver software de maneira profissional.

Fundamentos, conceitos e aprendizados são o que sobra depois que a moda passa. Microsserviços foram hype, viraram alvo de crítica, e hoje são usados com muito mais equilíbrio — mas os conceitos aprendidos estudando esse tema continuam valendo em qualquer projeto, distribuído ou não, e vão continuar valendo por muitos e muitos anos.

## IA Não Substitui Julgamento

É justamente aqui que entra um ponto fundamental: a IA é uma ferramenta poderosa, escreve código, sugere arquitetura, acelera decisões que antes levavam horas ou dias — mas ela não substitui o julgamento de quem entende de fato o que está sendo construído. Uma IA pode sugerir 10 formas diferentes de estruturar um sistema; decidir qual delas faz sentido para o seu contexto, para o seu time, para o seu produto, isso ainda depende da sua curadoria.

Sem fundamentos, você não sabe quando a sugestão da IA faz sentido e quando ela é só mais uma salada de letrinhas bonitas para agradar a gestão, o time, ou o seu post no LinkedIn.

A provocação final: use todas as ferramentas que o mercado te oferecer, mas nunca pare de estudar os fundamentos e os conceitos por trás delas. Foi isso que trouxe o autor — e muitos outros excelentes profissionais — de volta ao mercado, e é isso que vai manter você relevante daqui a 5, 10 anos, não importa qual seja a próxima moda que venha e saia.
