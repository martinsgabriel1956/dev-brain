---
type: question
title: "Retry fica dentro ou fora do circuit breaker?"
aliases: ["ordem retry circuit breaker", "retry dentro do breaker"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_count: 2
tags: [resiliencia, retry, circuit-breaker, contradicao, resolvida]
skill: tech-mentor-backend
status: stable
---

# Retry fica dentro ou fora do circuit breaker?

## Resposta

**Não há uma ordem universalmente correta: é uma escolha de composição, e cada uma muda o que o breaker mede.** A regra da wiki, de que retry por fora é "errado", não se sustenta como regra geral. Retry por fora é a ordem padrão documentada do Resilience4j e o cenário usado na documentação do Polly.

**Confiança:** alta de que retry por fora não é um erro em si. Nenhuma página lida declara uma ordem obrigatória, nem dá razões para preferir uma à outra, então a tabela abaixo é raciocínio, não evidência.

## Evidência

| Fonte | O que diz | Tipo |
|---|---|---|
| [Resilience4j, seção "Aspect order"](https://resilience4j.readme.io/docs/getting-started-3) `[external]` | Ordem padrão `Retry ( CircuitBreaker ( RateLimiter ( TimeLimiter ( Bulkhead ( Function ) ) ) ) )`, com o retry por fora. Pode ser alterada por propriedades ou encadeamento funcional. Não explica o porquê | Documentação oficial |
| [Polly, Circuit Breaker](https://www.pollydocs.org/strategies/circuit-breaker.html) `[external]` | O breaker monitora falhas e não gerencia retries. O exemplo tem breaker por dentro e retry por fora, e o retry trata `BrokenCircuitException`. Ele critica o modo de calcular a espera, não a composição | Documentação oficial |
| [Polly, Pipelines](https://www.pollydocs.org/pipelines/) `[external]` | A ordem das estratégias muda o comportamento (exemplo com timeout e retry). Não cita circuit breaker | Documentação oficial |
| [Azure, Retry pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/retry) `[external]` | Depois de muitas tentativas, é melhor parar de chamar o recurso, e remete ao Circuit Breaker. Não fixa ordem | Documentação oficial |
| [[wiki/sources/circuit-breaker]] (`raw/circuit-breaker.md`) | Retry dentro é o correto, porque cada retry por fora contaria como nova falha e abriria o circuito cedo. Autor não identificado, sem evidência | Artigo |
| [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]] | Diz só que o breaker indica quando quebrar o loop de retry. Não fixa ordem | Vídeo |

## O que muda na prática (raciocínio, não fonte)

| | Retry dentro do breaker | Retry fora do breaker |
|---|---|---|
| O breaker conta | Uma falha por operação, só depois de esgotar as tentativas | Uma falha por tentativa |
| O que o breaker enxerga | Falhas que o retry não absorveu; transientes ficam escondidos | A taxa de erro real do downstream |
| Com o circuito aberto | A operação inteira falha rápido | O retry recebe a rejeição e precisa tratá-la: não retentar, ou esperar a duração da abertura, como no exemplo do Polly |
| Risco principal | Reage mais tarde, e o timeout do breaker precisa cobrir todas as tentativas e esperas | Gastar as tentativas em rejeições instantâneas, se elas não forem tratadas |

O argumento de "abrir prematuramente" pesa num breaker por contagem de falhas consecutivas. Num breaker por taxa, como o exemplo com Opossum em [[wiki/concepts/circuit-breaker]], as tentativas extras tendem a manter a taxa parecida, então o efeito é menor.

## Limites

- A [página de Circuit Breaker da Azure](https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker) foi recusada pela ferramenta de leitura.
- *Release It!* e a documentação do Opossum não foram lidos.
- Resilience4j e Polly não representam todo o ecossistema, e um padrão de biblioteca não prova que a ordem seja a melhor.

## Key Sources

- [[wiki/concepts/circuit-breaker]]
- [[wiki/concepts/retry-backoff]]
- [[wiki/sources/circuit-breaker]]
- [[wiki/sources/cinco-design-patterns-strategy-observer-adapter-state-machine-retry-circuit-breaker]]
