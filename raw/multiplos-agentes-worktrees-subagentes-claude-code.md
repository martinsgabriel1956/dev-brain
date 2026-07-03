# Múltiplos Agentes no Claude Code — Work Trees e Subagentes

Continuamos, vamos para múltiplos agentes agora, porque esse é um tema mais profundo e acho que vai ser muito relevante para vocês. Múltiplos agentes dentro do Claude, tem como a gente trabalhar com agentes paralelos de duas formas: através de work trees e de subagentes.

O que são agentes paralelos? É basicamente eu conseguir fazer mais de uma tarefa ao mesmo tempo. Então, digamos, quando eu estou aqui no meu Claudinho — vamos lá, fazer `cd Desktop`, `cd RDV`, `cd CCAT app` — vou abrir o Claude. Quando eu estou aqui no meu Claudinho e peço para ele fazer alguma coisa para mim, por exemplo "troque todos os H2 para começar com 'olá mundo'", vamos pedir para ele fazer uma coisa. Quando eu dou um enter aqui, ele começa a processar. Enquanto ele tá fazendo isso, se eu não tivesse como rodar múltiplos agentes, eu ia ter que esperar ele terminar essa tarefa para pedir uma nova coisa para ele.

Só que tem certas coisas que a gente faz no nosso dia a dia, num mesmo projeto, que podem ser paralelizadas. Então, enquanto ele troca todos os H2 no projeto, eu poderia pedir para ele já ir corrigindo um teste unitário meu que tá falhando, né? São duas tarefas que dá para paralelizar. E aí, para paralelizar essas duas tarefas, é onde a gente pode trabalhar com work trees ou subagentes.

## Work Trees

Work trees, quando a gente fala disso, é basicamente paralelismo a nível de file system. Então, quando a gente usa work trees, a gente basicamente vai estar rodando uma sessão do Claude em uma cópia do nosso repositório principal. Ele vai criar uma cópia dos arquivos do repositório original e vai trabalhar em cima daqueles arquivos.

Dessa maneira, toda vez que eu abro uma nova work tree, cada um trabalha no seu mundinho separado, né? Cada agente tá trabalhando no seu mundinho separado e eles não têm conflitos entre as tarefas. Então eles podem inclusive estar mexendo nos mesmos arquivos ao mesmo tempo e isso não vai dar conflito entre eles, porque, apesar do agente 1 ter mexido no arquivo `autenticacao.tsx` e o agente 2 também ter mexido no arquivo `autenticacao.tsx`, esses dois arquivos, apesar de serem o mesmo a nível de conceito, a nível físico eles não são — porque quando eu abri essa nova work tree, ele criou uma cópia do repositório como um todo para trabalhar em cima dele.

E aí eu consigo lançar essas work trees pelo terminal só rodando um comando do Claude, que é `claude --worktree`. Antes disso ser algo nativo do Claude, a gente tinha que criar manualmente uma work tree do Git. Work tree é um conceito do Git, não é algo que o Claude Code inventou — já existe há muito tempo, já é um comando do Git. Só que a galera da Anthropic foi muito esperta e colocou isso como um funcionamento padrão do Claude.

Dessa forma, a gente pode vir aqui no nosso Claudinho e abrir um novo terminal e lançar uma nova work tree. Só que aí, percebam: ao abrir um novo terminal e chamar o meu Claudinho, eu já tô conseguindo fazer tarefas em paralelo, né? Tô vendo, eu tô com um Claudinho aqui e outro Claudinho aqui, são dois Claudes. Esse Claude tava mexendo nos textos e eu poderia pedir para esse outro Claude, o segundo Claude, ir corrigindo os testes que estão falhando. "Corrija os testes que estão falhando."

O problema é que o Claude 1 e o Claude 2 estão mexendo no mesmo projeto, na mesma pasta. Então, caso por algum motivo o Claude 1 e o Claude 2 acabem modificando o mesmo arquivo, vai dar conflito, porque eles estão coexistindo na mesma "bolinha", no mesmo mundo. E aí que entram as work trees, que era o que eu tava explicando para vocês, pra gente evitar esse tipo de problema.

