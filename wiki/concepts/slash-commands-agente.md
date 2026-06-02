---
type: concept
title: "Slash Commands de Agente"
aliases: ["commands claude code", "custom commands", ".claude/commands", "agent slash commands"]
date_created: 2026-05-31
date_updated: 2026-05-31
source_count: 1
tags: [claude-code, slash-commands, automacao, agente-ia, prompt-engineering, context-engineering]
skill: tech-mentor-ai
status: stable
---

# Slash Commands de Agente

## TL;DR

Arquivos `.md` na pasta `.claude/commands/` que viram comandos invocáveis com `/nome <argumentos>` dentro do [[claude-code]]. Permitem codificar workflows complexos, prompts longos e procedimentos recorrentes uma única vez — e reutilizá-los com qualquer tarefa. São o equivalente de shell scripts para o agente.

## Estrutura

```
.claude/
  commands/
    exec-prompt.md      → /exec-prompt
    security-check.md   → /security-check
    create-commit.md    → /create-commit
    review-pr.md        → /review-pr
```

A **primeira linha** do arquivo vira a descrição do comando (exibida no autocomplete).

## Exemplo: exec-prompt.md

```markdown
# Execução de tarefa com workflow estruturado

Siga as instruções abaixo para executar a tarefa fornecida como $ARGUMENTS.

## Estratégia de execução

### Alto nível
1. Compreender o problema completamente
2. Investigar o codebase existente — não assuma nada
3. Identificar os arquivos a serem modificados

### Baixo nível
4. Crie um plano detalhado e aguarde aprovação
5. Implemente seguindo o plano
6. Escreva testes para o comportamento adicionado
7. Valide que os testes passam antes de declarar conclusão

## Restrições
- Nunca use emojis em código ou logs
- Commits em inglês, estilo Conventional Commits
- Não modifique arquivos fora do escopo da tarefa
```

**Uso:**
```
/exec-prompt adicionar endpoint DELETE /users/:id com soft delete
```

## $ARGUMENTS

O placeholder `$ARGUMENTS` é substituído pelo texto digitado após o nome do comando. Permite que o mesmo arquivo `.md` sirva para qualquer tarefa.

## Casos de Uso

| Comando | O que faz |
|---------|-----------|
| `/exec-prompt <tarefa>` | Executa com workflow padrão de desenvolvimento |
| `/security-check` | Audita o código por vulnerabilidades com critérios definidos |
| `/create-commit` | Gera commit seguindo Conventional Commits com análise de diff |
| `/review-pr` | Code review com checklist personalizado do time |
| `/create-doc <feature>` | Gera documentação técnica no padrão do projeto |

## Por que é Poderoso

Sem commands, você copia e cola prompts longos toda sessão — e eles ficam desatualizados espalhados em Notepads. Com commands:

1. **Versionado no repositório** — o time compartilha os mesmos workflows
2. **Evoluível** — melhora o prompt no arquivo, todas as próximas execuções se beneficiam
3. **Consistente** — mesmo processo garantido para qualquer tarefa
4. **Composto** — um command pode invocar outros patterns

## Diferença de CLAUDE.md

[[claude-md]] = contexto e regras sempre presentes (lido em toda sessão)
Slash commands = workflows invocados explicitamente quando necessário

Use CLAUDE.md para o que deve estar *sempre* ativo. Use commands para workflows específicos.

## Key Sources

- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
