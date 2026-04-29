---
date: 2026-04-17
tags: [tech-mentor, arquitetura, estilos-arquiteturais, async, resiliencia]
skill: tech-mentor-system-design/references/architecture-styles
level: intermediário
---

# Reactive Architecture

## Contexto
O **Reactive Manifesto** (2014) define quatro propriedades que um sistema deve ter para ser considerado reativo: **Responsive, Resilient, Elastic, Message-Driven**. Não é um framework — é um conjunto de princípios que guiam decisões de design para sistemas que precisam responder a carga variável sem degradar.

Relevante entender porque muitos sistemas "assíncronos" ou "orientados a eventos" se identificam como reativos, mas a propriedade que diferencia de fato é o **backpressure**.

## O Reactive Manifesto

```
        ┌─────────────────────────┐
        │       RESPONSIVE        │ ← responde em tempo previsível
        │  (foundation of UX)     │
        └──────────┬──────────────┘
          ┌────────┴────────┐
          ▼                 ▼
   ┌────────────┐   ┌─────────────┐
   │ RESILIENT  │   │   ELASTIC   │
   │ falha sem  │   │ escala sob  │
   │ colapso    │   │ carga       │
   └─────┬──────┘   └──────┬──────┘
         └────────┬─────────┘
                  ▼
        ┌──────────────────┐
        │  MESSAGE-DRIVEN  │  ← o meio que viabiliza os outros três
        └──────────────────┘
```

**Message-Driven** é o alicerce: componentes comunicam via mensagens assíncronas, o que naturalmente desacopla produtor de consumidor, permite buffering e habilita backpressure.

## Backpressure

O conceito mais importante e mais mal entendido. Quando um consumidor não consegue processar mensagens na velocidade que o produtor envia, ele **sinaliza de volta** ao produtor para reduzir a taxa — em vez de simplesmente cair ou descartar mensagens silenciosamente.

```typescript
// Exemplo com Node.js Streams — backpressure nativo
import { createReadStream, createWriteStream } from "fs";

const readStream = createReadStream("large-file.csv");
const writeStream = createWriteStream("output.csv");

// pipe() gerencia backpressure automaticamente:
// se writeStream não drena, readStream pausa
readStream.pipe(writeStream);

// Sem pipe — errado, sem backpressure:
readStream.on("data", chunk => {
  // writeStream.write retorna false se o buffer encheu
  // mas aqui ignoramos esse sinal → memória explode
  writeStream.write(chunk);
});
```

```typescript
// Exemplo com RxJS — operadores de backpressure
import { interval } from "rxjs";
import { bufferTime, concatMap, delay } from "rxjs/operators";

// Produtor rápido: emite a cada 10ms
const fast$ = interval(10);

// Consumidor lento: processa a cada 100ms
fast$.pipe(
  bufferTime(100),          // coleta 10 eventos em 100ms
  concatMap(batch =>        // processa um batch de cada vez, em sequência
    processSlowly(batch).pipe(delay(50))
  )
).subscribe();
```

## Elastic vs. Scalable

| Propriedade | Definição |
|---|---|
| **Scalable** | aguenta mais carga com mais recursos |
| **Elastic** | escala **automaticamente** conforme a carga varia, sem intervenção humana |

Elastic pressupõe que o sistema detecta pressão (CPU, queue depth, latência) e provisiona/desprovisionamento automaticamente. KEDA e HPA do Kubernetes implementam elasticidade.

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Throughput | Não bloqueia threads enquanto espera I/O | Debugging de código assíncrono é mais complexo |
| Resiliência | Bulkheads e isolamento natural entre componentes | Stack traces não revelam o fluxo real |
| Elasticidade | Menos recursos em períodos de baixa carga | Requer infraestrutura de auto-scaling configurada |
| Backpressure | Evita falhas em cascata | Implementação correta exige atenção — fácil de ignorar o sinal |

## Quando Usar / Quando Evitar

**Usar quando:**
- Carga é variável e imprevisível (picos vs. vales claros)
- Latência de resposta é SLA crítico (p99 < 200ms sob carga)
- Integrações externas têm latência alta (APIs de terceiros, DB remoto)

**Evitar quando:**
- O sistema é batch ou offline — responsividade não é critério
- O time não domina async/await corretamente — erros sutis de backpressure quebram em produção
- CRUD simples com carga previsível — a complexidade não se paga

## Conceitos Relacionados
[[event-driven-architecture]] · [[graceful-degradation]] · [[circuit-breaker]] · [[kafka]] · [[bulkhead]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
