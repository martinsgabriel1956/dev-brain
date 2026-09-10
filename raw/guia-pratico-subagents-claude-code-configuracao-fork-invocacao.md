Hoje: guia prático de subagents. Eu vou te ensinar como configurar e como spawnar subagentes no Claude Code — isso é traduzível para quase todas as outras harness, quase todas têm algo parecido com isso daqui. Vou te explicar como configurar, que dá para fazer isso de maneira automática (dá para você só deixar o Claude Code fazer por você), quando que faz sentido utilizar e quando que não faz sentido utilizar, e qual que é a minha recomendação, o que eu acho sobre isso.

Antes disso, vou te falar do patrocínio de hoje, que é a UVP — a maior e melhor escola de investimentos do Brasil. A UVP vai te transformar em um investidor em oito semanas. O que significa ser um investidor? Você vai conseguir analisar sua vida financeira como um todo: em qual patamar você tá, qual situação você tá, quais os próximos passos que você pode tomar para te levar de onde você tá agora pro momento em que você tenha uma carteira, uma construção de patrimônio, um planejamento financeiro adequado pro seu estilo de vida e para como você vê sua vida no futuro. Você vai ter mais de 120 aulas, com qualidade altíssima, sobre tudo que você precisa aprender sobre investimentos: renda fixa, como o FGC funciona, riscos de cada investimento, investir no Brasil e fora (Petrobras, Nvidia, Alibaba), tirar dinheiro do Brasil, ETFs irlandeses ou americanos cotados em dólar, ouro, Bitcoin. Além disso, sujeito à aprovação, cartão de crédito com acesso a sala VIP e cashback na fatura, comunidade da UVP, ferramental de Open Finance e a plataforma de investimentos que eu uso para investir no Brasil. Tudo começa no link na descrição, em "faça sua análise de perfil". Diz que você veio do canal e ganha um presentinho.

## O que são subagentes

Você vai ter o seu main agent — eu iniciei uma sessão aqui no Claude Code, estou aqui na minha sessão. Podemos imaginar esse main agent como uma instância: essa instância vai ter ali a sua conversa, vai ter ali as suas skills, vai ter ali os seus MCPs, plugins, etc.

Agora existe como você delegar algumas coisas para outra instância, para outro agente — esse outro agente a gente vai chamar de subagent. Esse outro agente pode herdar a conversa, algumas skills, MCPs, plugins, ou pode não herdar, dependendo de como a gente configurar ele. Aí você acaba conseguindo delegar algumas tarefas do main agent para o subagent, e depois elas voltam pro main agent revisar ou validar que tá terminado, etc.

Você consegue rodar em paralelo — eu já rodei, acho que o número máximo foi 14 subagents, e lidou tranquilamente. Se você conseguir separar as tarefas em pedaços que são paralelizáveis, não tem problema você spawnar vários subagents.

## Fork não é subagent

Um subagent não é uma duplicação da sua conversa no main agent. Tem como você pegar isso aqui e falar "eu quero duplicar, eu quero ter dois main agents, eu quero fazer um fork do meu main" — o fork vai clonar tudo, vai clonar todo o contexto, vai clonar toda a conversa, vai clonar tudo que você tinha no seu agent. Você vai estar clonado ali no fork.

Com `/fork`, ele spawna um background agent que herda toda a conversa — assim que o fork funciona. Você tem também a parte de subagents, que não é o fork. E note que o `/agent` do Claude Code foi removido (vamos falar como invocar esse agente).

## Como invocar um subagent

Existem três principais maneiras de invocar um subagent, de fazer o Claude Code invocar uma instância nova:

1. **Linguagem natural.** Abre o Claude Code e fala: "Inicie um novo subagent que vai trocar a paleta de cores para pastel", dá enter. Ele vai de fato inicializar esse subagent — carrega a skill relacionada (ex.: front change design), roda uns shell commands preparando a tarefa que vai passar para o subagent, e cria o agente. Aparece embaixo um "General Purpose", um agente de propósito genérico realizando a tarefa em background, enquanto você pode pedir outras coisas pro seu main agent.

