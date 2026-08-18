---
type: concept
title: "Facade Pattern"
aliases: ["padrão facade", "design pattern facade", "fachada"]
date_created: 2026-05-01
date_updated: 2026-08-18
source_count: 4
tags: [design-patterns, structural, facade, oop, encapsulamento]
skill: tech-mentor-backend
status: stable
---

# Facade Pattern

Padrão [[structural-patterns|estrutural]] que fornece uma **interface simplificada** para um conjunto de interfaces em um subsistema complexo. O cliente fala com a Facade; ela coordena os componentes internos.

## Como funciona

```typescript
class OrderFacade {
  private paymentProcessor = new PaymentProcessor();
  private inventorySystem = new InventorySystem();
  private fraudChecker = new FraudChecker();
  private shippingCalculator = new ShippingCalculator();

  placeOrder(order: Order) {
    if (!this.fraudChecker.check(order)) return;
    if (!this.inventorySystem.hasStock(order)) return;
    if (!this.paymentProcessor.charge(order)) return;
    this.shippingCalculator.calculate(order);
  }
}

// Uso: complexidade zero para o consumidor
const facade = new OrderFacade();
facade.placeOrder(order);
```

## Quando usar

- Subsistemas complexos com muitos passos de orquestração
- Para reduzir acoplamento entre camadas
- Para criar uma API de alto nível sobre libs ou módulos de baixo nível

## Trade-offs

| ✅ | ❌ |
|---|---|
| Simplicidade para o consumidor | Pode virar [[god-object]] se fizer demais |
| Reduz acoplamento | Pode esconder complexidade que deveria ser visível |
| Ponto único de mudança para a orquestração | |

## Facade e o "S" do SOLID

Crítica comum: uma Facade que orquestra pagamento, notificação e estoque parece ferir a responsabilidade única. Contra-argumento (via [[wiki/sources/design-pattern-facade-renato-augusto]]): SRP é sobre ter **um único motivo para mudar**, não sobre "uma linha de código, uma ação". A razão de mudança da Facade é *o processo que ela orquestra* mudar (ex: adicionar um passo novo) — as classes internas que ela chama continuam com SRP estrito cada uma. O sintoma de que isso descamba para [[god-object]] é a Facade acumular responsabilidades **não relacionadas** ao fluxo que ela representa, não o fato de chamar várias classes.

### Sinal prático para extrair uma Facade

Quando o mesmo fluxo de orquestração (ex: processar um pedido) precisa ser repetido em mais de um Controller/rota, deixar a lógica solta em cada Controller cria risco de divergência — uma mudança de regra aplicada em um lugar e esquecida no outro. Esse é o gatilho concreto para migrar o fluxo para dentro de uma Facade: um único ponto de mudança.

## O Facade não bloqueia acesso direto ao subsistema

Via [[wiki/sources/design-pattern-facade-codigo-fonte-tv]]: diferente de encapsulamento que restringe acesso, a Facade **não impede** o código cliente de chamar os serviços do subsistema diretamente — ela só oferece um caminho mais simples. Isso é relevante quando um caso de uso específico precisa de controle fino que a Facade não expõe.

## Motivação de compliance: exclusão de dados sob LGPD

A mesma fonte usa como motivação um cenário de remoção de conta de cliente (avatar, documentos, histórico de acesso) sob a lei de proteção de dados: exclusão a pedido do titular não é um loop trivial de `remove()` em cada serviço, porque pode haver regra de negócio no meio (ex.: histórico de acesso com retenção legal obrigatória, que não deve ser removido junto com o resto). É um segundo caso motivacional ao lado do e-commerce de [[wiki/sources/design-pattern-facade-renato-augusto]] — ambos mostram que a orquestração escondida atrás de uma Facade tipicamente carrega ordem/exceções reais, não é "só chamar vários métodos".

## Variação: método estático em vez de instância

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] mostra a Facade tanto como classe instanciável (`new ClientFacade(cliente).removeConta()`) quanto como método estático que recebe o objeto a operar (`ClientFacade.removeConta(cliente)`) — a segunda forma evita reinstanciar a Facade a cada chamada, mas não resolve a tensão de acoplamento abaixo.

## Tensão entre acoplamento e Dependency Injection

Instanciar os serviços do subsistema direto no construtor da Facade (com `new`) acopla a Facade fortemente a implementações concretas — mas fazer [[wiki/concepts/dependency-injection|injeção de dependência]] completa devolve a complexidade para o código cliente, que passaria a precisar montar e passar todos os serviços na hora de usar a Facade, anulando parte do ganho de simplicidade. Nenhuma das duas fontes de vídeo (Renato Augusto, Código Fonte TV) resolve essa tensão — ambas expõem o trade-off e seguem com `new` direto no construtor por simplicidade didática.

## Debate aberto: Facade fere SRP?

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] discorda explicitamente da posição de [[wiki/sources/design-pattern-facade-renato-augusto]] descrita abaixo — ver a comparação completa em [[wiki/questions/facade-fere-srp-video-comparison]].

## Diferença do Proxy

O Facade simplifica acesso a **múltiplos** componentes. O [[proxy-pattern]] substitui **um único** objeto e controla o acesso a ele.

## Façades implícitas no dia a dia

- `fetch()` — esconde TCP, retry, header parsing
- `ArrayList` Java — esconde resize de array
- Qualquer ORM — esconde SQL gerado

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-facade]]
- [[wiki/sources/design-pattern-facade-renato-augusto]]
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]]
