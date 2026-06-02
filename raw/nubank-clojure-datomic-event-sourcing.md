# Por que o Maior Banco Digital da América Latina Escolheu Clojure e Datomic

> Transcrição e comentários do vídeo: *"Why Nubank, the largest digital bank, chose Clojure and Datomic"*
> Canal: Nova Devs (Vinícius Pasco Antônio)
> Data de visualização: ~2026

---

## Contexto

O Nubank é o maior banco digital da América Latina, com **100 milhões de clientes**, oferecendo pagamento, crédito e conta — um sistema financeiro de verdade, com escala gigantesca.

O vídeo original mostra os engenheiros que construíram o Nubank contando como tomaram as decisões técnicas fundamentais da empresa.

---

## Clojure como linguagem principal

O Nubank usa **Clojure** como linguagem principal — inclusive para scripts, infraestrutura com Kafka, e o próprio framework interno.

> *"Nubank uses Clojure as their main language. We also use it for scripts like using Kafka and stuff. We use it for infrastructure as well."*

O Nubank aparentemente não usa um framework externo padrão — eles construíram o próprio framework internamente, o que lhes dá controle total sobre:

- Gerenciamento de threads
- Garbage collector
- Alocação de memória

---

## O Paper que Influenciou Tudo

O CTO do Nubank citou um paper sobre **grandes sistemas** que destacava:

> *"Mutable state and effects are the source of most of the accidental complexity in large systems."*

Ou seja: **mutabilidade e efeitos colaterais são a fonte de quase toda a complexidade acidental em sistemas grandes.**

### Por que isso importa

**Mutabilidade** causa bugs que:
- São extremamente difíceis de reproduzir
- Exigem o alinhamento de múltiplas condições para aparecer
- Geralmente explodem em runtime (o pior momento)
- São quase impossíveis de testar de forma determinística

**Efeitos colaterais inesperados** são funções que fazem mais do que prometem. Exemplo clássico:

```
calcularPreco(item)
  → calcula o preço ✓
  → envia e-mail ✗ (inesperado)
  → atualiza banco de dados ✗ (inesperado)
```

---

## Programação Funcional como Solução

A programação funcional resolve esses dois problemas estruturalmente:

- **Imutabilidade por padrão** — variáveis não mudam após criadas
- **Efeitos colaterais explícitos** — o código obriga você a declarar onde efeitos acontecem

> "Jogar futebol é simples. Jogar futebol de forma simples é muito difícil. Escrever código é simples. Escrever código simples é muito difícil."

Em Kotlin, contextos (`run {}`) delimitam visualmente onde efeitos colaterais ocorrem. Em Clojure e Scala isso é ainda mais estrutural.

O padrão arquitetural recomendado é:
- **Domínio puro no centro** (sem efeitos colaterais)
- **Efeitos colaterais nas periferias** (adaptadores, I/O, banco de dados)

Essa ideia se conecta diretamente com **DDD (Domain-Driven Design)** e arquitetura hexagonal/ports & adapters.

---

## Datomic: O Banco de Dados Imutável

O CTO do Nubank chegou ao Datomic ao se perguntar: *"E o banco de dados? O estado precisa evoluir. Como ter um banco imutável?"*

> *"What that means is not that things don't change — it's that you don't lose the history of the prior states as they change over time."*

Para um banco com requisitos de auditoria e regulatórios, isso é um superpoder:
- Snapshots imutáveis de estados anteriores
- Viagem no tempo (ver o estado como era em qualquer ponto)
- Algo que nenhum banco construído em tecnologia legada consegue oferecer

---

## Event Sourcing

O que o Datomic representa na prática é **Event Sourcing**:

Em vez de salvar o estado atual (ex: saldo = R$ 1.000), você salva **todos os eventos que levaram a esse estado**.

```
[débito R$50 PIX] → [débito R$100 cassino] → [crédito R$1.150 salário]
= saldo atual: R$1.000
```

### Analogia do extrato bancário

Quando você abre seu app bancário, você não vê apenas o saldo — você vê cada transação. O banco **reaplica todos os eventos** para calcular o estado atual. Isso é Event Sourcing.

### Propriedades dos eventos

- São sempre **no passado** (fatos que já aconteceram)
- São **imutáveis** (você não muda o passado)
- Acumulam-se em um **log append-only**

### Vantagens

- **Real-time state** — estado construído a partir de fatos
- **Informação histórica completa** — audit trail nativo
- **Bugs 100% reproduzíveis** — basta salvar os eventos e dar play
- **Testes determinísticos** — replay exato de qualquer cenário
- **Debuggability** — você sabe exatamente o que aconteceu

### Desvantagens / Desafios

- **Transaction hell** (em modelos mutáveis, não no funcional)
- **Event logs crescem muito** — necessidade de snapshots e checkpoints
- **Curva de aprendizado gigante**
- **Complexidade arquitetural alta** — pouco comum no mercado

> Sistemas que geralmente usam essa arquitetura: bancos, apostas esportivas em tempo real, qualquer sistema que precisa de auditoria total.

---

## CQRS (Command Query Responsibility Segregation)

Mencionado como complemento ao Event Sourcing:

- **Command side** — processa eventos e persiste no log
- **Query side** — lê o estado atual a partir do log de eventos

O estado em memória (ex: saldo calculado) nunca vai direto ao banco — o banco só armazena eventos. O estado é derivado sob demanda.

---

## Por que Clojure sobre Java/Ruby

> *"My previous experiences were on Java and Ruby, in which codebases age like milk pretty quickly."*

Quanto mais tempo passa e mais você mexe em um codebase Java/Ruby tradicional, mais ele vira um **legado intocável** — depende do "Vlad que conhece o sistema há 20 anos".

Com programação funcional + DDD + Event Sourcing, o codebase **envelhece como vinho**.

Clojure sobre a JVM deu ao Nubank:
- Todo o **ecossistema Java** (bibliotecas maduras)
- Sem precisar reinventar a roda para primitivos básicos
- Foco no que importa: **resolver problemas de negócio**, não construir frameworks

---

## Conexão com o Momento Atual (IA e Código)

> "Código está barato. Código ruim é extremamente caro."

Com IA gerando código, o diferencial do engenheiro é:
- Saber **traduzir regras de negócio** em código
- Entender **arquitetura e trade-offs**
- Não reinventar a roda, entregar valor

---

## Leituras e Referências

- Paper citado: *"Out of the Tar Pit"* — Ben Moseley e Peter Marks (sobre complexidade acidental em sistemas grandes)
- Datomic: banco de dados imutável criado por Rich Hickey (criador do Clojure)
- Série no canal Nova Devs: Programação Funcional + DDD + Event Sourcing

---

## Tags

`nubank` `clojure` `datomic` `event-sourcing` `functional-programming` `DDD` `CQRS` `imutabilidade` `efeitos-colaterais` `arquitetura` `banco-digital` `scala` `JVM`
