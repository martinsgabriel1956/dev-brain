# Comunicação Assíncrona — Arquiteturas Distribuídas (Bernardo Lobato)

Fonte: transcrição de vídeo do YouTube, canal de Bernardo Lobato, vídeo introdutório sobre comunicação assíncrona, preparatório para a série sobre arquiteturas/padrões arquiteturais distribuídos. Já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento de fala.

Termos corrigidos por contexto (transcrição automática): "Devos" → Devs; "autoacoplamento" → alto acoplamento; "restt" → REST; "KFC" → Kafka; "RaptamQue" → RabbitMQ; "pulling" → polling; "end específico" → endpoint específico; "o nosso tech" → tech lead (provável); "gerar atração" → ganhar tração; "eh" (hesitação) removido. Trecho ambíguo: "já abre as suas cinco APIs ali que precisa para conseguir testar um módulo só" (abertura) — provável sugestão irônica de quem precisa subir várias APIs localmente só para testar um módulo; mantido como dito. Trecho ambíguo no fecho: "os nossos f gerados microsserviços" — provavelmente "e os nossos queridos microsserviços"; mantido como "microsserviços". Pedidos de like/inscrição/compartilhamento preservados no fecho por fidelidade, mas sem valor técnico.

---

## Abertura

Você já se viu esperando o retorno de uma API que o seu sistema integra, e esse retorno levava de 5 a 10 segundos e acabava engargalando o sistema como um todo? Já precisou integrar dois sistemas em que um deles estava muito bem desenhado e muito bem implementado, e o outro vivia caindo e demorando nas respostas? Isso acabou impactando a experiência do usuário como um todo. Então esse vídeo é para você. (Comentário irônico: já abre as suas cinco APIs que precisa para conseguir testar um módulo só.)

Olá, Devs, eu sou Bernardo Lobato. No nosso caminho até chegarmos aos padrões arquiteturais distribuídos — as arquiteturas distribuídas — vamos precisar passar por alguns conceitos importantíssimos, e o vídeo de hoje é um deles: a **comunicação assíncrona**.

Não é comum no nosso dia a dia — até pela forma como aprendemos a programar e como os projetos são desenvolvidos hoje — utilizar de maneira corriqueira a comunicação assíncrona. Mas vamos ver ao longo do vídeo que, quando bem utilizada, ela pode ter muitos benefícios e ajudar a salvar o seu projeto e a sua arquitetura.

---

## Comunicação síncrona (breve introdução)

Antes de falar de comunicação assíncrona, vamos falar brevemente da **comunicação síncrona**: aquela em que o nosso serviço ou sistema faz uma chamada para outro serviço ou sistema e já tem o retorno dessa chamada — já tem os dados de que precisa para trabalhar. Fazemos a solicitação e, muito provavelmente, o nosso fluxo de trabalho fica **bloqueado** até termos o retorno e prosseguir.

**Exemplo: autenticação e autorização.** Nessa arquitetura existe um serviço específico para autenticação e autorização, externo à nossa aplicação. Quando precisamos autenticar ou autorizar, fazemos uma chamada a esse serviço e aguardamos, bloqueados, até termos os dados da autenticação — por exemplo, um token JWT ou qualquer outro formato.

Essa comunicação parece mais simples e mais intuitiva, e de fato é, mas esconde problemas e armadilhas não tão triviais de visualizar num primeiro momento:

1. **Alto acoplamento.** Os dois sistemas — o que desenvolvemos e a API externa de autenticação/autorização — ficam altamente acoplados, de modo que qualquer alteração em um pode causar efeito colateral no outro.
2. **Baixa resiliência.** Se o sistema de autenticação cair, falhar ou ficar muito lento, ele prejudica a solução como um todo; o sistema pode ficar completamente inviável de ser utilizado caso um desses componentes caia ou não funcione adequadamente.

Este ainda não é o vídeo sobre comunicação síncrona; o autor promete, mais à frente, um vídeo muito mais detalhado sobre benefícios e melhor aproveitamento dela. Esta introdução serve só para entender a problemática e como a comunicação assíncrona pode endereçá-la.

---

## Comunicação assíncrona: conceito

