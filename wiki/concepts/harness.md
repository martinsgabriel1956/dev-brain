---
type: concept
title: "Harness"
aliases: ["AI harness", "harness de IA", "coding harness"]
date_created: 2026-06-02
date_updated: 2026-08-27
source_count: 20
tags: [harness, llm, tool-call, agente, context-engineering, erros-compostos, verificacao]
skill: tech-mentor-ai
status: stable
---

# Harness

Tudo que envolve um modelo LLM para torná-lo operacionalmente útil: gerenciamento de contexto, execução de [[wiki/concepts/tool-call|tool calls]], memória, subagentes, MCPs, system prompt e cache. O modelo em si é apenas um endpoint stateless; o harness é o que o "dá olhos e mãos".

## Por que o Conceito Importa

Um LLM isolado só consegue operar dentro do seu treinamento — não lê arquivos, não executa código, não consulta APIs. O harness conecta o modelo ao mundo real fornecendo:

1. **Tool calls registradas** — lista de operações que o modelo pode pedir (read_file, write_file, bash, web_search, MCP servers…)
2. **Contexto acumulado** — histórico da conversa + resultados das tools em cada ciclo
3. **Gerenciamento de janela** — compactação, cache, descarte de mensagens antigas
4. **Orquestração de subagentes** — paralelismo de tarefas em ambientes isolados ([[wiki/concepts/worktree-paralelismo]])
5. **System prompt** — regras, skills, CLAUDE.md — invisíveis ao usuário mas presentes em toda chamada

## Quem Executa as Tools?

**A LLM apenas orquestra. O harness executa.** Quando o modelo pede "liste os arquivos do diretório", é o processo local do harness que roda o `ls` e devolve o resultado ao contexto. Isso significa que tools maliciosas numa skill ou MCP não verificado rodam na máquina do usuário, não nos servidores do provider.

Esse mesmo fato é o que justifica isolar o processo do harness do restante do sistema — ver [[wiki/concepts/agent-containment]]. Se o harness roda `npm install` e a dependência instalada foi comprometida por um ataque de [[wiki/concepts/supply-chain-security|supply chain]], o código malicioso herda os privilégios do processo do harness na máquina real do usuário — não um sandbox do provedor.

## Ciclo de Uso

```
Usuário escreve prompt
      ↓
Harness monta contexto (system prompt + tools disponíveis + histórico)
      ↓
LLM recebe o contexto e decide: responder OU pedir tool call
      ↓
Harness executa a tool (lê arquivo, roda bash, busca na web…)
      ↓
Resultado da tool entra no contexto
      ↓
LLM decide: mais tool calls OU resposta final
```

Um único prompt do usuário pode gerar 40+ ciclos de tool calls antes da resposta final.

## Harnesses Principais (2026)

| Harness | Provider principal | Diferencial |
|---|---|---|
| Claude Code | Anthropic | Mais inovador; nativo em rules/skills/MCP/worktrees |
| Codex | OpenAI | Reset a cada 5h; GPT-5.x base |
| Cursor | Multi | IDE integrada; vários modelos incluindo open source |
| Windsurf | Multi | Interface visual; ficou uma passada atrás em features |
| ChatGPT | OpenAI | Consumer; sem acesso ao filesystem por default |
| AntiGravity | Google | Harness do Google para Gemini |
| OpenCode | Multi | Conecta em qualquer modelo via variável de ambiente |
| Cairo | — | Incorpora spec-driven nativamente |
| Devin | — | Sandbox isolado; L4; ~$15k/mês para uso intenso |

## Relação com IDE

IDE e harness são camadas separadas. O harness usa `read_file`/`write_file` independente de qual editor está aberto. IDEs como Cursor expõem diagnósticos do compilador ao harness (problema lints), o que pode ajudar, mas não é obrigatório. A tendência é que IDEs percam relevância conforme mais trabalho migra para o terminal.

## Duas Camadas do Harness

**Provider harness** — o que Claude Code, Cursor, Codex trazem por padrão: system prompt do provider, tools built-in, gerenciamento de janela.

**User harness** — o que você fornece: rules, skills, MCPs, sensores. É onde está a maior alavanca de qualidade. Ver [[wiki/concepts/sensores-vs-guias]].

