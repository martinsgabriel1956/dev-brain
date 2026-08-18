# LeetCode e System Design valem mais para parecer bom dev do que para ser um bom dev? — reação a tweet do Bero

> Fonte: transcrição de vídeo do YouTube (reação/discussão), falante não identificado no texto original. Transcrito e formatado a partir de fala corrida, sem cortes de conteúdo. Patrocínio (HostGator) preservado apenas como contexto, não é parte da tese do vídeo.

## Contexto / gancho

Reação a uma afirmação (atribuída a "Bero", citando também "Twitch"): agora que todo mundo usa IA para escrever código, vale mais a pena investir tempo para **parecer** um bom programador do que para **de fato ser** um bom programador — na prática, treinar LeetCode e System Design, que "passa em qualquer entrevista", e depois usar Kimi/GPT/Claude Code no trabalho.

## Transcrição (formatada)

Agora que todo mundo usa IA para escrever código, vale muito mais a pena você investir seu tempo para parecer que você é um programador bom do que para você de fato ser um programador bom. Eu diria 100% LeetCode, System Design passaria em qualquer entrevista, depois tacaria Kimi, GPT e Claude Code.

Vamos falar dessa "atrocidade" — em parte eu concordo. Hoje o tema é esse, tem bastante coisa pra gente abordar aqui. São os meus temas, eu pautei o canal em cima disso, e agora que eu cavei essa cova a gente vai ter que pular nela.

### Se vender vs. ser bom

Eu acho que, como comentado, tudo na vida é sobre a pessoa saber se vender. Partindo desse pressuposto: a ideia de se vender, de publicar o seu trabalho, de mostrar o que você faz, é algo que eu sempre valorizei e incentivei os devs a fazerem, porque a gente é muito ruim nisso — de nada adianta ser muito bom se você não consegue demonstrar que é bom.

Não dá para culpar só as empresas ou o RH (embora em parte dê). O RH contrata mal, sim, e eu tenho uma iniciativa nesse sentido para tentar ajudar o brasileiro a se vender bem e a acessar os empregos que ele tem capacidade técnica de acessar. Mas de nada adianta conseguir o emprego se você não conseguir se comunicar bem dentro dele. A habilidade de comunicação é cada vez mais crucial.

### Como o trabalho de dev mudou (da cascata ao multidisciplinar)

Antes, o trabalho de dev era mais parecido com waterfall: cliente/stakeholders → demanda → equipe de produto mastiga a demanda → vira tasks/features para devs, geralmente distribuídas entre um front-end, um back-end e um DevOps segregados.

Hoje, tenho visto uma concentração em menos cargos: contratações de front-end reduzidas, cargos mesclados em full stack. Ops e segurança parecem ter se mantido do mesmo tamanho (segurança talvez até crescido), mas front migrou para full stack. A maioria das empresas que vejo contratando busca full stack focado em back-end, full stack focado em front-end, ou só full stack.

A velocidade de iteração aumentou: geramos código mais rápido, prototipamos mais rápido, obtemos feedback mais rápido — a cascata está se perdendo. (Contra-argumento razoável: "o código tá vindo bugado, alguém vai ter que consertar no futuro" — concordo que é um ponto válido, mas a percepção individual não importa tanto quanto o que as empresas estão realmente fazendo agora; elas podem se arrepender depois, mas a realidade atual é essa.)

Isso tem levado a times mais multidisciplinares: já vi pessoas de produto abrindo PRs (o dev revisa e formata, sem problema), funções se mesclando. Tenho incentivado devs a entender um pouco dessa migração: como se faz um bom produto, como se coleta feedback, como se comunica com o cliente — sem garantia de que isso vai se concretizar, mas é a tentativa atual das empresas, principalmente pequenas e startups, no sentido de um "dev produteiro"/misto full-stack + produto.

### Por que CRUD "acabou" e a régua subiu

