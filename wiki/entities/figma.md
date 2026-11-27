---
type: entity
title: "Figma"
aliases: ["figma.com"]
date_created: 2026-04-22
date_updated: 2026-11-27
source_count: 65
tags: [figma, design, ferramenta, design-first]
skill: tech-mentor-frontend
status: stub
---

# Figma

Ferramenta de design colaborativo baseada em browser. Principal ferramenta da abordagem [[design-first]].

## Papel por abordagem

| Abordagem | Papel do Figma |
|---|---|
| Design First | Fonte de verdade — tudo começa aqui |
| Code First | Pouco ou nenhum uso |
| Design Engineer | Ferramenta de teste e validação, não fonte de verdade |

## Risco em times pequenos

Em times onde a mesma pessoa faz design e código, o Figma tende a ficar desatualizado conforme o código evolui — ver [[design-first]].

## Como ponto intermediário de um pipeline com IA

Fluxo observado: ferramenta de geração de UI por IA (ex.: [[wiki/entities/ux-pilot]]) gera o conceito de UI/UX → exporta para o Figma → o Figma é conectado, via MCP, a uma IA de código (Cursor, Claude Code) para implementação. Nesse pipeline, o Figma deixa de ser o ponto de partida (como no design-first clássico) e passa a ser um artefato intermediário de handoff entre a ferramenta de concepção e a IA de implementação.

## Figma e Protótipo com IA

[[wiki/sources/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin]]: o design deixa de ser "caixa por caixa no Figma do zero" e passa a usar design system com IA para prototipar; ver [[wiki/concepts/design-engineer]].

## Ferramenta de Prototipagem para Aprender UI

[[wiki/sources/como-aprender-ui]] manda escolher uma ferramenta de prototipagem como primeiro passo e usa o Figma no curso, citando Adobe XD, Sketch e InVision como alternativas "muito parecidas" em metodologia. `[external]` Hoje o Adobe XD está em modo de manutenção e o InVision encerrou os serviços de design em 2024 (ver a fonte).

## Export e plugins de imagem

Em [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]: o painel de export oferece escalas (0,5x, 0,75x, 1,5x, 2x, 3x) para gerar uma imagem por dispositivo; o plugin do [[wiki/entities/unsplash]] traz fotos já um pouco reduzidas; o plugin TinyImage Compressor comprime e ajusta qualidade. Ver [[wiki/concepts/otimizacao-de-imagens]].

Na parte 2 ([[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]]): ao puxar só um lado de uma imagem, o Figma faz "meio que um crop automático" e preserva o [[wiki/concepts/aspect-ratio]]; a Pen Tool vetoriza logo recebida em baixa definição.

Na parte 3 ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]): máscara com gradiente radial e [[wiki/concepts/blend-modes]] (color dodge, lighten, difference) substituem o Photoshop na composição; imagens padronizadas na mesma resolução e proporção antes do handoff.

## Plugins de ícones

Na aula de ícones, o plugin [[wiki/entities/iconly]] v2.3 é usado para comparar com o [[wiki/entities/feather-icons]] ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]).

## Construir ícones: grid, constraints e componentes

Em [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]]: com zoom num frame pequeno, o Figma mostra o pixel grid; o [[wiki/concepts/grid-de-icones|grid]] do ícone é agrupado (Ctrl G), com opacidade de 20–30% e travado; constraints definem "como o objeto vai se comportar quando eu modificar as dimensões do frame" (top/left fixa, right-bottom inverte, scale escala); o ícone vira componente e as instâncias crescem de 16 a 36 mantendo as proporções. A aula diz que o shape de triângulo já deixa dois pixels vazios para o play ficar no centro óptico (não verificado; [[wiki/concepts/centralizacao-optica]]).

## Espaçamento na prática

Em [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]]: Preferences → Nudge amount com big nudge de 8 faz Shift + seta mover de 8 em 8 (padrões do Figma: 1 e 10); Alt com o mouse sobre outro elemento mede a distância até o selecionado; Ctrl + G agrupa antes de medir; com vários elementos alinhados selecionados, digitar a distância (128) os separa por igual. Layout grid de 12 colunas de 72 com gutter de 32, centralizado. Ver [[wiki/concepts/grid-de-colunas]] e [[wiki/concepts/escala-de-espacamento]].

