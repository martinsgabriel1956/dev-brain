---
type: concept
title: "Ilustração isométrica"
aliases: ["isometria", "isométrico", "formas isométricas", "isometric", "perspectiva isométrica", "dimetria 2:1"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 3
tags: [ui, ui-design, ilustracoes, isometria, figma, plugins, perspectiva]
skill: ux-ui-mentor
status: stub
---

# Ilustração isométrica

Ilustração em perspectiva paralela: o objeto aparece "em 3D" sem ponto de fuga, com as três arestas principais em ângulos fixos. Em interfaces serve para mostrar telas, cards e dispositivos "deitados" e dar profundidade sem foto. É um tipo de [[wiki/concepts/ilustracoes-em-interfaces|ilustração]].

## Como fazer no Figma

[[wiki/entities/nasser|Násser]] cita plugins do [[wiki/entities/figma]] que ajudam a construir ilustrações "em modo de isometria" ([[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]]) e os demonstra na aula prática ([[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]]):

- **Método "raiz", sem plugin:** retângulo (bordas arredondadas se quiser), rotação de 45°, agrupar (Ctrl G) e reduzir a altura do grupo a 50%.
- **Plugin "isometric" (open isometric):** posições isométricas prontas; todos os itens isométricos do site dele saíram daí.
- **Segundo plugin "isometric":** pede uma forma de quatro pontos e deixa escolher o ângulo (45°, 35°).
- **"skill-depth":** transform na vertical e na horizontal, com mais liberdade (nome não confirmado).

## 50% ou 57,7%?

`[external]` Girar um quadrado 45° e achatar a altura para 50% gera a projeção 2:1 (arestas a cerca de 26,57°), comum em jogos e em pixel art, tecnicamente dimétrica. A isométrica "verdadeira" (arestas a 30°) pede a altura a cerca de 57,7% (tan 30°). Plugins de skew descrevem o isométrico como skew de ±30° nas faces laterais (https://www.samolevsky.com/blogs/figma-plugins/skew-objects). Na interface, o que importa é usar o mesmo ângulo em todas as peças ([[wiki/concepts/consistencia-visual]]).

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-compreensao-consistencia-svg-tinyimage]] — plugins de isometria prometidos
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — método 45° + 50%, dois plugins "isometric" e "skill-depth"
- [[wiki/sources/imagens-e-ilustracoes-svg-no-figma-undraw-mockup-iphone-codigo]] — wireframes do autor com isometria, gradiente linear e sombra; "skill-that"
