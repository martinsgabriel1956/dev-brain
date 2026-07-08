---
type: concept
title: "Governança de Código Gerado por IA"
aliases: ["paradoxo da ia no codigo", "governar codigo de ia"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 3
tags: [ia-no-processo-de-engenharia, arquitetura, carreira]
skill: tech-mentor-leadership
status: draft
---

# Governança de Código Gerado por IA

Paradoxo: quanto mais a IA gera código automaticamente, mais uma organização precisa de [[wiki/concepts/engenheiro-vs-programador|engenheiros]] capazes de julgar, revisar e assumir responsabilidade por esse código — não menos.

## O argumento

Ferramentas como Copilot, Cursor e Claude já escrevem código funcional a partir de uma descrição, e tendem a melhorar. Isso comoditiza a tarefa clássica do programador: transformar requisito claro em código funcional. Mas o trabalho do engenheiro — entender se o requisito faz sentido, decidir arquitetura, avaliar trade-offs, governar a complexidade do sistema como um todo — exige contexto, julgamento sobre incerteza e responsabilidade sobre consequências. A IA não faz isso.

> "Sem governança, a IA gerando código é como dar uma metralhadora para quem não sabe mirar."

## Quem perde o emprego, quem não perde

A IA ameaça quem permanece só na camada de execução e não evolui para julgamento e governança. Cria mais demanda por quem pensa, decide e governa o sistema. O autor não trata isso como verdade universal — depende da linguagem, de quão legado é o projeto, e de quão bem a IA já resolve aquele tipo de tarefa especificamente.

## Relação com outros conceitos

- [[wiki/concepts/engenheiro-vs-programador]] — a distinção de mentalidade que determina de que lado desse paradoxo alguém fica
- [[wiki/concepts/complexidade-acidental]] — código gerado sem revisão arquitetural tende a acumular complexidade acidental em volume maior e mais rápido do que código escrito manualmente
- [[wiki/concepts/pensamento-em-producao]] — código gerado ainda precisa sobreviver a produção; a IA não assume esse risco
- [[wiki/concepts/divida-cognitiva]] — falta de governança é o mecanismo pelo qual código gerado vira dívida cognitiva coletiva

## Quando quem gera o ticket não é técnico

[[wiki/sources/atrofia-cognitiva-ia-programacao]] descreve uma falha de governança mais severa que um dev usar IA para resolver seu próprio ticket: alguém **fora do time técnico** conectando o repositório do projeto a uma IA e gerando tickets com detalhamento técnico no backlog — sem nenhum engenheiro tendo formulado ou revisado o problema antes de virar tarefa. Isso quebra a premissa central da governança de código gerado por IA: não há humano exercendo julgamento em nenhum ponto do fluxo, nem na geração do requisito nem na geração do código.

## Vender Vibe Coding Como Produção é Falta de Governança

[[wiki/sources/vibe-coding-limites-maturidade-profissional]] descreve outro caso limite: construir um sistema inteiramente por [[wiki/concepts/vibe-coding|vibe coding]] e vendê-lo como pronto para produção — seguro, moderno, testado — sem nenhuma revisão arquitetural, de segurança ou de contexto de negócio. Isso é falta de governança na ponta de saída (venda ao cliente), não só na ponta de entrada (geração do requisito): o risco recai sobre quem comprou confiando na promessa de qualidade.

## Key Sources

- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
- [[wiki/sources/atrofia-cognitiva-ia-programacao]] — caso limite: pessoa não técnica gerando tickets via IA conectada ao repositório, sem nenhum julgamento de engenharia no fluxo
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — caso limite: vender sistema vibe-coded como pronto para produção sem revisão humana
