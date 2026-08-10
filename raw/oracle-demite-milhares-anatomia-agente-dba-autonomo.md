# Oracle Demitiu Milhares de Pessoas com um E-mail Automático — E Como Construir o Agente que Fez Isso

> Transcrição de vídeo (abertura de nova temporada do canal) sobre o layoff em massa da Oracle, o agente autônomo de DBA que supostamente motivou parte das demissões, e um blueprint prático de como construir esse tipo de agente — usado como argumento para o que responder em entrevistas de emprego quando perguntarem "você usa IA?".

---

## O layoff da Oracle

A Oracle demitiu entre 20.000 e 30.000 trabalhadores às 6 da manhã, via e-mail automático: "Seu cargo foi eliminado, obrigado pelos anos de serviço." Na prática, boa parte das pessoas nem chegou a ler o e-mail — quando uma empresa desse porte demite alguém, o acesso já é cortado antes, e é assim que a pessoa percebe que foi demitida: não consegue mais logar.

Contexto da empresa: Oracle tem market cap de ~400 bilhões de dólares, crescimento de 22% no trimestre, e Larry Ellison é o terceiro homem mais rico do planeta.

O motivo alegado (ou vazado) é que agentes de IA estão substituindo trabalho de DBA (database administrator). Mas vale questionar a causalidade direta: a Oracle tinha ~20.000 DBAs, então é mais provável que só uma fração desses cargos tenha sido afetada por automação — o resto do layoff tem outras causas de negócio. A teoria de que o dinheiro economizado com mão de obra vai direto para os data centers do projeto Stargate é especulação da internet, não fato confirmado (o próprio autor do vídeo tem dúvidas se o Stargate vai sair do papel).

**Conclusão sobre layoffs em geral**: é preciso olhar essas notícias com cautela, sem cair na narrativa de "a IA já está destruindo a profissão X". O que está acontecendo é mais sutil: a IA modifica a forma como as pessoas trabalham, pode modificar cargos, e algumas pessoas vão precisar migrar de função mantendo parte das habilidades que já tinham.

## Toda tarefa de alto risco ainda precisa de aprovação humana

Ensinamento do professor Fran Figueiroa, citado de uma palestra no encontro presencial do Stupid Button Club: toda tarefa que tem risco real de dar errado — a "criticidade" da tarefa — ainda vai precisar de um humano aprovando, mesmo com IA no loop. Quantos humanos por tarefa, isso ainda não está definido, mas a tendência é que tarefas de alto risco continuem exigindo esse checkpoint.

## O erro comum: só escrever código com IA, sem criar agentes

Muita gente pergunta "qual agente/ferramenta você usa para codar" — mas o problema não é a ferramenta, é o uso: a maioria está apenas escrevendo código com assistência de IA, sem criar os próprios agentes, sem agregar valor construindo automação para a empresa.

### O que responder em entrevista quando perguntarem "você usa IA?"

Em 2026 essa pergunta é óbvia demais — todo mundo já usa IA para codar, então respostas como "uso Claude Code" ou "uso Copilot" já não diferenciam ninguém. A pior resposta possível é algo como "eu uso o ChatGPT, mas ainda não confio muito, então só pergunto, vejo se faz sentido e daí implemento algo parecido" — isso soa como alguém que nem está de fato integrando IA no trabalho.

A resposta que diferencia é mostrar que você **criou algo com IA** — não um side project bonito com dashboard de gestão de clientes, mas uma automação real que resolveu um problema de fluxo de trabalho da empresa.

### Exemplo prático: o "Let me cloud for you"

Analogia com o antigo "Let Me Google That For You" — só que agora é PMs e stakeholders (pessoas de produto, projeto, ou qualquer área sem acesso ao código-fonte) fazendo perguntas técnicas ("como está implementada aquela funcionalidade", "como andam as feature flags", "o que dizem os analytics") e o time repassando manualmente para o Claude/GPT/agente e devolvendo a resposta.

A automação óbvia: criar um **bot no Slack/Teams** com acesso ao repositório, que qualquer stakeholder pode mencionar diretamente para tirar essas dúvidas — eliminando o trabalho manual do time de fazer de intermediário.

### A melhor documentação ainda é o código

Um dos motivos que torna esse bot viável sem manutenção paralela de documentação: a melhor documentação continua sendo o próprio código. Gerar documentação (via prompts, instruções, skills, agentes) é fácil, mas mantê-la atualizada é o problema histórico — e ela fica defasada de qualquer forma.

Agentes como Claude Code, Codex ou Open Code — que rodam com acesso ao terminal — conseguem usar ferramentas de busca de arquivo para, a partir de uma pergunta de produto, determinar em qual módulo do projeto a resposta está, buscar arquivos com palavras-chave relevantes e encontrar a implementação real. Isso é ainda mais viável com modelos de janela de contexto grande (na casa de 1 milhão de tokens). Em monorepos grandes, uma prática que ajuda o agente a navegar é ter um `.md` por módulo, funcionando como mapa — não como documentação exaustiva a ser mantida manualmente.

