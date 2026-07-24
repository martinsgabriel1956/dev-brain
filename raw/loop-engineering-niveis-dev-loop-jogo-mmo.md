# Loop Engineering: Os Níveis do Dev Loop e um Jogo Completo Construído em um Final de Semana

> Transcrição de vídeo em português, colada pelo usuário no chat e reorganizada em seções/parágrafos para leitura (removidas repetições e hesitações de fala; conteúdo não traduzido — já em português). Autoria não identificada no texto colado.

## Abertura

O Ban acabou de ser migrado para Rust — mais de 500.000 linhas de código — usando Loop Engineering, e toda a indústria está falando de Loop Engineering como se fosse a próxima grande coisa da IA. A internet explodiu nas últimas semanas com o criador do OpenCode, Peter, falando que não dá mais prompt, só trabalha em loops. O Boris, criador do Claude Code, falou algo bem similar: que ele trabalha em loops que decidem o que fazer. E a internet explodiu falando de loops como se fosse a próxima grande coisa que vai resolver tudo na IA.

Neste vídeo, além de mostrar como criar loops e os patterns principais de loop, também vou dar um code base completo de um jogo que fiz em um final de semana usando patterns avançados de loop engineering, todas as minhas skills e técnicas, para vocês conseguirem aplicar nos próprios projetos.

## Os Três Níveis do Dev Loop (Antes do Boom de Loop Engineering)

Antes do boom de loop engineering, a gente já vinha trabalhando com uma progressão de níveis de loop:

### Nível 1 — O Loop React

O primeiro loop que veio a público. Quem está desde o início de 2023 com IA lembra: a gente saiu do chat onde dava um prompt, esperava a resposta, dava mais um prompt — para o modo agêntico, onde tu dá um prompt e o agente fica num loop trabalhando até resolver aquele prompt que foi dado. Esse foi o primeiro loop criado, e em cima dele começou a automatização de coisas.

### Nível 2 — Spec Driven

Um clássico. Spec driven é uma lista de passos que dão gatilhos em vários loops de agentes por baixo — ou seja, o loop React do agente a gente não controla diretamente, mas tem controle em cima dele. Com spec driven a gente dá uma "receita" que executa vários loops: um loop para planejar, um loop para criar o design, vários loops (cada um) para implementar uma task.

No nível 1, um prompt fazia o agente loopar até fechar aquela tarefa — permitindo tarefas de alguns minutos. Com spec driven, um prompt aciona uma estrutura muito maior que executa vários loops, permitindo implementar coisas que levam horas. Só que quando essas coisas terminam, entra o humano.

### Nível 3 — O Humano no Loop

O humano entra para: abrir um pull request; decidir o próximo passo ("terminei de implementar essa spec, tenho que planejar a próxima"); consultar métricas; fazer triagem de um bug (investigar o bug, criar uma task do bug, fazer um plano para implementar o fix). O humano ficava nessa camada.

## A Proposta de Loop Engineering

A ideia do Loop Engineering — como o criador do Claude Code e o Peter (OpenCode) estão falando — é adicionar mais uma camada acima do nível 3. O criador do OpenCode é mais vibe coder (fez todo o OpenCode com vibe coding), então nem tudo que ele fala encaixa perfeitamente em desenvolvimento de software enterprise mais complexo, mas o criador do Claude Code é uma referência melhor para esse contexto.

A proposta: se já existia a camada de "mini loop do spec driven", adiciona-se mais uma camada que automatiza mais, permitindo sair de "horas numa spec" para "dias implementando vários planos/passos". Não precisa necessariamente ser uma spec do spec driven — pode ser, por exemplo: bater num Datadog, pegar informações de um incidente, criar uma task, planejar a task, ver a severidade, notificar as pessoas, implementar, abrir um pull request. A ideia é automatizar um loop inteiro e tirar o humano o máximo possível dele.

## Diferença entre Loop Agêntico e Cron Job / While

A comparação óbvia é com Cron Job — "isso não é só um loop rodando automático?" A diferença fundamental: num Cron Job ou `while`, um `if` decide se o loop continua. Num loop agêntico, é o próprio modelo que decide se continua ou não — não é um `if` determinístico, é um modelo que interpreta e decide se segue aquele passo. Ele lê um estado (por exemplo, um roadmap) e decide: "tem mais itens no roadmap, devo planejar o próximo item e continuar."

## Loop Fixo vs. Loop Criador

A indústria ainda não tem nomenclatura consolidada para esses tipos de loop. Duas categorias propostas neste vídeo:

### Loop Fixo

