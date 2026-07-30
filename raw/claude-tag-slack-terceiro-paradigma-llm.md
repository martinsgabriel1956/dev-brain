# Claude Tag no Slack: um novo paradigma de interface para LLMs?

> Transcrição de vídeo (transcrita e formatada a partir de áudio; conteúdo original já em português). Trecho publicitário (patrocínio HighGlobe) preservado no início por integridade da transcrição.

[Patrocínio] Esse vídeo tá sendo patrocinado pela HighGlobe, a melhor plataforma para receber pagamentos globais com menor custo garantido: apenas 0,3% de spread, sem taxas escondidas. Clica no link da descrição e usa o cupom "Montando20" para garantir 20% de desconto nos três primeiros meses fazendo transferências pela HighGlobe.

## Karpathy, o Claude Tag e a polêmica

Vamos falar do Karpathy sendo cancelado. Sim, ele falou algumas coisas sobre a Anthropic e o novo Claude Tag. Agora o Claude tá como um bot dentro do teu Slack.

Quando a Anthropic divulgou o Claude Tag, eu falei algo que eu tô começando a me arrepender. Deixa eu abrir aqui o anúncio pra vocês entenderem o que eu tô falando e a gente entra nesse tópico.

O que eu falei na internet sobre isso foi o seguinte: a Anthropic tinha basicamente comoditizado o próprio produto. Isso significa que o modelo dela tava "morto" — que a interface de @menção que tu ia poder colocar agora no Slack ia virar uma commodity, ia fazer o modelo virar commodity, que o que importa é o agente que tu tá construindo por debaixo daquele bot. Então, no momento em que a Anthropic possibilita que tu marque um bot ao invés de entrar na interface do Claude Code ou do Claude Desktop, nada impede a empresa no futuro de simplesmente trocar o que tá rodando por debaixo dos panos daquele bot. Essa foi minha primeira impressão quando vi que tu pode marcar o Claude dentro do Slack: seria como perder o usuário.

Mas hoje eu vim defender o lado contrário — eu vim defender inclusive o Karpathy, que recebeu muito hate porque ele postou o seguinte: "Cara, isso aqui é um novo paradigma."

Foi um exagero dele? Não — nesse vídeo eu vou defender ele. Vamos lá:

> "Este é um novo paradigma para interagir com o Claude, significativamente mais alinhado com todas as outras atividades humanas em toda a organização, depois de todo o trabalho de engenharia necessário para que ele simplesmente funcione — por exemplo em relação a ferramentas, integrações, ambientes de computação, memória, segurança etc. O Claude basicamente se junta à equipe de forma transparente."

Eu sinto que isso era o que a gente discutia quando usou o Devin — lembra do Devin, aquela IA que "roubaria o emprego do programador", que inclusive o Nubank utilizou pra refatorar um código que ia levar meses em poucos dias? O Devin tinha justamente essa abordagem: tu iniciava uma sessão pelo Slack e ele fazia o setup de um agente na nuvem — uma coisa que vocês vão ouvir falar muito esse ano, os "cloud agents", o agente que roda na nuvem. Basicamente ele cria um sandbox, faz o clone do teu repositório, inicializa o ambiente (tu pode parametrizar algumas coisas) e roda o que tu quer em cima daquilo.

Ao invés de ter vários workers no teu computador, tu pode inicializar vários agentes na nuvem. O benefício: eu posso, por exemplo, no meu celular, inicializar um agente sem precisar ter nada rodando no meu computador — o que é diferente do remote control que o Claude Code, o Codex e agora o Cursor também têm. Várias formas de interagir com esses modelos, mas interagir com o Claude no Slack aparentemente é um novo paradigma segundo o Karpathy (que inclusive está proibido de usar o Mitos, não é?).

E ele continua:

> "O Claude basicamente se junta à equipe de forma transparente. Você pode conversar com ele como conversaria com uma pessoa, e ele pode ajudar em uma grande variedade de cargas de trabalho. Na minha opinião, essa é a terceira grande reformulação da interface e experiência de usuário do LLM. O primeiro paradigma era o de que o LLM era um site que você acessava. O segundo, um aplicativo que você baixava para o computador. O terceiro paradigma é que ele é uma entidade autônoma, persistente e assíncrona, com ferramentas e contexto para toda a organização, trabalhando em conjunto com equipes de pessoas. Leva um tempo para se acostumar, mas funciona e é incrível."

