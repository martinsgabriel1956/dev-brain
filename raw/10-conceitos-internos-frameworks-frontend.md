# 10 Conceitos que os Frameworks Front-end Resolvem por Debaixo dos Panos

Transcrição de vídeo/short em português (React, Vue, Angular). Sem necessidade de tradução — já está no idioma original. Pontuação e divisão em seções adicionadas para legibilidade; a estrutura numérica decrescente (10 → 1) é do próprio vídeo. Pequenos erros de transcrição automática em termos técnicos óbvios foram corrigidos silenciosamente (ex.: "quer selector" → "querySelector", "Bunder" → "bundler"); trechos genuinamente ambíguos ficam marcados como `[transcrição incerta]`.

Você usa React, Vue ou Angular todo dia, mas você sabe o que esses frameworks fazem debaixo dos panos? Aprender sobre esses 10 conceitos vai ajudar você no dia a dia.

## 10. Gerenciamento de Estado

Esse é o conceito mais óbvio: todo framework precisa resolver como os dados fluem entre os componentes. E mesmo sendo óbvio, muita gente usa errado.

Imagina que o nome do usuário logado fica no componente raiz da aplicação, mas quem precisa mostrar esse nome é um componente lá no fundo, cinco níveis abaixo. Sem uma solução, você precisa passar essa prop por todo componente intermediário, mesmo que eles não usem o dado. Esse é o **prop drilling**, e é o primeiro problema que todo framework precisa resolver. A ideia é sempre a mesma: criar um canal direto entre quem produz o dado e quem consome, sem passar por ninguém no meio.

Mas nem todo estado precisa ser global. O valor de um input, o item selecionado numa lista — tudo isso é **estado local**: fica dentro do componente e morre com ele. **Estado global** é para dados que vários componentes precisam, como usuário logado, tema ou carrinho de compras. Se você coloca tudo no estado global, qualquer mudança pode re-renderizar componentes que não precisavam atualizar.

E tem um erro que muita gente comete: guardar no estado algo que pode ser calculado a partir de outro estado. Se você tem uma lista de itens e um filtro, os itens filtrados não precisam de estado próprio — eles são um **valor derivado**. Pensa assim: no primeiro caso, você tem dois estados separados, `itens` e `filtrados`. Toda vez que `itens` muda, você precisa lembrar de atualizar `filtrados` também; se esquece, os dois ficam fora de sincronia. No segundo caso, `filtrados` é só uma variável que calcula na hora, a partir de `itens` e `filtro` — não tem como ficar dessincronizado porque não tem estado duplicado. Se o valor pode ser calculado a partir de outro estado, não crie estado novo: apenas derive.

## 9. Batching (Agrupamento de Atualizações)

O estado decide o que o componente mostra, mas quando o estado muda, o framework precisa decidir *quando* aplicar essa mudança na tela. Esse processo tem um mecanismo próprio: **batching**.

Você clica num botão e o handler muda três estados diferentes — nome, e-mail e endereço. Sem batching, o framework renderizaria o componente três vezes, uma para cada mudança. Com batching, ele agrupa as três mudanças e renderiza uma vez só: o framework coleta as mudanças, joga numa fila e processa tudo junto. O DOM é atualizado uma vez, com o resultado final.

Isso tem uma consequência que pega muita gente: se você muda o estado e tenta ler o DOM logo em seguida, o valor ainda é o antigo — o DOM só atualiza depois que o framework processa a fila. O batching reduz quantas vezes o framework toca no DOM.

## 8. Tree Shaking e Code Splitting

Para a aplicação chegar no navegador em primeiro lugar, tem um passo que todo framework moderno precisa: transformar seu código num pacote otimizado.

Quando você compila uma aplicação, o bundler pega todos os seus arquivos JavaScript e junta num arquivo só. Se a aplicação é grande, esse arquivo pode passar de 2 MB tranquilamente, e o usuário vai precisar baixar tudo antes de ver qualquer coisa na tela.

O **tree shaking** resolve a primeira parte: o bundler analisa quais funções e módulos são realmente usados no seu código; tudo que não é importado em lugar nenhum ele remove do bundle final. Veja a diferença: importar a biblioteca inteira (ex. lodash) pode colocar ~70 KB no bundle; importar só a função específica (ex. debounce) pode colocar ~2 KB `[transcrição incerta: valores exatos]`. O tree shaking ajuda, mas importar de forma específica ajuda ainda mais.

O **code splitting** divide o bundle em pedaços. O usuário que acessa a Home baixa só o JavaScript da Home; quando navega pro dashboard, aí sim baixa o chunk do dashboard. Cada página carrega só o que precisa. Todo framework moderno tem uma forma de fazer isso: você marca um componente como *lazy* e ele só é baixado quando o usuário precisa dele.