Um loop sem side effect — a execução não altera o estado de forma cumulativa entre rodadas. Exemplo dado: um loop multiagêntico de avaliação de frameworks de spec driven ("bench run" — uma skill que orquestra frameworks de spec driven fazendo com que implementem algo e depois avalia o resultado). A skill orquestra três agentes especializados — um `planner`, um `implementer` e um `evaluator` — cada um responsável por uma etapa (plan → implement → evaluate). Ao rodar "rode duas avaliações do framework TLC Spec Driven", a skill sozinha controla o loop completo, rodando os três passos por avaliação, sem intervenção humana entre uma etapa e outra.

Chama-se de "fixo" porque não cria mais código nem estado cumulativo: a segunda execução não fica pior por causa da primeira. Esses loops são normalmente seguros. Uso comum: automações.

### Loop Criador

O tipo mais complexo, com side effects reais: quando o loop gera um roadmap, faz algo a partir dele, gera outro roadmap, e segue reiterando até construir uma aplicação inteira. É extremamente complexo porque acumula side effects — o principal deles é: quando algo é gerado com bug, e depois se gera coisas em cima daquele bug, o bug se perpetua e vira um grande problema no final.

Esse foi o tipo de loop usado na migração do Ban para Rust — e o autor relata ter passado pelos mesmos desafios na sua própria migração/experimento.

## Estudo de Caso: Um Jogo Completo Construído em Loop Criador (Um Final de Semana)

Para testar fluxos de longo prazo com side effects (loop criador), o autor construiu um jogo completo em um final de semana, usando uma engine aberta de um MMO famoso (código open source), aplicando o mesmo padrão usado pelo Ban para migrar para Rust — mas iniciado antes do blog post do Ban ser publicado. O jogo ficou totalmente funcional: teve mobs, e numa aula da comunidade (Techleads Clube) 200 pessoas entraram no jogo simultaneamente. O código completo do jogo será disponibilizado.

### O Roadmap Inicial

Para "loopar" o loop criador, é necessário um roadmap como base, mais passos para o agente saber executar. O autor fez uma primeira exploração e decidiu a fundação do jogo; a partir disso, criou um roadmap com 18 fases (como "épicos"). Cada fase tinha pouco detalhe, só o alto nível — porque, ao construir algo incrementalmente, não é possível planejar todas as fases de antemão sabendo que a fase anterior precisa estar pronta primeiro. O máximo possível é ter a visão do que a fase será; o planejamento detalhado só acontece depois que a fase anterior está implementada. As 18 fases cobriam apenas a fundação do jogo — ainda sem definição de personagens, assets, ou animações.

### Lições Aprendidas, Estado e Handoff

Além do roadmap, componentes fundamentais em loops criadores:

- **`lessons.md`** — gerado pelo próprio framework TLC Spec Driven. Cada vez que o agente passa por algo e aprende (por exemplo, resolve um problema após ficar "loopando" nele), registra a lição ali, para que os próximos agentes/passos não repitam o mesmo problema.
- **State** — registra o que foi feito numa fase, incluindo blockers enfrentados.
- **Handoff (randoff)** — ao terminar grandes fases, o agente deixa registrado o que o próximo agente precisa saber para continuar.

O loop autônomo precisa desse contexto — o que aconteceu e para onde as coisas estão indo, incluindo decisões tomadas — para funcionar bem ao longo do tempo. A única coisa que o TLC Spec Driven não faz é criar o roadmap; isso é responsabilidade da camada acima (o loop engineering, que orquestra vários loops de spec).

### Como o Loop Rodou

O primeiro loop usado foi o loop do Cursor (`/loop`), com o comando "avance no roadmap até que acabe o roadmap" (18 tarefas). Para cada item do roadmap, o agente: gerava uma spec (seguindo TLC Spec Driven), gerava as tasks, implementava, e ao final rodava uma validação (um subagente dedicado a validar se a fase foi cumprida — se falhar, o próprio sistema se corrige até ficar correto). Ao validar uma fase, iniciava automaticamente a fase seguinte: planejar → implementar → revisar. Isso ficou rodando por um final de semana inteiro.

O padrão geral do loop criador, o mesmo usado pelo Ban para mover 500.000 linhas para Rust: pegar uma tarefa → planejar a tarefa → implementar → verificar (no caso do autor, até 3 tentativas) → atualizar o roadmap → pegar o próximo item.

### Por Que uma Referência Sólida Importa

Esses loops funcionam bem quando existe uma referência sólida para validar contra. No caso do autor, havia uma engine em JavaScript muito similar à referência (assim como o Ban já tinha um codebase com (segundo o autor) cerca de 1,3 milhão de asserções de teste) — ou seja, era possível migrar e validar continuamente contra um comportamento de referência.

### O Loop Não Roda Para Sempre

Quem diz que o loop "roda para sempre" está errado — ele roda até esgotar o que há para fazer; a partir daí não sabe mais o que fazer e precisa do humano. O autor fez 18 fases e parou para pesquisar (chegou ao limite do roadmap). Depois de um dia rodando, entrou para decidir como seriam as animações e os personagens, pesquisou, e gerou mais um roadmap de ~10-15 épicos.

