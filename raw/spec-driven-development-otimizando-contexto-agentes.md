# Spec-Driven Development: Otimizando o Contexto para Agentes de Código

> Transcrição de vídeo (autor não identificado por nome completo/canal na fala — conteúdo e referências, como o workshop "Desenvolvimento Assistido por IA Avançado" e a skill "TLC Spec Driven" atribuída a "nosso grupo de pesquisa de IA" e a Felipe Rodrigues, apontam fortemente para a Tech Leads Club). Erros de reconhecimento de fala (ASR) corrigidos por contexto técnico ao transformar em Markdown — ver observações ao final.

Eu venho usando agentes de IA no meu dia a dia há muito tempo — Claude Code, Cursor, Copilot — e cheguei numa conclusão que a maioria das pessoas ignora: o modelo, mesmo que os atuais sejam muito bons, não é o suficiente. O que separa um resultado mais ou menos de um sistema completo e funcional é o **contexto** que você dá pra ele. E é aí que entra o **Spec-Driven Development**, um padrão para desenvolver otimizando o contexto para ter os melhores resultados.

Neste vídeo você vai aprender como aplicar isso em qualquer code agent para desenvolver com escala, segurança, economizar tokens e evitar retrabalho — que é o que a gente mais quer.

## O Problema: Como a Maioria das Pessoas Se Frustra com IA

A maioria das pessoas pega uma demanda — por exemplo, implementar recomendações num sistema de streaming — e faz um de dois caminhos ruins:

1. **Tenta quebrar isso em partes menores manualmente** e perde o contexto entre uma coisa e outra.
2. **Roda a implementação direto**, ou gera um plano a partir de um PRD grande de uma vez só.

No exemplo: um sistema de streaming fictício ("FakeFlix") onde os usuários não têm recomendações personalizadas — não sentem que existe uma experiência pensada para eles. É uma funcionalidade que impacta todo o sistema, toca vários módulos.

Se eu simplesmente disser "gera um plano a partir desse PRD para implementar", vou ter um plano — mas um plano não é feito para ser longo. A funcionalidade de "plano" que as ferramentas têm hoje não é feita para cobrir um projeto inteiro; é feita para fazer uma tarefa bem feita. Quando o projeto é grande, é preciso **paralelizar tarefas**, saber qual tarefa vem primeiro, qual pode ser feita junto com outra, quais dependem de quais. Um plano único não resolve isso.

Usando Spec-Driven Development, dá para escalar muito mais: criar uma spec da feature de recomendações com um *breakdown* de tasks — ordem das tasks, quais podem ser paralelizadas — e a partir disso, executar.

## Como Funciona o Contexto num LLM

Antes de entender por que Spec-Driven Development cresceu tanto, é preciso entender como funciona o contexto.

Hoje existem janelas de contexto de até 1 milhão de tokens, mas a recomendação é **não usá-las inteiras** — tentar manter o uso dentro de ~200.000 tokens. **Quanto maior a janela ocupada, maior a chance de alucinação.**

Quando você começa a usar um agente, a janela está limpa — ele não sabe de nada. Depois vai entrando: o prompt, os arquivos necessários que ele buscou, o `AGENTS.md`/rules, os MCPs necessários para a tarefa, as skills necessárias. A janela de contexto tem tamanho limitado, e quanto mais cheia, maior a chance de alucinar.

Primeira premissa: **otimizar a janela de contexto**.

Mas como fazer uma funcionalidade grande — tipo recomendações, que muda 90 arquivos — sem estourar a janela? Isso é possível implementando o padrão **RPI: Research → Plan → Implement**.

### Research

Na fase de research, abre-se um agente para pesquisar. Ele abre uma janela de contexto própria, passa pelo codebase respondendo às perguntas feitas, bate em arquivos relevantes, usa as skills necessárias, busca externamente via MCP ou em sites. É a fase de descobrir o que precisa ser feito.

### Plan

Depois que já se está mais seguro do que precisa ser feito (já se conversou e entendeu no alto nível), a fase de research termina e **tudo que foi aprendido é salvo em arquivos Markdown**. Isso é decisivo: se a implementação partisse direto de uma janela de research (já poluída, e que tende a crescer), não daria para fazer uma mudança de 90 arquivos sem gastar mais tokens e sem poluir o contexto.

Ao salvar o research em Markdown, é possível reaproveitar esses arquivos no futuro sem gastar tokens pesquisando de novo. A fase de plan no Spec-Driven Development é onde se cria a **spec** e, se necessário, o **design**. (O próprio Spec-Driven Development pode ser usado também para conduzir essa fase de research.)

### Implement

Com spec e design claros, o trabalho é separado em partes (tasks). Na implementação, o agente pega as tasks já definidas no planejamento e executa. Como a spec e o design já são muito claros, não é preciso refazer a fase de research — está tudo definido, e o agente sempre pode voltar a consultar esses documentos. Isso economiza tokens no futuro.

## Os Passos do Spec-Driven Development

A base usada aqui é uma skill chamada **"TLC Spec Driven"**, baseada nos melhores padrões de Spec-Driven Development, mas extremamente flexível. Outra alternativa conhecida é o **Spec Kit do GitHub** — mais engessado, mas com os mesmos princípios.

### 1. Specify (Especificar)

Passo obrigatório: capturar o que está sendo feito. Cria-se uma **spec**, que serve de base para depois quebrar o design e as tasks. A spec contém:

- O **problema** que está sendo resolvido
- A **meta** (ex.: reduzir tempo até o play, crescer número de plays)
- O que está **fora de escopo**
- As **user stories** — qual o problema do usuário que está sendo resolvido

