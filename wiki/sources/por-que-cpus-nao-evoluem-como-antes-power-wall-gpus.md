---
type: source
title: "Por que as CPUs não evoluem mais tão rápido e as GPUs ainda evoluem"
aliases: ["power wall e gpus", "por que cpus pararam de ficar mais rapidas"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/por-que-cpus-nao-evoluem-como-antes-power-wall-gpus.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-11-03
source_count: 1
tags: [cpu, gpu, power-wall, lei-de-moore, multicore, microarquitetura, simd, hardware, paralelismo, lang-systems]
skill: cs-fundamentals
status: stable
---

## TL;DR

Vídeo didático, de autor não identificado, sobre por que a CPU parou de ganhar desempenho no ritmo antigo. Até o início dos anos 2000 bastava somar transistores e frequência. O [[wiki/concepts/power-wall|power wall]] travou a frequência, e a indústria seguiu dois caminhos: [[wiki/concepts/multicore|multicore]] com avanços de [[wiki/concepts/microarquitetura|microarquitetura]], e [[wiki/concepts/gpu|GPUs]], em que uma instrução age sobre muitos dados e a latência de memória é escondida por paralelismo. A tese central confere com as fontes consultadas. Os detalhes são mais fracos: data e frequências imprecisas, o par latência/throughput trocado em dois trechos e a afirmação exagerada de que a GPU não tem stack. O próprio autor avisa que simplifica e que recorreu ao "chat" para lembrar o termo.

## Key Claims

**Claim:** Os ganhos de ordem de magnitude em 10 anos acabaram: um processador de hoje não é 10 vezes mais rápido que um de 2016.
**Evidence:** percepção do autor, sem benchmark.
**Confidence:** média, porque depende da métrica. [external] Inferência da wiki a partir de comparações aproximadas: em thread única, a diferença ficaria perto de 2× ([6700K em 2.494 no PassMark](https://www.cpubenchmark.net/compare/2565vs3598/Intel-i7-6700K-vs-AMD-Ryzen-9-3950X), 9950X estimado em cerca de 4.700 a partir de um chip irmão). Em múltiplas threads, a [comparação entre 6700T e 9950X](https://technical.city/en/cpu/Core-i7-6700T-vs-Ryzen-9-9950X) dá 7.090 contra 66.189, cerca de 9×. O 6700T é uma versão de baixo consumo, o que infla essa razão. O vídeo não faz essa separação, que é justamente o efeito do [[wiki/concepts/multicore]].

**Claim:** Nos anos 80 e 90, o ganho vinha de mais transistor e mais frequência, e o autor associa isso à [[wiki/concepts/lei-de-moore|Lei de Moore]], cujo enunciado diz não lembrar.
**Evidence:** explicação do vídeo (50, 70, 100, 200 MHz); dobrar a frequência dobraria as instruções executadas.
**Confidence:** alta para o quadro geral, com duas correções. [external] A [Lei de Moore](https://en.wikipedia.org/wiki/Moore%27s_law) trata só da contagem de transistores, dobrando a cada dois anos na revisão de 1975; a projeção de desempenho a cada 18 meses é de David House. Dobrar a frequência só dobra o desempenho se a memória acompanhar. O próprio vídeo diz depois que boa parte dos programas é limitada pela memória (inferência da wiki).

**Claim:** Por volta de 2002 e de 2 a 3 GHz, a indústria bateu no power wall: a potência cresce com a tensão ao quadrado e a frequência, e o calor deixou de poder ser dissipado. Até hoje as CPUs ficariam em 2 a 3 GHz.
**Evidence:** explicação do vídeo, com a fórmula tirada do "chat" na hora. Cita testes de overclock a 10 GHz, sem detalhes.
**Confidence:** alta para o mecanismo, baixa para os números. [external] A [Wikipedia](https://en.wikipedia.org/wiki/Dennard_scaling) traz a mesma fórmula de potência ativa (CV²f), situa o fim do [[wiki/concepts/power-wall|escalonamento de Dennard]] por volta de 2005 a 2007 e aponta a causa que o vídeo omite: corrente de fuga e tensão de limiar não escalam com o tamanho. O marco concreto é de [maio de 2004](https://www.theregister.com/2004/05/07/intel_kills_tejas/), quando a Intel cancelou o Tejas. A frequência também subiu depois: [agregadores de especificações](https://hmc-tech.com/cpus/amd-ryzen-9-9950x-vs-intel-core-i9-14900ks) listam base de 3,2 a 4,3 GHz e pico de 5,7 a 6,2 GHz em chips de desktop. O que parou foi o crescimento acelerado, não em 2 a 3 GHz.

**Claim:** O power wall incentivou o multicore: mantém-se a frequência e aumentam-se as instruções por segundo com mais processadores. Nos anos 80 e 90, tudo seria single core.
**Evidence:** explicação do vídeo; o autor admite não ter certeza sobre os anos 80 e 90.
**Confidence:** alta. [external] Em 2004, a Intel [trocou o Tejas por projetos dual-core](https://www.informationweek.com/it-leadership/intel-scraps-tejas-will-focus-on-dual-core-processors), citando-se problemas de consumo. O [IBM POWER4](https://en.wikipedia.org/wiki/POWER4) já tinha dois núcleos em 2001, antes desse marco, então o limite de potência não explica sozinho o surgimento do multicore (inferência da wiki).

**Claim:** A inovação atual de CPU está na [[wiki/concepts/microarquitetura]] (cache, pipeline, front end, back end, execução fora de ordem), não na [[wiki/concepts/isa-instruction-set-architecture|ISA]] nem no processo fabril de Intel, Arm e Apple, que mudaria pouco.
**Evidence:** exemplo dos processadores da Apple, sem dados. O autor abre dizendo "não sei detalhes".
**Confidence:** alta para a distinção entre ISA e microarquitetura; baixa para o processo fabril. [external] A [Arm não fabrica chips](https://en.wikipedia.org/wiki/Arm_Holdings), só licencia propriedade intelectual, e a Apple [produz na TSMC](https://www.iphoneincanada.ca/2022/12/29/apple-supplier-tsmc-starts-making-next-gen-3nm-chips/), então os três nomes não são fabricantes comparáveis. As páginas consultadas não medem quanto do ganho vem da microarquitetura e quanto do processo.

**Claim:** As GPUs são processadores massivamente paralelos em que uma instrução age sobre mais dados, o SIMD.
**Evidence:** explicação do vídeo; o autor avisa que simplifica.
**Confidence:** alta, com ressalvas. [external] As GPUs da NVIDIA usam [SIMT, com threads executadas em grupos de 32](https://cacm.acm.org/research/understanding-throughput-oriented-architectures). [skill: cs-fundamentals] `parallel-distributed-computing.md` lista AVX e NEON como SIMD em CPU, então [[wiki/concepts/simd|SIMD]] não separa os dois tipos de processador.

**Claim:** As duas abordagens otimizam coisas diferentes: multicore reduz o tempo de execução de uma instrução; a GPU esconde a latência, executando outra coisa enquanto o dado não chega, ao custo de cada instrução ser lenta.
**Evidence:** explicação do vídeo.
**Confidence:** alta para a GPU, baixa para o multicore. [external] Garland e Kirk (CACM, 2010) descrevem a [CPU como orientada a latência e a GPU como orientada a throughput](https://cacm.acm.org/research/understanding-throughput-oriented-architectures), que sacrifica a velocidade de cada thread e tolera latência. A página recusa acesso direto (HTTP 403), então a leitura veio só de trechos devolvidos pela busca. Quem reduz o tempo por instrução é a CPU com sua microarquitetura; mais núcleos elevam o total, como o próprio vídeo disse antes (inferência da wiki). Um [artigo do ISPASS 2015](https://doi.ieeecomputersociety.org/10.1109/ISPASS.2015.7095801) sustenta que as GPUs escondem latência menos do que se costuma supor (só o resumo foi consultado).

**Claim:** Programa de CPU fica na CPU e programa de GPU fica na GPU. Um sistema operacional não roda em GPU porque precisa de instruções com throughput alto, controle e [[wiki/concepts/context-switch|troca de contexto]] rápida.
**Evidence:** raciocínio do vídeo, sem exemplo.
**Confidence:** média. O argumento de fundo faz sentido e combina com a orientação a latência da CPU, mas "throughput" é o termo oposto ao que o raciocínio pede. Pode ser lapso do autor ou erro da correção de "trot" (ver [[wiki/log]]). A impossibilidade absoluta não foi conferida.

**Claim:** A GPU avança mais porque os núcleos são mais independentes e o número deles cresce muito, enquanto a CPU esbarra no limite térmico por precisar executar cada instrução rápido.
**Evidence:** comparação de memória, sem números. O autor diz que as limitações da GPU são "menores, no mínimo".
**Confidence:** média. [external] Garland e Kirk confirmam a [vantagem de throughput com paralelismo abundante](https://cacm.acm.org/research/understanding-throughput-oriented-architectures). A condição é decisiva e o vídeo só a sugere: sem paralelismo na carga, a [[wiki/concepts/paralelismo|Lei de Amdahl]] limita o ganho. O consumo atual das GPUs não foi verificado (ver Open Questions).

**Claim:** Na GPU não existe stack: não há push nem pop, o que limita a programação.
**Evidence:** afirmação do vídeo, sem exemplo.
**Confidence:** baixa como afirmação absoluta. [external] Respostas de [fórum da NVIDIA](https://forums.developer.nvidia.com/t/does-cuda-support-recursion/37139) e do Stack Overflow indicam recursão em CUDA desde a versão 3.1, com stack por thread configurável, e restrições nos kernels `__global__`. As fontes são antigas; a seção correspondente do guia atual da NVIDIA não abriu. Vale a leitura mais fraca: a [[wiki/concepts/pilha|pilha]] é limitada, e não um recurso comum como na CPU.

**Claim:** O power wall motivou a pesquisa em processadores massivamente paralelos, cuja expressão mais conhecida é a GPU.
**Evidence:** afirmação do vídeo.
**Confidence:** baixa como relação de causa. [external] A cronologia aponta outra origem: a [GeForce 256](https://www.electronicdesign.com/technologies/embedded-revolution/article/21178111/jon-peddie-research-nvidias-geforce-256-the-first-fullyintegrated-gpu) é de 1999, e os [shaders programáveis são de 2001 e 2002](https://dl.dropbox.com/s/fn6tikcbs2jovkq/Evolution_of_the_Graphics_Processing_Unit_GPU.pdf?dl=1), antes do marco de 2004. A GPU nasceu de gráficos; o limite da CPU pode ter ampliado o interesse no uso geral (inferência da wiki). O PDF dos shaders é um trabalho de origem incerta.

**Claim:** Colocar mais transistores também ficou difícil, com perda de aproveitamento de silício e do wafer.
**Evidence:** menção rápida na recapitulação. "Wafer" é correção de "buffer" feita na limpeza.
**Confidence:** média. [external] Há relatos de [desaceleração abaixo do ritmo de Moore desde cerca de 2010](https://en.wikipedia.org/wiki/Moore%27s_law), sem consenso sobre quando a lei deixa de valer. O vídeo não sustenta a parte de aproveitamento do wafer, e ela não foi conferida.

## Entities

Sem página própria: Intel, Apple, Arm e IBM aparecem de passagem ou só na conferência externa. A wiki tem [[wiki/entities/nvidia]], que o vídeo não cita.

## Concepts

[[wiki/concepts/power-wall]], [[wiki/concepts/lei-de-moore]], [[wiki/concepts/multicore]], [[wiki/concepts/microarquitetura]], [[wiki/concepts/gpu]], [[wiki/concepts/simd]], [[wiki/concepts/paralelismo]], [[wiki/concepts/transistor]], [[wiki/concepts/arquitetura-de-computadores]], [[wiki/concepts/isa-instruction-set-architecture]], [[wiki/concepts/context-switch]], [[wiki/concepts/pilha]], [[wiki/concepts/sistemas-operacionais]], [[wiki/concepts/gargalo]].

## Open Questions

- **Por que a GPU escapa do limite de potência?** O vídeo diz que as limitações são menores, mas não explica como nem as mede. O argumento pede dados de consumo e eficiência por geração, e esta ingestão não os reuniu.
- **Quanto do ganho recente vem da microarquitetura e quanto do processo fabril?** O vídeo aposta na microarquitetura sem dados.
- **Quanto cresceu o número de núcleos das GPUs em 10 anos?** O autor sugere conferir o número, mas não o apresenta.
- **Uma CPU a 10 GHz?** Os testes citados não são identificados nem foram conferidos.

## Quotes

> "Não é thermal wall, é power wall."

> "Executar uma instrução é igual a lento."
