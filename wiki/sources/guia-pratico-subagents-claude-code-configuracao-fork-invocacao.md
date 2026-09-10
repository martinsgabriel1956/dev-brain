---
type: source
title: "Guia Prático de Subagents no Claude Code — Configuração, Fork e as 3 Formas de Invocação"
aliases: ["guia pratico subagents", "como configurar subagent claude code", "claude --agent"]
date_created: 2026-09-10
date_updated: 2026-09-10
source_count: 0
tags: [subagentes, claude-code, fork, permission-mode, anthropic, harness, configuracao-de-agente]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/guia-pratico-subagents-claude-code-configuracao-fork-invocacao.md
source_url: ""
author: "desconhecido (canal com cursos próprios e workshop/bootcamp de IA em produção com um sócio; patrocínio UVP)"
date_published: "desconhecida"
date_ingested: 2026-09-10
---

# Guia Prático de Subagents no Claude Code — Configuração, Fork e as 3 Formas de Invocação

## TL;DR

Tutorial prático (com patrocínio da UVP) sobre [[wiki/concepts/subagentes]] no [[wiki/entities/claude-code]]: distingue **fork** (`/fork`, clona toda a conversa do main agent para um background agent) de **subagent** (não herda a conversa, roda com janela própria), lista as **três formas de invocar** um subagent (linguagem natural, menção explícita `@nome-do-agent`, e `claude --agent <nome>` fora da sessão), e detalha os campos de configuração de um subagent customizado em `.claude/agents/*.md`: `tools`, `model`, `permission mode` (`default`, `acceptEdits`, `dontAsk`/`deny`, `bypassPermissions`, `plan`), `isolation`/worktree, `max turns`, `skills` (pré-injeção ou bloqueio via `disallowedTools`), três tipos de `memory` (user, projeto, local) e `background`. Fecha com uma opinião pessoal cética sobre paralelismo massivo: o valor do subagent estaria mais no **isolamento de contexto para uma tarefa bem definida** do que em rodar dezenas em paralelo.

---

## Key Claims

1. **Fork (`/fork`) clona toda a conversa do main agent para um background agent; subagent não herda a conversa por padrão.** É a distinção central levantada logo no início: "um subagent não é uma duplicação da sua conversa no main agent" — para duplicar de fato (todo o contexto, toda a conversa), o comando é `/fork`. Confidence: alta — demonstrado ao vivo na sessão do autor. Nota: a fonte também menciona que `/agent` foi removido do Claude Code, então a via de invocação atual passa pelas três formas abaixo, não por um comando `/agent` direto.

2. **Três formas de invocar um subagent:**
   - **Linguagem natural** — pedir diretamente ("inicie um novo subagent que vai trocar a paleta de cores para pastel"); o Claude Code carrega a skill relevante, prepara a tarefa e instancia um agente **General Purpose** em background.
   - **Menção explícita `@nome-do-agent`** — exige que o subagent já tenha sido criado (manualmente ou pedindo ao Claude para criar); autocomplete lista os agentes disponíveis ao digitar `@`.
   - **`claude --agent <nome>`** fora da sessão atual — inicia uma sessão inteira do Claude Code já dentro daquele agente customizado, com seu contexto e modo de operação.

   Confidence: alta — as três vias foram demonstradas na tela.

3. **O agente General Purpose pré-instalado herda o modelo da conversa principal.** Se a conversa principal está no Fable, o subagent genérico também roda no Fable — diferente de um subagent customizado, que pode fixar um modelo próprio. Confidence: alta.

4. **Campos de configuração de um subagent customizado (`.claude/agents/*.md`), além de `tools` e `model` (já registrados em [[wiki/concepts/subagentes]]):**
   - **`permission mode`** — `default`; `acceptEdits` (autoaceita edição de arquivos, recomendação do autor para subagents); `dontAsk`/`deny` (nega automaticamente o que não está explicitamente permitido); `bypassPermissions` (pula todas as permissões — só recomendado dentro de VM/dev container, pelo risco de rodar em paralelo sem controle); `plan`.
   - **`isolation`** — rodar o subagent numa worktree isolada, evitando conflito de arquivo com outros agentes em paralelo. Conecta diretamente com [[wiki/concepts/worktree-paralelismo]].
   - **`max turns`** — limite de round trips de tool call; o autor não vê necessidade prática de configurar isso na maioria dos casos.
   - **`skills`** — controla quais skills entram pré-injetadas no contexto do subagent. Comportamento padrão (campo vazio): o subagent descobre skills disponíveis via tool call de skill, igual ao mecanismo geral já documentado em [[wiki/concepts/skills-agente]]. É possível pré-injetar explicitamente, ou bloquear o acesso via `disallowedTools` negando a ferramenta de skill — o autor não identifica caso de uso claro para bloquear.
   - **`memory`** — três tipos de memória persistente do subagent: **user** (aprendizados válidos em todos os projetos do usuário), **projeto** (aprendizados específicos deste projeto, só útil se a auto memory do projeto estiver ativa) e **local** (não versionada em Git, privada da máquina) — em contraste com uma memória de projeto compartilhada via Git com toda a equipe.
   - **`background`** — se o subagent roda em background ou não; o autor considera isso, em geral, desejável.
   
   Confidence: alta — todos os campos foram mostrados na documentação/UI do Claude Code durante a gravação.

