# 8 Pontos de Arquitetura de Software na Era da IA

*(Bloco de CTA — like, inscrição no canal, sino de notificações e comentário pedindo a opinião do espectador — omitido por não ser conteúdo técnico. Bloco de propaganda do MBA em Engenharia de Software com IA da Full Cycle, repetido no início e no fim do vídeo, condensado numa única nota ao final.)*

## Contexto: por que isso importa agora

A forma como se desenvolve software está mudando completamente depois da IA, e não tem mais volta. A cada dia, todo desenvolvedor — sem exceção — vai ter que entender muito mais sobre arquitetura de software e arquitetura de solução. O desenvolvedor não vai mais ficar digitando código o tempo todo; ele vai ter que ser capaz de **pilotar IA**. E para pilotar IA ele precisa de conhecimento profundo o suficiente para entender o código que está sendo gerado e qual vai ser o impacto disso no projeto. Sem entender arquitetura de software e arquitetura de solução, isso fica cada vez mais complexo.

Esses oito pontos foram extraídos do trabalho de montar a ementa do MBA em Engenharia de Software com IA da Full Cycle — vieram de muitas conversas com profissionais de grandes empresas sobre o que realmente está importando aprender hoje em arquitetura.

### Havia um mundo de arquitetura de software antes da IA

Muito do que se usava (e ainda se usa) de arquitetura de software tradicional continua atual — não é descartado. Mas depois da entrada da IA no jogo, a arquitetura de software mudou completamente: muita coisa foi adicionada, e partes da arquitetura tradicional vão precisar ser readaptadas para se encaixar nessa evolução.

### O perfil do desenvolvedor mudou

Desenvolvedores vão ter que atuar cada vez mais como arquitetos: organizar, criar workflows, ter visão clara do projeto, entender padrões em uso, restrições do projeto e atributos de qualidade. Antes, isso ficava muito a critério do arquiteto de software — um cargo tipicamente de alto nível, sem mão constante no código. Agora o papel do arquiteto também fica mais abrangente e mais ligado ao código de baixo nível, porque o desenvolvedor está assumindo parte dessas responsabilidades. Quem já trabalha com arquitetura hoje também vai precisar se adaptar.

Formas novas de desenvolver aplicações — que antes não existiam sem a tecnologia de IA — trazem novos componentes, regras e camadas de segurança, todos exigindo mais conhecimento de arquitetura de software.

Segue a lista dos oito pontos, cada um com uma pincelada de subtópicos — não é um aprofundamento completo, é um roadmap de estudo.

---

## 1. Agentes de IA e Protocolos de Comunicação

Ainda existe um conceito muito abstrato do que é um "agente de IA" — muitos desenvolvedores não têm clareza sobre isso. Um agente de IA não é um software comum, mas ao mesmo tempo **é** um software. Por isso vale revisitar a comparação entre microsserviços e agentes de IA: um agente de IA pode ser um microsserviço. Estruturalmente ele é diferente do software comum, mesmo rodando como microsserviço e tendo os mesmos problemas e conceitos de escala já conhecidos.

Isso implica **arquiteturas de agentes de IA** — arquitetar um agente exige pensar de forma completamente diferente. Existem vários tipos:

- Agentes que trabalham **em paralelo**
- Agentes que trabalham **de forma sequencial**
- Agentes **customizados**, onde se consegue forçar um workflow
- Agentes **completamente autônomos**, com pouco controle sobre como um agente chama outro

Se essa arquitetura não for pensada antes de sair desenvolvendo os agentes, surgem grandes problemas (o autor relata ter passado por isso). Um agente sozinho não resolve — normalmente se criam **equipes de agentes**, aplicações **multiagênticas**, o que exige aprender a orquestrar e fazer esses agentes se comunicarem: um novo formato de comunicação de sistemas.

Comunicação de sistema implica **protocolos**, e há protocolos novos surgindo:

- **MCP (Model Context Protocol)** — faz o agente executar ferramentas e ter acesso a *resources* e *prompts*. Pode ficar complexo rapidamente quando os meios de transporte mudam: de STDIO (uso comum, local) para **streamable HTTP**, necessário para escalar dentro de uma empresa e buscar dados de diversos lugares. **SSE está depreciado** dentro do ecossistema MCP.
- **A2A (Agent-to-Agent)**, protocolo feito pela Google, permite que agentes em tecnologias e frameworks diferentes se comuniquem entre si. Há cada vez mais iniciativas de novos protocolos além desses dois.

