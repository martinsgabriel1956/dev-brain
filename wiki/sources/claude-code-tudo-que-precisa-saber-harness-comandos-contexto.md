---
type: source
title: "Claude Code: tudo que você precisa saber sobre o harness, comandos, contexto e automação"
aliases: ["aula claude code harness comandos", "claude code tudo que precisa saber", "o harness não faz mágica"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 0
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/claude-code-tudo-que-precisa-saber-harness-comandos-contexto.md"
source_url: ""
author: "não identificado na transcrição; provavelmente o mesmo autor de [[wiki/sources/loop-engineering-guia-pratico-casos-reais-desastres-lucas-montano]], atribuído na wiki a Lucas Montano por inferência"
date_published:
date_ingested: 2026-11-10
tags: [claude-code, harness, agentes-ia, context-engineering, permissoes, skills, rules, mcp, worktree, headless, spec-driven, model-routing]
skill: tech-mentor-ai
status: draft
---

# Claude Code: tudo que você precisa saber sobre o harness, comandos, contexto e automação

**Formato:** transcrição de vídeo do YouTube (legenda automática, PT-BR), limpa sem alteração de conteúdo. A aula segue slides que a transcrição não mostra, e boa parte é leitura de lista de comandos. Inclui chamadas de venda para um workshop pago do autor.

## TL;DR

O [[wiki/entities/claude-code|Claude Code]] não é um chat com autocomplete: é um [[wiki/concepts/harness|harness]] que executa, aplica permissões e monta o contexto, enquanto o modelo só decide o próximo passo. O vídeo percorre instalação, loop agêntico, [[wiki/concepts/janela-de-contexto|janela de contexto]], [[wiki/concepts/modos-de-permissao-claude-code|modos de permissão]], [[wiki/concepts/plan-mode|plan mode]], comandos, modelos e esforço, [[wiki/concepts/claude-md|CLAUDE.md]], [[wiki/concepts/rules-agente|rules]], [[wiki/concepts/skills-agente|skills]], MCP, [[wiki/concepts/worktree-paralelismo|worktrees]] e modo headless. A tese de fecho: o harness não faz mágica. Quanto mais contexto e especificação entram antes da execução, menos retrabalho e menos tokens se gastam, e por isso o planejamento vai para o modelo forte e a execução para o mais simples.

## Key Claims

A conferência usou a documentação oficial em `code.claude.com/docs`, marcada como `[external]`.

1. **O harness faz o trabalho sujo; o modelo só decide.** O harness lê e escreve arquivos, roda comandos, aplica permissões, monta contexto, salva checkpoints, compacta e dispara hooks. O modelo escolhe ferramenta e argumentos e para quando acha que terminou, por isso precisa de verificador. Trocar de modelo muda a decisão, não as ferramentas. Evidência: explicação do autor, igual a [[wiki/concepts/harness]] ("a LLM apenas orquestra"). Confiança: alta.
2. **O mesmo motor roda em terminal, IDE, desktop e web/mobile.** Evidência: fala do autor; não conferida. Confiança: média.
3. **Comandos de setup e diagnóstico:** `claude auth login`, `auth status`, `setup-token` (token longo para CI), `claude doctor`, `update`, `/powerup` e o modo seguro. Evidência: todos existem na [referência da CLI](https://code.claude.com/docs/en/cli-reference.md) `[external]`; o modo seguro é a flag `--safe-mode`. Confiança: alta. Ressalva: `claude doctor` só diagnostica; quem aplica correção é o `/doctor` da sessão.
4. **Tudo que entra custa contexto: arquivo lido, saída de comando, resultado de MCP e a conversa inteira.** Sintomas de janela cheia: esquecer instrução inicial, repetir erro corrigido, reler arquivos, responder genérico. Evidência: experiência do autor, coerente com [[wiki/concepts/degradacao-de-contexto]]. Confiança: alta como heurística.
5. **Três táticas de contexto:** `/clear` entre tarefas ("resolve 80%", número sem medição), subagente para pesquisa e "Summarize from here" no menu de `Esc Esc`. O autor prefere nova sessão a `/compact`. Evidência: [checkpointing](https://code.claude.com/docs/en/checkpointing.md) confirma o item do menu `[external]`. Confiança: alta para os mecanismos, baixa para os 80%. Ver [[wiki/concepts/context-compaction]].
6. **`/btw` faz pergunta lateral sem entrar no histórico; o auto compact é configurável.** Evidência: [comandos](https://code.claude.com/docs/en/commands.md) confirma `/btw`; [model-config](https://code.claude.com/docs/en/model-config.md) traz `/autocompact` e `CLAUDE_CODE_AUTO_COMPACT_WINDOW` `[external]`. Confiança: alta. Os "500k" do slide são só um valor possível.
7. **Seis modos de permissão, cada um com seu uso.** Default, Accept Edits, Plan, Auto (classificador em segundo plano), Don't Ask (para CI) e Bypass Permissions (só em contêiner ou VM). Evidência: [permission-modes](https://code.claude.com/docs/en/permission-modes.md) `[external]`. Confiança: alta. Nas versões recentes o Auto é padrão em todos os planos, não só Pro e Max. Ver [[wiki/concepts/modos-de-permissao-claude-code]].
8. **O risco real é conteúdo hostil em arquivo ou site instruindo o agente.** Evidência: alerta do autor, é o cenário de [[wiki/concepts/prompt-injection]]. Confiança: alta.
9. **"O erro mais caro não é o código errado, é o código certo pro problema errado."** Daí o ciclo explorar, planejar, implementar, verificar. Evidência: argumento. Confiança: alta como heurística. Ver [[wiki/concepts/plan-mode]].
10. **`@arquivo` põe o arquivo inteiro no contexto; `@pasta` lista o diretório.** Evidência: [common-workflows](https://code.claude.com/docs/en/common-workflows.md) confirma; a inclusão de arquivo vai até cerca de 25 mil tokens `[external]`. Confiança: alta. O autor primeiro diz que a pasta é "lida" e logo corrige para "listar".
11. **Seja específico e aponte um padrão que já existe.** "Claude imita bem o que você mostra e inventa mal o que você descreve." Os exemplos de prompt ruim e bom seguem a página de [boas práticas](https://code.claude.com/docs/en/best-practices.md), incluindo o `HotDogWidget.php` `[external]`. Confiança: alta.
12. **`/batch` divide uma mudança entre 5 e 30 subagentes, cada um com worktree e PR; `/goal` trabalha até a condição ser satisfeita.** Evidência: [comandos](https://code.claude.com/docs/en/commands.md) `[external]`. Confiança: alta. O nome `/goal` corrige o `/go` registrado na wiki; ver [[wiki/concepts/gerenciamento-de-sessoes-claude-code]].
13. **Escolha de modelo:** `best`, Fable para sessões longas, Opus para raciocínio complexo, Sonnet para o dia a dia e subagentes, Haiku para o simples, `opusplan` e `sonnet[1m]`. Evidência: os aliases existem em [model-config](https://code.claude.com/docs/en/model-config.md) `[external]`. Confiança: alta para os nomes; a alocação é opinião. Ver [[wiki/concepts/modelo-por-leverage-tarefa]].
14. **Esforço: low, medium, high, xhigh, max e ultra code; high seria o padrão.** Evidência: os cinco níveis existem, mas o padrão é `medium` em Fable 5.2, Opus 5.5, Sonnet 5.5 e Haiku 5.5, e `ultracode` é uma configuração que acrescenta workflows dinâmicos, não um nível `[external]`. Confiança: média.
15. **"Esforço alto não conserta prompt ruim": arrume o contexto antes, é de graça.** Evidência: argumento. Confiança: alta como heurística.
16. **CLAUDE.md fica sempre no contexto, custa sempre e tem limite de 200 linhas.** Evidência: a [documentação](https://code.claude.com/docs/en/memory.md) recomenda ficar abaixo de 200 linhas `[external]`. Confiança: alta, lendo "limite" como recomendação. Ver [[wiki/concepts/claude-md]].
17. **Rules em `.claude/rules/`: sem `paths` carregam sempre; com `paths`, só quando o Claude toca um arquivo correspondente.** Evidência: [memory](https://code.claude.com/docs/en/memory.md) `[external]`. Confiança: alta. Isso matiza a tabela "Rule é sempre global" de [[wiki/concepts/rules-agente]].
18. **Critério rule ou skill: "se tem numeração de passos, é uma skill".** Rule é conhecimento passivo; skill é procedimento ativo, com só a description sempre no contexto. Evidência: opinião do autor para o critério; [skills](https://code.claude.com/docs/en/skills.md) confirma o carregamento `[external]`. Confiança: média para o critério. Ver [[wiki/concepts/skills-agente]].
19. **MCP se adiciona com `claude mcp add --transport http` e fica em `.mcp.json`.** Evidência: [mcp](https://code.claude.com/docs/en/mcp.md) `[external]`. Confiança: alta. Exemplos do autor: Asaas e Hostinger. Ver [[wiki/concepts/model-context-protocol]].
20. **Worktree permite editar em paralelo sem uma sessão atropelar a outra; exige ao menos um commit, e `.worktreeinclude` leva o que não está no git.** Evidência: [worktrees](https://code.claude.com/docs/en/worktrees.md) `[external]`. Confiança: alta. A explicação do autor é imprecisa: fala em "clonar para uma branch", mas worktree é um diretório extra ligado ao mesmo repositório. Ver [[wiki/concepts/worktree-paralelismo]].
21. **Uma sessão revisa o que a outra escreveu, porque "contexto novo não tem apego ao código".** Evidência: argumento, coerente com [[wiki/concepts/revisao-por-agente-independente]]. Confiança: alta como heurística.
22. **`claude -p` é a porta para CI, pré-commit e migrações em lote.** Evidência: [headless](https://code.claude.com/docs/en/headless.md) `[external]`. Confiança: alta. Ressalva: o autor descreve headless como "rodar em background", mas `-p` é modo não interativo, o que é outra coisa.
23. **Modelo forte especifica, modelo simples executa, e a especificação boa reduz gasto.** ADR, RFC e PRD dão à IA o porquê das decisões. Evidência: argumento, sem medição. Confiança: média. Ver [[wiki/concepts/spec-driven-development]].

> "O harness, ele não faz mágica, tu precisa configurar esse negócio direito." (autor)

> "Claude imita bem o que você mostra e inventa mal o que você descreve." (autor)

## Erros da fonte

- `Ctrl+O` abre o visualizador de transcrição, e a documentação não diz que ele mostra raciocínio escondido ([interactive-mode](https://code.claude.com/docs/en/interactive-mode.md)) `[external]`.
- Deep Research, Design e Dataviz foram citados como "especialistas embutidos", mas a lista de skills empacotadas da [documentação](https://code.claude.com/docs/en/skills.md) não os traz `[external]`. Só `/claude-api` confere.
- A página de comandos não traz `/todos` (a transcrição é incerta nesse ponto; `/tasks` existe, mas lista trabalho em segundo plano) e não traz `/worktree`: existe a flag `--worktree` `[external]`.
- Sobre xhigh, o autor diz que não gasta mais tokens, e sim que "vai ser mais caro o token". Não foi conferido. Por inferência `[skill: tech-mentor-ai]`, esforço muda quanto o modelo raciocina, e o preço por token depende do modelo, então a afirmação é suspeita.

## Entidades

- [[wiki/entities/claude-code]], [[wiki/entities/anthropic]].
- Citados de passagem: [[wiki/entities/codex-openai]], Antigravity, Kimi Code, [[wiki/entities/hostinger]], Asaas, Notion, [[wiki/entities/github]].

## Conceitos

- [[wiki/concepts/harness]]
- [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/context-compaction]], [[wiki/concepts/gerenciamento-de-sessoes-claude-code]]
- [[wiki/concepts/modos-de-permissao-claude-code]], [[wiki/concepts/plan-mode]], [[wiki/concepts/prompt-injection]]
- [[wiki/concepts/claude-md]], [[wiki/concepts/rules-agente]], [[wiki/concepts/skills-agente]], [[wiki/concepts/model-context-protocol]]
- [[wiki/concepts/subagentes]], [[wiki/concepts/worktree-paralelismo]], [[wiki/concepts/revisao-por-agente-independente]]
- [[wiki/concepts/modelo-por-leverage-tarefa]], [[wiki/concepts/spec-driven-development]], [[wiki/concepts/vibe-coding]]

## Relação com fontes anteriores

- [[wiki/sources/claude-code-guia-pratico-full-cycle]] cobre o mesmo terreno com mais prática; esta fonte é mais ampla e mais recente nos comandos.
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] registrou `/go`; aqui e na documentação o comando é `/goal`.
- **Tensão:** [[wiki/concepts/rules-agente]] trata a rule como sempre global, enquanto rules com `paths` são condicionais. A diferença pode vir de harnesses distintos, e a ressalva foi posta na página sem apagar a tabela.

## Open Questions

- Qual é a skill "NP Spec Driven" do autor? O nome veio distorcido da legenda ("NP", "ONP", "Anpace").
- O "quadro 35" prometido para o verificador não reaparece na fala. Provavelmente é um slide.
- Autoria: o vídeo não diz o nome do autor. Os sinais (workshop de 1º de agosto, Hostinger, "nossa skill de Spec Driven") coincidem com a fonte de loop engineering, cuja atribuição já é inferência.
