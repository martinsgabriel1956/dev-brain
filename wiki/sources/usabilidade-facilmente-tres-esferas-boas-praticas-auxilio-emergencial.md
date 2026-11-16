---
type: source
title: "Usabilidade (FrontPUSH, interfaces web): alcançar facilmente os objetivos, as três esferas e as boas práticas"
aliases: ["aula de usabilidade", "usabilidade FrontPUSH", "auxílio emergencial Caixa", "usabilidade nas três esferas"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ux, ux-design, usabilidade, padroes, heuristicas, apple, jornada, icones, cor, feedback, teste-de-usabilidade, simplicidade]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Usabilidade (FrontPUSH, interfaces web): alcançar facilmente os objetivos, as três esferas e as boas práticas

## TL;DR

Aula 2 do módulo de **interfaces web** do [[wiki/entities/frontpush]] (cerca de 13 min, slide com o logo "W7"). Ela abre o "pilar de pesquisa", a parte teórica antes da prática. Ele define [[wiki/concepts/usabilidade]] como o que "permite que as pessoas alcancem **FACILMENTE** os seus objetivos". Se você não percebe a usabilidade, provavelmente ela existe; se ficou nervoso usando o sistema, faltou. O exemplo é o app do auxílio emergencial da [[wiki/entities/caixa-economica-federal]] na pandemia: público de baixa renda e pouca instrução, e o meme de que a Caixa levou "a mesmíssima experiência" da fila física para o virtual. A usabilidade vale em **três esferas**. Para o **usuário**, concluir tarefas com precisão, velocidade e de forma agradável. Para o **dev**, evitar funções que ninguém usa ("usa-se em torno de 20%"). Para o **gerente**, garantir produtividade e a aquisição do produto. As boas práticas são usar heurísticas e [[wiki/concepts/padroes-de-interface|patterns]] já estabelecidos, com o site da [[wiki/entities/apple]] como exemplo: menu fixo no topo, seções repetidas e ícones no submenu. "Literalmente não reinventar a roda" ([[wiki/concepts/lei-de-jakob]]). Completam a lista jornadas sem bifurcação, cores e ícones adequados, confirmações visuais e textuais, conhecer o projeto e fazer perguntas ([[wiki/concepts/teste-de-usabilidade]]), e projetar com propósito, "o menos possível". Próxima aula: acessibilidade.

## Key Claims

### Definição

- **"Permite que as pessoas alcancem facilmente os seus objetivos"**, com "facilmente" em caixa alta no slide. "Um design cuidadoso, elaborado, que deixa o usuário feliz e imerso na interface." Ver [[wiki/concepts/usabilidade]] e [[wiki/concepts/objetivo-da-interface]].
- **Usabilidade boa não se nota:** "se você não conseguir identificar o que é usabilidade em determinada interface, é porque provavelmente ela tem." Ver [[wiki/concepts/simplicidade-visual]].
- **O teste do nervoso:** "se você ficou nervoso utilizando determinado sistema, provavelmente não teve um profissional que pensasse nessa questão da usabilidade."
- **É termo de UX:** "um termo mais aplicado ao UX Design", "importantíssimo", e "muita gente simplesmente não dá a devida importância". Ver [[wiki/concepts/ux-design]].

### Exemplo: auxílio emergencial da Caixa

- **O público:** trabalhadores informais, MEIs, autônomos e desempregados afetados pela pandemia, "talvez" de média ou baixa renda e com "nível de instrução [...] mais baixo". Ver [[wiki/entities/caixa-economica-federal]].
- **O que a interface precisa:** "ser literalmente claro nos seus objetivos, precisa ser fácil, precisa ser informativo", porque "é o Brasil inteiro" que vai usar.
- **O resultado virou meme:** "a Caixa conseguiu trazer a mesmíssima experiência que a gente tem no físico para o virtual", ou seja, "ficar horas na fila e não ter o seu problema resolvido". Outro sintoma: "pessoas que precisam de orientação de terceiros para poder utilizar da interface".
- **O designer projeta para o outro:** "você sabe o que você implementou porque você que está criando", e o usuário é outra pessoa. "Por isso que são feitos testes de usabilidade." Ver [[wiki/concepts/teste-de-usabilidade]].

