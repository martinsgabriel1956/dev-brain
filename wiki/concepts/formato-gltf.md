---
type: concept
title: "glTF e GLB (formatos 3D)"
aliases: ["glTF", "GLB", ".glb", ".gltf", "GL Transmission Format"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 1
tags: [3d, formato, webgl, assets, khronos]
skill: tech-mentor-frontend
status: stub
---

# glTF e GLB (formatos 3D)

Formato aberto da Khronos para transmitir e carregar cenas e modelos 3D, apelidado de "JPEG do 3D" `[external]`. A versão atual é a 2.0 (2017). Guarda malhas, materiais PBR, texturas, animações e hierarquia de cena.

- **.gltf:** JSON legível, com a geometria num `.bin` e as texturas em arquivos separados (ou embutidas em base64).
- **.glb:** a mesma coisa num único contêiner binário. É o mais prático para a web: um arquivo, uma requisição.
- **Peso:** malha e texturas dominam o tamanho. Compressão de malha (Draco, Meshopt) e de textura (KTX2) reduzem o download `[external]`. É o análogo 3D da otimização de imagem ([[wiki/concepts/formato-webp]]).

## No AxlePUSH

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], os modelos saem do [[wiki/entities/blender]] ou do [[wiki/entities/cinema-4d]], "geralmente [em] GLB", e são carregados no [[wiki/entities/three-js]]. O [[wiki/entities/spline]] importa GLB, mas limita o tamanho do arquivo para a cena rodar na web (valor não dito). Os formatos ficam para as próximas aulas.

## Related

- [[wiki/concepts/webgl]]
- [[wiki/concepts/pipeline-de-assets]]

## Key Sources

- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: GLB e glTF como formatos de importação