### Gradiente de Controle: Nem Toda Ferramenta Expõe o Mesmo Harness

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] refina a dicotomia acima com um espectro de três pontos, em vez de um corte binário provider/user:

- **OpenClaw** (construir o próprio agente do zero) — controle quase total: dá para escolher a implementação de observabilidade e plugar a própria camada de memória episódica, ex. via **Mem0/memzero**, popular na comunidade como memória persistente para agentes.
- **Codex e Claude Code** — meio-termo: o usuário não é responsável por todo o harness, mas tem flexibilidade real para adicionar guardrails, policies e outras peças.
- **Cursor** — menor controle: a ferramenta mantém a maior parte do harness fechado; o usuário fica limitado, na prática, à parcela de user harness (rules etc.).

Reforça, com exemplo concreto, por que "harness" não é sinônimo de "modelo": o mesmo Opus roda dentro do Cursor, do Claude Code; o mesmo GPT roda no Codex e no Trae; Kimi e GLM também aparecem no Trae. O modelo é o "miolo" comum — o que muda de ferramenta para ferramenta é só o harness construído em volta.

### Claude Code Open Source Após Vazamento na Anthropic

Ainda segundo [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]], o Claude Code se tornou open source no GitHub depois de um vazamento na Anthropic — o código do harness completo (tudo que a Anthropic constrói em volta dos próprios modelos para entregar a ferramenta) ficaria publicamente disponível para clonar e adaptar. **Confiança: não verificado nesta ingestão** contra fonte primária (anúncio oficial, repositório específico, data) — tratar como claim do autor do vídeo até confirmação independente.

## Harness como Trabalho Central do Product Engineer

Dados de campo do Cursor (2026) mostram o harness em maturidade: code review automatizado por t-shirt size, specs estruturadas para agentes, MCP central com governança, self-healing por request, agents que abrem PRs sozinhos. Construir essa infraestrutura — não escrever o código em si — é a face 2 do [[product-engineer]]. A evolução do dev não é "deixar de construir" — é construir em camada diferente.

## Próximo Degrau: Loop Engineering

Depois de harness engineering (melhorar o ambiente ao redor do modelo), o degrau seguinte é [[wiki/concepts/loop-engineering|loop engineering]] — melhorar o ciclo completo de execução como estrutura repetível e disparável automaticamente (por prompt, schedule ou evento), não apenas uma execução isolada. A relação não é de substituição: o loop **contém** o harness — é o harness (compactação de contexto, estado persistente, execução de tool calls) que sustenta um loop rodando por horas sem quebrar. A leitura popular "loop engineering matou harness engineering" inverte essa relação ([[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]]).

## Por Que o Harness Importa Mais que Parece: Erros Compostos

Agentes são processos de múltiplas etapas, e erros se compõem multiplicativamente — uma pequena chance de falha por etapa vira uma chance significativa de falha no resultado final. Exemplo: um processo de 10 etapas, cada uma com 99% de sucesso individual (excelente isoladamente), tem só ~90,4% de chance de todas darem certo (0,99¹⁰). Com 20 etapas, ~81,8%; com 50 etapas, ~60% ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]). Entender que a falha é composta, não binária, é o que justifica investir em harness em vez de só trocar de modelo quando algo dá errado.

### Quatro Formas de Atacar Erros Compostos

1. **Mecanismos de verificação** — dar ao agente uma forma de checar o próprio trabalho antes de avançar para o próximo passo. O criador do Claude Code é citado como tendo documentado ganho de qualidade de **2 a 3 vezes** só com isso — não trocando de modelo. Componente com o maior retorno comprovado.
2. **Checkpoints** — pontos definidos onde um humano ou sistema automatizado verifica antes do agente continuar; reduz a propagação do erro. Equivalente ao padrão HITL — ver [[wiki/concepts/human-in-the-loop]].
3. **Ferramentas corretas** — menos ambiguidade por etapa, menos chance de erro. Contraintuitivo: mais ferramentas **não** significa menos erro (ver caso Vercel abaixo).
4. **Contexto limpo** — quanto menos ruído no contexto, menor a chance do agente interpretar mal o estado atual. Ver [[wiki/concepts/context-engineering-harness]].

### Caso Vercel: Menos Ferramentas, Mais Performance