Startups têm ganhado força com IA porque ela reduz boa parte do trabalho que antes consumia muito tempo — CRUD era caro no sentido de demorado. Hoje, para mim, CRUD simples está 100% resolvido. A régua subiu: sobram para os devs os trabalhos mais complexos.

Mesmo que alguém seja muito bom de produto, pode não conseguir implementar uma codebase complexa; e se conseguir implementar, pode não entender as nuances necessárias para fazer algo escalável, seguro e resiliente. Às vezes a pessoa não tem noção de que uma escolha agora implica abrir mão de algo no futuro — ex.: escolher login com senha hoje versus migrar para login com Google/GitHub depois altera decisões de produto; desenhar o banco de dados de determinada forma vai requerer migração trabalhosa no futuro.

Ainda existe espaço para dev nesse cenário: empresas continuam contratando sênior, principalmente sênior "letrado em IA" — esse letramento em IA surge como pré-requisito. Pessoas de produto em geral não têm a fluência que devs têm em lidar com harness, com Claude Code, em setar pipeline de CI/CD, em setar testes. O controle de qualidade da pessoa de produto tende a ser "a feature funciona na minha máquina", não "eu olhei o código".

### Onde o argumento do Bero está certo

Dado tudo isso, o argumento do Bero presume que você já tem essa capacidade — e se você é um dev profissional na fronteira, lidando com esses modelos no dia a dia, em parte você já tem. Se sabíamos validar código antes, sabemos validar hoje.

O argumento de que LeetCode e System Design importam para passar em entrevista e entrar em uma empresa (principalmente Big Tech, que são as que mais contratam nesse modelo) — nisso, concordo que está certo. Por quê:

- Em 2019, um bom GitHub era forte evidência de que a pessoa era um bom dev. Hoje isso prova muito menos: um SaaS funcional com 100 usuários não exige mais tanta competência técnica para ser construído, e um recrutador não consegue avaliar as nuances reais do sistema.
- Mesmo assim, projetos e GitHub ainda diferenciam quem entende o jogo — quem não entende nada talvez nem saiba que isso vale a pena mostrar. Mas a forma que as empresas ainda usam para diferenciar tecnicamente continua sendo LeetCode e System Design.
- A maior parte das vagas em empresas como o Google é híbrida ou presencial, e a maior parte das entrevistas presenciais — você não consegue "colar" (usar IA) nelas.
- Algumas empresas estão adaptando o formato de entrevista para incluir IA: teste técnico onde você e a IA constroem algo juntos. Alguns subgrupos do Google (que na prática funciona como várias "microempresas" dentro de uma — Google Maps, YouTube, etc.) já aplicaram esse tipo de teste, e várias startups também.

### LeetCode caiu, System Design subiu

O conhecimento de "coisas mais baixo nível" ficou, na minha visão, menos relevante para o trabalho e para entrevistas. LeetCode é fácil de aprender — em ~20h dá para aprender o suficiente para passar em entrevista de LeetCode easy/medium (a maioria cobra isso, não difícil).

Utilidade prática para o trabalho: LeetCode caiu, System Design subiu — o inverso do que eu falava há dois anos no canal. Isso reflete tanto a tentativa de manter o canal relevante quanto minha experiência real como dev profissional: no dia a dia, System Design tem se tornado mais valioso, LeetCode menos valioso, e conhecimento de IA muito mais valioso (por isso trazemos mais conteúdo de IA no canal).

### "Se a IA é melhor que qualquer dev, por que não substituiu os devs?"

Narrativa comum: com modelos de fronteira (ex. Fable/Claude 5) seria possível fazer software extremamente impressionante, melhor que qualquer dev. Se isso for verdade, uma empresa deveria conseguir rodar 5-10 agentes em paralelo e produzir SaaS melhores que os de qualquer dev — e uma big tech deveria conseguir se manter com poucos devs. Isso eu não vi acontecer.

