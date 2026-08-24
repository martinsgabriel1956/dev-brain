---
type: concept
title: "Very Low Defect Project"
aliases: ["projeto de taxa de defeito muito baixa", "very low defect rate"]
date_created: 2026-08-23
date_updated: 2026-08-23
source_count: 1
tags: [extreme-programming, kent-beck, qualidade, defeitos, xp]
skill: tech-mentor-testing
status: stub
---

# Very Low Defect Project

Termo cunhado por [[wiki/entities/martin-fowler]] em bliki de janeiro de 2004 ([[wiki/sources/very-low-defect-project-martin-fowler]]) para descrever times de [[wiki/concepts/extreme-programming|Extreme Programming]] que atingem **menos de um bug em produção por mês**. Fowler observou o padrão como "pequeno mas crescente" em quatro casos concretos, e não como uma promessa automática da metodologia.

## Casos observados

- **Fabricante de máquinas de classificação de alimentos** — relatado por [[wiki/entities/kent-beck]]. Caiu de ~100 bugs abertos simultaneamente para cerca de um a cada dois meses após adotar XP.
- **Ex-colegas de [[wiki/entities/c3-project|C3]] construindo software de portal na Chrysler** — de um defeito por mês para exatamente um bug em todo o ano de 2002, lançando uma nova versão a cada uma ou duas semanas.
- **Empresa de software não nomeada** com sistemas legados e novos — alguns projetos novos abaixo de um bug/mês; um deles reduziu a certificação governamental pré-instalação de semanas para dias.
- **[[wiki/entities/thoughtworks]]** — alguns projetos-candidato mostrando o mesmo padrão, ainda cedo para conclusões segundo Fowler.

## Correlação, não garantia

Fowler é explícito nas ressalvas: só uma minoria dos projetos XP chega a essas taxas, os times observados são disciplinados e liderados por gente com um ou dois anos de experiência em XP, e ele evita duas afirmações fortes — que adotar XP garante o resultado, ou que outros processos não conseguiriam o mesmo. A conclusão dele é mais modesta: taxas de bug muito baixas são *alcançáveis* no desenvolvimento de software, e os times que chegam lá tendem a considerar XP uma ferramenta importante para isso.

## Relação com C3 e a tese "XP não é garantia de sucesso"

[[wiki/sources/c3-martin-fowler]] (publicado sete meses depois desta fonte) já citava, de passagem e sem nomear o time, que "vários ex-membros do C3 seguiram para outros projetos de XP, um dos quais alcançou reconhecimento por manter um VeryLowDefectProject" — essa referência não identificada é justamente o caso do time de portal na Chrysler documentado aqui. As duas fontes juntas mostram uma tensão interessante: [[wiki/entities/c3-project|C3]] em si não sustentou seu próprio sucesso (encerrado em 1999, parcialmente revertido a COBOL), mas parte de seus ex-membros produziu, em outro projeto, um dos resultados de qualidade mais fortes já atribuídos à XP. Ver [[wiki/concepts/extreme-programming]] para a discussão de "XP não é garantia de sucesso" à luz desse contraste.

## Ver também

- [[wiki/concepts/tdd]] — prática central da XP frequentemente citada como mecanismo por trás de taxas de defeito mais baixas, embora esta fonte não detalhe a causalidade prática-a-prática
- [[wiki/entities/kent-beck]]
- [[wiki/entities/martin-fowler]]

## Key Sources

- [[wiki/sources/very-low-defect-project-martin-fowler]]
