# Local-First vs Offline-First

Transcrição de vídeo (autor/canal não identificados no texto fornecido). Já em pt-BR — sem necessidade de tradução.

---

Imagina o seguinte: o seu aplicativo abre no modo avião e você consegue editar. Só que isso faz ele local-first? Na verdade não — offline-first também funciona sem a rede, e local-first também funciona sem a rede. Então a gente tem duas afirmações que são reais, são verdadeiras, porém nenhuma delas descreve de fato a definição entre essas duas modalidades, essas duas arquiteturas que são totalmente diferentes.

A pergunta que separa essas duas abordagens é basicamente: qual é a cópia do dado que é a autoridade?

**Offline-first**: a cópia no cliente é basicamente um cache — subordinado ao servidor. O local é apenas um cache. Você tem o seu app, ele vai gravar no local em cache (por exemplo, no IndexedDB), e quando a rede voltar, a aplicação vai enviar essa requisição pro servidor, que é de fato a fonte da verdade. A escrita só acontece de fato quando o servidor aceita essa requisição.

**Local-first**: aí a gente inverte essas regras. No local, o local é a verdade. Você tem o notebook como uma réplica primária, você tem o seu celular como uma réplica primária também — e eles vão convergir em algum momento. Você tem esse relay, que seria uma cópia secundária — seria o servidor, nesse caso. O relay pode cair e as réplicas vão continuar convergindo.

## Cenário de conflito

Pensa nesse cenário: você tem um aplicativo X logado em dois dispositivos diferentes, ambos estão offline, e você edita nos dois ao mesmo tempo. O que vai acontecer? Existem algumas maneiras de corrigir isso, de resolver esse problema que pode gerar vários conflitos quando a gente tá trabalhando com aplicações dessa natureza.

**LWW (Last Write Wins)**: talvez a mais simples, a mais utilizada pelo menos inicialmente. Como o próprio nome já diz, a última escrita é a que vence. É mais fácil de implementar, mas tem seus tradeoffs — o principal deles é uma possível perda silenciosa de dados, porque, como o último que escreve sobrescreve, se você teve alterações anteriores, pode perder elas.

**CRDT**: existem outras abordagens, como CRDT, que são um pouco mais complexas e também têm seus próprios tradeoffs.

## O teste da empresa que fecha

Pensa comigo: a empresa dona do aplicativo fecha amanhã. O que acontece com seus dados? Seus dados vão continuar abrindo?

- No **offline-first**: você tinha um cache de algo que agora não existe mais.
- No **local-first**: o arquivo é seu, ele tava local ali no seu disco.

## Quando local-first é a decisão errada

Quando que a decisão de estruturar uma aplicação local-first tá errada? Imagina uma aplicação de banco, uma aplicação de e-commerce, uma rede social, um app de corrida. Todos esses são cenários, são regras de negócio que dependem de uma autoridade central. O próprio desenho do negócio já mostra isso pra gente.

## A pergunta que decide

Se as duas cópias divergirem, quem tem razão?

- Se você precisa que o **servidor** tenha razão, você quer **offline-first** — você quer resiliência.
- Se as duas **se resolvem entre si**, você quer **local-first** — você quer posse (ownership), e quer fornecer essa posse, por exemplo, pro seu usuário.

Dá pra gente adicionar cache depois. Agora, adicionar posse é uma decisão de arquitetura bem mais robusta, e tem que ser planejada com um pouco mais de esmero.

---

Espero que você tenha gostado desse vídeo. Deixe seu like, seu comentário, e se você não é inscrito no canal, se inscreve aí — eu tô voltando com os vídeos, então vai ter bastante conteúdo das coisas recentes que eu venho estudando, principalmente sobre system design. Se você tem interesse nesse tipo de conteúdo, comenta aí o que você quer ver nos próximos vídeos, que eu posso casar com o que eu estou estudando e trazer aqui para vocês. Beleza, então é isso — forte abraço e até mais.
