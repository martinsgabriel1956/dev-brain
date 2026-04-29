---
type: source
title: "SOLID"
aliases: ["solid", "srp", "ocp", "lsp", "isp", "dip", "single responsibility", "open closed", "dependency inversion"]
date_created: 2026-04-23
date_updated: 2026-04-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/solid.md
source_url: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 0
tags: [solid, srp, ocp, lsp, isp, dip, design-principles, oop, typescript]
skill: tech-mentor-backend
status: stable
---

## TL;DR

SOLID: 5 princípios de design orientado a objetos (Robert C. Martin). S: Single Responsibility — uma classe, um motivo para mudar. O: Open/Closed — aberto para extensão, fechado para modificação. L: Liskov — subclasses substituem a classe pai sem quebrar o comportamento. I: Interface Segregation — interfaces específicas, não gordas. D: Dependency Inversion — dependa de abstrações, não implementações.

## Key Claims

**Claim:** SRP não é "fazer uma coisa" — é "ter um único motivo para mudar", definido pelo ator que solicita a mudança.
**Evidence:** `UserReport` com `calculateSalary()`, `formatAsPDF()` e `sendByEmail()`: muda por RH (regras de salário), por infraestrutura (formato PDF), por ops (configuração de email) — 3 motivos, 3 atores. Separar em `SalaryCalculator`, `ReportFormatter`, `EmailSender`: cada um muda por um único ator. Facilita manutenção e testes.
**Confidence:** alta

**Claim:** DIP (Dependency Inversion) é o mais impactante para testabilidade — depender de interfaces permite injetar mocks.
**Evidence:** `OrderService` instanciando `new StripePaymentGateway()` internamente: impossível testar sem chamar a Stripe de verdade. `OrderService(paymentGateway: PaymentGateway)` com interface: teste injeta `MockPaymentGateway`. Inversão: classe de alto nível (OrderService) não depende de classe de baixo nível (StripeGateway), ambos dependem da abstração (PaymentGateway).
**Confidence:** alta

**Claim:** OCP com polimorfismo elimina if-else chains que crescem a cada nova variante — extensão por composição.
**Evidence:** `PaymentProcessor` com `if method === "credit_card"` cresce para cada novo método de pagamento, exigindo modificação da classe. OCP: `PaymentStrategy` interface + `CreditCardPayment`, `PixPayment`, `BoletoPayment` como implementações. Novo método de pagamento = nova classe, sem tocar no `PaymentProcessor`.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/solid]]
- [[concepts/srp]]
- [[concepts/ocp]]
- [[concepts/lsp]]
- [[concepts/isp]]
- [[concepts/dip]]
- [[concepts/dependency-injection]]

## Open Questions

- SOLID em sistemas funcionais (TypeScript com funções puras) — como os princípios se traduzem sem classes e herança?
- Over-application de SOLID — quando abstrações antecipadas baseadas em OCP criam complexidade desnecessária?
