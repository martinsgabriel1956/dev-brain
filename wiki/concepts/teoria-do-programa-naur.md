---
type: concept
title: "Teoria do Programa (Peter Naur)"
aliases: ["programming as theory building", "theory of programs", "programa como teoria", "teoria na cabeça do dev"]
date_created: 2026-07-16
date_updated: 2026-08-03
source_count: 2
tags: [peter-naur, teoria-do-programa, divida-cognitiva, entendimento-compartilhado, engenharia-de-software]
skill: tech-mentor-leadership
status: stable
---

# Teoria do Programa (Peter Naur)

Ideia formulada por Peter Naur (1985, *"Programming as Theory Building"*): **um programa não é o código-fonte nem a documentação — é uma teoria que vive na mente de quem o desenvolveu**, abrangendo o que o programa faz e como ele pode evoluir.

## O que isso implica

Código-fonte e documentação são *representações* da teoria, não a teoria em si. Alguém pode ler o código inteiro de um sistema, entender cada linha isoladamente, e ainda assim não possuir a teoria — não saber explicar por que aquela decisão de design foi tomada, ou como o sistema deveria evoluir diante de um requisito novo.

Essa teoria, na prática, **fragmenta-se entre várias pessoas** dentro de um time — raramente reside inteira numa única cabeça, o que já torna sua perda um risco coletivo mesmo sem qualquer IA envolvida no processo.

## Por que isso importa mais na era da IA generativa/agêntica

Um agente de IA pode gerar código sintaticamente correto e até compreensível linha a linha — os testes passam, o PR parece bom — sem que nenhum humano do time tenha, de fato, construído a teoria por trás daquela mudança: por que essa abordagem, e não outra; como essa peça se encaixa nas demais; o que quebra se um requisito mudar amanhã. A velocidade de geração passa a superar a velocidade humana de internalizar a teoria — esse descompasso é exatamente o mecanismo descrito por [[wiki/concepts/divida-cognitiva]].

## Diagnóstico prático: dívida técnica parece dívida cognitiva

Um time pode travar sem conseguir fazer mudanças simples e atribuir isso a "dívida técnica" (código ruim), quando o problema real é que a teoria do programa nunca existiu de forma compartilhada — ninguém consegue explicar por que certas decisões foram tomadas ou como as partes deveriam funcionar juntas. O sintoma observável (time travado) é o mesmo; o diagnóstico e o remédio são diferentes: refatorar código não resolve ausência de teoria compartilhada — reconstruir entendimento via code review e documentação do "porquê" resolve.

## Relação com outros conceitos

- [[wiki/concepts/divida-cognitiva]] — a teoria do programa é o fundamento teórico (1985) sobre o qual "cognitive debt" (2026) foi construído: dívida cognitiva é, na prática, a teoria do programa nunca tendo sido formada ou tendo se perdido
- [[wiki/concepts/comprehension-debt]] — foco complementar: erosão *individual* da capacidade de entender o próprio código, enquanto a teoria do programa é sobre entendimento *coletivo/compartilhado*
- [[wiki/concepts/code-review]] — code review é o mecanismo prático mais citado para reconstruir e propagar a teoria entre membros do time
- [[wiki/entities/peter-naur]] — autor da teoria

## Segunda Fonte Independente: Base Filosófica da Escola "Na Unha"

[[wiki/sources/cinco-escolas-programacao-com-ia]] chega à mesma tese de Naur de forma independente, fora do contexto de dívida cognitiva de time: usa "programa é resíduo, teoria é o que importa" como fundamento filosófico da Escola 3 ("na unha", sem IA) dentro de uma taxonomia de cinco posições sobre programação com IA — ver [[wiki/concepts/escolas-de-programacao-com-ia]]. Observação adicional dessa fonte: Naur morreu em 2016, antes do boom de LLMs agênticos, e nunca teve a chance de se posicionar sobre agentes — ao contrário de [[wiki/entities/dhh]] e [[wiki/entities/antirez]], que defenderam publicamente a mesma posição ("fazer tudo na unha") e depois migraram para delegação alta a agentes, deixando a Escola 3 sem defensores contemporâneos consistentes.

## Key Sources

- [[wiki/sources/cognitive-debt-margaret-storey]]
- [[wiki/sources/cinco-escolas-programacao-com-ia]] — segunda fonte independente, aplicada ao debate de "escolas de programação com IA" em vez de dívida cognitiva de time
