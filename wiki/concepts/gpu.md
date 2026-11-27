---
type: concept
title: "GPU"
aliases: ["unidade de processamento gráfico", "graphics processing unit", "processador massivamente paralelo", "programação massivamente paralela"]
date_created: 2026-11-03
date_updated: 2026-11-27
source_count: 6
tags: [cs-fundamentals, hardware, gpu, paralelismo, throughput, latencia, simt]
skill: cs-fundamentals
status: draft
---

# GPU

Processador massivamente paralelo: muitos núcleos simples executam a mesma operação sobre muitos dados, trocando a velocidade de cada instrução por volume total de trabalho ([[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]).

## Latência e throughput

| | CPU | GPU |
|---|---|---|
| **Objetivo** | Baixa latência por thread | Alto throughput total |
| **Núcleos** | 8 a 64, complexos, fora de ordem | Milhares, simples, em ordem |
| **Latência de memória** | Convertida em acesso rápido por caches grandes | Tolerada: outras threads seguem executando |

[skill: cs-fundamentals] `parallel-distributed-computing.md` dá os números de núcleos. [external] Garland e Kirk (CACM, 2010), [lido em trechos devolvidos pela busca](https://cacm.acm.org/research/understanding-throughput-oriented-architectures), resumem o projeto em três traços: muitos núcleos simples, multithreading extenso em hardware e [[wiki/concepts/simd|SIMD]]. A página recusa acesso direto.

A fonte chama isso de "esconder latência": enquanto um dado não chega, a GPU executa outra coisa já pronta. O preço é que cada instrução fica lenta. Um [artigo do ISPASS 2015](https://doi.ieeecomputersociety.org/10.1109/ISPASS.2015.7095801) sustenta que esse efeito é menor do que se costuma supor.

## Quando serve

Serve quando a mesma operação se repete sobre muitos dados e a latência é o principal problema. Não serve quando o trabalho exige controle variado e [[wiki/concepts/context-switch|troca de contexto]] rápida. A fonte dá o [[wiki/concepts/sistemas-operacionais|sistema operacional]] como exemplo; a impossibilidade absoluta não foi conferida. Esse limite vale para qualquer carga pouco paralelizável (ver Lei de Amdahl em [[wiki/concepts/paralelismo]]).

## Pontos a corrigir na fonte

- **"Não existe stack":** exagero. Ver [[wiki/concepts/pilha]].
- **"O power wall motivou a GPU":** [external] a [GeForce 256 é de 1999](https://www.electronicdesign.com/technologies/embedded-revolution/article/21178111/jon-peddie-research-nvidias-geforce-256-the-first-fullyintegrated-gpu). A GPU nasceu de gráficos; o limite da CPU pode ter ampliado o uso geral (inferência da wiki).
- **"As limitações são menores":** não medido na fonte; o consumo atual das GPUs não foi verificado.

## Relação com outros conceitos

- [[wiki/concepts/power-wall]]: o limite da CPU contra o qual a fonte compara a GPU.
- [[wiki/concepts/multicore]]: o outro caminho descrito na fonte.
- [[wiki/concepts/tensor-processing-unit]]: chip do Google para ML, tratado como complemento à GPU.
- [[wiki/entities/nvidia]]: fabricante dominante em IA.
- [[wiki/concepts/deep-learning]]: a matemática matricial é uma carga natural de GPU. [skill: cs-fundamentals]

## No 3D da web

Em [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]], a GPU é quem renderiza as cenas 3D no navegador, via [[wiki/concepts/webgl]]: "isso aqui é tudo a placa de vídeo que faz utilizando o Three.js". Os fans da placa ligam durante a demonstração. Renderização é a carga original da GPU, a mesma operação sobre muitos vértices e pixels. Para o visitante de uma página com 3D, isso vira calor e bateria, sobretudo no celular.

## Camadas e composição (FrontPUSH, otimização aula 07)

Em [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]], a GPU aparece como gargalo do celular ("uma GPU um pouquinho mais lenta") e na composição de camadas. Cada camada promovida (`will-change`, `transform` animado) ocupa memória de GPU; camadas demais derrubam quadros.

## GPU como habilitador do deep learning (FrontPUSH, módulo de IA)

Em [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]], a GPU entra como um dos três recursos que destravaram o [[wiki/concepts/deep-learning]], ao lado de Big Data e de arquiteturas. A fala diz que hoje "está tudo na faixa dos gigahertz". O clock de GPU, porém, fica em torno de 1 a 2 GHz; o salto veio do paralelismo e da largura de banda de memória (ver "Latência e throughput").

## Key sources

- [[wiki/sources/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus]]
- [[wiki/sources/axlepush-por-que-usar-o-spline-webgl-threejs]]: AxlePUSH: a GPU renderiza o WebGL; fans ligando como sinal de custo
- [[wiki/sources/frontpush-otimizacao-de-animacoes-pipeline-renderizacao-transform-opacity-compositor]]: FrontPUSH, otimização aula 07: GPU lenta e memória de camadas
- [[wiki/sources/frontpush-ia-o-que-voce-deve-saber-de-ia]]: FrontPUSH, módulo de IA, parte 1: GPU como recurso do deep learning; paralelismo, não gigahertz
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-1]]: FrontPUSH, módulo de IA, aula 5: "a crise das placas de vídeo, que nunca mais baixou de preço"; GPUs como o recurso físico que limita a IA
- [[wiki/sources/frontpush-ia-o-futuro-da-ia-parte-2]]: FrontPUSH, módulo de IA, aula 6: o "corte do chip" da série 5000 da NVIDIA (RTX 5080 com ~49% dos núcleos da 5090, contra ~83% na geração 3000)