A Vercel testou internamente um agente com muitas ferramentas disponíveis e performance ruim. Em vez de adicionar mais ferramentas (a decisão intuitiva), **removeu 80% das ferramentas disponíveis** — a performance melhorou, porque cada etapa passou a exigir escolher entre menos opções, reduzindo o espaço de decisão e a chance de escolha errada ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]). O caso é consistente com o anti-padrão "Tool Overload/God Agent" — agentes com 50+ ferramentas ficam confusos ou lentos, e a solução documentada é reduzir ou selecionar por embedding, não acumular. **Conclusão:** harness não é sobre maximizar capacidade, é sobre otimizar o caminho até o resultado certo.

## Doze Componentes do Harness (Sete Documentados)

Enumeração parcial de componentes de harness, sete cobertos numa fonte que cita a existência de doze no total (os outros cinco não foram nomeados — ver open question na fonte):

1. **System prompt** — não é o "você é um assistente útil" genérico; é o caráter, os limites e as convenções do agente, o que nunca fazer. A "constituição" do agente.
2. **Ferramentas** — o que o agente pode fazer; menos ferramentas bem escolhidas supera todas as ferramentas possíveis (ver caso Vercel acima).
3. **Gestão de contexto** — o que o agente tem acesso, limite da janela, o que incluir/descartar. Decisão de engenharia, não do modelo — ver [[wiki/concepts/context-engineering-harness]].
4. **Mecanismos de verificação** — como o agente checa se o que fez está correto antes de avançar. Ver [[wiki/concepts/rubrica-de-verificacao]].
5. **Memória** — o que persiste entre sessões; sem memória o agente recomeça do zero a cada rodada.
6. **Sandboxes** — ambiente isolado para executar código/testar outputs/chamar APIs sem afetar produção. Ver [[wiki/concepts/agent-containment]].
7. **Hooks** — pontos definidos em que um humano ou sistema automatizado intervém; não é o agente decidindo quando escalar, é o harness definindo isso explicitamente. Ver [[wiki/concepts/hooks-agente]].

Dado de benchmark citado (sem número específico): o mesmo Claude Opus performa significativamente melhor dentro do harness do Claude Code do que em benchmark padrão sem harness — mesmo modelo, harness diferente, resultado diferente ([[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]]).

### Mais Quatro Componentes Nomeados (Onze de Doze)

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] descreve, sem se referir à contagem "doze componentes" acima, quatro peças adicionais de um agent run que preenchem parte da lacuna dos "cinco não nomeados":

8. **Assemble de contexto como RAG explícito** — a montagem do contexto antes de cada chamada ao modelo (rules + skills + memória) é descrita como um RAG de fato: dados em banco vetorial, markdown (a parte procedural) e SQL, com retrieval do que é relevante para aquela inferência. Sobrepõe-se parcialmente ao item 3 (gestão de contexto) e ao item 5 (memória) acima, mas nomeia o mecanismo de retrieval explicitamente.
9. **Agent loop com limites explícitos** — não só o ciclo reasoning→tool call→resultado ([[wiki/concepts/ciclo-agente]]), mas quem impõe o teto: número máximo de tool calls, timeout por tool, fail checks — para o ciclo não entrar em loop infinito de pedir mais informação antes de finalizar.
10. **Guardrails** — filtros de segurança e formato aplicados tanto ao input do usuário quanto ao output da tool (que pode ser maliciosa) e ao output final do modelo; inclui policy check de segurança/ética. Ver [[wiki/concepts/ai-safety-guardrails]].
11. **Observabilidade com retries e evals** — camada menos universal entre as ferramentas comerciais (mais comum em agentes customizados, ex. sobre OpenClaw): logs de falha, custo por token, mecanismo de retry para tarefas que falharam em execução, e evals medindo a resposta contra o padrão de qualidade esperado — resumido pela fonte como "how we know it works". Ver [[wiki/concepts/llm-evals-testing]].

Com isso, permanece nomeado apenas um componente indeterminado do total de doze citado pela fonte original — os quatro acima cobrem boa parte, mas não fecham definitivamente a lista, já que a segunda fonte não referencia a contagem da primeira nem confirma que os itens se mapeiam 1:1.

## Harnesses com Learning Loop Embutido (Hermes Agent, Open Claw)

