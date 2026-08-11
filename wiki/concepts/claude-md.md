---
type: concept
title: "CLAUDE.md"
aliases: ["claude md", "project memory", "user memory", "memory claude code"]
date_created: 2026-05-31
date_updated: 2026-08-11
source_count: 5
tags: [claude-code, claude-md, memory, context-engineering, agente-ia]
skill: tech-mentor-ai
status: stable
---

# CLAUDE.md

## TL;DR

Arquivo de configuração e memória do [[claude-code]]. Contém regras, contexto do projeto e instruções que o agente lê no início de cada sessão. Equivalente ao `cursor rules` / `.cursorrules`. É a principal forma de persistir conhecimento entre sessões — mas é uma *guideline*, não uma garantia (use [[hooks-agente]] para execução garantida).

## Dois Níveis de Memória

| Tipo | Localização | Escopo |
|------|-------------|--------|
| **Project Memory** | `CLAUDE.md` na raiz do repositório | Só este projeto |
| **User Memory** | `~/.claude/CLAUDE.md` | Todos os projetos do usuário |

O agente lê ambos a cada sessão. User Memory tem precedência menor — use para preferências pessoais globais (ex: "nunca use emojis").

## Gerar Automaticamente com /init

```
/init
```

O Claude analisa o codebase inteiro (README, estrutura de pastas, código) e gera um `CLAUDE.md` com:
- Comandos para rodar o projeto
- Arquitetura geral detectada
- Estrutura de diretórios relevante
- Notas de desenvolvimento

Você pode passar instruções adicionais:
```
/init — ignore a pasta vendor/, ela é dependência externa
```

## Adicionar Regras com /memory

```
/memory
```

Abre o arquivo de memória relevante. Para adicionar uma regra, prefixe com `#`:

```markdown
# nunca use emojis no projeto, nem em logs ou outputs
# sempre escreva commits em inglês no estilo Conventional Commits
# ao criar testes, use jest com describe/it — não use test()
```

O Claude confirma e salva no arquivo correto.

## O que Colocar no CLAUDE.md

Bons candidatos:
- Comandos de build/test/run do projeto
- Convenções de código do time
- Arquitetura e decisões de design (ADRs relevantes)
- Serviços externos e como acessá-los
- Fluxos de desenvolvimento (ex: sempre criar branch antes de implementar)
- Restrições (o que nunca fazer)

Evitar:
- Estado temporário da tarefa atual (vai para o histórico da conversa)
- Informação que muda com frequência e você não vai manter

## Limitação: Não é Garantido

O LLM lê o `CLAUDE.md` como contexto e tenta seguir as instruções, mas pode ignorá-las em casos de janela cheia, compactação ou ambiguidade. Para comportamentos críticos (rodar testes após cada mudança, validar lint antes de commit), use [[hooks-agente]].

## Relação com settings.json

`CLAUDE.md` = contexto e regras em linguagem natural para o LLM.
`settings.json` = configuração técnica do runtime (permissões, MCPs, hooks).

São complementares, não substitutos.

A própria Anthropic recomenda comitar o `.claude/` de **projeto** (incluindo o `settings.json` de projeto) mas nunca o `.claude/` **pessoal** do usuário — comitar a versão de projeto garante que toda a equipe trabalhe com as mesmas especificações do Claude Code e permite evoluir esse comportamento coletivamente, em vez de cada dev divergir silenciosamente.

## Evidência Empírica: o Paper de Zurique

Paper da Universidade de Zurique testou repositórios com e sem arquivos de contexto:

| Condição | Taxa de sucesso | Custo |
|---|---|---|
| Sem arquivo | baseline | baseline |
| Arquivo gerado por LLM | −3% | +20% |
| Arquivo gerado por humano | +4% | +19% |

**O que o paper não mediu:** qualidade, segurança, design patterns, adesão às instruções. A métrica era apenas "testes passaram?". Um agente que deletou testes para fazer o código passar seria contado como sucesso.

**Conclusão prática:** o arquivo é necessário (sem ele, alucinação aumenta). O custo extra é real, por isso o arquivo deve ser enxuto — veja [[instruction-budget]].

## Estratégia: Enxuto com Links

Em vez de colocar tudo no `CLAUDE.md`, manter apenas o mínimo necessário e linkar para arquivos específicos carregados sob demanda:

```markdown
# CLAUDE.md (base mínima)
Convenções gerais aqui.

Para padrões de API: ver @api-standards.md
Para convenções de testes: ver @testing-conventions.md
```

Isso reduz o custo por sessão sem perder as garantias de qualidade. Adicionar correções de tooling progressivamente — só quando o agente alucinar em algo específico.

## Idioma do CLAUDE.md Impacta o Custo

Devido à [[token-tax-multilingual]], um `CLAUDE.md` escrito em português consome **62% mais context budget** por sessão do que o equivalente em inglês. O efeito se repete em toda sessão — não é custo único. Combinado com a recomendação de manter o arquivo enxuto (ver [[instruction-budget]] e paper de Zurique), escrever em inglês é a escolha de melhor custo-benefício quando possível.

## `review.md`: o CLAUDE.md do Revisor Automático

[[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] estende o uso do `CLAUDE.md` para um arquivo irmão, `review.md`, que codifica o que um revisor deve procurar. A cadeia lógica atribuída a [[wiki/entities/boris]]: se você sabe explicar por que um código está ruim, sabe escrever essa explicação — então escreva-a num `CLAUDE.md`/`review.md` que um **agente revisor** lê como input, em vez de re-explicar a cada PR. Boris argumenta que escrever esses arquivos (mais skills e docs) que deixam agentes trabalharem com *zero contexto adicional* é o novo trabalho de engenharia, barateado pela automação. No fluxo de [[wiki/concepts/matriz-risco-dificuldade-review-ia|amostragem]], cada defeito encontrado por sampling vira uma regra nova nesses arquivos — o `CLAUDE.md` é o destino do aprendizado, não uma correção pontual. (A fonte nota de passagem a preferência da [[wiki/entities/anthropic|Anthropic]] por `AGENTS.md` sobre `CLAUDE.md`.)

## Key Sources

- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — `review.md` como CLAUDE.md do revisor automático; docs como o novo trabalho de engenharia (Boris); CLAUDE.md como destino do aprendizado de sampling
- [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] — paper de Zurique; evidência empírica de custo e efetividade; estratégia enxuto + links
- [[wiki/sources/custo-tokens-portugues-vs-ingles]] — token tax de 62% para português; impacto direto no context budget por sessão
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — recomendação de comitar `.claude/` de projeto (não o pessoal) para alinhamento de equipe
