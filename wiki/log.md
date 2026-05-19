# Wiki Log

---

## [2026-05-19] ingest | Soft Skills que Realmente Fazem Diferença na Carreira em Tecnologia

**Source:** [[wiki/sources/soft-skills-carreira-tecnologia-eduarda]]
**Skill:** tech-mentor-leadership (`references/career-progression.md`)

**Páginas criadas:**
- `wiki/sources/soft-skills-carreira-tecnologia-eduarda.md`
- `wiki/concepts/soft-skills.md`
- `wiki/concepts/colaboracao-times.md`
- `wiki/concepts/autonomia-responsabilidade.md`
- `wiki/concepts/pensamento-critico.md`
- `wiki/concepts/aprendizado-continuo.md`
- `wiki/concepts/adaptabilidade.md`
- `wiki/concepts/inteligencia-emocional.md`
- `wiki/entities/eduarda-rocket-city.md`

**Páginas atualizadas:**
- `wiki/concepts/comunicacao-tecnica.md` — +1 fonte (página já existia de ingest anterior); backlink adicionado
- `wiki/concepts/burnout-dev.md` — +1 fonte; inteligência emocional como proteção contra burnout
- `wiki/concepts/autodidata.md` — +1 fonte; conexão com aprendizado-continuo

**Notas:** Fonte é transcrição de vídeo do canal Rocket City. Argumento central: hard skills são o piso mínimo, soft skills são o multiplicador. As seis alavancas — comunicação, colaboração, autonomia, pensamento crítico, aprendizado contínuo e inteligência emocional/adaptabilidade — separam executor de solucionador e determinam quem constrói cultura vs. quem apenas entrega código. Conexão importante com wiki existente: aprendizado contínuo é a versão carreira do autodidata (Akita); inteligência emocional é a defesa direta contra burnout (token anxiety). Questões em aberto: soft skills são treináveis deliberadamente? Como medi-las? Em contextos com agentes de IA, qual soft skill se torna mais crítica?

---

## [2026-05-18] ingest | Token Anxiety — Como os Agentes de IA Estão Mudando o Comportamento dos Devs

