---
type: entity
title: "Claude Code"
aliases: ["claude code cli"]
date_created: 2026-05-18
date_updated: 2026-07-31
source_count: 11
tags: [ferramenta, agentes-ia, anthropic, llmops, cli, mcp, hooks]
skill: tech-mentor-ai
status: stable
---

## O Que É

CLI da Anthropic que age como [[agente-ia]] de desenvolvimento diretamente no terminal. Lê/escreve arquivos, executa comandos, navega na web e se integra a servidores [[mcp-server|MCP]] externos. Integra com qualquer IDE baseada em VS Code via extensão oficial.

---

## Recursos Principais

| Recurso | O que faz |
|---------|-----------|
| [[claude-md]] | Arquivo de memória e regras persistentes; lido em toda sessão |
| [[plan-mode]] | Modo de planejamento antes de executar (Shift+Tab) |
| [[slash-commands-agente]] | Commands customizados em `.claude/commands/*.md` |
| [[hooks-agente]] | Automação garantida em eventos (PreToolUse, PostToolUse, Stop) |
| [[mcp-server]] | Integração com ferramentas externas via protocolo MCP |
| [[context-compaction]] | Compactação automática da janela de contexto (~200k tokens) |
| [[wiki/concepts/worktree-paralelismo]] | `claude --worktree <nome>` — cópia isolada do repo por agente, paralelismo de file system |
| [[wiki/concepts/subagentes]] | `.claude/agents/*.md` — paralelismo de contexto, model/tools customizáveis por subagente |
| [[wiki/concepts/rewind-checkpoints-claude-code]] | Checkpoints ao longo da conversa; `rewind` volta a um ponto anterior sem depender só de commits Git |
| [[wiki/concepts/gerenciamento-de-sessoes-claude-code]] | Renomear e retomar sessões salvas localmente; `/go` para objetivos verificáveis de longo prazo |
| [[wiki/concepts/modelo-por-leverage-tarefa]] | Alocar modelos mais fortes (Fable) para planejamento/arquitetura, mais leves (Sonnet) para execução rotineira |

## Planos (referência da gravação — verificar preços atuais)

| Plano | Preço/mês | Características |
|-------|-----------|-----------------|
| Free | $0 | Uso muito limitado |
| Pro | ~$20 | Rate limiting rápido; uso ocasional |
| Max | $100 | 5× mais que Pro; acesso ao Opus |
| Max | $200 | 20× mais que Pro |

**Armadilha:** usar API Key diretamente (sem plano) cobra por token e pode custar centenas de dólares sem que o usuário perceba. Sempre autenticar com "Claude account with subscription".

## Integração com IDE

1. Instale a extensão "Claude Code" no VS Code/Cursor
2. Clique em "Run Claude Code" para abrir painel lateral
3. Dentro do Claude Code: `/ide` para conectar ao projeto aberto

## Configuração

Arquivos em `.claude/`:
- `settings.json` — commitado, compartilhado com o time
- `settings.local.json` — pessoal, não commitado (permissões, MCPs locais)

## Comandos Essenciais

```
/init          → gera CLAUDE.md analisando o codebase
/memory        → edita memória (CLAUDE.md) do projeto ou usuário
/ide           → conecta ao IDE aberta
/mcp           → lista servidores MCP ativos
/hooks         → gerencia hooks de eventos
/permissions   → visualiza permissões configuradas
/compact       → compacta o histórico para liberar contexto
Shift+Tab      → alterna entre Auto-accept e Plan Mode
Esc            → para a execução atual
```

---

## Seleção Automática de Ferramentas

As tools do Claude Code carregam descrições que entram no contexto do modelo — não é necessário nomear explicitamente qual ferramenta usar (ex.: "use o Playwright para testar isso"). Um pedido genérico como "testa aí no navegador" já é suficiente para o agente inferir e selecionar a ferramenta certa, embora nomear explicitamente também funcione e continue sendo válido quando há ambiguidade real entre ferramentas equivalentes.

## Retenção de Dados de Sessão

Sessões ficam retidas localmente em `~/.claude/projects` por padrão durante 30 dias, período configurável. Sessões individuais podem ser deletadas manualmente; enquanto não deletadas, ficam disponíveis para consulta, leitura ou análise.

## Sandbox Nativo

Desde outubro de 2025, o Claude Code tem sandbox próprio usando [[wiki/entities/bubblewrap]] no Linux e Sandbox-exec no Mac — o mesmo stack técnico usado pelo projeto independente [[wiki/concepts/agent-containment|AI Jail]]. Diferença apontada por [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]]: por padrão, quando um comando falha por restrição do sandbox, o próprio agente pode tentar de novo pulando a restrição (padrão de retry ativado por padrão de fábrica) — mecanismo de opt-out não verificado contra a documentação oficial nesta ingestão, mas que, se real, muda quem controla a saída da cela (o agente, não só o usuário). Ver [[wiki/concepts/defense-in-depth]] para a comparação completa com o AI Jail, que não tem esse opt-out.

