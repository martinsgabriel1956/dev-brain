---
type: concept
title: "Aritmética de ponteiros"
aliases: ["pointer arithmetic", "manipulação manual de ponteiros"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_count: 1
tags: [linguagem-c, ponteiros, memoria, baixo-nivel, aprendizado]
skill: lang-systems
status: stub
---

# Aritmética de ponteiros

Em C, mover um ponteiro manualmente por um número de unidades baseado no tamanho dos tipos para alcançar outro dado (ex.: pular um inteiro e um caractere para chegar ao booleano de uma `struct`). Citada em [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]] como uma das dificuldades humanas de [[wiki/concepts/linguagem-c]] — e como experiência formativa na faculdade (algoritmos e estruturas de dados, conceitos de linguagem, compiladores).

> Nota: a anedota oral usa tamanhos imprecisos ("inteiro = 8 bits, caractere = 4 bits"); em C usual `char` = 1 byte e `int` = 4 bytes, e o compilador insere *padding* entre campos. Acessar por `s.campo` evita a conta manual [skill: lang-systems, `c-cpp.md`: aritmética de ponteiros e arrays].

Relacionado: [[wiki/concepts/ponteiros-cpp-stack-heap-raii]], [[wiki/concepts/gerenciamento-de-memoria]].

## Key sources

- [[wiki/sources/c-linguagem-do-futuro-na-era-da-ia-bora-tomar-cafe]] — anedota de aprendizado e definição
