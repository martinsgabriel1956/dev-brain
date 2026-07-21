---
type: source
title: "20 Melhores Práticas de Claude Code Segundo a Própria Anthropic"
aliases: []
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 0
tags: [claude-code, boas-praticas, agente-ia, context-engineering, prompt-engineering, code-review, sessoes, sandboxing]
skill: tech-mentor-ai
status: stable
source_file: raw/20-melhores-praticas-claude-code-segundo-anthropic.md
source_url: ""
author: "não identificado na transcrição (canal de vídeo em português)"
date_published: "2026-07 (aprox. — vídeo grava referência a 'daqui dois dias, dia 16 ou 17 de julho')"
date_ingested: 2026-07-21
---

## TL;DR

Vídeo em português que resume ~19-20 boas práticas extraídas de uma leitura completa da documentação oficial do Claude Code, atribuídas à Anthropic. Cobre desde técnicas de prompt (descrever resultado e verificação, não passos) até mecânica operacional do CLI (checkpoints/rewind, gerenciamento de sessões, `/go`, sandboxing para loops longos, retenção de dados local de 30 dias).

## Key Claims

1. **Verificação embutida no prompt** — pedir para o Claude Code verificar o próprio resultado (rodar testes, comparar screenshot) reduz a chance de aceitar um resultado incorreto como pronto. *Evidência: exemplo da documentação oficial (`validateEmail` com casos de teste; comparação de screenshot com design original).*
2. **Descrever o estado desejado, não os passos** — deixar o Claude Code decidir os arquivos e o caminho, especialmente em modelos mais fortes (Fable). *Evidência: biblioteca de prompts oficial do Claude Code.*
3. **Refatorar em pequenos incrementos testáveis** — evitar grandes refatorações de uma vez. *Evidência: seção de fluxos de trabalho comuns da documentação.*
4. **Interromper cedo quando o agente erra o caminho.**
5. **Preferir regras concretas e específicas a diretrizes genéricas** (ex.: "use Clean Code" é pior que uma regra de projeto específica sobre como acessar uma URL).
6. **Usar `/clear` (ou subagentes) para tarefas não relacionadas**, evitando poluição de contexto.
7. **Iniciar a sessão no menor diretório possível** que resolve a tarefa (ex.: pasta `backend/` de um monorepo, não a raiz).
8. **Em modelos fortes (Fable), focar em resultado/limitações/evidências** em vez de sequência de passos.
9. **Alocar modelos por alavancagem (leverage) da tarefa** — modelos fortes para planejamento/arquitetura, modelos leves para execução rotineira; workflow sugerido: modelo forte cria spec → modelo intermediário quebra em tarefas → Sonnet implementa.
10. **Checkpoints e comando `rewind`** para voltar a um ponto anterior da conversa sem depender só de commits Git.
11. **Gerenciamento de sessões** — sessões salvas localmente, podem ser renomeadas (`/rename`) e retomadas (`--resume`), preservando contexto que se perderia ao só voltar a um commit Git.
12. **Comando `/go`** para manter o Claude Code trabalhando até um objetivo verificável de longo prazo (ex.: PR até zero erros de teste).
13. **Arquivo dedicado a code review** (`review`), separado do `CLAUDE.md`, contendo só instruções pertinentes a revisão; comando `/code-review` com effort "ultra" recomendado para revisões complexas.
14. **Comando `/context`** para inspecionar e limpar o contexto ativo.
15. **Comitar o `.claude/` do projeto** (não o pessoal) para alinhamento de equipe.
16. **Configurar auto mode com cuidado** — a tecla ESC nas permissões pode exigir aprovação explícita para ações como `git push` mesmo em modo automático.
17. **Usar sandbox (VM, container, dev container) para loops não interrompidos** de agente.
18. **Não é necessário nomear ferramentas explicitamente** nos prompts — a descrição da tool já entra no contexto do modelo.
19. **Retenção local de sessões por 30 dias** em `~/.claude/projects`, configurável, com exclusão individual possível.

## Entidades

- [[wiki/entities/anthropic]] — autora da documentação e das recomendações
- [[wiki/entities/claude-code]] — ferramenta central do vídeo

## Conceitos

- [[wiki/concepts/prompt-engineering]] — verificação embutida e "descreva o resultado, não os passos"
- [[wiki/concepts/context-compaction]] — `/clear`, `/context`, escopo de diretório mínimo
- [[wiki/concepts/code-review]] — arquivo `review` dedicado e `/code-review --ultra`
- [[wiki/concepts/agent-containment]] — sandbox/VM/container para loops não interrompidos
- [[wiki/concepts/claude-md]] — distinção entre `.claude/` de projeto (comitado) e pessoal
- [[wiki/concepts/rewind-checkpoints-claude-code]] — checkpoints e `/rewind`
- [[wiki/concepts/gerenciamento-de-sessoes-claude-code]] — `/rename`, `--resume`, retenção de 30 dias
- [[wiki/concepts/modelo-por-leverage-tarefa]] — alocação de modelo por alavancagem da tarefa

## Open Questions

- Autor do vídeo não se identifica explicitamente na transcrição.
- Sintaxe exata dos comandos citados (`/rename`, `/rewind`, `/go`, flags de retenção) não foi verificada contra a documentação oficial atual nesta ingestão — os nomes usados na transcrição podem divergir levemente da nomenclatura real da CLI em versões futuras.
- Referência a "Fable" como um dos modelos mais fortes é consistente com a nomenclatura usada em outras fontes já ingeridas na wiki, mas não há link direto para uma página de comparação de modelos Anthropic nesta fonte.

## Quotes

> "Descreva o resultado, não os passos, e deixe o Claude Code encontrar os arquivos."

> "Quanto mais impactante for essa tarefa, mais complexo é o modelo que a gente quer utilizar; quanto mais rotineiro, mais simples pode ser o modelo."

## Raw Source

[[raw/20-melhores-praticas-claude-code-segundo-anthropic]]