## O layoff da Oracle como estudo de caso: agente de DBA

Vazou que a Oracle estaria pilotando agentes de IA para administração de banco de dados há pelo menos 8 meses — ou seja, a própria empresa que inventou o conceito de DBA estava automatizando essa função. A pergunta interessante não é "a IA substituiu o DBA", é: **quem construiu esse agente provavelmente não foi a pessoa demitida.**

Automatizar esse tipo de tarefa não é mágica — é um padrão de engenharia replicável, muitas vezes implementável em poucas dezenas de linhas de orquestração.

### Anatomia do agente (usando DBA como exemplo)

1. **LLM Planner** — o cérebro do agente, com um *system prompt* que contém o **playbook** (no caso do DBA, um "playbook de DBA": o conhecimento operacional e as regras de decisão daquele domínio).
2. **Tool call loop** — o planner precisa de acesso a ferramentas do domínio. Para um DBA, isso inclui coisas como `psql`, backup, CloudWatch, Slack.
3. **Módulo de observação** — o resultado de cada ferramenta (ex.: resultado de uma query) vira contexto para a próxima decisão.
4. **Camada de decisão (LLM decision)** — a LLM decide entre: tentar de novo, pedir ajuda a um humano, ou pedir confirmação de uma ação antes de executá-la.
5. **Write back** — a camada de saída do agente: gerar log, criar ticket, disparar notificações.

Essa estrutura de cinco peças descreve, segundo o autor, cerca de 90% dos agentes que devem surgir ao longo do ano.

### Os quatro componentes essenciais de um agente autônomo em produção

1. **Trigger (gatilho)** — a LLM não decide sozinha o que fazer; ela é acionada por um evento. Pode ser um cron job, um alerta de observabilidade (Datadog, Sentry/Centry, Crashlytics) via webhook, etc. Exemplo dado: durante um rollout canário (ex.: 5% dos usuários), se surge um novo tipo de erro no Sentry cuja primeira ocorrência coincide com essa release, isso pode disparar automaticamente a criação de um ticket no Jira e o spawn de um agente que faz `git blame`, investiga o código e já abre um PR de rascunho corrigindo o bug.
2. **Whitelist de ferramentas** — lista explícita de funções que o agente pode chamar (ex.: rodar uma query, checar stats de uma tabela, fazer rotate de connection pool). Operações destrutivas — como `DROP TABLE` — nunca entram nessa lista. É essencialmente o princípio do menor privilégio aplicado a um agente.
3. **Loop de observação** — o ciclo de decisão que gera o output, equivalente aos itens 3–4 da anatomia acima.
4. **Escape hatch** — sempre existe um caminho de volta para o humano. Na prática, implementado como um prompt de auto-avaliação de confiança: os modelos atuais (GPT-4o, os novos Codex, etc.) conseguem estimar a própria confiança na resposta que estão dando. Se a confiança está abaixo de um limiar definido (ex.: 70%), o agente pausa e chama um humano em vez de agir. Esse padrão não foi inventado pela Oracle — é replicável em qualquer domínio.

### Outro exemplo: agente de "halt de release"

Fluxo manual comum em empresas com apps de dezenas de milhões de usuários: fazer rollout gradual (ex.: 5% → 20% → 100%), monitorar taxa de erro, e pausar/reverter o rollout se o erro passar de um limiar combinado pelo time. Esse processo é candidato natural a virar um agente que monitora os erros, decide sozinho quando pausar o rollout e notifica o time no Slack/Teams — liberando a pessoa que fazia esse monitoramento manualmente para outro trabalho que gere valor.

## O paradoxo da automatização e emprego

Automação de fato reduz a quantidade de pessoas necessárias para uma tarefa específica — nesse sentido, "rouba" empregos. Mas a decisão de demitir depende do que a empresa faz com a capacidade liberada:

- Se uma empresa tem um programador fazendo o trabalho de três (com ajuda de IA) e demite os outros dois para "ficar só com o que produz por três", ela está otimizando para custo.
- Se uma empresa concorrente mantém os três programadores e cada um agora produz o equivalente a três, o time inteiro produz por nove — gera muito mais valor para o cliente que a primeira empresa.

A pergunta prática não é "a IA vai automatizar meu cargo", é: **dado que a IA libera tempo, o que a empresa (ou eu) consegue fazer com esse tempo que gere valor adicional?** Empresas que não conseguem canalizar esse tempo livre para gerar mais valor tendem a demitir; empresas (e profissionais) que conseguem, tendem a crescer. É uma decisão de mercado e de concorrência, não uma fatalidade técnica.

---

*Nota: o áudio original menciona "Stupid Button Club" (comunidade do autor) de forma abreviada/pouco clara na transcrição original ("stupp button club da tatuê"); mantido conforme a grafia usada em outras transcrições já ingeridas no wiki.*
