---
type: entity
title: "Topaz Video"
aliases: ["Topaz Video AI", "TopazVideo", "Topaz Labs"]
date_created: 2026-11-23
date_updated: 2026-11-27
source_count: 2
tags: [video, upscaling, interpolacao-de-frames, ferramenta, desktop]
skill: tech-mentor-ai
status: stub
---

# Topaz Video

Software desktop da Topaz Labs para [[wiki/concepts/upscaling-com-ia|upscaling]], *denoise*, nitidez e interpolação de frames de vídeo. Roda localmente e depende de uma boa GPU.

Em [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]], é a última etapa do [[wiki/concepts/pipeline-de-midia-com-ia]] de [[wiki/entities/nasser|Násser]]: Enhancement 2x com o modelo Proteus ("General Enhancement for Most Videos"), Recover Detail em 50, pouco Sharpen e pouco Reduce Noise, Dehalo e Frame Interpolation para sair em 4K60. Outros modelos citados: Artemis (ruído e nitidez), Gaia (alta qualidade, animação) e Theia (fidelidade e detalhe). Ele comprou a licença vitalícia (v6) por cerca de R$ 1 mil. Segundo ele, a empresa abandonou esse modelo e hoje vende assinatura de US$ 25 a 58/mês.

`[external]`, alta: a interpolação 30 → 60 fps usa modelos próprios (Apollo, Chronos), separados do Proteus.

## Key Sources

- [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]]: upscale do vídeo do joystick
- [[wiki/sources/frontpush-ia-meu-workflow-de-ia-midia]]: FrontPUSH, módulo de IA, aula 7: escolha de modelo, nitidez, reconstrução de detalhes e interpolação 24 → 60 fps
