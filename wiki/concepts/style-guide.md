---
type: concept
title: "Style guide (guia de estilo)"
aliases: ["guia de estilo", "styleguide", "style-guide", "guia de estilos", "UI kit", "guia visual", "style guide de UI", "guia de estilo de interface", "style guide de interface", "mapa de design"]
date_created: 2026-11-15
date_updated: 2026-11-16
source_count: 9
tags: [ui, ui-design, style-guide, design-system, consistencia, cor, tipografia, figma, documentacao, handoff, design-tokens, css, prototipagem]
skill: ux-ui-mentor
status: stub
---

# Style guide (guia de estilo)

Documento que fixa as decisões visuais de um projeto (cores, tipografia, botões, estados, sombras, radius, ícones, inputs, cards) para que todo mundo aplique as mesmas, no arquivo de design e na implementação. As aulas do curso do [[wiki/entities/frontpush]], com [[wiki/entities/nasser|Násser]], descrevem o style guide de jeitos que se completam:

- "Meio que um guia para poder ter consistência no meu design", montado quando o projeto caminha para o protótipo final, "onde eu literalmente vou aplicar as cores e padrões com mais teor de fidelidade" ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]). Reúne as regras dos módulos anteriores numa referência só.
- O documento que padroniza o estilo de um produto e o entrega ao time de desenvolvimento. Cobre duas coisas: o **design** (cores, tipografia, cards, border-radius, marca, elementos de composição) e o **comportamento** (telas, especificações, guia de interação, flow, jornada) ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).
- O objetivo é "consistência tanto no Figma, tanto na documentação", e o style guide é "o mapa que traduz o design para o CSS" ([[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]).

Ver [[wiki/concepts/consistencia-visual]], o motivo de existir.

## Onde fica no processo

- É a terceira etapa do [[wiki/concepts/workflow-de-interface-web]] ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]).
- Vem depois de pesquisa, [[wiki/concepts/wireframe]] e [[wiki/concepts/grid-de-colunas|grids]], no protótipo final. É o momento de "passar o bastão" para o dev, por isso carrega "documentação, entrega, colaboração, comunicação" ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).
- No processo de wireframes, é o último passo: o "protótipo final com o auxílio dos style guides". Lá entram as cores auxiliares, onde vai gradiente, o [[wiki/concepts/contraste]] entre as cores e o alinhamento ao branding, além de "cada decisão de tela, de botão, de comportamento, de cores e animação". O wireframe cinza fica fora disso de propósito; ver [[wiki/concepts/fidelidade-de-prototipo]]. Nessa aula, o style guide é anunciado como o próximo tópico do curso ([[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]]).

## O que entra

O que entra depende do **level de complexidade** do projeto e do tamanho do time ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). Cada aula dá a sua lista:

| Fonte | O que lista |
|---|---|
| Case do [[wiki/entities/nubank]] ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]) | branding e cor, com o porquê de cada cor; [[wiki/concepts/tipografia]] no desktop e no mobile, "para poder garantir acessibilidade e legibilidade"; [[wiki/concepts/botoes-em-interfaces|botões]], inputs, [[wiki/concepts/grid-de-colunas|grids]], [[wiki/concepts/icones-em-interfaces|ícones]], cards, mockups |
| Aula de documentação ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]) | versão light e dark; paleta de cores com os hexadecimais prontos para Sass ou variáveis CSS; tipografia de h1 a span, desktop x mobile; [[wiki/concepts/familia-de-icones|família de ícones]] ou ícones próprios para download; cards e botões com estados (normal, hover, selecionado) e a transição entre eles; inputs com hover, focus, erro, warning e sucesso ([[wiki/concepts/feedback-do-sistema]]); [[wiki/concepts/elementos-de-composicao]]; animações e comportamento, com nota, descrição e link de apoio |
| Aula prática no [[wiki/entities/pegasus-design-system]] ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]) | cores, tipografia (desktop e mobile), controladores, cards e radius, blur, família de ícones, fotografia, elementos de composição, grid e componentes |
| Aula 16, documentação para dev ([[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]) | ver abaixo |

Na aula 16 ([[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]):

- **Sempre:** gradiente (ângulo e paradas), camadas de `box-shadow` ([[wiki/concepts/sombra-em-interfaces]]), cor em RGBA e hexadecimal, [[wiki/concepts/border-radius]] por tamanho de componente.
- **Quando importa:** dimensões e padding. No botão, padding em vez de largura fixa ([[wiki/concepts/botoes-em-interfaces]]).
- **Não entra:** o `position` gerado pelo Figma; o layout vai para flexbox e grid.
- **Estados de cada módulo:** normal, hover e clicável ([[wiki/concepts/feedback-do-sistema]], [[wiki/concepts/maquina-de-estados-ui]]).

Regra para decidir: "se coloque no papel do desenvolvedor. Se você perceber que ele precisa, documente!". O dev pode não abrir o [[wiki/entities/figma]], então tudo precisa estar escrito, até num PDF ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Citado em outras aulas

- O hover do botão, uma [[wiki/concepts/sombra-em-interfaces|sombra]] suave na cor da marca, deve ficar "muito bem claro no meu style guide"; os padrões de tamanho de texto ficam para a [[wiki/concepts/tipografia]] e para o style guide da parte de interfaces web, que vai ficar para download ([[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]). Estados como o hover entram aqui ([[wiki/concepts/feedback-do-sistema]]).
- A aula prática de ícones promete uma seção de style guide para os ícones próprios ([[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]).

## No Figma

O style guide é montado num arquivo do [[wiki/entities/figma]]. As partes repetidas viram **estilos** reutilizáveis ([[wiki/concepts/estilos-no-figma]]) de três tipos: texto, cor e efeito ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]). A página da aula 16 diz que a aula 15 do curso cria esses três estilos e a dava como não ingerida; a aula 16 parte deles para a documentação voltada ao desenvolvedor ([[wiki/concepts/handoff-design-dev]]) ([[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]). Inferência: a aula prática de estilos de cor, texto e efeito, hoje ingerida, trata do mesmo conteúdo.

## Documento vivo

- **Comece antes de ficar perfeito:** "o tanto que é importante você não esperar ficar perfeito para poder começar a escrever" ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).
- **Um link, não cópias:** em vez de "PDF com cópia versão 1 [...] cópia versão 2", compartilha-se o link do arquivo. Time, dev e cliente veem a versão atual, e a edição é em tempo real ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]); quem tem o link recebe as mudanças ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