Eu posso disparar uma nova work tree, e o Claudinho 2 não ia estar modificando no mesmo espaço de arquivos que o Claudinho 1 — ele ia ter criado uma cópia só para ele. Como é que eu posso fazer isso? É bem fácil: eu venho aqui, deixo fechar o Claudinho 2, crio um novo Claudinho, abro um novo terminal (fiz um `Cmd+T` aqui para abrir um novo terminal) e, ao invés de só lançar o Claude (só chamar o Claudinho), eu vou chamar `claude --worktree` e vou dar um nome para essa work tree. Vou chamar de "improve unit testing".

Se eu olhar esse meu Claude 1 — qual o contexto que ele tá trabalhando? Esse meu Claudinho 1 tá vendo, ele tá trabalhando em `/Desktop/HiperDev/certificates-app`. Ele tá trabalhando em cima dos arquivos que estão dentro dessa pasta `certificates-app`. Se eu abrir aqui no meu Finder, vai ficar visual pra vocês: tô na minha mesa, né, no meu `Desktop/HiperDev/certificates`, é aqui que o Claudinho 1 tá mexendo nesses arquivos.

O Claudinho 2, quando eu lancei uma nova work tree, ele criou uma cópia para ele, e ele cria essa cópia dentro da pasta `.claude`. Então ele tá mexendo em `/Desktop/HiperDev/certificates-app`, mas em `.claude/worktrees/improve-unit-testing`. E se eu abrir essa pasta `improve-unit-testing` lá no meu Cursor, pra mostrar pra vocês como é que estão os arquivos — se eu abrir `.claude/worktrees/improve-unit-testing`, eu vou ver que tem uma cópia de todos os arquivos aqui dentro.

Então todas as modificações que eu fizer dentro desse meu chat com o Claudinho 2 vão ser feitas dentro das cópias dos arquivos e não nos arquivos principais. Dessa maneira eu evito conflito e consigo trabalhar com múltiplos agentes sem conflito.

Quando eu finalizar essas alterações, eu crio uma PR, crio um pull request — não tem muito mistério. Criei uma work tree e, quando eu encerro um chat com o Claudinho 2, eu peço para ele encerrar a work tree também, para não deixar ela aqui existindo. Dentro do `CLAUDE.md`, a ideia é que sempre que finalizar uma modificação você finalize a work tree, porque senão isso aqui vai ser commitado — na verdade você pode até colocar isso no `.gitignore`, mas se não tiver no gitignore você vai commitar isso.

Então a ideia é que, quando finalizar as alterações que você tá fazendo ali em paralelo, você commite, encerre essa work tree, abra o pull request, enfim, faça ali o seu fluxo de Git.

## Subagentes

Mas existe outra maneira da gente trabalhar com múltiplos agentes, que é através de subagentes. Diferente das work trees, eles não são paralelismo a nível de file system, eles são paralelismo a nível de contexto. Então, quando a gente trabalha com subagentes, a nossa sessão principal ali do Claude (o nosso chatzinho com ele) basicamente vai delegar trabalhos para subagentes, que nada mais são do que threads que estão sendo lançadas, que vão trabalhar numa task específica.

Ele faz isso usando a tool `Task` — lembra que a gente aprendeu que são ferramentas do Claude que permitem que ele seja agente. Cada subagente que o Claude lança é como se ele tivesse lançando processos mesmo, né, um processo iniciando outros processos. Quando o Claude inicia esses outros subagentes, cada um dos subagentes tem uma janela de contexto própria.

E aí, o grande ponto, a grande diferença do subagente para uma work tree, é o seguinte: quando eu tô usando a técnica de work trees, cada work tree é um espaço de trabalho, um file system diferente e independente. E quando eu finalizo o trabalho numa work tree e na outra, são dois trabalhos diferentes, onde eu vou ter duas branches — no final vão ser duas branches separadas com modificações diferentes que os agentes geraram, e são funcionalidades apartadas que eu vou criar PRs separados.

