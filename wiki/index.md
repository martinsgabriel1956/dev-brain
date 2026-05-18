---
type: index
date_updated: 2026-05-17
---

# Wiki Index

## Sources

| Página | TL;DR |
|---|---|
| [[wiki/sources/chain-of-thought-prompting]] | CoT prompting (Wei et al., 2022) — passos intermediários como exemplares few-shot é uma capacidade emergente de ~100B+ parâmetros; supera GPT-3 fine-tuned no GSM8K via prompting apenas |
| [[wiki/sources/microsoft-prompt-engineering-guide]] | Quatro padrões de prompt engineering (Tell/Show/Describe/Remind) + Software 3.0 — guia prático da Microsoft para obter boas completions do Codex/GPT |
| [[wiki/sources/gpt3-language-models-are-few-shot-learners]] | GPT-3 (175B) formaliza in-context learning — aprender tarefas via exemplos no prompt sem atualizar pesos; few-shot rivaliza com fine-tuned SOTA em vários benchmarks |
| [[wiki/sources/logica-de-programacao-quatro-passos]] | Quatro passos para transformar qualquer problema em código: entender, decompor, criar fluxo, traduzir |
| [[wiki/sources/akita-como-aprender-programacao]] | Autodidatas avançam independente do material; copie código por centenas de horas; DSA é a fundação inegociável; Design Patterns são para depois |
| [[wiki/sources/trd-technical-requirements-document]] | TRD traduz PRD em especificação técnica — contratos, NFRs, segurança; distinto de RFC (proposta aberta) e ADR (decisão registrada) |
| [[wiki/sources/architecture-decision-record]] | ADR captura decisões arquiteturais — imutável, datado, versionado com o código; RFC propõe, ADR registra |
| [[wiki/sources/request-for-comments]] | RFC propõe mudanças grandes demais para decidir em silêncio — coleta objeções antes de implementar; RFC aceito gera ADR |
| [[wiki/sources/prd]] | PRD é o artefato de alinhamento estratégico — "por quê" e "o quê" sem entrar em implementação; antecede FRD e TRD |
| [[wiki/sources/frd]] | FRD detalha fluxos funcionais e regras de negócio — derivado do PRD, base para QA e engenharia |
| [[wiki/sources/user-stories]] | User Stories são a unidade mínima de valor em contextos ágeis — Como/Quero/Para + critérios Given/When/Then |
| [[wiki/sources/high-level-design]] | HLD alinha times sobre direção do sistema antes do código — serviços, integrações e fluxo de dados |
| [[wiki/sources/low-level-design]] | LLD remove ambiguidade antes de codificar — schemas, contratos de API, estrutura de classes, sequência de chamadas |
| [[wiki/sources/runbook]] | Runbook é procedimento linear para operações repetíveis — elimina variação humana, reduz MTTR |
| [[wiki/sources/playbook]] | Playbook é árvore de decisão para incidentes com causa desconhecida — guia investigação sob pressão |
| [[wiki/sources/post-mortem]] | Post-mortem blameless analisa incidentes após resolução — 5 Porquês até causa sistêmica, action items com dono e prazo |

## Concepts

### LLMs e IA

| Página | Hook |
|---|---|
| [[wiki/concepts/prompt-engineering]] | Construção sistemática de prompts para elicitar outputs de LLMs — primeira alavanca, barata e iterável |
| [[wiki/concepts/completion]] | Texto gerado pelo modelo em resposta a um prompt — gerado token a token por modelo autoregressivo |
| [[wiki/concepts/zero-shot-learning]] | Prompt sem exemplos — só instrução; ponto de partida antes de escalar para few-shot |
| [[wiki/concepts/chain-of-thought]] | Forçar raciocínio passo a passo no prompt — melhora performance em tarefas de lógica e matemática |
| [[wiki/concepts/context-window]] | Limite máximo de tokens (prompt + completion) por chamada — restrição central de prompt engineering |
| [[wiki/concepts/hyperparameters-llm]] | Temperature, max_tokens, stop sequence — controlam como o modelo amostra tokens durante a geração |
| [[wiki/concepts/software-3]] | Terceira geração de programação (Karpathy) — lógica especificada em linguagem natural via prompts |
| [[wiki/concepts/in-context-learning]] | Aprender tarefas via exemplos no prompt, sem gradient descent — capacidade emergente de LLMs grandes |
| [[wiki/concepts/few-shot-learning]] | Variante de ICL com 10–100 exemplos; sweet spot prático é 3–5; supera fine-tuned SOTA em vários benchmarks |
| [[wiki/concepts/scaling-laws]] | Performance de LLMs segue power law em parâmetros, dados e compute — previsível e smooth |
| [[wiki/concepts/data-contamination]] | Sobreposição entre dados de treino e benchmarks de teste — problema crescente em modelos treinados em web-scale data |
| [[wiki/concepts/foundation-model]] | Modelo pré-treinado em larga escala que serve de base para downstream tasks via ICL, fine-tuning ou prompting |
| [[wiki/concepts/autoregressive-language-model]] | Arquitetura decoder-only que gera token a token — base do GPT-3 e da maioria dos LLMs modernos |
| [[wiki/concepts/fine-tuning]] | Continuar treinamento num dataset específico de tarefa — alternativa mais custosa ao ICL |
| [[wiki/concepts/emergent-ability]] | Capacidade que não existe em modelos pequenos e aparece abruptamente acima de certo limiar de escala — CoT é o exemplo canônico |

