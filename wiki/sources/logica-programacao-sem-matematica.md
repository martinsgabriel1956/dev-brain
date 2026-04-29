---
type: source
title: "Lógica de Programação Sem Ser Gênio da Matemática"
aliases: []
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/gabriel-martins/Documentos/dev-study/raw/logica-programacao-sem-matematica.md
source_url: ""
author: "speaker brasileiro (canal de programação — Java/Eclipse)"
date_published: ""
date_ingested: 2026-04-22
tags: [tech-mentor, carreira, logica, algoritmos, solid, java, iniciante]
skill: tech-mentor-leadership
status: stable
---

# Lógica de Programação Sem Ser Gênio da Matemática

## TL;DR

Três técnicas para quem acredita não ter "dom" para programação: decompor o problema em passos menores, refatorar cada passo em método com responsabilidade única (SRP/SOLID), e desenvolver pensamento algorítmico pela prática constante e explicação em voz alta. Matemática exigida é básica (divisão inteira, módulo).

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Programação não exige matemática avançada | Exercício do caixa eletrônico usa só divisão inteira e módulo | Alta |
| Decomposição em passos é o núcleo da lógica | 4 passos: receber → definir notas → calcular → exibir | Alta |
| SRP em métodos facilita debug | Cada método = uma responsabilidade → falha localizada | Alta |
| Explicar código em voz alta melhora raciocínio lógico | Sugestão prática: explicar para alguém sem contexto | Média |
| Outline da IDE depende de métodos separados | Com código monolítico no main, outline fica vazio | Alta |

## Exercício Demonstrado — Caixa Eletrônico

**Problema:** dado valor de saque, calcular quantas notas de cada denominação.

**Decomposição:**
```
Passo 1: Receber valor (Scanner)
Passo 2: Definir notas {100, 50, 20, 5, 2}
Passo 3: Calcular quantidade por denominação (divisão inteira + módulo)
Passo 4: Exibir resultado
```

**Refatoração SRP:**
- `obterValorSaque(Scanner)` — I/O
- `calcularNotas(int valor, int[] notas)` — lógica pura
- `exibirNotas(int[] notas, int[] qtd)` — apresentação

## Concepts Touched

- [[concepts/decomposicao-de-problemas]]
- [[concepts/aprendizado-deliberado]]
- [[concepts/postura-de-programador]]

## Open Questions

- Como aplicar a mesma decomposição em problemas com estado mutável/assíncrono?
- SRP em métodos estáticos vs. classes — quando escalar para OO completo?
