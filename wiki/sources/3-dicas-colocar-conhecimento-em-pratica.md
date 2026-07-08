---
type: source
title: "3 Dicas para Colocar Conhecimento em Prática no Trabalho"
aliases: ["dicas prática no trabalho", "andré casciotti próximo nível", "não peça permissão vai lá e faz"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [carreira, aprendizado, mentoria, produtividade, autonomia, arquitetura]
skill: tech-mentor-leadership
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/3-dicas-para-colocar-conhecimento-em-pratica-no-trabalho.md"
source_url: ""
author: "André Casciotti (canal Próximo Nível)"
date_published: ""
date_ingested: "2026-07-03"
---

## TL;DR

Vídeo argumenta que a maioria dos devs "entope de teoria" (cursos, livros, vídeos) sem nunca praticar em contexto real, e que a prática de curso — por ser deliberadamente simplificada — não substitui a prática no ambiente real de trabalho, imperfeito e desfavorável por natureza. Três dicas para reverter isso: (1) não tentar aplicar tudo de uma vez — mudanças grandes geram barreiras grandes, separe em partes pequenas e coesas que gerem valor real; (2) criar pequenas automações pessoais, fora da infraestrutura e da pressão da empresa, como veículo de baixo risco para praticar tecnologias novas; (3) não pedir permissão — a empresa não vai autorizar iniciativa que não vê retorno financeiro claro, então pratique por conta própria, assuma o risco e não espere reconhecimento automático.

---

## Reivindicações Principais

**Claim:** A maioria dos devs consome informação (cursos, livros, vídeos) sem nunca praticar, e isso não converte conhecimento em habilidade.
**Evidência:** Analogia com capacidade limitada de memória ("é tipo um HD"); comparação histórica entre a escassez de material nos anos 2000 (o autor começou nessa época) e a abundância de hoje, que paradoxalmente aumentou o consumo passivo em vez da prática.
**Confiança:** Média-alta — plausível e alinhada com [[wiki/concepts/aprendizado-passivo]] e [[wiki/concepts/pratica-deliberada]], mas apresentada como observação empírica do autor, não como estudo citado.

**Claim:** A prática feita dentro de um curso tem valor bem menor que a prática no mundo real, porque cursos precisam simplificar por razões didáticas — código bem dividido, boa arquitetura, ausência de restrições de prazo/infraestrutura/política interna.
**Evidência:** Contraste descritivo entre "solution de curso" (bem estruturada) e código real ("10 arquivos, 300 mil linhas, mexido por 300 pessoas ao longo do tempo").
**Confiança:** Alta — argumento consistente com o próprio conceito de [[wiki/concepts/zona-de-desconforto-da-aprendizagem]] (ambiente desfavorável favorece o aprendizado) e com a distinção estrutural entre exercício de curso e codebase real.

**Claim:** Mudanças grandes (ex: migrar monólito para microsserviços, ou impor um framework ágil inteiro) geram barreira de implementação proporcional ao tamanho — demoram mais, são mais complexas e exigem argumento maior para convencer as pessoas. Por isso, quem não tem autoridade formal (CTO, diretor, dono) deveria separar mudanças em partes pequenas e coesas.
**Evidência:** Raciocínio por analogia com o princípio de granularidade da arquitetura de software; relato pessoal do autor como "dev que queria mudar tudo" no início da carreira.
**Confiança:** Alta — coerente com [[wiki/concepts/coesao]] e com o próprio raciocínio de engenharia de sistemas (quanto mais granular, mais simples de manter/adotar).

**Claim:** Pequenas automações pessoais (web scrapers, geradores de relatório, importadores de dados) rodando na própria máquina do dev, fora da infraestrutura da empresa, são um veículo eficiente para praticar tecnologia nova, porque removem a pressão de entrega e a burocracia de aprovação.
**Evidência:** Exemplo pessoal do autor: um extrator de logs próprio, reescrito três vezes em linguagens diferentes (incluindo F#, Elixir, Blazor) só para praticar, sem depender de infraestrutura da empresa.
**Confiança:** Alta — anedótico mas coerente com [[wiki/concepts/pratica-deliberada]] (prática no limite da competência, com liberdade de errar).

**Claim:** A empresa não se importa com a evolução do dev como pessoa — ela paga para ele ajudar a gerar mais dinheiro; por isso ninguém vai autorizar iniciativa que não tenha retorno financeiro óbvio, e o dev que quer praticar algo novo não deve esperar aprovação — deve fazer por conta própria, assumindo o risco caso dê errado, e sem esperar reconhecimento automático caso dê certo.
**Evidência:** Argumento normativo/observacional do autor, sem estudo citado; reforçado por analogia de que o próprio dev também estuda em primeiro lugar por interesse próprio (salário, prestígio), não por altruísmo com a empresa.
**Confiança:** Média — plausível como generalização de mercado, mas é opinião/observação de carreira, não dado verificável. Vale notar a tensão que essa recomendação cria com o escopo formal de entrega (ver seção de contradições abaixo).

**Claim:** Reserve 20 minutos por dia (ou 10, se suficiente) fora do expediente para praticar — não é necessário parar o trabalho ou dedicar semanas inteiras; constância importa mais que volume.
**Evidência:** Recomendação prática do autor baseada na própria rotina.
**Confiança:** Média-alta — coerente com o princípio geral de que consistência supera intensidade esporádica, já presente em [[wiki/concepts/pratica-deliberada]] (teto cognitivo diário).

---

## Entidades

- Autor do vídeo, canal "Próximo Nível" → [[wiki/entities/andre-casciotti]] (novo)

## Conceitos

- [[wiki/concepts/pratica-deliberada]]
- [[wiki/concepts/aprendizado-passivo]]
- [[wiki/concepts/aprender-a-aprender]]
- [[wiki/concepts/autonomia-responsabilidade]]
- [[wiki/concepts/coesao]]
- [[wiki/concepts/cargo-cult-tecnologico]]
- [[wiki/concepts/zona-de-desconforto-da-aprendizagem]]
- [[wiki/concepts/granularidade-de-mudanca]] (novo)
- [[wiki/concepts/automacao-pessoal-para-aprender]] (novo)

## Questões em Aberto

- O autor não cita nenhum estudo para a afirmação central de que "a maioria dos devs estuda do jeito errado" — é observação de mercado, não dado. Tratar como opinião experiente, não fato verificado.
- Não fica claro qual o limiar entre "automação pessoal de baixo risco" (dica 2) e "mudança arriscada assumida sem permissão" (dica 3) — o vídeo trata as duas dicas como complementares, mas na prática dica 2 é sempre fora do escopo formal de trabalho (roda na própria máquina), enquanto dica 3 fala em aplicar mudanças reais no sistema da empresa sem autorização prévia, o que é um risco de escopo bem maior.

## Contradições com a Wiki

Tensão parcial (não uma contradição direta) com [[wiki/concepts/autonomia-responsabilidade]], que documenta — a partir de [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]] — a recomendação de **não criar tarefas fora do escopo pedido** e alinhar prioridade com o PO antes de abrir PR, especialmente nos primeiros meses de carreira. Esta fonte recomenda o oposto na Dica 3 ("não peça permissão, vai lá e faz"). A reconciliação: os contextos são diferentes — a fonte de code review fala de trabalho formal dentro do sprint/escopo da equipe; esta fonte fala majoritariamente de automações pessoais rodando na própria máquina do dev, fora do pipeline de entrega, e reconhece explicitamente que, quando a iniciativa aplicada tem risco real ao produto ("mudar uma tecnologia", "fazer uma mudança agressiva pro contexto do negócio"), quem assume a decisão deve também assumir sozinho a responsabilidade se der errado. Ainda assim, a fonte deixa a fronteira entre os dois cenários pouco definida — registrado acima como questão em aberto.

Reforça, sem contradição, o argumento central de [[wiki/concepts/cargo-cult-tecnologico]] e [[wiki/concepts/decisao-terceirizada]] — de que decisões técnicas devem ser motivadas por valor real e contexto próprio, e não por vaidade ou hype ("não adianta querer trocar Java por Clojure só porque você achou legal").

Convergência interessante: o autor descreve ter mudado, ao longo da carreira, de ler livros técnicos do início ao fim para uma leitura não-linear (primeiros capítulos, volta ao meio só quando a prática exige) — quase a mesma observação já registrada em [[wiki/concepts/aprender-a-aprender]] a partir de [[wiki/entities/fabio-akita]] (fonte [[wiki/sources/pare-de-terceirizar-suas-decisoes]]). Dois criadores de conteúdo independentes chegando à mesma prática de estudo por caminhos distintos é um sinal (fraco, mas real) de que a técnica generaliza além de uma única experiência pessoal.

## Citações Preservadas

> "Não adianta você só engolir informação, você precisa praticar, porque é com a prática que essa informação começa a virar habilidade."

> "Uma mudança grande gera barreira grande de implementação."

> "A empresa te paga porque ela acha que você pode ajudar ela a ganhar mais dinheiro... se você não evoluir, se você não ajudar a trazer cada vez mais dinheiro, ela simplesmente troca você por outra pessoa."

> "Faça por você, faça pela sua carreira... se der resultado, você precisa mostrar, porque aí você vai ter reconhecimento."