É a mesma ideia de [[wiki/concepts/living-documentation]], aplicada a design.

As duas aulas dão peso diferente ao PDF: a de documentação aceita que tudo esteja escrito "até num PDF" para o dev que não abre o Figma; a prática critica as cópias versionadas em PDF e prefere o link.

## Nomes que o dev entende

- Labels iguais às do código (`card-hover`, `$orange`) reduzem tradução entre design e dev ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]). Ver [[wiki/concepts/design-tokens]].
- "Projetar as labels para que o time de design e dev possam entender." O design pode criar uma label "que não tem nada a ver com o que o dev costuma utilizar", então "é legal conversar e colaborar" ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Onde buscar referência

Community do Figma (design systems, wireframes, UI Kits) e guidelines de [[wiki/entities/apple]], Google ([[wiki/entities/material-design]]), Microsoft, IBM e Airbnb ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Style guide x design system

`[skill: ux-ui-mentor]` A skill define design system como "acordo compartilhado entre design e dev", em camadas: design tokens → componentes base → componentes compostos → patterns → guidelines. Um style guide documenta a linguagem visual; um design system junta essa linguagem a componentes reutilizáveis, tokens com nome e regras de uso, mantidos como produto. Sem tokens e componentes em código, o style guide descreve; com eles, vira fonte única de verdade.

`[skill: ux-ui-mentor]` Onde os style guides das aulas ficam nessa escala:

- O style guide da aula cobre a parte visual (os valores e os componentes desenhados) num arquivo do Figma, ficando na camada de tokens (valores e nomes), com parte da documentação de componentes.
- O da aula de documentação também cobre os estados de componentes e parte das guidelines de comportamento.
- O da aula 16 está no meio do caminho: tem estilos e estados, mas valores sem nome de token.

`[skill: ux-ui-mentor]` Para virar design system faltam nomes de token, estados completos de cada componente (hover, focus, active, disabled, loading), variantes com regra de uso, regras de uso em geral e acessibilidade. Ver [[wiki/concepts/mobile-design-system]] para a mesma ideia em código, com tokens em camadas, e como o passo seguinte, em escala de produto.

`[external]` Um "style guide" costuma ser a parte visual e de marca de um design system, que também inclui a biblioteca de componentes e a documentação de uso (https://www.nngroup.com/articles/design-systems-101/).

## Relação com outros conceitos

- [[wiki/concepts/consistencia-visual]]: o motivo de existir.
- [[wiki/concepts/mobile-design-system]]: o passo seguinte, em escala de produto.
- [[wiki/concepts/feedback-do-sistema]]: estados como o hover entram aqui.
- [[wiki/concepts/handoff-design-dev]]: o style guide é o veículo da entrega ao dev.
- [[wiki/concepts/design-tokens]]: os nomes que o style guide ainda não dá aos valores.

## Position fica fora, comportamento fica dentro

O style guide descarta o `position` do Figma, mas a aula de CSS do curso ([[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]) mostra que menu fixo e sticky são decisões de interface. Cabe anotar esse comportamento no guia ("menu gruda no topo"). Ver [[wiki/concepts/menu-fixo]].

## Style guide como fonte das variáveis (FrontPUSH, Sass)

Em [[wiki/sources/frontpush-variaveis-sass]], o style guide do projeto Nubank é a origem das `$variáveis`: "está tudo documentado, as determinadas cores com seus hexadecimais". Um erro no próprio guia: a fonte aparecia como Montserrat, mas é Sora.

## Key Sources

- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — definição, momento no workflow e conteúdo do style guide do Nubank
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — definição, levels de complexidade, lista de padronização, evolução por link, inspect, labels
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]] — documentação viva, link compartilhado, referências, estilos de cor, texto e efeito
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]] — objetivo do style guide, o que documentar, três estados, "mapa de design"
- [[wiki/sources/wireframes-parte-3-passo-a-passo-fidelidade-escala-de-cinza-segredo]] — último passo do processo; entra só no protótipo de alta fidelidade
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — hover a documentar "muito bem claro no meu style guide"; tamanhos de texto; style guide para download prometido
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — seção de style guide para ícones próprios prometida
- [[wiki/sources/position-css-static-relative-absolute-fixed-sticky]]: menu fixed/sticky como comportamento a documentar
- [[wiki/sources/frontpush-variaveis-sass]]: style guide → variáveis do Sass; fonte errada no guia
