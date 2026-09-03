---
type: source
title: "Como Calcular a Complexidade de Algoritmos (Big-O) em 3 Passos"
aliases: ["3 passos big-o", "calcular complexidade de algoritmos", "método dos 3 passos big-o"]
date_created: 2026-09-03
date_updated: 2026-09-03
source_count: 0
tags: [cs-fundamentals, algoritmos, big-o, complexidade, entrevista-tecnica]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-calcular-complexidade-de-algoritmos-big-o-em-3-passos.md
source_url:
author:
date_published:
date_ingested: 2026-09-03
---

# Como Calcular a Complexidade de Algoritmos (Big-O) em 3 Passos

## TL;DR

Vídeo do canal do usuário ensinando um método operacional de três passos para calcular a complexidade de tempo (Big-O) de um código, sem depender de decorar fórmulas: (1) contar apenas as repetições (loops) do código, (2) verificar a complexidade das funções/métodos nativos da linguagem usados (consultando a documentação oficial, ex.: cppreference), e (3) ignorar constantes e manter apenas o termo de maior grau. Aplica o método em sete exemplos de código em C++ (`std::vector`), incluindo um caso didático em que uma solução com `sort()` "parece" mais simples e enxuta que uma alternativa com dois loops lineares, mas é assintoticamente pior (O(n log n) vs. O(n)) — reforçando que menos linhas de código não é sinônimo de mais rápido.

## Key Claims

1. **Cronometrar a execução não é uma medida confiável de complexidade** — o tempo depende da máquina, e uma entrada "de sorte" pode mascarar um pior caso muito mais lento em outro cenário. Evidência: framing de abertura do vídeo.
2. **Complexidade mede o número de passos no pior caso, em função do tamanho da entrada** — não o tempo em segundos. Evidência: definição dada antes de introduzir a notação Big-O.
3. **Ordem prática das complexidades, da melhor para a pior**: O(1), O(log n), O(n), O(n log n), O(n²), O(n³), O(2ⁿ), O(n!). Evidência: tabela apresentada no vídeo — coincide com [[wiki/concepts/big-o|Big O]] já registrado na wiki.
4. **Heurística de ordem de grandeza**: um computador executa cerca de 10⁷–10⁸ operações por segundo; comparar esse número com o total de operações estimado (tamanho da entrada elevado à complexidade) permite prever se uma solução passa dentro de um limite de tempo antes mesmo de rodá-la. Evidência: exemplo com entrada 10⁶ e limite de 1s — uma solução O(n²) resultaria em 10¹² operações (inviável), uma O(n) resultaria em 10⁶ (viável).
5. **Método de 3 passos**: (i) achar as repetições do código, (ii) checar a complexidade das funções/métodos nativos da linguagem usados (via documentação oficial), (iii) ignorar constantes e manter só o termo de maior grau. Evidência: núcleo do vídeo, aplicado a sete exemplos de código.
6. **Funções nativas da linguagem custam tempo e precisam ser verificadas na documentação, não assumidas como O(1)** — exemplo concreto: `vector::size()` é O(1), mas `sort()` é O(n log n) e `count()` (estrutura ordenada) é O(log n). Evidência: consulta direta ao cppreference.com mostrada no vídeo (seção "Complexity" de cada função).
7. **Menos linhas de código ≠ mais rápido**: duas soluções que resolvem o mesmo problema (verificar se a menor idade de um vetor aparece repetida) — uma com dois loops lineares (O(n)) e outra com uma chamada a `sort()` seguida de uma comparação (O(n log n)) — parecem, à primeira vista, que a segunda (mais curta, sem loop explícito) seria mais rápida. É o oposto: a complexidade escondida dentro de `sort()` domina e a torna assintoticamente pior. Evidência: exemplos 5 e 6 do vídeo, comparados lado a lado.
8. **Laços independentes sobre entradas de tamanhos diferentes não podem ser tratados como a mesma variável `n`** — dois `for`s sobre vetores de tamanhos distintos geram termos O(n) e O(m) separados, não dois O(n) somáveis/multiplicáveis como se fossem a mesma grandeza. Evidência: exemplo 4 do vídeo.

## Entidades mencionadas

- Nenhuma entidade nomeada (canal do próprio usuário, autor/nome do canal não citado na fala).
- Ferramenta citada: **cppreference.com**, usada ao vivo no vídeo como fonte para verificar a complexidade de métodos de `std::vector` (`size`, `sort`, `count`) — reforça [[wiki/concepts/documentacao-oficial-como-recurso|documentação oficial como recurso]].

## Conceitos tocados

- [[wiki/concepts/big-o|Big O]] — núcleo do vídeo: método prático de cálculo, não apenas definição.
- [[wiki/concepts/algoritmos-de-busca|Algoritmos de busca]] — exemplo 1 (busca linear).
- [[wiki/concepts/algoritmos-de-ordenacao|Algoritmos de ordenação]] — exemplos 6 e 7 (custo de `sort()` e de busca em estrutura ordenada).
- [[wiki/concepts/documentacao-oficial-como-recurso|Documentação oficial como recurso]] — hábito de consultar cppreference para complexidade de funções nativas.
- [[wiki/concepts/entrevista-tecnica-coding|Entrevista técnica de coding]] — motivação de abertura do vídeo (pergunta de complexidade em entrevista).
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio|Melhor caso, pior caso, caso médio]] — complexidade definida explicitamente como análise do pior caso.

## Open questions

- O exemplo 4 (dois `for`s independentes sobre vetores de tamanhos `n` e `m`) é apresentado no vídeo com o resultado final O(n·m), mas o código-fonte por trás da fala transcrita não deixa claro se os laços são sequenciais (o que daria O(n + m), não O(n·m)) ou se há de fato aninhamento/produto cartesiano entre eles. A transcrição automática não permite recuperar o código exato — sinalizado aqui como incerteza, e refletido com uma nota equivalente na página [[wiki/concepts/big-o]].
- Autor/nome do canal não identificado na fala — se o usuário confirmar, atualizar o campo `author` desta fonte.

## Quotes / trechos preservados

> "Complexidade de algoritmos a gente tenta basicamente analisar a quantidade de passos ou interações que o nosso código leva para executar do início ao fim... isso a gente considera no pior caso possível."

> "Nem sempre um código menor é mais rápido, com quase maior é mais fácil, a gente não consegue distinguir essa forma [só de bater o olho]."

## Key sources

(nenhuma — esta é a primeira fonte a introduzir o método dos 3 passos na wiki)
