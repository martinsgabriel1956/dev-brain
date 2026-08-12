# Algoritmos de Busca: Busca Linear e Busca Binária

> Transcrição limpa e estruturada de vídeo (canal Alura, apresentado por Giovana). Já em PT-BR — sem tradução necessária. Erros de reconhecimento de fala (ASR) corrigidos e marcados quando relevante: "Rei"/"Way"/"Away" → array; "Windows"/"index" → índice; "PicsArt" → Quicksort; "map.flor" → `Math.floor`; "map.c" → `Math.ceil`; "já fez script" → JavaScript; "Country"/"conte" → `count`; "loira"/"lura" → Alura.

## Introdução

Neste vídeo veremos os **algoritmos de busca**: busca linear e busca binária. Aprender sobre algoritmos de busca é extremamente importante porque em diversas situações você precisará buscar um certo elemento em uma lista de elementos. A busca binária, em especial, é um algoritmo extremamente eficiente — e não adianta simplesmente desenvolver uma solução, ela precisa ser eficiente. Ter conhecimento sobre fundamentos da Computação, algoritmos e estrutura de dados é essencial para desenvolver melhor o pensamento computacional e a forma de resolver problemas através de código.

*(Menção patrocinada: Alura, escola de tecnologia com cursos de programação, front-end, dados, DevOps, design, mobile e inovação/gestão — promoção de Black Friday.)*

## Teoria primeiro, código depois

Sempre que resolvemos um problema, é importante desenvolver a solução no papel ou na própria cabeça **antes** de partir para o código. O código deve ser a **última etapa** do processo.

### Busca Linear

A busca linear funciona assim: você **percorre todos os elementos da lista** e faz uma verificação para cada elemento, checando se ele é igual ao elemento buscado.

Exemplo com um livro (o livro *Código Limpo* / *Clean Code*) de 423 páginas — ou seja, 423 elementos. Buscando a página 310:

- Começa na página 1 → é igual a 310? Não.
- Página 2 → não.
- Página 3 → não.
- ... e assim por diante, elemento por elemento.

O **pior cenário possível** é o elemento buscado ser o último (página 423): é preciso percorrer todos os elementos. Mas ninguém procura uma página assim — sabemos que a 310 está mais para o final, um pouco à direita da metade.

### Busca Binária

A busca binária faz uma **divisão pela metade a cada etapa**. Usando o mesmo livro (buscando a página 310):

1. Abre na metade → cai na página **200**. Como 310 > 200, descartamos a metade da esquerda e vamos para a direita.
2. Divide a metade da direita → cai na página **332**. Como 310 < 332, descartamos a direita e vamos para a esquerda.
3. Divide novamente → cai na página **277**. Como 310 > 277, vamos para a direita.
4. Divide novamente → chega na página **310**. ✅

**Quatro etapas** contra as ~310 etapas que a busca linear levaria.

> **Pré-requisito obrigatório:** a busca binária só funciona se a lista estiver **ordenada**. O livro é naturalmente ordenado (página 1, 2, 3... sequencial). Para dados não ordenados, é preciso ordenar antes — e existem diversos algoritmos de ordenação eficientes, como o **Quicksort**.

## Problema prático

Um array com 8 elementos, buscando o número **7**, que está na posição de índice **6** (lembrando que a indexação começa no índice 0 e vai até o tamanho total do array − 1).

- **Busca linear:** percorre todo o array verificando cada elemento.
- **Busca binária:** a partir de um array já ordenado, divide pela metade a cada iteração.

Boa prática: retornar o **índice** do elemento encontrado, ou **−1** caso não encontre (índice impossível de ser atingido, já que os índices começam em 0). Poderia-se também retornar um booleano ou o próprio elemento — depende da solução.

*(A linguagem usada é JavaScript, mas o importante é entender a teoria e como aplicar os algoritmos; a linguagem é a última coisa com que se preocupar. Somos desenvolvedores: desenvolvemos soluções independentemente da tecnologia.)*

### Implementação — Busca Linear

```javascript
function buscaLinear(array, target) {
  let index = -1;
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    count++;
    if (array[i] === target) {
      index = i;
      console.log(`A busca linear levou ${count} etapas`);
      return index;
    }
  }
  return index;
}
```

Para executar: `node <arquivo>`. Resultado: a busca linear achou o elemento no índice 6, levando **7 etapas**.

### Implementação — Busca Binária

O **índice do meio** é `(primeiroIndex + ultimoIndex) / 2`. Ex.: `(0 + 7) / 2 = 3,5`. Como não existe índice decimal, arredonda-se para **3** usando `Math.floor` (arredonda para o menor inteiro possível). `Math.ceil` faria o contrário (arredonda para cima).

> Observação sobre JavaScript: diferente de outras linguagens, um inteiro dividido por inteiro pode dar um número decimal — por isso o `Math.floor` explícito.

```javascript
function buscaBinaria(array, target) {
  let firstIndex = 0;
  let lastIndex = array.length - 1; // -1 senão "explode": não existe índice igual a 8
  let midIndex = 0;
  let count = 0;

  while (lastIndex >= firstIndex) {
    count++;
    midIndex = Math.floor((firstIndex + lastIndex) / 2); // parênteses obrigatórios

    if (target > array[midIndex]) {
      firstIndex = midIndex + 1; // descarta a metade da esquerda
    } else if (target < array[midIndex]) {
      lastIndex = midIndex - 1;  // descarta a metade da direita
    } else {
      console.log(`A busca binária levou ${count} etapas`);
      return midIndex; // achou
    }
  }
  return -1; // não encontrado
}
```

Resultado: a busca binária também achou o elemento no índice 6, levando **3 etapas** (contra 7 da busca linear).

## Complexidade

- **Busca linear:** O(n) — depende de *n* elementos. Sempre consideramos o **pior cenário possível** (elemento no fim ou ausente). Mesmo que o elemento pudesse estar na primeira posição (O(1) no melhor caso), não há como prever isso.
- **Busca binária:** O(log n + 1), que em complexidade se simplifica para **O(log n)** — o `+1` se torna irrelevante (pega-se sempre o maior fator).

### A matemática do logaritmo

Na notação `log_b(x)`, a base do logaritmo binário é sempre **2** (por isso é omitida na complexidade). Definição: `a^x = B`, onde `a` é a base (2) e `B` é o logaritimando (n).

Assim, `2^x = n`. Para n = 8: `2^x = 8` → `x = 3`. Somando o `+1` da complexidade → **4 etapas** no máximo com busca binária, contra **8** da busca linear.

### Crescimento comparado

| Total de elementos | Busca binária (log₂n) | Busca linear (n) |
|---|---|---|
| 8 | ~4 etapas | 8 etapas |
| 64 | ~7 etapas | 64 etapas |
| 128 | ~8 etapas | 128 etapas |

O crescimento da busca linear é muito maior que o da busca binária — por isso a busca binária é extremamente eficiente para conjuntos grandes (milhares, milhões de elementos).

## Fechamento

Fundamentos de Computação envolvem matemática básica (como logaritmos) — não é preciso ser expert, mas entender como os conceitos funcionam. Esteja sempre aberto a aprender novas tecnologias e linguagens; um desenvolvedor não fica preso a uma só coisa para o resto da vida.