**Source:** [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
**Skill:** tech-mentor-ai (domínio: LLMs, agentes, LLMOps, comportamento)

**Páginas criadas:**
- `wiki/sources/token-anxiety-agentes-ia-comportamento-devs.md`
- `wiki/concepts/token-anxiety.md`
- `wiki/concepts/agente-ia.md`
- `wiki/concepts/janela-de-contexto.md`
- `wiki/concepts/fomo-tecnologico.md`
- `wiki/concepts/burnout-dev.md`
- `wiki/concepts/dopamina-produtividade.md`
- `wiki/concepts/llmops.md`
- `wiki/entities/nikon-cotaro.md`
- `wiki/entities/claude-code.md`

**Notas:** Fonte é transcrição de vídeo brasileiro comentando o artigo *Token Anxiety* de Nikon Cotaro (fev/2025). Argumento central: ferramentas de agentes com janela de tokens finita (ex.: Claude Code com reset 3–5h) estão criando um novo padrão de ansiedade que distorce comportamentos sociais, rotinas e prioridades de desenvolvedores. O fenômeno amplifica FOMO (mais capacidade = mais ansiedade, não menos) e torna a linha entre ownership saudável e burnout mais tênue para todos — não apenas seniores. Camada brasileira: dev que compete no mercado internacional sente urgência amplificada. Questões em aberto: o fenômeno chegou massivamente ao Brasil? Pricing diferenciado por horário é real? Como diferenciar operacionalmente ownership saudável de token anxiety patológica?

---

## [2026-05-17] ingest | Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

**Source:** [[wiki/sources/chain-of-thought-prompting]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md`)

**Páginas criadas:**
- `wiki/sources/chain-of-thought-prompting.md`
- `wiki/concepts/emergent-ability.md` (novo conceito)
- `wiki/entities/jason-wei.md` (nova entidade)

**Páginas atualizadas:**
- `wiki/concepts/chain-of-thought.md` — source_count 1→2, major update com resultados empíricos, ablações e condições de uso
- `wiki/concepts/few-shot-learning.md` — source_count 2→3, seção Few-Shot CoT adicionada
- `wiki/concepts/in-context-learning.md` — source_count 2→3, backlink adicionado
- `wiki/concepts/scaling-laws.md` — source_count 1→2, seção de limites expandida com emergent abilities
- `wiki/concepts/prompt-engineering.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/fine-tuning.md` — source_count 2→3, seção CoT vs Fine-Tuning adicionada

**Notas:** Paper seminal de Wei et al. (Google Brain, 2022). Argumento central: fornecer exemplares few-shot com passos de raciocínio intermediários (chain-of-thought) desbloqueia capacidades de raciocínio complexo em LLMs grandes — sem fine-tuning. Resultado mais impactante: PaLM 540B com 8 exemplares supera GPT-3 fine-tuned com verificador no GSM8K (~57% vs ~35%). Chain-of-thought é uma propriedade emergente que só aparece em modelos ~100B+. Questões em aberto: (1) o que exatamente no pré-treino causa a emergência do CoT nessa escala? (2) reasoning models (o1/o3/Claude extended thinking) internalizam CoT no treinamento — qual a relação com CoT prompting explícito? (3) CoT pode ser destilado para modelos menores via rationale distillation?

---

## [2026-05-17] ingest | Microsoft Prompt Engineering Guide

**Source:** [[wiki/sources/microsoft-prompt-engineering-guide]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md`)

**Páginas criadas:**
- `wiki/sources/microsoft-prompt-engineering-guide.md`
- `wiki/concepts/prompt-engineering.md`
- `wiki/concepts/completion.md`
- `wiki/concepts/zero-shot-learning.md`
- `wiki/concepts/chain-of-thought.md`
- `wiki/concepts/context-window.md`
- `wiki/concepts/hyperparameters-llm.md`
- `wiki/concepts/software-3.md`

**Páginas atualizadas:**
- `wiki/concepts/few-shot-learning.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/fine-tuning.md` — source_count 1→2, backlink adicionado
- `wiki/concepts/in-context-learning.md` — source_count 1→2, backlink adicionado
- `wiki/entities/openai.md` — source_count 1→2, Codex adicionado, backlink adicionado

**Notas:** Guia prático da Microsoft (2022) sobre prompt engineering com Codex. Argumento central: a qualidade das completions depende diretamente da construção do prompt. Quatro padrões: Tell It (instrução de alto nível), Show It (few-shot), Describe It (APIs desconhecidas), Remind It (histórico conversacional). Karpathy cunha "Software 3.0" — prompts como a terceira geração de programação. Questões em aberto: o guia foi escrito pré-reasoning models (o1/o3/Claude extended thinking) — como esses paradigmas se relacionam com CoT explícito? Com LoRA/QLoRA, a hierarquia "few-shot antes de fine-tuning" ainda se sustenta da mesma forma?

---

## [2026-05-17] ingest | Language Models are Few-Shot Learners (GPT-3)

**Source:** [[wiki/sources/gpt3-language-models-are-few-shot-learners]]
**Skill:** tech-mentor-ai (`references/ai/prompt-engineering.md` + `references/ai/fundamentals.md`)

**Páginas criadas:**
- `wiki/sources/gpt3-language-models-are-few-shot-learners.md`
- `wiki/concepts/in-context-learning.md`
- `wiki/concepts/few-shot-learning.md`
- `wiki/concepts/scaling-laws.md`
- `wiki/concepts/data-contamination.md`
- `wiki/concepts/foundation-model.md`
- `wiki/concepts/autoregressive-language-model.md`
- `wiki/concepts/fine-tuning.md`
- `wiki/entities/openai.md`

**Notas:** Paper seminal do GPT-3 (Brown et al., 2020). Argumento central: modelos maiores são meta-aprendizes melhores — aprendem tarefas via exemplos no contexto sem atualizar pesos (in-context learning). Few-shot sem fine-tuning supera SOTA fine-tuned em TriviaQA e PIQA. Questões em aberto: ICL é aprendizado genuíno ou recuperação de padrões do pré-treino? Até onde as scaling laws se sustentam? Como medir data contamination em modelos que não publicam dados de treino?

---

## [2026-05-17] ingest | Batch — Documentação Técnica e Operacional (10 fontes)

**Skills:** tech-mentor-system-design · tech-mentor-infra · tech-mentor-leadership

**Fontes ingeridas:**
- `raw/architecture-decision-record.md` → [[wiki/sources/architecture-decision-record]]
- `raw/request-for-comments.md` → [[wiki/sources/request-for-comments]]
- `raw/high-level-design.md` → [[wiki/sources/high-level-design]]
- `raw/low-level-design.md` → [[wiki/sources/low-level-design]]
- `raw/prd.md` → [[wiki/sources/prd]]
- `raw/frd.md` → [[wiki/sources/frd]]
- `raw/user-stories.md` → [[wiki/sources/user-stories]]
- `raw/runbook.md` → [[wiki/sources/runbook]]
- `raw/playbook.md` → [[wiki/sources/playbook]]
- `raw/post-mortem.md` → [[wiki/sources/post-mortem]]

**Páginas criadas:**
- `wiki/concepts/frd-functional-requirements-document.md`
- `wiki/concepts/high-level-design.md`
- `wiki/concepts/low-level-design.md`
- `wiki/concepts/playbook.md`
- `wiki/concepts/post-mortem.md`
- `wiki/concepts/user-stories.md`
- `wiki/concepts/runbook.md` (atualizado — +1 fonte, +seção pré-requisitos/rollback)

**Notas:** Batch de notas próprias do tech-mentor. Dois clusters principais: (1) documentação arquitetural e de produto — hierarquia PRD→FRD→TRD, HLD→LLD, RFC→ADR com papéis distintos e complementares; (2) documentação operacional — tríade runbook (execução)/playbook (investigação)/post-mortem (retrospectiva). Questão aberta: como o LLD se relaciona com o FRD em projetos onde produto e engenharia fazem as duas coisas?

---

## [2026-05-17] ingest | TRD — Technical Requirements Document

**Source:** [[wiki/sources/trd-technical-requirements-document]]
**Skill:** tech-mentor-system-design (`references/c4-adr.md`)

**Páginas criadas:**
- `wiki/sources/trd-technical-requirements-document.md`
- `wiki/concepts/trd-technical-requirements-document.md`
- `wiki/concepts/prd-product-requirements-document.md` (stub)
- `wiki/concepts/brd-business-requirements-document.md` (stub)
- `wiki/concepts/rfc-request-for-comments.md` (stub)
- `wiki/concepts/adr-architecture-decision-record.md` (stub)

**Notas:** Fonte é nota própria sobre documentação técnica. Argumento central: TRD é o elo entre produto e implementação — responde "como" depois que PRD respondeu "o quê". Conceito chave: distinção TRD (especificação) vs RFC (proposta aberta) vs ADR (decisão registrada). Nenhuma contradição com wiki existente. Questão aberta: quando o TRD se sobrepõe funcionalmente com o ADR em times menores?

**Nota:** `raw/akita-como-aprender-programacao.md` estava listado como untracked pelo git mas já foi ingerido em 2026-05-16 — sem re-ingest necessário.

---

## [2026-05-16] ingest | Como Aprender Programação — Fábio Akita

**Source:** [[wiki/sources/akita-como-aprender-programacao]]
**Skill:** tech-mentor-leadership (`references/technical-mentoring.md`)

**Páginas criadas:**
- `wiki/sources/akita-como-aprender-programacao.md`
- `wiki/concepts/autodidata.md`
- `wiki/concepts/aprendizado-por-exposicao.md`
- `wiki/concepts/memoria-muscular.md`
- `wiki/concepts/pattern-recognition.md`
- `wiki/concepts/anti-pattern.md`
- `wiki/concepts/design-patterns.md`
- `wiki/concepts/algoritmos-e-estruturas-de-dados.md`
- `wiki/concepts/fundacao-tecnica.md`
- `wiki/concepts/fluencia-vs-perfeicao.md`
- `wiki/concepts/hacker-mindset.md`
- `wiki/concepts/foco-profundo.md`
- `wiki/entities/fabio-akita.md`
- `wiki/entities/christopher-alexander.md`

**Notas:** Fonte é transcrição de vídeo do canal Akita On Rails. Argumento central: autodidata vs. passivo é a variável que determina quem aprende, não a qualidade do curso. Contradição potencial com wiki existente: nenhuma. Questão aberta: é possível desenvolver a postura autodidata deliberadamente, ou ela é formada na infância?

---

## [2026-05-13] ingest | Lógica de Programação: Como Qualquer Problema Vira Código

**Source:** [[wiki/sources/logica-de-programacao-quatro-passos]]
**Skill:** cs-fundamentals
**Páginas criadas:**
- `wiki/sources/logica-de-programacao-quatro-passos.md`
- `wiki/concepts/logica-de-programacao.md`
- `wiki/concepts/decomposicao-de-problemas.md`
- `wiki/concepts/separacao-de-responsabilidades.md`
- `wiki/concepts/fluxo-logico.md`
- `wiki/concepts/fluxo-de-controle.md`
- `wiki/concepts/traducao-logica-para-codigo.md`
- `wiki/concepts/estado.md`
- `wiki/concepts/caminho-feliz.md`
- `wiki/concepts/edge-case.md`

**Notas:** Vídeo introdutório de lógica de programação usando caixa eletrônico como exemplo central. Anuncia próxima fonte sobre estruturas de dados. Nenhuma contradição (wiki iniciado neste ingest).
