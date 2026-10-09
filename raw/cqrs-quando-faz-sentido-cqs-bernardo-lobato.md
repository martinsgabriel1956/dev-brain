---
title: "CQRS: o que é, de onde veio (CQS) e quando faz sentido"
source_type: transcrição de vídeo (PT-BR, fala corrida)
author: "Bernardo Lobato"
date_ingested: 2026-10-09
---

# CQRS: o que é, de onde veio (CQS) e quando faz sentido

> Transcrição limpa (pontuação, parágrafos e termos corrigidos). Já em português; sem tradução. Correções de ASR: "Cqs/RS" (quando se refere ao padrão) → CQRS; "Cafca" → Kafka; "eventour" → event sourcing; "Mayer" → Meyer; "queres" → queries; "consistência virtual" → consistência eventual; "Commandery" → CQRS. Autor identificado pela própria apresentação no vídeo.

## Abertura

O que você faria se, depois de semanas refinando as regras de negócio do sistema, descobrisse que, diante de tanta complexidade do modelo, os relatórios e as telas de consulta estão extremamente lentos? E se o sistema tivesse que processar milhares de alterações por segundo e responder milhões de consultas sobre os mesmos dados ao mesmo tempo, sem comprometer a eficiência? No vídeo de hoje: entender CQRS e, principalmente, quando essa separação realmente faz sentido — e se é preciso uma arquitetura complexa para implementar o padrão.

Olá, devs, eu sou Bernardo Lobato e hoje vamos falar brevemente sobre CQRS: o que é, o que não é, um breve histórico, como aplicar e quando faz ou não sentido utilizar.

## O que é CQRS

CQRS é *Command Query Responsibility Segregation*: uma abordagem que propõe separar as operações que modificam o estado de uma aplicação (ou de um objeto) das operações que apenas consultam esse estado. A ideia parte de uma observação simples: as necessidades de leitura e de escrita de um sistema podem ser diferentes e, quando essa diferença se torna muito relevante, não deveria existir a obrigação de usar sempre o mesmo modelo para atender os dois lados.

Isso significa mais de um banco de dados? Um serviço para ler e outro para escrever? Calma, já chegamos lá.

Em uma aplicação tradicional é comum haver um único modelo de domínio/dados usado tanto para receber alterações (cadastros, edições) quanto para responder a consultas (relatórios, telas simples). No CQRS, um modelo é orientado às operações de escrita — responsável por representar todas as regras de negócio e todas as invariantes que precisam ser preservadas — enquanto o outro é construído especificamente para as necessidades de leitura.

## O que CQRS não é

CQRS **não exige**, por definição, microsserviços, event sourcing, mensageria, Kafka ou sequer dois bancos de dados separados. Esses recursos podem ser usados em conjunto, mas não devem servir de muleta para o uso do CQRS. É possível aplicar a separação entre comandos e consultas dentro de uma aplicação monolítica, com o mesmo banco, porque o conceito fundamental está na separação de responsabilidades, não na infraestrutura.

## Origem: CQS (Command Query Separation)

CQRS não surgiu como arquitetura distribuída nem como estratégia para sistemas de grande escala. Antes dele já existia o *Command Query Separation* (CQS), que propunha separar comandos de consultas no próprio design das operações de um sistema, distribuído ou não.

O princípio é associado a **Bertrand Meyer** e foi apresentado no livro *Object-Oriented Software Construction* (originalmente 1988) — o livro está disponibilizado gratuitamente pelo próprio autor (link na descrição do vídeo). A ideia: as operações de um objeto devem ser separadas em **commands** (modificam o estado do objeto) e **queries** (fornecem informação sem modificar, em hipótese alguma, o estado).

Exemplo: num objeto `Customer`, `changeAddress` é um command (altera o estado); `getAddress` é uma query (apenas consulta uma informação já existente).

A motivação era relevante: quando uma operação só consulta, pode ser usada com muito mais previsibilidade, porque se sabe que ela não produz alteração observável no objeto nem no sistema — uma leitura simples não deveria ter efeito colateral de negócio. E quando uma operação modifica o estado, isso fica explícito para quem a usa, em vez de uma função que ao mesmo tempo retorna informação e produz efeito colateral. O CQS torna o comportamento mais previsível e o modelo mais fácil de entender.

**Distinção importante:** CQS é um princípio de design aplicado à forma como se modelam as operações em objetos. Não propõe separar banco de dados, serviços ou modelos inteiros de leitura/escrita. Uma operação representa só uma consulta ou só uma alteração; tudo continua dentro do domínio de classes, métodos e objetos, interno à aplicação.

