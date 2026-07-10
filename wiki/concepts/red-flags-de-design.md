---
type: concept
title: "Red Flags de Design"
aliases: ["design red flags", "sinais de alerta de design", "code smell (ousterhout)"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [design, code-review, ousterhout, complexidade, qualidade]
skill: tech-mentor-backend
status: draft
---

# Red Flags de Design

## TL;DR

Método prático de [[wiki/entities/john-ousterhout]] para reconhecer complexidade desnecessária: um red flag é um sinal de que um trecho de código provavelmente é mais complicado do que precisa ser. Ao ver um, a resposta é parar e procurar um design alternativo que elimine o problema — mesmo que isso exija testar várias alternativas antes de achar uma boa.

## Por que via code review, não introspecção

Princípios de design abstratos são difíceis de aplicar olhando só para o próprio código — é mais fácil ver problemas de design no código de outra pessoa do que no próprio. Por isso o método recomendado é usar os red flags durante [[wiki/concepts/code-review]]: identificar o sinal, sugerir a melhoria, e no processo se expor a novas abordagens de design.

## O ciclo de aprendizado

1. Ver o red flag (ou no próprio código, ou revisando o de outra pessoa).
2. Parar e procurar um design alternativo que elimine o problema — não aceitar o primeiro que aparece.
3. Testar várias alternativas se necessário; quanto mais alternativas testadas antes de corrigir, mais se aprende.
4. Com o tempo, o código tende a ter cada vez menos red flags, e a experiência revela novos red flags não catalogados previamente.

## Limite do princípio

Todo red flag e todo princípio de design tem exceções — levar qualquer ideia ao extremo tipicamente piora o resultado. Design bonito é equilíbrio entre ideias concorrentes, não aplicação mecânica de regras.

## Relação com outros conceitos

- [[wiki/concepts/code-review]] — o veículo prático recomendado para exercitar o reconhecimento de red flags.
- [[wiki/concepts/modulo-profundo]] — módulo raso é, na prática, um dos red flags mais citados no livro (interface complexa demais para a funcionalidade que expõe).
- [[wiki/concepts/accidental-complexity]] — red flags são heurísticas para detectar complexidade acidental antes que ela se acumule.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-introducao]]
