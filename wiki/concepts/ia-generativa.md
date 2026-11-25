---
type: concept
title: "IA Generativa"
aliases: ["generative AI", "genai", "ia que cria"]
date_created: 2026-10-14
date_updated: 2026-11-25
source_count: 4
tags: [ia, ia-generativa, fundamentos]
skill: tech-mentor-ai
status: draft
---

## Definição

IA cujo **objetivo** é gerar conteúdo novo (texto, imagem, música, vídeo, código, voz) a partir de um comando. O termo descreve a **finalidade da aplicação**, não uma tecnologia específica: modelos diferentes servem tipos diferentes de conteúdo (ChatGPT para texto, Midjourney para imagem). [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Contraste com IA discriminativa/preditiva

Os exemplos anteriores (spam, preço, dígito) **classificam ou preveem**; a generativa **cria**. Mesmo assim ela só **recombina padrões aprendidos no treino**, sem criatividade ou compreensão humana. [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]

## Para texto

A base é o [[wiki/concepts/llm-large-language-model|LLM]] sobre [[wiki/concepts/transformer-architecture|Transformer]]. Limites: [[wiki/concepts/alucinacao-llm]] e [[wiki/concepts/determinismo-vs-probabilismo-em-ia]].

## Para imagem e vídeo (FrontPUSH, módulo de IA)

Em [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]], a generativa de mídia aparece como uma cadeia de ferramentas especializadas, e não como um modelo só: LLM para o prompt, [[wiki/entities/midjourney]] ou [[wiki/entities/nano-banana-pro]] para a foto, [[wiki/entities/kling-ai]] para o vídeo e [[wiki/entities/topaz-video]] para o upscale ([[wiki/concepts/pipeline-de-midia-com-ia]]). O limite que a aula mostra é o mesmo do texto, "quando você não especifica ele inventa": botões que não existem e um joystick deformado. Ver [[wiki/concepts/start-frame-e-end-frame]].

## Key Sources

- [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]]
- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]: FrontPUSH, módulo de IA aula 01: pipeline de imagem e vídeo
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: IA generativa listada entre os "tipos" de IA, ao lado de ML, deep learning e LLMs
- [[wiki/sources/frontpush-ia-como-dar-comandos-na-ia-da-forma-correta]]: FrontPUSH, módulo de IA, parte 4: slide "ela não cria, ela replica coisa que existe na internet" (simplificação)
