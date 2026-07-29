---
type: concept
title: "Red Flags de Design"
aliases: ["design red flags", "sinais de alerta de design", "code smell (ousterhout)"]
date_created: 2026-07-10
date_updated: 2026-07-29
source_count: 2
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

## Catálogo completo (Summary of Red Flags, apêndice do livro)

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] traz, no apêndice final, a lista consolidada de todos os red flags nomeados ao longo do livro. Reproduzida aqui (paráfrase, não citação literal) por ser referência prática de consulta rápida durante code review:

| Red Flag | O que sinaliza | Capítulo |
|---|---|---|
| **Shallow Module** | Interface de uma classe/método não é muito mais simples que sua implementação | 4 |
| **Information Leakage** | Uma decisão de design se reflete em múltiplos módulos | 5 |
| **Temporal Decomposition** | Estrutura do código segue a ordem de execução, não o conhecimento necessário | 5 |
| **Overexposure** | API força quem usa um recurso comum a conhecer recursos raramente usados | 5 |
| **Pass-Through Method** | Um método só repassa argumentos para outro de assinatura quase idêntica | 7 |
| **Repetition** | Um trecho de código não trivial se repete várias vezes | 9 |
| **Special-General Mixture** | Código de propósito especial não está separado do código de propósito geral | 9 |
| **Conjoined Methods** | Dois métodos têm tantas dependências entre si que só dá para entender um lendo o outro | 9 |
| **Comment Repeats Code** | Toda a informação do comentário já é óbvia a partir do código ao lado | 13 |
| **Implementation Documentation Contaminates Interface** | Comentário de interface descreve detalhes de implementação desnecessários para quem só usa a coisa documentada | 13 |
| **Vague Name** | Nome de variável/método é tão genérico que não carrega informação útil | 14 |
| **Hard to Pick Name** | É difícil achar um nome preciso e intuitivo para algo — sinal de que o design subjacente pode não estar limpo | 14 |
| **Hard to Describe** | Para ser completo, o comentário de uma variável ou método precisa ser longo | 15 |
| **Nonobvious Code** | O comportamento ou significado de um trecho de código não é fácil de entender rapidamente | 18 |

## Relação com outros conceitos

- [[wiki/concepts/code-review]] — o veículo prático recomendado para exercitar o reconhecimento de red flags.
- [[wiki/concepts/modulo-profundo]] — módulo raso é, na prática, um dos red flags mais citados no livro (interface complexa demais para a funcionalidade que expõe).
- [[wiki/concepts/complexidade-acidental]] — red flags são heurísticas para detectar complexidade acidental antes que ela se acumule.
- [[wiki/concepts/ocultamento-de-informacao]] — Information Leakage e Temporal Decomposition são os red flags específicos desse conceito.
- [[wiki/concepts/comentarios-como-ferramenta-de-design]] — Comment Repeats Code, Implementation Documentation Contaminates Interface e Hard to Describe são os três red flags de comentários.
- [[wiki/concepts/naming]] — Vague Name e Hard to Pick Name.

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — catálogo completo dos 14 red flags nomeados no livro (apêndice "Summary of Red Flags")