## Imagens e plugins de ilustração na prática

Em [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]]: importar arrastando, por Place Image ou Ctrl Shift K; instalar plugin pela Community; editor de imagem nativo (exposição, contraste, saturação, temperatura; fit, crop, fill); plugins Blobs, dois "isometric", um de ondas e "skill-depth"; isometria sem plugin (45°, Ctrl G, altura a 50%); TinyImage Compressor; export pelo frame. Ver [[wiki/concepts/ilustracao-isometrica]].

## Pen Tool e Bend Tool

Em [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]]: Pen Tool para contornar uma imagem de referência; Bend Tool para arredondar os pontos; duplo clique no elemento e clique no ponto abrem as duas alças; opacidade para ver por baixo; efeitos de sombra interna e externa. Ver [[wiki/concepts/vetorizacao-com-pen-tool]].

## Plugins de ícones e constraints na prática

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: comunidade → "icons" para achar arquivos e plugins (Feather, Bootstrap Icons, Material Design Icons, Iconify); duplicar o arquivo do Piqo; círculos com Ctrl D, Shift e opacidade; cor de branding desconectada do estilo para mudar a opacidade; ícone do plugin chega como frame, e [[wiki/concepts/constraints-no-figma|constraints]] (top/left, center) evitam que ele deforme ao esticar o frame.

## Botões e sombras na prática

Em [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]]: Ctrl D ou Ctrl C/Ctrl V para duplicar; botão direito → bring to front; medições automáticas com linhas ao arrastar; plugin Smooth Shadow (layers, alpha, offset, blur, color); duplo clique e "edit style" para ler o estilo de sombra de um arquivo da Community ([[wiki/entities/pegasus-design-system]]). A aula mede o padding à mão; `[external]` o Auto Layout manteria o padding fixo com a largura seguindo o texto.

## Os três primeiros passos do workflow

Pesquisa, wireframes e protótipo final de UI, os três passos do [[wiki/concepts/workflow-de-interface-web]] cobertos no módulo, acontecem no Figma (o logo aparece ao lado deles no slide); a biblioteca de wireframes do Notion é copiada para o Figma dos alunos ([[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]]).

## Style guide: share, grupos de estilo e inspect

Share por link para os alunos copiarem e receberem as atualizações; grupos de estilo pré-definidos (texto, cor, sombra); aba inspect com o CSS do elemento selecionado "sem ser um grupo" ([[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]]).

## Estilos e compartilhamento na prática

Na aula prática de [[wiki/concepts/style-guide]], color, text e effect styles com nome `Grupo / nome`, edit style, add description e detach ("correntinha quebrando"); ver [[wiki/concepts/estilos-no-figma]]. Também: share por link (ver ou editar), set as thumbnail para a capa, save local copy e a Community como fonte de design systems, wireframes e UI Kits ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Inspect e style guide

Em [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]]: o Inspect dá width, height e o CSS de `box-shadow` e gradiente, e "com relação ao estilo em si, o Figma acerta muito"; o posicionamento gerado "não condiz muito com a realidade" e é descartado (flexbox e grid no código). Padding ajustado na aba Design. `[external]` Com Auto Layout, o CSS gerado sai em flexbox. Ver [[wiki/concepts/handoff-design-dev]].

## Wireframes no Figma

Em [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]], o Figma aparece ao lado do papel como lugar do wireframe: "onde eu posso simplesmente clicar e arrastar e apresentar uma estrutura inicial que seja muito próxima daquilo que eu vou implementar".

## Big Nudge e tamanhos de texto

Em [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]]: Preferences, Nudge Amount, Big Nudge de 8 ("quando você segura Shift, ele vai dando espaços de oito pontos"); o menu de tamanhos de texto (14, 18, 24, 36, 48) como prova de que a regra dos oito já está na ferramenta.

## Grid System Library

Em [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]]: kit gratuito de grids de iOS, Android e Bootstrap com versão para Figma (doação opcional de US$ 4).

## Layout Grid