2. **Menção explícita ao agent.** Você precisa ter criado esse agente em algum lugar (ou pedido pro Claude Code criar). Você dá o `@` e dentro dele o nome do seu agente — por exemplo `@code-reviewer` — no formato `@"code reviewer agent"`. Quando você começa a digitar ele aparece na lista, e você passa o prompt para esse agente. Exemplo: um code reviewer agent para consertar um PR — copia o link do PR, passa pro agent, ele pede permissões, você aceita, e ele instancia o Code Reviewer Agent em background. Dá para entrar no subagent e ver o que ele está fazendo, ou voltar pro main.

3. **Fora do Claude Code.** Você dá `claude --agent <nome-do-agent>`, por exemplo `claude --agent code-reviewer`, e ele já começa a sessão inteira do Claude Code dentro desse agente específico, com o contexto e a maneira com que esse agente deve rodar.

## Para que serve um subagent, além de paralelizar

O Claude Code já tem pré-instalado o **General Purpose Agent**, um subagente de propósito genérico. Se você pedir por um subagent, provavelmente o Claude Code vai instanciar esse agente, que herda o mesmo modelo da conversa principal (se você tiver conversando com o Fable, o subagent é instanciado no Fable). Ele é geralmente utilizado para delegar alguma tarefa e depois voltar pra você.

Se você estiver alterando várias coisas em paralelo, fazendo várias tarefas em paralelo, é possível que o próprio Claude decida instanciar subagentes, ou você pode pedir para fazer isso: se você tem uma tarefa, quebrou em 10 subtarefas, você pode pedir para rodar um subagent por subtarefa e depois analisar o output de cada um para ver se está correto. Na minha visão, o agente de propósito geral do Claude Code funciona bem.

## Configurando seus próprios subagents

Você pode configurar seus próprios subagents. Na pasta `.claude` — dentro do seu projeto ou na global, dependendo se você quer o subagent só pro projeto ou global — você pode criar manualmente um arquivo, ou pedir pro Claude criar esse arquivo; ambas maneiras funcionam. Em `agents/` você vai ter o `.md` explicando como funciona o seu agent.

Ele tem um system prompt que explica o que o agent faz — sinceramente, acho essa parte não tão relevante assim; as configurações de cima são bem mais legais. Você tem o nome do subagent, a descrição do subagent, e embaixo disso as coisas mais interessantes:

- **Tools.** Quais ferramentas esse subagent tem acesso. Por padrão, tem acesso a todas.

- **Model.** Essa parte é legal porque, na minha visão, é quase pra isso que se configura um subagent: para você ter um main agent rodando em algum modelo inteligente, como Fable ou Opus, e um subagent rápido, simples, que vai economizar tokens. O seu main pode quebrar uma tarefa complexa em várias tarefinhas simples — pegar os arquivos, definir o entry point de cada tarefa, como validar que cada tarefa está feita — e delegar isso pro subagent com um modelo mais simples. Para mim, uma das grandes vantagens de ter um subagent é criar um subagent que vai utilizar um modelo diferente do seu main agent: um agente mais completo, mais complexo, mais caro, mais lento, e um subagent rápido e simples que economiza tokens.

- **Permission mode.** Você pode configurar o modo de permissão do subagent. Os modelos de permissão são: `default`; `acceptEdits`, que autoaceita edição de arquivos; `dontAsk`/`deny`, que automaticamente nega as permissões que não são explicitamente permitidas; `bypassPermissions`, que simplesmente aceita tudo, pula as permissões; e `plan`. Para um subagent eu gosto de `acceptEdits`. Se estiver rodando dentro de uma VM ou de um dev container, aí você pode rodar com `bypassPermissions`, que acho tranquilo — mas só nesse caso, porque se você rodar em paralelo 1 milhão de agentes com bypass, alguma hora vai dar ruim.

- **Isolation / worktree.** Dá pra definir para um subagent rodar de maneira isolada numa worktree, para não entrar em conflito com outros agentes — isso é legal também, se você tiver usando worktree pode ser interessante.

- **Max turns.** É o número máximo de round trips de uma tool call. Honestamente não acho que você precisa configurar isso.

