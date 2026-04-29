---
date: 2026-04-17
tags: [tech-mentor, arquitetura, principios, testes, qualidade]
skill: tech-mentor-system-design/references/architecture-principles
level: avançado
---

# Architecture Fitness Functions

## Contexto
Conceito de *Building Evolutionary Architectures* (Ford, Parsons, Kua). Uma **fitness function** é qualquer mecanismo que avalia se uma característica arquitetural está sendo respeitada — de forma automatizada e executada em CI.

Em vez de apenas documentar "não deve haver dependências circulares" em um ADR que ninguém lê, você **escreve um teste** que quebra o build se a regra for violada.

A questão central: como garantir que decisões de arquitetura sobrevivam ao longo do tempo, conforme o código cresce?

## Tipos de Fitness Functions

| Tipo | Descrição | Exemplo |
|---|---|---|
| **Atomic** | Testa uma única característica isolada | Sem dependência cíclica entre módulos |
| **Holistic** | Testa comportamento emergente do sistema | Latência p99 < 200ms sob carga |
| **Triggered** | Executa por evento (commit, deploy) | ArchUnit no CI |
| **Continual** | Executa periodicamente em produção | Chaos engineering semanal |
| **Static** | Resultado binário pass/fail | Cobertura de testes > 80% |
| **Dynamic** | Resultado relativo (threshold) | Latência não piorou em relação à baseline |

## Código de Referência

### ArchUnit (Java/Kotlin) — Dependências entre camadas

```java
// Garante que Controllers não acessem Repositories diretamente
@Test
void controllers_should_not_depend_on_repositories() {
    JavaClasses classes = new ClassFileImporter().importPackages("com.example");

    ArchRule rule = noClasses()
        .that().resideInAPackage("..controllers..")
        .should().dependOnClassesThat()
        .resideInAPackage("..repositories..");

    rule.check(classes);
}

// Garante que Domain não importe nada de Infrastructure
@Test
void domain_should_not_depend_on_infrastructure() {
    JavaClasses classes = new ClassFileImporter().importPackages("com.example");

    ArchRule rule = noClasses()
        .that().resideInAPackage("..domain..")
        .should().dependOnClassesThat()
        .resideInAPackage("..infrastructure..");

    rule.check(classes);
}
```

### Deptrac (PHP/TypeScript) — via YAML

```yaml
# deptrac.yaml
layers:
  - name: Domain
    collectors:
      - type: directory
        value: src/domain/.*

  - name: Application
    collectors:
      - type: directory
        value: src/usecases/.*

  - name: Infrastructure
    collectors:
      - type: directory
        value: src/infrastructure/.*

ruleset:
  Domain:
    - ~Application    # Domain não pode depender de Application
    - ~Infrastructure # Domain não pode depender de Infrastructure
  Application:
    - Domain          # Application pode usar Domain
    - ~Infrastructure # Application não pode usar Infrastructure
  Infrastructure:
    - Application     # Infrastructure pode usar Application
    - Domain          # Infrastructure pode usar Domain
```

### k6 — Fitness function de performance em CI

```javascript
// performance-fitness.js
import http from "k6/http";
import { check } from "k6";

export const options = {
  thresholds: {
    // Fitness function: p99 deve ser < 300ms
    http_req_duration: ["p(99)<300"],
    // Fitness function: taxa de erro < 1%
    http_req_failed: ["rate<0.01"]
  },
  vus: 50,
  duration: "30s"
};

export default function() {
  const res = http.get("https://api.example.com/health");
  check(res, { "status 200": r => r.status === 200 });
}
```

## Onde Executar

```
Commit → Unit Tests → ArchUnit/Deptrac → Build
                              │
                              ▼ (se passar)
Deploy → Integration Tests → Performance k6 → Release
                                    │
                                    ▼ (contínuo)
              Produção → Chaos Engineering → SLO dashboards
```

## Trade-offs

| Aspecto | Vantagem | Desvantagem |
|---|---|---|
| Confiança | Regras arquiteturais verificadas automaticamente | Escrever as regras exige entender a arquitetura profundamente |
| Feedback | Violação detectada no PR, não em code review tardio | False positives podem ser frustrantes |
| Evolução | Mudança de arquitetura exige atualizar os testes | Overhead inicial de setup |
| Documentação | O teste *é* a documentação viva da intenção | Necessita manutenção junto com o código |

## Quando Usar / Quando Evitar

**Usar quando:**
- O projeto tem mais de 2 times contribuindo e as fronteiras de módulo precisam ser protegidas
- Há histórico de "drifts" arquiteturais (domain importando infra, etc.)
- Performance é SLA crítico e regressões precisam ser detectadas antes do deploy

**Evitar quando:**
- Projeto solo ou time pequeno com disciplina forte — overhead não se paga
- A arquitetura ainda está em definição — fitness functions prematuras engessam

## Conceitos Relacionados
[[clean-architecture]] · [[hexagonal-architecture]] · [[tdd]] · [[solid]] · [[adr]]

---
*Fonte: tech-mentor skill · tech-mentor-system-design · 2026-04-17*
