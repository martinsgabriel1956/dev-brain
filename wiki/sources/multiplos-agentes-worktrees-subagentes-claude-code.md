---
type: source
title: "Múltiplos Agentes no Claude Code — Work Trees e Subagentes"
aliases: ["multiplos agentes claude code", "worktrees vs subagentes", "claude --worktree"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [claude-code, worktree, subagentes, multi-agent, anthropic, paralelismo, context-engineering]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/multiplos-agentes-worktrees-subagentes-claude-code.md
source_url: ""
author: "HiperDev (live coding, canal de cortes)"
date_published: ""
date_ingested: 2026-07-03
---

# Múltiplos Agentes no Claude Code — Work Trees e Subagentes

## TL;DR

Transcrição de live coding explicando as duas formas nativas do [[wiki/entities/claude-code]] de rodar múltiplos agentes em paralelo: **work trees** (`claude --worktree`, paralelismo a nível de file system, cada agente numa cópia isolada do repositório) e **subagentes** (`.claude/agents/`, paralelismo a nível de janela de contexto, resultados convergem para uma única PR). Cobre como declarar subagentes (modelo e tools por agente), disparo automático vs. custom, e o problema de "parafernália" — excesso de skills/agentes sobrepostos confundindo o roteamento do próprio modelo.

---

## Claims Principais

### 1. Work trees isolam a nível de file system, não de contexto
**Evidência:** `claude --worktree <nome>` cria uma cópia física do repositório em `.claude/worktrees/<nome>`, apontando para um branch novo. Dois agentes podem editar o "mesmo" arquivo (mesmo path lógico) sem conflito, porque fisicamente são arquivos diferentes.
**Confidence:** Alta — demonstrado ao vivo com Finder/Cursor mostrando as duas pastas.
> "Apesar do agente 1 ter mexido no arquivo autenticação.tsx e o agente 2 também ter mexido no arquivo autenticação.tsx... a nível físico eles não são."

### 2. `claude --worktree` é wrapper nativo sobre `git worktree`
**Evidência:** Git worktree já existia antes; a Anthropic o tornou um fluxo de primeira classe dentro do Claude Code, evitando a criação manual (`git worktree add`).
**Confidence:** Alta.

### 3. Finalizar uma work tree exige encerramento explícito
**Evidência:** Recomendação de instruir isso no `CLAUDE.md` — senão os arquivos da cópia podem acabar sendo commitados (a menos que estejam no `.gitignore`). Fluxo completo: commit → encerrar worktree → abrir PR.
**Confidence:** Média — recomendação de prática, não uma trava do próprio Claude Code.

### 4. Subagentes são paralelismo a nível de contexto via tool `Task`/`Agent`
**Evidência:** Cada subagente roda como uma "thread"/processo com janela de contexto própria. Só o resultado final retorna para o agente pai — o raciocínio intermediário não entra no contexto principal.
**Confidence:** Alta.

### 5. Subagentes convergem em uma única PR; work trees geram PRs separadas
**Evidência:** Work trees = branches/PRs independentes (funcionalidades apartadas). Subagentes = trabalho consolidado pelo chat pai numa única síntese/PR.
**Confidence:** Alta — distinção central do vídeo.

### 6. Subagentes customizados aceitam `model` e `tools` restritos no front-matter
**Evidência:** Arquivo Markdown em `.claude/agents/*.md` com metatag de nome, descrição, cor e corpo de instrução — mesmo formato de uma skill, mas com campos extras. Exemplo: PM usa Opus, implementadores usam Sonnet, documentação usa Haiku; um "code reviewer" recebe só `Read`, `Grep`, `Glob`, `Bash` (sem `Write`/`Edit`), reduzindo o system prompt do subagente.
**Confidence:** Alta — mostrado no arquivo do agente.

### 7. Skills não aceitam `model`/`tools` customizados; subagentes sim
**Evidência:** Autor verificou ao vivo a documentação da Anthropic — skill é só um prompt reutilizável carregado dinamicamente; subagente tem "papel mais profundo" por rodar em paralelo com processo próprio.
**Confidence:** Média — checado ao vivo, mas vale confirmar contra doc oficial mais recente (ver [[wiki/concepts/skills-agente]]).

### 8. Excesso de skills/subagentes sobrepostos confunde o roteamento automático
**Evidência:** Autor relata ter ~300 skills baixadas de repositórios públicos (ex. "awesome claude skills"), gerando subagentes duplicados e overlap de responsabilidade. Resultado: ao pedir uma tarefa de segurança esperando o subagente "CTO", o Claude acionou primeiro uma skill de "security review" em vez do subagente esperado.
**Confidence:** Alta — observado ao vivo como falha de roteamento.
> "Tem uma skill que faz aquela tarefa, tenho subagentes, tenho rules... acaba ficando um monte de parafernália, que no final é um monte de coisa que enche a minha janela de contexto."

### 9. Effort baixo pode impedir o disparo automático de paralelismo
**Evidência:** Com `effort: low`, o Claude não despachou agentes paralelos para uma tarefa de pesquisa (comparar Brevo vs. Postmark); ao trocar para `effort: high`, o mesmo prompt gerou 3 subagentes em paralelo (um por provedor).
**Confidence:** Média — anedota única, mas mecanismo plausível (mais raciocínio → mais chance de reconhecer oportunidade de paralelização).

---

## Entidades Mencionadas

- [[wiki/entities/claude-code]] — ferramenta central; comando `--worktree`, tool `Task`/`Agent`, `.claude/agents/`
- [[wiki/entities/anthropic]] — criadora do padrão de subagentes e do wrapper nativo de worktree

---

## Conceitos Tocados

- [[wiki/concepts/worktree-paralelismo]] — aqui descrito especificamente via `claude --worktree` nativo (a página existente cobria `git worktree` manual/spec-driven)
- [[wiki/concepts/subagentes]] — página nova; conceito central da fonte
- [[wiki/concepts/agente-ia]] — subagentes como especialização do padrão de agente
- [[wiki/concepts/tool-call]] — tools nativas citadas: `Agent`, `AskUserQuestion`, `Bash`, `Grep`, `Glob`, `Read`/`Write`/`Edit`
- [[wiki/concepts/skills-agente]] — comparação direta subagente vs. skill (mesma sintaxe de front-matter, propósito diferente)
- [[wiki/concepts/ciclo-agente]] — subagentes como forma de conter o crescimento do ciclo/contexto do agente pai
- [[wiki/concepts/janela-de-contexto]] — subagentes e worktrees como estratégias de economia de contexto

---

## Armadilhas Documentadas

1. **Parafernália excessiva** — muitas skills/subagentes sobrepostos confundem o roteamento automático do modelo; a solução é curadoria, não acúmulo.
2. **Work tree esquecida** — se não for encerrada e não estiver no `.gitignore`, pode ser commitada acidentalmente.
3. **Banco de dados / estado compartilhado entre worktrees** — não coberto diretamente nesta fonte, mas já documentado em [[wiki/concepts/worktree-paralelismo]] como limitação geral da técnica.
4. **Effort baixo mascarando capacidade de paralelismo** — o modelo pode simplesmente não reconhecer que uma tarefa é paralelizável se o nível de raciocínio estiver baixo.

---

## Quotes Valiosas

> "Work trees... é basicamente paralelismo a nível de file system." / "Subagentes... são paralelismo a nível de contexto."

> "Quando os subagentes finalizam o trabalho deles, o trabalho deles é unido, é convergido numa única coisa. [...] no final isso vai gerar uma única PR."

> "Escolham as tools que ele necessita somente, para evitar system prompt muito grande, pra evitar bazuca pra matar formiga."

> "É um problema de ter muita parafernália... às vezes ele não usa o que eu queria que ele usasse."

---

## Contradições / Questões Abertas

- A afirmação de que skills não suportam `model`/`tools` customizados foi checada ao vivo contra a doc da Anthropic no momento da gravação — vale reconfirmar na documentação oficial atual, já que o produto evolui rápido.
- Não fica claro qual o limite prático de subagentes em paralelo antes de custo/latência dominarem — tema não coberto aqui, potencial gancho para [[wiki/concepts/token-anxiety]] ou uma futura fonte sobre custo de multi-agent.
- Tabela de decisão worktree-vs-subagente dada pelo autor é heurística pessoal, não uma regra formal da Anthropic — útil, mas vale tratar como opinião de prática, não spec.