Quando eu trabalho com subagentes, como é paralelismo a nível de contexto e tá tudo existindo dentro da mesma janela do Claude, quando os subagentes finalizam o trabalho deles, o trabalho deles é unido, é convergido numa única coisa. O chat pai consolida o trabalho de todos os subagentes numa única coisa, e no final isso vai gerar uma única PR, uma única síntese.

E aí a vantagem de usar subagentes num chat pai é economia de janela de contexto. Então, se eu preciso, dentro de uma única tarefa que eu passei pro meu Claude, modificar tanto backend quanto frontend, quanto escrever teste unitário, escrever documentação — se eu fosse fazer isso tudo dentro de uma única janela de contexto, a minha janela de contexto ia encher muito rapidamente, e eu já ia ter que ficar compactando janela de contexto. O resultado já não ia ficar tão legal.

Agora, se eu criar agentes específicos — um especializado em backend, um especializado em frontend, um especializado em documentação e outro especializado em teste — e eu faço o meu chat pai lançar esses subagentes, cada um responsável por uma tarefa com janela de contexto separada, executarem suas tarefas e depois se unirem num resultado só, e a janela pai ir coordenando cada um dos subagentes, eu economizo janela de contexto e tenho um resultado mais eficiente.

### Como escrever subagentes

Muito fácil. De novo, lá no meu repositório `certificates-app`, se a gente olhar a minha pastinha `.claude`, a gente tem dentro dela uma pasta `agents`. Aqui a gente criou alguns agentes nossos que existem a nível de projeto. Aquela regrinha que eu tinha explicado no começo da live, da hierarquia dos arquivos — que existe hierarquia a nível usuário, a nível projeto e a nível diretório — o mesmo se aplica para as skills, como a gente mostrou antes, e o mesmo se aplica pros agentes. Eu tenho agentes nível de usuário, nível de repositório.

A gente criou, por exemplo, o nosso "backend engineer", o nosso "CTO", o nosso "frontend engineer", o nosso "infrastructure engineer", cada um responsável por fazer tarefas específicas, cada um com detalhamento de quais skills eles devem utilizar. E aí a gente tem um agente que seria o nosso CTO (ou "tech lead", como preferirem chamar), que é o responsável por delegar as tarefas.

Ele tem um time — "your team" — e ele deve despachar pro time dele, que são outros subagentes, de acordo com o cargo de cada um do time. Então pro backend engineer ele delega tarefas de API routes, de server actions, de mexer no Prisma, autenticação etc. Pro frontend engineer ele delega tarefas de React, de página, de estilização. Pro de infrastructure ele delega coisas de CD, de DevOps etc. E o Product Manager ele delega coisas de roadmap, PRD etc.

Então esse meu subagente vai ser usado como meu orquestrador principal de novas funcionalidades no certificates-app, e então ele vai despachar os especialistas em cada coisa. E se vocês olharem de novo o formato do arquivo, é idêntico ao de skills — é a mesma coisa no final, é tudo contexto, é tudo instrução. É só um nome diferente que tem propósito diferente, mas no final é tudo instrução.

Se eu olhar o detalhamento aqui do meu subagente, é um arquivo Markdown com uma metatag aqui em cima, escrevendo o nome desse subagente, uma descrição pro Claude saber quando usar ele, inclusive uma cor (isso vai mudar a cor do terminal quando ele estiver rodando), e aqui uma instrução gigantesca explicando pra ele como ele deve se comportar, regrinhas etc.

### Como despachar os subagentes

Duas formas: eu posso fazer invocação automática via texto, ou fazer os subagentes customizados que nem eu mostrei pra vocês.

Como é que é um despacho automático de subagentes? Vou mostrar exatamente pra vocês. Vou abrir aqui meu Claude e vou pedir pra ele fazer essa tarefa: "Pesquise em paralelo como o Brevo e o Postmark lidam com webhooks de bounce, compare e me diga qual se encaixa melhor nesse projeto." Vou lançar essa tarefa.

