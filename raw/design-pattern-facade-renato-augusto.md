# Facade (Fachada) — Padrão de Projeto Mais Simples de Implementar

**Autor/Canal:** Renato Augusto
**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (sem necessidade de tradução)
**Tema:** Padrão de projeto estrutural Facade, com exemplo prático de e-commerce (Order Controller → Order Facade)

---

## Introdução

Fala pessoal, Renato Augusto aqui. No vídeo de hoje vou te ensinar o padrão de projeto mais simples e mais fácil de implementar: o padrão **Facade** (ou Façade, ou em português, Fachada).

Basicamente, é uma interface entre o teu código cliente e a complexidade que você deseja ocultar do teu código, para tornar ele um pouco mais estável — ou seja: instanciação de objetos, complexidade de regras de negócio, controle de fluxo, e por aí vai. Tudo isso a gente já vai pra telinha ver como funciona.

Antes de mais nada: tudo que eu te ensino aqui é completamente agnóstico de linguagem de programação, então você vai conseguir implementar isso na sua linguagem e no seu framework favorito.

## A Analogia

Aqui no Refactoring Guru a gente não perde tempo com teoria — tudo que tá aqui eu vou te ensinar na prática, porque faz muito mais sentido aprender assim. Mas a analogia eu achei interessante — inclusive ela faz parte do código que a gente vai implementar.

Imagine que você é um cliente e precisa fazer um pedido por telefone, uma compra. Nesse pedido, você precisa de uma fachada para intermediar você e toda a complexidade por trás de um pedido. Não faz sentido que você soubesse como dar baixa no estoque, como funcionam os fornecedores do produto que você comprou, as taxas, processar o pagamento. Você precisa de uma fachada que intermedeie a resolução do teu pedido com toda a complexidade por trás dele. Você, como cliente, só tem que fazer o teu pedido — é a única coisa que você quer.

Uma analogia mais próxima do mundo real: você provavelmente já comprou na Amazon ou no Mercado Livre. O site ou o aplicativo é a tua fachada. Você faz o pedido na plataforma, mas não precisa saber que tem que dar baixa no estoque, processar o pagamento, aplicar impostos, calcular a rota de entrega. Você é só o cliente — quando entra no site, só faz o seu pedido.

Quando a gente fala de código: o teu código cliente tem que apenas fazer aquilo que foi programado para fazer. Ele não tem que cuidar de fluxo, não tem que cuidar de toda uma complexidade.

## O Problema (Exemplo Prático)

Vamos fazer uma simulação: a gente trabalha num e-commerce e tem um `OrderController` — o controller de pedidos. Existe um endpoint para criar um novo pedido. O cliente está na interface gráfica, no formulário, seleciona o pedido que quer, finaliza o pagamento, e essa requisição chega no endpoint.

O trabalho desse endpoint: pegar os dados da requisição (nomeados `OrderDetails`) e passar para algumas classes de serviço, num passo a passo estabelecido:

1. Processar o pagamento (`PaymentProcessor`)
2. Enviar confirmação por e-mail (`Notifier`)
3. Atualizar o estoque (`InventoryManager` / equivalente)
4. Inicializar a entrega

Cada uma dessas classes de serviço faz exatamente o que foi feita para fazer — está seguindo corretamente o **S** do SOLID (responsabilidade única). A classe de processar pagamento só processa pagamento; o `Notifier` só envia notificação; o manager de inventário só atualiza estoque.

O problema é que o **Controller está cuidando do fluxo**. A ordem importa: se você inverter `processPayment` com o envio de confirmação, dá problema — o cliente recebe um e-mail dizendo que o pagamento foi aprovado antes mesmo do pagamento ser processado. Ou seja, o Controller está sabendo demais sobre como um pedido deve ser processado.

### O gatilho da dor

Chega uma nova demanda: enviar um e-mail para o time comercial informando o estado do estoque daquele produto (se está acabando, se precisa fazer um novo pedido aos fornecedores). Para atender essa demanda, seria preciso alterar o `OrderController` — o que não é nada legal, porque:

- Controller não é lugar para regra de negócio.
- Se existir outro Controller/rota que também processa pedidos, a mesma lógica precisaria ser duplicada e mantida em sincronia manualmente.
- Se um desenvolvedor esquecer de replicar a mudança no outro lugar, o e-mail pro comercial simplesmente não é enviado ali.

É aí que o Facade entra: ocultar essa complexidade de dentro do código cliente, movendo o fluxo para uma classe própria. Assim, mudanças futuras no fluxo do pedido são feitas em um único lugar.

## A Implementação

Cria-se uma classe `OrderFacade` (dentro de uma pasta `service`, por simplicidade — o foco do vídeo não é a questão arquitetural).

No construtor da `OrderFacade`, injeta-se as dependências que antes viviam soltas no Controller: `PaymentProcessor`, `Notifier`, `InventoryManager`/estoque, serviço de entrega.

Cria-se um método `processOrder` (retorno `void`, recebendo um array de `OrderDetails` — o autor pontua que isso é obsessão por tipos primitivos e que, idealmente, se usaria um DTO/objeto de verdade em vez de array de tipos primitivos, inclusive para representar valor monetário — mas o foco do vídeo é o padrão, não modelagem de dados). Dentro desse método, cola-se o passo a passo que antes estava no Controller: processar pagamento → enviar confirmação → atualizar estoque → inicializar entrega (e, agora, também notificar o comercial sobre o estoque).

De volta ao `OrderController`: remove-se todo o fluxo e as instâncias das classes de serviço, e o Controller passa a apenas instanciar/injetar a `OrderFacade` e chamar `facade.processOrder(orderDetails)`. O Controller não sabe mais nada sobre o que acontece por trás — não sabe que precisa enviar notificação, não sabe da ordem das operações.

## O Debate: Facade Fere o "S" do SOLID?

Ponto polêmico do padrão: a `OrderFacade` está processando pagamento, enviando confirmação, atualizando estoque — parece estar "fazendo coisa demais".

A defesa do autor: o princípio da responsabilidade única é filosófico, não é sobre "cada trecho de código faz literalmente uma coisa". A `OrderFacade`, apesar de orquestrar um passo a passo, não faz nada além de **processar um pedido**. O único motivo para essa classe mudar é se o *processo de um pedido* mudar (ex: adicionar o e-mail pro comercial). Internamente, ela delega para classes que seguem SRP de forma estrita cada uma. Portanto, a Facade em si está alinhada com SRP no seu próprio nível de abstração — sua única razão de mudança é a mudança no fluxo de pedido.

O autor reconhece que esse é um ponto genuinamente controverso e gerador de debate na comunidade, assim como outros padrões de projeto.

## Fechamento

O Facade é, segundo o autor, o padrão de projeto mais simples de implementar: basicamente uma classe que encapsula complexidade, regra de negócio e controle de fluxo, ocultando isso do código cliente. O Controller (código cliente) passa a apenas delegar para a fachada, sem saber dos detalhes internos.
