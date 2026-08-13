---
type: source
title: "Por que começar com C em 2026 (CS50 — David Malan)"
aliases: ["CS50 por que C", "David Malan C first principles", "engenheiro vs coder Malan"]
date_created: 2026-08-13
date_updated: 2026-08-13
source_count: 0
tags: [cs-fundamentals, aprendizado, carreira, estruturas-de-dados, abstracao, primeiros-principios]
skill: cs-fundamentals
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/por-que-comecar-com-c-em-2026-cs50-david-malan.md
source_url: ""
author: "David Malan"
date_published: ""
date_ingested: 2026-08-13
---

# Por que começar com C em 2026 (CS50 — David Malan)

## TL;DR

David Malan, professor do [[wiki/concepts/cs50|CS50]] (Harvard), defende por que o curso ainda **começa por C** em 2026 e responde à crítica de que "você não precisa saber como o computador funciona". Dois argumentos centrais:

1. **C como fundação pedagógica.** É o mais perto do hardware que dá para chegar antes do assembly, mas com sintaxe parecida com inglês. É uma linguagem pequena e sem biblioteca padrão grande — então você é obrigado a **construir suas próprias estruturas de dados** (hash tables, listas ligadas, tries, árvores, pilhas, filas). Isso ensina a raciocinar por [[wiki/concepts/primeiros-principios|primeiros princípios]], diagnosticar problemas e serve de **andaime** para linguagens de alto nível (a hash table de 100 linhas em C vira um `dict` de uma linha em Python).
2. **"Não precisar usar" ≠ "não precisar saber".** Malan reformula a crítica: ele mesmo só usa C por 5 semanas no ano, mas o conhecimento extraído desses detalhes de implementação é o que separa um **engenheiro** (que entende e cria o que ainda não existe) de um **coder** (que só cospe o que "uma IA hoje conseguiria cuspir"). Ver [[wiki/concepts/engenheiro-vs-programador]].

## Claims principais

### 1. C encontra o equilíbrio pedagógico entre hardware e legibilidade
> **Evidência:** "É quase o mais perto que dá para chegar do hardware antes que as coisas descambem — pelo menos esteticamente — para o código assembly". C tem sintaxe parecida com inglês e abstrações sobre primitivas de baixo nível, com os construtos fundamentais (loops, condicionais, funções, variáveis, valores de retorno). Ao mesmo tempo é uma linguagem **pequena**, com biblioteca padrão enxuta.
> **Confiança:** alta (opinião pedagógica fundamentada de quem leciona o curso).

### 2. A ausência de estruturas prontas em C é a feature pedagógica
> **Evidência:** Diferente de Java/C++ com STL, em C "se você quer uma [estrutura], vai ter que construí-la você mesmo". No CS50, na semana 5 os alunos constroem suas próprias hash tables, listas ligadas simples/duplas, tries, árvores, pilhas e filas. O valor não é reusar essa implementação depois, mas entender de baixo para cima o que acontece dentro do dispositivo.
> **Confiança:** alta.

### 3. Entender a implementação habilita três coisas
> **Evidência:** (1) decisões de design mais informadas sobre as próprias estruturas; (2) diagnóstico de problemas por primeiros princípios, porque se entende como os dados são armazenados e quais algoritmos operam sobre eles; (3) andaime para linguagens de alto nível.
> **Confiança:** alta.

### 4. A hash table de C → dicionário de uma linha em Python
> **Evidência:** Entre a semana 5 e a semana 6 do CS50, a implementação própria de hash table (dezenas de linhas) "é reduzida a uma única linha, na qual você apenas instancia um dicionário em Python". Muitos cursos ensinam só por Python e o aluno "nunca chega de fato a entender o que está acontecendo por baixo do capô".
> **Confiança:** alta. Conecta a [[wiki/concepts/abstracao|abstração]] por camadas.

### 5. O objetivo é formar engenheiros, não programadores
> **Evidência:** "Um dos nossos objetivos no CS50 não é produzir programadores, mas engenheiros — e cidadãos instruídos, gente que realmente entende, a partir de primeiros princípios, como a tecnologia funciona."
> **Confiança:** alta (declaração explícita de objetivo do curso).

### 6. "Não vai precisar usar" é diferente de "não precisa saber"
> **Evidência:** Resposta à crítica ("faça o que fizer, não faça CS50"). Malan: para um **engenheiro full stack**, por definição, "você deveria estar entendendo tudo o que acontece entre essas camadas". Ele reformula: você não vai *usar* C, Scratch etc. no dia a dia, mas o conhecimento e os princípios extraídos deles são valiosos. Ele mesmo usa C só 5 semanas/ano, Scratch 1 semana/ano, e no resto usa Python, JavaScript, HTML, CSS.
> **Confiança:** alta.

### 7. C ainda é #1/#2 em onipresença por ser performático
> **Evidência:** "Segundo alguns rankings, ano após ano ela é a número um ou número dois em onipresença, ainda hoje, porque é altamente performática — ainda que mais difícil de escrever que algumas linguagens."
> **Confiança:** média (rankings de linguagem — ex.: TIOBE — variam; C de fato figura no topo consistentemente, mas "número 1 ou 2" depende do ranking).

### 8. A distinção engenheiro vs coder na era da IA
> **Evidência:** Se você vai se chamar de engenheiro, "deveria absolutamente ter domínio dos blocos de construção fundamentais — se o que você quer é não apenas cuspir algo que, francamente, uma IA hoje conseguiria cuspir, mas entender e criar a próxima coisa, ou a solução para algum problema que a gente ainda nem resolveu".
> **Confiança:** alta. Reforça [[wiki/concepts/engenheiro-vs-programador]].

## Entidades

- [[wiki/entities/david-malan]] — professor e apresentador do CS50 (autor da fala)
- [[wiki/concepts/cs50]] — o curso em questão

## Conceitos

- [[wiki/concepts/linguagem-c]] — C como fundação pedagógica
- [[wiki/concepts/primeiros-principios]] — raciocínio a partir de fundamentos
- [[wiki/concepts/engenheiro-vs-programador]] — engenheiro vs coder
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]] — construir as próprias estruturas
- [[wiki/concepts/abstracao]] — hash table em C → dict de uma linha em Python
- [[wiki/concepts/fundacao-tecnica]] — entender de baixo para cima
- [[wiki/concepts/sintaxe-vs-conhecimento-perene]] — "não usar" vs "não saber"

## Perguntas em aberto

- Malan afirma que full stack "por definição" deve entender todas as camadas. Isso é definição normativa (o que *deveria* ser) ou descritiva do mercado atual? Ver tensão com fontes sobre [[wiki/concepts/engenheiro-vs-programador]] no mercado real.
- Até onde a defesa de C se sustenta contra alternativas modernas com modelos de memória mais seguros (ex.: Rust) para ensinar os mesmos primeiros princípios? Ver [[wiki/concepts/rust-fundamentos]].

## Citações preservadas

> "É quase o mais perto que dá para chegar do hardware antes que as coisas descambem — pelo menos esteticamente — para o código assembly."

> "Se você quer uma [estrutura de dados], vai ter que construí-la você mesmo. E só isso já é um bom exercício educacional."

> "Um dos nossos objetivos no CS50 não é produzir programadores, mas engenheiros."

> "Você não vai precisar *usar* essas coisas — mas o conhecimento e os princípios que extraímos desses detalhes de implementação são incrivelmente valiosos se o que você quer é ser um engenheiro, e não apenas um coder."
