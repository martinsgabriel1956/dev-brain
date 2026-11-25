---
type: concept
title: "Array"
aliases: ["vetor", "lista indexada", "indexed array"]
date_created: 2026-06-01
date_updated: 2026-11-25
source_count: 23
tags: [cs-fundamentals, estruturas-de-dados, array, performance, big-o]
skill: cs-fundamentals
status: draft
---

# Array

Coleção **ordenada** de elementos onde cada item ocupa uma posição numérica chamada **índice**. A contagem começa em zero — o primeiro elemento está na posição 0, o segundo na posição 1, e assim por diante.

## Operações e Complexidade

| Operação | Complexidade | Por quê |
|---|---|---|
| Acesso por índice | **O(1)** | Posição conhecida — vai diretamente |
| Busca por valor | O(n) | Percorre um por um até encontrar |
| Inserção no final | O(1) amortizado | Sem deslocamento |
| Inserção no meio | **O(n)** | Todos os elementos seguintes se deslocam |
| Remoção no meio | **O(n)** | Idem — deslocamento obrigatório |

## Ponto Forte

Acesso por índice em tempo constante. Você sabe exatamente onde o elemento está — sem busca.

```python
usuarios[9]  # acessa o 10º usuário diretamente — O(1)
```

## Ponto Fraco

Inserir ou remover no meio é caro. Remover o elemento da posição 3 de um array com 1 milhão de elementos exige deslocar todos os ~999.997 elementos seguintes.

## Quando Usar

- A ordem importa e você acessa por posição
- Você vai iterar por todos os elementos em sequência
- O tamanho é previsível e relativamente fixo
- Leituras são muito mais frequentes que inserções no meio

## Quando Não Usar

- Você busca elementos por atributo (use [[hashmap]])
- Você insere ou remove no meio com frequência (considere linked list)
- Você precisa de estrutura FIFO/LIFO (use [[fila]] ou [[pilha]])

## Analogia

Uma fila de pessoas num show. Você sabe que a 10ª pessoa está na posição 9. Para acessar, vai direto — sem percorrer.

## Relação com outros conceitos

- [[hashmap]] — alternativa quando a busca é por atributo, não por posição
- [[algoritmos-e-estruturas-de-dados]] — array é a estrutura mais básica da sequência de aprendizado
- [[wiki/concepts/algoritmos-de-busca]] — array ordenado é pré-requisito obrigatório de binary search; array não ordenado permite só busca linear
- [[wiki/concepts/two-pointer]] — técnica que navega dois índices do mesmo array sem recriá-lo

## Uso: remontar pacotes

[[wiki/concepts/remontagem-de-pacotes-fora-de-ordem]]: array pré-alocado com o total de pedaços, indexado pela sequência ([[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]]).

## Na NLW #1, dia 2 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] explica array (vetor) para iniciantes como "uma coleção de dados", uma caixa de bolinhas, que pode misturar strings, number e objeto; acesso por posição a partir de 0 ("a posição que vai de 0 até o número 3, apesar de ter 4 elementos"). A resposta de estados do IBGE é um array de 27 objetos.

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] guarda os itens de coleta selecionados em `let selectedItems = []`, com três métodos:
- **`findIndex`:** recebe uma função que devolve verdadeiro ou falso e retorna o índice ou `-1` ("não existe nenhum item na lista").
- **`filter`:** monta "um novo array" só com os itens para os quais a função devolve `true`.
- **`push`:** adiciona no fim.

O array vai para um `input hidden` e vira o texto `4,6,2`.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] passa um array de valores para os placeholders `?` do INSERT e recebe de volta `rows`, sempre um array, mesmo com um registro. `rows.length` dá o total de pontos. Lembra que o array JavaScript aceita vírgula no fim, "o que eu não posso ter é no SQL".

## Na NLW #2, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]], `querySelectorAll('input')` devolve uma NodeList, parecida com um array: posições a partir de 0 ("eu não sei porquê"), acesso por `fields[0]` e `forEach` para repetir em vez de escrever 20 linhas iguais.

## Na NLW #2, dia 4 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]], os professores são "um objeto dentro de uma lista de objetos"; `profs.push(data)` ("push significa empurrar") adiciona, `Object.keys(data).length` diz se o objeto tem chaves e `subjects[+n - 1]` corrige o índice que começa em 0.

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], `map` x `forEach`: o `map` monta "um novo array" com os retornos, e o segundo argumento "é a posição do array". É usado para os `db.run` dos horários e para casar `weekday[index]` com `time_from[index]`. No fim, um `proffys.map` só muda os objetos, que é trabalho de `forEach`.

## Arrays no Sass (FrontPUSH)

Em [[wiki/sources/frontpush-for-while-each-sass]]: "o que é um array? Literalmente é um vetor com vários valores dentro". No Sass, listas (`40px, 50px, 80px`) e mapas, percorridos com `@each` ([[wiki/concepts/loops-sass]]).

## No FrontPUSH, módulo de JavaScript, aula 06 (Násser)

