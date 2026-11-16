---
type: concept
title: "Usabilidade"
aliases: ["usability", "facilidade de uso", "usável"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 1
tags: [ux, ux-design, usabilidade, heuristicas, padroes, iso-9241]
skill: ux-ui-mentor
status: stub
---

# Usabilidade

O quanto uma interface "permite que as pessoas alcancem **facilmente** os seus objetivos". Na aula, é um termo de [[wiki/concepts/ux-design]] que "muita gente simplesmente não dá a devida importância" ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]).

## Definições

| Origem | Definição |
|---|---|
| Aula | Usuários concluem tarefas "com precisão e velocidade de forma agradável" |
| ISO 9241-11 `[external]` | Eficácia, eficiência e satisfação de usuários especificados, com objetivos especificados, num contexto de uso especificado (https://www.iso.org/standard/63500.html) |
| Nielsen `[external]` | Cinco componentes: aprendizado, eficiência, memorização, erros, satisfação (https://www.nngroup.com/articles/usability-101-introduction-to-usability/) |
| `[skill: ux-ui-mentor]` | O usuário correto completa a tarefa certa, no contexto certo, com eficiência, eficácia e satisfação |

As três batem no núcleo. A aula deixa de fora o **contexto** (quem usa e onde), mas o exemplo dela é justamente sobre isso: o app do auxílio emergencial da [[wiki/entities/caixa-economica-federal]] tinha de servir a um país inteiro, com muita gente de pouca instrução.

## Sinais

- **Quando funciona, não se nota:** "se você não conseguir identificar o que é usabilidade em determinada interface, é porque provavelmente ela tem." Ver [[wiki/concepts/simplicidade-visual]].
- **Quando falta, irrita:** "se você ficou nervoso utilizando determinado sistema", ninguém pensou nela. Outro sinal é precisar de "orientação de terceiros" para usar.

## As três esferas

1. **Usuário:** precisão, velocidade, agrado.
2. **Desenvolvedor:** flow mais fácil e menos implementação desnecessária ([[wiki/concepts/principio-de-pareto|os "20%"]] de funções usadas).
3. **Gerente de projeto:** produtividade do time e aquisição do produto. Produto difícil tende a não ser usado.

## Como se chega lá (boas práticas da aula)

- Heurísticas e [[wiki/concepts/padroes-de-interface|padrões]] já estabelecidos; "não reinventar a roda" ([[wiki/concepts/lei-de-jakob]]).
- Jornadas com [[wiki/concepts/objetivo-da-interface|objetivos]] claros e pouca bifurcação.
- Cores adequadas ([[wiki/concepts/cor-semantica]]), [[wiki/concepts/icones-em-interfaces|ícones]] e confirmações visuais e textuais ([[wiki/concepts/feedback-do-sistema]]).
- Conhecer o projeto, perguntar e testar ([[wiki/concepts/teste-de-usabilidade]]).
- Projetar com propósito e "o menos possível".

## Usabilidade e acessibilidade

A aula usa "acessibilidade" uma vez onde o sentido é usabilidade e deixa a acessibilidade para a aula seguinte. `[skill: ux-ui-mentor]` Os dois se sobrepõem, mas não são a mesma coisa. Acessibilidade se mede pela WCAG (POUR, níveis A/AA/AAA); usabilidade, por tarefa, tempo, erro e satisfação. Avaliação heurística (as 10 de Nielsen) é o método rápido de usabilidade.

## Key Sources

- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]] — definição, auxílio emergencial, três esferas, boas práticas
