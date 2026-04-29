---
type: concept
title: "Temporal Coupling"
aliases: ["temporal coupling", "acoplamento temporal", "ordem implícita de chamadas"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_count: 1
tags: [temporal-coupling, api-design, acoplamento, ordem-implícita, design-patterns]
skill: tech-mentor-system-design
status: stable
---

## Definição

Temporal coupling ocorre quando duas ou mais partes do sistema precisam ser executadas em uma ordem específica, mas nada no código impõe ou comunica essa ordem.

A dependência é implícita — vive em comentários, README, ou na memória do desenvolvedor original.

## Por que é perigoso

O bug resultante de chamar fora de ordem raramente diz "você chamou na ordem errada". Diz:

- `NullPointerException` (porque o estado ainda não foi inicializado)
- `Connection refused` (porque a conexão ainda não foi aberta)
- `Cannot read property of undefined`

A causa real está a vários frames de stack acima do erro. É um dos bugs mais difíceis de reproduzir e de explicar em code review.

## Exemplos de temporal coupling

```typescript
// ❌ Temporal coupling implícito
class ReportService {
  private db: Database;

  initialize(connectionString: string) {
    this.db = new Database(connectionString);
  }

  generate(reportId: string) {
    // crash se initialize() não foi chamado antes
    return this.db.query(`SELECT * FROM reports WHERE id = $1`, [reportId]);
  }
}

const service = new ReportService();
// alguém esquece de chamar initialize()
service.generate("123"); // NullPointerException — mensagem enganosa
```

```typescript
// ✅ Ordem imposta pelo design — impossível chamar errado
class ReportService {
  private constructor(private db: Database) {}

  static async create(connectionString: string): Promise<ReportService> {
    const db = await Database.connect(connectionString);
    return new ReportService(db);
  }

  generate(reportId: string) {
    return this.db.query(`SELECT * FROM reports WHERE id = $1`, [reportId]);
  }
}

// construtor privado + factory async = db sempre inicializado
const service = await ReportService.create(CONNECTION_STRING);
```

## Padrões para eliminar temporal coupling

**Constructor injection** — dependências obrigatórias passadas no construtor. Objeto não existe sem elas.

**Builder pattern com tipos** — cada step retorna um tipo diferente. Só o tipo correto pode chamar o próximo passo.

**Factory async** — construtor privado + método estático async que garante inicialização antes de retornar a instância.

**Typestate pattern** — estados representados como tipos distintos. Impossível chamar `send()` em um `ClosedConnection`.

## Temporal coupling em microsserviços

Service A depende de Service B estar rodando para inicializar. Kubernetes não garante ordem de startup.

Solução: retry com backoff exponencial no startup + health check que falha enquanto dependência não estiver disponível. Readiness probe do K8s só marca o pod como pronto quando a dependência responde.

## Relação com outros conceitos

- [[concepts/dependency-injection]] — DI elimina temporal coupling ao tornar dependências explícitas no construtor
- [[concepts/hexagonal-architecture]] — ports tornam dependências de infraestrutura declarativas
- [[concepts/accidental-complexity]] — temporal coupling implícito é uma forma de complexidade acidental

## Key Sources

- [[sources/conceitos-que-ninguem-ensina]]