Em [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]], o array é "uma variável com vários compartimentos" e o índice é a gaveta de um armário que "sempre começa com 0". Aninhado: `frutas[4][1]`. Métodos: `pop` (remove e devolve o último), `push` (adiciona no fim; devolve o novo tamanho) e `length`. `frutas[4]` fora do intervalo dá `undefined`, sem erro. Percorrer com `i <= 5` em cinco itens lê um `undefined`; a aula chega a `i < frutas.length`. `typeof` dá `'object'`; `Array.isArray` distingue.

Em [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]], a continuação: `forEach` percorre "sem você ficar pensando em índice", e `map` devolve um array novo, usado para juntar `marcas` e `carros` pela posição ([[wiki/concepts/metodos-de-array-javascript]]).

Em [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]], `const [marca1, marca2, marca3, marca4] = carros` pega as marcas por posição: "array, colchetes". Também existem pulo (`[a, , c]`), resto (`[a, ...resto]`) e valor padrão ([[wiki/concepts/desestruturacao-javascript]]).

## No JavaScript Ninja, aula 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]], o array é "uma lista de valores" com índice a partir de 0 (`numeros[3]` dá `4`), e "no JavaScript não existem arrays [...] eles nada mais são do que objetos". `[external]` Arrays são objetos com índices como chaves (`numeros['3']` funciona), mas especiais: `length` automático e `Array.prototype`. Ver [[wiki/concepts/notacao-de-ponto-e-colchetes]].

## No JavaScript Ninja, semana 5, vídeo 01 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]], o array é o jeito de uma função devolver mais de um valor: `return [1, 2, 3]` e o índice direto na chamada (`f()[2]` traz 3; índice inexistente, `undefined`).

## Key sources

- [[wiki/sources/estruturas-de-dados-pratica-array-hashmap-fila-pilha-arvore]]
- [[wiki/sources/10-conceitos-fundamentais-computacao]]
- [[wiki/sources/estruturas-de-dados-algoritmos-big-o-como-escolher]] — array citado como estrutura de partida para sentir a diferença entre acesso direto, varredura e deslocamento
- [[wiki/sources/binary-search-em-5-minutos]] — array ordenado como pré-condição para trocar O(n) por O(log n)
- [[wiki/sources/resolvendo-3-problemas-classicos-entrevista-coding-dsa]] — Longest Consecutive Sequence: transformar array em hash set para checar membership em O(1) em vez de O(n)
- [[wiki/sources/busca-linear-e-binaria-giovana]] — indexação começa em 0 e vai até `length - 1`; array ordenado como pré-condição da busca binária
- [[wiki/sources/como-ficar-bom-em-leetcode]] — array como primeira estrutura da lista essencial; base de [[wiki/concepts/two-pointer|two pointer]] e [[wiki/concepts/sliding-window|sliding window]]
- [[wiki/sources/ordenacao-selection-quicksort-bubble-sort-live-coding]] — arrays e listas como pré-requisito declarado para os algoritmos de ordenação; Quicksort particiona o array em subarrays a cada chamada
- [[wiki/sources/icmp-browser-navegar-na-internet-via-ping-go-michel-leonardo]] — array para reordenar pacotes
- [[wiki/sources/nlw-1-dia-2-media-queries-formulario-javascript-ecoleta]]: coleção de dados, índice a partir de 0
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: findIndex, filter e push na seleção de itens
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: values do INSERT, rows e length
- [[wiki/sources/nlw-2-dia-3-formulario-dar-aulas-javascript-proffy]]: NLW #2, dia 3: NodeList, índice 0 e forEach
- [[wiki/sources/nlw-2-dia-4-back-end-node-express-nunjucks-proffy]]: NLW #2, dia 4: array de objetos, push, Object.keys
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: map com index, map x forEach
- [[wiki/sources/frontpush-for-while-each-sass]]: listas e mapas do Sass com `@each`
- [[wiki/sources/frontpush-arrays-e-loops-for-while-javascript]]: FrontPUSH, JavaScript aula 06: índice como gaveta, aninhado, pop/push/length
- [[wiki/sources/frontpush-arrays-e-iteracoes-foreach-map-javascript]]: FrontPUSH, JavaScript aula 07: forEach e map
- [[wiki/sources/frontpush-desestruturacao-objetos-arrays-mousemove]]: FrontPUSH, JavaScript aula 18: desestruturação de array
- [[wiki/sources/frontpush-o-que-preciso-saber-de-javascript-antes-do-react]]: FrontPUSH, React aula 02: arrays porque o JSON das APIs é "objetos e arrays"
- [[wiki/sources/javascript-ninja-variaveis-e-tipos-de-dados]]: JavaScript Ninja, aula 01: lista indexada a partir de 0; "arrays são objetos"
- [[wiki/sources/javascript-ninja-retorno-de-funcoes-com-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 01: função retorna array para devolver vários valores; `f()[0]`
- [[wiki/sources/javascript-ninja-parametros-de-funcoes-como-arrays-e-objetos]]: JavaScript Ninja, semana 5, vídeo 02: array como argumento; `arg[1]` dentro da função; literal direto na chamada
