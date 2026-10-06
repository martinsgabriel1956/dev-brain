---
type: concept
title: "Traffic Shaping e Traffic Policing"
aliases: ["traffic shaping", "traffic policing"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 2
tags: [redes, rate-limiting, controle-de-trafego]
skill: tech-mentor-backend
status: stub
---

# Traffic Shaping e Traffic Policing

Duas estratégias de controle de taxa vindas das redes de pacotes, ancestrais do [[wiki/concepts/rate-limiting]] ([[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]).

- **Traffic shaping:** retém temporariamente pacotes para transmiti-los numa taxa definida (suaviza). Base conceitual do [[wiki/concepts/leaky-bucket]].
- **Traffic policing:** mais rígido; confere o tráfego contra uma política e descarta ou marca o excedente. Equivale ao "rejeitar com 429" ([[wiki/concepts/http-429-too-many-requests]]).

Rede de pacotes: dados intercalados de várias comunicações na mesma infraestrutura, base da internet. Ligação com [[wiki/concepts/token-bucket]]: ambos modelam as duas políticas.

Parte 2: [[wiki/concepts/leaky-bucket]] (suaviza, shaping) e [[wiki/concepts/fixed-window-rate-limit]] (corta, policing) ilustram os dois comportamentos no HTTP.

## Key Sources

- [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]]
- [[wiki/sources/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato]] — ligação com os algoritmos da parte 2 (inferência)
