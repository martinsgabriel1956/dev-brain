---
type: source
title: "A Filosofia do Design de Software — Cap. 2: A Natureza da Complexidade"
aliases: ["philosophy of software design cap 2", "ousterhout capítulo 2", "a natureza da complexidade", "nature of complexity"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-02-natureza-da-complexidade.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-25
source_count: 0
tags: [complexidade, design, ousterhout, traducao, dependencias, obscuridade, carga-cognitiva, change-amplification, unknown-unknowns, tech-debt]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 2 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 2.1 a 2.5. É o capítulo que dá ao livro seu vocabulário. **Definição:** complexidade é qualquer aspecto da estrutura que torne o sistema difícil de entender e modificar, pesado pelo tempo que se passa em cada parte ($C = \sum_p c_p t_p$). **Sintomas:** amplificação de mudanças, carga cognitiva e incógnitas desconhecidas, sendo esta a pior ([[wiki/concepts/sintomas-de-complexidade-ousterhout]]). **Causas:** dependências e obscuridade ([[wiki/concepts/causas-de-complexidade-ousterhout]]). **Dinâmica:** ela cresce aos poucos, em milhares de pequenas concessões, e por isso pede "tolerância zero" ([[wiki/concepts/complexidade-incremental]]). Até aqui a wiki conhecia o cap. 2 por um podcast e por uma linha do livro completo. Esta é a primeira leitura de primeira mão, e ela corrige um ponto: no livro, amplificação de mudanças não exige dependência oculta.

## Key Claims

### 2.1 Definição

**Claim:** Complexidade é qualquer aspecto da estrutura de um sistema que o torne difícil de entender e modificar. Não tem a ver com tamanho ou com quantidade de recursos: um sistema grande e sofisticado em que é fácil trabalhar não é complexo, e um sistema pequeno pode ser bastante complexo.
**Evidence:** Primeiro e terceiro parágrafos da 2.1. A definição já estava na wiki por fontes indiretas ([[wiki/concepts/complexidade-acidental]], seção "Quarta fonte"). O que o texto acrescenta é o recorte: complexidade é "o que um desenvolvedor vivencia em um determinado momento ao tentar alcançar um objetivo específico". Ela é relativa à tarefa e a quem a executa, não uma propriedade absoluta do código.
**Confidence:** alta.

**Claim:** A complexidade total é a de cada parte pesada pelo tempo que os desenvolvedores passam nela: $C = \sum_p c_p t_p$. Uma parte muito complicada que quase nunca é alterada pesa pouco. "Isolar a complexidade em um lugar onde ela nunca será vista é quase tão bom quanto eliminá-la."
**Evidence:** 2.1. É a justificativa formal para a segunda abordagem do cap. 1, encapsular ([[wiki/concepts/reducao-de-complexidade]]), e para os módulos profundos ([[wiki/concepts/modulo-profundo]]): a complexidade escondida atrás de uma interface simples tem $t_p$ perto de zero para quem só usa o módulo. O próprio autor chama a fórmula de caracterização "matemática bruta", não de métrica.
**Confidence:** alta quanto ao texto. A ligação com módulos profundos é inferência desta wiki, mas o livro a faz depois (cap. 4).

**Claim:** A complexidade é mais evidente para quem lê do que para quem escreve. Se o código parece simples para o autor e complexo para os outros, ele é complexo. O trabalho do desenvolvedor é escrever código com que **os outros** trabalhem com facilidade.
**Evidence:** Último parágrafo da 2.1. O autor sugere investigar a divergência com os colegas, porque ela traz lições. É a base do método da seção 1.1, aprender design revisando código alheio ([[wiki/concepts/code-review]]), e reaparece no cap. 14, quando ele rebate Andrew Gerrand sobre nomes curtos: a legibilidade é julgada por quem lê ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).
**Confidence:** alta.

### 2.2 Sintomas

**Claim:** Amplificação de mudanças é quando uma alteração aparentemente simples exige mudanças em muitos lugares.
**Evidence:** Figura 2.1(a): cada página do site define `bg = 'red'` no próprio código, então trocar a cor exige editar milhares de páginas. Na 2.1(b), a cor fica numa variável central (`bannerBg`) e muda com uma edição. Objetivo de design: reduzir a quantidade de código afetada por cada decisão de projeto. Note que, em (a), a dependência é **conhecida**: todos sabem que a cor está em cada página. O problema é a quantidade de lugares, não a falta de visibilidade.
**Confidence:** alta.