Tree shaking remove código morto; code splitting divide o código vivo em pedaços menores. Juntos, fazem seu app carregar mais rápido.

## 7. Ciclo de Vida do Componente

O código que o bundler otimiza é o código final, mas entre o que você escreve e o que o bundler recebe tem um passo que todo framework precisa fazer: transformar cada componente em algo que o navegador entenda em cada uma de suas fases de vida.

Todo componente passa por três fases: ele **monta** quando aparece na tela pela primeira vez, **atualiza** toda vez que estado ou props mudam, e **desmonta** quando sai da tela. Cada framework te dá uma forma de executar código nessas fases; entender quando cada fase acontece evita um monte de bugs.

Exemplo: um componente de chat que conecta numa sala. Quando ele monta, abre uma conexão WebSocket. Quando o usuário sai da página, o componente desmonta e precisa fechar essa conexão. Se você não fizer esse cleanup, a conexão antiga continua aberta; se o usuário trocar de sala três vezes, agora tem três conexões rodando ao mesmo tempo.

Todo framework te dá hooks para executar código em cada fase — a sintaxe muda, mas o conceito é o mesmo: montar, atualizar, limpar. Preste atenção para não esquecer o cleanup: timers que continuam rodando, event listeners que acumulam, conexões que nunca fecham. Cada vez que um componente monta e desmonta sem limpar, mais lixo fica acumulando na memória.

## 6. Compilação

O ciclo de vida controla quando o código roda, mas como o framework transforma o código que você escreve em algo que o navegador entende? Esse processo acontece antes de qualquer coisa rodar.

O navegador não entende a sintaxe que os frameworks usam: templates, JSX, arquivos com extensão própria — nada disso roda direto no browser. Tudo precisa ser transformado em JavaScript puro antes de chegar no usuário. O compilador pega a sintaxe declarativa do framework e transforma em chamadas de função que o navegador entende: templates viram instruções de DOM, expressões viram lógica de atualização. Tudo isso acontece no build, antes do código chegar no usuário.

E aqui tem um trade-off que separa os frameworks em dois campos: alguns fazem mais trabalho no navegador, mandando um runtime que cuida da atualização em tempo real; outros fazem mais trabalho no compilador, gerando instruções de DOM específicas para cada componente e mandando quase nada de runtime. Mais trabalho no navegador significa mais flexibilidade em runtime.

## 5. Roteamento no Cliente

O compilador prepara o código, mas quando o usuário navega entre páginas, o framework precisa trocar o que aparece na tela sem recarregar. O mecanismo por trás disso é mais simples do que parece.

Num site tradicional, quando você clica num link, o navegador faz uma requisição pro servidor, recebe um HTML novo e renderiza a página do zero — a tela pisca, o estado se perde, e leva pelo menos meio segundo. Numa SPA, quando você clica num link, o JavaScript intercepta o clique, atualiza a URL e troca o conteúdo na tela sem requisição pro servidor — sem recarregar, praticamente instantâneo.

O que faz isso funcionar é a **History API** do navegador: `pushState` muda a URL na barra do navegador sem fazer nenhuma requisição, e o evento `popstate` dispara quando o usuário aperta o botão voltar. Todo router de framework usa isso por debaixo dos panos.

E aqui tem um problema: se o usuário digita `seusite.com/produtos` direto no navegador, o servidor recebe essa requisição, e se o servidor não estiver configurado para devolver o `index.html` para todas as rotas, ele retorna 404. A solução é configurar o servidor para redirecionar toda rota pro `index.html`; aí o JavaScript carrega, lê a URL e renderiza a página certa.

## 4. Hydration

O roteamento no cliente troca o que aparece na tela, mas quando a aplicação roda no servidor primeiro, o HTML chega pronto e o JavaScript precisa "acordar" ele. Esse processo tem nome: **hydration**.

Quando você usa Server-Side Rendering (SSR), o servidor renderiza o HTML completo e manda pro navegador. O usuário vê a página praticamente instantânea, mas ela é estática: os botões não fazem nada, os inputs não respondem. Aí o JavaScript carrega, olha pro HTML que já está na tela e conecta os event listeners e o estado em cada elemento. Esse processo é a hydration: o HTML estático, entre aspas, ganha vida e se torna interativo.

A vantagem é que o usuário vê o conteúdo antes do JavaScript carregar; numa conexão lenta, isso pode ser a diferença entre o usuário sair ou ficar na página. Mas um problema comum é: se o HTML que o servidor gerou é diferente do que o JavaScript gera no cliente, acontece uma **divergência de hydration** — o framework vai reclamar, e em caso mais grave, renderiza tudo de novo do zero, perdendo a vantagem do SSR.