O Claude é inteligente o suficiente para saber... Pera aí, que eu tô com effort low, talvez não funcione. Vamos lá, deixa eu só trocar o effort pra high, porque é uma tarefa de pesquisa. Pronto, agora de novo vou mandar a mesma tarefa pra ele. E aí o próprio Claude já vai perceber que essa é uma tarefa que ele consegue fazer em paralelo, despachando parallel agents. Ele falou: "Perfeito, vou despachar três agentes em paralelo, um por provedor."

E aí a tarefa de cada um desses subagentes, que eles forem fazer essas pesquisas, não vai consumir a janela de contexto desse meu agente principal, desse agente pai. Cada um vai agir em paralelo, vai fazer as pesquisas e vai voltar só com o resultado, e somente o resultado da execução desses caras vai ser imputado na janela de contexto do agente pai — as demais informações que eles produziram durante toda a pesquisa não vão. Dessa maneira eu consegui lançar três subagentes no disparo automático.

Mas, como eu falei pra vocês, a gente pode criar agentes customizados, que era o exemplo que eu tava dando pra vocês aqui, dos nossos agentes de CTO, de backend, de frontend, que eu crio dentro da pastinha `.claude/agents`. Pode existir tanto a nível de usuário, como comentei, quanto a nível de projeto.

E aí, como é que o Claude vai saber quando chamar esses agentes? De acordo com a descrição que eu passei ali, e o Claude vai acionar esses agentes somente quando necessário. Um exemplo clássico de agente, que tem até na documentação da Anthropic, é criar um agente específico para revisão de código.

No final é tudo texto, é tudo prompt, é tudo prompt bem feito, é tudo encadeamento de prompt, injeção de contexto — mas eles criaram essas nomenclaturas de cada uma das coisas só pra gente saber quando a gente tá usando um prompt de um jeito, um prompt que paraleliza, um prompt que não paraleliza, um prompt que serve como input de contexto maior. Tudo prompt no final.

### Modelo e tools por subagente

Uma coisa legal de criar subagentes é que a gente pode inclusive definir qual é o modelo que esse subagente vai usar. Isso é legal — diferente das skills, que a princípio não dá pra setar modelo nem tools, porque a skill no final é só um prompt reutilizado, uma pasta com instruções pra serem carregadas dinamicamente e injetadas no contexto do Claude quando ele precisar.

Já o subagente, como ele roda em paralelo, tem um papel um pouco mais profundo: eu consigo definir o modelo que esse subagente vai rodar. Posso setar, por exemplo, pro meu modelo de Product Manager eu vou usar o Opus, pros outros que vão só implementar eu vou usar o Sonnet, e pra um que vai fazer só escrita de documentação eu vou usar o Haiku.

Então eu consigo definir o modelo pros agentes, e consigo definir também as tools que ele tem disponível. Dá pra definir as tools que ele vai ter. Esse exemplo aqui de um agente que seria um "code reviewer", que vai revisar meu código — como ele só vai revisar, ele não vai escrever nada, ele não precisa ter a tool nativa para modificar arquivo. Ele só tem as tools de Read, Grep, Glob e Bash, né, lembra que eu expliquei o que era tool no começo da live. Tool é o que dá poder pro agente, o que faz com que ele consiga fazer ações e não só escrever texto.

Então a tool de Read permite que ele leia o conteúdo de arquivos. A tool de Grep/Glob permite que ele busque conteúdo dentro dos arquivos. E a tool de Bash é pra ele rodar comandos no Bash e interagir com o Bash. E aí eu consigo especificar as tools desse agente — não preciso colocar todas, isso vai diminuir a janela de contexto dele também, limitando o número de tools que ele tem, porque esse agente só precisa dessas tools.

