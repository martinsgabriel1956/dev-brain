---
type: concept
title: "Memória RAM"
aliases: ["RAM", "random access memory", "memória de trabalho", "memória volátil"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [hardware, memoria, cs-fundamentals, ram, volatil]
skill: cs-fundamentals
status: stub
---

# Memória RAM

Memória volátil de acesso rápido que serve como espaço de trabalho de curto prazo do computador — guarda temporariamente tudo que precisa ser acessado rapidamente (código em execução, arquivos abertos, estado de um jogo), perdendo o conteúdo assim que a energia é cortada. É a camada logo abaixo do [[wiki/concepts/cache|cache]] de CPU na hierarquia de memória e acima do armazenamento persistente ([[wiki/concepts/memoria-flash|flash]], SSD, HD).

## Por que importa

Quanto mais RAM disponível e quanto maior sua frequência/largura de banda, mais processos e dados "quentes" o sistema consegue manter prontos para acesso imediato. Quando a RAM esgota, o SO recorre a [[wiki/concepts/swap|swap]] — mover páginas para disco — que é ordens de magnitude mais lento e é a causa mais comum de travamentos e lentidão perceptível.

Um erro comum de usuário é assumir que "mais RAM" resolve qualquer lentidão — a largura de banda e a arquitetura do processador/controlador de memória também limitam o desempenho final; adicionar capacidade não substitui gargalos de frequência ou latência.

## Famílias e evolução

O padrão dominante em PCs, notebooks e servidores desde os anos 2000 é o **DDR SDRAM**, hoje na sua quinta geração — ver [[wiki/concepts/ddr-sdram]] para a evolução completa (DDR1 até DDR5) com voltagem, pinagem, frequência e largura de banda de cada uma.

## Relação com outros conceitos

- [[wiki/concepts/ddr-sdram]] — a família de tecnologia por trás da RAM moderna, e sua evolução geracional
- [[wiki/concepts/memoria-virtual]] — abstração de SO construída sobre a RAM física, dando a cada processo a ilusão de memória dedicada
- [[wiki/concepts/swap]] — o que acontece quando a RAM física se esgota
- [[wiki/concepts/memoria-flash]] — contraste: RAM é volátil e rápida, flash é não volátil e mais lenta, mas persiste sem energia
- [[wiki/concepts/cache]] — camada ainda mais rápida (e menor) que fica entre CPU e RAM
- [[wiki/concepts/transistor]] — cada célula de DRAM é fisicamente um transistor + capacitor, exigindo refresh periódico para não perder a carga (o que a torna "volátil")

## Key Sources

- [[wiki/sources/evolucao-memorias-ram-ddr1-a-ddr5]]