**Exemplo didático — notificações** (rede social, chat): ao clicar no botão de notificações, o próprio ato de consultar já marca a notificação como lida. Se existir só o método `visualizarNotificacoes`, responsável por buscar *e* marcar como lidas, a manutenção e a reutilização do método em outros módulos ficam difíceis por causa do efeito colateral. Separando em `obterMensagensNaoLidas` e `marcarMensagensComoLidas`, o comportamento fica previsível. Isso é implementação interna: a UI pode continuar com exatamente o mesmo comportamento.

Foi essa ideia de separar comandos e consultas que, anos depois, foi levada a outro nível de abstração e deu origem ao CQRS.

## Do CQS ao CQRS: separar os modelos

Até aqui a separação era no nível das operações, internamente nas classes. Podemos levar a mesma ideia para um nível maior: o mesmo sistema pode ter necessidades muito diferentes para ler e escrever. O modelo que representa bem as regras para alterar o estado pode não ser o mais adequado para responder às consultas. O modelo de escrita se preocupa com regras de negócio, invariantes e consequências das alterações; o modelo de leitura se preocupa com a forma como os dados são consultados, apresentados em telas ou combinados em relatórios.

Então há um **write model**, usado pelas operações de escrita, e um **read model**, construído de acordo com as necessidades de leitura. É isso que está por trás do CQRS: levar a separação que existia no nível das operações (CQS) para o nível dos modelos usados pela aplicação. A partir daqui deixa de ser só organização de código e passa a ser uma **decisão arquitetural** — que só se justifica se trouxer uma vantagem que compense a complexidade adicional. Se um único modelo atende às duas necessidades, criar dois modelos é complexidade sem benefício.

## Quando faz sentido

### 1. Assimetria entre leitura e escrita

Um sistema pode ter regras complexas para modificar dados enquanto suas consultas precisam de uma representação completamente diferente das mesmas informações.

Exemplo — e-commerce: um pedido tem vários itens, o preço precisa ser validado por diferentes regras de domínio, descontos seguem regras complicadas, o estoque precisa ser reservado, o pagamento autorizado, e certos estados do pedido não podem ser alterados arbitrariamente porque a transição precisa respeitar regras de negócio. Algumas alterações precisam respeitar invariantes do domínio. Esse modelo é excelente para proteger os dados, mas não necessariamente é uma boa estrutura para responder a uma consulta que combina informações de várias partes do sistema.

Imagine agora uma tela com: número do pedido, nome do cliente, total de produtos, total pago, status do pagamento, situação da entrega e status do pedido. Para montá-la queremos uma visão extremamente simples, juntando pedido, pagamento, entrega e produtos — sem usar toda aquela estrutura de regras. E essa tela provavelmente é muito mais acessada do que as operações que modificam os status. Poderíamos ter um modelo de pedido, com suas regras e invariantes, e outro modelo de consulta com esses dados consolidados.

Atenção: não é simplesmente ter muitas leituras e poucas escritas que determina o uso adequado de CQRS. A natureza do trabalho em cada lado é diferente. O modelo de leitura pode ser mais simples, mais desnormalizado e até ter uma estrutura completamente diferente do modelo de escrita. Também ajuda quando há **múltiplas projeções** das mesmas informações (visão do usuário, dashboard, relatórios, integrações), cada uma justificando uma representação diferente. E há a questão de **escala**: se as características de leitura e escrita são muito diferentes, pode-se querer otimizar cada lado de forma independente (armazenamento, indexação, processamento, serviços de nuvem).

### 2. Precisa existir um problema concreto

Parece óbvio, mas é difícil defender o óbvio. A complexidade do sistema, por si só, não justifica separar os modelos. O CQRS começa a fazer sentido quando os modelos de leitura e escrita têm responsabilidades significativamente diferentes, a ponto de manter um único modelo criar mais problemas do que resolver.

Exemplo — contador de visualizações num YouTube hipotético: a cada visualização é preciso registrar e somar um contador, enquanto milhares ou milhões de pessoas consultam o mesmo número na tela do vídeo. Usar o mesmo modelo para registrar cada visualização e responder constantemente à consulta cria uma disputa desnecessária entre duas necessidades muito diferentes. A gravação da view provavelmente envolve mais regras de domínio do que a simples contagem; seria uma tragédia ninguém conseguir assistir a um vídeo porque a tabela de visualizações está travada (*locked*) por excesso de gente tentando ver. Um modelo de escrita otimizado para receber atualizações em alta frequência e um modelo de leitura otimizado para responder rapidamente "quantas visualizações o vídeo tem?" — os dois lados trabalham com a mesma informação de negócio, mas com necessidades bem diferentes.

### 3. Quando a separação simplifica uma parte importante do sistema