Aqui, basicamente, temos o Claude trabalhando *com* o time, e não *para* um membro do time. É diferente. E com isso o feed se dividiu em dois: metade começou a gritar que de fato isso é incrível, uma mudança de paradigma; a outra metade começou a dizer "calma aí, isso a gente já tinha feito".

## Céticos certos tecnicamente, errados estrategicamente

Acho que os mais céticos (como eu fui no início) estão tecnicamente certos, mas estrategicamente errados.

O que a Anthropic realmente entregou, e por que o @Claude dentro do Slack não é apenas "um bot do Slack"? Ter um bot no Slack que pega teu prompt e retorna resposta já existe — não é nada de novo. Várias empresas fazem isso até pro time de produto ter acesso ao código-fonte de forma mais leiga, pra fazer perguntas. Aquelas perguntas que o time de design/produto fazia tipo "Lucas, como é a lógica de mostrar o menu de navegação no app?" — antes o programador tinha que ir ver no código ou perguntar pro Claude; agora o time de produto poderia fazer um @Claude, ou @bot criado internamente, e perguntar.

Mas o que a Anthropic lançou com o Claude Tag não é isso. O que ele tem de diferente:

- **É multiplayer**: um Claude por canal — o time inteiro se dirige ao mesmo agente.
- **Ele aprende**: constrói uma memória daquele canal e de outras fontes que tu vai liberando pra ele. Imagina um canal sobre deploys onde às vezes tu manda links do Sentry, Datadog e outros serviços de observabilidade/monitoramento/crash analytics — o Claude vai aprendendo tudo isso, e na próxima versão ele já sabe o que fazer.
- **É proativo** (modo "ambient"): ele se mete sozinho pra te avisar de algo. Não testei ainda, mas se for como imagino: toda vez que uma nova release é criada, um bot avisa no canal, programadores entram e discutem, mandam link do Sentry, o Claude aprende, e depois já traz esses links automaticamente. Provavelmente dá pra conectar skills ou subagentes nele.
- **Trabalha de forma assíncrona**: pega uma tarefa longa, se auto-agenda, e trabalha por horas ou dias nela.

Um número que achei interessante, do anúncio oficial (lido no The Next Web): a própria Anthropic diz que **65% do código do time de produto deles é criado pela nova versão do Claude Tag**. Não sei exatamente a diferença de escopo (ex: se o Claude Desktop também é escrito via Claude Tag), mas mostra a mudança que eu falava: normalmente uma mudança de paradigma acontece quando a empresa toda começa a atuar em cima de uma ferramenta, e no início as pessoas levam tempo pra se acostumar.

Aqui, acho que o que vai levar mais tempo pra as pessoas se acostumarem é que **a memória desse agente é compartilhada**: imagina que tu pede pra ele fazer algo, eu peço pra ele fazer outra coisa, e ele consegue unir essas duas pontas e ter contexto do que tá sendo feito ao mesmo tempo por todo mundo.

## A terceira reformulação da interface de LLM

Sobre o Karpathy falar que isso é o "terceiro maior redesign da interface de LLM": uma coisa que eu trago desde o início desse canal, lá quando o ChatGPT lançou e a gente fez o review aqui (uns 2-3 anos atrás — o tempo da IA roda diferente): ia chegar um momento em que a nova geração teria a primeira experiência dela com um sistema através de uma interface de chat com IA. Assim como a minha primeira experiência foi com o sistema operacional (Windows 95, ou um pouco antes), pra mim o conceito de pastas e arquivos de configuração é muito simples, mas pra uma geração mais nova, tu vai se surpreender se pedir pra criar um arquivo e salvar numa pasta lá no "C:" — eles nem sabem do que tu tá falando. Eles nasceram na era dos aplicativos; pra eles o padrão é aplicativo, e usam o sistema operacional só quando precisam de algo muito específico.

Acredito que pra nova geração o padrão vai ser conversar com a IA, e usar um aplicativo só quando precisar de algo muito específico. Eu acredito nessa mudança de paradigma, mas acho que a gente ainda não chegou nela. Acho que essa mudança que o Karpathy descreveu não é tão incrível assim tecnicamente — é um desafio tecnicamente muito grande, de fato, e aqui eu tenho que concordar com os céticos: um bot em chat com ferramenta e memória já existe há anos.

## O contraponto: Gergely Orosz (Pragmatic Engineer)

O contraponto que vi foi do Gergely, do Pragmatic Engineer:

