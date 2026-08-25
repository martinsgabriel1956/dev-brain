---
type: concept
title: "Padrão de Seções de Documentação Técnica"
aliases: ["getting started tutorials api reference examples", "estrutura padrão de docs"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [carreira, aprendizado, documentacao]
skill: tech-mentor-leadership
status: stub
---

# Padrão de Seções de Documentação Técnica

Praticamente toda documentação oficial de linguagem/framework segue as mesmas quatro seções, o que torna a navegação previsível independente da stack:

| Seção | Para que serve | Palavras-chave de busca |
|---|---|---|
| **Getting Started** | Criar o primeiro projeto funcionando. Nunca pular. | "getting started X", "quick start", "quick start guide", "installation guide X", "setup X" |
| **Tutorials** | Passo a passo por tópico específico | "tutorial X" |
| **API Reference** | Referência exaustiva de classes/métodos/assinaturas — ver [[wiki/concepts/javadoc-api-reference]] | — |
| **Examples** | Código de exemplo pronto | "examples X" |

## Por que importa

Saber os nomes das seções antes de abrir a documentação transforma "não sei por onde começar" em uma busca dirigida no Google (ex.: "getting started spring boot"). O padrão foi verificado em [[wiki/entities/spring-boot]] (Learning → Guides → Projects), Go ("get started") e Angular ("getting started" → tutorial "your first Angular project").

## [skill: tech-mentor-leadership] O padrão bate com o framework Diátaxis

O padrão de quatro seções observado empiricamente pela fonte corresponde de perto ao framework **Diátaxis** (Daniele Procida), usado do lado de quem *escreve* documentação (ver `docs-as-code.md` na skill): documentação se divide em **Tutorial** (aprender fazendo — equivalente a Getting Started/Tutorials) e **Reference** (consultar detalhes — equivalente a API Reference), cruzados com os eixos aprendizado/trabalho e prático/teórico. Isso não é coincidência: a fonte descreve o padrão do lado do consumidor, e Diátaxis é a formalização do mesmo padrão do lado de quem projeta a documentação. **Examples**, citado pela fonte, fica mais próximo do quadrante **How-to** de Diátaxis (resolver um problema pontual) do que de Reference.

## Ver Também

- [[wiki/concepts/documentacao-oficial-como-recurso]] — por que ler a documentação tem retorno alto; este conceito é o "como" complementar
- [[wiki/concepts/javadoc-api-reference]] — a camada de API reference aprofundada, com foco em Java/JavaDoc

## Key Sources

- [[wiki/sources/como-ler-documentacao-de-uma-linguagem-de-programacao]]
