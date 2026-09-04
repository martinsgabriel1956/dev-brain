# Agent Waves + Modelos Fortes e Fracos: Otimizando Custo de API de IA

Se você utiliza algum modelo de IA que é cobrado via API e não está utilizando essa técnica de otimização de modelos, você provavelmente está deixando dinheiro na mesa. Então, sem mais enrolações, vamos ao vídeo.

A técnica discutida aqui é bem simples, mas eu quero mostrar a diferença que ela consegue fazer num cenário real. Essa técnica é a combinação de **agent waves** com a **distribuição de tarefas para modelos fortes e fracos**.

## O que são Agent Waves

Agent waves nada mais é do que um nome bonitinho que deram para fazer uma orquestração das tarefas de forma paralela, utilizando uma técnica de multiagentes. A gente vai ter um agente que vai ser o nosso **primary coordinator** (o coordenador principal), que vai fazer o breakdown das tarefas — de todas as etapas que precisam ser realizadas, de todos os objetivos que precisam ser alcançados — e transformar essas tarefas em subtarefas que podem ser paralelizadas em workers: essas seriam as chamadas waves de fato.

Então, ao invés de lidar com todas as tarefas que compõem uma tarefa mais complexa de forma sequencial, a gente quebra isso em tarefas paralelas para multiagentes/subagentes que vão ser chamados. Até aqui, essa técnica já era conhecida e já se usava na comunidade — só não tinha um nome bonito ainda, mas agora estão chamando isso de agent waves.

## Onde entra a otimização de custo

A otimização de custo entra na estratégia de utilizar modelos fortes e fracos para cada uma das tarefas, dependendo do perfil da tarefa que está sendo realizada. A grande moral é que o agente coordenador (primary coordinator) utiliza um modelo mais caro — no exemplo, o **Kimi K3**, por ser o modelo do momento — para fazer o planejamento, quebrar as tarefas em etapas paralelas e detalhar exatamente o que precisa ser feito.

Então esse agente coordenador delega as tarefas de implementação, já todas detalhadas com tudo que precisa ser feito, para um modelo mais barato — no exemplo, o **Kimi K2 (K2.7 Code)**, que tem um custo bem mais baixo que o K3.

A família de modelos da Kimi já tem um custo mais baixo comparada a preços do Codex ou do Claude Code, mas, olhando só para a família Kimi, o K3 é o mais caro e o K2 é o mais barato (lançado anteriormente). Então é inteligente pegar a tarefa complexa, passar para o K3 pesquisar tudo que precisa ser feito, detalhar exatamente o que vai ser feito, ajudar na tomada de decisão (com contribuição técnica do humano também) e, quando estiver tudo planejado e decidido, paralelizar e delegar somente a tarefa de implementação para os modelos mais baratos, para economizar.

O grande comparativo deste vídeo é: se eu pegasse essa mesma tarefa e esse único contexto e desse para o K3 fazer tudo, com uma resposta final, versus eu trabalhar com agentes (agent waves) — qual seria o custo final, o que sairia mais em conta, e qual a diferença de custo.

## Como se calcula o custo

Custo = (input + contexto reinjetado) × preço do input + output gerado × preço do output.

Isso vai dizer qual vai ser o custo final daquela tarefa, porque soma-se o preço dos tokens de input mais o preço dos tokens de output. Uma coisa importante de lembrar: no input, sempre há contexto extra sendo injetado além do que foi escrito manualmente (CLAUDE.md, AGENTS.md, rules do projeto, etc.).

## Simulação no Google Colab

Foi feito primeiro um comparativo no Google Colab, com um algoritmo para simular uma tarefa sendo passada de forma paralela e de forma única para o agente forte, usando os preços reais do Kimi:

- **Kimi K3**: US$ 15 de output; US$ 3 de input com cache miss; US$ 0,30 de input com cache hit.
- **Kimi K2.7 Code** (modelo específico deles para trabalhos de código): US$ 0,19 com cache hit; US$ 0,95 com cache miss; US$ 1,4 de output — cerca de três vezes mais barato que o K3.

A simulação considerou uma tarefa maior quebrada em seis subtarefas, realizada seis vezes por mês, com estimativas de tokens do pedido do usuário e de contexto compartilhado/instruções por subagente (~700 tokens de input, ~2.500 tokens de contexto por subagente — uma tarefa pequena, propositalmente).

**Resultado da simulação:**
- Um agente único usando K3 para tudo: custo mensal de **R$ 110**.
- Agent Waves (K3 como coordinator + K2.7 como worker): custo mensal de **R$ 73**.

Analisando os tokens de input e output de cada modelo: com Agent Waves, o número de input tokens foi muito maior do que com o agente único. Isso acontece porque, a cada subagente spawnado (delegado uma tarefa), é preciso passar um contexto inicial para aquele agente e reinjetar arquivos do contexto. Com um único agente que faz tudo, o input é dado uma vez, o contexto é capturado uma vez, e a partir daí ele trabalha sem precisar reinjetar contexto.