### Usabilidade nas três esferas

- **Usuários:** "concluir as tarefas com precisão e velocidade de forma agradável". É "o conceito inicial de usabilidade".
- **Desenvolvedores:** "facilitar o flow e evitar implementações desnecessárias". O exemplo é o programa de gestão "com N funções" em que "usa-se em torno de 20% das funções implementadas". A saída é projetar só "aquilo que é realmente útil com base em testes". Ver [[wiki/concepts/principio-de-pareto]] e [[wiki/concepts/simplicidade-visual]].
- **Gerentes de projeto:** "garantir produtividade ao time" sem implementar o que "às vezes está na sua mente, mas não necessariamente o usuário vai de fato utilizar". E a **aquisição de produtos**: "uma vez que o produto não tem uma boa usabilidade, a tendência dele não ser usado é muito grande."

### Boas práticas

- **"Um dos pilares para você construir qualquer coisa"**, e a resposta para quem manda uma interface perguntando "o que você acha?".
- **Heurísticas e patterns:** "a usabilidade se dá muito, muito, muito pelo bom uso de boas heurísticas, de patterns, de padrões que já estão bem estabelecidos no mercado." Ver [[wiki/concepts/padroes-de-interface]].
- **Apple, menu:** horizontal, no topo, fixo, com todos os produtos, "que é justamente onde você procura. Isso aqui é um padrão". "Não fazer menus mirabolantes e permanecer no padrão." Ver [[wiki/entities/apple]].
- **Por que padrões funcionam:** "as empresas já trabalharam para poder instalar esses padrões na sua cabeça". "Quanto mais você utilizar padrões que já são bem estabelecidos, [...] testados, [...] comprovados no mercado, melhor será o quesito usabilidade." Ver [[wiki/concepts/lei-de-jakob]].
- **Apple, seções:** ilustração, "uma headline maior, uma headline segunda com a hierarquia de texto" e um link, repetido em todos os produtos. "Mesma coisa, olha só, mesma coisa." Ver [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/consistencia-visual]].
- **Apple, submenu do iPhone com ícones:** "por mais que eu não saiba ler, eu sei que esse aqui é um celular". Dois aparelhos lado a lado sugerem comparar. "Os ícones transmitem muito e também ajudam no quesito usabilidade." Ver [[wiki/concepts/icones-em-interfaces]].
- **"Literalmente não reinventar a roda."**
- **Jornadas com objetivos claros, "sem muita bifurcação":** num e-commerce, "muitos links, muitas coisas na jornada" fazem o usuário "se perder". Ver [[wiki/concepts/objetivo-da-interface]].
- **Cores, ícones e confirmações:** "uso adequado das cores" (a teoria das cores de aulas anteriores, ver [[wiki/concepts/cor-semantica]]); ícones para "melhor passar determinada informação"; "confirmações visuais e textuais sempre" ([[wiki/concepts/feedback-do-sistema]]).
- **Módulo futuro:** "UX e heurísticas", "um dos módulos que também eu pretendo falar".

### As regrinhas

- **"Tente conhecer o projeto, faça perguntas":** "você não vai saber de tudo", vai descobrir "conversando com outras pessoas, [...] fazendo teste de usabilidade". "Não é uma receita de bolo, mas tem algumas boas práticas e tem guias."
- **"Sempre projete a interface com propósito":** "não saia colocando coisas mirabolantes que você tirou da sua cabeça", "sempre use o menos possível". "Não necessariamente uma interface muito carregada [...] com muitas funções é necessariamente boa para se utilizar." Ver [[wiki/concepts/simplicidade-visual]].

## Entities

