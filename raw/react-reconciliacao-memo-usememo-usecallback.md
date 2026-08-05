# React: Algoritmo de Reconciliação, memo, useMemo e useCallback

## Abertura

Um vídeo anterior do canal mostrou como otimizar a performance da Context API usando uma nova funcionalidade que estava por vir dentro do próprio React: a questão dos **selectors** dentro do contexto. Com selectors, um componente consegue dizer exatamente quais informações ele deve observar de dentro de um contexto, para que apenas quando essas informações mudarem esse componente entre no fluxo de renderização — diferente do que acontece hoje, em que qualquer mudança em qualquer propriedade do contexto faz todo componente que o utiliza renderizar novamente, o que pode causar gargalos de performance difíceis de lidar.

Hoje o tema é mais fundo sobre três coisas do universo React: o **algoritmo de reconciliação**, o **memo**, e o **useMemo e useCallback**.

## Otimização Prematura

Um erro muito comum no desenvolvimento (seja front-end ou back-end) é a otimização prematura. Na performance isso também acontece: queremos que a aplicação performe mais e tenha resultados mais rápidos, mas na grande maioria das vezes estamos colocando esforço demais para ganhar performance com resultado pouco significativo.

Isso acontece porque a grande maioria das ferramentas — como o próprio React — já é feita para performar muito bem, independente de quantas camadas de código ou funcionalidades o usuário adicione. Seguindo a documentação do React, dificilmente você vai precisar acoplar muita coisa extra ao código: a maioria das aplicações React é performática por natureza.

Isso não significa que as funcionalidades de otimização (`memo`, `useMemo`, `useCallback`) não sejam importantes — são ferramentas para casos específicos de gargalo de performance. Mas o uso indiscriminado delas, sem entender onde realmente está o problema, tende a deixar a aplicação **mais lenta**, não mais rápida. É basicamente otimização prematura.

## Algoritmo de Reconciliação

**Renderizar** é um conjunto de três etapas:

1. O componente cria seu HTML (o Virtual DOM daquela versão do componente).
2. Verifica se existe uma mudança desse HTML em relação ao HTML anterior (caso não seja a primeira vez que o componente é exibido em tela).
3. Caso existam mudanças, aplica um algoritmo de **reconciliação** para identificar quais são as mudanças e aplicá-las em tela.

O algoritmo de reconciliação faz parte do processo de renderização — é a etapa de comparar a árvore de elementos (HTML) nova com a árvore anterior.

Quando um componente sofre uma alteração — seja de estado, propriedade, ou porque o componente pai renderizou — esse componente **sempre** vai, em todos os casos, independente de qual informação mudou, gerar novamente sua Virtual DOM. Ou seja, ele sempre entra no fluxo de renderização. Só que gerar essa nova versão não significa necessariamente que o DOM real vai ser reescrito em tela.

Diferente do funcionamento de two-way data binding (como em versões antigas do Angular, onde atualizações causavam gargalos monstruosos de performance, especialmente em formulários grandes), o React não gera essa árvore diretamente no HTML real que o usuário está vendo. Ele gera uma nova versão do HTML dentro de uma representação em JavaScript chamada **Virtual DOM**, e faz a comparação entre o HTML que o usuário está vendo e o HTML novo, para descobrir a diferença entre os dois (mudou uma `div` para um `span`, mudou um texto de "Hello World" para "Hello React", etc.). Só então aplica o algoritmo de reconciliação — e, se nada mudou, o algoritmo nem entra em ação.

### Como o algoritmo de reconciliação funciona

O algoritmo de reconciliação não substitui a DOM antiga pela nova inteira. Ele identifica a menor mudança possível. Exemplos:

- Uma `div` que tinha `className="Before"` e passa a ter `className="After"`: o React não deleta a `div` antiga e cria uma nova — ele percebe que é a mesma `div` e só troca o valor do atributo `className`.
- Uma estilização inline que muda de `color: red` para `color: green`: o React só altera a propriedade `color`, sem reescrever o resto.
- Um elemento que muda de tipo (ex.: uma `div` vira um `span`): o React também consegue perceber essa mudança de tipo.

Isso lembra (com diferenças) o algoritmo de diff usado em sistemas de controle de versão como o Git — que, ao contrário do React, normalmente trabalha por linha inteira e não percebe mudanças de conteúdo dentro da mesma linha.

### Por que a `key` importa

A `key` é a forma do React entender qual elemento é qual dentro de uma lista — pelo texto sozinho não dá, porque pode haver duplicidade.

