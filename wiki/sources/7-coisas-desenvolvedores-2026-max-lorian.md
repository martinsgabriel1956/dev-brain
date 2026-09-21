---
type: source
title: "7 Coisas Que Desenvolvedores Estão Fazendo em 2026 Que Pareceriam Loucura Há Três Anos"
aliases: ["7 things developers are doing in 2026"]
date_created: 2026-09-21
date_updated: 2026-09-21
source_count: 0
tags: [agentes-ia, ia-para-devs, coding-agents, automacao, agents-md, worktree, code-review, containment, event-driven]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/7-coisas-que-desenvolvedores-fazem-em-2026-max-lorian.md
source_url: "https://medium.com/@the.coding.front/7-things-developers-are-doing-in-2026-that-would-have-looked-insane-three-years-ago-1c9b46db719c"
author: "Max Lorian ('Maxime')"
date_published: "2026-09-12"
date_ingested: 2026-09-21
---

# 7 Coisas Que Desenvolvedores Estão Fazendo em 2026 Que Pareceriam Loucura Há Três Anos

## TL;DR

Ensaio de opinião (Medium, publicação The Coding Front) listando sete comportamentos hoje normalizados em times que usam agentes de codificação, que soariam absurdos em 2023: delegar uma tarefa inteira e sair, rodar o mesmo problema em vários modelos em paralelo e escolher o vencedor, escrever documentação (`AGENTS.md`/`CLAUDE.md`) para uma "terceira audiência" não-humana, dar máquina virtual própria ao agente, IA revisando/aprovando PR de outra IA, agentes disparados por evento como cron jobs (Cursor Automations, com números da Faire e da Amplitude), e um projeto interno da OpenAI de ~1 milhão de linhas escrito majoritariamente sem digitação humana. Argumento central do autor: o vocabulário de "assistente de IA" já não descreve o que está acontecendo — é delegação, não assistência — e o gargalo estrutural migrou de **produzir código** para **julgar qual produção merece sobreviver**.

---

## Key Claims

### Claim 1 — Delegação, não assistência

**Evidência:** GitHub Copilot, Cursor e Codex hoje recebem uma issue/ticket, trabalham em um ambiente próprio (edita repositório, roda comandos, testa, abre PR) sem o humano presente durante a execução — diferente de 2023, quando "IA para codar" significava o dev observar e colar cada trecho gerado.
**Confiança:** alta (comportamento observável, sem número/benchmark citado).

### Claim 2 — Produzir ficou barato; escolher virou a habilidade central

**Evidência:** Cursor permite enviar o mesmo problema para múltiplos modelos em paralelo, cada um numa worktree isolada, para depois comparar e ficar com a melhor implementação — trabalho duplicado que antes era visto como desperdício de gestão agora compensa porque o recurso escasso é compute, não tempo de engenheiro.
**Confiança:** média — é observação/opinião do autor sobre uma feature real do Cursor, sem dado quantitativo de adoção.

### Claim 3 — Repositórios ganharam uma "terceira audiência"

**Evidência:** Arquivos como `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` e `copilot-instructions.md` documentam arquitetura, convenções e regras de teste para agentes — não apenas para humanos e para o compilador. O GitHub já faz o Copilot gerar as próprias instruções que depois o guiarão no repositório.
**Confiança:** alta (fenômeno amplamente documentado; ver [[wiki/sources/agents-md-vale-a-pena-paper-zurique]] e [[wiki/concepts/agents-md-vs-claude-md]] já na wiki).

### Claim 4 — Agente com sua própria máquina muda o modelo de ameaça

**Evidência:** Agentes na nuvem (Cursor, entre outros) ganham VMs com terminal, browser, credenciais e acesso de rede — no caso do Cursor, inclusive um desktop operável. O autor argumenta que dar mais autonomia é o que torna o agente útil (um agente que pede permissão a cada comando "é só um autocomplete carente com shell"), mas isso cria simultaneamente um problema de permissões maior.
**Confiança:** média-alta — descrição de capacidade real de produto, julgamento de risco é opinião do autor mas alinhado ao raciocínio padrão de defense-in-depth.

### Claim 5 — IA revisa e aprova PR de IA

**Evidência:** GitHub Copilot pode revisar pull requests abertos por bots (incluindo pelo próprio agente na nuvem do Copilot) e, se o admin do repositório habilitar, aprovar o PR. O ponto de decisão humana se move para "definir a política de quando um agente pode aprovar", não mais para ler cada diff.
**Confiança:** alta (feature de produto documentada publicamente pelo GitHub).