## Relevância para Token Anxiety

O mecanismo de [[context-compaction]] da janela de contexto do Claude Code é um dos principais catalisadores do fenômeno [[token-anxiety]]: desenvolvedores sentem urgência de maximizar o uso dos tokens disponíveis antes do reset, distorcendo rotinas e prioridades.

---

## Comparação com Harnesses de Learning Loop (Hermes Agent, Open Claw)

[[wiki/sources/hermes-agent-open-claw-learning-loop]] compara o Claude Code a projetos open source como [[wiki/entities/hermes-agent]] e [[wiki/entities/open-claw]], que embutem um [[wiki/concepts/closed-loop-skill-learning|closed-loop skill learning system]] sobre uma [[wiki/concepts/agent-memory-tres-camadas|memória em três camadas]]. Tese central da fonte: "Hermes não é o Claude Code com mais memória" — a diferença não é quantidade de memória, mas o loop que gera e refina skills automaticamente a partir do histórico de tarefas. O Claude Code foi citado no ranking global de uso de tokens do OpenRouter (perdendo para o Hermes Agent na semana anterior à publicação da fonte), e a Anthropic respondeu ao mesmo padrão com a feature "Dreaming in Claude" (ver [[wiki/entities/anthropic]]).

## VPS com Claude Code Pré-instalado (Oferta de Provedor)

[[wiki/sources/continuous-integration-delivery-deploy-vs-release]] menciona, em bloco patrocinado da [[wiki/entities/hostgator]], uma oferta de VPS com Claude Code pré-instalado — promovida como alternativa a rodar localmente: não exige deixar o computador ligado, e permite interagir remotamente (ex.: via celular). Conteúdo patrocinado, sem avaliação técnica independente da oferta em si.

## Citação de Boris (Criador) sobre Loop Engineering

[[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] cita Boris, criador do Claude Code, dizendo que trabalha "em loops que decidem o que fazer" em vez de dar prompts — citação usada (junto com uma fala similar do criador do OpenCode) como gatilho do hype recente em torno de [[wiki/concepts/loop-engineering]].

## "By The Way" e Recuperação de Contexto em Múltiplos Agentes Paralelos

[[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] cita o recurso "By The Way" como útil para recuperar contexto ao alternar entre vários agentes rodando em paralelo (o autor cita até 8 simultâneos) — mas trata o próprio uso do recurso como sintoma do problema mais amplo de custo: reconstruir contexto perdido consome tokens adicionais sem ganho de valor equivalente. A mesma fonte cita devs trocando o Claude Code pelo [[wiki/entities/opencode]] alegando loops de correção supérflua (bug suspeito → sugestão → reescreve testes → reescreve código) que multiplicam consumo de token — anedota sem confirmação/benchmark independente.

## Uso como "Professor" em Autopentest, Não Como Executor Autônomo

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve um uso deliberadamente diferente de vibe coding: a autora usou o Claude Code para conduzir um autopentest guiado no próprio SaaS ([[wiki/entities/pulsar-saas]]), documentando e tentando entender cada decisão em vez de apenas aceitar o resultado. O padrão de prompt que ela descreve — apontar para documentação existente do sistema, testar um escopo por vez em sessões separadas, e declarar explicitamente o que a IA não pode fazer sem nova autorização — é apresentado como defesa contra dois problemas: a IA "delirar" ao lidar com escopo grande demais, e refatoração não solicitada quando uma autorização ampla é mal-interpretada como permissão permanente. → [[wiki/concepts/prompt-engineering]]

## Key Sources

- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — autopentest guiado (autenticação, IDOR, CSRF, XSS/SQLi, rate limiting, secrets, dependências); método de seis passos para prompt de segurança
- [[wiki/sources/token-anxiety-agentes-ia-comportamento-devs]]
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — recurso "By The Way" como sintoma de custo; devs trocando para OpenCode por loops de correção supérflua
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — sandbox nativo (Bubblewrap/Sandbox-exec) e comparação com o AI Jail
- [[wiki/sources/hermes-agent-open-claw-learning-loop]] — comparação com harnesses de learning loop (Hermes Agent, Open Claw)
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — checkpoints/rewind, gerenciamento de sessões, `/go`, alocação de modelo por leverage, seleção automática de ferramentas, retenção de 30 dias
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — citação de Boris sobre trabalhar "em loops que decidem o que fazer"
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — seleção manual de modelo por tarefa na UI, e automação da escolha via skill + subagentes (um subagente por modelo)
- [[wiki/sources/continuous-integration-delivery-deploy-vs-release]] — oferta patrocinada de VPS (HostGator) com Claude Code pré-instalado