Com Agent Waves, a cada nova tarefa paralelizada é necessário spawnar um agente novo, que precisa de um contexto pequeno e de contexto injetado do que está sendo realizado — por isso consome-se mais tokens de input. Mas, como o modelo usado nos workers tem custo de input muito mais baixo que o K3, isso compensa no custo final.

**Ponto central:** não basta olhar para número de tokens, é preciso olhar para o custo final. Consumiu-se mais tokens usando Agent Waves, mas de um modelo mais barato — isso baixou o custo total. Se o consumo extra fosse do modelo mais caro (K3), obviamente sairia mais caro, e não haveria o que comparar.

**Alerta:** se a estratégia de multiagentes (Agent Waves) usar sempre o mesmo modelo caro em todos os subagentes, a estratégia só vai aumentar o custo, não reduzir. A redução de custo só existe se as tarefas de implementação forem delegadas para modelos mais baratos.

## Teste prático na API da Kimi

Depois da simulação, foi feito um teste real na plataforma da Kimi (Moonshot AI), com créditos carregados na conta (US$ 7, com parte já consumida em teste). A Kimi tem dois modelos relevantes: **K3** e **K2.7** (específico para código) — além de um K2.6 de propósito geral.

Preço do Kimi K2 Code: em torno de US$ 0,19 por 1 milhão de tokens (com cache hit) — extremamente barato, por isso os preços aparecem com várias casas decimais.

A Moonshot também oferece assinatura mensal (não só API), com planos a partir de $ mensal / $15 anual, até $159/$199 no mensal, dando acesso a uma quantidade de créditos por mês para uso geral com os agentes deles.

### Teste 1: agente único (K3 fazendo tudo)

Usando o **OpenCode** (harness open source) num projeto real (newsletter "Bora Tomar Café"), foi enviado um prompt pedindo para criar um preview de e-mails no painel de administração, antes de enviar a newsletter — funcionalidade que ainda não existia. Modo "high" (reasoning effort), modelo K3.

Saldo antes: R$/US$ 26,9(16) (balance da conta).

Ao final, o agente alterou 6 arquivos, com 298 adições e ~25 remoções: gerou testes unitários (suite com dois testes), alterou o template de e-mail (renderização de newsletter em HTML), modificou o formulário de edição de edição da newsletter (upload de markdown já gera preview do e-mail), criou o componente de e-mail preview, adicionou uma action (`preview edition email action`) com teste unitário, e atualizou a documentação do projeto.

Saldo final: 25,4984 → **custo de aproximadamente US$ 0,42** e alguns centavos usando somente um agente forte (sem delegação, sem quebra em subagentes).

### Teste 2: Agent Waves (K3 coordinator + K2.7 worker)

Mesmo prompt, mas pedindo ao agente: "planeje a seguinte tarefa e então delegue as subtarefas de implementação para o modelo Kimi K2.7", mantendo o K3 como coordenador (responsável por quebrar em subtarefas e delegar para o modelo mais barato). Foi pedido também para criar uma worktree nova, para não conflitar com as alterações do teste anterior.

Ressalva do autor: essa não é a forma ideal de fazer Agent Waves — o ideal seria um fluxo de orquestração de agentes automático, conectado a uma pipeline originadora de tarefas, com prompts/specs melhor estruturados. Aqui é uma simplificação só para efeito de comparação.

Saldo final: caiu para **24,4893**, dando um custo total um pouco menor que o do agente único — diferença de cerca de **40 centavos de dólar**.

## Interpretação do resultado

A diferença absoluta (40 centavos) parece pequena numa única tarefa simples (editar preview de e-mail, exportar uma função, gerar testes, mexer em um arquivo de documentação). Mas em escala — uma reestruturação grande, ou um time inteiro usando a API do modelo de IA, ou uma API usada para chat com clientes — essa diferença se torna muito mais significativa.

Vale notar que o teste de Agent Waves teve uma tarefa extra: como foi pedida a criação de uma worktree, houve mais idas e voltas de conversa com o agente (ele avisou que a branch já tinha alterações feitas, perguntando o que fazer) — gastando um pouco mais de tokens do que o teste do agente único, que não teve essas trocas extras. Isso foi algo irrisório no teste, mas relevante de lembrar.

A estratégia de Agent Waves seguida no vídeo foi deliberadamente a mais simples/"porca" possível (só um prompt pedindo para delegar), não uma configuração bem estruturada — o autor sugere que uma abordagem mais madura de orquestração de agentes tiraria mais proveito da técnica.

## Conclusão

Para quem usa modelos de IA cobrados via API com estratégia de multiagentes (Agent Waves ou equivalente), a economia de custo só existe se as tarefas de implementação forem delegadas para modelos mais baratos — usar o mesmo modelo caro em todos os subagentes apenas aumenta o custo total, mesmo com a paralelização. O coordenador que planeja/decide pode (e talvez deva) usar o modelo mais forte, já que aquela etapa é mais crítica; a implementação detalhada, uma vez bem especificada, pode ir para um modelo mais barato sem perda relevante de qualidade — pagando o preço de mais tokens de input (contexto reinjetado a cada subagente) em troca de um preço por token muito menor.