No meio disso entra **evaluation**: como observar o comportamento dos agentes e verificar se estão trazendo os resultados esperados de forma controlada — lembrando que IA trabalha de forma **não determinística**, diferente dos `if`/`else` tradicionais.

## 2. Design Patterns Focados em IA

Hoje já existem design patterns voltados para IA — padrões para desenvolver aplicações que se integram a LLMs, e padrões específicos para a criação de agentes de IA. Também existem design patterns focados em **segurança**, porque prompt injection pode contaminar um agente; usar múltiplos agentes ajuda a impedir que informações contaminadas se propaguem.

Uma iniciativa relevante: **12 Factor Agents** — em analogia ao **Twelve-Factor App** que a Heroku criou na época para escalar software. Quem nunca desenvolveu um agente ou não entende com clareza o que é um agente vai ter dificuldade para entender o 12 Factor Agents, porque falta a base.

## 3. Caching

Nada muda mais um software do que a mudança de escala (10, 100, 1.000, 100.000, 1 milhão, 10 milhões de acessos) — a escala muda a fundação inteira do sistema. Caching é o que torna o sistema mais rápido e, fundamentalmente, mais barato.

Conceitos de cache que já existiam continuam existindo: formas de invalidação, **time to live (TTL)**, **cache-aside**, **write-through**, e *eviction policies* como **LRU**, **LFU**, **FIFO**, **MRU**, *random replacement*.

A partir daí entra a camada específica de IA:

- **Cache de tokens em LLMs** — depende muito do provider (OpenAI, Gemini, Claude cada um trabalha de um jeito)
- **Cache de contexto e embeddings**, principalmente em aplicações com RAG
- **Cache-aware prompts** e uso de *fingerprints* para controle de resposta

Não entender caching bem em aplicações de IA impacta não só a latência, mas fortemente o **custo** — cada chamada a um LLM custa dinheiro, cada token custa dinheiro, então otimizar isso é matéria obrigatória.

## 4. Segurança

Sem virar especialista em segurança, alguns conceitos são obrigatórios:

- **Jailbreaking** — impedir que a IA seja sugestionada a se comportar fora do esperado (ex.: um usuário mal-intencionado força a IA a falar como uma galinha, ou a usar discurso de ódio, e depois alega que foi "atendido" daquela forma por uma empresa).
- **Prompt injection** — diferente e mais grave que jailbreak: consegue extrair dados sensíveis e fazer a IA executar operações dentro do sistema de forma destrutiva, comprometendo segurança da empresa, servidores e infraestrutura.
- **Guardrails** — técnicas e frameworks para manter a IA dentro de limites determinados: validações antes/depois de chamar o agente, antes/depois de chamar uma tool, etc.
- **Proteção de dados sensíveis** — ofuscação antes de passar dados para a IA, principalmente no pipeline de observabilidade.
- **OWASP Top 10 para LLM e IA Generativa** — assim como existe o OWASP Top 10 tradicional, existe uma versão específica trazendo as principais falhas de segurança a observar ao desenvolver agentes e aplicações com IA.

## 5. Prompt Engineering e Context Engineering

**Prompt engineering** é a base de tudo — se não se sabe especificar o que pedir e quais técnicas usar (chain of thought, tree of thoughts, skeleton of thoughts, ReAct, self-refining, entre outras), o agente não se comporta como esperado. Boa parte do tempo de desenvolvimento de uma aplicação de IA vai para ajustar o prompt.

**Context engineering** é dar o máximo de contexto possível para a IA: documentação, design docs, documentos de contexto, playbooks de execução — tudo que documenta o projeto ajuda a IA a ser mais precisa. Não é só gerar documentação estática — é fazer a IA buscar, em tempo real, documentações que estão em servidores e bancos de dados da empresa. Isso importa especialmente em aplicações de grande porte (não numa prova de conceito). Ao longo do tempo, cada documento e cada decisão registrada vira um ativo do projeto — o mesmo raciocínio de teste automatizado: você investe uma vez e colhe o resto do projeto.

Outro ponto complexo: **versionamento de prompts e históricos de interação**. Não é simplesmente versionar um prompt no Git ou num banco de dados — uma nova versão de prompt pode quebrar o sistema, então é preciso ter formas de validação e capacidade de rollback, idealmente dentro da pipeline de CI/CD, barrando prompts que falham em testes automatizados antes de subir.

