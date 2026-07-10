# Mappers — conversão de entidades entre camadas (Clean Architecture / Ports & Adapters)

> Transcrição de vídeo. Formatada em Markdown para ingest na wiki, sem alteração de conteúdo ou opinião do autor. Já estava em português, sem necessidade de tradução; falas foram limpas de repetições e organizadas em seções para leitura, sem alterar o conteúdo técnico.

Vamos entrar num conceito muito legal, que é o conceito de **mappers**, muito utilizado em arquiteturas de código organizadas em camadas — a própria Clean Architecture e Ports and Adapters são exemplos de arquiteturas com múltiplas camadas.

## O problema: a mesma entidade, representada de formas diferentes em cada camada

Quando se tem uma arquitetura com múltiplas camadas, uma das coisas comuns de acontecer é ter a representação da mesma entidade em formatos diferentes em cada camada.

Exemplo: pensando em uma entidade de `Notification` (notificação):

- Na **camada de persistência** (banco de dados, ex.: dentro de `infra`), a notificação é tratada como uma tabela no banco — mas continua sendo a mesma entidade `Notification`.
- Na **camada de aplicação/domínio**, essa entidade também existe, representada como uma classe (a entidade original, criada nas `entities`).
- Na **camada HTTP**, que é a camada que expõe os dados para o front-end (ou para qualquer consumidor da aplicação), também existe uma representação da notificação nos retornos das rotas. Hoje esse retorno está usando diretamente o retorno do use case, mas o ideal seria moldar a forma como a notificação é devolvida ao front — por exemplo, ao ver o retorno atual no Insomnia, o formato está "esquisito".

O formato correto seria, na hora de retornar a notificação pela API, formatar o objeto explicitamente: pegar só o campo `id` (que vem de `notification.id`), o `content` (que vem de `notification.content.value`, pois é um Value Object), a `category` (de `notification.category`) e o `recipientId` (de `notification.recipientId`). Quando isso é feito, o objeto retornado deixa de ser a entidade original — não é mais a mesma classe `Notification` criada anteriormente, e sim quase uma nova entidade, um novo formato de trabalhar com a notificação.

**Conclusão do problema:** mesmo existindo uma única entidade de notificação conceitualmente, ela é representada de maneiras diferentes em cada camada da aplicação, e frequentemente é preciso converter de um formato para outro.

## Exemplo concreto: salvando no Prisma

Ao salvar a notificação no Prisma, dentro do repositório, não é possível salvar a classe `Notification` (das `entities`) exatamente como ela é. É necessário converter — um processo de mapeamento (mapping): pegar o `id` da entidade e mapear para o campo `id` do Prisma, e assim por diante, campo a campo. Isso é, na prática, um processo de **map**.

O problema é que esse processo tende a se repetir — conforme a aplicação cresce e surgem mais métodos, esse mesmo mapeamento precisaria ser refeito em vários lugares. Para evitar essa repetição e desacoplar o código (permitindo reaproveitamento), cria-se um **mapper**.

## Mappers são associados a cada camada específica

Os mappers ficam totalmente associados à camada/tecnologia que representam. Por exemplo, o Prisma recebe as informações para criar uma notificação de uma maneira específica. Se um dia o ORM for trocado, a forma de receber os dados provavelmente muda também — então o mapper, nesse caso, está atrelado ao Prisma. Trocar de Prisma para outro ORM provavelmente exige um mapper diferente, porque o processamento necessário pode mudar.

### Implementação do mapper

Criar um arquivo/classe `PrismaNotificationMapper`, exportando uma classe `PrismaNotificationMapper` com um método **estático** chamado `toPrisma`.

- O método é estático porque não é necessário instanciar a classe `PrismaNotificationMapper` para usá-lo.
- `toPrisma` recebe a notificação original — a entidade `Notification` da camada de aplicação/domínio — e converte para o formato que o Prisma precisa para persistir os dados.
- Dentro do método, monta-se o objeto no formato esperado pelo Prisma e faz-se o `return` desse objeto.

### Uso no repositório

No repositório, ao invés de montar manualmente o objeto para salvar, cria-se uma constante — o autor costuma chamar de `raw` (não pode se chamar `notification` porque esse nome já está em uso pelo parâmetro; outras opções seriam algo como `persistenceNotification`, mas `raw` é mais curto e não prejudica a leitura). Essa constante recebe o retorno de `PrismaNotificationMapper.toPrisma(notification)`, que devolve os dados exatamente no formato necessário para salvar no Prisma — porque foi exatamente esse o formato retornado dentro do método `toPrisma`.

## Resumo

O mapper faz o trabalho de conversão dos dados entre o formato da entidade de domínio e o formato exigido por uma camada específica (banco de dados via Prisma, HTTP, etc.), evitando repetição de lógica de conversão espalhada pelo código e mantendo o acoplamento a uma tecnologia (como o ORM) isolado em um único lugar.
