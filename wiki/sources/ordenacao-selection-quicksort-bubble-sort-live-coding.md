---
type: source
title: "Ordenação de Listas: Selection Sort, Quicksort e Bubble Sort (Live Coding)"
aliases: ["selection sort quicksort bubble sort live", "ordenação de listas live coding", "quicksort entendendo algoritmos live"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [cs-fundamentals, algoritmos, sorting, selection-sort, quicksort, bubble-sort, big-o, dividir-para-conquistar, recursao]
skill: cs-fundamentals
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ordenacao-selection-quicksort-bubble-sort-live-coding.md
source_url:
author: canal de cortes de "Fernanda Kiperdev" (live coding, com leitura do livro Entendendo Algoritmos)
date_published:
date_ingested: 2026-09-29
---

# Ordenação de Listas: Selection Sort, Quicksort e Bubble Sort (Live Coding)

## TL;DR

Corte de live coding (continuação da live de busca binária — ver [[wiki/sources/busca-binaria-fila-protocolos-atendimento-live-coding]]) que revisa três algoritmos de ordenação. Abre com uma pergunta de visão crítica: *qual algoritmo o `.sort` nativo da linguagem usa, e até que tamanho de lista ele continua eficiente?* Depois percorre [[wiki/concepts/selection-sort]] (exemplo do livro *Entendendo Algoritmos*: ordenar artistas por plays; O(n²), com a justificativa de por que a constante ½ é descartada), [[wiki/concepts/quicksort]] (dividir-para-conquistar: caso base `len < 2`, pivô, particionamento, O(n log n) = n por nível × log n níveis; pior caso O(n²)) e [[wiki/concepts/bubble-sort]] (`for` dentro de `for`, melhor caso O(n), pior O(n²)). Fecha com a tese de que a eficiência do Quicksort depende da [[wiki/concepts/escolha-de-pivo]].

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Funções nativas (`sort` de JS, Python, Java) já encapsulam algoritmos; é preciso saber qual roda, sua eficiência e até onde ele serve ao caso de uso | "quando a gente chama essas funções, qual algoritmo tá rodando por trás? qual a eficiência daquele algoritmo? até que ponto eu posso usar?" | Alta (o argumento); a resposta sobre qual algoritmo *não* é dada na fonte — ver [[wiki/concepts/sort-nativo-das-linguagens]] |
| Selection Sort é O(n²): achar o maior é O(n) e essa busca é repetida n vezes | "é como se eu tivesse um for dentro de um for… n vezes n é n²" | Alta |
| Constantes (como ½ vindo de n + (n−1) + (n−2)…) são descartadas em Big O | "as constantes são cortadas… porque a constante é muito irrelevante para casos gigantescos" | Alta na regra; justificativa da fonte é intuitiva (escala), não formal — ver [[wiki/concepts/descarte-de-constantes-big-o]] |
| Com poucos elementos (dezenas/centenas) a escolha do algoritmo quase não importa; a diferença aparece em milhares a milhões | "se tu tem 100 elementos não importa qual algoritmo… a diferença vai começar a gritar na casa de milhões" | Média (heurística de campo; exceção citada: algoritmos recursivos/O(n²) degradam antes) |
| Quicksort usa [[wiki/concepts/dividir-para-conquistar]] com recursão; caso base é array vazio ou de 1 elemento (`len(array) < 2`) | Leitura do livro: "arrays vazios ou com apenas um elemento serão o caso base" | Alta |
| Quicksort funciona com **qualquer** pivô; a escolha só afeta a velocidade | "isso funcionará com qualquer pivô" | Alta |
| Quicksort é O(n log n) = O(n) de particionamento por nível × O(log n) níveis de recursão | "n vezes log de n… o n porque a gente vai ter que fazer um for para cada elemento" | Alta |
| Quicksort tem pior caso O(n²) (igual à seleção) e caso médio O(n log n) | Leitura do livro | Alta |
| Bubble Sort: melhor caso O(n), pior caso O(n²) (geeksforgeeks) | "o best case do bubble sort é n, o pior caso é n²" | Alta (com ressalva: O(n) exige a variante com flag de "nenhuma troca" — ver Open Questions) |
| A eficiência do Quicksort depende da escolha do pivô (primeiro, meio, último ou aleatório) | "a eficiência do quicksort também vai tá muito atrelada à escolha do pivô" | Alta |
| O quadro de tempos (10 ops/s, n = 1000) é ilustrativo, não regra: hardware, SO, linguagem e processador interferem | "não posso considerar segundos aqui… só de maneira ilustrativa" | Alta |

## Pontos didáticos

- **Analogia do exemplo do livro:** lista de artistas com contagem de plays (Radiohead 156, Kishore Kumar 141, The Black Keys 35) → construir uma *nova* lista pegando sempre o mais tocado. Cada seleção custa O(n); n seleções → O(n²).
- **Por que n·(n−1)/2 vira O(n²):** verifica-se n, n−1, n−2… elementos (média ≈ n/2), logo ½·n·n; a constante ½ cai.
- **Quadro do livro (n = 1000, 10 ops/s):** O(log n) ≈ 1 s; O(n) ≈ 100 s; O(n log n) ≈ 996 s; O(n²) ≈ 27 h; O(n!) astronômico. Confere aritmeticamente: log₂1000 ≈ 10 ops; 1000·10 ≈ 10⁴ ops ≈ 1000 s (a fonte diz 996 s, valor exato de n·log₂n = 9 966 ops ÷ 10) [skill: cs-fundamentals].
- **Comparação Quicksort × Bubble Sort:** Quicksort se autochama e particiona (cada chamada recebe um subarray menor); Bubble Sort é iterativo com dois loops aninhados e uma variável temporária para o swap.

## Entidades Mencionadas

- [[wiki/entities/fernanda-kipper]] — canal principal "Fernanda Kiperdev", live coding no 2º e 4º domingo do mês
- *Entendendo Algoritmos* (tradução PT-BR de *Grokking Algorithms*, Aditya Bhargava) — capítulos de ordenação por seleção e Quicksort lidos ao vivo; ver [[wiki/concepts/livros-recomendados-programador]]
- GeeksforGeeks — fonte da implementação e da tabela de complexidade do Bubble Sort usada ao vivo (em JavaScript)

## Conceitos Tocados

- [[wiki/concepts/selection-sort]] (novo)
- [[wiki/concepts/quicksort]] (novo)
- [[wiki/concepts/bubble-sort]] (novo)
- [[wiki/concepts/dividir-para-conquistar]] (novo)
- [[wiki/concepts/escolha-de-pivo]] (novo)
- [[wiki/concepts/sort-nativo-das-linguagens]] (novo)
- [[wiki/concepts/descarte-de-constantes-big-o]] (novo)
- [[wiki/concepts/algoritmos-de-ordenacao]]
- [[wiki/concepts/big-o]]
- [[wiki/concepts/melhor-caso-pior-caso-caso-medio]]
- [[wiki/concepts/recursao]]
- [[wiki/concepts/logaritmo]]
- [[wiki/concepts/algoritmos-de-busca]]
- [[wiki/concepts/algoritmos-e-estruturas-de-dados]]
- [[wiki/concepts/array]]
- [[wiki/concepts/livros-recomendados-programador]]

## Contradições e imprecisões da fonte

- **Caso base do Quicksort:** a fala primeiro diz "de zero a um elemento", corrige para "um ou dois elementos" e, ao ler o livro, volta a `len < 2` (0 ou 1 elemento). O correto é 0 ou 1; o caso de 2 elementos é só ilustração de que a recursão o resolve sozinha (particiona em um subarray de 1 e outro vazio).
- **Pior caso do Quicksort = "array completamente invertido":** a fonte descreve o pior caso pelo formato da entrada, mas ele é função do par (entrada, estratégia de pivô). Com pivô = primeiro elemento (a escolha usada na própria live), o array **já ordenado** também é pior caso — e o "melhor caso: quase ordenado, um único swap" descreve mais o Bubble Sort/Insertion Sort do que o Quicksort. A própria fonte se corrige parcialmente no final ("se eu pegasse o elemento do meio e o array já tivesse ordenado, garanto n log n"). Ver [[wiki/concepts/escolha-de-pivo]] e [[wiki/concepts/algoritmos-de-ordenacao]] (pivô extremo).
- **"Recursão → complexidade exponencial?":** a fala sugere que fazer recursão implicaria complexidade exponencial; recursão só é exponencial quando há sobreposição de subproblemas (ex.: Fibonacci ingênuo). No Quicksort as chamadas trabalham em partes disjuntas do array.
- **Bubble Sort com melhor caso O(n):** só vale para a versão otimizada que interrompe quando uma passada não faz trocas; a versão de dois `for` completos (descrita ao vivo) é O(n²) sempre. [external] https://www.geeksforgeeks.org/bubble-sort-algorithm/

## Open Questions

- A fonte **não responde** sua própria pergunta de abertura (qual algoritmo o `sort` de JS/Python/Java usa). Resposta em [[wiki/concepts/sort-nativo-das-linguagens]] (marcada como [external]/[skill]).
- Não mostra código de Quicksort nem de Selection Sort (só o Bubble Sort do GeeksforGeeks aparece na tela); o Merge Sort é apenas citado. Implementações e trace numérico completos: [[wiki/sources/algoritmos-de-ordenacao-bubble-insertion-selection-merge-quicksort-heapsort]].
- Afirmação de que a `qsort` da biblioteca padrão C é "a implementação do Quicksort" (do livro): o padrão C não impõe o algoritmo, e implementações variam — não verificado nesta ingestão.
- Como "otimizar" o algoritmo padrão do `sort` quando necessário (pergunta de abertura) não é abordado.

## Raw Quotes

> "Quando a gente utiliza o ponto sort do JavaScript… qual algoritmo tá rodando por trás? Qual a eficiência daquele algoritmo? Até que ponto eu posso usar esse algoritmo?"

> "Sempre quando a gente tem uma constante atrelada dentro dessa função que calcula o tempo de execução do algoritmo, as constantes são cortadas."

> "Sempre quando eu tenho um for dentro de outro loop for eu vou ter essa complexidade que a gente chama de O de n²."

> "A cada recursão eu tô diminuindo o número do array, eu tô dividindo esse array ao meio, literalmente. Então isso é um comportamento padrão de um logaritmo."

> "A eficiência do quicksort também vai tá muito atrelada à escolha do pivô."