Tudo isso fica como referência para a IA durante a implementação: o problema, os gols, o que não está em escopo, as user stories, e o contexto geral.

### 2. Design (opcional)

Num projeto grande — por exemplo, ~40 tasks — se o design ficasse dentro de cada task, ficaria repetido. Por isso os diagramas e decisões de projeto ficam num arquivo separado, referenciável a partir de qualquer task: diagrama de arquitetura da solução, o que vai ser reusado, componentes no alto nível, decisões importantes do projeto. Esse arquivo não é criado manualmente — a própria skill cria a partir da spec.

### 3. Tasks

Com spec e design prontos, o trabalho é quebrado em tasks. Cada task é entregável. A quebra é otimizada para permitir boas decisões sobre o que pode ser rodado em paralelo e o que não pode — otimizando tanto velocidade de entrega quanto uso de contexto.

Exemplo de estrutura: tasks que precisam ser sequenciais (task 0, task 1...), depois um bloco de tasks (ex.: camada de persistência) que podem ser feitas em paralelo entre si.

Cada task no breakdown documenta:

- O que vai ser feito
- Onde vai ser feito
- O que vai ser reusado
- De quais outras tasks ela é pré-requisito
- Uma *definition of done*

Isso é, na prática, um plano — tem todo o contexto que a IA precisa para escrever aquele bloco de código específico, sem precisar fazer uma nova pesquisa: a task já diz tudo que precisa ser feito. Isso reduz muito a chance de erro ou de comportamento inesperado, porque o agente tem um escopo claro e pequeno, e pode inclusive decidir se várias tasks pequenas cabem numa única execução ou se uma task está grande demais e precisa ser quebrada mais.

### 4. Execute

Hoje em dia, subagentes genéricos permitem escalar e fazer implementações grandes sem explodir o contexto principal. Ao rodar a implementação de um projeto grande com o prompt "use subagents o máximo possível, não precisa — a maioria das ferramentas novas já é inteligente o suficiente para isso" — o agente abriu subagentes para fazer a pesquisa, e depois, na fase de implementação, olhou nas tasks o que podia ser feito em paralelo e usou (no exemplo mostrado) **quatro subagentes em paralelo**, cada um cuidando de um subconjunto de tasks.

Isso permite: otimizar contexto, reduzir chance de erro (cada agente faz uma coisa específica) e escalar para mudanças grandes.

## Projeto, Estado e Continuidade

Quando se cria uma spec, mais artefatos são gerados:

- Um **projeto**: definição de alto nível do projeto como um todo, com um resumo.
- Um **estado**: guarda as decisões importantes que o agente tomou durante a implementação.

O estado é importante porque permite abrir uma nova janela de contexto e dizer "continua o projeto tal" — e funciona, porque o estado garante continuidade e registra o porquê das decisões tomadas. Também permite commitar as specs e seguir o resto do projeto depois, inclusive separando o trabalho em vários pull requests.

## Uso na Prática

É possível simplesmente pedir "me ajuda a especificar o novo projeto" — a skill faz perguntas até chegar num entendimento suficiente. Se um contexto for dado de início (ex.: um PRD já pronto), a skill usa esse PRD como base e cria tudo que der para criar a partir dali, perguntando apenas o que não estiver claro.

Exemplo de prompt usado num projeto real: *"Esse é o novo projeto que vou começar, tem o PRD, já fiz uma POC e o recommendations vai ser um novo módulo no sistema. Use a spec-driven para planejar o projeto."* A partir disso a skill criou a spec, o design e as tasks.

A implementação foi feita numa **janela de contexto nova**, separada da janela usada para pesquisa/planejamento — prática já reforçada em vídeos anteriores: pesquisa numa janela, implementação limpa em outra.

## Sobre a Skill

A skill demonstrada ("TLC Spec Driven") foi criada pela Tech Leads Club, principalmente por Felipe Rodrigues (grupo de pesquisa de IA). Recomendação de uso: instalar globalmente, para que qualquer projeto já saia usando a partir do prompt.

A skill é flexível — nem todo projeto precisa de tudo. Para projetos pequenos, dá para pedir só a spec e as tasks, pulando a fase de design ("estou planejando um projeto pequeno, cria as tasks" pula o design). Para projetos grandes, a recomendação é usar todas as fases.

## Divulgação: Workshop

Menção a um workshop chamado "Desenvolvimento Assistido por IA Avançado" (2ª edição, dias 16 e 17 de maio), cobrindo fundamentos de context engineering, spec-driven development e desenvolvimento autônomo com agentes.

---

## Notas de Transcrição

Transcrição original obtida via reconhecimento automático de fala, com diversos erros de ASR corrigidos por contexto técnico ao formatar em Markdown — por exemplo: "SPC Driven Development" → **Spec-Driven Development**; "RPI research plan implement" mantido e expandido para **Research → Plan → Implement**; "gols" (fonética de "goals") mantido como está, mas esclarecido como "metas"; "Fake Flix" → **FakeFlix** (nome fictício do sistema de streaming usado como exemplo); "Speck Kit do GitHub" → **Spec Kit do GitHub**; "agentes.m e as rules" → **`AGENTS.md` e as rules**; a repetição "gente" (marcador de fala coloquial comum em português brasileiro) foi reduzida na reescrita para melhorar a legibilidade, sem alterar o conteúdo técnico. Autoria não confirmada por nome completo — inferida por contexto (menções à Tech Leads Club, ao workshop e à skill "TLC Spec Driven") como possivelmente Valdemar Neto, cofundador da Tech Leads Club, mas isso **não está confirmado** na transcrição em si.