Vamos ver a lista de tools do Claude — quanto que as tools consomem de tokens do system prompt dos modelos. A tool de `Agent` permite que ele "spawne" subagentes. A tool de `AskUserQuestion` permite que ele faça aquelas perguntas pra gente (lembra que a gente respondeu uma pergunta antes na live também, no meu Claude Desktop, eu respondi uma pergunta pra ele porque tinha uma skill que eu usava que fazia com que ele me perguntasse coisas antes de dar o resultado — isso é através de uma tool). A tool de `Bash` permite que ele execute comandos no shell. A tool de `Glob` é pra achar arquivos baseado num pattern matching, e a `Grep` é pra achar conteúdos dentro de um arquivo através de pattern matching — um é pra procurar arquivo através de pattern, e o outro pra procurar conteúdo dentro do arquivo através de pattern.

Enfim, todas essas tools estão disponíveis nativamente no Claude Code, isso é o que dá poder pra ele fazer ações. E a gente pode inclusive setar as tools dos nossos subagentes e limitar esse número de tools para diminuir o system prompt do agente, diminuir o quanto de prompt ele vai gastar. Tudo isso vai otimizar os tokens gastos no final, se a gente construir bem os nossos subagentes.

Então, quando forem construir subagentes, escolham as tools corretas — escolham as tools que ele necessita somente, para evitar system prompt muito grande, pra evitar "bazuca pra matar formiga". Resumindo: esse caso do frontend engineer, por exemplo, usa as tools de Read, Write, Edit (pra editar arquivo), Glob, Grep. Todas as outras tools, de "spawnar" outros agentes, de fazer outras coisas aqui, de rodar cron job (esse `CronCreate` é basicamente pra ele fazer schedule de tasks) — todas essas outras coisas ele não tem disponível, porque aquele subagente ali é um subagente que vai fazer só uma tarefa de frontend, todo o resto ele não precisa. E tudo isso otimiza os tokens que eu gasto.

### Disparo forçado de subagente customizado

Aí é o que eu tava explicando, como "spawnar" os agentes automaticamente, que foi quando eu pedi pra ele fazer as tarefas em paralelo — o próprio Claude pai "spawnou" os três subagentes pra fazer as pesquisas. E tem como a gente criar os subagentes manuais, e aí ele vai "spawnar" só quando precisar. Vou tentar "spawnar" um aqui forçado pra gente.

Ele tá perguntando se pode fazer o fetch, pode fazer. Vamos abrir um próximo aqui, eu vou abrir o Claudinho e vou pedir pra ele: "Plan a big... we will refactor the frontend and backend to ensure that not any... look for public routes or for data that are being transmitted not encrypted" (não sei escrever "criptografado" em inglês, mas enfim) — uma tarefa qualquer de segurança. Eu só inventei: "Vamos refatorar o frontend e o backend para garantir que não tem nenhum problema de segurança, procure por rotas públicas e que não tem nenhum dado sendo transmitido de forma não criptografada."

Então essa tarefa, teoricamente, era pra fazer com que ele acionasse o meu agente de CTO. Ele primeiro acionou minha skill de "security review", que é uma skill que eu tenho aqui. Eu quero ver se ele vai acionar meu subagente.

Uma coisa que eu sinto: quando a gente tem muita skill, muito subagente, muita coisa, acaba ficando até confuso pro próprio modelo saber quando ele deve usar cada coisa. No meu caso, eu tenho já umas 300 skills que eu baixei da internet, porque a gente consegue baixar skills — não sei se vocês sabem — do GitHub, da galera. Então a galera, por exemplo, procura "skills Claude" e vai aparecer um monte de repositório do GitHub, tipo "awesome claude skills", e dá pra baixar todas essas skills. Tudo isso são pastas que a gente pode baixar, que nada mais são do que skills. Poderia baixar tudo isso e usar no meu Claude, então eu inclusive já baixei muita skill online, meu Claude tá cheio de skill, cheio de parafernália, cheio de subagente duplicado. E aí as pessoas, às vezes, acabam mais atrapalhando do que ajudando, porque ele não sabe o que usar.