**Claim:** Carga cognitiva é quanto o desenvolvedor precisa saber para concluir uma tarefa. Mais carga significa mais tempo aprendendo e mais risco de bug por algo que passou despercebido.
**Evidence:** Exemplo em C: uma função aloca memória, devolve o ponteiro e espera que quem chama a libere. Esquecer gera *memory leak*. Se o mesmo módulo alocar e liberar, a carga cai. Fontes citadas: APIs com muitos métodos, variáveis globais, inconsistências e dependências entre módulos ([[wiki/concepts/carga-cognitiva]]).
**Confidence:** alta.

**Claim:** Linhas de código não medem complexidade. "Às vezes, uma abordagem que exige mais linhas de código é, na verdade, mais simples, porque reduz a carga cognitiva."
**Evidence:** O autor cita *frameworks* em que poucas linhas bastavam para escrever uma aplicação, mas era muito difícil saber o que elas faziam. A frase antecipa o debate com *Clean Code* sobre tamanho de função ([[wiki/concepts/modulo-profundo]], [[wiki/entities/uncle-bob]]).
**Confidence:** alta.

**Claim:** Incógnitas desconhecidas (*unknown unknowns*) são o pior dos três sintomas. Não é óbvio que código mudar nem que informação é preciso ter, e só se descobre depois, quando os bugs aparecem.
**Evidence:** Figura 2.1(c): algumas páginas usam um tom mais escuro (`emph = 'darkred'`) escrito à mão. Quem troca `bannerBg` dificilmente sabe disso e, mesmo sabendo, teria de procurar em todas as páginas. O autor compara: a amplificação "é irritante", mas, se está claro o que mudar, o sistema funciona ao final; a carga cognitiva encarece a mudança, mas, se está claro o que ler, a mudança tende a sair certa. Com incógnitas desconhecidas, a única garantia seria ler todas as linhas, o que é impossível e talvez nem baste, porque a mudança pode depender de uma decisão de design nunca documentada.
**Confidence:** alta.

**Claim:** Um dos objetivos mais importantes do design é que o sistema seja **óbvio**: o desenvolvedor dá um palpite rápido sobre o que fazer e pode confiar que acertou. Óbvio é o oposto de carga cognitiva alta e de incógnitas desconhecidas.
**Evidence:** Último parágrafo da 2.2, com remissão ao cap. 18.
**Confidence:** alta.

### 2.3 Causas

**Claim:** A complexidade tem duas causas: **dependências** e **obscuridade**. Há dependência quando um trecho não pode ser compreendido e modificado isoladamente.
**Evidence:** Exemplos: a cor do banner na Figura 2.1(a); remetente e destinatário de um protocolo de rede, que mudam juntos; a assinatura de um método, que obriga todos os chamadores a mudar quando ganha um parâmetro. Ver [[wiki/concepts/causas-de-complexidade-ousterhout]] e [[wiki/concepts/acoplamento]].
**Confidence:** alta.

**Claim:** Dependências não podem ser eliminadas: criar uma classe já cria dependências em torno da API dela. O objetivo é ter menos dependências e deixar as que restam **simples e óbvias**.
**Evidence:** O site novo não eliminou dependências. Ele trocou a dependência entre todas as páginas por uma dependência de cada página com `bannerBg`, que é óbvia: aparece numa busca pelo nome, e o compilador acusa quem usar o nome antigo.
**Confidence:** alta.

**Claim:** Obscuridade é quando informação importante não é óbvia. Costuma andar junto com dependências cuja existência não é óbvia.
**Evidence:** Exemplos: um nome genérico demais (`time`); uma variável sem unidade documentada; um novo status de erro que exige uma entrada numa tabela de mensagens que ninguém sabe que existe ([[wiki/concepts/dependencia-externa-oculta]] é um caso vizinho); o mesmo nome usado para dois propósitos, como no bug da variável `block` do cap. 14 ([[wiki/concepts/naming]]).
**Confidence:** alta.

**Claim:** A obscuridade vem muitas vezes de documentação ruim, mas também é questão de design. "A necessidade de documentação extensa costuma ser um alerta vermelho de que o design não está muito adequado"; a melhor forma de reduzi-la é simplificar o design.
**Evidence:** 2.3, com remissão ao cap. 13. Não contradiz a defesa que o livro faz dos comentários: os comentários cobrem o que o código não diz, e um bom design reduz o quanto há para dizer ([[wiki/concepts/comentarios-como-ferramenta-de-design]]).
**Confidence:** alta quanto ao texto; média quanto à conciliação (inferência desta wiki).

