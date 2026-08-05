---
type: source
title: "Três Estágios de Acoplamento e o Observer Pattern na Prática"
aliases: ["três estágios de acoplamento", "de quem é essa linha", "observer pattern jogo javascript"]
date_created: 2026-08-04
date_updated: 2026-08-04
source_count: 0
tags: [design-patterns, acoplamento, observer, factory, gof, refatoracao, javascript, jogo]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tres-estagios-de-acoplamento-observer-pattern-na-pratica.md
source_url:
author: desconhecido (canal de vídeo, playlist de construção de um jogo em JavaScript)
date_published:
date_ingested: 2026-08-04
---

# Três Estágios de Acoplamento e o Observer Pattern na Prática

## TL;DR

Vídeo de uma playlist de construção de um jogo em JavaScript que usa a refatoração incremental do código como veículo didático para ensinar [[wiki/concepts/acoplamento]] de forma prática. Propõe uma heurística de leitura de código — perguntar "de quem é essa linha?" a cada linha — e define **três estágios de desacoplamento**: (1) tudo misturado num só lugar, (2) componentes isolados mas com chamada estática/explícita entre eles (resolvido aqui com [[wiki/concepts/factory-pattern|Factory]]), e (3) componentes que não se conhecem nem estaticamente (resolvido com [[wiki/concepts/observer-pattern|Observer]], implementado do zero: `subscribe` + array de observers + `notifySubscribers`). Argumento central: nenhum estágio é "melhor" objetivamente — cada um tem seu trade-off de velocidade de protótipo vs. flexibilidade de extensão, e o Observer só compensa a complexidade extra quando há múltiplos observers anexados (ex.: sincronizar cliente e servidor com o mesmo fluxo de comandos).

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| "De quem é essa linha?" é heurística prática para detectar acoplamento | Se a resposta é sempre "do mesmo componente", o software é uma "ameba total"; se não há clareza na resposta, não há compreensão da modelagem do código | Alta |
| Existem três estágios de acoplamento, nenhum superior ao outro | Estágio 1 (tudo misturado) é ótimo para prototipagem rápida; estágio 2 (chamada estática entre componentes isolados) é como a maioria do software profissional é construído, inclusive com DI; estágio 3 (Observer) só compensa com múltiplos observers | Alta |
| Injeção de dependência não elimina o acoplamento do estágio 2, só o torna mais flexível | "mesmo assim a camada de input ainda acaba conhecendo o código da camada do jogo" mesmo com DI | Alta |
| Observer implementado sem função padronizada tipo `update` é mais flexível que a variante clássica | O autor não encontrou "um padrão" nas implementações que usam `update()`; prefere receber a função observadora diretamente (`observerFunction`), podendo ser qualquer função, não só um "observer" formal | Média — é uma escolha de design pessoal, não uma regra estabelecida na literatura de patterns |
| O custo do Observer só se paga com múltiplos observers, não com um único | "se você fizer só um subscribe com um observer, talvez não valha a pena mesmo... a partir do momento que você começa a anexar mais observers, começa a ficar muito interessante" | Alta |
| Impacto de adicionar um novo observer no código existente é praticamente zero | Exemplo dado: simular uma camada de rede (`network`) que se inscreve nos mesmos comandos de teclado, sem tocar no subject nem nos observers já existentes | Alta |

## Estrutura do exemplo (jogo em JavaScript)

```
Estágio 1 (ameba)
└── camada de input: keydown handler com regra de negócio do jogo misturada

Estágio 2 (Factory — acoplamento estático explícito)
input.js ──chama──> createGame().multiplayer(command)
                          │
                          └── state { players, frutas } isolado dentro da factory

Estágio 3 (Observer — desacoplamento total)
createGame() [Subject]
  .subscribe(observerFunction)   // registra observer
  .notifySubscribers(command)    // loop pelos observers, executa cada um

input.js (keydown) ──notifySubscribers(command)──> [subscribers array]
                                                        ├── game.multiplayer  (subscribe)
                                                        └── network.send      (subscribe, exemplo hipotético)
```

## Pseudocódigo central do Observer implementado

```javascript
function createGame() {
  const state = { players: [], frutas: [], observers: [] };

  function subscribe(observerFunction) {
    state.observers.push(observerFunction);
  }

  function notifySubscribers(command) {
    console.log('notify:', state.observers.length);
    state.observers.forEach((observerFunction) => observerFunction(command));
  }

  return { subscribe, notifySubscribers, /* ... */ };
}

// input.js
document.addEventListener('keydown', (event) => {
  game.notifySubscribers({ player: 1, action: event.key });
});

// engate dinâmico, fora da camada de input
game.subscribe(gameLogic.multiplayer);
```

## Entidades Mencionadas

Nenhuma entidade nomeada (canal/autor não identificado na transcrição).

## Conceitos Tocados

- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/observer-pattern]]
- [[wiki/concepts/factory-pattern]]
- [[wiki/concepts/design-patterns]]
- [[wiki/concepts/single-responsibility]]
- [[wiki/concepts/dependency-injection]]

## Open Questions

- A fonte não menciona ordem de notificação entre observers nem tratamento de erro caso um `observerFunction` lance exceção durante o loop — mesma lacuna já registrada em [[wiki/sources/design-pattern-observer]] ("como garantir ordem de notificação quando ela importa").
- Não há discussão de memory leak por observers não removidos (falta um `unsubscribe` na implementação mostrada) — o Refactoring Guru ([[wiki/sources/design-pattern-observer]]) já levanta essa mesma lacuna.
- A crítica implícita ao padrão `update()` clássico do Observer (preferir passar a função diretamente) é uma opinião de implementação, não confrontada com a literatura GoF formal nesta fonte — vale nuance futura comparando com [[wiki/sources/design-pattern-observer]] e [[wiki/sources/design-patterns-gof]].

## Raw Quotes

> "Toda vez que vocês olharem uma linha de código [...] a pergunta é bem simples: de quem é essa linha?"

> "Dentro de um sistema, se você 100% das vezes conseguir responder que aquela linha de código pertence ao mesmo componente, você tem um software 'ameba' total."

> "Isso com certeza traz mais complexidade, e se você fizer só um subscribe com um observer, talvez não valha a pena mesmo. Mas a partir do momento que você começa a anexar mais observers, começa a ficar muito interessante, porque o impacto no código existente é praticamente zero."

> "Não achei um padrão em implementações que [...] executam uma função padronizada tipo update [...]. Acho muito mais flexível passar a função na qual você quer que o dado chegue."
