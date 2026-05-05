# Observer — Padrão de Projeto Comportamental

**Fonte:** https://refactoring.guru/pt-br/design-patterns/observer
**Também conhecido como:** Observador, Assinante do evento, Event-Subscriber, Escutador, Listener
**Categoria:** Padrão Comportamental
**Data de adição:** 2026-05-05

---

## Propósito

O **Observer** é um padrão de projeto comportamental que permite que você defina um **mecanismo de assinatura** para notificar múltiplos objetos sobre quaisquer eventos que aconteçam com o objeto que eles estão observando.

---

## Problema

Dois objetos: um `Cliente` e uma `Loja`. O cliente quer saber quando um produto (novo iPhone) estará disponível.

**Opção 1 — Polling:** o cliente visita a loja todos os dias para checar. A maioria das visitas é em vão — desperdício de tempo.

**Opção 2 — Broadcast:** a loja manda e-mail para *todos* os clientes sempre que qualquer produto chega. Resolve para quem quer, irrita quem não está interessado — spam.

**O conflito:** ou o consumidor desperdiça esforço verificando, ou o produtor desperdiça recursos notificando quem não importa. Nenhuma solução escala bem.

---

## Solução

O objeto que tem o estado interessante é chamado de **publicadora**. Os que querem saber das mudanças são **assinantes**.

O padrão Observer sugere adicionar um **mecanismo de assinatura** à classe publicadora:

1. Um vetor (lista) para armazenar referências aos objetos assinantes
2. Métodos públicos para adicionar e remover assinantes da lista

Quando um evento importante ocorre, a publicadora percorre a lista e chama o método de notificação em cada assinante.

**Ponto-chave:** a publicadora trabalha com todos os assinantes **através de uma interface comum** — não sabe nada sobre as classes concretas. Novos assinantes podem ser adicionados sem nenhuma mudança nas classes publicadoras existentes.

---

## Analogia com o Mundo Real

Uma assinatura de jornal ou revista:

- Você **assina** uma publicação → entra na lista de entrega
- Cada edição nova → publicadora percorre a lista e envia para cada assinante
- Você **cancela** → sai da lista, para de receber

Os assinantes recebem exatamente o que querem, quando acontece — sem polling, sem spam para quem não quer.

---

## Estrutura

```
                 ┌─────────────────────────┐
                 │       Publicadora       │
                 │  - listeners: List      │
                 │  + subscribe(l)         │
                 │  + unsubscribe(l)       │
                 │  + notifyListeners()    │
                 └─────────────────────────┘
                            │ notifica
                            ▼
                    <<interface>>
                      Assinante
                    + atualizar(ctx)
                            ▲
               ┌────────────┴────────────┐
        AssinanteConcreto A      AssinanteConcreto B
```

**Participantes:**

1. **Publicadora** — emite eventos quando muda de estado. Contém a infraestrutura de inscrição (lista de assinantes + métodos subscribe/unsubscribe). Quando evento ocorre, percorre a lista e notifica cada assinante.

2. **Interface do Assinante** — declara o método de notificação, normalmente `atualizar(dados)`. Permite que a publicadora não fique acoplada a classes concretas.

3. **Assinantes Concretos** — implementam ações em resposta às notificações. A publicadora passa dados de contexto como argumentos do método de notificação (ou passa ela mesma como argumento para o assinante buscar o que precisar).

4. **Cliente** — cria publicadoras e assinantes separadamente e então registra assinantes para atualizações de publicadoras.

> A lista de assinantes é **dinâmica**: assinantes podem entrar e sair durante a execução.

---

## Pseudocódigo

Exemplo: editor de texto notifica objetos de serviço sobre mudanças em seu estado. O editor **delega** o gerenciamento de assinaturas para um `EventManager` separado — isso permite que o EventManager seja reutilizado como enviador de eventos centralizado.

