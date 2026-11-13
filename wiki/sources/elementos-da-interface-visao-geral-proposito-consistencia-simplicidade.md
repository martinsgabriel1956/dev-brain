---
type: source
title: "Elementos da interface: visão geral, propósito, consistência e simplicidade"
aliases: ["visão geral dos elementos da interface", "o que faz uma boa interface", "aula introdutória elementos da interface (versão 2)"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 0
tags: [ui, ui-design, design, elementos-da-interface, espaco-em-branco, formas, cor, cor-semantica, tipografia, icones, botoes, links, consistencia, simplicidade, hierarquia-visual]
skill: ux-ui-mentor
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-13
---

# Elementos da interface: visão geral, propósito, consistência e simplicidade

## TL;DR

Aula introdutória do "segundo módulo" do curso de UI Design, sobre [[wiki/concepts/elementos-da-interface]]. Passa por cada elemento de forma geral, com exemplos de sites reais: espaçamento e linhas nos resultados do [[wiki/entities/google]], formas (retângulo e círculo), cores que informam ([[wiki/concepts/cor-semantica]]), [[wiki/concepts/tipografia]] e hierarquia textual (G1), ícones que se entendem mesmo com o [[wiki/entities/meta|Facebook]] em japonês, botões e links distinguíveis, e [[wiki/concepts/elementos-de-composicao]]. Todo elemento existe para **comunicar ou interagir**. Uma boa interface tem três coisas: **propósito** (saber o porquê de cada elemento), **[[wiki/concepts/simplicidade-visual|simplicidade]]** e **[[wiki/concepts/consistencia-visual|consistência]]** (o que vale para um elemento vale para todos os iguais, como nos blocos do site da [[wiki/entities/stripe]]).

Não é a mesma aula que [[wiki/sources/elementos-da-interface-introducao-ui-design]]. As duas abrem o mesmo módulo; aquela trata de fatores e melhores práticas, esta faz o tour dos elementos.

## Key Claims

### O que são

- **Elementos da interface são "tudo aquilo que compõe a interface".** A lista do slide: espaçamento e linhas, formas, cores, tipografia, ilustrações, ícones, botões e links, elementos de composição. Tratá-los um a um ajuda a "desmembrar" qualquer interface. Ver [[wiki/concepts/elementos-da-interface]].
- **A aula é generalista; cada tema ganha aula própria depois.** O autor avisa que a carga teórica é maior nessa parte.

### Espaçamento e linhas

- **Espaçamento e linhas servem para organizar e dispor a informação na tela.** Sem eles, os resultados do Google seriam "um tanto de texto jogado".
- **Espaço causa separação e agrupamento.** O texto pertence ao título maior "por ele estar mais próximo"; o recuo maior à esquerda e acima marca sublinks; cada resultado vira "uma caixinha" sem borda. Mesmo exemplo de [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]]. Ver [[wiki/concepts/lei-da-proximidade-gestalt]] e [[wiki/concepts/espaco-em-branco]].
- **A linha entra quando o espaço não basta**: para reforçar que são produtos ou informações diferentes.

### Formas

- **Toda interface é feita de formas**: cards, retângulos arredondados, retângulos que chamam atenção para links, círculo no perfil. Retângulo e círculo predominam, em ícones, imagens, cards e links. Ver [[wiki/concepts/formas-geometricas-e-organicas]].

### Cores

- **Cores servem para dar informação.** Um link de cor diferente sugere hierarquia maior. No site do autor, o botão preenchido com cor fica acima do que não é preenchido. Ver [[wiki/concepts/hierarquia-visual]].
- **Convenções de cor:** link azul é informação; vermelho é alerta; amarelo é warning. Ver [[wiki/concepts/cor-semantica]].
  - `[skill: ux-ui-mentor]` A skill dá o mesmo mapa (verde sucesso, vermelho erro, âmbar warning, azul info) com uma regra: nunca usar só a cor para comunicar estado, sempre com ícone, texto ou padrão, porque daltonismo afeta cerca de 8% dos homens.
- **Cores e tipografia terão módulos próprios.**

### Tipografia

- **"Tipografia compõe 90% da web, praticamente tudo é texto."** Hierarquia textual melhora a leitura: se o título interessa, o usuário desce para o corpo. Exemplo: o G1, quase todo texto, "disposto de maneira a facilitar a leitura". Ver [[wiki/concepts/tipografia]].
  - `[external]` A frase lembra "Web Design is 95% Typography", de Oliver Reichenstein (iA, 2006): https://ia.net/topics/the-web-is-all-about-typography-period. É um argumento de designer, não uma medição. Confiança média de que esta é a origem.

### Ilustrações, imagens e ícones

- **Ilustrações e imagens acompanham as explicações** para melhorar interação e entendimento. Ver [[wiki/concepts/imagens-em-interfaces]] e [[wiki/concepts/ilustracoes-em-interfaces]].
- **Ícones ficam numa classe à parte porque carregam uma informação a mais: o que fazer na interface.**
- **Exemplo do Facebook em japonês:** dá para navegar porque os ícones não mudam. Caixa de entrada, dashboard, sininho de notificação, engrenagem de configurações, lápis de edição, escudo de segurança. Ver [[wiki/concepts/icones-em-interfaces]] e [[wiki/concepts/padroes-de-interface]].
- **Os ícones dão "melhor acessibilidade".** Ver Tensões.

### Botões, links e elementos de composição

- **Botão e link precisam se diferenciar, por exemplo pela cor.** Link azul se reconhece "de cara"; texto branco "é literalmente texto". Onde há link, é preciso sinalizar. Ver [[wiki/concepts/affordance]].
- **Elementos de composição trazem pontos de atenção e deixam a interface "um pouco mais elegante".** Ver [[wiki/concepts/elementos-de-composicao]].

