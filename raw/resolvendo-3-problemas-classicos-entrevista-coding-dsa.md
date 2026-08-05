---
title: "Resolvendo 3 dos problemas mais populares de entrevista de coding (Estruturas de Dados e Algoritmos)"
source_type: video-transcript
language: pt-BR
translated: false
---

## Introdução

Você pode ser contra, você pode não gostar, você pode achar que não faz sentido — eu tenho minhas críticas — mas o fato é que a indústria de software adotou como parte do processo de contratação a resolução de problemas de estruturas de dados e algoritmos. Essa abordagem é ainda mais comum fora do Brasil, então quando você for fazer a famosa entrevista pra gringa, você vai precisar conseguir resolver esses problemas de estrutura de dados e algoritmo.

Hoje a gente vai resolver três dos problemas mais populares — e não vamos só resolver, porque só te dar a resolução você podia muito bem procurar no Google e estaria tudo certo, né, mas não é isso que a empresa tá medindo. Então o que a gente vai fazer é o seguinte: a gente vai pensar, a gente vai chegar na solução, a gente vai explicar como que a gente chegou na solução, e a gente vai entender o porquê essa solução é boa, o porquê essa solução é melhor do que outras soluções.

## Problema 1: Maior Sequência Consecutiva (Longest Consecutive Sequence)

Esse é um problema de array. Problemas de array são os que mais caem, são os mais populares. Esse é um problema que não é particularmente muito difícil de encontrar uma solução, mas a solução ótima para esse problema vai revelar o quanto que a gente conhece de fato sobre estruturas de dados, algoritmos e Big O notation. Calma que eu vou explicar tudo de uma maneira fácil.

O problema é o seguinte: a gente tem um array de números inteiros e a gente precisa encontrar o maior comprimento de sequência de números consecutivos. Por exemplo, se a gente tem esse array: `[100, 4, 200, 1, 3, 2]`, a maior sequência possível de se fazer com esse array é a sequência `1, 2, 3, 4` — números que estão um atrás do outro, números sequenciais. Eles não precisam estar em ordem dentro do array, mas você precisa encontrar qual a sequência que dá para fazer. Outro exemplo: um array com todos os números entre 0 e 8, numa ordem totalmente bagunçada — dá para formar uma sequência de nove elementos, todos entre 0 e 8.

### Solução força bruta (ruim)

A primeira maneira que surge na cabeça: a gente pega o elemento 100, e para o elemento 100 a gente percorre todos os outros elementos para ver se existe um elemento maior em 1 (o 101). Não achou, passa pro próximo. Repete isso pra cada elemento do array, procurando o próximo número da sequência a cada vez. Essa é a solução força bruta: percorrer o array inúmeras vezes até encontrar a sequência que a gente quer.

Essa solução é péssima porque a gente não sabe onde os elementos estão — fica procurando quase que aleatoriamente — e a gente também não tem memória de quais elementos já viu e quais ainda não viu.

### Primeira solução boa: ordenar o array

O output dessa função é só um número (o tamanho da maior sequência), então a gente pode fazer o que quiser com o array de entrada — não importa se a função tem side effects ou não, nada foi especificado.

A sacada: ordenar o array. Depois de ordenado, `[1, 2, 3, 4, 100, 200]`, fica fácil percorrer com um único ponteiro e ir checando se o próximo elemento é o elemento atual + 1. Se for, a sequência atual cresce; se não for, uma nova sequência começa. No final, comparamos o tamanho de todas as sequências encontradas e retornamos a maior.

**Sobre a complexidade:** percorrer o array ordenado uma única vez é O(n), mas a transformação que fizemos antes — ordenar o array — não é gratuita. Na maioria das linguagens isso é feito via `sort()`, que internamente usa algum algoritmo de ordenação (quicksort, mergesort, timsort etc.), com complexidade O(n log n) (a não ser que você implemente um algoritmo de ordenação não convencional como bubble sort). Como o sort domina o custo total, a complexidade real da solução inteira é **O(n log n)**, não O(n) — mesmo que a parte de "varrer e contar sequência" seja O(n). É preciso saber que ordenar um array nunca é de graça computacionalmente, mesmo que você não lembre o nome exato do algoritmo usado internamente.

Essa solução é muito boa, mas existe uma solução melhor.

### Solução ótima: usar um set (hash set)