A comunicação assíncrona é outro modelo de comunicação, pouco difundido nos projetos mais triviais do dia a dia — em parte pela falta de familiaridade dos desenvolvedores com essa forma de se comunicar, e em parte pela sua própria complexidade (vista ao longo do vídeo e dos vídeos sobre arquiteturas distribuídas). Mas, usada de maneira adequada, traz benefícios que podem salvar a arquitetura e o projeto.

**Definição:** a comunicação assíncrona acontece quando um sistema envia uma mensagem (ou chama um método externo de determinada API ou serviço) e **não espera a resposta imediatamente**. O serviço que recebe a mensagem pode processar os dados em background, sem devolver imediatamente ao emissor. Uma vez processados, é preciso uma maneira de **notificar o emissor** de que o processamento foi concluído — ou o serviço originário passa a **solicitar o status** do processamento de tempos em tempos.

**Analogia do WhatsApp:** é como mandar um áudio no grupo. Você manda e não precisa ficar esperando todo mundo responder; conforme as pessoas vão ouvindo, vão tendo tempo de responder, e você recebe essas respostas e age de acordo.

---

## Síncrona vs. assíncrona (tabela do vídeo)

| Aspecto | Síncrona | Assíncrona |
|---|---|---|
| Tempo de resposta | Imediato: a requisição já devolve os dados do processamento | Não imediato: é preciso esperar para receber os dados ao final do processamento (há várias estratégias para receber) |
| Acoplamento | Forte: um serviço vira codependente do outro; se um cair, pode prejudicar a arquitetura/sistema como um todo | Fraco: mesmo com um sistema lento, o funcionamento do restante não é necessariamente comprometido; outras partes seguem normalmente mesmo com uma API lenta |
| Exemplo | Comunicação REST entre microsserviços | Mensageria via broker (Kafka, RabbitMQ ou outros) |

---

## Formas de estabelecer comunicação assíncrona

Existem outras maneiras de estabelecer comunicação assíncrona sem necessariamente utilizar mensageria:

1. **Polling por ID de operação.** O serviço retorna um **ID da operação** ao solicitante; de tempos em tempos o cliente faz **polling** em um endpoint específico, com esse ID como parâmetro, e o endpoint devolve o **status** da solicitação ou, se já concluída, os **dados** do processamento.
2. **Webhook / callback.** O receptor devolve apenas um **OK** quando a mensagem chega do cliente solicitante; depois, quem está processando chama um **webhook** (ou **callback**) cadastrado na estrutura do cliente/solicitante, e esse callback é o responsável por dar o tratamento adequado às mensagens/dados.
3. **Mensageria: broker de tópicos ou eventos.** Uma das maneiras mais utilizadas de comunicação assíncrona. Será tratada especificamente em vídeo futuro.

As duas primeiras são bastante comuns em arquiteturas mais simplificadas ou quando não temos muito controle sobre todos os sistemas envolvidos — por exemplo, ao integrar com uma **API externa** que não é desenvolvida pelo nosso time, já está em produção e funciona, e nós precisamos nos adequar às regras dela.

---

## Exemplo prático: sistema de pedidos (e-commerce simplificado)

Contexto: serviço de **Pedidos**, que em algum momento recebe um pedido, que precisa ser integrado ao subsistema de **Estoque** (produtos) e ao sistema de **Pagamentos/Faturamento**.

Uma maneira de estabelecer comunicação assíncrona mantendo dependência baixa entre os três serviços é **publicar um evento em uma fila (ou tópico)**:

- Quando um pedido é criado, gera-se um evento/mensagem de **pedido criado** e publicam-se todas as informações do pedido na fila/tópico.
- Os serviços de **Produtos/Estoque** e de **Faturamento** escutam a mesma fila; quando a mensagem do pedido cai, ambos leem a mesma mensagem e prosseguem com seus tratamentos individuais:
  - **Produtos/Estoque:** aloca a quantidade devida no estoque.
  - **Pagamentos/Faturamento:** faz a cobrança devida — no cartão de crédito, via Pix, boleto etc.