Por que hidratar a página inteira se só alguns pedaços precisam de JavaScript? Existe uma abordagem chamada **arquitetura de ilhas** (islands architecture): a maior parte da página é HTML puro sem JavaScript, só os componentes que precisam de interatividade recebem hydration. O resultado é menos JavaScript, que carrega mais rápido, com a mesma interatividade onde precisa.

## 3. Sistema de Reatividade

A hydration conecta o JavaScript ao HTML, mas como o JavaScript sabe o que precisa atualizar quando o estado muda? Cada framework resolve isso de um jeito.

A primeira abordagem é o **Virtual DOM**: toda vez que o estado muda, o framework cria uma cópia nova da árvore de componentes na memória, compara a cópia nova com a antiga, encontra as diferenças e aplica só as mudanças no DOM real. A vantagem é que você escreve código como se renderizasse tudo do zero, mas o framework é inteligente o suficiente para atualizar só o que mudou.

A outra abordagem são **signals**: em vez de comparar árvores inteiras, o framework sabe exatamente qual variável está ligada a qual elemento do DOM. Quando o `count` muda, ele vai direto no elemento que mostra `count` e atualiza, sem nenhum tipo de diff e sem nenhuma varredura. Alguns frameworks fazem isso em tempo de execução com proxies; outros vão além e resolvem isso em tempo de compilação, gerando JavaScript que já sabe quais instruções de DOM executar para cada mudança de estado.

Na prática, o Virtual DOM funciona muito bem pra maioria das aplicações, mas em listas com milhares de itens ou animações pesadas, os signals têm vantagem porque pulam a etapa de comparação.

## 2. Reconciliação

O sistema de reatividade decide o que atualizar, mas frameworks que usam Virtual DOM precisam de um algoritmo para decidir *como* fazer essa atualização de forma eficiente. Esse algoritmo é a **reconciliação** — e entender como funciona explica vários comportamentos estranhos que você já encontrou.

Se o tipo do elemento mudou (por exemplo, de `div` para `span`), o framework destrói o componente antigo e cria um novo do zero. Se o tipo é o mesmo, ele só atualiza as props que mudaram.

Quando o framework compara uma lista de elementos, ele precisa saber qual é qual — é aí que entram as **keys**. Sem key, o framework compara por posição: o primeiro item novo com o primeiro antigo, o segundo com o segundo, e assim por diante. Se você deleta o item do meio, ele acha que os dois últimos mudaram e recria eles. Com key, o framework compara por identidade: ele sabe que "Ana" é "Ana" e "Carla" é "Carla" independente da posição — só o item removido (ex.: "Bruno") é tratado como removido.

Usar o índice da lista como key é o erro mais comum: isso só funciona quando a lista é estática. Quando você adiciona, remove ou reordena itens, o framework confunde os componentes — inputs perdem o texto, animações se resetam, estado vaza de um item pro outro.

Outra coisa útil: se você precisa resetar um componente completamente, é só mudar a `key` dele — o framework vai tratar como componente novo e remontar do zero.

## 1. O DOM

Antes de qualquer framework, antes de qualquer Virtual DOM, existe uma coisa que todo navegador tem: o próprio **DOM**. Ele é a base de tudo — cada conceito visto até agora (reconciliação, reatividade, hydration, routing) existe por causa do DOM.

Quando o navegador recebe HTML, ele não trabalha com texto puro: ele transforma esse texto numa árvore de objetos na memória. Cada tag vira um nó; cada nó tem propriedades, métodos e relações com os outros nós. Essa árvore é o DOM (Document Object Model), e o JavaScript interage com a página através dele. Quando você faz `querySelector`, você não está lendo o HTML — você está acessando um objeto na memória. Quando muda o `textContent`, o navegador atualiza o que está na tela.

Mas cada mudança no DOM tem um custo: o navegador precisa recalcular estilos, recalcular o layout e repintar os pixels na tela. Uma mudança pode ser rápida; várias mudanças em sequência já vão deixar o navegador lento. Mexer no DOM de forma descontrolada é muito caro, e esse é um dos motivos pelos quais os frameworks existem: reconciliação, reatividade, batching — tudo isso minimiza quantas vezes o DOM precisa ser tocado.

Mas frameworks também existem para você ser mais produtivo: gerenciamento de estado, ciclo de vida, compilação, routing são conceitos que organizam o código e te deixam focar no que a aplicação faz, em vez de como ela atualiza a tela.

---

*(Fim da lista. Vídeo encerra com CTA padrão de "se inscreve e deixa um like".)*
