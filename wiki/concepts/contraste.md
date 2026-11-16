---
type: concept
title: "Contraste"
aliases: ["contraste de cor", "color contrast", "contraste em UI", "isolation effect", "efeito Von Restorff"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 21
tags: [ui, ui-design, cor, acessibilidade, hierarquia-visual, cta]
skill: ux-ui-mentor
status: stub
---

# Contraste

Diferença perceptível entre elementos (luminância, cor, tamanho) que torna um elemento legível e destacável. Aparece na wiki em dois papéis.

## Contraste para legibilidade

Contraste mal aplicado é o primeiro exemplo de UI ruim em [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]: você consegue ler o texto, mas idosos e pessoas com problema de visão não. Princípio base de [[wiki/concepts/ui-design]] segundo [[wiki/sources/o-que-e-ux-ui-design]].

`[skill: ux-ui-mentor]` WCAG AA pede 4.5:1 para texto normal e 3:1 para texto grande (≥ 18pt, ou ≥ 14pt em negrito); AAA pede 7:1 e 4.5:1. Passar no número não basta: texto branco sobre azul saturado pode passar e ainda cansar a leitura.

## Contraste para direcionar a ação

Na landing page do [[wiki/entities/frontpush]], tudo é preto e neutro, o texto é branco e o azul aparece só em pontos específicos. "Quanto menos eu utilizar a cor azul", mais o botão de lista de espera salta de longe ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]). Um botão de cadastro sem contraste trai o [[wiki/concepts/objetivo-da-interface|objetivo da página]].

O catálogo de [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] chama isso de **Isolation Effect** (efeito Von Restorff): o item diferente dos demais é o mais notado e lembrado. A cor de destaque só funciona se for escassa. É o mecanismo da [[wiki/concepts/hierarquia-visual]].

## Contraste como prioridade

Em [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]], contraste é condição de acessibilidade: "como é que eu vou deixar algo acessível se eu não consigo enxergar direito?". Vale para ilustrações e tudo mais, mas pesa mais na tipografia. O slide da aula diz que contraste "define a prioridade" e lista quatro meios: **tamanho, peso tipográfico, cor e preenchimento**. Ou seja, contraste não é só de cor.

## Contraste para idosos

Em [[wiki/sources/elementos-da-interface-introducao-ui-design]], projetar para idosos pede mais contraste na tipografia: cuidado com a escala de cinza para não ficar próxima do fundo, e um botão de alto contraste para quem tem problema de vista. Cor e contraste aparecem como melhor prática que complementa a [[wiki/concepts/hierarquia-visual]]. Ver [[wiki/concepts/contexto-do-usuario]].

## Contraste como recurso de forma

Um botão de cantos retos numa interface orgânica não é erro: "pode ser que você queira criar contraste, é um recurso". O contraste aqui é de forma e de mensagem, não de cor ([[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]]; ver [[wiki/concepts/harmonia-visual]]).

## Contraste para escrever sobre imagem

Em [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]], Násser retoma o contraste para texto em foto: "99% das vezes" letra branca, garantida por uma capa de gradiente (preto ou a cor do background, de 30–50% a 90–100%) atrás do texto. "Se eu não preciso garantir legibilidade é porque não precisa ler." Ver [[wiki/concepts/texto-sobre-imagem]].

## Ferramenta: Who Can Use

Na parte 3 das aulas de imagens, Násser complementa a seção de contraste com o [[wiki/entities/who-can-use]]: duas cores, uma nota e a simulação de vários problemas de visão. Para título, lembra que há outros meios além da cor, como peso e tamanho ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]). `[external]` A ferramenta já pondera tamanho e peso, e WCAG não tem critério de contraste no nível A, só AA e AAA (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Contraste em ícones

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: a setinha azul num botão azul do [[wiki/entities/frontpush]] é neutra por ter pouco contraste; os ícones de destaque têm "contraste maior, um tamanho maior". Preto e branco "não são cores, são extremos de luz", e por isso deixam ícones de linha mais neutros. `[skill: ux-ui-mentor]` Ícone informativo pede 3:1; decorativo ao lado de texto, não.

## Contraste baixo no fundo

Na aula de [[wiki/concepts/elementos-de-composicao]], o fundo decorativo fica em baixo contraste para não competir com o ponto focal: com o azul "em 100%", "eu estou tirando a atenção". "O background tem esse nome justamente por isso, ele cria contraste com aquilo que eu quero apresentar" ([[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]]). `[external]` WCAG não exige contraste de elemento decorativo (https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), mas o texto por cima precisa passar no pior ponto do fundo.

## Contraste entre foto orgânica e letra geométrica

O Madero mostra hambúrgueres e pessoas (orgânicos) e contrasta com tipografia sem serifa e elementos regulares, "essa dualidade de contraste"; um site de arquitetura faz o inverso, formas regulares com serifa "para contrastar" ([[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]]).

## Escurecer a imagem para o texto

Para pôr texto branco em foto clara: baixar saturação ou brilho, ou sobrepor capa preta com opacidade ([[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]]). Ver [[wiki/concepts/texto-sobre-imagem]].

## Contraste no botão

Em [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]]: o fundo do botão leva "a cor de contraste da sua paleta" para chamar a atenção. No [[wiki/entities/frontpush]], o azul contra o preto se repete em labels ("3 em 1"), ícones e botões: "um ímã na visão do usuário". `[skill: ux-ui-mentor]` O texto do botão precisa de 4.5:1 com o fundo (3:1 se for texto grande). Ver [[wiki/concepts/botoes-em-interfaces]].