```
// Publicadora base — gerenciamento de inscrições e notificações
class EventManager is
    private field listeners: hash map of event types and listeners

    method subscribe(eventType, listener) is
        listeners.add(eventType, listener)

    method unsubscribe(eventType, listener) is
        listeners.remove(eventType, listener)

    method notify(eventType, data) is
        foreach (listener in listeners.of(eventType)) do
            listener.update(data)

// Publicadora concreta — lógica de negócio real
// Delega gerenciamento de assinaturas para o EventManager
class Editor is
    public field events: EventManager
    private field file: File

    constructor Editor() is
        this.events = new EventManager()

    method openFile(path) is
        this.file = new File(path)
        events.notify("open", file.name)

    method saveFile() is
        file.write()
        events.notify("save", file.name)

// Interface do assinante
interface EventListener is
    method update(filename)

// Assinantes concretos — cada um reage de forma diferente ao mesmo evento
class LoggingListener implements EventListener is
    private field log: File
    private field message

    constructor(log_filename, message) is
        this.log = new File(log_filename)
        this.message = message

    method update(filename) is
        log.write(replace('%s', filename, message))

class EmailAlertsListener implements EventListener is
    private field email: string
    private field message

    constructor(email, message) is
        this.email = email
        this.message = message

    method update(filename) is
        system.email(email, replace('%s', filename, message))

// Uso — cliente monta a estrutura
editor = new Editor()

logger = new LoggingListener(
    "/path/to/log.txt",
    "Alguém abriu o arquivo: %s")
editor.events.subscribe("open", logger)

emailAlerts = new EmailAlertsListener(
    "admin@example.com",
    "Alguém mudou o arquivo: %s")
editor.events.subscribe("save", emailAlerts)
// logger e emailAlerts ficam desacoplados entre si e do editor
```

---

## Como Implementar

1. **Quebre a lógica de negócio em duas partes:** a funcionalidade principal (independente de outros códigos) será a publicadora; o resto vira assinantes.

2. **Declare a interface do assinante** com no mínimo um método `atualizar`.

3. **Declare a interface da publicadora** com métodos para adicionar e remover assinantes. Publicadoras devem trabalhar com assinantes **apenas pela interface**.

4. **Decida onde colocar a lista de assinantes.** Geralmente em uma classe abstrata base da publicadora, ou em um objeto separado (como o `EventManager` do exemplo) para reutilização via composição.

5. **Crie publicadoras concretas.** A cada evento importante, notifique os assinantes.

6. **Implemente `atualizar` nas classes assinantes concretas.** A maioria precisará de dados contextuais — forneça via argumentos do método ou passe a publicadora como argumento para o assinante buscar o que precisar.

7. **O cliente** cria publicadoras e assinantes, e registra assinantes para as atualizações relevantes.

---

## Aplicabilidade

**Use o Observer quando:**

- Mudanças no estado de um objeto podem precisar mudar outros objetos, e o **conjunto de objetos é desconhecido de antemão ou muda dinamicamente**. Exemplo: botões customizados de UI onde o cliente registra código para executar quando o botão é clicado.

- Alguns objetos devem observar outros, mas **apenas por tempo limitado ou em casos específicos**. A lista de inscrição é dinâmica — assinantes entram e saem quando quiserem.

---

## Prós e Contras

| ✅ Prós | ❌ Contras |
|---|---|
| *Princípio aberto/fechado* — novas classes assinantes sem mudar o código da publicadora | Assinantes são notificados em **ordem aleatória** |
| Relações entre objetos estabelecidas durante a execução | Pode causar event callback hell se abusado |
| Desacoplamento entre publicadora e assinantes | Assinantes não registrados podem causar vazamentos de memória |

---

## Relações com Outros Padrões

**Quatro padrões para conectar remetentes e destinatários:**

| Padrão | Mecanismo |
|---|---|
| Chain of Responsibility | Passa pedido sequencialmente pela corrente até alguém atuar |
| Command | Conexão unidirecional entre remetente e destinatário |
| Mediator | Elimina conexões diretas — todos comunicam via mediador |
| Observer | Destinatários se inscrevem/desinscrevem dinamicamente |

**Observer vs Mediator** — diferença sutil:
- **Mediator:** objetivo é eliminar dependências múltiplas. Componentes dependem de *um* objeto mediador. O mediador conhece e orquestra todos os componentes.
- **Observer:** objetivo é comunicação de uma via dinâmica entre objetos, onde alguns agem como subordinados de outros. Pode usar Observer para implementar o próprio Mediator (assinantes se inscrevem e desinscrevem dinamicamente no mediador).

---

## Diferença de Pub/Sub

Observer e Pub/Sub são frequentemente confundidos:

| | Observer | Pub/Sub |
|---|---|---|
| Comunicação | Direta — assinante conhece a publicadora | Indireta — via broker/channel |
| Acoplamento | Publicadora mantém lista de assinantes | Desacoplamento total via intermediário |
| Exemplos | Eventos DOM, listeners de estado | Kafka, Redis Pub/Sub, SNS |

---

## Referência

- **URL:** https://refactoring.guru/pt-br/design-patterns/observer
- **Site:** Refactoring Guru
- **Série:** Padrões de Projeto — Padrões Comportamentais
