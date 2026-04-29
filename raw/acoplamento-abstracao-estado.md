# Acoplamento, Abstração e Estado — Lentes para Enxergar Código

**Fonte:** Transcrição de vídeo  
**Data:** 2026-04-25  
**Domínio:** Fundamentos de programação / Arquitetura

---

## O problema com decoreba técnica

Termos como *acoplamento*, *abstração* e *estado* não servem para decorar — servem como **lentes**. Sem entender o que significam na prática, você programa vendado: o código pode funcionar hoje e quebrar amanhã sem você saber por quê.

---

## Acoplamento

### O que é

Acoplamento não significa "tudo junto em um lugar". Significa que **cada parte depende de todo o resto**. Numa função que faz tudo (busca, valida, transforma, envia, loga), mudar uma etapa pode quebrar outra que você nem tocou.

Pense num quebra-cabeça com peças coladas: você não consegue tirar uma sem destruir as vizinhas.

### Exemplo acoplado

```typescript
function processarPedido(pedidoId: string) {
  // busca no banco
  const pedido = db.query(`SELECT * FROM pedidos WHERE id = '${pedidoId}'`);

  // valida
  if (!pedido || pedido.status !== "pendente") throw new Error("Inválido");

  // transforma
  const payload = { id: pedido.id, total: pedido.valor * 1.1 };

  // envia para API
  await api.post("/pedidos", payload);

  // loga
  console.log({ message: "Pedido processado", pedidoId });
}
```

Mudou a estrutura do banco? Mexe na validação. Mudou o formato da API? Mexe na transformação. Tudo puxa tudo.

### Exemplo de baixo acoplamento

```typescript
async function buscarPedido(pedidoId: string) {
  return db.query(`SELECT * FROM pedidos WHERE id = '${pedidoId}'`);
}

function validarPedido(pedido: Pedido) {
  if (!pedido || pedido.status !== "pendente") throw new PedidoInvalidoError(pedido?.id);
}

function transformarPedido(pedido: Pedido) {
  return { id: pedido.id, total: pedido.valor * 1.1 };
}

async function enviarPedido(payload: PedidoPayload) {
  await api.post("/pedidos", payload);
}
```

Cada função tem uma responsabilidade. Mudança no banco → mexe só em `buscarPedido`. Mudança na API → mexe só em `enviarPedido`.

### Por que importa

Sistemas altamente acoplados se tornam insustentáveis: uma mudança pequena quebra coisas inesperadas. O time para de evoluir e começa a apagar incêndio. O código congela.

---

## Abstração

### O que é

Abstração é **esconder o que não precisa ser visto**. Você não precisa saber como a antena do celular funciona para fazer uma ligação — a complexidade fica oculta.

No código: você não precisa saber se os dados vêm de banco, API ou arquivo. Só precisa saber que a função retorna os dados.

### Exemplo com interface

```typescript
// Abstração: contrato genérico
type PedidoRepository = {
  buscarPorId: (id: string) => Promise<Pedido | null>;
};

// Implementações concretas
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

// Código principal: não sabe (nem liga) de onde vêm os dados
async function processarPedido(repo: PedidoRepository, pedidoId: string) {
  const pedido = await repo.buscarPorId(pedidoId);
  // ...
}
```

### Por que importa

Você pode trocar de banco para API **sem mexer em nenhuma linha de código principal**. O resto do código não sabe o que está por baixo — só sabe que recebe um objeto que consegue buscar pedidos.

---

## Estado

### O que é

Estado é **o que está guardado naquele momento**. Uma variável `contador = 5` tem estado `5`. Depois de incrementar, estado é `6`. Simples — até você compartilhar esse estado.

### Problema: estado compartilhado

```typescript
const estadoGlobal = { saldo: 1000 };

function fazerCompra(valor: number) {
  estadoGlobal.saldo -= valor;
}

function aplicarDesconto(percentual: number) {
  estadoGlobal.saldo *= 1 - percentual / 100;
}

function consultarSaldo() {
  return estadoGlobal.saldo;
}

fazerCompra(500);     // saldo: 500
aplicarDesconto(10);  // saldo: 450
consultarSaldo();     // qual é o estado real?
```

Quando algo dá errado, você não sabe qual função mexeu no estado primeiro, nem qual sequência de mudanças causou o problema.

### Solução: estado isolado

```typescript
function fazerCompra(saldoAtual: number, valor: number): number {
  return saldoAtual - valor;
}

function aplicarDesconto(saldoAtual: number, percentual: number): number {
  return saldoAtual * (1 - percentual / 100);
}

const saldo = 1000;
const saldoAposCompra = fazerCompra(saldo, 500);       // 500
const saldoFinal = aplicarDesconto(saldoAposCompra, 10); // 450
```

Cada função **recebe um estado e retorna um novo estado** sem mutar o original. Você sempre sabe quem mudou o quê e em que ordem. Rastreabilidade total.

### Por que importa

Estado compartilhado + múltiplas funções mutando o mesmo objeto = impossível debugar em sistemas grandes. Isolamento de estado é a base de código previsível.

---

## Outros termos da mesma família

Os três conceitos acima são um ponto de partida. O vocabulário completo inclui:

| Termo | TL;DR |
|---|---|
| **Coesão** | Quanto uma unidade faz coisas relacionadas entre si |
| **Idempotência** | Executar N vezes = mesmo resultado que executar 1 vez |
| **Efeito colateral** | Uma função que muda algo além do que retorna |
| **Imutabilidade** | Dados que não podem ser alterados após criados |

---

## Na era da IA

IAs geram código que **funciona**. Nem sempre geram código que é **bom**. Sem essas lentes você não distingue os dois. O código gerado pode ser altamente acoplado, ter estado compartilhado e zero abstração — e você só vai perceber quando ele quebrar na próxima mudança.

Entender esses termos como ferramentas de pensamento é o que diferencia quem constrói sistemas que **duram** de quem constrói sistemas que **funcionam por enquanto**.
