# useEffect — Problemas, Armadilhas e Soluções

11 linhas, três useState, dois useEffect. Você consegue ver o problema? Três renderizações por mudança. Agora, três linhas, um useState, nenhum effect, uma só renderização. O mesmo resultado. E provavelmente metade dos seus componentes têm esse problema.

O useEffect foi feito para efeitos colaterais, ou seja, coisas que acontecem fora do React: chamadas API, event listeners, timers. Mas a maioria ainda usa o useEffect para sincronizar estado: quando X mudar, atualiza Y. Parece fazer sentido, mas é aí que os bugs aparecem.

Voltando pro código exemplo do início: quando itens muda, o React renderiza, depois o primeiro useEffect roda e seta filtrado. Isso causa outra renderização. Aí o segundo useEffect roda e seta total, mais uma renderização. Três renderizações. E, entre o primeiro e o terceiro, o componente tá num estado inconsistente: itens já mudou, mas total ainda é o valor antigo.

A correção é bem simples: filtrado e total não são estado, são valores derivados. Você consegue calcular eles a partir de itens, então calcula durante a renderização. Isso, sem os effect, sem os state extras, uma renderização só, que é impossível ficar inconsistente, porque tudo é calculado junto. A regra é essa: se dá para calcular a partir de estado ou props existentes, não coloca no useState.

Mas e se eu calcular o estado durante a renderização, não corre o risco de ficar lento? Essa é uma pergunta bem comum, e na maioria dos casos não. Filtrar 1000 itens leva menos de 1 milissegundo. Overhead: duas renderizações extras com effect. Mas se o cálculo for realmente pesado, e você mediu isso com profiler, por exemplo, aí sim você usa o useMemo, não useEffect com useState. O useMemo faz o cálculo durante a renderização, sem uma renderização extra. É uma diferença pequena, mas importante: o useMemo calcula e retorna na mesma renderização; o useEffect com useState agenda uma segunda renderização.

O exemplo do início tinha dois effect em cadeia, mas, por exemplo, em produção eu já vi componentes com cinco ou seis effects encadeados. Quatro state, três useEffect, quatro renderizações em cadeia. E o pior é que, se você muda a lógica de permissions, por exemplo, você precisa rastrear o impacto nos effects seguintes. E isso é bem ruim, porque gera um efeito dominó: cada peça depende da anterior e qualquer mudança pode quebrar toda a cadeia. E agora, com quatro linhas, um useState e nenhum effect, uma renderização. E a lógica fica legível, porque é sequencial, de cima para baixo, sem pular entre effects.

## Closure congelada

Agora eu vou mostrar uma consequência prática que a maioria dos devs não entende ainda de usar muitos useEffects. Esse counter nunca passa de um. O useEffect com array vazio captura o count da primeira renderização, que é zero, e esse valor fica congelado dentro da closure para sempre. A closure captura variáveis, não valores, mas, como cada renderização cria novas variáveis, a closure da primeira renderização só vê as variáveis da primeira renderização. Para corrigir isso, é só usar o updater function do setState. Em vez de ler count da closure, você pede pro React te dar o valor mais recente. Mas um detalhe importante desse bug é que ele só existe porque tem os effect. Se o seu código não dependesse de effects, não teria esse problema. Caso queira saber mais detalhes sobre closures, tem um vídeo sobre fundamentos de JavaScript aqui no canal.

## Buscar dados

Agora vamos falar do uso mais popular do useEffect, que é buscar dados. Esse código é tão comum, você provavelmente já deve ter visto, que parece certo, mas dentro dele tem três bugs escondidos. O bug número um é a race condition: se userId muda rápido, as respostas podem voltar fora de ordem. Você clica no usuário dois, mas a resposta do usuário um chega por último e o componente mostra os dados errados. O bug número dois é: se o componente desmonta antes da resposta chegar, o setUser tenta atualizar um componente que não existe mais. E o bug número três é: entre mudar o userId e a resposta chegar, o componente mostra os dados do usuário anterior, sem estado de loading, sem tratamento de erro.

Essa versão corrigida usa AbortController para cancelar requests antigos no cleanup. Isso resolve a race condition e o vazamento de memória, mas olha quanta coisa que teve que ser escrita: 30 linhas para fazer um fetch com tratamento correto.

Agora, um dos pontos principais desse vídeo: você não deveria estar fazendo fetch no effect. No exemplo desse código, a race condition tá tratada, cache tratado, retry tratado também, loading, erro também, revalidação automática também tratado. Cinco linhas em vez de 30 e nenhum useEffect. Bibliotecas como TanStack Query, SWR ou até os hooks de data fetching do Next.js e do Remix resolvem todos esses problemas. Elas existem especificamente porque o fetch é tão difícil de fazer direito que virou uma categoria de bug específica.

## Usos legítimos e resumo

Mas, deixando claro que useEffect não é errado, temos alguns usos legítimos, por exemplo: sincronizar com sistemas externos ao React, event listeners no window ou document, subscriptions a web sockets, integração com bibliotecas que manipulam diretamente, timers e intervalos com cleanup correto, analytics, logging etc. A regra é: se dá para calcular a partir de estado ou props, calcula na renderização. Se é fetch de dados, usa uma biblioteca de data fetching especializada. Se é um efeito colateral externo ao React, aí sim você usa o useEffect.

Fazendo um resumo agora: estado derivado — se dá para calcular, calcula na renderização. Não usa o useEffect para sincronizar estado. Cadeia de effects: se um useEffect seta estado que dispara outro useEffect, provavelmente ambos deveriam ser cálculos diretos. E o data fetching effect conf tem race condition, vazamento de memória e estados inconsistentes: usa o TanStack Query ou similar. O melhor effect é o que você deleta. E é isso. Se curtiu, se inscreve e deixa um like, que isso ajuda bastante o canal.
