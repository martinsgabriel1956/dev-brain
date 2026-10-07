# Decisões de arquitetura: contexto, "depende" e trade-offs (Bernardo Lobato)

> **Fonte:** transcrição de vídeo colada pelo usuário (fala corrida, sem pontuação). Já estava em português, então não foi traduzida.
> **Autor:** Bernardo Lobato (apresenta-se no vídeo; canal Dev, "olá devon" no ASR = "olá, dev").
> **Limpeza:** pontuação e parágrafos restaurados; erros de ASR corrigidos ("jagger" → Jaeger, "prometeus" → Prometheus, "dyrace" → Dynatrace, "cash" → cache, "event drive" → event-driven, "retrais" → retries, "design system" no contexto de estilos arquiteturais lido como *system design*, "infraisponível" → "a infra disponível", "expl explain analyze" → `EXPLAIN` / `ANALYZE`). Nada foi omitido; o vídeo não tem propaganda no trecho colado. O final está truncado: a última frase termina em "escolha quais" (provavelmente "escolha quais problemas você quer ter").

---

## Abertura — o cenário

Digamos que você tenha um sistema monolítico rodando em produção, recebendo por volta de 20.000 acessos por dia. A performance começa a degradar e, ao mesmo tempo, o código fica cada vez mais difícil de manter pelo time. O que você faz?

No vídeo, o objetivo é entender como funciona um processo de decisão como esse, e como a mesma decisão pode resolver alguns problemas do sistema e criar outros que o time talvez ainda não esteja preparado para administrar. A provocação: "já convenceu seu chefe de que o certo é recomeçar tudo do zero?"

O autor quer falar abertamente sobre o processo de tomada de decisões que se refletem na arquitetura, conforme se acompanha a evolução do produto. Toda decisão técnica relevante pode resolver um problema importante e, ao mesmo tempo, criar novos que, se não administrados, podem piorar a situação original.

## A ilusão da solução única

Ao começar um projeto (do zero, ou aproveitando estrutura de outro projeto ou boilerplate), costuma-se pensar em arquitetura como a busca de uma estrutura que permita o sistema crescer, ser mantido e atender os requisitos do momento. Isso faz sentido: o objetivo de uma boa arquitetura é reduzir problemas, facilitar mudanças e tornar decisões futuras mais simples.

O que o autor vê com frequência, tanto em fases iniciais de projetos reais quanto em materiais de estudo, é a tentativa de achar **uma solução arquitetural que elimine todos os problemas relevantes de uma vez**. Exemplo irônico: "quem nunca estudou arquitetura limpa achando que ia resolver todos os seus problemas, sem saber nem o que é arquitetura limpa e nem como o sistema vai se adaptar a ela?"

Quem já trabalhou com sistemas em sustentação, ou acompanhou o ciclo de vida de um produto, sabe que na prática, conforme o sistema cresce, os desafios que acompanham cada decisão também crescem e precisam ser considerados sempre.

## O exemplo: frontend → API → banco

Arquitetura inicial: um frontend chama uma API que conecta no banco de dados. O projeto cresce: 20.000 acessos diários, usuários reclamando de lentidão, o time demorando cada vez mais para entregar uma tarefa, testes cada vez mais demorados.

Alguém que estuda e quer evoluir o repertório técnico sugere: "vamos quebrar o sistema e transformar em microsserviços". O autor pergunta ao espectador se a troca faz sentido ("sem julgamentos, pode responder de coração") e responde: **"infelizmente, não dá para saber".**

Existe justificativa plausível: reduzir certos tipos de acoplamento, separar responsabilidades, permitir que partes evoluam de forma independente, escalar componentes separadamente. Mas isso ainda é insuficiente para dizer se é uma boa decisão. Falta uma informação importante: "peço licença para usar a palavrinha da moda — **falta contexto**".

## Descobrindo de onde vem o problema

20.000 acessos por dia pode parecer bastante, mas o número sozinho não diz quase nada. É preciso saber como os acessos estão distribuídos, quais operações são realizadas, qual o tempo de resposta, onde está o gargalo. Hipóteses:

1. **Consulta pesada no banco.** O problema pode ser resolvido com um **índice**, uma mudança na consulta, ou na forma como os dados são acessados ou estruturados. Quebrar a aplicação em 10 serviços não traria nenhum ganho para esse gargalo e, "de brinde", aumentaria muito a complexidade.
2. **Processamento pesado de forma síncrona durante a requisição**, aumentando o tempo de resposta. Talvez uma **fila ou processamento assíncrono** já resolva essa parte.
3. **Acoplamento.** Os problemas de performance e de manutenção podem estar no acoplamento: uma aplicação relativamente simples exige mudanças em vários componentes porque módulos conhecem detalhes demais uns dos outros. Aí existe um problema de **fronteiras e responsabilidades** que precisa ser tratado, e a parte arquitetural faz mais sentido.
4. **Uma parte específica do sistema recebe carga muito maior que as outras.** Nesse cenário pode fazer sentido isolar aquele componente (talvez como serviço externo) para evoluir ou escalar de forma independente.

Antes de decidir quebrar a aplicação em uma arquitetura distribuída, é preciso descobrir onde está o problema.

## Ferramentas de investigação

