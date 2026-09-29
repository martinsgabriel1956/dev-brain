---
type: concept
title: "CLR e Garbage Collector (.NET)"
aliases: ["CLR", "common language runtime", "garbage collector .net", "CTS", "GC .net"]
date_created: 2026-09-28
date_updated: 2026-09-28
source_count: 1
tags: [dotnet, csharp, runtime, performance, fundamentos]
skill: tech-mentor-leadership
status: stub
---

# CLR e Garbage Collector (.NET)

## TL;DR

Segundo [[wiki/entities/andre-casciotti]], entender como funciona a **CLR** (Common Language Runtime), a **CTS** (Common Type System) e o **Garbage Collector** do .NET é um fundamento que costuma ser pulado — tanto por iniciantes quanto por devs experientes — e cuja falta explica boa parte dos problemas de performance em produção que, sem esse conhecimento, parecem inexplicáveis ("a aplicação tá pressionando o GC e comendo CPU da máquina, e eu não sei por quê").

## Onde isso se encaixa no pipeline de compilação

O runtime do .NET é o "meio-termo" entre compilador puro e interpretador puro descrito em [[wiki/concepts/compilador]]: C# compila para bytecode (IL) que roda sobre a CLR, com compilação JIT (Just-In-Time) para código nativo em tempo de execução — o mesmo modelo geral de Java/JVM. A CLR é quem gerencia esse bytecode, tipos (via CTS) e o ciclo de vida de memória (via GC), abstraindo do programador a alocação e liberação manual de memória.

## Recomendação de estudo

O autor recomenda que isso seja estudado **em paralelo** com a prática, não como pré-requisito teórico isolado — na mesma lógica de "devagar, por demanda" descrita em [[wiki/concepts/aprender-com-foco-no-problema]]: entender IDE, compilador (Roslyn) e depois a CLR/GC conforme problemas reais de build, warning ou performance forem aparecendo.

## Relação com outros conceitos

- [[wiki/concepts/compilador]] — a CLR é a máquina virtual que executa o bytecode gerado pelo compilador C#/Roslyn (mesmo modelo de JVM para Java)
- [[wiki/concepts/arquitetura-cliente-servidor]] — fundamento irmão recomendado na mesma seção da fonte, sobre "como as coisas funcionam por baixo"

## Key Sources

- [[wiki/sources/o-que-estudar-guia-para-iniciantes-andre-casciotti]]