**Nenhum desses serviços depende da resposta imediata dos outros.** Mesmo com um exemplo simples, isso melhora a **escalabilidade**, o **desempenho** e a **autonomia** dos serviços entre si — sem falar na **manutenibilidade**: com essa arquitetura, times reduzidos de desenvolvimento podem trabalhar somente em um serviço específico, sem precisar conhecer a fundo a solução como um todo.

---

## Complexidade maior e benefícios

O modelo assíncrono **tem complexidade maior** que o síncrono — é preciso investir tempo na capacitação do time (ou na sua própria), fazendo exemplos e estudando essas formas de integrar. Mas, se bem utilizado, os benefícios são incríveis, podendo ser a diferença entre o sistema funcionar e não funcionar.

- **Arquiteturas distribuídas** (microsserviços, arquitetura baseada em eventos) se beneficiam fortemente desse modelo, pois permite sistemas mais **desacoplados e tolerantes a falha**: se um serviço cair, a experiência como um todo não é prejudicada; quando o serviço voltar, ele **relê as mensagens que perdeu** e continua o processamento normalmente, como se nada tivesse acontecido.
- **Picos de carga:** pense num e-commerce na **Black Friday**. Os serviços de pagamento ou geração de pedidos podem sofrer um pico de carga, e não é necessário escalar a solução como um todo para atender essa demanda maior em um único dia.

**Aviso:** é essencial saber o que se está fazendo e **não usar comunicação assíncrona "por usar"**, sem um detalhamento melhor de como ela funcionará na arquitetura específica — principalmente quando o time está acostumado ao modelo tradicional com REST e HTTP. É muito comum, em times que estão adotando o modelo agora, **tentar emular uma comunicação síncrona sobre o modelo assíncrono; isso não funciona**. O ideal é aprender como funciona o modelo assíncrono, suas boas práticas, e usá-lo dentro da arquitetura/produto.

---

## Três grandes desafios da comunicação assíncrona

(Existem outros, mas serão tratados nos próximos vídeos, para não ficar denso.)

1. **Debug.** Como a comunicação é assíncrona, não há um passo a passo bem direcionado de onde um problema X pode acontecer; pode ser preciso depurar vários sistemas individualmente sem saber necessariamente a ordem ou como o problema surgiu. Existem ferramentas que dão **rastreabilidade** a esse problema; ao falar de **observabilidade**, isso ficará claro.
2. **Garantia de entrega.** Principalmente no modelo de fila ou tópico, muitos brokers de mensageria **não têm, por padrão, a configuração ajustada** para garantir que a mensagem será entregue a todos os seus receptores. É um cuidado necessário ao desenvolver uma aplicação assíncrona.
3. **Consistência eventual.** Pode ser o maior problema se não for planejado. Se gero um pedido em um serviço e um pagamento em outro, no meio tempo em que o pagamento é processado, bloqueado ou disponibilizado — qualquer mudança de status — essa mudança pode demorar a se propagar para o outro serviço; consultar a informação ali pode retornar dado **desatualizado**. Daí o nome: **eventualmente** ela será atualizada, mas não necessariamente agora. É importante ter isso em mente, inclusive para "vender" o modelo à liderança ou ao cliente: **os sistemas não estarão consistentes o tempo inteiro**.

---

## Vale a pena?

Dependendo do sistema, **vale e muito**. Talvez não tenha ficado tão claro neste vídeo, mas o tema da comunicação assíncrona será recorrente nos próximos vídeos, sempre detalhando um pouco mais para fixar os benefícios desse modelo.

Com esses conceitos já há base para conversar sobre arquiteturas distribuídas e evoluir para estilos arquiteturais mais complexos: **CQRS**, **Event Sourcing**, **arquitetura baseada em eventos** e **microsserviços**. Os próximos vídeos explorarão esses padrões arquiteturais distribuídos com mais detalhes.

---

## Fechamento

O autor pede like, comentário, inscrição no canal ("a gente está bem no começo, precisa ganhar tração") e que o vídeo seja compartilhado com o time de desenvolvimento e com o tech lead. Pergunta final ao público: já conhecia a comunicação assíncrona? Já precisou integrar algum sistema com mensageria ou com callback? Como fez, e quais problemas enfrentou?
