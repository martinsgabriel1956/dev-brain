---
type: concept
title: "DDR SDRAM (Evolução DDR1–DDR5)"
aliases: ["DDR", "DDR SDRAM", "Double Data Rate", "DDR1", "DDR2", "DDR3", "DDR4", "DDR5"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 1
tags: [hardware, memoria, cs-fundamentals, ram, ddr, dram]
skill: cs-fundamentals
status: draft
---

# DDR SDRAM (Evolução DDR1–DDR5)

Família de tecnologia de [[wiki/concepts/memoria-ram|memória RAM]] dominante em PCs, notebooks e servidores desde os anos 2000. "Double Data Rate" refere-se a transferir dados nas duas bordas do ciclo de clock (subida e descida), dobrando a taxa de transferência efetiva sem dobrar a frequência do clock. Cada geração reduziu voltagem (menor consumo/calor), aumentou frequência e largura de banda, e mudou fisicamente a posição do entalhe do módulo — tornando cada geração **fisicamente incompatível** com a placa-mãe da geração anterior.

## Tabela comparativa

| Geração | Ano | Voltagem | Pinos (desktop) | Frequência | Largura de banda | Buffer pré-busca | Capacidade típica/módulo |
|---|---|---|---|---|---|---|---|
| DDR1 | ~2000 | 2,5–2,6 V | 184 | 200–400 MHz | até 3,2 GB/s | 2N | ~1 GB |
| DDR2 | 2003 | 1,8 V | 240 | 400–1066 MHz | ~8,5 GB/s | 4N | até 4 GB |
| DDR3 | 2007 | 1,5 V (1,35 V low-power) | 240 | 800–2133 MHz | >17 GB/s | 8N | até 16 GB |
| DDR4 | 2014 | 1,2 V | 288 | 1600–3200 MHz | >25 GB/s | — (+ bank groups, CRC) | até 128 GB (servidor) |
| DDR5 | 2021 | 1,1 V | 288 | 4800–9600+ MHz | >38 GB/s | 16N | até 512 GB (servidor) |

## O que mudou geração a geração

- **Voltagem em queda constante** (2,5 V → 1,1 V) — cada geração consome menos energia e gera menos calor por operação, mesmo rodando mais rápido.
- **Entalhe do módulo muda de posição a cada geração** — impede fisicamente encaixar um módulo DDR errado numa placa-mãe de outra geração (proteção mecânica, não só elétrica).
- **Buffer de pré-busca dobra a cada geração** (2N → 4N → 8N → 16N) — mais dados buscados por ciclo de acesso interno, viabilizando o aumento de frequência efetiva sem reprojetar o núcleo da célula de memória.
- **DDR4** introduziu *bank groups* (paralelismo interno) e verificação de erro CRC.
- **DDR5** trouxe **ECC on-die** — corrige erros de bit automaticamente dentro do próprio chip (diferente do ECC tradicional de servidor, que é uma camada externa) — e canais duplos dentro de um único módulo, além de circuitos de gerenciamento de energia (PMIC) embutidos no módulo.

## Latência vs. largura de banda: um trade-off recorrente

Frequência mais alta nem sempre significa desempenho percebido maior. A DDR2, por exemplo, ficou marcada por ter **latências mais altas** que em certos cenários anulavam parte do ganho de velocidade bruta sobre a DDR1. O mesmo padrão se repete com DDR5 vs. DDR4: mesmo com largura de banda muito maior, a diferença real em jogos do dia a dia nem sempre é tão perceptível — o ganho mais concreto de DDR5 está na confiabilidade (ECC on-die) e na capacidade para workloads de IA/processamento em larga escala, não necessariamente em FPS.

## Por que importa

Cada geração de DDR foi adotada junto com uma geração de CPU específica (DDR1 com Pentium 4/Athlon, DDR2 com Core 2 Duo/Phenom, DDR3 com Core i.../FX, DDR4 com Skylake/Ryzen 1ª geração, DDR5 com Alder Lake/Ryzen 7000) — a escolha de plataforma amarra o tipo de RAM disponível, e não é possível fazer upgrade de DDR sem trocar a placa-mãe (e geralmente o processador).

## Relação com outros conceitos

- [[wiki/concepts/memoria-ram]] — conceito geral do qual DDR é a implementação dominante atual
- [[wiki/concepts/transistor]] — cada célula de DRAM é um transistor + capacitor por bit, base física que a evolução DDR não muda geração a geração (a mudança é na interface/controlador, não na célula em si)
- [[wiki/concepts/memoria-virtual]] — a RAM física DDR é o recurso que a memória virtual abstrai e compartilha entre processos
- [[wiki/concepts/swap]] — quando a capacidade DDR instalada não basta, o SO recorre a disco

## Key Sources

- [[wiki/sources/evolucao-memorias-ram-ddr1-a-ddr5]]
