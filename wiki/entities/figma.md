---
type: entity
title: "Figma"
aliases: ["figma.com"]
date_created: 2026-04-22
date_updated: 2026-11-13
source_count: 22
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

## Key Sources

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