5. **Opinião do autor: o ganho do subagent está no isolamento de contexto, não no paralelismo massivo.** Argumenta que trabalho massivamente paralelo reduz a atenção do desenvolvedor ao que está sendo feito, e que a velocidade de geração de código das IAs já é alta o suficiente para que paralelizar tudo não seja o gargalo real. Recomenda subagent para: (a) uma subtarefa bem definida, com entry point e critério de aceitação claros, extraída de uma tarefa maior já quebrada; (b) code review, porque o revisor não carrega o contexto de quem escreveu o código. Fora desses dois casos, o autor diz que não abusaria da ferramenta. Confidence: opinião pessoal explícita, não um dado de benchmark — o autor contrasta com [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]], que chega a uma recomendação semelhante (evitar granularidade excessiva) só que a partir de números medidos, não de intuição.

6. **Anedota de escala: até 14 subagents em paralelo "sem problema", desde que a tarefa seja decomponível em pedaços paralelizáveis.** Confidence: média — número citado sem detalhar a tarefa, o tempo total ou o custo em tokens dessa execução específica; não é um benchmark controlado como o de [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]].

7. **Teste-e-veja: configurar todos os campos com cuidado vs. não configurar nada e deixar o Claude Code decidir "deu resultado final parecido" nos testes do autor.** Confidence: baixa — auto-relato sem metodologia, comparável em tom (mas não em rigor) à conclusão de granularidade de [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]]; vale tratar como opinião de prática pessoal, não como dado a ser citado como fato estabelecido.

---

## Entidades e Conceitos Tocados

- [[wiki/entities/claude-code]] — comandos `/fork`, `claude --agent`, `.claude/agents/*.md`
- [[wiki/entities/anthropic]] — criadora do padrão de subagentes e do Claude Code
- [[wiki/concepts/subagentes]] — conceito central; esta fonte adiciona os campos de configuração não cobertos anteriormente (`permission mode`, `isolation`, `max turns`, `skills`, `memory`, `background`) e as três formas de invocação
- [[wiki/concepts/worktree-paralelismo]] — campo `isolation` do subagent liga diretamente a esse conceito
- [[wiki/concepts/skills-agente]] — mecanismo de descoberta automática de skills por um subagent, e a opção de pré-injetar ou bloquear via `disallowedTools`
- [[wiki/concepts/ciclo-agente]] — subagent como forma de isolar um ciclo de vida curto dentro do ciclo do agente pai

---

## Contradições / Reforços com o Resto da Wiki

**Reforço parcial, tom mais cauteloso:** [[wiki/concepts/subagentes]] já documentava, a partir de [[wiki/sources/subagentes-quando-vale-a-pena-custo-velocidade-tlc-spec-driven]], que granularidade excessiva de subagentes piora tempo, custo e qualidade simultaneamente, com um "sweet spot" de agrupamento coeso. Esta fonte chega a uma recomendação de mesma direção (não abusar de subagents, preferir tarefas bem definidas e delimitadas) mas por via de opinião pessoal do autor, sem benchmark — vale citar separadamente das conclusões numéricas já registradas, marcando o grau de confiança diferente.

**Dado novo, não contradiz nada:** as três formas de invocação (linguagem natural, `@nome`, `claude --agent`) e os campos `permission mode`/`isolation`/`max turns`/`skills`/`memory`/`background` não estavam detalhados em nenhuma fonte anterior da wiki sobre subagentes — [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]] cobria `model` e `tools`, mas não esses outros campos.

**Observação não resolvida:** a fonte afirma que `/agent` foi removido do Claude Code, mas não detalha desde quando nem se há um changelog oficial citado — não verificado contra documentação primária da Anthropic.

---

## Open Questions

- **Removal de `/agent` não confirmado contra changelog oficial** — a fonte apenas observa o fato na própria UI ("note que o agent aqui foi removido"), sem indicar versão ou data.
- **Sem detalhe sobre `plan` como permission mode de subagent** — a fonte lista o modo mas não demonstra seu efeito específico num subagent (só explica os outros quatro modos).
- **Diferença entre `disallowedTools` bloqueando skill e simplesmente não pré-injetar nenhuma skill não é totalmente clara** — o autor reconhece não saber por que alguém bloquearia explicitamente, sugerindo que o comportamento default (descoberta automática) já cobre a maioria dos casos.

## Raw Quotes

> "Um subagent não é uma duplicação da sua conversa no main agent... isso aqui a gente vai chamar de fork."

> "Uma das grandes vantagens de ter um subagent é você criar um subagent que vai utilizar um modelo diferente do seu main agent."

> "Eu acho que a vantagem do subagent acaba sendo mais o isolamento do que o paralelismo massivo."

> "Se você configurar tudo aqui com maior cuidado, fazer tudo certinho, ou então se você não configurar absolutamente nada e só pedir pro Claude Code, o resultado final na minha visão é bem parecido."
