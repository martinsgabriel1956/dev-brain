---
type: concept
title: "Abstração"
aliases: ["abstraction", "esconder detalhes", "contrato genérico"]
date_created: 2026-04-25
date_updated: 2026-08-13
source_count: 5
tags: [abstracao, software-design, clean-code, arquitetura, interfaces]
skill: tech-mentor-backend
status: stable
---

# Abstração

Abstração é **esconder o que não precisa ser visto**. O consumidor de uma abstração sabe *o que* ela faz, não *como*.

Analogia: você disca um número e aperta ligar. A complexidade de antena, rede e codificação fica oculta. Você só precisa do contrato (número → ligação).

## No código

Abstração é implementada via contratos (tipos, interfaces) que desacoplam o consumidor da implementação concreta.

```typescript
// contrato genérico — consumidor só precisa saber disso
type PedidoRepository = {
  buscarPorId: (id: string) => Promise<Pedido | null>;
};

// implementações concretas — detalhes ocultos
class PedidoRepositoryDB implements PedidoRepository {
  async buscarPorId(id: string) {
    return db.query(`SELECT * FROM pedidos WHERE id = '${id}'`);
  }
}

class PedidoRepositoryAPI implements PedidoRepository {
  async buscarPorId(id: string) {
    return api.get(`/pedidos/${id}`);
  }
}

// consumidor: não sabe se é banco ou API
async function processarPedido(repo: PedidoRepository, pedidoId: string) {
  const pedido = await repo.buscarPorId(pedidoId);
  // ...
}
```

Você pode trocar `PedidoRepositoryDB` por `PedidoRepositoryAPI` **sem tocar em `processarPedido`**.

## Níveis de abstração

- **Baixo nível:** lidar diretamente com banco, HTTP, filesystem
- **Alto nível:** consumir contratos sem saber a implementação

Misturar níveis na mesma função é um code smell — viola [[single-responsibility]] e aumenta [[acoplamento]].

## Analogia dos Órgãos (Maturidade em Pensar Primeiro em Abstrações)

[[wiki/sources/7-habitos-programador-altamente-eficaz]] descreve a progressão de um programador eficaz como parar de pensar só em código e passar a pensar primeiro nas abstrações, no limite de cada uma, e na interface que expõe — deixando a implementação como "detalhe de interior" a ser resolvido depois. No começo da carreira isso é difícil; os limites entre abstrações só começam a ficar visíveis com experiência, principalmente quando um componente fere o limite de outro.

A fonte usa uma analogia médica para justificar por que isso é necessário: um cardiologista entende a fundo os limites do coração e um dentista os limites do dente porque o corpo humano não é uma "ameba" — é dividido em órgãos, cada um com seu limite e responsabilidade próprios. Problemas graves de saúde surgem quando o limite de um órgão começa a furar o de outro; o mesmo sintoma aparece em software quando abstrações e responsabilidades são mal definidas e tudo fica misturado (ver [[wiki/concepts/acoplamento]]).

## A hash table de C → o `dict` de uma linha (aprender a abstração de baixo para cima)

[[wiki/sources/por-que-comecar-com-c-em-2026-cs50-david-malan]] ilustra abstração por camadas do ponto de vista pedagógico: no [[wiki/concepts/cs50|CS50]], os alunos escrevem em [[wiki/concepts/linguagem-c|C]] a própria implementação de uma [[wiki/concepts/algoritmos-e-estruturas-de-dados|hash table]] (dezenas de linhas) e, na semana seguinte, isso vira um dicionário de **uma única linha** em Python. A tese de [[wiki/entities/david-malan]]: você pode ser produtivo com a abstração de alto nível sem nunca entender o que ela esconde — mas quem construiu a camada de baixo entende *por que* funciona, toma decisões de design melhores e diagnostica problemas por [[wiki/concepts/primeiros-principios|primeiros princípios]]. Abstração poupa esforço; a fundação técnica é o que permite não ficar cego para o que está embaixo dela.

## Relações

- [[acoplamento]] — boa abstração é o que permite baixo acoplamento entre camadas
- [[single-responsibility]] — cada abstração deve representar uma única responsabilidade
- [[hexagonal-architecture]] — Ports & Adapters é a formalização arquitetural de abstração: Port = contrato, Adapter = implementação concreta
- [[dependency-injection]] — DI é o mecanismo que injeta a implementação concreta numa abstração

## Key sources

- [[wiki/sources/acoplamento-abstracao-estado]]
- [[sources/roadmap-dev-senior-2026]] — abstração como pilar 2: camadas que escondem complexidade sem esconder clareza
- [[wiki/sources/10-conceitos-fundamentais-computacao]] — abstração como o #1 conceito fundamental; cada um dos 9 outros conceitos é uma camada de abstração
- [[wiki/sources/design-pattern-adapter]] — caso concreto: extrair uma interface (`PdfAdapter`) entre a classe de negócio e uma lib externa de PDF é o que permite trocar de lib (DomPDF → TCPDF) sem tocar no consumidor
- [[wiki/sources/7-habitos-programador-altamente-eficaz]] — pensar primeiro em abstrações e seus limites como hábito de maturidade; analogia dos órgãos do corpo humano para justificar por que limites bem definidos importam
- [[wiki/sources/por-que-comecar-com-c-em-2026-cs50-david-malan]] — abstração por camadas no ensino: hash table de C (semana 5) → `dict` de uma linha em Python (semana 6); entender de baixo para cima o que a abstração esconde
