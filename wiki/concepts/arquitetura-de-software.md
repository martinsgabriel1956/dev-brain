---
type: concept
title: "Arquitetura de Software"
aliases: ["software architecture", "decisao arquitetural"]
date_created: 2026-07-03
date_updated: 2026-07-10
source_count: 4
tags: [arquitetura, carreira, fundamentos, ia]
skill: tech-mentor-leadership
status: draft
---

# Arquitetura de Software

Como sistemas são estruturados e como certas decisões de estrutura escalam bem enquanto outras criam bola de neve de problemas. Não existe arquitetura boa para tudo — existe **arquitetura certa para o contexto certo** (restrições reais de tempo, escala, dinheiro, equipe).

## Por que é parte da fundação do engenheiro

Decisão arquitetural errada não se corrige com refatoração pontual — pode custar meses de trabalho jogados fora e gerar [[wiki/concepts/complexidade-acidental|dívida técnica]] que a equipe carrega por anos. Ver a distinção entre execução (programador) e decisão arquitetural (engenheiro) em [[wiki/concepts/engenheiro-vs-programador]].

## Decisão Arquitetural Não É Um Prompt

A IA ajuda um arquiteto a discutir alternativas, explicar trade-offs para públicos não técnicos e gerar rascunhos de solução — mas a decisão em si exige analisar o [[wiki/concepts/contexto-organizacional-para-arquitetura|contexto organizacional]] real:

- Como os dados são manipulados e onde estão armazenados
- Quais integrações entre sistemas existem
- Custo da arquitetura sugerida vs. disposição do cliente a pagar por ela
- Se a empresa tem *know-how* e licenciamento para as tecnologias sugeridas

Perguntar para uma IA "que arquitetura eu uso?" com um prompt enxuto não substitui essa análise. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Leituras de referência citadas

- *Clean Architecture* (Robert Martin) — princípios
- *Fundamentals of Software Architecture* (Mark Richards & Neal Ford) — trade-offs práticos
- *Designing Data-Intensive Applications* (Martin Kleppmann) — sistemas distribuídos, o livro que "separa júnior de sênior" nesse tema
- *Domain-Driven Design* (Eric Evans) e *A Philosophy of Software Design* (John Ousterhout) — tradução de domínio de negócio em modelo de código, ver [[wiki/concepts/entendimento-de-dominio]]

Nenhum desses livros foi lido/ingerido diretamente ainda no wiki — são citações de segunda mão a partir da fonte abaixo. **Atualização:** *A Philosophy of Software Design* passou a ter citação de primeira mão em [[wiki/sources/filosofia-do-design-de-software-introducao]] (capítulo 1, traduzido diretamente do livro) — ver [[wiki/entities/john-ousterhout]] e [[wiki/concepts/modulo-profundo]].

## Design de arquitetura como processo contínuo, não fase única

[[wiki/sources/filosofia-do-design-de-software-introducao]] fornece o argumento estrutural para por que decisão arquitetural nunca deveria ser tratada como "congelada" no início do projeto: o modelo cascata falha porque é impossível visualizar todas as implicações de um design grande antes de construir algo — os problemas só ficam claros com a implementação avançada, ponto em que o cascata não tem mecanismo de retorno ao design. Ver [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]. Isso reforça a tensão já descrita nesta página entre "decisão errada custa meses de trabalho" e a necessidade de revisão arquitetural contínua ao longo do projeto, não só na largada.

## Módulos Profundos: a Unidade Estrutural que Decide se a Arquitetura Escala

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] concretiza "decisões de estrutura que escalam bem vs. geram bola de neve" (frase de abertura desta página) com o conceito de Ousterhout: poucos módulos grandes com interface simples ([[wiki/concepts/modulo-profundo|módulos profundos]]) escalam; muitos módulos pequenos com interfaces complexas (módulos rasos) geram a bola de neve. Na era da IA isso ganha um segundo motivo para importar: agentes de IA navegam mal bases de código com módulos rasos, e produzem módulos rasos por padrão quando não há uma interface bem projetada guiando a implementação.

## Key Sources

- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — fatores de contexto de negócio e organizacional que uma decisão arquitetural precisa considerar
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] — módulos profundos como unidade estrutural concreta
- [[wiki/sources/filosofia-do-design-de-software-introducao]] — por que design (arquitetural ou não) é processo contínuo, não fase única
