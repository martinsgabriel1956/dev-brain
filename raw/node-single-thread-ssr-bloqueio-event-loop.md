# Como uma única requisição derruba o servidor Node.js (Event Loop, SSR e CPU-bound)

> Transcrição de vídeo, em português, colada diretamente pelo usuário no prompt. Transformada em Markdown estruturado. Sem tradução necessária (conteúdo já em português).

E aí galera, beleza? Júnior Alves aqui de novo. Bom, continuando aqui a nossa saga de trazer fundamentos mais aplicados em problemas do nosso dia a dia, hoje eu vou te convidar pra gente ver uma questão que é bem comum, infelizmente, mas dá pra gente tirar muito ensinamento dela, entender o porquê isso acontece por debaixo dos panos.

## O cenário

Imagina que você tá acessando uma página. Essa página tá com lentidão, fica com a tela em branco por muito tempo, e quando você vai investigar um pouco mais a fundo, você vê que uma requisição só acabou causando todo esse problema ali no servidor. Isso pode acontecer basicamente pela própria natureza do event loop de ser uma thread única — e principalmente o trabalho pesado na hora errada.

## Onde isso acontece: renderização client-side vs. server-side

Antes de falar desse bug em específico, a gente precisa primeiro entender onde ele acontece.

**Renderização client-side (CSR):** o navegador baixa o JavaScript, o HTML e o CSS, e o próprio navegador monta a página. O servidor só entrega esses arquivos estáticos e responde as APIs.

**Renderização server-side (SSR):** o servidor é quem renderiza de fato a página — ele roda o componente, monta o HTML e devolve essa página pronta pro navegador. É o que o Next.js faz, o Remix, se você utilizar server components ou o próprio SSR.

Detalhe importante: se a renderização acontece no servidor, a CPU do servidor é quem paga essa conta. Na renderização client-side, quem executa todo o processo de renderização é o cliente. No SSR, o cliente só faz a requisição — o servidor recebe, processa e devolve o HTML pronto.

## Onde o Node entra em jogo

O Node é single thread — principalmente o event loop. Ele roda em uma thread única, a famosa main thread: só existe um processador de JavaScript dentro do processo, então ele executa uma operação por vez. Guarda isso, porque isso vai ser importante: se ele executa uma operação por vez, isso é receita para um problema dependendo da forma que você tiver executando esses processos.

## Como o event loop funciona

O servidor, na maior parte do tempo, faz operações de I/O: lê um arquivo, consulta o banco, chama uma API, lê dados de uma conexão de rede. Aí está a grande genialidade do event loop: quando o Node precisa fazer uma operação de I/O, ele não fica esperando — ele delega essa operação pro sistema operacional (ou pra uma thread), registra uma callback, e o event loop volta a ficar atendendo a fila de eventos.

Então chega uma requisição de I/O, o event loop pega, delega (pra uma API do sistema operacional ou, no caso do Node, uma thread) e volta a atender. É por isso que ele consegue atender várias requisições sem travar mesmo sendo single thread: iniciar uma operação de I/O é rápido — o problema é executá-la de fato.

## As duas categorias de operação

Toda operação no servidor cai em duas categorias:

**I/O bound:** o tempo é dominado pela espera de um recurso externo — disco, rede, banco. O JavaScript faz a chamada, entrega e espera a resposta. A CPU quase não trabalha nesse tipo de operação. Exemplos: acesso a disco, enviar/receber dados na rede, acesso a banco de dados.

**CPU bound:** operações que seguram a CPU de fato. Exemplos: criptografia, compactação de imagens, parse de JSON ou CSV muito grande, ordenação e transformação de dados em memória, e renderização de página complexa via SSR.

## O bug: juntando tudo

O usuário faz uma requisição, dispara uma renderização de server-side rendering pesada — um componente gigante, um parse de um JSON de 50MB, um loop de transformação de dados. Enquanto essa tarefa está sendo executada, o event loop fica parado: não consegue processar novos eventos. Isso significa que novas requisições HTTP entram na fila e ficam esperando — mesmo um callback de banco de dados que já respondeu não roda, porque o event loop não consegue recuperá-lo. O servidor não envia o que já está pronto.

Pro usuário final, a tela fica em branco: a página carrega, carrega e não renderiza nada. Pior: quanto mais gente tenta acessar o mesmo recurso no mesmo momento, mais requisições entram na fila, mais renderizações vão se acumular, e isso vai virando uma bola de neve.

## O que NÃO resolve o problema

- **`await`**: se a função faz um trabalho pesado de forma síncrona, `await` não tira nada da thread principal — só funciona com operações de I/O.
- **`setTimeout` ou microtasks**: o código ainda vai rodar na thread principal. A única coisa que você está fazendo é adiar — você está adiando o inevitável.

## O que de fato resolve

- **Quebrar o trabalho pesado em pedaços menores** (chunks) — identificar loops e "respirar" entre eles já ajuda bastante.
- **Worker threads** — mandar o trabalho CPU-bound para uma thread separada, receber o resultado de volta; a thread principal continua atendendo.
- **Filas e processamento assíncrono** — processar fora do caminho da requisição, quando houver recursos disponíveis.
- **Cache de renderização** — o SSR puro, se 100 usuários acessarem a mesma página, gera 100 requisições e 100 vezes que o servidor precisa gerar o mesmo HTML. Para páginas que não mudam com tanta frequência, dá para usar cache e estratégias híbridas (unir estático com dinâmico). O Next, por exemplo, tem o ISR (Incremental Static Regeneration) como um dos mecanismos para aliviar esse problema.

## Recapitulando

- O Node é single thread: basicamente uma thread que delega as operações de I/O e volta a atender — por isso dá conta de atender tanta gente de uma vez.
- Operações CPU-bound não são delegadas — elas seguram a thread principal, então é preciso tomar cuidado.
- O SSR entra na categoria de operação CPU-bound.
- Soluções possíveis: worker threads, filas e cache — tirando a parte pesada do caminho da requisição.
