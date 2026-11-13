---
type: concept
title: "Hierarquia Visual"
aliases: ["visual hierarchy", "hierarquia de elementos", "padrão Z", "padrão F", "Z-pattern", "F-pattern"]
date_created: 2026-07-21
date_updated: 2026-11-13
source_count: 17
tags: [ui, ux, design, frontend, hierarquia-visual]
skill: tech-mentor-frontend
status: draft
---

# Hierarquia Visual

Ordem em que o olho do usuário percorre os elementos de uma tela, definida deliberadamente por meio de peso de fonte, tamanho, cor e posicionamento — não deixada ao acaso. O objetivo é que os elementos mais importantes chamem atenção primeiro, e os demais em ordem decrescente de importância.

## O problema de dois pontos focais

Se dois elementos (por exemplo, dois CTAs) têm o mesmo peso visual — mesmo tamanho, mesma cor chamativa, mesma fonte — o cérebro não sabe qual priorizar. Na prática, o usuário tende a escolher a ação mais fácil de executar, não a mais desejada pelo produto: um CTA de "ver conteúdo" (passivo, sem fricção) tende a roubar cliques de um CTA de "se inscrever" (ativo, com fricção de preencher um formulário), mesmo que o segundo seja o objetivo real da página.

O mesmo vale dentro da foto: "toda imagem é interessante que ela tenha um ponto focal, não dois" ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]; ver [[wiki/concepts/ponto-focal-em-fotografia]]).

## Padrões de leitura em tela

Além do peso visual dos elementos individuais, o **posicionamento relativo** segue padrões de escaneamento documentados:

- **Padrão Z**: usado em páginas com mais elementos e menos texto (apps, landing pages). O olho percorre da esquerda pra direita a partir do topo, desce em diagonal até a parte inferior esquerda, e finaliza a leitura da esquerda pra direita novamente — desenhando um Z.
- **Padrão F**: usado em páginas com muito texto (blogs, artigos). O usuário primeiro escaneia o conteúdo em formato de F (sem ler de fato) e só depois volta para ler o que interessou.

Escolher o padrão errado para o tipo de conteúdo — por exemplo, aplicar F numa tela com poucos elementos e um único objetivo de conversão — dilui o fluxo de atenção que a hierarquia visual tenta impor.

## Aplicação em prompts de geração de UI

Ao pedir para uma IA (ex.: UX Pilot, Cursor) gerar ou refatorar uma interface, é possível declarar a hierarquia explicitamente no prompt: qual elemento é o ponto focal primário (ex.: título com peso de fonte máximo), qual é o secundário (ex.: formulário), e garantir que a ação de CTA seja visualmente dominante sobre o resto — evitando CTAs concorrentes.

## Hierarquia como um dos "pequenos acertos" de UI

Em [[wiki/sources/o-que-e-ux-ui-design]], hierarquia aparece ao lado de consistência e contraste como princípio base de [[wiki/concepts/ui-design]]: um dos acertos pequenos que, somados, viram UX dentro da UI.

`[skill: ux-ui-mentor]` Ferramentas de hierarquia em ordem de impacto: tamanho, peso, cor, posição, espaço em branco e tipografia. Usar todas no mesmo elemento anula o efeito.

## Cor de destaque escassa

Na landing page do [[wiki/entities/frontpush]], o fundo é preto e neutro e o azul aparece só nos pontos de ação: quanto menos azul, mais o CTA se destaca de longe ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]). O catálogo de [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] chama o mecanismo de Isolation Effect. Ver [[wiki/concepts/contraste]].

## Relação com outros conceitos

- [[wiki/concepts/lei-da-proximidade-gestalt]] — hierarquia define *o que* chama atenção primeiro; proximidade define *quais elementos são lidos como um grupo único*.
- [[wiki/concepts/affordance]] — hierarquia guia a atenção; affordance guia a ação depois que a atenção chegou lá.
- [[wiki/concepts/design-como-interacao]] — hierarquia é uma das camadas de design que vai além do "bonito", com efeito direto em conversão.
- [[wiki/concepts/porque-das-decisoes-de-design]] — a escala tipográfica é um dos porquês que criam hierarquia

## Tamanho, forma, posição e cor

Slides de [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] (o autor adia a explicação falada para uma aula própria). Hierarquia é o "nível de importância dos elementos":

- **Tamanho:** olhamos primeiro para os maiores elementos (destaque no topo de um feed de notícias; Reels maiores no Explorar do Instagram).
- **Forma:** um elemento diferente dos demais se destaca (avatar redondo acima de um grid de quadrados).
- **Posição:** elementos fixos e no topo vêm primeiro, porque lemos de cima para baixo.
- **Cores:** as que contrastam mais têm mais hierarquia ([[wiki/concepts/contraste]]).

