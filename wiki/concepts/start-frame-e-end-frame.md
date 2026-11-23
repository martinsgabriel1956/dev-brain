---
type: concept
title: "Start frame e end frame (vídeo por quadros-chave)"
aliases: ["first frame last frame", "primeiro e último quadro", "keyframe-conditioned video", "image-to-video com quadro final"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 1
tags: [ia-generativa, geracao-de-video, image-to-video, keyframes, prompt-engineering]
skill: tech-mentor-ai
status: stub
---

# Start frame e end frame

Modo de geração de vídeo (image-to-video) em que se dá ao modelo **a imagem inicial** e, opcionalmente, **a imagem final**, e o modelo gera o movimento entre as duas. É a mesma ideia dos [[wiki/concepts/keyframes-css|keyframes]] de animação, com a IA no papel da interpolação. Em [[wiki/entities/kling-ai]], é o recurso que [[wiki/entities/nasser|Násser]] chama de "campeão" ([[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]).

## Regras práticas da fonte

- **Frames próximos funcionam sozinhos:** se um é zoom do outro, "a inteligência artificial consegue bater o olho" e acerta.
- **Frames distantes pedem descrição da transição:** frente → verso do controle só deu certo com "a primeira imagem é a frente [...] a outra é o verso [...] e ele vai rotacionar, faça isso de maneira leve, suave".
- **Sem end frame, o modelo inventa:** botões que não existem no controle real apareceram nos clipes sem quadro final. Para zooms suaves, o start frame sozinho basta.
- **Clipes curtos e encadeados:** 3 a 5 s, com o end frame de um como start frame do próximo, montam um vídeo longo coerente. Voltar ao quadro inicial fecha um loop.
- **Pedir movimento suave:** movimento maior obriga o modelo a inventar mais.

## Por que funciona

Cada quadro fixado restringe o espaço de saídas. Com início e fim definidos, o modelo só precisa gerar a trajetória entre eles, e não o conteúdo novo. Pela mesma lógica, um prompt específico reduz [[wiki/concepts/alucinacao-llm|alucinação]] em texto. `[skill: tech-mentor-ai]`

## Key Sources

- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]
