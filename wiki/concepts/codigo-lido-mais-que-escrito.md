---
type: concept
title: "Código É Lido Mais Vezes do Que Escrito"
aliases: ["code is read more than written", "legibilidade como prioridade", "lido mais do que escrito"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [clean-code, legibilidade, manutencao, craftsmanship]
skill: tech-mentor-leadership
status: draft
---

# Código É Lido Mais Vezes do Que Escrito

Máxima de engenharia de software: como sistemas duram anos e equipes mudam, cada trecho é lido muito mais vezes do que foi escrito, então otimiza-se para o **leitor**. Consequências práticas: nomes que dizem a intenção ([[wiki/concepts/naming]]), métodos curtos com variáveis declaradas perto do uso, e modelos que tornam o estado inválido impossível ([[wiki/concepts/classe-como-conceito-de-dominio]]). Relacionada a [[wiki/concepts/codigo-para-o-mantenedor]] e [[wiki/concepts/codigo-para-o-futuro-eu]]. Exemplo do autor: uma variável `d` alterada várias vezes na linha 533 de um método de 1000 linhas. [external] A máxima costuma ser atribuída a Robert C. Martin (*Clean Code*), variando em Guido van Rossum; atribuição não verificada aqui.

## Key Sources

- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — a frase-chave do vídeo e o exemplo `double d` vs `valorDescontoPedido`