Em [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]]: seleciona o frame e adiciona em Layout Grid (o padrão é um grid de 8 pontos). No módulo colunas, 12, tipo Center, width 72 e gutter 36. O olhinho esconde o grid quando "fica muito poluído". Distribuir horizontal spacing iguala o espaço entre elementos agrupados. `[external]` Tipos de column grid: Stretch, Left, Center, Right (https://help.figma.com/hc/en-us/articles/360040450513).

## Elementos de composição na prática

Em [[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]]: stroke 3 sem preenchimento, dash "2, 10" com cap round em elipses, Shift para crescer de forma proporcional, conta-gotas para a cor da sombra, drop shadow com spread negativo, gradiente linear a 45° numa linha para cometas.

## Cores em código

A abertura do módulo de cores promete uma aula prática para representar cores em código no Figma (HSB, hexadecimal, RGB x CMYK), base para compor paleta e variar cores ([[wiki/concepts/modelos-de-cor]]; [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]).

## Move x Scale e agrupar

Em [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]]: Ctrl+G agrupa e Ctrl+Shift+G desagrupa; Fill e stroke pintados por parte do ícone. Aumentar com o Move (V), mesmo com Shift, mantém a espessura do stroke; o Scale aumenta "de forma proporcional". `[external]` O atalho do Scale é K (https://help.figma.com).

## Seletor de cor

Em [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]: o fill abre a "caixinha de diálogo" de cor, "muito comum em toda e qualquer ferramenta de prototipagem". Mostra os modos Hex, RGB, CSS (RGB + alfa) e HSB; trocar de modo converte a mesma cor (`8FFF00` → 143, 255, 0). Ver [[wiki/concepts/modelos-de-cor]].

## Cores na prática

Seletor em [[wiki/concepts/modelo-de-cor-hsb|modo HSB]], conta-gotas sobre um print, overlay e opacidade para tingir neutros, e a paleta como base dos estilos do Figma ([[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]]).

## Modo luminosity

Na aula de variação de cores, o tipo de layer luminosity transforma o espectro em escala de cinza e mostra o [[wiki/concepts/luminosidade-das-cores]]; a prática de variação no Figma fica para a aula seguinte ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]).

## Escala de tamanhos de fonte

Násser recomenda "a escala do próprio Figma" para fontes: começa em 9 e cresce em passos maiores no topo (96 → 144 → 288) ([[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]]). Lista exata não verificada.

## Line-height no Figma

Em [[wiki/sources/altura-de-linha-e-largura-do-texto]], alterar o line-height no Figma faz a caixa do texto crescer; o valor é dado em porcentagem (140% equivale a `line-height: 1.4` no CSS). Ver [[wiki/concepts/altura-de-linha]].

## Google Fonts embutido

Em [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]], o Figma "espelha de forma automática" o [[wiki/entities/google-fonts]]: fonte nova aparece sem baixar nem instalar. A demonstração da monoespaçada (fileira de "i" contra "Monospaced") também roda no Figma. `[external]` No Linux o Figma não usa fontes locais (https://help.figma.com/hc/articles/360039956894).

## Inspect e tipografia

Em [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]]: a aba Inspect mostra o [[wiki/concepts/css]] do texto (`letter-spacing` em `em`, `font-family`, `font-style`, `font-weight`); trocar para Medium vira `font-weight: 500`. O Figma só lista os pesos que a fonte tem (a Mukta vai de extra light a extra bold), o que evita o "estilo falso" ([[wiki/concepts/peso-tipografico]]). A opção "case" põe o texto em [[wiki/concepts/texto-em-maiusculas|maiúsculas]].

## Justificado na prática

Em [[wiki/sources/alinhamento-e-espacamento-de-texto]], o autor tenta mostrar no Figma o espaçamento irregular do texto justificado e admite que "não deu para perceber muito". Ver [[wiki/concepts/alinhamento-de-texto]].

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] copia cores, fontes e espaçamentos do painel de inspeção do Figma para o CSS dos cards, menos o posicionamento, "uma parada muito absoluta". Diverge do layout de propósito no modal de busca (um campo só, botão ao lado): "espero que me perdoem especialmente quem construiu layout".

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], [[wiki/entities/mayk-brito|Mayk]] abre o layout do Proffy no Figma (é preciso login para ver as cores), usa +/- para zoom e espaço para arrastar, e copia as cores para variáveis CSS. O painel de CSS do Figma "são só sugestões".