Nesse ponto, criou uma **skill de "spec driven execution"** — uma skill que sabe orquestrar o TLC Spec Driven em loop (composição de duas skills: o TLC Spec Driven sabe planejar/implementar/validar, mas não sabe trabalhar em loop; a segunda skill faz essa orquestração). O prompt voltou a ser mínimo: "loopa no [roadmap], usa a spec driven execution, vai até o final."

### Pesquisa Prévia como Redutor de Prompts Durante o Loop

Quando se trabalha com spec driven dentro de um loop longo, é comum precisar dar muitos prompts de esclarecimento ao longo do caminho. Para evitar isso, o autor fez toda a pesquisa sobre personagens/monstros/efeitos antes de começar, e encapsulou o resultado numa **skill "game designer"**, com tudo que é necessário para criar monstros, personagens e efeitos. Assim o loop seguiu sem precisar de intervenção humana — a pesquisa feita antes valeu para todo o roadmap de ~15 itens.

## Harness como Fator Decisivo (Por Que o Ban Migrou para Rust)

O loop criador funciona muito melhor quando existe algo sólido para validar contra. Isso conecta com o motivo da migração do Ban para Rust: Rust é seguro por construção — o próprio compilador não deixa compilar código com problemas de memória. A linguagem anterior usada (Zig, segundo o vídeo) deixa compilar e só quebra em produção.

Não existe harness/sensor melhor do que isso: a IA não precisa "interpretar" se algo é memory-safe — ela roda o compilador, e se quebrar, tem um problema objetivo para resolver. A própria linguagem funciona como harness: tipagem é harness, arquitetura é harness, compilador é harness. Guidelines (skills, specs) + sensores (testes, lint, compilador) formam o harness completo — quanto melhor o harness, melhor o loop.

### Onde o Autor Quase Estragou Tudo

O autor usava testes end-to-end com Playwright, mas o processo começou a ficar lento porque os testes eram "guardados" (persistidos/reexecutados continuamente). A solução tomada foi remover os testes e2e e usar só testes de integração e unidade — só que um jogo tem muitas variáveis, e sem teste de ponta a ponta os erros começaram a se acumular sem serem pegos.

A correção: trazer de volta os testes e2e, mas sem deixá-los salvos/acumulados — para entregar uma fase, o agente precisava iniciar um Playwright, jogar de fato, e provar que a fase estava funcionando ponta a ponta. Isso parou o acúmulo de erros. Lição: quem for fazer loops precisa de uma boa suíte de testes e uma boa forma de garantir que erros não se perpetuem entre iterações do loop.

## Os Limites do Loop Engineering

Loop Engineering não resolve uma suíte de testes fraca. E não resolve a intenção — ou seja, o loop não cria novos roadmaps sozinho; esse é o momento em que o humano precisa entrar. No caso do jogo: 18 fases da fundação → o autor entrou para decidir sobre personagens, criou skills de apoio, deixou loopar de novo (mais ~10-15 fases, chegando a pouco mais de 20) → o autor entrou de novo para a parte final (polimento, multiplayer). Ao todo, cerca de 30 fases (30 "loops" de spec driven) foram necessárias; em vez de o autor dar prompt fase a fase, ele deu três grandes "loops de loop engineering" que cobriram tudo isso, rodando sozinho por um final de semana.

### Custo do Harness

Construir toda essa estrutura de harness (skills, specs, sensores) tem um custo. Na maioria dos casos de software enterprise com features normais, esse nível de investimento em loop não é necessário — ele compensa em migrações, automações, e cenários onde saber usar loop fixo e loop criador realmente ajuda.

## As Quatro Perguntas Para Decidir se Vale Usar um Loop

1. **Existe um bom harness?** — a ponto de praticamente não revisar mais pull requests. Se todo PR precisa de correções, o harness ainda não está bom, e cada loop vai perpetuar erros, criando um problema grande. Recomendação: usar spec driven (com humano mais presente) até o harness ficar bom.
2. **O feedback é rápido?** — testes rodam rápido? Se for lento, o loop gasta muito token e fica muito demorado.
3. **Existe uma stop condition confiável?** — algo que sinaliza "tem que parar e chamar o humano".
4. **Há backlog suficiente** para valer a pena deixar loopando, comparado a simplesmente planejar e fazer manualmente?

## Encerramento

O autor disponibiliza o código do jogo (baseado em uma engine derivada de MMO conhecido, sem citar o nome completo por direitos autorais — todo o código usado é livre/open source), incluindo as specs e as skills criadas (spec driven execution, game designer, etc.), como base para outros projetos futuros do canal.
