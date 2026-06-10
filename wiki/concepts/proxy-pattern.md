---
type: concept
title: "Proxy Pattern"
aliases: ["padrão proxy", "design pattern proxy"]
date_created: 2026-05-01
date_updated: 2026-06-05
source_count: 2
tags: [design-patterns, structural, proxy, oop]
skill: tech-mentor-backend
status: stable
---

## Definição

Padrão estrutural que fornece um substituto ou espaço reservado para outro objeto. O proxy controla o acesso ao objeto real e pode executar ações antes ou depois que a requisição chega a ele.

## Estrutura Mínima

```
<<interface>>
SubjectInterface
    + operation()
         ▲
    ┌────┴────┐
RealSubject   Proxy
+ operation() + operation()
              - realSubject: RealSubject
```

O cliente fala apenas com a interface — não sabe se está falando com o proxy ou com o objeto real ([[liskov-substitution-principle]]).

## Casos de Uso

| Tipo | O que faz |
|---|---|
| Cache Proxy | Evita reprocessamento de operações custosas |
| Protection Proxy | Verifica permissões antes de delegar |
| Logging Proxy | Registra chamadas sem poluir a classe original |
| Virtual Proxy (Lazy) | Adia criação de objetos pesados |
| Remote Proxy | Representa objeto em outro processo/rede |

## Por que não colocar direto na classe real?

Modificar a classe original viola [[open-closed-principle]]. O Proxy permite estender o comportamento criando algo novo, sem tocar no que já funciona em produção.

## Diferença de padrões similares

- **[[decorator-pattern]]:** adiciona comportamento em cadeia, motivação de extensão funcional
- **[[facade-pattern]]:** simplifica interface de subsistema complexo
- **[[adapter-pattern]]:** converte interface incompatível

## Exemplo Concreto — Cache Proxy

```typescript
class ReportGeneratorProxy implements IReportGenerator {
  constructor(private real: ReportGenerator, private cache: CacheInterface) {}

  generate(report: Report): any[] {
    return this.cache.get(`report_${report.id}`, () => {
      return this.real.generate(report); // só executa em cache miss
    }, { expiresIn: 3600 });
  }
}

// No Controller — única linha que muda:
const generator = new ReportGeneratorProxy(new ReportGenerator(), cache);
```

O Controller não sabe que está lidando com um Proxy — depende apenas da interface `IReportGenerator`.

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/design-pattern-facade]] — relações com Facade e distinção entre os dois