## Na NLW #2, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]], [[wiki/entities/mayk-brito|Mayk]] compara a página com o layout de Thiago (1440 × 820) e mede os espaços do grid (86 e 87 px), mas avisa: "não precisa dessa minúcia toda".

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], o layout tem um estado vazio ("Nenhum professor encontrado com a sua pesquisa") e uma versão 2.0 com página de sucesso do cadastro, que vira desafio.

## Smooth Shadow → variável Sass

Em [[wiki/sources/frontpush-variaveis-sass]], a sombra do botão é feita com o plugin Smooth Shadow e o CSS copiado do Inspect para uma variável do Sass; para mudar, ajusta-se no Figma e recopia-se.

## Variações prontas antes do Sass

Em [[wiki/sources/frontpush-funcoes-sass]]: as versões clara e escura das cores saem do Figma e viram variáveis do Sass, em vez de `darken`/`lighten`; o bloco vermelho de 30% no layout do Nubank aparece como RGBA no Inspect.

## Na NLW #2, dia 5 (Diego Fernandes)

Layout da versão 2.0 do Proffy (web e mobile: login, cadastro, perfil, onboarding) entregue como desafio. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]].

## Image Tracer (FrontPUSH, otimização aula 03)

Em [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]], o plugin Image Tracer vetoriza um logo da Adidas buscado no Google; a Pen Tool fica como alternativa manual. Imagens exportadas do Figma sem otimizar são citadas como erro comum.

## Gradiente para a demo de rotate (FrontPUSH, básico CSS aula 01)

Em [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]], [[wiki/entities/nasser|Násser]] copia do Figma um gradiente "blue-red" para ver o `rotate` girar.

## Espelho do SVG (FrontPUSH, propriedades SVG aula 01)

Em [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: "pense como um espelho do Figma". Export em PNG, JPG, SVG e PDF; o SVG "não muda em nada"; layer blur, background blur e inner shadow "a gente também consegue fazer no SVG"; Ctrl-Shift-G (desagrupar) mostra os vetores separados. Precisão: background blur não tem equivalente em filtro SVG (`backdrop-filter` é do CSS).

## Origem do código SVG (FrontPUSH, propriedades SVG aula 03)

Em [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: "eu faço pelo Figma" e nunca entendeu o `d` do path; `fill` é "muito parecido com o do Figma"; efeitos viram filtros nos `defs`, gradiente com `stop-color`, e o export repete IDs como `filter0_d`.

## Escolha pela comunidade

Na [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga|aula 04 do módulo Monetização e Freelancer]], [[wiki/entities/nasser|Násser]] diz que o designer deve escolher o Figma pela comunidade: features, plugins e "muito material [...] de forma gratuita" no Figma Community. "Isso é ferramenta, não é o mais importante."

## Arquivo do Dash Class

Na [[wiki/sources/frontpush-dashboards-introducao-para-que-serve-utilidades-tipos|aula de abertura do módulo de dashboards]], o módulo de dashboards vive num arquivo do Figma com fluxos, modelos de wireframe e uma página "de aulas" com os slides. Ver [[wiki/entities/dash-class]].

## Arquivo do DashClass por dentro

Na [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass|aula 02 do módulo de dashboards]]: abas de inspirações (prints de cards, gráficos e esquemas), style guide e grids, telas dos fluxos (home ainda em wireframe) e página de aulas.

## Layout grid tipo Left (DashClass)

Na [[wiki/sources/frontpush-dashboards-grids-e-patterns|aula 03 do módulo de dashboards]]: grid de 12 colunas tipo Left (não Center nem Stretch), largura fixa de coluna, gutter e offset para a sidebar, em frame de 1440 × 900; para inspecionar, ligar a visibilidade do grid e abrir os ajustes.

## Páginas e estilos do DashClass

Na [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos|aula 07 do módulo de dashboards]]: páginas Cover, Inspirations, StyleGuide & Grids, UI DashClass e Aulas; estilos de texto (heads, body), cor (cian, blue, black, white, gradient, gray, auxiliary) e grid (Desktop, iOS, Android, iPad, Dashboard 1 a 3).

## Key Sources

