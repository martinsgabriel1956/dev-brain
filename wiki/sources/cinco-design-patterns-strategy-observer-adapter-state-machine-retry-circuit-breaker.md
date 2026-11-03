---
type: source
title: "Cinco Design Patterns Úteis com ou sem IA: Strategy, Observer, Adapter, State Machine e Retry com Circuit Breaker"
aliases: ["cinco design patterns", "5 design patterns com ou sem ia", "strategy observer adapter state machine retry"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker.md
source_url: ""
author: "Não identificado (vídeo em português; o nome não aparece na transcrição). O patrocínio AUVP é sinal fraco de [[wiki/entities/lucas-montano]], não confirmado: outras fontes com esse patrocínio seguem sem autor definido, e a busca não achou o vídeo."
date_published: ""
date_ingested: 2026-11-03
source_count: 0
tags: [design-patterns, strategy, observer, adapter, state-machine, retry, jitter, circuit-breaker, resiliencia, pagamentos, agentes, tech-mentor-backend, tech-mentor-ai]
skill: tech-mentor-backend
status: stable
---

# Cinco Design Patterns Úteis com ou sem IA: Strategy, Observer, Adapter, State Machine e Retry com Circuit Breaker

## TL;DR

Vídeo didático que apresenta cinco [[wiki/concepts/design-patterns|padrões]] contra a gambiarra, com exemplos de notificação, compra e pagamento:

1. **[[wiki/concepts/strategy-pattern|Strategy]]:** formas intercambiáveis de fazer algo atrás da mesma interface, no lugar de `if/elif`. Exemplo: e-mail, SMS e push com um método `send`.
2. **[[wiki/concepts/observer-pattern|Observer]]:** quem emite o evento encerra o trabalho e não sabe quem ouve. Exemplo: compra finalizada e serviço de analytics.
3. **[[wiki/concepts/adapter-pattern|Adapter]]:** traduz a interface de um componente para a que o código espera. Exemplo: `charge` chamando `PayPal.pay`.
4. **[[wiki/concepts/finite-state-machine|Máquina de estados]]:** estados válidos mais um [[wiki/concepts/mapa-de-transicoes|mapa de transições]], no lugar de `if`s espalhados. Exemplo: ciclo de vida de um pedido.
5. **[[wiki/concepts/retry-backoff|Retry]] com [[wiki/concepts/circuit-breaker|circuit breaker]]:** do `while true` ingênuo até backoff exponencial, jitter e um breaker global para provedor fora do ar.

A contribuição mais útil é a [[wiki/concepts/strategy-com-adapter|combinação de Strategy com Adapter]]: a estratégia escolhe o provedor (cartão ou Pix), e o adaptador esconde o SDK dele.

**Limites da fonte:** não há dados nem casos reais, só exemplos didáticos. O código mostrado na tela não aparece na transcrição, então os detalhes vêm apenas da narração. O bloco de patrocínio (AUVP) não é conteúdo técnico; ficou no raw por fidelidade e foi ignorado aqui.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Strategy substitui ramificações por tipo e simplifica o core, que não precisa saber qual estratégia está em uso | Exemplo de notificação; converge com [[wiki/concepts/strategy-pattern]] | Alta |
| `if/elif` ou `switch` funcionam, mas viram gambiarra conforme as variações crescem | O próprio autor admite que funcionam; o custo aparece com o crescimento | Alta para o crescimento; não dá critério de quando começar: ver "Tensões" |
| Classes de estratégia com dependência injetada facilitam testar sem [[wiki/concepts/efeito-colateral|efeitos colaterais]], como enviar e-mail a um cliente | Raciocínio do autor; converge com [[wiki/concepts/dependency-injection]] | Alta |
| Observer desacopla: para o emissor, não faz diferença se alguém ouve | Exemplo de finalizar compra sem chamar `saveAnalytics` de forma síncrona | Alta para o desacoplamento; a descrição se aproxima mais de pub/sub: ver "Tensões" |
| Event driven é mais amplo que Observer | "Na minha concepção", diz o autor; converge com [[wiki/concepts/event-driven-architecture]] | Alta |
| Redis e BullMQ servem para fazer um emissor de eventos, com ressalva do próprio autor | Trecho ambíguo na transcrição ("exatamente mest") | Média: em [[wiki/concepts/bullmq]], cada job vai para um único worker, sem cópia por ouvinte |
| Adapter isola o provedor: trocar de provedor mexe só no adaptador | Exemplo do PayPal; converge com [[wiki/concepts/adapter-pattern]] | Alta |
| Strategy e Adapter se parecem, mas fazem coisas diferentes e combinam bem | Fluxo cartão→Stripe e Pix→AbacatePay | Alta |
| Um mapa de transições é mais limpo e validável que `if/else` espalhado | Exemplo de pedido; converge com o exemplo de tabela em [[wiki/concepts/finite-state-machine]] | Alta |
| Tecnicamente, um `if/else` também pode ser uma máquina de estados | O autor mesmo hesita ("posso estar viajando") | Média: vale quando há estados e transições, não para qualquer `if` |
| Máquina de estados ajuda a orquestrar agentes de IA, com requisitos, validação e gatilhos em cada transição | Raciocínio do autor; converge com [[wiki/concepts/grafo-como-abstracao-de-agentes]] | Alta |
| O n8n "é uma máquina de estados" | Afirmação sem justificativa | Média-baixa: a [documentação do n8n](https://docs.n8n.io/workflows/) `[external]` descreve nós conectados acionados por gatilho; vale como analogia. Visto só no resumo da busca |
| Retry sem espera pode lembrar um DDoS contra o próprio sistema | Raciocínio do autor; converge com [[wiki/concepts/thundering-herd]] | Alta |
| Backoff exponencial dá mais tempo de recuperação | Sequência de 1, 2 e 4 segundos, sem medição | Alta (converge com [[wiki/concepts/retry-backoff]]) |
| Jitter evita que as chamadas colidam no mesmo instante | Explicação do autor, entre partes do mesmo código | Alta |
| Um circuit breaker global evita chamar um provedor que já se sabe offline, com uma sondagem a cada 10 minutos | Raciocínio do autor | Alta para a ideia; os 10 minutos são exemplo, e "global" fica sem definição: ver "Questões abertas" |

## Tensões com a wiki

- **Retry em pagamento sem idempotência (lacuna importante):** o vídeo aplica retry a provedores de pagamento e não menciona [[wiki/concepts/idempotencia]]. Pela [[wiki/concepts/retry-backoff|página de retry]], ela é pré-requisito. Seguir o vídeo ao pé da letra pode cobrar duas vezes o mesmo cliente, depois de um timeout em que a cobrança na verdade passou. Ele também não separa erro transitório de erro permanente.
- **Observer ou pub/sub:** a wiki distingue Observer (referência direta ao subject) de Pub/Sub (broker intermediário). O vídeo fala em assincronia e em Redis, BullMQ ou solução na cloud, o que está mais perto de pub/sub ou de fila. Ver [[wiki/concepts/observer-pattern]].
- **Nem todos são GoF:** o vídeo chama os cinco de design patterns. Strategy, Observer e Adapter são do catálogo; retry e circuit breaker são padrões de resiliência (ver [[wiki/concepts/circuit-breaker]], que situa o breaker em *Release It!*). Já a máquina de estados é um modelo computacional, e o GoF tem o [[wiki/concepts/state-pattern|State]], que o vídeo não usa: ele usa um mapa de transições.
- **Quando não usar:** o vídeo não fala de custo. Com duas variações que não mudam, `if/else` pode bastar; ver [[wiki/concepts/over-engineering]] e [[wiki/concepts/yagni]] (inferência a partir da wiki, não dita pelo autor).
- **Adapter com moeda fixa:** no exemplo, o adaptador sempre passa USD. Serve à didática, mas um adaptador real precisa receber a moeda, senão perde informação na tradução (inferência). Também é provável que `PayPal.pay` seja ilustrativo, não a API real (não verificado).

## Questões abertas

- **O que é "global" no breaker?** Com várias instâncias da aplicação, o estado fica em cada processo ou é compartilhado (por exemplo, no Redis)? O vídeo não diz, e isso muda o custo e o tempo de reação.

**Resolvida:** o vídeo não fixa a ordem entre retry e breaker, e não há uma ordem universalmente correta: [[wiki/questions/ordem-retry-circuit-breaker]].

## Citação

> "Nosso código vai ficar uma porcaria se a gente fizer isso" (sobre controlar transições com `if`s)

## Conceitos e entidades

**Conceitos:** [[wiki/concepts/design-patterns]], [[wiki/concepts/strategy-pattern]], [[wiki/concepts/observer-pattern]], [[wiki/concepts/adapter-pattern]], [[wiki/concepts/strategy-com-adapter]], [[wiki/concepts/finite-state-machine]], [[wiki/concepts/mapa-de-transicoes]], [[wiki/concepts/state-pattern]], [[wiki/concepts/retry-backoff]], [[wiki/concepts/circuit-breaker]], [[wiki/concepts/thundering-herd]], [[wiki/concepts/event-driven-architecture]], [[wiki/concepts/dependency-injection]], [[wiki/concepts/efeito-colateral]], [[wiki/concepts/grafo-como-abstracao-de-agentes]], [[wiki/concepts/bullmq]], [[wiki/concepts/idempotencia]].

**Entidades:** [[wiki/entities/stripe]]. Citados sem página própria: PayPal, AbacatePay, n8n, Visa.