Pensa comigo: quando a gente está num item, por exemplo o 100, para saber se ele faz parte de uma sequência a gente não precisa olhar todos os números — só precisa saber se o número 101 está na sequência. Qual a forma mais rápida (menor complexidade temporal) de checar se 101 está numa lista de elementos?

Procurar num array não ordenado exige percorrer todos os elementos — O(n). Só existiria busca rápida se o array estivesse ordenado. Mas existe outra transformação possível: transformar o array num **set** (ou hash map). Buscar um elemento num set acontece em **O(1)** — não importa se o set tem 1 elemento ou 1 milhão, a busca é computacionalmente barata sempre, não fica mais cara com mais elementos.

Transformar o array num set custa O(n) — diferente da ordenação, adicionar elementos a um set exige percorrê-los uma única vez, e a inserção de cada elemento é O(1). Essa transformação é mais barata que ordenar (para arrays de tamanho relevante — para arrays muito pequenos, ordenar pode ser mais rápido na prática, mas isso é um detalhe de constantes, não de Big O).

**A grande sacada da solução ótima:** ao invés de checar a sequência a partir de todo elemento, só vale a pena checar a partir dos elementos que são o **início** de uma sequência. Por exemplo, estando no 3 (que está no meio da sequência 1-2-3-4), não faz sentido checar a sequência a partir dele porque ela já foi (ou será) descoberta a partir do 1. Como saber se um elemento é início de sequência? Um número `x` é início de sequência se `x - 1` **não** está no set. Ex.: o 1 é início de sequência porque o 0 não está no set; o 100 é início de sequência porque o 99 não está no set; o 200 é início porque o 199 não está no set; já o 3 não é início, porque o 2 está no set.

Com isso, o algoritmo só gasta trabalho real checando sequências a partir dos elementos que são efetivamente início — os demais são pulados com uma única checagem O(1) no set. O resultado final é uma solução **O(n)**: mesmo repetindo buscas no set várias vezes durante a expansão de uma sequência, cada elemento só é "gasto" computando a sequência que o contém uma única vez ao longo de todo o algoritmo — não é O(n²).

### Implementação (Python, pensando em inglês como numa entrevista pra gringa)

```python
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in nums:
        # só começa a contar se for o INÍCIO de uma sequência
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
```

### Por que esse problema é tão popular em entrevistas

Primeiro tem a solução péssima (força bruta), depois duas soluções boas (ordenar e checar em sequência, ou usar set) — qual das duas é melhor depende do tamanho do array. A solução em si importa pouco; o que importa é a explicação: ela demonstra conhecimento de array, hash map/set e do algoritmo de ordenação, além de Big O notation. É um problema que não é muito difícil, mas exige pensamento suficiente para revelar profundidade de conhecimento em estruturas de dados e algoritmos.

## Problema 2: Top K Frequent Elements

Você recebe um array e um número inteiro `k`, e precisa retornar os `k` elementos mais frequentes do array. Por exemplo, com `k = 2`, você retorna os dois elementos mais presentes no array.

Esse problema costuma vir com uma pergunta *follow-up* opcional: a complexidade temporal tem que ser melhor que O(n log n). O motivo dessa pergunta: quando você lê "n log n" você pensa em ordenação — com sort, é fácil ordenar do menor pro maior e contar frequência porque elementos iguais ficam um do lado do outro. A sacada do follow-up é conseguir resolver **sem ordenar**.

### Passo 1 — mapa de frequências

Usar um `dict` (hash map) para contar quantas vezes cada elemento aparece no array. Para cada item, você faz um `get` no dicionário com valor default 0 e soma 1:

```python
frequency_map = {}
for num in nums:
    frequency_map[num] = frequency_map.get(num, 0) + 1
```

Popular esse mapa é O(n) — percorre o array uma vez.

### Passo 2 — evitar ordenar o mapa de frequências

Uma forma óbvia de achar os `k` mais frequentes seria ordenar o `frequency_map` por frequência e pegar os `k` primeiros — mas ordenar um hash map é O(n log n), exatamente o que o follow-up pede para evitar.