A mesma aula mostra hierarquia criada pelo [[wiki/concepts/eixo-visual|eixo]]: itens alinhados no mesmo eixo são pares; um item deslocado é filho do de cima. E pelo [[wiki/concepts/espaco-em-branco]], que isola o ponto focal.

## Hierarquia como melhor prática

[[wiki/sources/elementos-da-interface-introducao-ui-design]] lista hierarquia entre as melhores práticas e repete os meios do módulo anterior: cor, contraste da cor, forma e tamanho. Cor e contraste "complementam a prática da hierarquia visual". Exemplo no próprio slide: ícone preenchido e maior ao lado da descrição principal, ícones menores nos itens.

## Hierarquia pelo espaço

Em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]], o espaço ordena a leitura: o macro espaço ao redor de um elemento dá foco e ênfase, e vãos de tamanhos diferentes dizem o que pertence a quê. Título (h1, maior e mais contrastado) e descrição ficam colados (4 a 8 px) por serem a mesma mensagem; o CTA fica mais longe (40 ou 48) por ser outra função. No menu, links equidistantes estão "em uma mesma hierarquia". Ver [[wiki/concepts/espaco-em-branco]].

## Ícone ao lado do título

No site da Apple analisado na aula de ícones, o título vem primeiro por tamanho, posição (em cima, à esquerda) e cor mais viva; a descrição fica em cor neutra; e um ícone acompanha cada item ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). Ver [[wiki/concepts/icones-em-interfaces]].

## Ícone preenchido x linha

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: preenchido destaca ("Get More with Pro" do [[wiki/entities/font-awesome]] tem "maior área preenchida"); linha é neutra e "às vezes é justamente essa a intenção" (abas, menus). No [[wiki/entities/frontpush]], ícones de linha sobem de hierarquia pela cor de destaque azul e por virem primeiro, à esquerda; a setinha azul dentro do botão azul, pequena e com pouco contraste, fica neutra. "Um jogo complexo de várias variáveis": posicionamento, tamanho, formas, preenchimento.

## Ícone de linha com hierarquia (parte 3)

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], os ícones da grade do FrontPUSH ficam de linha (minimalismo), mas maiores, "posicionados mais acima" e no gradiente azul da marca, para não ficarem com "a hierarquia muito baixa".

## O fundo não compete

[[wiki/concepts/elementos-de-composicao|Elementos de composição]] ficam em baixo contraste para que a hierarquia vá para logo, título e CTA ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]).

## Hierarquia textual e cor de destaque

Link em cor diferente dos demais sugere hierarquia maior; botão preenchido fica acima do não preenchido. Em sites de notícia como o G1, quase todo texto, a hierarquia textual decide se o leitor desce do título para o corpo ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]). Ver [[wiki/concepts/cor-semantica]] e [[wiki/concepts/tipografia]].

## Espaço, recuo e cor

Na aula de espaçamento e linhas, agrupamento, um espaço maior até o próximo elemento e o recuo lateral criam hierarquia, junto com a diferença de cor ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]).

## Hierarquia por distância, na prática

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]], o que está mais alto na hierarquia ganha mais distância: 16 dentro do grupo, 32 entre grupos, 128 entre blocos, todos medidos com Alt no [[wiki/entities/figma]].

## Hierarquia entre botões e links

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: botão primário preenchido e secundário "vazio", sem background, criam hierarquia entre ações. Na [[wiki/entities/apple]], links em branco e texto em cinza; no [[wiki/entities/sketch]], o link "tem a hierarquia visual maior do corpo de texto". Ver [[wiki/concepts/botoes-em-interfaces]].

## Key Sources

- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
- [[wiki/sources/o-que-e-ux-ui-design]]
- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — azul escasso para isolar o CTA
- [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] — Isolation Effect como padrão persuasivo de atenção
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — slides: tamanho, forma, posição e cor; hierarquia pelo eixo
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — hierarquia como melhor prática; ícone preenchido maior no slide
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — macro espaço como foco; vãos diferentes entre título, descrição e CTA
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — um ponto focal por imagem, não dois
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — título > descrição na Apple, sempre com ícone ao lado
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — preenchido destaca, linha neutraliza; cor e posição sobem a hierarquia do ícone
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — linha + tamanho, posição e gradiente azul na grade do FrontPUSH
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — elementos de composição em baixo contraste para não roubar o foco
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — cor de destaque e hierarquia textual (G1)
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — espaço, recuo e cor como hierarquia
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — 16 / 32 / 128 como níveis de hierarquia
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — destaque por cor nas ilustrações aponta onde está o motion
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — botão primário x secundário; link branco x texto cinza (Apple)