- **Comportamento das requisições:** OpenTelemetry, Jaeger, Zipkin; ou ferramentas de APM como Datadog, New Relic, Dynatrace.
- **Gargalo de infraestrutura:** métricas de CPU, memória, disco e rede, com Prometheus e Grafana, ou a ferramenta do provedor de nuvem.
- **Suspeita no banco:** analisar as consultas com `EXPLAIN`, `ANALYZE` etc.

A ideia **não** é usar todas as ferramentas "a torto e a direito" ao mesmo tempo, e sim identificar se o problema está na aplicação, no banco, na infraestrutura, ou numa operação executada de forma ineficiente. Entender esse contexto é importante para a solução e principalmente para o produto, porque **uma boa arquitetura começa quando se tenta entender qual problema se está tentando resolver**.

Antes de causar mudanças estruturais no projeto inteiro, o autor quer entender: o problema, as restrições, o produto, o sistema e, principalmente, o time.

## Não existe arquitetura perfeita — o mito da padronização

O profissional responsável pelo desenho deve ter maturidade para entender: **não existe arquitetura perfeita para todos os problemas; existe uma arquitetura mais ou menos adequada para determinado contexto.**

Daí vem o **mito da padronização de arquitetura**. Em qualquer discussão mais rasa sobre estilos arquiteturais ou system design aparecem afirmações como: "monolito é melhor", "microsserviço é melhor", "event-driven é melhor", "clean architecture é melhor", "arquitetura em camadas é melhor". Tratar como regra universal uma decisão que depende de tanta coisa é, no mínimo, perigoso.

- Uma aplicação pequena, com equipe pequena e poucos requisitos de escala, tem problemas completamente diferentes de uma plataforma distribuída que opera em várias regiões, processa milhões de operações e é desenvolvida por várias equipes independentes.
- Mesmo sistemas com características parecidas têm outras restrições que mudam a decisão: uma empresa aceita certa complexidade operacional porque tem equipes especializadas, infraestrutura adequada e experiência; outra olha a mesma arquitetura e conclui que o custo de manter não compensa.
- **Tudo muda ao longo do tempo:** uma decisão que fazia sentido 3 anos atrás pode deixar de fazer depois que o produto cresceu, a equipe mudou ou os requisitos de negócio foram alterados.

## "Depende" é o começo da investigação

Dizer "depende" não é fugir da decisão; **é o começo da investigação.** A decisão depende de:

- o problema que se tenta resolver;
- o tamanho e as características do sistema;
- o produto;
- a infraestrutura disponível;
- o nível de experiência do time;
- o custo que se está disposto a assumir;
- e, principalmente, **as consequências que se está preparado para administrar.**

Porque ao escolher uma arquitetura, também se escolhe **um conjunto de problemas e complexidades atrelados àquela decisão**, que passam a fazer parte da realidade do time no dia a dia.

## Trade-off

"Se você quiser parecer um pouquinho mais refinado e não quer dizer 'depende' para tudo, usa a palavra da moda: **trade-off**." Quando se toma uma decisão arquitetural, prioriza-se algumas características do sistema e aceita-se determinadas consequências em troca. "Essa é literalmente a tese do vídeo."

No exemplo, ao introduzir uma arquitetura mais distribuída, pode-se ganhar independência entre componentes, possibilidade de escalar partes específicas e maior autonomia para evolução. Em troca, passa-se a lidar com:

- comunicação de rede e latência;
- observabilidade distribuída;
- consistência entre serviços;
- timeouts e retries;
- transações distribuídas;
- "toda uma classe de problemas que simplesmente não existia quando tudo estava dentro do mesmo processo".

O mesmo raciocínio vale para praticamente toda decisão relevante:

- uma **abstração** no código pode facilitar a evolução de um comportamento, mas aumenta a complexidade do código;
- um **cache** pode reduzir latência, mas introduzir problemas de consistência;
- o **processamento assíncrono** pode melhorar o tempo de resposta, mas torna o fluxo geral muito mais difícil de acompanhar;
- uma arquitetura **altamente preparada para escala** suporta carga muito maior, mas exige mais infraestrutura e mais conhecimento para ser operada.

Falar em trade-off é falar de **qual característica se tenta melhorar e quais consequências se aceita pagar**. Por isso uma decisão arquitetural jamais deve ser avaliada somente pelo problema que resolve: "aqui o buraco é mais embaixo". Cada decisão precisa ser avaliada também pelos problemas e complexidades que coloca no sistema e no dia a dia.

## Voltando à pergunta do começo

Depois de entender o problema, olhar o contexto e avaliar as consequências, talvez a resposta seja separar parte do sistema numa arquitetura distribuída; talvez seja introduzir uma fila, um cache, melhorar o banco ou reorganizar alguns módulos; talvez, dependendo do contexto, seja realmente migrar para microsserviços. O ponto é que agora a decisão **não** é tomada porque "arquiteturas distribuídas são melhores", e sim porque se entendeu qual problema se quer resolver e quais consequências se está disposto a assumir.

## Fecho

"Isso pode ser chocante para você, mas **todo projeto vai ter problema. A diferença está nos problemas que você escolhe ter.**" Essa é uma das partes mais importantes e gratificantes do trabalho de arquitetura de software ou system design: entender que cada decisão coloca novas responsabilidades dentro do sistema e do time, e que elas precisam ser compatíveis com o produto, o contexto e a capacidade do time.

E se há uma pergunta em TI ou arquitetura de sistemas cuja resposta nunca é "depende", é esta: **"meu projeto vai dar problema?" — Vai. Escolha quais.**