Aqui eu queria que ele "spawnasse" o CTO, porque é uma "big notification", mas ele acabou primeiro "spawnando" a minha skill de "security review", aí ele tá lendo os arquivos, tá explorando e tudo mais. Agora ele tá me pedindo pra ler o que ele pode fazer, tá lendo os arquivos.

Então uma forma de eu pedir pra ele explicitamente usar o CTO seria eu pedir pra ele usar o CTO, senão eu vou depender da identificação automática dele de que ele deveria utilizar aquele subagente. Esse é o problema de ter muita parafernália, que é o meu problema hoje: tenho coisa demais, um monte de agente, um monte de coisa, e às vezes ele não usa o que eu queria que ele usasse, porque eu tenho um monte de coisa que tem overlap com aquela tarefa — tem uma skill que faz aquela tarefa, tenho subagentes, tenho rules e skills a nível de usuário, skills a nível de projeto, e acaba ficando um monte de parafernália, que no final é um monte de coisa que enche a minha janela de contexto.

Então tem que tomar cuidado também com o uso de todas as ferramentas que eu apresentei pra vocês, porque se a gente botar coisa demais que não precisa, às vezes vai acabar ficando mais confuso.

## Uso prático: work trees vs. subagentes

Mas é basicamente isso. Acho que terminamos aqui. O que eu mais tenho usado para agentes paralelos mesmo é work trees. Eu disparo duas work trees, cada uma com seu file system separado, os agentes vão trabalhando ali em cima, e no final eu crio uma branch e faço/abro os PRs. É basicamente isso que eu faço quando eu quero fazer tarefas em paralelo.

O Léo tem usado muito subagentes, ele achou bem mais utilidade do que eu. Ele usa muito um subagente pra ir modificando o backend enquanto o outro tá fazendo o frontend e outro vai escrevendo a documentação — é um caso clássico que o Léo usa bastante. Eu confesso que eu não uso tanto.

É basicamente isso. Aqui eu botei também como criar subagentes, mas sem novidade nenhuma — dá pra gente usar o próprio Claude para criar subagentes. A gente pode criar um subagente em `.claude/agents` chamado, por exemplo, "supabase migration reviewer", que valida migrations seguindo as regras que estão especificadas em `.claude/rules`. Então o próprio Claude te ajuda a criar pequenos Claudes, subagentes.

### Tabela de comparação: quando usar cada um

- **Quero ler muitos arquivos, fazer pesquisas na internet para tomar uma decisão e fazer uma feature, mas não quero entupir minha janela de contexto** → uso **subagentes**, porque tudo no final vai virar uma única coisa — todo esse trabalho em paralelo converge para uma única tarefa.
- **Preciso editar alguns arquivos do meu projeto sem que outro agente que tá rodando sobrescreva esses arquivos** → vou criar uma nova **work tree**.
- **Quero criar N implementações** (por exemplo, três versões diferentes de uma mesma feature/POC para ver qual funciona melhor) → uso **work trees**, porque vou ter três cópias do meu projeto e cada agente vai trabalhar numa cópia separada, sem uma sobrescrever a outra.
- **Quero fazer diversas pesquisas e análises e consolidar em uma única resposta** → **subagente**.
- **Vou fazer tarefas independentes que vão virar PRs separados** (por exemplo, peguei duas tarefas do Jira/Linear que são coisas diferentes e vou fazer as duas em paralelo) → uso **work trees**.
- **Vou fazer uma tarefa gigantesca, que pode ser dividida em várias partes mas no final é uma única coisa** (por exemplo, uma tarefa que envolve mexer no front, no back, documentação e teste) → posso usar **subagentes**, mas no final vira uma única coisa, uma única PR, uma única modificação.

---

Esse quadro que você assistiu foi retirado do nosso live coding, que acontece todo segundo e quarto domingo do mês lá no nosso canal principal, com vários conteúdos bem profundos sobre programação e tecnologia. Se você gostou, não esqueça de deixar seu like, se inscrever aqui no canal de cortes e também acompanhar a live ao vivo lá no nosso canal principal. Valeu!