Exemplo: uma lista de 2.000 itens onde o usuário pode arrastar um item da posição 2 para a posição 1264 (drag and drop) ou deletar um item. Sem uma `key` estável, o React não teria como saber que aquele item específico mudou de posição — ele provavelmente re-renderizaria a lista inteira, o que é extremamente pesado.

Com uma `key` estável, o React percebe: "esse elemento que estava na posição 2 agora está na posição 1264 — é o mesmo elemento, só mudou de lugar." Ele não reescreve a lista inteira: apaga o item da posição antiga e recria com o mesmo conteúdo na nova posição; o resto permanece igual.

É por isso que **não se deve usar chaves aleatórias ou o índice da lista como `key`** em listas dinâmicas: a cada renderização o índice muda de acordo com a posição, e o React perde a capacidade de saber qual item é qual quando a lista é reordenada, um item é deletado ou um item novo é adicionado.

## Setup do Projeto de Exemplo

Criação de um projeto simples com Create React App (template `hook-callback`), removendo boilerplate do `App.tsx` e deixando um "Hello World" inicial.

Criado um componente `Item` (`componentes/Item.tsx`) que recebe uma propriedade `item` (string) e a exibe. No `App.tsx`:

- Estado `items` (array de strings) via `useState`.
- Função `addItem` que adiciona um novo item ao array (copiando os itens existentes e adicionando um número no final, gerando um valor único).
- Botão "Add" que chama `addItem` ao clicar.
- `items.map(...)` para renderizar um `Item` para cada item, usando o próprio valor do item como `key` (já que cada item adicionado é único).

Ao clicar em "Add" repetidamente, novos itens aparecem na lista.

### Observando com o React DevTools Profiler

Usando o React DevTools (aba Components) é possível ver os itens da lista sendo adicionados, cada um com sua `key` única (o próprio valor do array).

Na aba **Profiler**, gravando enquanto se adiciona um item:

- Acontece um único "commit" (fluxo de renderização em massa), disparado no componente `App`.
- O motivo mostrado é `Hooks changed` — o valor de um Hook (o estado `items`) mudou.
- **Todos os itens da lista** (item 0, 1, 2, 3, 4...) aparecem coloridos no profiler, indicando que **todos sofreram uma nova renderização** — mesmo os que já existiam antes e não mudaram de conteúdo.
  - Cor verde: renderização rápida.
  - Amarelo: um pouco mais lenta.
  - Vermelho: lenta.

Isso acontece porque **renderizar não significa reconstruir o DOM real** — significa apenas entrar no fluxo dos três passos (criar nova versão do Virtual DOM, comparar com a versão anterior via reconciliação, aplicar mudanças em tela caso existam). Para os itens que não mudaram, apenas o primeiro passo (criar a nova versão do Virtual DOM) acontece; os passos seguintes não fazem nada porque não há diferença.

Mesmo assim, esse primeiro passo — gerar a nova versão do Virtual DOM para *cada item* da lista — pode ser um processo lento quando há muitos itens (formulário grande, tabela grande, listagem grande), mesmo que a mudança real seja em um único item.

Isso acontece porque o estado `items` está armazenado no componente `App`, e uma das formas mais comuns de um componente entrar no fluxo de renderização é quando o componente **pai** renderiza: sempre que o `App` renderiza (por mudança de estado, propriedade, etc.), todos os filhos também entram no fluxo de renderização — o que em listas grandes pode virar um problema real (embora só valha a pena resolver quando o problema é real e mensurável, não de forma preventiva).

## `memo`

`memo` é uma função importada do React que evolve um componente e diz: "antes de esse componente entrar no fluxo de renderização (mesmo que o pai tenha renderizado, um estado tenha mudado, uma propriedade tenha mudado), faça uma comparação das propriedades e do estado desse componente. Se nenhuma informação mudou, nem entre no fluxo de renderização."

### Aplicando no exemplo

No componente `Item`, a função do componente é renomeada para `ItemComponent`, e o `export default` passa a ser `memo(ItemComponent)`.

Voltando à aplicação, adicionando itens e gravando no Profiler: agora os itens que já existiam aparecem como **"did not render"** — ou seja, nem entraram no fluxo de criar uma nova versão do componente na Virtual DOM para comparar com a versão anterior. O `memo` evitou isso porque verificou que nenhuma propriedade ou estado relevante mudou para aquele item específico.

### Quando `memo` NÃO vale a pena

