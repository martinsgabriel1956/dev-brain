---
type: entity
title: "Three.js"
aliases: ["three.js", "threejs", "three", "3DS (erro de ASR)"]
date_created: 2026-11-19
date_updated: 2026-11-27
source_count: 3
tags: [3d, webgl, webgpu, javascript, biblioteca, frontend]
skill: tech-mentor-frontend
status: stub
---

# Three.js

Biblioteca JavaScript de 3D sobre o [[wiki/concepts/webgl]], criada por Ricardo Cabello (mrdoob) em 2010 `[external]`. Abstrai cena, câmera, renderer, geometria, material, mesh e luzes, e carrega modelos [[wiki/concepts/formato-gltf|glTF/GLB]] (GLTFLoader). `[skill: tech-mentor-frontend]` Tem um `WebGPURenderer` para o WebGPU. É preciso liberar a memória da GPU com `dispose()` ao desmontar a cena.

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], é o caminho profissional que o [[wiki/entities/axlepush]] evita. Os modelos vêm do [[wiki/entities/blender]] ou do [[wiki/entities/cinema-4d]] e são manipulados "direto no código", o que exigiria "saber JavaScript para caramba" ([[wiki/concepts/curva-de-aprendizado]]). Nos exemplos do site, "é tudo a placa de vídeo que faz" ([[wiki/concepts/gpu]]). A legenda automática transcreve "3DS".

Alternativas: Babylon.js, PlayCanvas, `<model-viewer>` para só exibir um modelo `[skill: tech-mentor-frontend]`.

## Biblioteca 3D no mini curso de animação (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], bibliotecas JS de manipulação 3D são o caso em que JS "não tem como" evitar. Tensão com o [[wiki/entities/axlepush|AxlePUSH]], onde ele diz que "nunca" levou 3D ao FrontPUSH pela curva de aprendizado do Three.js ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## Key Sources

- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: Three.js como alternativa de código ao Spline
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: 3D como exceção ao CSS puro
- [[wiki/sources/frontpush-ia-meu-workflow-de-ia-midia]]: FrontPUSH, módulo de IA, aula 7: sobreposição de duas imagens (pessoa e armadura) no hover, no estilo do site de Lando Norris
