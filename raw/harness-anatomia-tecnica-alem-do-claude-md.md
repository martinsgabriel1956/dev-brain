# Harness: a anatomia técnica por trás do Claude Code, Cursor e Codex

## Introdução

A palavra "harness" e o conceito de "harness engineering" estão aparecendo em todo lugar, mas boa parte das pessoas que usam o termo não entende de fato o que é harness — que não é só criar um `CLAUDE.md` na raiz do projeto ou configurar um monte de skills. Este vídeo apresenta uma definição mais técnica e teórica do que é considerado harness, e algumas técnicas de harness engineering já aplicadas pelas ferramentas de agentic coding mais populares — Claude Code, Codex, Cursor, e outras.

## Definição de Harness

Harness é tudo que está ao redor do modelo: toda a camada de aparatos, ferramentas, frameworks e técnicas colocadas em volta de um modelo de IA para tentar extrair dele a melhor eficiência e o melhor resultado possível.

É aqui que a confusão começa. Quando se fala em harness, muita gente pensa só nas skills, no arquivo `AGENTS.md` (ou no próprio `CLAUDE.md`), nas rules, nos hooks, etc. Mas todas essas estratégias compõem apenas a parcela do que se chama **user harness** — o harness que o usuário consegue manipular, criar e montar em volta do próprio projeto ou localmente, para trabalhar com os agentes e tentar extrair a melhor eficiência deles.

O harness vai muito além disso. Além da parcela que o usuário configura e monta, existe uma camada que normalmente não é visível: o harness feito pelas próprias ferramentas de agentic coding — o harness do Claude Code, o harness do Cursor, o harness do Codex, etc. Como usuários, não enxergamos todas as técnicas e ferramentas que estão por trás para que, no final, o input chegue ao modelo e a inferência aconteça.

Harness é tudo isso que está ao redor do modelo tentando controlar o resultado, tentando gerar resultados mais previsíveis, fazendo o modelo seguir instruções, seguir regras, se lembrar de coisas e entregar alta eficiência.

## As Ferramentas de Agentic Coding São, Elas Mesmas, Harness

Olhando para as principais ferramentas de agentic coding, fica claro que elas são harness:

- **Claude Code** é o harness da Anthropic. Além de desenvolver os modelos, a Anthropic também construiu uma ferramenta de agentic coding — um aparato de tools e técnicas de harness engineering rodando em volta dos próprios modelos, para entregar uma boa ferramenta de código.
- **OpenClaw**, **OpenCode**, **Hermes Agent**, **Trae**, **Codex**, **Cursor** — todos são, no fundo, harness.

Todas essas ferramentas colocam um monte de coisas em volta do modelo, que fica no meio, sendo alimentado com contexto, tools, skills, rules, instruções, guardrails e trace, para que, no final, tudo isso gere um bom resultado.

O ponto central: no Cursor é possível usar os mesmos modelos usados no Claude Code — dá para usar o Opus no Cursor, dá para usar o GPT no Cursor (o mesmo GPT usado no Codex), no Trae também é possível usar GPT, Kimi, e provavelmente GLM. O modelo é sempre a mesma peça — GPT, Kimi, GLM, Opus, Fable. É só o "miolo". Tudo que está ao redor é o que cada ferramenta adiciona. O mesmo vale para o Hermes e para o OpenCode: qualquer um desses modelos pode ser conectado ali dentro. O que muda de ferramenta para ferramenta é o harness em volta.

## Anatomia do Harness: o que tem dentro dessas ferramentas

Se o modelo é só uma fração do que essas ferramentas oferecem, o resto — o harness — pode ser detalhado observando o que acontece durante um **agent run** (uma execução do agente), antes da mensagem do usuário chegar de fato ao modelo para o reasoning.

### 1. Assemble do Contexto

Antes de a mensagem do usuário chegar à LLM, a ferramenta monta o contexto que será enviado ao modelo. Isso inclui:

- **Rules** — regras configuradas no projeto, aplicadas quando relevante.
- **Skills** — skills que podem se aplicar à tarefa solicitada.
- **User memory** — fatos memoráveis sobre o usuário, "durable facts": preferências, contexto de quem é o usuário.
- **Episodic memory** — uma memória em linha do tempo de coisas que já aconteceram, relevante porque, se o modelo já vem trocando mensagens com o usuário sobre um problema específico, tudo que já foi descoberto e analisado é relevante para a próxima inferência.
- **Semantic memory** — tudo que já se sabe sobre as preferências daquele usuário e daquele projeto (ex.: "a Fernanda é engenheira de software, tem conhecimento técnico, está construindo uma startup, ensina Java") — fatos que podem ou não ser relevantes para a tarefa atual.
- **Procedural memory** — os arquivos/markdowns configurados localmente na máquina do usuário, no projeto, e na própria ferramenta — playbooks, instruções do que fazer e não fazer (dos e don'ts).

Tudo isso é filtrado, agregado ao que for relevante, e inserido num contexto único que é então passado ao modelo para o reasoning — e isso acontece de forma invisível para o usuário, que só vê o próprio pedido.

Nem toda ferramenta implementa todas essas camadas de memória. Algumas oferecem memória episódica nativamente, outras exigem configuração manual, outras não têm nada disso — usam só o contexto do projeto e o que foi passado na conversa, sem "self-improving" sobre o usuário ao longo do tempo. O que existe ou não depende inteiramente da ferramenta usada.

Esse mecanismo de assemble de contexto é, no fundo, um **RAG**: informações salvas em banco vetorial, em markdown (principalmente a parte procedural) e em SQL, com um retrieval do que é relevante para montar o contexto que alimenta o modelo.

Mas o harness não acaba na montagem de contexto — essa é só a primeira parte.

### 2. Tools

Depois que o modelo faz o reasoning, ele pode perceber que precisa executar uma tool: rodar um comando no terminal, modificar um arquivo, fazer uma consulta na web. As tools disponíveis para o modelo também são harness — cada tool adiciona poder de ação ao modelo e abre mais possibilidades do que ele pode fazer.

### 3. Agent Loop

O agent loop é o que controla o fluxo do agente: reasoning → tool request → tool action (executar uma API, buscar um arquivo, acessar a web, alterar código) → tool result → resultado realimentado no contexto → novo reasoning → possivelmente nova tool call, e assim por diante.

Em algum momento esse ciclo precisa terminar — senão o modelo pode entrar num loop infinito pedindo cada vez mais informação antes de finalizar. Quem controla esse limite (quantas chamadas de tool o agente pode fazer, qual o timeout de cada tool, quanto tempo esperar, fail checks, etc.) é o mecanismo de agent loop.

### 4. Guardrails

Além do agent loop, há uma camada de guardrails: filtros de segurança, de formato de input, de formato do resultado da tool (uma tool pode ser maliciosa e retornar algo perigoso para injetar de volta no agente), e checagem de políticas de segurança/ética que devem ser respeitadas tanto no que se pede ao modelo quanto no output que ele entrega.

Depois de passar por todos esses filtros — recuperação de contexto, chamada de tools, filtragem de respostas, decisão de quando parar de chamar tools — a ferramenta finalmente chega na resposta final para o usuário. Todas essas etapas são feitas por Cursor, Claude Code, Codex, Trae, Hermes, OpenCode, OpenClaw, Kleine, Kiro e as demais — cada uma com técnicas ligeiramente diferentes, mas todas realizando esse mesmo loop.

### 5. Observabilidade

Nem toda ferramenta oferece essa camada — é mais comum em agentes/assistentes construídos sob medida (ex.: Hermes ou OpenClaw, quando o usuário está construindo o próprio agente). Observabilidade permite:

- Monitorar logs, ver quando o agente está falhando ou não conseguindo performar uma tarefa — o que possibilita self-improving (adicionar novas tools, novos contextos, corrigir o que está causando falha).
- Controlar custo por token — quantos tokens estão sendo gastos, quanto isso custa, o que está consumindo mais.
- **Retries**, para recuperar tarefas ou processos que falharam durante a execução.
- **Evals** — medir as respostas geradas pelo modelo contra um padrão de qualidade esperado, e identificar o que poderia ser melhorado se o padrão não for atingido. É assim que se sabe, de fato, que um agente construído está funcionando para a tarefa que ele foi desenhado para resolver ("how we know it works").

Tudo isso — assemble de contexto, tools, agent loop, guardrails, observabilidade — pode ser considerado harness.

## Grau de Controle Depende da Ferramenta

Dependendo da ferramenta usada, o usuário tem mais ou menos controle sobre esse harness:

- **OpenClaw** (construindo o próprio agente): controle quase total. É possível escolher como implementar observabilidade, e até conectar memórias episódicas próprias — por exemplo usando o **Mem0** (memzero), uma camada de memória persistente para agentes bastante popular na comunidade. O mesmo tipo de conexão é mais difícil de fazer no Cursor.
- **Cursor**: menos controle. O Cursor mantém mais controle sobre o harness internamente — o usuário é, essencialmente, só o usuário final, com controle apenas sobre a parcela de user harness (rules, etc.).
- **Codex e Claude Code**: um meio-termo. O usuário não é responsável por tudo, mas tem alguma flexibilidade para adicionar guardrails, policies e outras peças do harness.

É possível, inclusive, construir o próprio "Claude Code" — trabalhoso, mas viável. O próprio Claude Code se tornou open source no GitHub depois de um vazamento na Anthropic: o código de tudo que a Anthropic faz de harness em volta dos próprios modelos, para entregar essa ferramenta, está publicamente disponível — dá para pegar esse código, adaptar, adicionar novas técnicas, novos retrievals, outras policies e outras coisas que se queira controlar. Tudo isso que se coloca em volta, antes de gerar o resultado final, é o que se pode considerar harness.

## Conclusão

Harness não é só um `CLAUDE.md` na raiz do projeto ou um punhado de skills configuradas — isso é apenas a parcela de user harness. Harness completo inclui a montagem de contexto (rules, skills, memória de usuário, memória episódica, memória semântica, memória procedural), as tools disponíveis, o agent loop que controla os limites de execução, os guardrails de segurança e política, e a camada de observabilidade (logs, custo, retries, evals). Ferramentas como Claude Code, Cursor, Codex, Trae, Hermes, OpenCode, OpenClaw, Kleine e Kiro são, no fundo, produtos de harness engineering construídos em volta dos mesmos modelos de fundação — o que muda entre elas não é o "miolo" (o modelo), mas tudo que foi construído ao redor dele.