`memo` precisa **comparar** as propriedades e o estado do componente com a versão anterior para decidir se deixa ou não o componente renderizar. Esse cálculo de comparação, em alguns casos, pode ser mais lento do que simplesmente deixar o algoritmo de reconciliação do React fazer seu trabalho normalmente. Por isso `memo` não deve ser usado em todos os componentes.

### As quatro situações onde vale a pena usar `memo`

1. **Componente puro (pure function)**: dado o mesmo conjunto de propriedades, o retorno é sempre o mesmo. Se o componente depende de algo externo às propriedades (ex.: a data/hora atual, largura da tela, qualquer informação do ambiente que não vem via props), ele não é puro — e `memo` não ajuda nesses casos.
2. **Componente que renderiza demais**: por exemplo, um componente controlado (input) que causa renderização de uma árvore inteira a cada tecla digitada.
3. **Componente que renderiza muitas vezes, mas sempre com as mesmas propriedades**: se as propriedades mudam a cada renderização, `memo` não ajuda em nada — só adiciona comparações desnecessárias que sempre vão concluir que é preciso renderizar, aumentando a complexidade e piorando a performance.
4. **Componentes médios a grandes**: em componentes muito simples e pequenos (como o `Item` do exemplo), o custo do React recriar o Virtual DOM e comparar via reconciliação costuma ser mais rápido do que o próprio `memo`. `memo` compensa mais em componentes com bastante código/funcionalidade, que renderizam bastante.

## Comparação Rasa (Shallow Compare)

Antes de falar de `useMemo` e `useCallback`, é preciso entender **igualdade referencial** e o conceito de **shallow compare** (comparação rasa) — mencionado na própria documentação do React.

Quando `memo` (ou `useMemo`/`useCallback`) faz a comparação entre o valor anterior e o novo, essa comparação é equivalente a um `===` — ou seja, uma comparação rasa (shallow), não uma comparação profunda (deep compare) que entra recursivamente dentro do objeto para ver se cada propriedade interna mudou.

Isso é configurável no `memo`: por padrão, ele compara propriedade por propriedade usando shallow compare; mas é possível passar uma segunda função de comparação customizada para `memo`, recebendo `prevProps` e `nextProps`, retornando `true`/`false` para indicar se o componente deve ou não renderizar.

## Igualdade Referencial e `useCallback`

Um segundo motivo para usar `memo`/`useMemo`/`useCallback` é resolver problemas de **igualdade referencial**.

### Exemplo do problema

Um componente `App` tem uma função `addItemToWishlist` que recebe um item e o adiciona a uma lista de favoritos (`wishlist`, um estado). Essa função é passada como propriedade para o componente `Item` (prop `onAddToWishlist`, tipada como uma função que recebe uma string e não retorna nada). Dentro de `Item`, um botão "Add to wishlist" chama `props.onAddToWishlist(props.item)`.

Ao digitar no input (que atualiza um estado `newItem` a cada tecla), gravando no Profiler: **todos os itens da lista renderizam novamente**, mesmo estando com `memo`. O motivo: a propriedade `onAddToWishlist` mudou.

Isso acontece porque, toda vez que o componente `App` renderiza (nesse caso, a cada tecla digitada), qualquer função declarada dentro do corpo do componente é **recriada** — ela ocupa uma nova posição na memória. Quando o JavaScript compara se duas funções são iguais, ele verifica se ambas ocupam a **mesma posição na memória**. Como a função é recriada a cada renderização, ela nunca é "igual" à anterior nessa comparação — mesmo que o conteúdo da função seja idêntico. Isso é a tal comparação rasa detectando uma "mudança" que na prática não é uma mudança de comportamento, só de referência.

### Resolvendo com `useCallback`

`useCallback` permite memorizar (manter a mesma referência de) uma função entre renderizações, desde que suas dependências não mudem.

```tsx
const addItemToWishlist = useCallback((item: string) => {
  setWishlist(prevWishlist => [...prevWishlist, item]);
}, []); // sem dependência de wishlist, porque usamos a forma funcional do setState
```

Dica prática: quando uma atualização de estado depende do próprio valor anterior desse estado (ex.: para criar a nova wishlist é preciso da wishlist antiga), é melhor passar uma **função** para o setter de estado (`setWishlist(prevState => ...)`) em vez de acessar a variável de estado diretamente — isso remove a necessidade de colocar aquele estado no array de dependências do `useCallback`.