**Claim:** As causas explicam os sintomas. Dependências geram amplificação de mudanças e carga cognitiva. Obscuridade gera incógnitas desconhecidas e também aumenta a carga cognitiva.
**Evidence:** Último parágrafo da 2.3.
**Confidence:** alta.

### 2.4 e 2.5 Complexidade incremental

**Claim:** A complexidade não vem de um erro catastrófico. Ela se acumula em centenas ou milhares de pequenas dependências e obscuridades, até que qualquer mudança esbarre em várias delas. Isso a torna difícil de controlar (cada concessão parece pequena) e de remover (corrigir uma só não faz diferença). A resposta é "tolerância zero", tema do cap. 3.
**Evidence:** 2.4. Ver [[wiki/concepts/complexidade-incremental]] e [[wiki/concepts/tech-debt-como-ferramenta]] (programação tática vs. estratégica).
**Confidence:** alta.

**Claim:** No fim, a complexidade torna a modificação de uma base de código existente difícil e arriscada: mais mudanças por funcionalidade, mais tempo levantando informação e, no pior caso, informação que não se consegue achar.
**Evidence:** 2.5.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **Amplificação de mudanças não precisa de dependência oculta.** [[wiki/concepts/sintomas-de-complexidade-ousterhout]] e [[wiki/concepts/ocultamento-de-informacao]], escritas a partir do podcast ([[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]]), descrevem a amplificação como mudança que "se espalha para dependências desconhecidas". No livro, o caso de livro-texto, Figura 2.1(a), tem dependência conhecida: o problema é só a quantidade de lugares. Quando a dependência é desconhecida, o livro chama de incógnita desconhecida, Figura 2.1(c). O podcast junta os dois sintomas. As duas páginas foram ajustadas com nota.
- **Duas traduções de *unknown unknowns* no mesmo capítulo.** A 2.2 usa "incógnitas desconhecidas"; a 2.5 usa "variáveis totalmente desconhecidas", e a N.T. diz que essa é a adaptação escolhida. "Variáveis" atrapalha num capítulo em que `bannerBg` e `time` são variáveis de verdade. Sugestão: ficar com "incógnitas desconhecidas", ou só o termo em inglês.
- **"Complicado" e "complexo"** aparecem como sinônimos, como no original (*complicated* / *complex*), sem a distinção que alguns autores fazem entre os dois (Cynefin). Não é erro de tradução.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-01-traducao-revisada]]
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]]
- [[wiki/concepts/causas-de-complexidade-ousterhout]] (nova)
- [[wiki/concepts/complexidade-incremental]] (nova)
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/cognitive-load]]
- [[wiki/concepts/reducao-de-complexidade]]
- [[wiki/concepts/ocultamento-de-informacao]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/complexidade-acidental]]
- [[wiki/concepts/comentarios-como-ferramenta-de-design]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/entropia-de-software]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/zonas-de-desconhecimento]]
- [[wiki/concepts/modulo-profundo]]

## Open Questions

- A fórmula $C = \sum_p c_p t_p$ não tem como medir $c_p$. Dá para aproximá-la com *hotspots* (complexidade × frequência de mudança no git), como em [[wiki/concepts/tech-debt-como-ferramenta]] (seção "Medindo Dívida")? A analogia é da wiki, não do livro.
- A wiki tem [[wiki/concepts/carga-cognitiva]] (UX e memória de trabalho) e [[wiki/concepts/cognitive-load]] (stub de times e plataforma). Com o sentido de Ousterhout são três usos do termo. Fundir ou desambiguar no próximo lint.
- O cap. 3 ("tolerância zero", programação tática vs. estratégica) é o próximo da tradução; a wiki já o tem pelo livro completo.

## Raw Quotes

> "Isolar a complexidade em um lugar onde ela nunca será vista é quase tão bom quanto eliminá-la por completo."

> "Às vezes, uma abordagem que exige mais linhas de código é, na verdade, mais simples, porque reduz a carga cognitiva."

> "A necessidade de documentação extensa costuma ser um alerta vermelho de que o design não está muito adequado."
