---
type: concept
title: "WebGL"
aliases: ["Web Graphics Library", "WebGL 2", "WebGraphics Library"]
date_created: 2026-11-19
date_updated: 2026-11-20
source_count: 2
tags: [frontend, 3d, gpu, browser-api, canvas, graficos]
skill: tech-mentor-frontend
status: stub
---

# WebGL

API JavaScript que dá ao navegador acesso à [[wiki/concepts/gpu]] para desenhar gráficos 2D e 3D num `<canvas>`, sem plugin. É mantida pela Khronos e baseada no OpenGL ES: WebGL 1.0 em 2011, WebGL 2 em 2017 `[external]`. Substituiu, para gráficos, o papel dos [[wiki/concepts/plugin-de-navegador|plugins]] como o Flash ([[wiki/concepts/historia-do-front-end]]).

- **API de baixo nível:** shaders em GLSL, buffers e estados. Por isso quase todo mundo usa uma biblioteca: [[wiki/entities/three-js]], Babylon.js, PlayCanvas. Para só exibir um modelo, o `<model-viewer>` `[skill: tech-mentor-frontend]`.
- **Custo:** a GPU acelera o desenho, mas a página fica mais pesada que sem 3D (runtime, modelo [[wiki/concepts/formato-gltf|glTF]], memória de vídeo, bateria do celular). Detectar o suporte (`canvas.getContext("webgl2")`) e ter fallback ([[wiki/concepts/compatibilidade-entre-navegadores]]) `[skill: tech-mentor-frontend]`.
- **Sucessor:** o WebGPU (Chrome 113+, Safari 18+) traz uma API mais próxima de Metal, Vulkan e D3D12 e compute shaders `[skill: tech-mentor-frontend]`.

## No AxlePUSH

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], o WebGL é a base de qualquer 3D no browser: "você vai precisar utilizar do WebGL e de bibliotecas como o Three.js". O instrutor lê uma definição do Google (truncada na legenda) e mostra a GPU trabalhando: os fans ligam nos exemplos do Three.js. O [[wiki/entities/spline]] esconde tudo isso atrás de uma interface visual.

## Related

- [[wiki/concepts/gpu]]
- [[wiki/concepts/formato-gltf]]
- [[wiki/concepts/alto-nivel-vs-baixo-nivel]]

## 3D "imprescindível" com biblioteca (FrontPUSH, motion aula 04)

Em [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]], Násser diz que para 3D com perspectiva "as bibliotecas JavaScript meio que são imprescindíveis". Precisão: CSS faz 3D simples (`perspective`, `rotateY`, `preserve-3d`); malhas, luz e câmera pedem WebGL ([[wiki/concepts/css-puro-vs-biblioteca-de-animacao]]).

## Key Sources

- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: WebGL como base do 3D na web
- [[wiki/sources/frontpush-bibliotecas-js-vs-css-puro-otimizacao-vs-facilidade]]: FrontPUSH, mini curso de CSS Animations, aula 04: 3D: CSS transforms × WebGL
