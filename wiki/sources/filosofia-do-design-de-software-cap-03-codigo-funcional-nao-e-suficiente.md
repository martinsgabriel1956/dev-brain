---
type: source
title: "A Filosofia do Design de Software — Cap. 3: Código Funcional Não É Suficiente"
aliases: ["philosophy of software design cap 3", "ousterhout capítulo 3", "working code isn't enough", "programação estratégica vs. tática", "código que funciona não basta"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-25
source_count: 0
tags: [design, ousterhout, traducao, programacao-tatica, programacao-estrategica, tech-debt, startups, cultura-de-engenharia, leadership]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 3 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 3.1 a 3.5. O capítulo diz que a decisão de design mais importante é a **mentalidade** com que se programa. A **programação tática** quer que a tarefa funcione o mais rápido possível e aceita pequenas complexidades a cada tarefa. A **estratégica** trata código que funciona como requisito mínimo e tem como objetivo um bom design ([[wiki/concepts/programacao-tatica-vs-estrategica]]). O extremo da tática é o [[wiki/concepts/tornado-tatico]]. A régua é investir **10 a 20%** do tempo de desenvolvimento em design, em pequenas doses contínuas. Pela opinião do autor, sem dado que a sustente, o investimento se paga em 6 a 18 meses. Facebook é o exemplo de cultura tática; Google e VMware, de cultura estratégica. A wiki já conhecia o capítulo pelo [[wiki/sources/filosofia-do-design-de-software-livro-completo]]. Esta leitura de primeira mão corrige uma afirmação: Ousterhout **não** cunha o termo "dívida técnica", só o usa.

## Key Claims

### Introdução e 3.1 Programação tática

**Claim:** Um dos elementos mais importantes do bom design é a mentalidade com que se aborda uma tarefa. A abordagem estratégica produz designs melhores e, no longo prazo, sai **mais barata** que a tática.
**Evidence:** Introdução do capítulo. O argumento de custo, e não só de qualidade, é o que sustenta o resto do capítulo (3.3).
**Confidence:** alta quanto ao texto. O "mais barata" é opinião do autor (ver 3.3).

**Claim:** Na programação tática, o foco é fazer algo funcionar, seja uma funcionalidade ou uma correção. Ela é imediatista: planejar o futuro não é prioridade, e cada pequena complexidade ou gambiarra parece aceitável se acelerar a tarefa atual.
**Evidence:** 3.1, primeiro e segundo parágrafos.
**Confidence:** alta.

**Claim:** É assim que os sistemas ficam complicados. A complexidade é incremental, cada tarefa tática acrescenta algumas pequenas complexidades e, com todo o time programando assim, elas se acumulam rápido.
**Evidence:** 3.1, com remissão explícita ao cap. 2 ([[wiki/concepts/complexidade-incremental]], [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]).
**Confidence:** alta.

**Claim:** O caminho tático se reforça sozinho. Quando os atalhos começam a doer, a próxima funcionalidade parece mais importante que refatorar; os remendos criam mais complexidade, que pede mais remendos; quando a bagunça fica grande, limpar levaria meses e corrigir um ou dois problemas não parece fazer diferença. "Uma vez que você segue pelo caminho tático, é difícil mudar."
**Evidence:** 3.1, quarto e quinto parágrafos. É o mecanismo de saída da 2.4 ("corrigir uma só não faz diferença") transformado em ciclo vicioso.
**Confidence:** alta.

**Claim:** O **tornado tático** é o programador prolífico que entrega muito mais rápido que os outros, mas de forma totalmente tática. A gerência às vezes o trata como herói; os engenheiros que herdam o código dele, não. Os que limpam a bagunça são "os verdadeiros heróis" e parecem mais lentos por causa disso.
**Evidence:** 3.1, último parágrafo. Ver [[wiki/concepts/tornado-tatico]].
**Confidence:** alta quanto ao texto.

### 3.2 Programação estratégica

**Claim:** O primeiro passo para ser um bom designer é perceber que código que funciona não basta. A maior parte do código é escrita estendendo a base existente, então o trabalho mais importante do desenvolvedor é facilitar as extensões futuras. O objetivo é "um excelente design, que por acaso também funciona".
**Evidence:** 3.2, primeiro parágrafo.
**Confidence:** alta.

**Claim:** A programação estratégica exige **mentalidade de investimento**. Os investimentos são de dois tipos. **Proativos:** tentar algumas alternativas de design para cada classe nova e escolher a mais limpa, imaginar como o sistema pode mudar e garantir que o design aguente isso, escrever boa documentação. **Reativos:** quando um erro de design aparecer, não ignorar nem remendar, e sim gastar o tempo para consertá-lo.
**Evidence:** 3.2, terceiro e quarto parágrafos. O proativo antecipa [[wiki/concepts/projetar-duas-vezes]] (cap. 11) e [[wiki/concepts/comentarios-como-ferramenta-de-design]]. O reativo é o que a wiki chama de [[wiki/concepts/refatoracao]] e de [[wiki/concepts/boy-scout-rule]], embora o livro não use nenhum dos dois termos.
**Confidence:** alta quanto ao texto. As equivalências são da wiki.

### 3.3 Quanto investir?

**Claim:** Um investimento inicial gigante, como tentar projetar o sistema inteiro, não funciona: "esse é o método cascata, e sabemos que ele não funciona". O bom design surge aos poucos, com a experiência no sistema. Por isso o melhor é fazer **muitos pequenos investimentos contínuos**.
**Evidence:** 3.3, primeiro parágrafo. Retoma o argumento do cap. 1 ([[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]).
**Confidence:** alta.

**Claim:** A régua é **10 a 20%** do tempo total de desenvolvimento. Os primeiros projetos atrasam nessa proporção, mas em alguns meses o desenvolvimento fica pelo menos 10 a 20% mais rápido que o tático, e a partir daí "seus investimentos se tornam gratuitos". Na mão contrária, quem programa taticamente logo estará pelo menos 10 a 20% mais lento, pelo resto da vida do sistema.
**Evidence:** 3.3, segundo e quarto parágrafos, e a Figura 3.1. A legenda da figura diz que ela é só ilustração qualitativa: o autor não conhece medição sobre o formato das curvas. O único dado de suporte é anedótico: quem já trabalhou numa base degradada diz que ela atrasa o desenvolvimento em pelo menos 20%.
**Confidence:** média. O próprio autor apresenta as cifras como opinião.

**Claim:** "Dívida técnica" é o termo que costuma descrever os problemas da programação tática: pega-se tempo emprestado do futuro e devolve-se mais do que se pegou. Diferente da dívida financeira, a maior parte da dívida técnica nunca é quitada, e se continua pagando para sempre.
**Evidence:** 3.3, quinto parágrafo. O texto diz que o termo "é frequentemente usado", ou seja, Ousterhout o adota, não o cria. A metáfora é de Ward Cunningham, de 1992 `[external, não verificado]`. Ver [[wiki/concepts/tech-debt-como-ferramenta]], que foi corrigida.
**Confidence:** alta quanto ao texto.

**Claim:** O ponto em que a curva estratégica cruza a tática fica, na opinião do autor, entre **6 e 18 meses**. A razão é a memória: depois de alguns meses, os desenvolvedores esquecem o que tinham em mente ao escrever o código, e o código complexo passa a custar caro. O autor diz duas vezes que não tem dados e que o experimento controlado seria difícil.
**Evidence:** 3.3, último parágrafo.
**Confidence:** baixa como fato; alta como registro da opinião do autor.

### 3.4 Startups e investimento

**Claim:** Startups sofrem pressão para lançar rápido e tendem a ser táticas, com a ideia de que, se derem certo, terão dinheiro para contratar engenheiros e arrumar a casa. O autor responde com três argumentos. (1) Depois que a base vira código espaguete, é quase impossível consertá-la, e o custo alto dura a vida inteira do produto ([[wiki/concepts/code-espaguete]]). (2) O retorno do bom design vem rápido, então a tática talvez nem acelere o primeiro lançamento. (3) Os melhores engenheiros se importam com design, uma base ruim espanta esse perfil e a equipe medíocre que sobra degrada ainda mais o sistema.
**Evidence:** 3.4, primeiro a terceiro parágrafos. O argumento (3) é sobre contratação, não sobre código: o design ruim vira problema de recrutamento.
**Confidence:** média. São argumentos de experiência, sem dado. Entram em tensão com a defesa de velocidade de [[wiki/concepts/mvp]] e [[wiki/concepts/lean-startup]] (ver Contradições).

**Claim:** O Facebook é o exemplo de startup tática. O lema "Mova-se rápido e quebre as coisas" e os commits em produção na primeira semana davam autonomia aos engenheiros, mas a base ficou instável, difícil de entender, com poucos comentários e testes. A empresa trocou o lema por "Mova-se rápido com uma infraestrutura sólida". O autor ressalva que o código deles provavelmente não é pior que a média das startups, só mais visível.
**Evidence:** 3.4, quarto a sexto parágrafos. Ver [[wiki/entities/meta]].
**Confidence:** média. É um relato de terceiros sobre o código de outra empresa. O lema de 2014 costuma ser citado como "Move fast with stable infra" `[external, não verificado]`; a diferença para "solid infrastructure" não muda o argumento.

**Claim:** Google e VMware cresceram na mesma época com cultura estratégica, com ênfase em código de qualidade e bom design, e por isso poucas empresas competiam com elas por talento. Conclusão do autor: dá para ter sucesso das duas formas, mas "é muito mais divertido" trabalhar numa empresa que se importa com design.
**Evidence:** 3.4, dois últimos parágrafos. Ver [[wiki/entities/google]]. A conclusão admite que o sucesso comercial não decide a questão, e o argumento final é a qualidade de vida do engenheiro.
**Confidence:** alta quanto ao texto.

### 3.5 Conclusão

**Claim:** Bom design não vem de graça: é investimento contínuo, para que problemas pequenos não virem grandes. O perigo está nos períodos de pressão. Adiar a limpeza "até o aperto acabar" é terreno escorregadio, porque depois de uma crise vem outra, o adiamento fica permanente e a cultura do time escorrega para o tático. Quanto mais se espera, maiores os problemas e mais fácil continuar adiando. O mais eficaz é cada engenheiro fazer pequenos investimentos contínuos.
**Evidence:** 3.5. É a versão de comportamento da "tolerância zero" da 2.4.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **Ousterhout não cunha "dívida técnica".** [[wiki/concepts/tech-debt-como-ferramenta]] dizia que o capítulo "cunha explicitamente o termo". O texto diz o contrário: o termo "é frequentemente usado". A página foi corrigida.
- **"Para sempre" não é ressalva ao quadrante de Fowler.** A mesma página dizia que se paga para sempre "se a decisão foi tática pura (equivalente ao quadrante Imprudente)". O livro não faz essa ressalva: diz que **a maior parte** da dívida técnica nunca é quitada, sem separar a deliberada da imprudente. Isso deixa Ousterhout mais restritivo que Fowler também no cap. 3, como já se tinha visto no cap. 2. A página foi ajustada.
- **Tensão com MVP e startups.** A 3.4 diz que a tática talvez nem acelere o primeiro lançamento. [[wiki/concepts/mvp]], [[wiki/concepts/lean-startup]] e o "build for rebuilding" de [[wiki/concepts/tech-debt-como-ferramenta]] defendem velocidade e descarte. As duas posições se conciliam em parte: o MVP reduz **escopo** (o que construir) e a programação tática reduz **cuidado** (como construir). Um MVP feito de forma estratégica é possível. A conciliação é da wiki, não do livro.
- **Provável lapso no último parágrafo da 3.3.** A tradução diz que os custos extras "compensam rapidamente qualquer ganho inicial da programação **estratégica**". Pela lógica do parágrafo, e pela Figura 3.1, o ganho inicial é da **tática**. A N.T. diz que o original escreve *strategic* e que a tradução manteve a literalidade. Não verifiquei o original. Ao citar, ler como "tática".
- **"Código funcional" no título.** O título traduz *Working Code Isn't Enough* como "Código Funcional Não É Suficiente". "Funcional" pode ser lido como programação funcional. O corpo usa "código que funciona", que é mais claro. Sugestão: "Código que funciona não basta".
- **10–20% e a folga de 20%.** A régua de Ousterhout bate com a [[wiki/concepts/folga-de-capacidade-slack]] de ~20% de [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]], mas o mecanismo é outro: Ousterhout embute o investimento em cada tarefa; a folga é capacidade reservada no time. Convergência da wiki.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/entities/meta]]
- [[wiki/entities/google]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]
- [[wiki/concepts/programacao-tatica-vs-estrategica]] (nova)
- [[wiki/concepts/tornado-tatico]] (nova)
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/complexidade-incremental]]
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]
- [[wiki/concepts/projetar-duas-vezes]]
- [[wiki/concepts/refatoracao]]
- [[wiki/concepts/boy-scout-rule]]
- [[wiki/concepts/code-espaguete]]
- [[wiki/concepts/comentarios-como-ferramenta-de-design]]
- [[wiki/concepts/folga-de-capacidade-slack]]
- [[wiki/concepts/mvp]]

## Open Questions

- O original diz mesmo "*initial gains from strategic programming*" no último parágrafo da 3.3? Se disser, é errata do livro. Conferir no epub ou na errata do autor.
- O livro não diz como defender os 10–20% para uma gestão que mede entrega de funcionalidades. A wiki tem respostas parciais em [[wiki/concepts/refatoracao]] (embutir sem pedir permissão) e em [[wiki/concepts/tech-debt-como-ferramenta]] (expor o custo em horas).
- A 3.4 trata contratação como consequência do design. Existe evidência, além da anedota de Google e VMware, de que a qualidade da base afeta o recrutamento?
- O cap. 4 (módulos profundos) é o próximo da tradução. A wiki já o tem pelo livro completo e por [[wiki/concepts/modulo-profundo]]. Respondida: ingerido em [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]].

## Raw Quotes

> "Uma vez que você segue pelo caminho tático, é difícil mudar."

> "Seu objetivo principal deve ser produzir um excelente design, que por acaso também funciona."

> "Diferente da dívida financeira, a maior parte da dívida técnica nunca é totalmente quitada: você continuará pagando e pagando para sempre."
