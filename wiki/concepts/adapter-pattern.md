---
type: concept
title: "Adapter Pattern"
aliases: ["padrão adapter", "design pattern adapter", "adaptador"]
date_created: 2026-05-01
date_updated: 2026-07-24
source_count: 5
tags: [design-patterns, structural, adapter, oop, integracao]
skill: tech-mentor-backend
status: stable
---

# Adapter Pattern

Padrão [[structural-patterns|estrutural]] que **converte a interface de uma classe em outra interface** esperada pelo cliente. Permite que classes com interfaces incompatíveis trabalhem juntas sem modificar nenhuma das duas.

## Como funciona

```typescript
// API de terceiro retorna Celsius/km — app espera Fahrenheit/mph
interface WeatherApp {
  getTempF(): number;
  getSpeedMph(): number;
}

class WeatherAdapter implements WeatherApp {
  constructor(private weatherApi: ThirdPartyWeatherApi) {}

  getTempF() {
    return (this.weatherApi.getTempC() * 9/5) + 32;
  }

  getSpeedMph() {
    return this.weatherApi.getSpeedKmh() * 0.621371;
  }
}

const weather = new WeatherAdapter(new ThirdPartyWeatherApi());
console.log(weather.getTempF()); // conversão isolada no adapter
```

## Quando usar

- Integração com APIs ou libs de terceiros com interface incompatível
- Quando não pode modificar a lib externa
- Clean Architecture: adaptar serviços externos à interface do domínio

## Trade-offs

| ✅ | ❌ |
|---|---|
| Lógica de conversão isolada em um lugar | Tedioso para APIs muito grandes |
| Não modifica nenhum dos dois lados | Mais uma camada de indireção |
| Testável isoladamente | |

## Diferença do Proxy

O Adapter **muda a interface**. O [[proxy-pattern]] **mantém a mesma interface** — apenas intercepta e adiciona comportamento (cache, log, auth).

## Diferença do Mapper

O Adapter adapta **comportamento** — expõe métodos de uma interface incompatível através da interface esperada. O [[wiki/concepts/mapper-pattern]] converte a **forma dos dados** — pega uma entidade de domínio e devolve um objeto plano no shape que outra camada espera (ex: `PrismaNotificationMapper.toPrisma()`), sem interceptar chamadas de método nem satisfazer um contrato de interface.

## Exemplo: troca de biblioteca sem tocar na regra de negócio

Caso didático (geração de relatório em PDF): uma classe de negócio (`SalesReportGenerator`) que dá `new` direto numa lib externa (DomPDF) e chama seus métodos específicos (`loadHtml`, `setPaper`, `render`) está violando [[single-responsibility]] — muda por dois motivos (regra de negócio *e* API da lib) — e fica impossível de testar unitariamente sem gerar o PDF de verdade. Extraindo uma interface própria do domínio (`PdfAdapter.generate(fileName, content)`) e um adaptador concreto (`DomPdfAdapter`) injetado via construtor, a troca por outra lib com API totalmente diferente (TCPDF: `writeHTML`, `setFont`) exige só um novo adaptador (`TcpdfAdapter implements PdfAdapter`) — zero alteração na classe de negócio. Regra prática: sempre que uma classe de alto nível instancia diretamente uma classe concreta de baixo nível/externa, é sinal para aplicar o Adapter.

## Inversão de Dependência nas Fronteiras da Clean Architecture

As interfaces `Input Boundary`, `Output Boundary` e `Data Access` descritas em [[wiki/concepts/clean-architecture]] são o mesmo mecanismo estrutural do Adapter — uma interface própria do domínio que isola o código de alto nível de uma dependência concreta — aplicado nas fronteiras entre Controller/Use Case, Use Case/Presenter e Use Case/persistência. Ver [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]], que chama essas interfaces de "protocolo".

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-facade]] — distinção Facade vs Adapter formalizada
- [[wiki/sources/mappers-conversao-entre-camadas]] — distinção Adapter vs Mapper
- [[wiki/sources/design-pattern-adapter]] — caso DomPDF/TCPDF: extração de interface + adaptador concreto elimina acoplamento a lib externa e viabiliza testabilidade
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — Input/Output Boundary e Data Access interface como aplicação do mesmo princípio nas fronteiras da Clean Architecture
