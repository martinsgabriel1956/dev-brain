---
type: concept
title: "Testar o Próprio Código"
aliases: ["self testing", "testes automatizados", "testar antes de entregar", "happy path só"]
date_created: 2026-04-22
date_updated: 2026-04-26
source_count: 3
tags: [testes, hábitos, qualidade, craftsmanship, carreira]
skill: tech-mentor-leadership
status: stable
---

# Testar o Próprio Código

Responsabilidade do dev de **validar seu código além do caminho feliz** — incluindo casos de erro, edge cases e comportamentos inesperados — antes de considerar a entrega pronta.

## O problema do happy path exclusivo

Testar só o caminho feliz é equivalente a concordar com a própria opinião: você está procurando confirmação, não evidência contrária. Bugs vivem nos caminhos que ninguém testou.

```
Happy path: o usuário faz exatamente o que você espera
Realidade: o usuário vai tentar tudo que você não esperou
```

## O que testar além do happy path

- **Inputs inválidos**: campo vazio, tipo errado, valor fora do range
- **Estados de erro**: API fora, timeout, permissão negada
- **Edge cases**: lista vazia, um único item, limite máximo
- **Comportamento esperado de falha**: mensagem de erro correta, sem crash, sem dado corrompido

## Testes automatizados vs. manual

Testar manualmente uma vez não é suficiente — a regressão vai aparecer em outra entrega. Testes automatizados garantem que o comportamento correto **persiste ao longo do tempo**.

```typescript
// ✅ Testa happy path E erro
describe("createUser", () => {
  it("should create user with valid data", async () => { ... });
  it("should throw UserAlreadyExistsError when email is taken", async () => { ... });
  it("should throw ValidationError when email is invalid", async () => { ... });
});
```

## Ser enganado pelo próprio teste

O nível seguinte: escrever um teste que passa mas não valida o que você pensa que valida. Acontece quando o teste não é específico o suficiente ou quando o mock não representa o comportamento real.

## Relação com definição de pronto

Código sem testes de erro não está pronto — ver [[definicao-de-pronto]].

## Usuários como agentes do caos

Usuários não seguem o fluxo esperado. Eles digitam emoji em campos de nome, submetem formulários 50x porque a resposta demorou 0.2s, colam SQL injection em campos de texto, e usam browsers que você nunca testou. Cada suposição sobre comportamento do usuário é um test case que falta.

> "O impossível se torna possível no segundo em que alguém começa a digitar." — [[sources/5-principios-programador]]

## Key Sources

- [[wiki/sources/habitos-ruins-de-programador]]
- [[sources/5-principios-programador]]
- [[wiki/sources/4-habitos-programador-ineficiente]]