[[wiki/sources/hermes-agent-open-claw-learning-loop]] descreve uma nova geração de harness que embute um [[wiki/concepts/closed-loop-skill-learning|closed-loop skill learning system]] — o harness não só executa tool calls, mas extrai padrões do histórico de execuções e gera/refina skills sozinho, sobre uma [[wiki/concepts/agent-memory-tres-camadas|memória em três camadas]]. Exemplos citados: [[wiki/entities/hermes-agent]] e [[wiki/entities/open-claw]] (ambos open source/MIT), e o "Dreaming in Claude" da Anthropic como resposta proprietária ao mesmo padrão. Isso desloca parte do trabalho antes feito manualmente com [[wiki/concepts/hooks-agente]] (extrair padrões de sessões passadas) para dentro do próprio ciclo do harness.

## Harness Mínima em Código: o Esqueleto por Trás de Claude Code e Codex

[[wiki/sources/harness-explicado-function-calling-hag-evals]] demonstra ao vivo que uma harness funcional cabe num único arquivo Python: chave de API, system prompt, uma lista de tools (uma única tool `run`/bash é suficiente para o modelo interagir com o filesystem local) e um loop `while True` que alterna entre resposta do usuário e do modelo — enquanto houver `function_call` pendente, o script executa a tool localmente e reenvia o resultado ao contexto, até o modelo devolver um `output_text` final. É o mesmo mecanismo por trás de Claude Code e Codex, só que sem as camadas de rules/skills/MCP/worktrees que as ferramentas comerciais empilham em cima. A mesma fonte relata que, antes do function calling nativo existir em todo provider (inclusive Anthropic), o workaround usado era pedir ao modelo que sinalizasse chamadas de função via tags XML no texto — funcionava ~99% das vezes, com retry cobrindo o restante.

Essa mesma fonte também traz um exemplo concreto de "user harness" anterior à popularização do próprio termo "harness": um sistema RAG corporativo (chunking → vector database → busca KNN/BM25 → prompt restrito aos documentos recuperados → avaliação de fidelidade por outra IA, no estilo Evals da OpenAI) construído numa empresa antes do vocabulário atual existir — reforça que "harness" nomeia uma prática de engenharia (código determinístico + prompts + avaliação sistemática) que já existia informalmente.

## Harness como Multiplicador Oculto de Custo