### Claim 6 — Agentes rodando como cron job/event handler

**Evidência:** Cursor Automations dispara agentes a partir de agendamento ou evento (mensagem no Slack, ticket no Linear, PR mesclado, incidente no PagerDuty). Números citados: Faire roda >2.000 jobs autônomos/semana (investigação de CI, bugfix, code review); Amplitude roda >1.000/semana, com 60–70% dos PRs de baixo risco indo direto para produção.
**Confiança:** média — números vêm de declarações das próprias empresas citadas pelo autor, sem link/fonte primária no artigo, tratar como autorrelato não auditado.

### Claim 7 — Produto interno da OpenAI com "zero código escrito manualmente"

**Evidência:** A OpenAI descreve cinco meses construindo um produto interno sob a restrição de que nenhuma linha fosse escrita manualmente — lógica de aplicação, testes, CI, documentação, observabilidade e ferramentas internas, produzidos pelo Codex, chegando a ~1 milhão de linhas. O trabalho dos engenheiros é descrito como desenhar ambientes, especificar intenção e construir loops de feedback.
**Confiança:** média — claim de origem OpenAI (autorrelato de caso de uso interno), sem link/paper técnico citado no artigo; número "um milhão de linhas" não verificável de forma independente.

---

## Entidades

- [[wiki/entities/cursor]] — Cursor Automations (evento/agendamento), execução multi-modelo em worktrees paralelas, desktop operável por agente
- [[wiki/entities/codex-openai]] — projeto interno da OpenAI com ~1M linhas geradas via Codex, zero código manual
- [[wiki/entities/openai]] — dona do Codex; caso do produto interno "zero manually written code"

## Conceitos Tocados

- [[wiki/concepts/era-agentica]] — delegação de ticket inteiro como nova unidade de trabalho, não mais sugestão de linha
- [[wiki/concepts/autonomy-slider]] — "dar o ticket e ir embora" como posição de volume máximo no slider de Karpathy
- [[wiki/concepts/worktree-paralelismo]] — variante N-modelos-mesmo-problema do padrão de paralelismo via worktree
- [[wiki/concepts/agents-md-vs-claude-md]] — enquadramento do arquivo de contexto como documentação para uma "terceira audiência" (o agente), não só humano/compilador
- [[wiki/concepts/agent-containment]] — VM própria, credenciais e acesso de rede do agente como superfície de ameaça nova
- [[wiki/concepts/code-review]] — IA aprovando PR de IA desloca a decisão humana para política de aprovação, não leitura de diff
- [[wiki/concepts/human-in-the-loop]] — humano "sobe um andar": intervém em exceção/política, não em cada execução
- [[wiki/concepts/loop-engineering]] — Cursor Automations como produto comercial do padrão "loop disparado por evento/schedule" (Faire, Amplitude)
- [[wiki/concepts/governanca-de-codigo-gerado-por-ia]] — com produção barata, julgamento sobre qual implementação sobrevive vira o trabalho central

## Citações Preservadas

> "Assistants generally assist while you do something. A system working through your ticket while you are arguing about roadmap priorities in another room feels closer to delegation."

> "Producing an implementation can become cheap enough that choosing becomes more important than producing."

> "A build process living entirely inside Dave's head used to become a problem when Dave went on vacation. Now it becomes a problem every time an agent touches the system."

> "We moved the human one floor higher and left two machines downstairs arguing about TypeScript."

## Open Questions

1. Os números de Faire (>2.000 jobs/semana) e Amplitude (>1.000/semana, 60–70% de PRs low-risk direto para produção) não têm fonte primária linkada no artigo — vale checar se há post técnico ou case study oficial dessas empresas para validar/contradizer.
2. O claim da OpenAI ("zero manually written code", ~1M linhas) também é autorrelato sem link para paper/post técnico detalhado — não dá para avaliar o que conta como "não escrito manualmente" (specs em linguagem natural também são um tipo de especificação humana do comportamento).
3. Nenhuma fonte já na wiki cobria especificamente **Cursor Automations** como produto (agentes disparados por Slack/Linear/PR/PagerDuty) — [[wiki/concepts/loop-engineering]] já previa esse padrão teoricamente ("disparável por prompt, schedule ou evento"), esta fonte fecha a lacuna com um exemplo comercial concreto.