**A sacada: bucket sort por frequência.** O tamanho da lista original (`n`) é o número máximo de vezes que qualquer elemento pode aparecer. Isso significa que dá para criar um array de `n + 1` "baldes" (buckets), onde o índice do balde representa a frequência — o balde de índice 3 recebe todos os números que apareceram exatamente 3 vezes. Isso é efetivamente uma ordenação (o elemento mais frequente fica no balde de índice mais alto), mas sem custo de comparação: colocar um elemento no balde certo é O(1), porque a posição já é conhecida (a frequência dele).

```python
def top_k_frequent(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    n = len(nums)
    buckets = [[] for _ in range(n + 1)]  # índice = frequência
    for num, freq in frequency_map.items():
        buckets[freq].append(num)

    result = []
    for frequency in range(n, 0, -1):  # do mais frequente pro menos frequente
        for num in buckets[frequency]:
            result.append(num)
            if len(result) == k:
                return result

    return result
```

### Sobre a complexidade

A lista é percorrida três vezes (popular o mapa de frequências, inicializar os buckets, popular os buckets) — tecnicamente O(3n), mas em notação Big O as constantes são descartadas: O(3n) = O(2n) = O(n). O resultado final é **O(n)**, cumprindo o requisito de bater melhor que O(n log n).

### Por que esse problema é popular

Mostra domínio de hash map/dictionary — provavelmente a estrutura de dados mais usada no dia a dia de um programador (mais do que árvore binária, por exemplo) — e mostra que alterar um elemento numa posição já conhecida dentro de um array é O(1), a "gambiarra" que permite vencer o O(n log n) do sort sem de fato ordenar.

## Problema 3: Reverse Only Letters (Inverter Apenas Letras)

Esse é o mais fácil dos três. Dada uma string, você precisa inverter a posição apenas dos caracteres que são letras, mantendo os demais caracteres (números, hífens, símbolos) fixos em sua posição original. Ex.: `"ab-cd"` → `"dc-ba"` (o `a` troca com o `d`, o `b` troca com o `c`, o hífen permanece no lugar).

A solução usa a técnica de **two pointers** (dois ponteiros): um ponteiro no início da string, outro no fim, avançando/recuando de acordo com uma condição, até se encontrarem.

### Algoritmo

1. Converter a string numa lista, para facilitar manipulação.
2. Inicializar `left = 0` e `right = len(lista) - 1`.
3. Enquanto `left < right`:
   - Se o caractere em `left` não for uma letra, avança `left`.
   - Senão, se o caractere em `right` não for uma letra, recua `right`.
   - Senão (os dois são letras), troca os dois de posição e avança `left` / recua `right`.
4. Junta a lista de volta em string.

```python
def reverse_only_letters(s):
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        if not s_list[left].isalpha():
            left += 1
        elif not s_list[right].isalpha():
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)
```

Em Python, a troca de duas variáveis não precisa de variável auxiliar (`a, b = b, a`); em outras linguagens, normalmente é necessária uma variável temporária para o swap.

### Complexidade

A string é percorrida uma única vez, cada caractere é olhado no máximo uma vez — **O(n)**.

### Por que esse problema é popular

A solução é simples, mas demonstra a técnica de two pointers — dois ponteiros manipulados com lógicas/condições diferentes para cumprir um objetivo comum — uma técnica que aparece com frequência em problemas de array e string em entrevistas.

## Fechamento

Recapitulando os três problemas: Longest Consecutive Sequence (array + hash set, evitando ordenação O(n log n) em favor de O(n)), Top K Frequent Elements (hash map + bucket sort, evitando ordenação O(n log n) em favor de O(n)), e Reverse Only Letters (two pointers, O(n)). Em todos os três, o valor da entrevista não está em "chegar na resposta certa" — está em explicar o raciocínio, comparar soluções alternativas, e demonstrar domínio real das estruturas de dados e da notação Big O por trás de cada escolha.

## Bloco de patrocínio (resumido)

Entre a explicação da solução força bruta e a solução com set do Problema 1, o vídeo insere um bloco publicitário de um serviço de câmbio/remessas internacionais para receber pagamentos em dólar no Brasil (conversão para PIX, cartão virtual pré-pago, custo de câmbio de 0,5%). O apresentador oferece um cupom de desconto de 20% chamado **"Augusto 20"**, repetido várias vezes ao longo do bloco. Conteúdo publicitário resumido aqui (não é o foco técnico da fonte), mas preservado porque o nome do cupom é um indício de autoria.
