---
type: concept
title: "Boy Scout Rule"
aliases: ["regra do escoteiro", "leave the campground cleaner", "deixe o código mais limpo do que encontrou"]
date_created: 2026-07-09
date_updated: 2026-07-09
source_count: 1
tags: [craftsmanship, tech-debt, refactoring, clean-code, principios]
skill: tech-mentor-leadership
status: stable
---

## Definição

Princípio emprestado dos escoteiros americanos — *"deixe o acampamento mais limpo do que você o encontrou"*. Popularizado na comunidade de programação por [[wiki/entities/uncle-bob]]: a prática de deixar o código um pouco mais limpo a cada mudança feita numa base de código existente, mesmo que a limpeza não faça parte do escopo pedido.

## Por Que Funciona

A qualidade do código degrada naturalmente com o tempo — cada mudança tende a acumular pequenas imprecisões (nomes ruins, duplicação, acoplamento). Essa degradação é [[wiki/concepts/tech-debt-como-ferramenta|dívida técnica]] inadvertida.

A Boy Scout Rule ataca essa dívida de forma incremental e contínua, em vez de esperar por um "projeto de refactoring" dedicado — que segundo a literatura de gestão técnica raramente é aprovado ou termina bem.

## Exemplo

Tarefa: alterar um valor dentro de uma função. O escopo pedido é só isso. Mas o dev percebe que os nomes das variáveis da função não são claros.

- **Sem a regra:** faz só o que foi pedido, ignora o resto.
- **Com a regra:** faz o que foi pedido *e* renomeia as variáveis, já que está ali mesmo.

Não se limita a nomes — qualquer melhoria pequena e segura (extrair uma função, remover um comentário morto, corrigir uma indentação) conta.

## Limites do Princípio

- Não é licença para expandir o escopo do PR indefinidamente — a melhoria deve ser pequena e não deve arriscar quebrar o comportamento existente.
- Difere de refactoring dedicado: a Boy Scout Rule é sempre acoplada a uma mudança que já estava sendo feita por outro motivo, não é uma tarefa própria.
- Complementar, não substituto, de estratégias maiores de pagamento de dívida técnica como [[wiki/concepts/strangler-fig]] ou debt sprints.

## Relação com Outros Princípios

- [[wiki/concepts/tech-debt-como-ferramenta]] — a Boy Scout Rule é uma das estratégias de pagamento contínuo citadas no Quadrante de Fowler (dívida inadvertida-prudente sendo corrigida aos poucos).
- [[wiki/concepts/code-review]] — revisores podem usar a regra como critério: "o PR deixou o código pior, igual ou melhor do que estava?"

## Key Sources

- [[wiki/sources/5-principios-que-mudaram-como-programador]]
