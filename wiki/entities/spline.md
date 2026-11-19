---
type: entity
title: "Spline"
aliases: ["spline.design", "Spline Design", "Spline 3D"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
tags: [3d, ferramenta, no-code, design, webgl, colaboracao]
skill: tech-mentor-frontend
status: stub
---

# Spline

Ferramenta web de design 3D (spline.design), "a place to design and collaborate in 3D". É web-based, colaborativa e em tempo real. Modela objetos, materiais, cenas, animações e interações sem código e exporta para a web (embed, código, integração com o [[wiki/entities/webflow]]) ou como imagem e vídeo.

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], é a escolha do [[wiki/entities/axlepush]]. Traz features de modelagem do [[wiki/entities/blender]] e do [[wiki/entities/cinema-4d]] de forma simplificada, sem toda a iluminação e as sombras, porque precisa rodar no navegador. Por isso também limita o tamanho dos arquivos [[wiki/concepts/formato-gltf|GLB]] importados (valor não informado). O instrutor diz que o Spline atende "80%, 90% ou até mais dos casos" de experiência 3D na web (opinião). A alternativa descartada é o [[wiki/entities/three-js]] direto, por exigir JavaScript a fundo ([[wiki/concepts/curva-de-aprendizado]]).

O Spline fica no topo de uma pilha de abstrações: Spline → runtime e biblioteca → [[wiki/concepts/webgl]] → [[wiki/concepts/gpu]]. Ver [[wiki/concepts/alto-nivel-vs-baixo-nivel]].

## Key Sources

- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: por que usar o Spline
