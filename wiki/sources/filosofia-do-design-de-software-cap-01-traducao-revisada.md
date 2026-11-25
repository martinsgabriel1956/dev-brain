---
type: source
title: "A Filosofia do Design de Software — Cap. 1 e 1.1 (tradução revisada)"
aliases: ["philosophy of software design cap 1 tradução revisada", "ousterhout capítulo 1 segunda tradução", "é tudo sobre complexidade"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-01-traducao-revisada.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-25
source_count: 0
tags: [complexidade, design, ousterhout, traducao, red-flags, code-review, waterfall, agile, modularidade]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Segunda tradução do capítulo 1 de *A Philosophy of Software Design*, feita pelo usuário e com notas do tradutor. Cobre a introdução e a seção 1.1, "Como usar este livro". **O conteúdo é o mesmo** de [[wiki/sources/filosofia-do-design-de-software-introducao]] (ingerida em 2026-07-10). Por isso esta página não repete os claims que já estavam lá. Ela acrescenta os três pontos do capítulo que a página de julho não cobria (os objetivos do livro, a ausência de receita e o alcance das ideias fora da orientação a objetos), além das diferenças entre as duas traduções e das notas do tradutor. Em geral, esta versão é mais fiel: mantém o subtítulo do capítulo, a primeira pessoa e os dois apartes do autor, e segue a divisão de seções do livro.

## Key Claims

### Conteúdo do capítulo que faltava na wiki

**Claim:** O livro tem dois objetivos. O primeiro é descrever a natureza da complexidade de software: o que ela é, por que importa e como reconhecer complexidade desnecessária. O segundo, que o autor considera o mais difícil, é apresentar técnicas para minimizá-la durante o desenvolvimento.
**Evidence:** Último parágrafo da introdução. Os dois objetivos correspondem às duas partes do livro: o capítulo 2 trata da natureza da complexidade, e os seguintes, principalmente, das técnicas ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).
**Confidence:** alta quanto aos objetivos; média quanto à correspondência com os capítulos (inferência desta wiki).

**Claim:** Não existe receita simples que garanta um bom design. O livro oferece conceitos de alto nível, "que beiram o filosófico", como "as classes devem ser profundas" ([[wiki/concepts/modulo-profundo]]) e "elimine os erros desde a concepção" ([[wiki/concepts/definir-erros-para-fora-da-existencia]]). Eles não apontam o melhor design de imediato, mas servem para **comparar alternativas** e orientar a exploração do espaço de design.
**Evidence:** Mesmo parágrafo da introdução. A ideia combina com o método da 1.1: diante de um sinal de alerta, testar várias alternativas de design até eliminá-lo ([[wiki/concepts/red-flags-de-design]]).
**Confidence:** alta.

**Claim:** Os exemplos são quase todos em Java ou C++, e a discussão gira em torno do design de classes, mas as ideias valem fora da orientação a objetos. O que vale para métodos vale para funções numa linguagem como C. O que vale para classes vale para outros tipos de módulo, como subsistemas e serviços de rede.
**Evidence:** Penúltimo parágrafo da 1.1. Isso explica por que a wiki aplica o vocabulário de Ousterhout a APIs e serviços, e não só a classes (por exemplo, a API de I/O do Java e o cliente HTTP do Go em [[wiki/concepts/modulo-profundo]]).
**Confidence:** alta.

### Diferenças entre as traduções

**Claim:** Esta tradução tem mais texto do autor que a anterior.
**Evidence:** Tem o subtítulo "(É Tudo Sobre Complexidade)" e os dois apartes em primeira pessoa: o pedido de bons exemplos ("por favor, envie-os para mim") e o de novos sinais de alerta ("eu adoraria ouvir sobre eles"). A versão de julho não traz nenhum dos três e reescreve trechos na terceira pessoa ("o autor aponta"). São cerca de 1.700 palavras contra cerca de 1.640.
**Confidence:** alta. A comparação é entre os dois arquivos em `raw/`; o original em inglês não está no repositório.

**Claim:** A divisão de seções segue o livro: introdução corrida e depois só a seção 1.1.
**Evidence:** A versão de julho tem os subtítulos "Design de software é um processo contínuo" e "Sobre este livro". Até onde se sabe, eles não existem no livro: o capítulo 1 só tem a seção 1.1, "How to use this book".
**Confidence:** média. Vem de memória do original `[external, não verificado]`.