## 6. System Design, Escala e Observabilidade na Era da IA

Desenvolver uma aplicação de grande porte exige entender os novos princípios de system design — como o ecossistema se comunica entre componentes. A era da IA traz novas formas de fazer system design, novos componentes, novas chamadas, novas formas de interação.

Escalar para milhões de usuários exige balancear um triângulo:

- **Performance** (menor latência nas respostas)
- **Custo** (menor gasto)
- **Qualidade** (resultado satisfatório)

Encontrar o modelo mais barato com qualidade satisfatória e boa performance para escalar exige técnicas específicas de trade-off.

Componentes que passam a se integrar com IA:

- **Pipelines, mensageria e streaming** (Kafka, RabbitMQ)
- **Bancos de dados vetoriais** para consulta por proximidade/embeddings — inclusive bancos como Redis, que oferecem suporte a vetores, funcionando como uma nova camada de cache
- **Compatibilidade entre versões de embeddings**, importante ao trocar de provider de modelo
- **Arquitetura de RAG** (Retrieval Augmented Generation) — não é só "buscar num banco vetorial e jogar no contexto". Para trazer informação acurada de verdade envolve metadado, estruturação, tipos de documento, fontes, versões, invalidação e sincronização — complexo principalmente em escala
- **Cloud providers** (Google, AWS, Azure, OpenAI) — cada um com um conjunto de serviços prontos (ex.: Vertex AI da Google com bancos vetoriais integrados para acelerar RAG)

**Observabilidade** — logs, tracing, métricas, eventos — agora precisa responder por IA: como fazer tracing de um LLM, como analisar a chamada de um agente para outro e sua latência. Open Telemetry está incorporando essa camada orientada a IA.

## 7. Testes de Qualidade em Sistemas com IA

Da mesma forma que existem testes automatizados de aplicação, é preciso ter testes de **prompts e contextos** ("promptings"). Existem frameworks especializados que:

- Criam componentes de prompt testáveis
- Recebem entrada/saída desejadas e ajustam o prompt automaticamente, gerando variações até melhorar o resultado
- Permitem avaliar agentes com **datasets reais** e **snapshots** do comportamento esperado, rodando testes mais determinísticos para garantir que atualizações em modelo, código ou prompt mantenham (ou melhorem) o comportamento

Ferramentas citadas: LangSmith, entre outras. Ferramentas de observabilidade tradicionais como Datadog e New Relic também estão evoluindo com agentes de IA embutidos para ajudar nesse processo.

## 8. Controle de Custos em Arquiteturas com IA

Há casos de empresas que quase fecharam as portas por implementar IA sem entender gestão de custos e receberem uma conta gigante no fim do mês. Pontos obrigatórios:

- Entender **input tokens** vs. **output tokens**
- **Limites por modelo**
- Estratégias de **caching** para reduzir custo (ligação direta com o ponto 3)
- Calculadoras e ferramentas de estimativa de custo — por usuário, por chamada, por uso completo de fluxos multiagente
- **Logging e monitoramento** de custo
- Otimizações: truncamento inteligente de prompt, sumarização para economizar tokens, testes A/B custo × qualidade

Para cada parte de um sistema, o modelo ideal tende a ser diferente — nem todo modelo serve para todo caso de uso. Às vezes usar dois ou três modelos/chamadas diferentes dentro de um único processo acaba sendo mais rápido e mais barato do que depender de um único modelo mais lento e caro.

---

## Fechamento

A lista é longa, mas dá um ponto de partida para pensar em arquitetura de software e arquitetura de solução numa era em que a profissão está sendo redefinida. O convite do autor: comentar o que já está sendo estudado desses oito pontos, o que é novidade, e quais itens adicionar ou remover da lista.

*(Nota: bloco promocional do MBA em Engenharia de Software com IA da Full Cycle, citado no início e no fim do vídeo — estrutura com quatro pilares: desenvolvimento de aplicações integradas com IA, desenvolvimento de agentes de IA, entrega rápida/segura/confiável via DevOps e SRE, e uma trilha de arquitetura cobrindo os mesmos oito pontos deste vídeo — mais soft skills, marketing pessoal, trabalho em equipe e empreendedorismo. Condensado aqui por ser conteúdo comercial, não técnico.)*