## Contraste pela forma do botão

No Madero, botões retos e letra sem serifa "vêm aqui justamente para poder causar um contraste maior" com as fotos de comida e de pessoas ([[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]]). Ver [[wiki/concepts/formas-de-botoes]].

## Texto do botão sobre gradiente

"Sempre é importante a gente garantir a melhor legibilidade possível": no gradiente laranja, branco e preto servem, mas "o preto vai ter um contraste melhor"; no amarelo, só o preto ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]). `[external]` Texto de 16 px pede 4,5:1 (WCAG 1.4.3), medido no ponto mais claro do gradiente.

## Contraste nas três notas do WCAG

Em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]], contraste é a primeira recomendação de [[wiki/concepts/acessibilidade]]: "saber distinguir elementos dos outros", garantir legibilidade, e "bem aplicado, ele até guia [...] o usuário pela sua jornada". Há três notas: A mínima, AA média e AAA alta. Násser mira "no mínimo" em AA e reserva AAA para interfaces de governo de massa, como a do auxílio emergencial. Checkers: Contrast Ratio e [[wiki/entities/who-can-use]]. `[external]` No [[wiki/concepts/wcag]], contraste só tem critérios AA (1.4.3) e AAA (1.4.6); não existe nota A de contraste.

## Contraste e tamanho puxam a leitura em Z

Em [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]]: "pelo contraste e pelo tamanho, eu tendo a olhar aquilo que é maior". Na leitura em Z, headline, ilustração e CTA viram pontos de atenção por contraste ([[wiki/concepts/hierarquia-visual]]).

## Contraste fica para o protótipo final

No processo de wireframes, o "contraste bem colocado entre as cores" é decisão do protótipo final, com o [[wiki/concepts/style-guide]]; o [[wiki/concepts/wireframe]] fica em escala de cinza para continuar fácil de mudar ([[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]]).

## Cor de contraste no fundo, em pouca quantidade

Na prática de elementos de composição, os planetinhas usam "a cor de contraste do branding" (laranja no slide "W7"), com sombra da mesma cor a 30%; o resto (órbitas pontilhadas, linhas) fica em cinza baixo sobre preto ([[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]]). `[skill: ux-ui-mentor]` sombra colorida no escuro lê como brilho, não como elevação.

## Contraste como objetivo da cor

Na abertura do módulo de [[wiki/concepts/teoria-das-cores]], contraste é o primeiro dos seis objetivos da cor. Para mandar algo para segundo plano, "eu diminuo o contraste dela com relação ao background"; para acentuar, aumento. Sites de notícia e a [[wiki/entities/apple]] (mesmo peso tipográfico, branco x cinza) são os exemplos ([[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]). `[skill: ux-ui-mentor]` O texto secundário de baixo contraste ainda precisa de 4.5:1. Pares complementares dão contraste forte ([[wiki/concepts/harmonia-de-cores]]); a [[wiki/concepts/regra-60-30-10]] reserva o acento para o CTA.

## Key Sources

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — contraste para acessibilidade e para o CTA
- [[wiki/sources/o-que-e-ux-ui-design]] — contraste como princípio de UI
- [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] — Isolation Effect
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — contraste para acessibilidade e como definidor de prioridade (tamanho, peso, cor, preenchimento)
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — mais contraste para idosos; cor e contraste como melhor prática
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — título chama atenção por contraste e tamanho; o espaço complementa
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — botão reto em interface orgânica como contraste proposital
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — como escrever em imagens: letra branca e capa de gradiente
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — Who Can Use como checker; notas "A, 2A, 3A"; peso e tamanho como contraste de título
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — seta azul em botão azul como ícone neutro; preto e branco como extremos de luz
- [[wiki/sources/elementos-de-composicao-ambiencia-background-branding-empty-screens]] — fundo decorativo em baixo contraste para preservar o ponto focal
- [[wiki/sources/formas-geometricas-organicas-exemplos-dropbox-madero-coco-bambu-nubank]] — Madero e arquitetura: contraste entre forma e tipografia
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — texto branco sobre imagem: saturação, brilho ou capa preta
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — elemento na cor da marca sobre fundo cinza/preto como "ímã na visão do usuário" para o motion
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — retângulo preto a 20% de opacidade atrás do título branco; editor de imagem do Figma (exposição, contraste)
- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — fundo do botão na cor de contraste da paleta; o "ímã"
- [[wiki/sources/formas-de-botoes-reto-arredondado-circular-chanfrado-diagonal-hexagonal]] — botões retos como contraste no Madero
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — branco ou preto no gradiente laranja; preto obrigatório no amarelo
- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — aula de acessibilidade: contraste guia a jornada; A/AA/AAA; AA no mínimo, AAA para governo
- [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]] — contraste e tamanho como pontos de atenção na leitura em Z
- [[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]] — contraste é decisão do protótipo final, não do wireframe cinza
- [[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]] — planetinhas na cor de contraste com sombra da própria cor
- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — contraste como objetivo da cor; segundo plano com contraste menor; 60-30-10
