---
type: concept
title: "Adapter Pattern"
aliases: ["padrão adapter", "design pattern adapter", "adaptador"]
date_created: 2026-05-01
date_updated: 2026-05-05
source_count: 2
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

## Key Sources

- [[wiki/sources/design-pattern-proxy]]
- [[sources/sete-padroes-de-design-de-software]]
- [[sources/design-pattern-facade]] — distinção Facade vs Adapter formalizada