- [[wiki/sources/frontpush-monetizacao-freelancer-como-conseguir-a-primeira-vaga]]: escolher Figma pela comunidade
- [[wiki/sources/novos-cargos-ia-e-hunting-de-vagas-fora-do-linkedin]] — design deixa de montar do zero no Figma
- [[wiki/sources/design-first-vs-code-first-referencias]]
- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
- [[wiki/sources/como-aprender-ui]] — Figma como ferramenta escolhida no curso de UI
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — onde o curso compara pacotes de ícones (Feather Icons, Iconify, Iconly)
- [[wiki/sources/espaco-em-branco-whitespace-micro-macro-grid-8-pontos]] — wireframe de menu e análise de print da busca do Google; Figma delimita cards com linhas, o Google não
- [[wiki/sources/formas-geometricas-organicas-predominancia-harmonia]] — comparação ao vivo de fonte, botão e cor para uma loja de bebês
- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]] — export multi-escala, plugins do Unsplash e TinyImage, demonstração de SVG
- [[wiki/sources/imagens-e-ilustracoes-aspect-ratio-pessoas-ponto-focal-texto]] — crop automático contra distorção; Pen Tool para vetorizar logo; demonstração de grid e gradiente
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — blend modes e máscara com gradiente; padronização das imagens
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — ilustrações em SVG feitas no Figma; modelos de apps prometidos
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — plugin Iconly para comparar famílias
- [[wiki/sources/icones-parte-2-hierarquia-tamanho-simetria-grid-constraints]] — pixel grid, grid de ícone travado, constraints em scale, componente
- [[wiki/sources/espacamento-e-linhas-espaco-vs-meio-sistema-geometrico-padding]] — prática da aula de espaçamento prometida para a aula seguinte
- [[wiki/sources/espacamento-e-linhas-pratica-figma-grid-12-colunas-nudge-8pt]] — nudge de 8pt, Alt para medir, grid de 12 colunas, distribuição a 128
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — caminho do SVG traçado no Figma pensando na animação; impede esticar imagem; export em tamanhos
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — ilustração que imita o Figma; plugins de isometria; TinyImage
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — importar (Place Image, Ctrl Shift K), instalar plugin, editor de imagem, plugins de ilustração e isometria, TinyImage, export pelo frame
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — SVG do unDraw editável no Figma; mockup de iPhone com guias da régua, opacidade 20%, subtração; export do frame em SVG
- [[wiki/sources/imagens-e-ilustracoes-vetorizar-icones-figma-pen-tool-bend-tool]] — Pen Tool, Bend Tool e alças para vetorizar ícone de telefone
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — plugin do Feather Icons prometido para a aula prática de ícones
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — comunidade, plugins de ícones, Ctrl D, Ctrl G, constraints
- [[wiki/sources/botoes-pratica-figma-padding-gradiente-contraste-smooth-shadow]] — botão de 56 px, bring to front, plugin Smooth Shadow, edit style no Pegasus
- [[wiki/sources/interfaces-web-introducao-workflow-grids-pagemap-wireframes-style-guide]] — três primeiros passos do workflow; biblioteca de wireframes copiada para o Figma
- [[wiki/sources/style-guide-documentacao-padronizacao-elementos-visao-do-desenvolvedor]] — share por link, grupos de estilo, aba inspect
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]] — color, text e effect styles; edit style, detach; share, set as thumbnail, save local copy
- [[wiki/sources/style-guide-pratica-parte-2-documentacao-para-dev-sombra-gradiente-estados]] — Inspect: copiar box-shadow e gradiente; descartar position
- [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]] — wireframe por "clicar e arrastar"
- [[wiki/sources/grids-parte-2-colunas-bootstrap-breakpoints-8-pontos]] — Big Nudge de 8; menu de tamanhos de texto
- [[wiki/sources/grids-pratica-2-material-de-apoio-bootstrap-material-design-flexbox-grid]] — Grid System Library para Figma
- [[wiki/sources/grids-pratica-figma-12-colunas-alinhamento-blocos-equilibrio-menu]] — Layout Grid de 12 colunas tipo Center, olhinho do grid, distribuir horizontal spacing
- [[wiki/sources/elementos-de-composicao-pratica-figma-orbitas-pontilhado-cometas-playstation]] — stroke, dash 2, 10, cap round, conta-gotas, sombra, gradiente
- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — aula prática de códigos de cor prometida
- [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]] — Ctrl+G / Ctrl+Shift+G; Move mantém o stroke, Scale aumenta proporcional
- [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]] — seletor de cor e modos Hex, RGB, CSS e HSB (autoria inferida)
- [[wiki/sources/paleta-de-cores-na-pratica-dribbble-hsb-variacoes-cores-neutras]] — HSB, conta-gotas, overlay para neutros
- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — modo luminosity no tipo de layer; prática de variação prometida
- [[wiki/sources/tipografia-escala-tamanho-hierarquia-textual-escala-do-figma]] — escala de fonte do Figma
- [[wiki/sources/altura-de-linha-e-largura-do-texto]] — line-height em % aumenta a caixa do texto
- [[wiki/sources/classificacoes-tipograficas-serifa-sem-serifa-script-monoespacada-display]] — espelho do Google Fonts; demonstração da monoespaçada
- [[wiki/sources/tipografia-negrito-italico-tracking-kerning-maiusculas]] — Inspect para letter-spacing e font-weight; pesos reais da fonte
- [[wiki/sources/alinhamento-e-espacamento-de-texto]] — demonstração do justificado
- [[wiki/sources/frontpush-layout-css-botao-hover-flexbox-media-query]]: o design feito no Figma traduzido "para o CSS de maneira plena"
- [[wiki/sources/frontpush-position-css-relative-absolute-coordenadas]]: eixos X e Y desenhados para explicar o `position: absolute`
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: inspeção de estilos; divergência consciente do layout
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: design do layout do YouTube com grid de 12 colunas (96 px, gutter 24) que vira o container (ferramenta inferida)
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: cores do Proffy copiadas do Figma
- [[wiki/sources/nlw-2-dia-2-landing-page-grid-pagina-de-estudo-proffy]]: NLW #2, dia 2: medir o layout e não exagerar na minúcia
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: estado vazio e versão 2.0
- [[wiki/sources/frontpush-variaveis-sass]]: Smooth Shadow e Inspect → variável Sass
- [[wiki/sources/frontpush-funcoes-sass]]: variações de cor no Figma, não no Sass
- [[wiki/sources/nlw-2-diego-fernandes-dia-5-listagem-filtros-api-favoritos-mobile-proffy]]: NLW #2, Diego, dia 5: Proffy 2.0
- [[wiki/sources/frontpush-otimizacao-de-imagens-svg-webp-lazy-loading]]: FrontPUSH, otimização aula 03: plugin Image Tracer
- [[wiki/sources/frontpush-propriedade-transform-parte-1-translate-scale-rotate-skew-matrix-perspectiva]]: FrontPUSH, mini curso de CSS Animations, básico CSS aula 01: gradiente copiado para a demo de rotate
- [[wiki/sources/frontpush-propriedades-svg-introducao-o-que-e-por-que-usar]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 01: espelho do SVG; efeitos no export; Ctrl-Shift-G
- [[wiki/sources/frontpush-estrutura-svg-viewport-viewbox-formas-basicas-path-defs]]: FrontPUSH, mini curso de CSS Animations, propriedades SVG aula 03: fill, filtros, gradientes e IDs do export
- [[wiki/sources/frontpush-monetizacao-freelancer-como-construir-um-portfolio]]: FrontPUSH, Monetização e Freelancer aula 05: layout da próxima versão do portfólio do Násser
- [[wiki/sources/frontpush-monetizacao-freelancer-como-cobrar-hora-ou-projeto]]: FrontPUSH, Monetização e Freelancer aula 08: medir as horas do design para precificar
- [[wiki/sources/frontpush-monetizacao-freelancer-workflow-de-apresentacao-de-freelas]]: FrontPUSH, Monetização e Freelancer aula 10: protótipo de baixa fidelidade na 2ª reunião; arquivo entregue na 4ª
- [[wiki/sources/frontpush-dashboards-introducao-para-que-serve-utilidades-tipos]]: FrontPUSH, dashboards aula 01: arquivo do Dash Class
- [[wiki/sources/frontpush-dashboards-overview-do-projeto-dashclass]]: FrontPUSH, dashboards aula 02: abas do arquivo do DashClass
- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: FrontPUSH, dashboards aula 03: layout grid com offset
- [[wiki/sources/frontpush-dashboards-wireframes-e-fluxos]]: FrontPUSH, dashboards aula 07: estrutura do arquivo
- [[wiki/sources/frontpush-ia-meu-workflow-de-ia-midia]]: FrontPUSH, módulo de IA, aula 7: onde o autor guarda as versões das imagens do site do robô