Teste de sanidade: "se a IA é tão boa, manda ela fazer um competidor do Figma em um mês." Ninguém fez isso ainda, e ganharia muito dinheiro se conseguisse. Não estou convencido de que isso é suficiente — construir software é inerentemente iterativo, cada iteração demanda atenção e cuidado que a IA ainda não replica sozinha, e os requisitos mudam ao longo do processo.

### O domínio de IA está aqui para ficar (e vai ficar barato)

Independente de certo/errado, o domínio dessas ferramentas está no mercado e não vai embora. Segundo a Artificial Analysis, os modelos de fronteira ficam cada vez mais inteligentes, mas também cada vez mais caros — porém a maioria das tarefas não precisa de modelo de fronteira. Modelos abertos e mais baratos (Kimi K2/K3, DeepSeek, Claude Sonnet, GLM) já resolvem muita coisa mais simples.

Não acho que vamos chegar num ponto em que essas IAs fiquem caras demais para todo mundo — vamos ficar melhores em rotear tarefas difíceis para modelos bons e tarefas simples para modelos mais fracos/baratos. Esse conhecimento (de IA) está aqui para sempre.

### O risco de estagnar no nível da IA

Ainda assim, como alguém sênior com bastante experiência, corro o risco de subestimar o quão difícil é o trabalho mesmo com modelos de fronteira. Há muito conhecimento adquirido ao longo do tempo — completude dos sistemas, como eles se comunicam, como as empresas fazem as coisas — que permite fazer as coisas funcionarem de forma intuitiva.

Exemplo prático: na última empresa em que trabalhei, devs júnior tinham acesso a todos os modelos e podiam fazer qualquer coisa com IA — e mesmo assim cometiam erros típicos de júnior que, com experiência, era possível enxergar como não sendo a melhor forma de resolver o problema.

Conclusão parcial: para entrar numa empresa, dominar harness/Claude Code/System Design ajuda a "botar o pé na porta". A preocupação maior é: uma vez dentro, como você evolui? Ter construído uma boa carreira antes da IA ensina como as coisas funcionam — e quem não entende como as coisas funcionam tende a estagnar num limite máximo igual ao limite máximo da própria IA. Nesse ponto, nativamente, a empresa contrata a IA em vez de você, porque sua capacidade é a mesma.

### O que continua sendo diferencial (mesmo com IA dando velocidade)

A IA dá muita velocidade, mas você ainda precisa entender do funcionamento — esse é hoje o seu diferencial frente à pessoa de produto: entender onde ela erraria usando só a IA e onde você acerta. Isso se traduz em:

- Conhecimento de **System Design**.
- Saber lidar com banco de dados.
- Saber transformar um pedido nebuloso de cliente em requisitos cristalinos, validar input/output, validar se a linguagem do cliente foi bem traduzida para a IA e se o resultado da IA é o que o cliente queria — o que volta para comunicação, leitura e escrita.
- **CI/CD** com pipelines que fazem sentido, incluindo testes que de fato cobrem os casos de uso reais.
- Medir: complexidade ciclomática, cycle time, **observabilidade** (avaliar um log de erro, identificar rápido que um bug foi gerado, voltar no PR que gerou o bug e corrigi-lo).
- Uso de **feature flags** para testar features novas em subconjunto de clientes, identificar comportamento estranho, desligar a flag, corrigir e subir de novo.
- Lidar com **contexto** — hoje muito centrado em documentação e specs de qualidade.
- Capacidade interdisciplinar: entender o produto, a necessidade do cliente, o que gera dinheiro para a empresa, de onde vem o dinheiro, quem é o cliente, quanto custa cada solução/cloud, estimativas de custo e velocidade — decisões que ainda recaem sobre o dev.

Empresas não confiam 100% no output de IA. Credenciais ainda valem: faculdade, currículo bom, contratação ainda muda de forma mais ou menos rápida. O que se mantém constante e valioso é: como você demonstra que entrega software confiável, robusto, com alta confiabilidade — o que diferencia isso de simplesmente gerar um MVP num "Lovable" qualquer.

