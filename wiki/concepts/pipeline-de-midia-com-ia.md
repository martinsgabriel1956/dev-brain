---
type: concept
title: "Pipeline de mídia com IA (referência → prompt → foto → vídeo → upscale)"
aliases: ["fluxo de mídia com IA", "workflow de imagem e vídeo com IA", "produção de mídia com IA generativa"]
date_created: 2026-11-23
date_updated: 2026-11-23
source_count: 1
tags: [ia-generativa, geracao-de-imagem, geracao-de-video, workflow, prompt-engineering, upscaling]
skill: tech-mentor-ai
status: stub
---

# Pipeline de mídia com IA

Fluxo em etapas para produzir fotos e vídeos de produto com [[wiki/concepts/ia-generativa]], uma ferramenta especializada por etapa. A versão de [[wiki/entities/nasser|Násser]] ([[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]):

| # | Etapa | Ferramenta | Entra | Sai |
|---|---|---|---|---|
| 0 | Referência (opcional) | Internet, fotos do produto | Ideia | Fotos de base |
| 1 | Prompt | ChatGPT ou Gemini | Descrição ditada em áudio | Prompt detalhado ([[wiki/concepts/meta-prompting]]) |
| 2a | Foto do zero | [[wiki/entities/midjourney]] | Prompt + `--ar`, `--v` | 4 variações |
| 2b | Foto a partir de foto | [[wiki/entities/nano-banana-pro]] | Prompt + foto anexada | Foto alterada (sem logos, outro ângulo) |
| 3 | Vídeo | [[wiki/entities/kling-ai]] | Prompt + [[wiki/concepts/start-frame-e-end-frame\|start/end frame]] | Clipe 1080p30 de 3 a 5 s |
| 4 | Aprimoramento | [[wiki/entities/topaz-video]] | Clipe | 4K60 ([[wiki/concepts/upscaling-com-ia]]) |
| 5 | Entrega | Otimização para web | 4K60 | 1080p30 no site |

## Princípios que a fonte repete

- **Quanto menos a IA inventa, melhor.** Vale em todas as etapas: referência > só descrição; start + end frame > só start frame; movimento suave > movimento brusco; upscale 2x > 4x.
- **Escolha pela tarefa:** "criar do zero" e "alterar uma foto" são tarefas diferentes e pedem ferramentas diferentes. O Midjourney deformou o joystick quando recebeu a foto como anexo.
- **Método estável, ferramenta trocável:** fixar um fluxo em vez de assinar cada IA nova ([[wiki/concepts/apego-a-ferramentas]]).
- **Produzir acima do destino** e reduzir no fim, porque cada conversão perde qualidade.

## Ressalvas

- A etapa 5, a otimização para web, é onde mora o custo de performance ([[wiki/concepts/core-web-vitals]], [[wiki/concepts/otimizacao-de-imagens]]), e a aula a deixa para depois.
- Direitos de uso e proveniência (logos, desenho do produto, SynthID e C2PA) atravessam o fluxo inteiro, e não só a etapa 2b. Ver as ressalvas da source.

## Key Sources

- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]
