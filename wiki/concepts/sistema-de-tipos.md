---
type: concept
title: "Sistema de Tipos"
aliases: ["type system", "tipagem estática", "tipagem dinâmica", "inferência de tipos", "static vs dynamic typing"]
date_created: 2026-07-09
date_updated: 2026-07-16
source_count: 3
tags: [cs-fundamentals, linguagens-de-programacao, tipagem, compiladores]
skill: cs-fundamentals
status: draft
---

# Sistema de Tipos

Conjunto de regras que decide o que uma linguagem considera um valor válido de determinado tipo, e o que acontece quando tipos diferentes interagem (ex.: somar um número com uma string). A decisão central é **quando** essas regras são verificadas.

## Estática vs. Dinâmica

| | Tipagem Estática | Tipagem Dinâmica |
|---|---|---|
| **Quando verifica** | Em tempo de compilação, antes do código rodar | Em tempo de execução |
| **Vantagem** | Erros de tipo pegos cedo; editor consegue oferecer autocomplete melhor | Mais rápida de escrever; menos verbosidade |
| **Custo** | Mais informação explícita no código (tipos de parâmetro, genéricos, tratamento de nulos) | Erros só aparecem quando aquele caminho de código executa — às vezes em produção |
| **Exemplos** | Rust, Java, TypeScript, C | Python, JavaScript, Ruby |

Exemplo do trade-off prático: somar um número com uma string. Em JavaScript (dinâmica), o número é convertido e concatenado silenciosamente. Em Python (dinâmica), lança erro em runtime. Numa linguagem estaticamente tipada como Rust, essa operação inválida nem passa pela compilação.

### "Tipagem fraca" é um eixo diferente de estática/dinâmica

JavaScript costuma ser descrito como de "tipagem fraca" — não porque os tipos sejam checados em momento diferente (isso é o eixo estática/dinâmica acima), mas porque a linguagem **converte tipos implicitamente** em vez de lançar erro (`"1" + 2` → `"12"`, `null == undefined` → `true`). Ver [[wiki/concepts/tipos-primitivos-javascript]] para os 8 tipos primitivos de JS e o detalhamento de onde essa conversão implícita acontece (concatenação, `==`, parâmetros default vs. `||`).

## Inferência de tipos — o meio-termo

Linguagens como TypeScript e Rust deduzem o tipo sem exigir declaração explícita: `let x = 42` já é reconhecido como número pelo compilador. Mantém boa parte da segurança da tipagem estática com a concisão da dinâmica.

## Além de número vs. string

Um sistema de tipos completo também precisa decidir: se uma função pode retornar tipos diferentes, se variáveis podem mudar de tipo, como genéricos funcionam, e como representar a ausência de valor (null, `Option`/`Maybe`, `undefined`). Cada uma dessas decisões afeta diretamente a segurança e a ergonomia da linguagem.

## Ausência de valor e erro como tipo, não como valor mágico

Rust representa ausência de valor com `Option<T>` (`Some`/`None`) em vez de um `null` implícito, e erro recuperável com `Result<T, E>` (`Ok`/`Err`) em vez de exceptions não tipadas. O `match` sobre esses tipos é exaustivo — o compilador exige tratar todos os casos, então o erro (ou a ausência) aparece no tipo da função, não escondido atrás de um valor que só quebra quando alguém esquece de checar. O mesmo princípio se estende a `enum`: modelar estado com variantes exaustivas (em vez de campos soltos) torna combinações inválidas irrepresentáveis em compile-time. Ver [[wiki/concepts/rust-fundamentos]].

## Relação com outros conceitos

- [[wiki/concepts/compilador]] — o sistema de tipos é validado sobre a AST que o parser produz, antes (estática) ou depois (dinâmica) da geração de código
- [[wiki/concepts/gerenciamento-de-memoria]] — em Rust, o *type checker* e o *borrow checker* trabalham juntos: ownership é, em parte, verificação de tipos em tempo de compilação
- [[wiki/concepts/rust-fundamentos]] — `Option`/`Result`/`enum` exaustivo como exemplo concreto de sistema de tipos carregando comportamento possível

## Key sources

- [[wiki/sources/como-criar-uma-linguagem-de-programacao]]
- [[wiki/sources/8-tipos-de-javascript]]
- [[wiki/sources/rust-por-que-tanto-hype-ownership-borrowing-lifetimes]] — `Option`/`Result`/`match` exaustivo como caso concreto de tipo carregando o comportamento possível