Apesar de haver dois modelos em vez de um, cada um fica mais adequado ao seu propósito, e partes da aplicação podem ficar mais simples de entender e evoluir.

Exemplo — sistema financeiro: o modelo de escrita lida com saldo, lançamento, estorno, transferência, conciliação etc.; a tela de extrato não precisa conhecer essa complexidade — precisa de uma lista com data, descrição, valor, tipo de movimentação e saldo após o lançamento. Usando o mesmo modelo nos dois lados, a tela de consulta acaba dependendo de toda a estrutura de regras de uma movimentação. Separando, o modelo de escrita foca nas regras e operações financeiras e o de leitura é uma representação bem mais simples criada para o extrato. O benefício aqui não é processar mais requisições nem usar um banco mais rápido: é tornar cada lado mais simples de entender.

### 4. A complexidade adicional precisa ser compensada

Na opinião do autor, é um dos critérios mais importantes. Adotar CQRS significa aceitar mais modelos, mais código, mais processo e, dependendo da implementação, mais infraestrutura. Num sistema de pedidos simples (cria pedido, adiciona produtos, acompanha status, consulta histórico), existe separação conceitual entre leitura e escrita — poderíamos criar um modelo de escrita e um de leitura para o histórico, talvez com uma projeção otimizada —, mas a pergunta é se isso resolve um problema relevante. Se o domínio é simples, o volume baixo, as consultas diretas e o mesmo modelo atende bem, provavelmente só se está adicionando complexidade.

A partir do momento em que se adota CQRS é preciso manter dois módulos, definir como o modelo de leitura é atualizado, lidar com possíveis inconsistências entre leitura e escrita, e aumentar a quantidade de componentes que a equipe precisa entender e manter. A separação pode ser tecnicamente possível, mas o benefício não compensar o custo. Em arquitetura não basta a solução funcionar: o benefício precisa justificar a complexidade introduzida.

## Custo de implementação

Adotar CQRS não é criar uma classe para command e outra para query. É preciso definir como os modelos são construídos, como o modelo de leitura é atualizado, como os dados são sincronizados e como tratar falhas no meio do processo. Numa implementação simples, pode-se usar o mesmo banco e atualizar o modelo de leitura dentro da própria aplicação — não precisa ser distribuído. Conforme as necessidades crescem, pode-se chegar a eventos, filas, consumidores e até bancos diferentes.

Se o modelo de leitura é uma projeção do modelo de escrita, é preciso um mecanismo para mantê-los sincronizados. Dependendo da implementação, isso pode introduzir **consistência eventual**: uma alteração na escrita pode levar um tempo para aparecer no modelo de leitura, se o negócio permitir. Isso muda a forma de operar e observar o sistema: um problema que antes acontecia numa única operação agora pode envolver escrita, atualização do modelo de leitura e todos os componentes entre os dois pontos. O debug também fica mais complicado: a alteração foi gravada? O evento foi publicado? A projeção foi processada? O modelo de leitura foi atualizado?

## Arquitetura distribuída é opcional

Dá para ter CQRS dentro da mesma aplicação, com o mesmo banco, aplicando os conceitos. Uma arquitetura distribuída aparece quando existe motivo para separar fisicamente ou operacionalmente as partes. Aí o CQRS pode ser combinado com outros padrões, mas eles não fazem parte do CQRS por definição: por exemplo, uma arquitetura orientada a eventos em que uma alteração no modelo de escrita gera um evento consumido por um componente que atualiza o modelo de leitura; mensageria; filas; bancos diferentes para cada modelo; escala independente dos componentes; estratégias de armazenamento específicas. CQRS pode usar event-driven, mensageria e bancos separados, mas nenhuma dessas coisas é requisito para o CQRS existir.

## Quando não usar

Há vários cenários em que o CQRS não traz benefício suficiente: um CRUD de pouca complexidade de domínio, consultas diretas e um modelo que atende bem leitura e escrita; necessidades de leitura e escrita praticamente iguais; volume de operações que não exige estratégias diferentes; ou quando a separação só adicionaria abstrações e componentes sem resolver nenhuma dificuldade real. Nesses casos, manter uma arquitetura mais simples é uma decisão perfeitamente válida. O fato de o CQRS ser capaz de resolver determinados problemas não significa que deva ser usado sempre que a aplicação é um pouco mais complexa.

## Fechamento

A pergunta correta: **existe uma diferença entre leitura e escrita que justifique a complexidade de manter esses dois lados separados?** Se sim, pode ser uma ferramenta útil. Se essa diferença não existe, separar os modelos provavelmente só adiciona complexidade onde não é necessário. O autor oferece uma continuação com estratégias de implementação ou conceito mais aprofundado, se pedida nos comentários.