> "It's not about Slack but about a Claude AI hooked up to all internal company systems that just works. This is the breakthrough."

Ou seja: o Slack é só a porta de entrada. O difícil, que ninguém tinha feito funcionar de verdade pra uma empresa comum, é uma IA na nuvem plugada em todos os sistemas internos — tools, integrações, ambientes de computação, memória, segurança — e as coisas simplesmente funcionarem, sem um time de plataforma de 10 pessoas mantendo a gambiarra.

Isso conecta com algo que eu já falava aqui no canal: uma das coisas que vocês precisam aprender não é "saber usar o Claude Code". Quando um entrevistador pergunta "tu sabe mexer com IA?", ele não quer ouvir "sim, baixei o Antigravity, usei o Cursor, testei o Codex, mas prefiro o Claude Code CLI". Ele quer saber se tu já fez RAG, se já configurou um bot, se já colocou um agente rodando numa VPS, se já integrou sistemas e ajudou o time de produto. É isso que meus amigos que trabalham com IA em empresas grandes estavam fazendo: compartilhar memória entre sessões de agentes, criar hooks que disparam auto-melhoria da própria documentação, etc. — é esse tipo de uso de IA que as empresas esperam que tu saiba.

E o mais incrível, como o Gergely falou: pra colocar um bot funcionando no Slack normalmente tu precisava de um time de várias pessoas pra fazer as integrações. E quando se fala de segurança — OTP, logins corporativos, sistemas atrás de VPN — tem muita coisa envolvida. Se de fato tudo isso funciona "e just works", é incrível, porque é o que tá escondido atrás dessa frase. Qualquer um que já tentou conectar um agente no Jira da empresa, no banco de produção e nas regras de acesso do RH sabe que a distância entre um bot que responde uma menção em 30 linhas e um agente confiável, worldwide, que não vaza dados, é gigante — assumindo todo o risco do vazamento.

## Anthropic ultrapassa a OpenAI no cartão corporativo

Um gráfico interessante: o gasto real de dezenas de milhares de empresas americanas no cartão corporativo. Em abril, a Anthropic passou a OpenAI pela primeira vez no cartão corporativo — subiu para 34,4% das empresas, enquanto a OpenAI caiu pra 32,3%. Isso significa que a Anthropic tá comendo uma fatia do bolo corporativo/business, que é onde tá a maior grana — algo em que o Google sempre se destacou, e que a OpenAI também tinha "destronado" o Google. A Anthropic veio e conseguiu um crescimento absurdo, muito ligado a essas funcionalidades que ela tá lançando.

No gráfico também aparece a xAI, ainda pequena, mas alugando por milhões os data centers do Elon Musk. Tem muita competição no B2B do uso de LLM via API, e muita geopolítica envolvida — e o Dario Amodei sabe que política é importante. Um vídeo de 2023 viralizou de novo recentemente, onde o Dario falava no Senado americano que a escala dos modelos open source tava se tornando muito perigosa — sinalizando uma postura de proteção contra o uso irrestrito de modelos open source.

Juntando essas peças: a Anthropic domina o "coding enterprise" e também vem ganhando força com pessoas físicas (programadores, mas também arquitetos, advogados etc. usando os modelos via Claude Desktop). É por isso que o hype em torno dela está tão alto.

## Vale a pena depender do Claude Tag? O risco de lock-in

Tem vários céticos discordando de forma respeitosa: "não tem breakthrough nenhum". Talvez o único breakthrough seja a Anthropic sair na frente de todas as outras grandes empresas corporativas e assumir o risco de integrar todos esses sistemas num único clique que simplesmente funciona (assumindo que seja de fato um único clique — eu não testei ainda).

Mas tem um risco importante: **o lock-in**. Quando o time todo despeja meses de contexto e memória dentro de uma tag, migrar pra outro lugar vai ficar complicado. Como CTO/CIO de uma empresa, eu ainda investiria em contratar dois ou três devs que manjam bastante disso pra fazer essas integrações internamente, e depois poder trocar o modelo por debaixo dos panos quando quiser. Pode ser legal colocar o bot da Anthropic pra ver o ganho de produtividade e as pessoas pegarem o ritmo, mas eu começaria a desenvolver minha própria solução em paralelo — isso também é commodity, como o próprio Karpathy meio que reconhece. Não foi "tão difícil" fazer o que foi feito — é software, não precisa de muito dinheiro pra construir algo parecido.
