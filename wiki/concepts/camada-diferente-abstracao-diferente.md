---
type: concept
title: "Camada Diferente, Abstração Diferente"
aliases: ["different layer, different abstraction", "camadas diferentes, abstrações diferentes", "abstrações semelhantes em camadas adjacentes"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_count: 2
tags: [design, ousterhout, camadas, abstracao, modulo-profundo, pass-through]
skill: tech-mentor-backend
status: draft
---

# Camada Diferente, Abstração Diferente

## TL;DR

Regra de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, cap. 7): em um sistema bem projetado, cada camada fornece uma abstração diferente das vizinhas. Seguindo uma operação pelas chamadas, a abstração deve mudar a cada método. Camadas adjacentes com abstrações parecidas indicam decomposição ruim ([[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]]).

## Exemplos de camadas bem separadas

| Sistema | Camada de cima | Meio | Camada de baixo |
|---|---|---|---|
| Sistema de arquivos | arquivo: bytes de tamanho variável, leitura e escrita de intervalos | cache em memória de blocos de tamanho fixo | drivers movendo blocos entre disco e memória |
| TCP | fluxo de bytes confiável | — | pacotes de tamanho limitado, melhor esforço |

## Como o problema aparece

- **[[wiki/concepts/metodo-de-repasse]]**: método que só chama outro de assinatura igual (`TextDocument.insertString` → `TextArea.insertString`).
- **[[wiki/concepts/decorator-pattern|Decorator]] em excesso**: mesma API embrulhada para pouca função nova; vira [[wiki/concepts/classite]].
- **Variável de passagem**: argumento que desce por métodos que não o usam. Saída: [[wiki/concepts/objeto-de-contexto]].
- **Interface igual à implementação**: classe de texto que guarda linhas e expõe `getLine`/`putLine`. Os chamadores passam a dividir e juntar linhas. Com `insert`/`delete` sobre posições arbitrárias, a diferença entre API e armazenamento é a função da classe ([[wiki/concepts/modulo-profundo]]).

## Quando a mesma assinatura é aceitável

Quando cada método agrega função. O *dispatcher* escolhe qual método executa (servidor Web roteando por URL). Várias implementações da mesma interface (drivers de disco) reduzem a [[wiki/concepts/carga-cognitiva]] e costumam ficar na mesma camada, sem chamar umas às outras.

## Por que importa

O cap. 7.6 liga a regra ao custo-benefício geral: todo elemento de design (classe, método, argumento) é algo a mais para aprender e só vale se eliminar mais complexidade do que traz. Uma camada com a mesma abstração da vizinha adiciona a infraestrutura sem o ganho.

## Relação com outros conceitos

- [[wiki/concepts/architecture-sinkhole]]: o mesmo sintoma na escala de camadas de aplicação (controller → service → repository só repassando). Ligação feita pela wiki, não pelo livro.
- [[wiki/concepts/abstracao]]: cada camada deve esconder algo da de cima; se a de cima vê a mesma coisa, não há abstração nova.
- [[wiki/concepts/modulo-de-proposito-geral]]: os drivers de disco aparecem nos dois capítulos, como especialização empurrada para baixo (cap. 6) e como implementações múltiplas aceitáveis (cap. 7).
- [[wiki/concepts/red-flags-de-design]]: o catálogo do livro só tem *Pass-Through Method* para este capítulo.

## Key sources

- [[wiki/sources/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente]]: texto do cap. 7, com exemplos, Figuras 7.1 e 7.2 e conclusão
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]: resumo do cap. 7 (camadas adjacentes semelhantes como red flag)
