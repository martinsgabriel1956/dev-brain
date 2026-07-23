---
type: concept
title: "BFF (Backend for Frontend)"
aliases: ["bff", "backend for frontend", "best friends forever"]
date_created: 2026-07-23
date_updated: 2026-07-23
source_count: 2
tags: [bff, api-gateway, over-fetching, under-fetching, aggregation, frontend]
skill: tech-mentor-backend
status: stable
---

# BFF (Backend for Frontend)

Tipo específico de [[wiki/concepts/api-gateway]]: cada frontend (mobile, admin web, usuário final web) tem seu próprio backend dedicado, em vez de todos consumirem a mesma API genérica.

## Problema que Resolve

Uma API genérica que serve todos os clientes tende a dois problemas simultâneos:

- **Over-fetching** — a API retorna 40 campos, o mobile usa 8.
- **Under-fetching** — montar uma tela de resumo exige 4 chamadas separadas porque nenhum endpoint devolve tudo junto.

Cada BFF resolve os dois ao mesmo tempo: agrega chamadas a serviços internos (fan-out) e devolve exatamente o formato que aquele cliente específico precisa — sem mudar os serviços internos, que permanecem genéricos.

```typescript
// BFF Mobile — agrega e formata para a tela específica
const [perfil, pedidos, saldo] = await Promise.all([
  usuarioService.buscarPerfil(),
  pedidosService.listarRecentes(),
  walletService.getSaldo(),
]);
```

Ver [[wiki/concepts/api-composition]] para o padrão de fan-out/agregação em si.

## Por que um BFF por Tipo de Cliente

- Um app **mobile** precisa de recursos otimizados para banda/latência limitada.
- Um **admin web** precisa de recursos de gestão que não interessam ao mobile.
- Um app de **usuário final web** usa recursos próprios, irrelevantes para os outros dois.

O ganho mais importante: tirar quase 100% da regra de negócio do frontend, que passa a só exibir o que o BFF já entrega pronto. Isso é especialmente valioso quando os serviços internos são legados ou geridos por outro time — há pouca flexibilidade para alterá-los, mas total flexibilidade sobre o BFF e o frontend que o consome.

## Quem Implementa

Frequentemente os próprios desenvolvedores frontend implementam o BFF — são quem melhor entende as necessidades de dados daquele cliente específico.

## Risco: BFF Inchado

Um BFF exagerado ou mal escopado vira mais um projeto para manter, negando o ganho original de simplicidade. **Um bom BFF é aquele que quase se esquece que existe** — mexe-se nele pouco, só quando surge um novo endpoint ou um envelopamento de dado novo, e ele consome pouca infraestrutura.

## Quando é Exagero

Nem todo sistema precisa de múltiplos BFFs — para poucos clientes com necessidades parecidas, um único Gateway genérico com composição pode bastar. Avaliar caso a caso; multiplicar BFFs sem necessidade real infla a arquitetura. Ver [[wiki/concepts/over-engineering]].

## Relação com Gatekeeper Pattern

Um BFF é, ao mesmo tempo, um Gatekeeper especializado por tipo de cliente — herda os mesmos ganhos de segurança de borda (auth, rate limit, redução de attack surface). Ver [[wiki/concepts/gatekeeper-pattern]].

## Key Sources

- [[wiki/sources/api-gateway-bff]]
- [[wiki/sources/api-gateway-padrao-essencial-arquiteturas-distribuidas]]
