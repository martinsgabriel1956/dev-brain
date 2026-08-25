---
type: concept
title: "Scratch (Linguagem de Blocos)"
aliases: ["Scratch", "linguagem visual de programação", "drag-and-drop programming"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [cs-fundamentals, scratch, programacao-visual, ensino-de-programacao, cs50, mit]
skill: cs-fundamentals
status: stub
---

# Scratch (Linguagem de Blocos)

Linguagem de programação **gráfica** (drag-and-drop), criada há cerca de 20 anos pelo [[wiki/entities/mit-media-lab]], usada em programas extracurriculares e como introdução lúdica à programação — jogos, gráficos, arte. Representa com blocos de "quebra-cabeça" coloridos os mesmos conceitos fundamentais que sustentam linguagens textuais como C e Python: funções, condicionais, expressões booleanas e loops.

## Anatomia da interface

- **Paleta de blocos** — os "blocos de construção" organizados por categoria/cor (Eventos, Aparência, Som, Sensores, Controle, Operadores, Variáveis).
- **Área de programação** — onde os blocos são arrastados e encaixados magneticamente.
- **Sprites** — os personagens/objetos manipulados (o gato padrão pode virar qualquer coisa).
- **Palco** — o mundo 2D onde o sprite existe, com plano cartesiano (X, Y), origem no centro.

## Conceitos fundamentais mapeados em blocos

| Conceito de programação | Bloco/exemplo em Scratch |
|---|---|
| Função | `fale [texto]`, `toque som [X]` — verbos que fazem algo |
| Argumento/parâmetro | O campo editável dentro de um bloco (ex.: o texto de `fale`) |
| Efeito colateral (side effect) | Balão de fala aparecendo na tela ao usar `fale` |
| Valor de retorno | Variável `resposta`, preenchida pelo bloco `pergunte...e espere` |
| Condicional | `se [...] então [...]` / `senão` |
| Expressão booleana | `tocando no ponteiro do mouse?` |
| Loop | `repita [n]`, `para sempre` |
| Definição de função própria | "Fazer um Bloco" (bloco customizado, com argumentos próprios) |

## Efeito colateral vs. valor de retorno

Distinção didática central: um bloco como `fale` tem efeito colateral **imediato e visível ao humano** (o balão de fala aparece na tela). Um bloco como `pergunte...e espere` não tem efeito colateral visível — ele **retorna um valor** (armazenado na variável `resposta`), visível apenas ao código, até ser explicitamente usado em outro bloco (ex.: `junte [hello] [resposta]` dentro de um `fale`).

## Bug clássico: instruções sequenciais rápidas demais

Encadear `pergunte` e `fale` em sequência (duas instruções separadas) falha visualmente — o computador executa as duas tão rápido que o humano não percebe a primeira fala antes do input ser digitado. Duas soluções demonstradas: inserir um `espere N segundos` entre as duas (funciona, mas fica "picotado"), ou compor tudo em uma única chamada usando `junte` (join) — análogo a funções aninhadas em matemática, resolvendo o que está "mais dentro" primeiro.

## Abstração via blocos customizados

Repetir manualmente os mesmos blocos (ex.: copiar e colar 3x um par de blocos para "miar 3 vezes") é correto, mas mal projetado — qualquer ajuste precisa ser repetido em cada cópia. A correção passa por duas etapas: primeiro usar um loop (`repita [3]`) para centralizar a repetição; depois, opcionalmente, encapsular a lógica inteira num bloco customizado (`mie [n]`), escondendo os detalhes de implementação — o mesmo princípio de [[wiki/concepts/abstracao]] que faz um `print()` em Python esconder código C por baixo.

## Relação com outros conceitos

- [[wiki/concepts/cs50]] — Scratch é a primeira linguagem ensinada no curso (semana 0/1), antes de C e Python
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — pseudocódigo e a terminologia funções/condicionais/booleanos/loops precedem a introdução ao Scratch
- [[wiki/concepts/abstracao]] — blocos customizados como exemplo concreto de esconder implementação atrás de uma interface simples
- [[wiki/entities/mit-media-lab]] — criador e mantenedor do Scratch

## Key sources

- [[wiki/sources/cs50-2026-semana-0-representacao-dados-algoritmos-scratch]] — introdução completa à interface, demos ao vivo (Hello world, chatbot de voz, bug de sincronização, blocos customizados) e dois projetos completos (Oscar Time, IB's Hardest Game)
