---
type: source
title: "Very Low Defect Project (Martin Fowler)"
aliases: ["very low defect project bliki", "projeto de taxa de defeito muito baixa"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_file: /home/nemomartins/Documentos/new/dev-study/raw/very-low-defect-project-martin-fowler.md
source_url: "https://martinfowler.com/bliki/VeryLowDefectProject.html"
author: "Martin Fowler"
date_published: 2004-01-24
date_ingested: 2026-08-23
source_count: 0
tags: [extreme-programming, kent-beck, qualidade, defeitos, xp, thoughtworks]
skill: tech-mentor-testing
status: stable
---

# Very Low Defect Project (Martin Fowler)

## TL;DR

Bliki curto (jan/2004) em que Fowler observa uma tendência pequena mas crescente entre times de [[wiki/concepts/extreme-programming|Extreme Programming]]: taxas de defeito muito baixas, definidas como menos de um bug em produção por mês. Ele relata quatro casos — uma fabricante de máquinas de classificação de alimentos (relatado por [[wiki/entities/kent-beck]]), um time de ex-colegas do [[wiki/entities/c3-project|C3]] construindo software de portal na Chrysler (exatamente um bug registrado em 2002, lançando versões novas a cada uma ou duas semanas), uma empresa de software não nomeada com sistemas legados e novos, e projetos-candidato na [[wiki/entities/thoughtworks]]. Fowler encerra com ressalvas explícitas: só uma minoria dos projetos chega lá, os times observados são disciplinados e liderados por gente com um ou dois anos de XP, e ele evita afirmar que XP garante esse resultado ou que outros processos não conseguiriam o mesmo.

## Key Claims

- **Definição do termo**: "Very Low Defect Project" = menos de um bug em produção por mês.
- **Caso 1 — fabricante de máquinas de classificação de alimentos**: relatado por [[wiki/entities/kent-beck]] a Fowler. Sistema em Smalltalk com esteiras, câmeras e sensores. Tinha ~100 bugs abertos simultaneamente antes de adotar XP; depois da adoção, a taxa caiu para cerca de um bug a cada dois meses.
- **Caso 2 — software de portal na Chrysler, por ex-colegas do C3**: Fowler identifica o time como "vários dos meus velhos amigos do C3" ([[wiki/entities/c3-project]]). Começaram com a taxa "chocante" de um defeito por mês; durante 2002 registraram **exatamente um bug** contra o sistema, enquanto lançavam uma nova versão a cada uma ou duas semanas — cadência de entrega frequente na linha de [[wiki/concepts/ci-cd]] (o bliki original carrega a tag "continuous delivery").
- **Caso 3 — empresa de software não nomeada**: fez uma grande adoção de XP; trabalho com sistemas legados grandes continua desafiador, mas alguns desenvolvimentos novos rodam com menos de um bug por mês. Um deles teve a certificação governamental pré-instalação reduzida de semanas para dias.
- **Caso 4 — [[wiki/entities/thoughtworks]]**: Fowler nota que a empresa também está vendo esse padrão em alguns de seus "projetos-candidato" a very-low-defect, ainda cedo para conclusões.
- **Ressalva central 1 — minoria e disciplina**: só uma minoria dos projetos chega a essas taxas; os times observados são "bastante disciplinados" e liderados por pessoas com um ou dois anos de experiência em XP.
- **Ressalva central 2 — correlação, não garantia**: Fowler conclui que essas taxas de bug são alcançáveis no desenvolvimento de software e que os times que chegam lá consideram XP uma ferramenta importante — mas explicitamente não afirma que adotar XP garante o resultado, nem que outros processos sejam incapazes de alcançar o mesmo.
- **Padrão mais amplo**: mesmo fora dos casos sub-um-bug-por-mês, Fowler diz ter ouvido "muitos relatos" de quedas significativas na taxa de defeitos em adoções sérias de XP.

## Entities

[[wiki/entities/martin-fowler]] · [[wiki/entities/kent-beck]] · [[wiki/entities/c3-project]] · [[wiki/entities/thoughtworks]]

## Concepts

[[wiki/concepts/very-low-defect-project]] · [[wiki/concepts/extreme-programming]] · [[wiki/concepts/tdd]]

## Conexão com c3-martin-fowler

[[wiki/sources/c3-martin-fowler]] (publicado sete meses depois, em ago/2004) já mencionava de passagem que "vários membros da equipe do C3 seguiram para outros projetos de XP, um dos quais alcançou reconhecimento por manter um 'VeryLowDefectProject'" — e registrava como open question que "o time e o projeto específico... não são nomeados". Esta fonte, cronologicamente anterior, **é** esse relato: o projeto é o software de portal na Chrysler construído por ex-colegas de C3 de Fowler, com o resultado concreto de um bug em todo o ano de 2002. A open question em c3-martin-fowler fica resolvida na medida do que Fowler publicou — ele não nomeia pessoas nem a empresa cliente, só descreve o time e o resultado.

## Open Questions

- A empresa de software do Caso 3 (sistemas legados + novos, certificação governamental) não é nomeada — Fowler não dá detalhes suficientes para identificá-la.
- Fowler não detalha quais práticas específicas de XP cada time seguia à risca (pair programming, TDD, planning game) — o artigo fica no nível do resultado (taxa de bug), não do mecanismo causal.
- Não fica claro se "durante 2002" cobre o ano calendário inteiro ou um período menor descrito de forma aproximada.

## Raw Quotes

*(Tradução completa em `raw/very-low-defect-project-martin-fowler.md`; para o texto exato em inglês, ver `source_url`.)*
