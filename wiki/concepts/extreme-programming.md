---
type: concept
title: "Extreme Programming (XP)"
aliases: ["xp", "programação extrema"]
date_created: 2026-08-23
date_updated: 2026-09-04
source_count: 5
tags: [extreme-programming, kent-beck, agile, historia, craftsmanship]
skill: tech-mentor-testing
status: stub
---

# Extreme Programming (XP)

Metodologia ágil de desenvolvimento de software criada por [[wiki/entities/kent-beck]], consolidada durante o recomeço (1996) do projeto [[wiki/entities/c3-project|C3]] na Chrysler. Reúne, de forma coesa pela primeira vez, práticas como pair programming, TDD, refatoração contínua e planning game — muitas das quais já apareciam isoladamente em projetos anteriores de Beck. Formalizada no livro *Extreme Programming Explained* (1999), de Beck, onde também aparece o princípio [[wiki/concepts/yagni]].

## XP não é garantia de sucesso

[[wiki/sources/c3-martin-fowler]] usa o próprio destino do C3 — sucesso inicial em 1997, mas encerramento do novo desenvolvimento em 1999 e reversão parcial ao sistema COBOL legado — como argumento de que a XP "não é garantia de sucesso". O que sustentou a evolução da metodologia depois do fim do C3 foram *outros* projetos que replicaram suas conquistas, não o C3 propriamente dito.

## Adoção séria correlaciona com taxas de defeito muito baixas

[[wiki/sources/very-low-defect-project-martin-fowler]] (2004) mostra o outro lado da moeda da tese acima: apesar de "XP não ser garantia de sucesso", Fowler observa que uma minoria (mas crescente) de times com adoção séria de XP chega a menos de um bug em produção por mês — o [[wiki/concepts/very-low-defect-project|VeryLowDefectProject]]. O contraste é direto: o próprio [[wiki/entities/c3-project|C3]] não sustentou seu sucesso, mas ex-membros do time do C3 produziram, em outro projeto (portal na Chrysler), um dos resultados de qualidade mais fortes já atribuídos à XP — exatamente um bug em todo o ano de 2002. Fowler é cuidadoso para não transformar essa correlação em garantia: os times observados são disciplinados, liderados por gente com anos de XP, e ele não descarta que outros processos cheguem ao mesmo resultado.

## "Unit test" em XP tem dois sinônimos: developer test e programmer test

Fonte primária isolada: [[wiki/sources/unit-test-xunitpatterns]] (verbete de glossário de Gerard Meszaros). Na nomenclatura da XP, **"unit test"** também é chamado de **developer test** ou **programmer test** — sinônimos históricos, não termos com significado distinto. Detalhe de vocabulário nunca antes registrado nesta página, apesar de [[wiki/concepts/tdd]] já documentar o ciclo red-green-refactor que produz exatamente esse tipo de teste.

## Definição de dicionário do glossário xUnitPatterns.com: só três práticas visíveis

Fonte primária isolada: [[wiki/sources/extreme-programming-xunitpatterns]] (verbete de glossário de Gerard Meszaros). A definição mais enxuta já registrada para XP nesta wiki — uma única frase: "uma metodologia ágil de desenvolvimento de software que destaca pair programming, testes unitários automatizados e iterações curtas". Não cita TDD como ciclo, não cita planning game, refatoração contínua nem YAGNI — reforça, por contraste, o quanto o restante desta página (via Fowler) é mais rico que o vocabulário puro de glossário do site.

## Industrial XP (IXP): variante de marca para escalar XP em empresas maiores

Fonte primária isolada: [[wiki/sources/ixp-industrial-xp-xunitpatterns]] (verbete de glossário de Gerard Meszaros, seção References). **Industrial XP (IXP)**, criada por [[wiki/entities/joshua-kerievsky]], é uma variante "de marca" do XP clássico que acrescenta práticas para escalar sua adoção em empresas de maior porte — a fonte cita **Project Chartering** como exemplo. IXP é também o contexto em que Kerievsky cunhou [[wiki/concepts/storytest-driven-development]], termo já registrado nesta wiki, mas que até esta ingestão não tinha uma página própria para IXP nem para seu criador. Ver [[wiki/concepts/industrial-xp]].

## Relação com práticas específicas já documentadas nesta wiki

- [[wiki/concepts/tdd]] — ciclo RED-GREEN-REFACTOR, uma das práticas centrais da XP
- [[wiki/concepts/dois-chapeus-kent-beck]] — metáfora de Beck sobre separar refatoração de mudança de comportamento
- [[wiki/concepts/yagni]] — princípio apresentado no livro fundador da XP
- [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]] — mesmo espírito pragmático da XP aplicado a complexidade de solução
- [[wiki/entities/junit]] — nasceu em 1997 (mesmo ano da entrada em produção do C3), a partir do framework de testes caseiro que Beck já usava no C3; essencial, segundo Fowler, para sustentar a adoção de XP e TDD na indústria

## Ver também

- [[wiki/entities/kent-beck]]
- [[wiki/entities/c3-project]]
- [[wiki/concepts/very-low-defect-project]]

## Key Sources

- [[wiki/sources/c3-martin-fowler]]
- [[wiki/sources/very-low-defect-project-martin-fowler]] — adoção séria de XP correlaciona com taxas de defeito muito baixas, sem ser garantia
- [[wiki/sources/unit-test-xunitpatterns]] — fonte primária dos sinônimos "developer test"/"programmer test" para unit test em XP
- [[wiki/sources/extreme-programming-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição mais genérica do próprio termo "eXtreme Programming"
- [[wiki/sources/ixp-industrial-xp-xunitpatterns]] — verbete de glossário do mesmo site, isolando a definição de Industrial XP (IXP) como variante de escala do XP, criada por Joshua Kerievsky