**Claim:** A frase sobre não conseguir prever o design de um sistema grande está correta nesta versão e truncada na anterior.
**Evidence:** Nova: "não é possível visualizar o design de um grande sistema de software bem o suficiente para entender todas as suas implicações". Antiga: "visualizar o design de um sistema de software grande o suficiente para entender", que muda o sentido (o "o suficiente" passa a qualificar o tamanho do sistema). Esse é o argumento central contra o cascata em [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]].
**Confidence:** média-alta (leitura gramatical das duas frases).

**Claim:** Nesta versão, "estruturar" se afasta do original no papel das fases depois do design congelado no cascata.
**Evidence:** Nova: "o papel das fases subsequentes é estruturar e implementar esse design". Antiga: "detalhar e implementar". O original usa algo como *flesh out*, mais perto de "detalhar" ou "desenvolver" `[external, não verificado]`. "Estruturar" sugere que ainda há design a decidir, que é o contrário do que o parágrafo descreve.
**Confidence:** média.

**Claim:** "Define errors out of existence" agora tem três versões em português na wiki.
**Evidence:** "Elimine os erros desde a concepção" (esta versão), "elimine erros por definição" (julho) e "definir erros para fora da existência" (o nome do conceito, em [[wiki/concepts/definir-erros-para-fora-da-existencia]] e [[wiki/concepts/define-errors-out-of-existence]]). "Desde a concepção" se aproxima de "prevenir no design", mas perde o jogo com *define*. A técnica do cap. 10 é **redefinir a semântica** da operação para que a condição de erro deixe de existir, como o `substring` que aceita índices fora do limite.
**Confidence:** alta quanto à divergência; a recomendação é só uma sugestão.

**Claim:** A nota do tradutor que iguala *red flags* a "antipadrões ou cheiros no código" vai além do livro.
**Evidence:** A N.T. diz que os sinais de alerta são antipadrões ou *code smells*. Para esta wiki são linhagens paralelas que se sobrepõem em parte, não sinônimos ([[wiki/concepts/red-flags-de-design]], seção "Linhagem paralela"). No livro, os *red flags* são sintomas de complexidade, e vários deles (Pass-Through Method, Conjoined Methods, Comment Repeats Code) não estão no catálogo de Fowler. A equiparação é do tradutor, não de Ousterhout.
**Confidence:** alta.

**Claim:** A outra N.T. define code review como prática para "garantir qualidade". A seção 1.1 usa a revisão com outro objetivo.
**Evidence:** Na 1.1, revisar código serve para **aprender design**, porque é mais fácil ver problemas no código dos outros, e expõe o revisor a "novas abordagens de design e técnicas de programação". Os dois sentidos se complementam (ver [[wiki/concepts/code-review]]).
**Confidence:** alta.

**Claim:** Algumas escolhas de termo diferem da wiki sem erro de sentido.
**Evidence:** "Sinais de alerta" para *red flags* (alias já presente em [[wiki/concepts/red-flags-de-design]]). "Indo longe demais" para *Taking it too far* (julho: "Levando longe demais"). "Exagerando na dose" para *overdoing a good thing*, que perde o "algo bom" `[external, não verificado]`. "Design modular" e "módulos" em itálico, como no original.
**Confidence:** alta quanto às escolhas; baixa quanto ao *overdoing*.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]
- [[wiki/concepts/definir-erros-para-fora-da-existencia]]
- [[wiki/concepts/define-errors-out-of-existence]]
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/reducao-de-complexidade]]

## Próximo capítulo

A tradução continua em [[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]. O cap. 2 cumpre o primeiro objetivo anunciado aqui: descrever a natureza da complexidade e como reconhecê-la.

## Open Questions

- Sem o original em inglês no repositório, quatro pontos ficaram com confiança média: *flesh out*, *overdoing a good thing*, a ausência de subtítulos no livro e a palavra exata do subtítulo. O epub citado no ingest de 2026-07-29 estava em `/home/nemomartins/...`, um caminho que não existe nesta máquina.
- Se o usuário continuar traduzindo os capítulos seguintes, vale padronizar os termos com a wiki ("Levando/Indo longe demais", "define errors out of existence").
- A wiki tem duas páginas para o mesmo conceito: [[wiki/concepts/definir-erros-para-fora-da-existencia]] e [[wiki/concepts/define-errors-out-of-existence]]. É uma candidata a fusão no próximo lint.

## Raw Quotes

> "Tem sido um desafio encontrar exemplos que sejam pequenos o suficiente para incluir no livro, mas grandes o bastante para ilustrar problemas em sistemas reais (se você encontrar bons exemplos, por favor, envie-os para mim)."

> "Sua experiência também mostrará outros sinais que você poderá usar para identificar problemas de design (eu adoraria ouvir sobre eles)."
