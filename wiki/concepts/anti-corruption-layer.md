---
type: concept
title: "Anti-Corruption Layer (ACL)"
aliases: ["camada de anticorrupção", "acl pattern", "anti corruption layer"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [ddd, context-map, facade-pattern, adapter-pattern, strangler-fig, sistemas-legados, acoplamento, dependencia-oculta]
skill: tech-mentor-backend
status: draft
---

# Anti-Corruption Layer (ACL)

Padrão de **Context Mapping** do DDD estratégico (Eric Evans): o lado **downstream** (quem depende) cria uma camada de tradução explícita na fronteira com um sistema externo ou legado, para que os conceitos, nomes e formatos desse sistema **nunca vazem** para dentro do próprio modelo de domínio.

```
[Seu Domínio] ──→ [ACL: Translator/Adapter] ──→ [Sistema Legado / ERP / Sistema Novo]
```

## Como funciona

```typescript
// Sem ACL: modelo externo vaza para o seu domínio
class Pedido {
  sap_vbeln: string;      // campo SAP vazando
  sap_matnr: string;      // você está pensando em SAP, não em pedidos
}

// Com ACL: seu modelo permanece limpo
class Pedido {
  id: PedidoId;
  itens: ItemPedido[];
}

class SAPAdapter {
  toPedido(sapOrder: SAPOrder): Pedido {
    return new Pedido({
      id: new PedidoId(sapOrder.VBELN),
      itens: sapOrder.ITEMS.map(this.toItem)
    });
  }
}
```

O `OrderService`/`Pedido` do domínio só conhece uma interface própria (ex. `IERPGateway`); a implementação concreta (`SAPAdapter`/`ERPAdapter`) é quem conhece o vocabulário do sistema externo.

## Mecanismo estrutural vs. motivação

ACL **não é** um padrão GoF por si só — é a motivação de DDD estratégico (proteger o modelo de domínio de um modelo externo problemático) implementada com o mecanismo estrutural de um [[wiki/concepts/facade-pattern|Facade]] ou de um [[wiki/concepts/adapter-pattern|Adapter]]:

- **Adapter** quando o objetivo é traduzir **uma interface** incompatível para a interface esperada pelo domínio (ex. `SAPAdapter.toPedido()`).
- **Facade** quando o ACL precisa **orquestrar múltiplas chamadas** ao sistema legado/externo para produzir um único conceito do domínio.

A fonte que introduziu essa página na wiki trata Facade e Adapter como intercambiáveis para esse fim, sem escolher um — a escolha depende de quantas interações com o sistema externo o ACL precisa esconder.

## Por que existe: dependência forte entre versão nova e versão legada

Sem ACL, o sistema novo (ou o domínio) chama diretamente os componentes do legado — cria-se uma **dependência forte bidirecional**: mudança no sistema de origem quebra a chamada; mudança no sistema provedor (resposta ou assinatura da requisição) quebra o consumidor. O ACL absorve essa instabilidade numa única camada, isolando as duas pontas uma da outra.

## Dependência escondida — um problema mais grave que dependência explícita

Além da dependência direta óbvia, existe a dependência **escondida**: por exemplo, uma URL de chamada vinda de uma configuração em banco de dados, arquivo ou variável de ambiente; ou, em linguagens que suportam reflexão (.NET, Java), *linkage* entre componentes feito em tempo de execução via reflection. Esse tipo de dependência é difícil de diagnosticar porque não aparece como um `import`/chamada estática no código — o ACL mitiga a dependência de *chamada direta*, mas não resolve, por si só, a falta de observabilidade sobre configuração dinâmica.

## Relação com o Context Map de DDD

ACL é um entre vários padrões de relacionamento entre Bounded Contexts:

| Padrão | Descrição | Quando usar |
|---|---|---|
| **Anti-Corruption Layer (ACL)** | Downstream traduz modelo upstream | Proteger domínio de modelo externo problemático (legado, ERP, sistema em migração) |
| **Open Host Service (OHS)** | Upstream expõe protocolo publicado único | Múltiplos consumidores — upstream não se adapta a cada um |
| **Published Language** | Protocolo compartilhado e documentado (JSON Schema, Avro, Protobuf) | Integração entre sistemas heterogêneos |
| **Separate Ways** | Sem integração — cada contexto resolve sozinho | Quando integrar custa mais que aceitar duplicação |

Quando o sistema legado precisa ser consumido por **múltiplos** sistemas (não só um), a resposta costuma deslocar-se de "cada consumidor cria seu próprio ACL" para Open Host Service + Published Language no lado do legado — reduzindo N traduções redundantes a uma só.

## Relação com Strangler Fig

Durante uma migração incremental ([[wiki/concepts/strangler-fig-pattern]]), o ACL é o componente que fica na fronteira entre o sistema novo e o legado ainda ativo, permitindo que a substituição avance gradativamente sem que os dois lados fiquem fortemente acoplados um ao outro enquanto coexistem.

## Trade-off ausente na motivação ingênua

Nem toda integração com um sistema legado justifica um ACL — o custo de manter a camada de tradução pode superar o problema que ela resolve. Nesse caso, **Separate Ways** (aceitar duplicação, não integrar) é uma alternativa de Context Map legítima, não apenas "não fazer nada".

## Key Sources

- [[wiki/sources/anti-corruption-layer-facade-adapter-sistema-legado]] — motivação de alto nível (dependência forte, dependência escondida, múltiplos legados); skill `tech-mentor-backend` (`references/architecture/ddd-advanced.md`) supriu o nome formal do padrão, o exemplo de código e os padrões vizinhos de Context Map (OHS, Published Language, Separate Ways)
