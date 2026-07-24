---
type: concept
title: "Mapper Pattern"
aliases: ["mapper", "data mapper por camada", "toPrisma", "toDomain"]
date_created: 2026-07-10
date_updated: 2026-07-24
source_count: 2
tags: [design-patterns, mapper, clean-architecture, hexagonal, prisma, camadas, acoplamento]
skill: tech-mentor-backend
status: stable
---

# Mapper Pattern

Classe dedicada à conversão de uma entidade de domínio para o formato exigido por uma camada específica (persistência, HTTP, mensageria) — e vice-versa. Existe porque, em arquiteturas por camadas ([[wiki/concepts/hexagonal-architecture]], Clean Architecture), a mesma entidade de negócio é representada de forma diferente em cada camada: classe pura no domínio, formato de tabela no ORM, JSON moldado na resposta HTTP.

## Problema que resolve

Sem mapper, a conversão campo-a-campo entre entidade de domínio e formato externo é feita manualmente em cada método do repositório (ou de qualquer código de borda) — repetição que cresce com o número de métodos e mistura lógica de conversão com lógica de acesso a dados.

## Estrutura típica

```typescript
class PrismaNotificationMapper {
  static toPrisma(notification: Notification) {
    return {
      id: notification.id,
      content: notification.content.value, // desembrulha Value Object
      category: notification.category,
      recipientId: notification.recipientId,
    };
  }
}

// no repositório:
const raw = PrismaNotificationMapper.toPrisma(notification);
await prisma.notification.create({ data: raw });
```

- Método **estático**: não há estado a manter, então não há motivo para instanciar a classe.
- A constante de saída no repositório costuma ser chamada `raw` (nome curto, já que `notification` está ocupado pelo parâmetro de entrada).

## Mapper é acoplado à camada/tecnologia, não ao domínio

O mapper pertence à camada de destino, não à entidade em si. `PrismaNotificationMapper` está atrelado ao Prisma — trocar de ORM provavelmente exige reescrever o mapper (o formato de dados esperado muda), mas a entidade `Notification` no domínio permanece intocada. Esse é o mesmo princípio de isolamento de infraestrutura descrito em [[wiki/concepts/hexagonal-architecture]]: a mudança fica contida no adapter/mapper, não vaza para o domínio.

Cada camada de borda tende a ter seu próprio mapper: `PrismaNotificationMapper` para persistência, um mapper equivalente para a camada HTTP (formatar a resposta da API sem expor a entidade de domínio crua) — ver [[wiki/sources/presenters]] para o caso específico de moldar saída por tipo de interface (REST, GraphQL, CLI), que resolve o mesmo problema de raiz na camada de apresentação.

## Diferença do Adapter Pattern

Ambos convertem entre formatos incompatíveis, mas com propósitos distintos: o [[wiki/concepts/adapter-pattern]] adapta uma **interface de comportamento** (métodos de uma API externa) para a interface que o cliente espera. O Mapper converte a **forma dos dados** (shape de um objeto) entre representações da mesma entidade em camadas diferentes — não expõe comportamento, só transforma estrutura.

## Relação com Value Object

Ao mapear para persistência, campos que são [[wiki/concepts/ddd|Value Objects]] no domínio (ex: `content` como objeto com validação) precisam ser desembrulhados para o tipo primitivo que o banco entende (`content.value`) — o mapper é o lugar natural para essa extração, mantendo o Value Object imutável e sem lógica de serialização própria.

## Por que "Object-Relational Mapper" é um Nome Equivocado

[[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] dá a justificativa teórica para o que esta página já descreve na prática: um banco relacional contém apenas **estruturas de dados** (linhas/campos sem comportamento — ver [[wiki/concepts/objeto-vs-estrutura-de-dados]]), enquanto uma entidade de domínio é um **objeto** (dados + comportamento). Como os dois lados não são equivalentes, o mapper não "mapeia" um para o outro — ele **transfere dados** de um formato para o outro. Uncle Bob (fonte do post original) sugere que o nome correto seria algo como *Relational Datastructure Mapper*, não *Object-Relational Mapper* — reforça por que o mapper "pertence à camada/tecnologia, não ao domínio", como já registrado acima.

## Key Sources

- [[wiki/sources/mappers-conversao-entre-camadas]]
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — justificativa teórica (objeto vs. estrutura de dados) para por que ORM é um nome equivocado
