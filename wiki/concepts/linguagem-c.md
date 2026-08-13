---
type: concept
title: "Linguagem C"
aliases: ["C", "C language", "linguagem C como fundação"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 1
tags: [cs-fundamentals, linguagens, aprendizado, fundamentos, performance]
skill: cs-fundamentals
status: stub
---

# Linguagem C

Linguagem procedural de baixo nível, criada nos anos 1970, que ocupa um lugar único no ensino de computação: é **o mais perto do hardware que se chega mantendo sintaxe parecida com inglês**, antes de descer para assembly e, abaixo dele, para zeros e uns.

## Por que C é uma boa fundação pedagógica

Segundo [[wiki/entities/david-malan]] em [[wiki/sources/por-que-comecar-com-c-em-2026-cs50-david-malan]], C equilibra dois lados:

- **Abstrações legíveis** sobre primitivas de baixo nível — os construtos fundamentais que hoje são comuns a quase toda linguagem: loops, condicionais, funções, variáveis, valores de retorno.
- **Linguagem pequena, biblioteca padrão enxuta.** Sem baixar bibliotecas de terceiros, quase tudo o que você quiser precisa ser construído por você mesmo.

Essa ausência de estruturas prontas é a **feature pedagógica**, não um defeito: diferente de Java/C++ com STL, em C você não instancia uma hash table — você a constrói. Isso força o entendimento de baixo para cima (ver [[wiki/concepts/fundacao-tecnica]]) e o raciocínio por [[wiki/concepts/primeiros-principios]]. No [[wiki/concepts/cs50|CS50]], é em C que os alunos escrevem, na semana 5, suas próprias [[wiki/concepts/algoritmos-e-estruturas-de-dados|estruturas de dados]] (listas ligadas, hash tables, tries, árvores, pilhas, filas).

## Andaime para linguagens de alto nível

A hash table de dezenas de linhas escrita em C na semana 5 do CS50 vira um dicionário de **uma linha** em Python na semana 6. Quem passou pela implementação em C entende o que a abstração de alto nível esconde — ver [[wiki/concepts/abstracao]]. Quem aprende só pela linguagem de alto nível "nunca chega a entender o que está acontecendo por baixo do capô".

## Relevância prática

C ainda figura no topo dos rankings de onipresença de linguagens (número 1 ou 2 em alguns, ano após ano) por ser **altamente performática**, ainda que mais difícil de escrever que linguagens modernas. Mas seu valor no ensino não está no uso diário: Malan usa C só ~5 semanas por ano. O valor está nos princípios extraídos dela — a distinção "[[wiki/concepts/sintaxe-vs-conhecimento-perene|não precisar usar ≠ não precisar saber]]".

## Relações

- [[wiki/concepts/ponteiros-cpp-stack-heap-raii]] — ponteiros e stack vs. heap, conceitos que C expõe crus
- [[wiki/concepts/rust-fundamentos]] — alternativa moderna que tenta ensinar os mesmos primeiros princípios com memória segura (ownership/borrowing)
- [[wiki/concepts/gerenciamento-de-memoria]] — manual (C), garbage collector ou ownership

## Key sources

- [[wiki/sources/por-que-comecar-com-c-em-2026-cs50-david-malan]] — C como fundação pedagógica; construir as próprias estruturas de dados; andaime para Python