[[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] oferece uma explicação concreta para um paradoxo de custo: o preço por token caiu continuamente desde 2022 e a qualidade dos modelos subiu, mas o gasto total sobe mesmo assim — porque a orquestração de agentes (o harness por trás) multiplica o consumo por tarefa "dezenas de vezes" frente ao uso direto do modelo. A fonte cita, como anedota (confiança baixa, sem link/benchmark), devs trocando de [[wiki/entities/claude-code]] para [[wiki/entities/opencode]] alegando que o primeiro entra em loops de correção supérflua (bug suspeito → sugestão de correção → reescreve testes → reescreve código → reescreve testes de novo) sem ganho de valor proporcional ao token gasto — o mesmo padrão que [[wiki/concepts/token-maxing]] descreve como "scripts descartáveis" incentivados por métricas de volume de token.

## Resumo Reaplicado em Fonte de Graph Engineering: "O Harness é o Carro, o Looping é o Piloto Automático"

[[wiki/sources/graph-engineering-matematica-do-erro-composto]] reabre esta definição ao recapitular o vídeo anterior do mesmo autor antes de introduzir grafo: harness é tudo que não é o modelo (ferramentas, contexto, verificação); o modelo é o motor; harness é o resto do carro. Sem claim novo sobre harness em si — a contribuição desta fonte é estender o argumento adiante, para [[wiki/concepts/grafo-como-abstracao-de-agentes|grafo]] e [[wiki/concepts/loop-engineering|loop]].

## Nomenclatura de Memória do Assemble de Contexto: User / Episodic / Semantic / Procedural

[[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] nomeia quatro tipos de memória agregados durante o assemble de contexto de um agent run: **user memory** (fatos duráveis sobre o usuário — preferências, quem é), **episodic memory** (linha do tempo de descobertas já feitas na conversa atual, relevante porque análises anteriores informam a próxima inferência), **semantic memory** (fatos gerais sobre usuário/projeto — ex. "é engenheira de software, está construindo uma startup"), e **procedural memory** (os arquivos markdown/playbooks configurados na máquina, no projeto e na ferramenta). Nomenclatura paralela, mas não idêntica, à [[wiki/concepts/agent-memory-tres-camadas|memória em três camadas]] (sessão/persistente/skill) já documentada na wiki — a peça nova frente ao que já existia é distinguir episodic de semantic explicitamente, algo que a fonte de três camadas não fazia.

## Complexidade Crescente como Justificativa de Investir em Harness (Ligação com Clean Architecture)

[[wiki/sources/prompt-context-harness-engineering-tres-pilares]] amarra explicitamente o gráfico de complexidade-versus-tempo de [[wiki/entities/uncle-bob|Robert Martin]] (Clean Architecture) à motivação de harness engineering: complexidade de software cresce com o tempo independente de haver IA envolvida — múltiplas pessoas passam pelo projeto, código se acumula. O harness (regras, guidelines, mecanismos de verificação) é apresentado como o equivalente, na era de agentes, a "ter uma boa arquitetura" — o jeito de manter essa complexidade crescente sob controle. Reforça, sem contradizer, a dicotomia já registrada acima entre provider harness e user harness, e a mesma metáfora "cérebro sem mãos" para a LLM isolada. A mesma fonte também restaura, em tradução livre para o português e sem atribuição de autoria, o mantra de [[wiki/entities/peter-steinberger]] ("se você não é o modelo, você é o harness").

## Key Sources

- [[wiki/sources/prompt-context-harness-engineering-tres-pilares]] — gráfico de complexidade de Robert Martin/Clean Architecture como justificativa de harness; mantra de Peter Steinberger restaurado em português sem atribuição; evolução prompt→context→harness engineering narrada como resposta ao crescimento da janela de contexto (4k tokens em 2022 → 1M hoje)
- [[wiki/sources/harness-anatomia-tecnica-alem-do-claude-md]] — gradiente de controle por ferramenta (OpenClaw > Codex/Claude Code > Cursor); quatro componentes adicionais nomeados (RAG de contexto, agent loop com limites, guardrails, observabilidade com retries/evals); claim não verificado de Claude Code open source pós-vazamento; nomenclatura user/episodic/semantic/procedural memory
- [[wiki/sources/graph-engineering-matematica-do-erro-composto]] — recapitulação da definição (harness = carro, loop = piloto automático) como ponte para graph engineering
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — harness como multiplicador de custo mesmo com preço por token em queda; troca de Claude Code para OpenCode por loops de correção supérflua
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
- [[wiki/sources/loop-engineering-planner-critic-grafo]] — propõe loop engineering como degrau seguinte a harness engineering
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — execução local de tool calls como o risco que motiva contenção/sandboxing do processo do harness
- [[wiki/sources/impacto-ia-mercado-frontend]] — harness próprio (skills, agente de code review a partir de causas de incidente) como requisito de contratação em frontend, não só prática de produtividade
- [[wiki/sources/hermes-agent-open-claw-learning-loop]] — harness com closed-loop skill learning embutido (Hermes Agent, Open Claw)
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — a própria linguagem como harness (Rust vs. Zig na migração do Ban: compilador memory-safe como sensor objetivo); harness fraco em testes e2e removidos fez erros se acumularem num loop criador
- [[wiki/sources/loop-engineering-harness-e-a-frase-que-viralizou]] — corrige a leitura "loop engineering matou harness engineering": o loop contém o harness, não o substitui; três fatores que tornaram loops longos viáveis em 2026 (modelo, harness, estado persistente)
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — matemática de erros compostos (99%ⁿ), quatro mecanismos de mitigação (verificação, checkpoints, ferramentas, contexto limpo), caso Vercel (remoção de 80% das ferramentas), doze componentes do harness (sete documentados)
- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]] — a harness executa comandos de shell nativos (`cat`, `echo`, `grep`, `sed`) na máquina do usuário e envia o output ao servidor da Anthropic; "puro suco da harness"
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — qualidade de compactação de contexto do Codex como diferencial do harness no comando `/go`; stop hook como ponto de extensão determinístico para o padrão judge
- [[wiki/sources/harness-explicado-function-calling-hag-evals]] — harness mínima em ~1 arquivo Python (system prompt + 1 tool + loop while true) como esqueleto didático do mecanismo por trás de Claude Code/Codex; workaround via tags XML antes do function calling nativo existir em todo provider; sistema RAG corporativo pré-termo "harness" como exemplo de "user harness" informal