Depois de aplicar `useCallback`, gravando novamente no Profiler ao digitar: nenhum item sofre nova renderização, porque a função agora está memorizada e mantém a mesma referência entre renders.

### Quando usar `useCallback`

`useCallback` **não faz a função em si mais rápida** — ele só evita que ela seja recriada a cada renderização. Vale a pena usar quando:

- A função é passada como propriedade para um componente filho com `memo` (para não quebrar a memoização do filho).
- A função é usada como dependência de `useEffect` ou `useMemo`.

**Não vale a pena** quando a função é simples, usada apenas pelo próprio componente que a criou (não é repassada a filhos nem usada em um contexto compartilhado entre componentes), e o componente não sofre muitas renderizações — nesses casos, `useCallback` tende a ser mais custoso do que deixar o React recriar a função a cada render.

## `useMemo`

`useMemo` memoiza o **resultado de um cálculo**, evitando recalculá-lo quando as dependências não mudaram.

### Exemplo do problema

Um valor derivado — `countItemsWithOne`, que conta quantos itens da lista contêm o número "1" na string — é calculado diretamente no corpo do componente `App` a cada renderização, usando um `filter`/contagem sobre `items`.

Como esse código está no corpo do componente, ele é **executado do zero a cada vez que o componente entra no fluxo de renderização** — inclusive quando o usuário só está digitando no input (`newItem`) e a lista `items` nem mudou. Em um cálculo simples isso não é grave, mas em um cálculo pesado (ex.: processar uma lista de 5.000 itens, ou um filtro complexo), recalcular a cada tecla digitada é desperdício.

### Resolvendo com `useMemo`

```tsx
const countItemsWithOne = useMemo(() => {
  return items.filter(item => item.includes('1')).length;
}, [items]); // só recalcula quando `items` mudar
```

`useMemo` recebe dois parâmetros: uma função que retorna o valor calculado, e um array de dependências — as informações que, ao mudarem, justificam recalcular. Nesse exemplo, o cálculo só depende de `items`, então só quando `items` mudar o cálculo é refeito (confirmado com um `console.log` dentro da função: ele só reexecuta quando um item é adicionado, não quando se digita no input).

### Cuidado: `useMemo` também tem custo de comparação

Assim como `memo`, `useMemo` precisa comparar as dependências com a versão anterior para decidir se recalcula. Para cálculos muito simples e baratos, deixar o React recalcular a cada render pode ser mais rápido do que o overhead de comparação do `useMemo`. `useMemo` compensa quando o recálculo evitado é genuinamente caro.

### `useMemo` também resolve igualdade referencial

Se o valor calculado (mesmo que primitivo, como um número) for passado como prop para um componente `memo`, o comportamento de evitar recriação por igualdade referencial é similar ao do `useCallback` com funções — mas para **valores primitivos** (number, string, boolean) a comparação `===` já retorna `true` quando os valores são iguais, então não há o mesmo problema de referência que ocorre com objetos e funções.

O problema de igualdade referencial aparece quando o valor **não é primitivo** — por exemplo, um objeto (`{ items: [...], count: N }`) criado diretamente no corpo do componente. Cada renderização cria um objeto novo, e a comparação rasa (`===` ou shallow compare) entre dois objetos distintos sempre retorna `false`, mesmo que o conteúdo interno seja idêntico — porque a comparação de objetos, arrays e funções em JavaScript é por **referência**, não por valor. Isso é diferente de uma comparação profunda (deep compare), que entraria recursivamente nas propriedades do objeto para verificar se o conteúdo é equivalente.

Nesse caso, sem `useMemo`, um componente `memo` receberia a cada renderização um objeto "diferente" (por referência) mesmo que o conteúdo seja o mesmo, e acabaria renderizando de novo desnecessariamente. Envolvendo a criação do objeto em `useMemo` com as dependências corretas, o objeto só é recriado quando o conteúdo relevante muda de fato — resolvendo o problema.

## Encerramento

Resumo do vídeo: o algoritmo de reconciliação do React, o que significa o fluxo de renderização, quando usar `memo`, quando usar `useMemo` e `useCallback`, e o que é a comparação rasa (shallow compare) que o React usa nessas comparações.

Mensagem final: essas ferramentas de otimização (`memo`, `useMemo`, `useCallback`) resolvem problemas reais, mas usá-las indiscriminadamente ("colocar `memo` em tudo") tende a ser pior do que não otimizar nada — especialmente porque o React já é uma biblioteca construída para performar bem por padrão na construção de interfaces.