### O que faz uma boa interface

- **Todo elemento existe para comunicar ou interagir.** O módulo serve para entender o porquê de cada coisa. Ver [[wiki/concepts/porque-das-decisoes-de-design]].
- **Três pontos, ligados aos princípios do primeiro módulo:**
  1. **Propósito.** Nada fica "porque é legal" ou "porque está em cor diferente dos outros textos". Tudo comunica ou interage; "não está ali à toa".
  2. **Simplicidade.** Nada inútil na tela; a interface simples guia o usuário e ele "não se perde em tantas informações". Sistemas cheios de funções em que o usuário "só utiliza 20% das funcionalidades". Ver [[wiki/concepts/simplicidade-visual]] e [[wiki/concepts/sobrecarga-de-informacao]].
  3. **Consistência.** "O mesmo princípio que você aplicou para um, aplique para o resto." No site da Stripe, dois subtópicos de mesma hierarquia têm o mesmo espaçamento, tamanho, cor de título, estrutura de corpo e link embaixo; os ícones são da mesma [[wiki/concepts/familia-de-icones|família]]. Ver [[wiki/concepts/consistencia-visual]].
- **Botões com cor diferenciada indicam que algo é clicável** (outro site mostrado, não identificado).

## Entities

- [[wiki/entities/nasser]]: autor, confirmado pelo usuário em 2026-11-13 (o nome não é dito na aula). Fala em "meu site" com botões em cor de destaque, como o [[wiki/entities/frontpush]] nas outras aulas.
- [[wiki/entities/google]]: resultados de busca como exemplo de espaço e linhas.
- [[wiki/entities/meta]]: Facebook em japonês, navegável pelos ícones.
- [[wiki/entities/stripe]]: site como exemplo de consistência entre blocos de mesma hierarquia.
- Sem página própria: G1 (Globo), exemplo de hierarquia textual.

## Concepts

- [[wiki/concepts/elementos-da-interface]]
- [[wiki/concepts/cor-semantica]] (novo)
- [[wiki/concepts/espaco-em-branco]]
- [[wiki/concepts/lei-da-proximidade-gestalt]]
- [[wiki/concepts/formas-geometricas-e-organicas]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/icones-em-interfaces]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/affordance]]
- [[wiki/concepts/elementos-de-composicao]]
- [[wiki/concepts/porque-das-decisoes-de-design]]
- [[wiki/concepts/simplicidade-visual]]
- [[wiki/concepts/consistencia-visual]]
- [[wiki/concepts/sobrecarga-de-informacao]]
- [[wiki/concepts/principio-de-pareto]]

## Tensões com a wiki

- **Ícone e acessibilidade.** A aula diz que os ícones garantem "melhor acessibilidade" porque se entendem sem ler o idioma. Para quem enxerga, sim. Para leitor de tela, um ícone sem rótulo não diz nada. `[skill: ux-ui-mentor]` Ícone funcional precisa de `aria-label` quando não tem texto, e itens primários levam ícone e rótulo, nunca só o ícone. A própria [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] diz que o significado vem do pattern aprendido. Lápis e escudo, por exemplo, são menos universais que a engrenagem (o autor diz "talvez").
- **Link só pela cor.** A aula separa link de texto pela cor (azul contra branco). `[external]` A WCAG 2.2, critério 1.4.1 (Use of Color), pede que a cor não seja o único meio de passar informação. Um link só com cor precisa de contraste de 3:1 com o texto em volta e outro sinal no foco ou hover (técnica G183): https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. O sublinhado resolve. Não é contradição, é uma condição que a aula não menciona.
- **"20% das funcionalidades".** A aula não cita fonte. `[external]` O número costuma vir do Standish Group (Jim Johnson, XP 2002): 7% das funções usadas "sempre" e 13% "com frequência", 45% "nunca". A amostra era de software customizado e o dado é muito repetido sem checagem. Confiança baixa a média; não foi relido nesta sessão. Ver [[wiki/concepts/principio-de-pareto]].
- **Propósito como princípio.** A aula diz que propósito, consistência e simplicidade "fazem parte dos princípios do design" do primeiro módulo. Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] os princípios são eixo, simetria, consistência e simplicidade (mais contraste). Propósito não estava lá como princípio. Está mais perto de [[wiki/concepts/objetivo-da-interface]] e [[wiki/concepts/porque-das-decisoes-de-design]].
- **Duas aberturas para o mesmo módulo.** Esta se chama de "segundo módulo" e "aula introdutória", como [[wiki/sources/elementos-da-interface-introducao-ui-design]]. O conteúdo se complementa, não se repete. A ordem dentro do curso é desconhecida (talvez uma seja de outra edição do curso).

## Open Questions

- Qual é o "outro site" que o autor abre para mostrar ícones e botões? E o "meu site" do trecho de cores é o FrontPUSH?
- O trecho da Stripe começa com "aqui no meu site, por exemplo, ou no site da Stripe". Não dá para saber qual dos dois estava na tela.
- Logo "W7" no slide: não aparece nas outras aulas ingeridas. Edição diferente do curso?
- `date_published` vazio.

## Raw Quotes

> "O que são elementos da interface? Literalmente, é tudo aquilo que compõe a interface."

> "Os ícones não mudam."

> "Tudo tem que comunicar ou interagir de alguma forma, não está ali à toa."

> "O mesmo princípio que você aplicou para um, aplique para o resto."

## Continuação

A aula seguinte da mesma edição ("W7") aprofunda espaçamento e linhas: [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]].

## Continuação

A aula de formas da mesma edição ("vamos dar continuidade"): [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]].

## Ver também

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — botões e links em profundidade: primário x secundário, área clicável, hover