### Fundamentos de Lógica e Programação

| Página | Hook |
|---|---|
| [[wiki/concepts/logica-de-programacao]] | Raciocínio por trás das decisões que o sistema precisa tomar |
| [[wiki/concepts/decomposicao-de-problemas]] | Quebrar problemas complexos em subproblemas menores e independentes |
| [[wiki/concepts/separacao-de-responsabilidades]] | Cada módulo cuida de uma coisa só |
| [[wiki/concepts/fluxo-logico]] | Mapa de decisões desenhado antes de abrir o editor |
| [[wiki/concepts/fluxo-de-controle]] | if/while/for — materialização do fluxo lógico em código |
| [[wiki/concepts/traducao-logica-para-codigo]] | Código como tradução de decisões já tomadas, não criação |
| [[wiki/concepts/estado]] | O que o sistema precisa lembrar para tomar decisões |
| [[wiki/concepts/caminho-feliz]] | Fluxo ideal em que tudo ocorre conforme esperado |
| [[wiki/concepts/edge-case]] | Cenários fora do fluxo principal que precisam ser tratados explicitamente |
| [[wiki/concepts/algoritmos-e-estruturas-de-dados]] | A fundação que separa amadores de profissionais — DSA antes de qualquer framework |

### Aprendizado e Mentalidade

| Página | Hook |
|---|---|
| [[wiki/concepts/autodidata]] | Quem investiga o porquê quando o procedimento falha, em vez de travar |
| [[wiki/concepts/hacker-mindset]] | Curiosidade ativa — não só faz a pergunta, mas procura a resposta |
| [[wiki/concepts/aprendizado-por-exposicao]] | Copiar código sem objetivo por centenas de horas para formar fluência |
| [[wiki/concepts/memoria-muscular]] | Familiaridade instintiva com código formada pela repetição, pré-analítica |
| [[wiki/concepts/fluencia-vs-perfeicao]] | Fluência é operar mesmo errando — perfeição no início bloqueia o aprendizado |
| [[wiki/concepts/foco-profundo]] | Estado de concentração ininterrupta incompatível com redes sociais |
| [[wiki/concepts/fundacao-tecnica]] | Multiplicador de aprendizado — torna qualquer nova tecnologia simples |

### Padrões e Design

| Página | Hook |
|---|---|
| [[wiki/concepts/pattern-recognition]] | Capacidade humana de detectar repetições — base do aprendizado por exposição |
| [[wiki/concepts/design-patterns]] | Catálogo de soluções nomeadas — útil só depois de já ter visto os padrões na prática |
| [[wiki/concepts/anti-pattern]] | Repetição que parece solução mas cria problemas — frequência não implica qualidade |

## Entities

| Página | Hook |
|---|---|
| [[wiki/entities/openai]] | Organização responsável pelo GPT-3/4 — formalizou in-context learning e scaling laws |
| [[wiki/entities/jason-wei]] | Pesquisador Google Brain — lead author do paper de chain-of-thought prompting e do paper de emergent abilities |
| [[wiki/entities/fabio-akita]] | Programador brasileiro, autodidata desde 1991, criador do canal Akita On Rails |
| [[wiki/entities/christopher-alexander]] | Arquiteto que criou a linguagem de patterns original — inspiração para o GoF |

### Documentação de Arquitetura

| Página | Hook |
|---|---|
| [[wiki/concepts/trd-technical-requirements-document]] | Especificação técnica completa — o "como" entre PRD e código |
| [[wiki/concepts/prd-product-requirements-document]] | O "o quê" do produto — antecede o TRD |
| [[wiki/concepts/brd-business-requirements-document]] | O "o quê" do negócio — antecede o PRD |
| [[wiki/concepts/rfc-request-for-comments]] | Proposta aberta buscando feedback antes da decisão |
| [[wiki/concepts/adr-architecture-decision-record]] | Registro histórico de decisão arquitetural já tomada |
| [[wiki/concepts/frd-functional-requirements-document]] | Contrato funcional entre produto e engenharia — fluxos, regras de negócio, tratamento de erro |
| [[wiki/concepts/user-stories]] | Unidade mínima de valor ágil — Como/Quero/Para + critérios Given/When/Then |
| [[wiki/concepts/high-level-design]] | Primeira camada de documentação arquitetural — serviços, integrações, fluxo de dados |
| [[wiki/concepts/low-level-design]] | Zoom dentro de um componente — schemas, contratos, estrutura de classes, sequência de chamadas |

### Documentação Operacional

| Página | Hook |
|---|---|
| [[wiki/concepts/runbook]] | Passos lineares para operações repetíveis — elimina variação humana, reduz MTTR |
| [[wiki/concepts/playbook]] | Árvore de decisão para incidentes com causa desconhecida |
| [[wiki/concepts/post-mortem]] | Análise retrospectiva blameless — 5 Porquês até causa sistêmica, action items com dono e prazo |

## Questions

_(vazio)_
