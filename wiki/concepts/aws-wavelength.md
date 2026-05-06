---
type: concept
title: "AWS Wavelength"
aliases: ["Wavelength", "AWS Wavelength Zones"]
date_created: 2026-05-06
date_updated: 2026-05-06
source_count: 1
tags: ["aws", "5g", "edge", "baixa-latência", "telecomunicações"]
skill: tech-mentor-infra
status: stub
---

# AWS Wavelength

Infraestrutura AWS embutida fisicamente nas redes 5G das operadoras de telecomunicações. Permite executar aplicações com latência de milissegundo único diretamente na borda da rede móvel, sem que o tráfego precise atravessar a internet pública até uma região AWS.

## Como Funciona

```
Dispositivo móvel 5G
└── Antena da operadora (Tower)
    └── MEC (Mobile Edge Computing) da operadora
        └── Wavelength Zone (hardware AWS embutido)
            └── Conectado à Região AWS via backbone
```

O tráfego de dados do dispositivo nunca sai da rede da operadora para chegar na aplicação — a computação acontece dentro da infraestrutura da telco.

## Casos de Uso

- Jogos em nuvem com latência < 10ms
- Realidade aumentada/virtual em dispositivos móveis
- Veículos autônomos (edge AI)
- Transmissão ao vivo de eventos esportivos
- IoT industrial em tempo real

## Diferença: Wavelength vs. Local Zone

| | Wavelength | Local Zone |
|---|---|---|
| Onde fica | Dentro da rede da operadora 5G | Data center metropolitano AWS |
| Acesso | Via rede móvel 5G | Via internet ou Direct Connect |
| Latência | < 10ms (edge 5G) | < 5ms (usuários locais) |
| Operadoras parceiras | Verizon, KDDI, SK Telecom, Vodafone | N/A |

## Key Sources

- [[wiki/sources/aws-infraestrutura-global]]
