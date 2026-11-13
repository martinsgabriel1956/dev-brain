---
type: concept
title: "Consistência Visual"
aliases: ["consistência", "consistência em UI", "consistency", "identidade visual", "família de ícones"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 20
tags: [ui, ui-design, consistencia, icones, cor, identidade-visual, design-system]
skill: ux-ui-mentor
status: stub
---

# Consistência Visual

Escolher um padrão e segui-lo em toda a interface: a mesma família de ícones, a mesma paleta, o mesmo tom de cor. "O design bonito é aquele consistente" ([[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]]). Aparece já em [[wiki/sources/o-que-e-ux-ui-design]] ao lado de [[wiki/concepts/contraste]] e [[wiki/concepts/hierarquia-visual]] como princípio base de [[wiki/concepts/ui-design]].

Não confundir com consistência de dados em sistemas distribuídos ([[wiki/concepts/consistency-models]]).

## Ícones: uma família por projeto

Uma família de ícones tem o mesmo estilo (só contorno, sem preenchimento) e o mesmo traço: parecem "filho de uma mesma pessoa". O autor usa o Feather Icons. Misturar com outro pacote de linha (do Iconify) de contorno diferente já quebra a consistência: dá para ver que são "duas pessoas diferentes". Pacotes como o Iconly têm várias variantes (preenchido, duas cores, linha, linha com cortes, curvado); escolha uma e fique nela.

## Cor: uma paleta mantida

O site do [[wiki/entities/frontpush]] usa preto, branco e um único azul gradiente com transparência, sem trocar o tom em nenhuma tela.

## Identidade visual

Consistência ao longo do tempo e dos produtos vira identidade: reconhecer a empresa sem ver a logo. Exemplo da aula: iMac, iPhone, iPad e MacBook da Apple seguem a mesma linguagem.

`[skill: ux-ui-mentor]` É a heurística 4 de Nielsen (consistência e padrões), que vai além do visual: mesmas ações, mesmas palavras, mesmos resultados. Violação clássica: "Salvar" numa tela, "Confirmar" em outra para a mesma ação. Na implementação, consistência se garante com design tokens e componentes de um design system, não com disciplina manual. Consistência externa (seguir o que outros produtos fazem) é a [[wiki/concepts/lei-de-jakob]]; ver também [[wiki/concepts/padroes-de-interface]].

## Consistência de escala, hierarquia e botões

[[wiki/sources/elementos-da-interface-introducao-ui-design]] amplia a lista: escala tipográfica seguida à risca, hierarquia bem definida, paleta estabelecida e botões usados sempre para guiar a ação do usuário ("link é diferente de botão"). Ver [[wiki/concepts/elementos-da-interface]].

## Consistência de espaçamento

Em [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]], o [[wiki/concepts/grid-de-8-pontos]] é apresentado como ferramenta do princípio da consistência: estabelecer uma escala de "bons números" múltiplos de 8 e usá-la ao longo de toda a interface para ter consistência visual e uma interface "mais agradável". Vale para espaços e tamanhos (altura de botão, logo de 72 × 72).

## Consistência não é harmonia

A aula de formas acrescenta uma camada: além de repetir o mesmo padrão, os padrões diferentes (forma, tipografia, cor) precisam passar a mesma mensagem. Ver [[wiki/concepts/harmonia-visual]] ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]).

## Consistência de forma: o radius

"Se você escolheu 8 como radius do seu botão, você vai aplicar 8-radius no resto da sua interface": cards, ícones e demais elementos. Botão arredondado com ícones totalmente retos é "uma quebra". No [[wiki/entities/frontpush]], até os ícones quadrados têm cantos arredondados ([[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]]). Ver [[wiki/concepts/border-radius]].

## Consistência de imagens

Na aula de imagens (parte 3), Násser padroniza resolução e proporção de todas as thumbs do blog para que nenhuma fique deslocada no layout ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]). Ver [[wiki/concepts/aspect-ratio]].

## Consistência de ilustrações

"Com ilustrações é do mesmo jeito": escolha uma família (ex.: [[wiki/entities/humaaans]]), em que todos os bonequinhos têm o mesmo traço, e não junte três sites com "três traços totalmente diferentes". É a regra da família de ícones aplicada à ilustração ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]]). Ver [[wiki/concepts/ilustracoes-em-interfaces]].

## Ícones: shapes e família