- **Skills.** Define quais skills vão ser injetadas como contexto para dentro do subagent. De maneira geral, o seu agente não vai ter no contexto todas as skills que você tem, mas ele pode descobrir essas skills usando a ferramenta de skills — então se você não configurar nada aqui, é provável que o subagent descubra por conta própria quais skills existem e use as que forem relevantes. Se você quiser explicitamente pré-injetar algumas, pode. Se quiser proibir o acesso às skills, dá pra usar `disallowedTools` colocando a ferramenta de skill como não permitida, e o subagent não vai conseguir usar suas skills — eu não sei por que você faria isso, mas dá pra fazer.

  Pessoalmente, num subagent de code reviewer, eu pré-carregaria as skills que têm relação com revisão de código ou com os padrões da minha codebase específica.

- **Memory.** É a memória do subagent — se a gente quiser permitir uma memória persistente nele, existem três tipos: memória a nível de **user**, em que o subagent lembra de coisas em todos os seus projetos; memória de **projeto**, em que o subagent lembra de aprendizados pertinentes a esse projeto (só faz sentido se a auto memory estiver ligada); ou memória **local**, que não entra no versionamento de Git — versus uma memória compartilhada com a equipe inteira, que entra no Git e o Claude Code de todo mundo tem acesso à mesma memória, ou uma memória local só sua, do jeito que você usa.

- **Background.** Se é para rodar o agente em background ou não. Para mim faz sentido, acho que sim.

## Minha opinião

Dito tudo isso, agora a parte mais opinativa e pessoal do vídeo: eu não abusaria de subagents. Acredito que fazer muito trabalho em paralelo faz com que a gente preste menos atenção no nosso trabalho — não acho que você vai ficar o tempo todo rodando 20 subagents em paralelo. Acho que a velocidade com que as IAs fazem código já é muito rápida, e a gente muitas vezes não precisa paralelizar tanto assim.

Tendo em vista que não acho que o paralelismo massivo é onde está o ganho do subagent, acho que o ganho está em iniciar um pedaço de tarefa sem ter todo o contexto da história — um contexto reduzido, uma tarefa bem definida, com um modelo já pré-definido (que pode ser um modelo menor), e essa tarefa vai ter um ciclo de vida curto. Acho que a vantagem do subagent acaba sendo mais o isolamento do que o paralelismo massivo.

Acho interessante você conhecer essas configurações que eu te mostrei, mas acho que você não precisa pirar muito nisso. Nos meus testes: se você configurar tudo com maior cuidado, fazer tudo certinho, ou se você não configurar absolutamente nada e só pedir pro Claude Code, o resultado final na minha visão é bem parecido.

Quando eu acho útil utilizar um subagent: peguei uma tarefa muito grande, quebrei em tarefas pequenas, essa tarefa pequena tem entry points, tem critério de aceitação, tem os arquivos prováveis, ela é bem definida, não é muito grande — acho legal delegar isso para subagents. Um code review também é um caso legal de delegar para um subagent, porque você vai ter alguém que não tem o contexto de escrever o código revisando.

Fora esses casos de uso, acho que eu não usaria e abusaria tanto assim. Não é uma ferramenta muito legal, tem muito hype em cima disso, mas acho que a gente tenta complicar algo que é bastante simples. Honestamente, não acho que causa ganhos expressivos em performance, velocidade, ou qualquer outra coisa — acho que é mais uma questão de se organizar um pouco melhor.

Se você quiser aprender mais comigo, temos diversos cursos aqui no canal, o link vai estar na descrição, se quiser conferir o sitezinho com os cursos. A gente também tá preparando um workshop/bootcamp — estamos preparando uma série de conteúdos de IA. Se tiver interesse em entrar na lista de espera pro nosso conteúdo de IA (ainda sendo produzido, não sei exatamente qual formato vai ter), tem uma lista de espera aqui embaixo, e quando ficar pronto eu mando um e-mail explicando o que é. Eu e mais um sócio estamos trabalhando em juntar todo o nosso conhecimento de IA em algo legal. É isso.