### Concordando com o ponto central do Bero, mas com ressalva

O ponto do Bero de que todo dev precisa aprender a se vender melhor é válido — a gente se vende mal, é um povo técnico que gosta de ficar na caverna desenhando soluções. Mas isso não basta mais: mostrar "olha essa contribuição, um PR pro Node.js" é valioso só em algumas empresas — a maioria não está desenvolvendo o Node.js, está fazendo CRUD simples.

Nesse mundo novo, boa parte da diferenciação é conseguir fomentar um ambiente onde a única possibilidade é código robusto, observável e confiável:

- Codebase onde um bug introduzido quebra um teste → mais confiável.
- Codebase com testes → mais confiável.
- Codebase bem documentada → mais confiável.
- Codebase com feature flags e recuperação rápida → mais confiável.
- Codebase mensurável (com boas métricas escolhidas) → mais confiável.

Por isso vale a pena aprender System Design.

### O que perdeu valor

- "Escovar bit" (nuances de baixo nível de linguagem — ex. `==` vs `===` em JavaScript, `NaN`, etc.): ainda vale saber que existe, mas testes hoje são tão baratos que, cobrindo bem os casos com testes (inclusive testes de mutação), um bom dev consegue trabalhar numa codebase de linguagem com pouca familiaridade (nenhuma familiaridade ainda é difícil; pouca é possível, não ideal, mas possível).

### "Admirável mundo novo" — fechamento

Não é o caso de dizer que tudo que aprendemos até aqui continuará sendo exatamente o que vamos precisar saber. Quem entrou na área sempre ouviu que é uma área de estudar pelo resto da vida — isso está sendo posto à prova agora: o mercado mudou, precisamos nos adaptar, e tudo que você aprendeu até hoje te dá segurança e permite avançar mais rápido.

Pergunta-teste: pergunte ao melhor dev que você conhece o que ele está fazendo com IA hoje — a resposta tende a mostrar que entender como as coisas funcionam, todo o básico construído ao longo dos anos, colocou essa pessoa em destaque na carreira.

Analogia: um engenheiro no dia a dia usa calculadora e AutoCAD; você, no seu dia a dia, vai usar pelo menos por ora um Claude Code ou similar. Isso não desmerece o conhecimento de base — é uma ferramenta em cima dele.

Outra analogia: pense na IA como um trator gigante. Antes você colhia maçã na mão ou arava a terra com enxada/arado; hoje ara com trator — mas ainda estuda um pouco do trator. Pode ser que o mercado piore e fique mais difícil conseguir emprego — isso é possível — mas diferente de um trator, você não precisa de "terra" (recursos caros) para manusear IA: só um PC, e já dá para ter um output absurdo com modelos baratos (~R$20/mês). No futuro, bons modelos locais vão rodar no seu próprio PC (hoje ainda não são tão bons, mas vão chegar).

Quem tem uma pegada multidisciplinar e empreendedora deve se sair bem. Quem só gosta de "escovar bit" — sinceramente, o cenário está um pouco pior para essa pessoa, que vai precisar se adaptar mais. Isso vindo de alguém que adora escovar bit e já fez vídeo comparando velocidade de `else` contra `switch/case`, benchmark de otimização em C.

A área sempre mudou e vai continuar mudando — e se isso desincentiva, bem, é a vida: toda área requer atualização com o tempo, a nossa requer mais. Quem quiser parar de aprender deveria considerar saliente sair da área de software — você não pode querer parar de aprender.

## Nota do transcritor

O texto original inclui um trecho de patrocínio (HostGator — hospedagem, VPS, e um produto "AllStack"/passe de assinaturas de IA) no meio da fala. Esse trecho foi preservado apenas como contexto de que o vídeo é monetizado por patrocínio; não faz parte da tese técnica e não foi incorporado à síntese acima.