A aula de ícones repete "estou sempre batendo na tecla": consistência em tamanhos e shapes; uma curva aleatória numa família de formas regulares "desconecta". Uma [[wiki/concepts/familia-de-icones]] por projeto, escolhida pela identidade visual: Iconly arredondado e preenchido no Creator Push, Feather de linha (stroke 2, cantos arredondados) no FrontPUSH ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]).

## Ícones: grid e componente

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: um [[wiki/concepts/grid-de-icones|grid]] travado no frame dá "a maior exatidão possível e consistência possível", e transformar o ícone em componente com constraints em scale no [[wiki/entities/figma]] "vai aumentar demais a sua consistência quando você estiver construindo os seus assets". Destacar alguns ícones em azul mantém a consistência porque a família (linha) não muda.

## Ícones: exceção proposital

Em [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]], tudo nos ícones do FrontPUSH segue "à risca" (grossura da borda, gradiente, tamanho no grid), até logos de terceiros ficam retos. A única quebra é o asterisco da turma Epsilon, de propósito e numa só seção: "acredito que não quebrou tanto". A exceção só funciona por ser rara.

## Blocos iguais, tratamento igual

"O mesmo princípio que você aplicou para um, aplique para o resto." No site da [[wiki/entities/stripe]], dois subtópicos de mesma hierarquia repetem espaçamento, tamanho, cor de título, estrutura de corpo e link embaixo, e os ícones são da mesma [[wiki/concepts/familia-de-icones|família]] ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Sistema de espaçamento

"O nosso sistema precisa ter consistência em todo ele": uma [[wiki/concepts/escala-de-espacamento]] fixa (ou por porcentagem do pai), linear ou geométrica, usada em toda a interface ([[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]]).

## Mesma relação, mesma distância

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: 16 entre título e descrição e 16 entre os itens da lista, "para poder manter a consistência"; "a mesma distância de cá para cá" vale para os dois grupos de 32.

## Ícones: como "curar" a consistência

"Como é que você cura o problema da consistência?" Uma [[wiki/concepts/familia-de-icones|família de ícones]] na interface inteira, no máximo duas com papéis distintos; ilustrações e ícones precisam parecer "do mesmo designer" ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]).

## Ícones próprios como exercício

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]], desenhar os próprios ícones é "exercício de consistência visual" e um jeito de "criar algo literalmente que faça mais sentido" para cada módulo. Ícones de proporções diferentes ganham a mesma estrutura (círculo ou card) e a mesma escala.

## Consistência de botões

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: "escolheu um botão para sua interface, utilize o mesmo botão do mesmo jeito". Altura, padding e [[wiki/concepts/border-radius]] iguais; só a largura varia com o texto. Primário e secundário, nunca "cinco tipos de botão". Exemplos: [[wiki/entities/sketch]] e [[wiki/entities/frontpush]]. Ver [[wiki/concepts/botoes-em-interfaces]].

## Key Sources

- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — ícones, paleta e identidade visual
- [[wiki/sources/o-que-e-ux-ui-design]] — consistência como princípio base de UI
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — escala tipográfica, paleta e botão vs. link
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — grid de 8 pontos como consistência de espaçamento
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — harmonia como coerência de mensagem entre padrões
- [[wiki/sources/formas-exemplos-praticos-radius-consistencia-projetos]] — o mesmo radius em botões, cards e ícones
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — mesmas resolução e proporção em todas as imagens do blog
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — uma família de ilustrações, mesmo traço
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — shapes consistentes; uma família de ícones por projeto
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — grid de ícones e componente com scale
- [[wiki/sources/icones-parte-3-icones-do-frontpush-formas-geometricas-referencias]] — tudo "à risca"; logos redesenhados; asterisco como exceção proposital
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — consistência como o mesmo tratamento para elementos iguais (Stripe)
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — sistema de espaçamento como consistência
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — mesma relação, mesma distância (16 e 32)
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — ilustrações com o mesmo fundo cinza e a mesma cor de destaque; não misturar unDraw com outra biblioteca
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — isometria: mesmo ângulo em todas as peças
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — montar ilustração com trechos do unDraw: não misturar com outra biblioteca
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — ícones: uma família, no máximo duas com papéis distintos
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — ícones próprios como exercício de consistência; mesma estrutura e escala
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — mesmo botão em toda a interface: altura, padding e radius iguais