- [[wiki/entities/nasser]]: autor (inferido). Na legenda, "para quem tem sempre aquela dificuldade nascer, eu não estou conseguindo" foi lido como "Násser, eu não estou conseguindo", a fala de aluno que ele imita. Somam-se o arquivo na pasta FrontPush, o logo "W7" do slide e o módulo de interfaces web já citado na aula prática de botões.
- [[wiki/entities/frontpush]]: curso; aula 2 do módulo de interfaces web.
- [[wiki/entities/caixa-economica-federal]] (novo): app do auxílio emergencial como contraexemplo.
- [[wiki/entities/apple]]: site como exemplo de padrões (menu, seções, ícones).

## Concepts

- [[wiki/concepts/usabilidade]] (novo)
- [[wiki/concepts/teste-de-usabilidade]] (novo)
- [[wiki/concepts/ux-design]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/objetivo-da-interface]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/principio-de-pareto]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/cor-semantica]]
- [[wiki/concepts/feedback-do-sistema]]

## Tensões com a wiki

- **"Garantir acessibilidade" no lugar de usabilidade.** Sobre o menu da Apple, ele diz que seguir o padrão "é uma forma de a gente garantir acessibilidade" e conclui com "melhor será o quesito usabilidade". Pelo contexto, a palavra certa é usabilidade. A próxima aula separa os dois termos. `[skill: ux-ui-mentor]` Acessibilidade é a WCAG e os princípios POUR (perceptível, operável, compreensível, robusto). Usabilidade é eficácia, eficiência e satisfação. Uma interface pode ser usável para a maioria e inacessível para quem usa leitor de tela.
- **Definição contra a ISO e a NN/g.** "Precisão e velocidade de forma agradável" casa com a ISO 9241-11: eficácia, eficiência e satisfação "num contexto de uso especificado" `[external]` https://www.iso.org/standard/63500.html. A aula deixa de fora "usuários especificados" e o contexto, que o exemplo da Caixa mostra na prática (o público define o que é "fácil"). Jakob Nielsen dá cinco componentes: aprendizado, eficiência, memorização, erros e satisfação `[external]` https://www.nngroup.com/articles/usability-101-introduction-to-usability/. Erros e memorização não aparecem na aula.
- **"20% das funções" de novo.** É o mesmo número de [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]], de novo sem fonte. `[external]` O número costuma vir do Standish Group (Jim Johnson, XP 2002): "64% das funcionalidades raramente ou nunca usadas". A metodologia nunca foi publicada por inteiro e o dado vem de poucos sistemas internos. Confiança baixa como lei geral.
- **"Não reinventar a roda" contra "padrão não é regra".** [[wiki/concepts/padroes-de-interface]] registra que padrão não é regra. Aqui o tom é mais forte, mas a aula não proíbe exceções. Sem conflito real.

## Open Questions

- **"Três pilares":** só o "pilar de pesquisa" é nomeado. Os outros dois devem estar na aula 1 do módulo de interfaces web, que não foi ingerida.
- **"Três regrinhas, aliás duas":** o slide repete "Projete a interface com propósito" duas vezes; a fala corrige para duas regras.
- **"Um exemplo legal que eu achei irreal":** mantido literal. Talvez "real" (ele chamou o exemplo de "aplicado na nossa realidade"); ambíguo.
- **Data:** "nesse momento de pandemia que estamos passando atualmente" e o auxílio emergencial `[external]` (Lei 13.982, abril de 2020) põem a gravação entre 2020 e 2021. `date_published` vazio.
- **Testes de usabilidade "mais à frente"** e o módulo "UX e heurísticas": prometidos, não ingeridos.

## Raw Quotes

> "Se você não conseguir identificar o que é usabilidade em determinada interface, é porque provavelmente ela tem."

> "A Caixa conseguiu trazer a mesmíssima experiência que a gente tem no físico para o virtual."

> "Então é literalmente não reinventar a roda, tá bom?"

## Ver também

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]: a aula de patterns do módulo de UI Design; busca no menu do topo
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]: propósito, simplicidade e os "20% das funcionalidades"
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: o site da Apple pela ótica dos links
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: a última aula do módulo de UI Design, que já cita o style guide de interfaces web
