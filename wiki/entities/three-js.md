---
type: entity
title: "Three.js"
aliases: ["three.js", "threejs", "three", "3DS (erro de ASR)"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
tags: [3d, webgl, webgpu, javascript, biblioteca, frontend]
skill: tech-mentor-frontend
status: stub
---

# Three.js

Biblioteca JavaScript de 3D sobre o [[wiki/concepts/webgl]], criada por Ricardo Cabello (mrdoob) em 2010 `[external]`. Abstrai cena, câmera, renderer, geometria, material, mesh e luzes, e carrega modelos [[wiki/concepts/formato-gltf|glTF/GLB]] (GLTFLoader). `[skill: tech-mentor-frontend]` Tem um `WebGPURenderer` para o WebGPU. É preciso liberar a memória da GPU com `dispose()` ao desmontar a cena.

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], é o caminho profissional que o [[wiki/entities/axlepush]] evita. Os modelos vêm do [[wiki/entities/blender]] ou do [[wiki/entities/cinema-4d]] e são manipulados "direto no código", o que exigiria "saber JavaScript para caramba" ([[wiki/concepts/curva-de-aprendizado]]). Nos exemplos do site, "é tudo a placa de vídeo que faz" ([[wiki/concepts/gpu]]). A legenda automática transcreve "3DS".

Alternativas: Babylon.js, PlayCanvas, `<model-viewer>` para só exibir um modelo `[skill: tech-mentor-frontend]`.

## Key Sources

- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: Three.js como alternativa de código ao Spline
