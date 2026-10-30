---
type: source
title: "História do Computador: da Máquina de Antikythera ao Computador Quântico (Link Nacional)"
aliases: ["história do computador", "gerações de computadores", "patinho feio", "eniac", "link nacional história do computador"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/historia-do-computador-da-antikythera-ao-computador-quantico.md
source_url: ""
author: "Link Nacional (canal/empresa; identificado na abertura e no encerramento)"
date_published: ""
date_ingested: 2026-10-30
source_count: 0
tags: [historia-da-computacao, hardware, geracoes-de-computadores, armazenamento, brasil, computacao-quantica, cs-fundamentals]
skill: cs-fundamentals
status: stable
---

# História do Computador: da Máquina de Antikythera ao Computador Quântico

## TL;DR

Roteiro de divulgação da [[wiki/entities/link-nacional]] em cinco blocos:

1. **Ancestrais de cálculo:** máquina de Antikythera, ábaco, ossos de Napier, Pascalina (1642), calculadora de Leibniz (1673), Máquina Analítica de [[wiki/entities/charles-babbage]] (1837) e o algoritmo de [[wiki/entities/ada-lovelace]].
2. **Segunda Guerra e primeiros modernos:** Z1 de Zuse, Harvard Mark I ([[wiki/entities/ibm]] + [[wiki/entities/harvard-university]]), [[wiki/entities/eniac]] (1946).
3. **As [[wiki/concepts/geracoes-de-computadores|gerações]]:** válvulas → [[wiki/concepts/transistor|transistores]] → circuitos integrados → microprocessador (Intel 4004) → "quinta geração" de IA.
4. **Computador pessoal e armazenamento:** Altair 8800, Apple I; do [[wiki/concepts/cartao-perfurado]] à fita, ao [[wiki/concepts/hd-disco-rigido|HD]] (RAMAC), disquete, [[wiki/concepts/armazenamento-optico|óptico]] e nuvem.
5. **Brasil e futuro:** Zezinho (ITA, 1961), [[wiki/entities/patinho-feio]] (Poli-USP, 1972), G-10, Cobra; e a [[wiki/concepts/computacao-quantica]].

Serve como linha do tempo de [[wiki/concepts/historia-da-computacao]], mas tem **vários erros factuais típicos de texto de divulgação**, listados abaixo.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| Antikythera: calculadora mais antiga conhecida, >2 mil anos, ~30 engrenagens de bronze, prevê eclipses | Afirmação do roteiro | Alta (amplamente documentado) |
| Ábaco de origem incerta (Mesopotâmia), sistema decimal | Afirmação do roteiro | Média-alta |
| Ossos de Napier (~1617), Pascalina (1642, soma e subtração), Leibniz (1673, quatro operações) | Afirmação do roteiro | Alta |
| Leibniz defendia a numeração binária usada hoje | Afirmação do roteiro | Alta → [[wiki/concepts/sistema-binario-bit-byte]] |
| Máquina Analítica (1837): CPU, memória, entrada por cartões; nunca passou de protótipo | Afirmação do roteiro | Alta; "primeiro computador mecânico" é título de *projeto*, não de máquina construída |
| Ada Lovelace: primeiro algoritmo para a Máquina Analítica | Afirmação do roteiro | Alta (Nota G, 1843) |
| **Z1 (1938) era eletromecânico** | Afirmação do roteiro | **Baixa.** `[external]` O Z1 era puramente mecânico; o Z3 (1941) é que usava relés. A réplica no Deutsches Technikmuseum (Berlim) foi reconstruída por Zuse nos anos 1980 |
| **Harvard Mark I foi "produzida em larga escala"** | Afirmação do roteiro | **Baixa.** `[external]` Só existiu uma. Provável tradução literal de *large-scale* ("de grande porte") |
| ENIAC (1946), Mauchly e Eckert, Universidade da Pensilvânia, Exército dos EUA, para "trajetórias balísticas de mísseis" | Afirmação do roteiro | Média: `[external]` eram tabelas de tiro de **artilharia**, não mísseis. "Pioneiro dos eletrônicos digitais" ignora Atanasoff-Berry (1942) e Colossus (1943–44); o ENIAC foi o primeiro eletrônico **de propósito geral** |
| Gerações: 1ª 1940–56 (válvulas), 2ª 1956–63 (transistores), 3ª 1963/64–71 (CI), 4ª 1971– (microprocessador), 5ª (IA) | Afirmação do roteiro | Média: as datas variam entre autores; é uma periodização didática, não um consenso |
| **2ª geração: "primeiros a armazenar instruções na memória"** | Afirmação do roteiro | **Baixa.** `[external]` O programa armazenado é da 1ª geração (Manchester Baby, 1948; EDSAC, 1949). A frase circula em sites de divulgação em inglês |
| UNIVAC: primeiro computador comercial | Afirmação do roteiro | Média: `[external]` UNIVAC I (1951) nos EUA; o Ferranti Mark 1 foi entregue meses antes no Reino Unido |
| CI de silício por Jack Kilby e Robert Noyce | Afirmação do roteiro | Alta (Kilby 1958, germânio; Noyce 1959, silício planar) |
| CDC 6600 (1964), primeiro supercomputador, mais rápido do mundo até o CDC 7600 | Afirmação do roteiro | Alta; chamá-lo de "mainframe" é impreciso |
| Intel 4004 (1971) "posicionava todos os componentes do computador em um único chip" | Afirmação do roteiro | Baixa-média: `[external]` era a **CPU** num chip; memória e E/S ficavam em chips à parte |
| Altair 8800 (1975), vendido montado ou em kit | Afirmação do roteiro | Alta |
| Apple I (1976): "caixa de madeira com teclado", US$ 666,66, Homebrew Computer Club, placa montada com "cerca de 30 chips" | Afirmação do roteiro | Média: `[external]` vinha **só a placa**, sem gabinete nem teclado (a caixa de madeira foi feita a pedido da Byte Shop); fontes atuais falam em ~60 chips |
| Hollerith "fundador da IBM"; cartão perfurado deu lugar à fita "na década de 1970" | Afirmação do roteiro | Baixa-média: `[external]` a empresa dele (1896) se fundiu na CTR (1911), que virou IBM (1924); fita magnética existe desde 1951 (UNIVAC) — o cartão é que sobreviveu até os anos 70 |
| IBM RAMAC 305 (1956): primeiro disco, 5 MB, 50 discos | Afirmação do roteiro | Alta → [[wiki/concepts/hd-disco-rigido]] |
| Disquete, CD/DVD, banco de dados e nuvem como etapas de armazenamento | Afirmação do roteiro | Média: banco de dados é organização lógica, não mídia; mistura categorias |
| Brasil: importação 1958–75; Zezinho (ITA, 1961); Patinho Feio (Poli-USP, 1972, 4 KB, 45 placas); Cisne Branco (Unicamp) | Afirmação do roteiro | Alta. `[external]` Patinho Feio demonstrado em 24/jul/1972; o nome era piada com o Cisne Branco da Unicamp, que nunca foi concluído |
| G-10 (Marinha) originou o primeiro computador comercial brasileiro, "lançado pela Cobra em 1974" | Afirmação do roteiro | Média: `[external]` a Cobra foi fundada em 1974; o G-10 (Poli-USP + PUC-Rio) foi entregue em 1975 e deu origem ao MC 500 |
| Cobra 700 (tecnologia Ferranti Argus 700), Cobra 400 (Sycor 440, 1979), Cobra 530 (1980, primeiro 100% nacional) | Afirmação do roteiro | Média-alta |
| Computação quântica: qubits em superposição e emaranhamento; velocidade "exponencialmente maior" e "consumo de energia muito menor" | Afirmação do roteiro | **Baixa para a generalização.** Ganho só para problemas específicos (fatoração, simulação quântica); as máquinas atuais exigem refrigeração criogênica. Ver [[wiki/concepts/computacao-quantica]] |

## Erros e imprecisões (resumo)

O roteiro é útil como mapa, mas reproduz erros comuns de divulgação: Z1 eletromecânico, Mark I "em larga escala", ENIAC para mísseis, programa armazenado na 2ª geração, 4004 como "computador inteiro" num chip, Apple I com caixa de madeira, Hollerith fundador da IBM, fita só nos anos 70 e quântico como "mais rápido e econômico em tudo". [skill: cs-fundamentals] A skill não tem referência de história da computação; a checagem foi feita com fontes externas e conhecimento base ⚠️.

## Entities

[[wiki/entities/link-nacional]] · [[wiki/entities/charles-babbage]] · [[wiki/entities/ada-lovelace]] · [[wiki/entities/eniac]] · [[wiki/entities/patinho-feio]] · [[wiki/entities/ibm]] · [[wiki/entities/harvard-university]]

## Concepts

[[wiki/concepts/historia-da-computacao]] · [[wiki/concepts/geracoes-de-computadores]] · [[wiki/concepts/computacao-quantica]] · [[wiki/concepts/cartao-perfurado]] · [[wiki/concepts/transistor]] · [[wiki/concepts/sistema-binario-bit-byte]] · [[wiki/concepts/arquitetura-de-computadores]] · [[wiki/concepts/hd-disco-rigido]] · [[wiki/concepts/armazenamento-optico]] · [[wiki/concepts/mainframe]] · [[wiki/concepts/post-quantum-cryptography]]

## Conexão com outras fontes

Complementa [[wiki/sources/conceitos-que-regem-a-computacao-bits-turing-complexidade]] (a teoria por trás) e [[wiki/sources/como-transistores-formam-portas-logicas-celulas-padrao-cmos]] (o transistor por dentro). Curiosamente, não menciona [[wiki/entities/alan-turing]] nem a arquitetura de von Neumann — as duas ideias que definem o computador moderno, mais do que qualquer máquina específica.

## Open Questions

- **Data do vídeo:** não informada; "quinta geração a partir de 2010" sugere texto pré-LLM.
- **Fonte das contagens:** "10.000 cartões por bobina de fita" e "30 chips no Apple I" não foram confirmados.
- **Cobra 700:** ano de lançamento não confirmado.

## Raw Quotes

> "A palavra “computador” vem do verbo “computar”, que significa calcular, fazer contagem."

> "O Patinho Feio serviu de trampolim para outros projetos como o G-10, um protótipo feito para a Marinha e que foi base para criar o primeiro computador comercial do Brasil, lançado pelo Cobra em 1974."
