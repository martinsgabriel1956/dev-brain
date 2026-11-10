---
type: source
title: "Fluxo completo de desenvolvimento de uma funcionalidade complexa 100% com IA"
aliases: ["fluxo feature com ia valdemar", "design doc ate worktree", "integracao stripe com cursor"]
date_created: 2026-11-10
date_updated: 2026-11-10
source_count: 0
tags: [tech-mentor-ai, context-engineering, rpi-workflow, design-doc, cursor, worktree, paralelismo, skills, mcp, rules, model-routing]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/fluxo-completo-feature-com-ia-design-doc-worktrees-valdemar-neto.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-11-10
---

# Fluxo completo de desenvolvimento de uma funcionalidade complexa 100% com IA

## TL;DR

Vídeo de [[wiki/entities/valdemar-neto]] que aplica na prática o [[wiki/concepts/rpi-workflow|RPI]] e a [[wiki/concepts/progressive-disclosure-ia|progressive disclosure]] do vídeo anterior dele ([[wiki/sources/context-engineering-codebases-grandes-rpi]]). O caso é integrar o [[wiki/entities/stripe|Stripe]] ao módulo de billing de um monorepo modular, no [[wiki/entities/cursor|Cursor]]. O fluxo: um [[wiki/concepts/design-doc|design doc]] revisado por humanos vira tasks no Jira; cada task vira um plano em contexto novo; cada plano é executado em outro agente, com modelo mais barato; o humano revisa. Enquanto espera, o autor abre outras tasks em [[wiki/concepts/worktree-paralelismo|worktrees]]. A promessa de "100% de segurança" não se sustenta no próprio vídeo: o autor termina dizendo que teria de testar mais.

## Key Claims

1. **A boa engenharia de contexto começa em documentos revisados por humanos.** Evidência: RFCs, ADRs, PRDs e design docs como fonte da verdade; a partir dali a IA enriquece o contexto e escreve o código. O design doc demonstrado tem contexto do projeto, APIs, MVP, tarefas e o que está definido ou não. Ver [[wiki/concepts/design-doc]]. Confiança: média, argumento de prática com um único caso.

2. **O agente pode auditar o design doc antes de quebrar tarefas.** Evidência: o agente leu o documento pelo MCP e apontou webhooks e tratamento de falhas como indefinidos, além da falta de definição de pacote e arquitetura. O autor atribui esta última lacuna ao agente não ter carregado os padrões do projeto. Confiança: alta para o que a demonstração mostra, média para generalizar.

3. **O setup mínimo tem três camadas: rules com o básico e o mapa da documentação, skills para capacidades e MCPs para o que está fora.** Evidência: rule sempre carregada que aponta para `docs/` conforme o tipo de task; skills de Confluence e Jira; MCPs da Atlassian e do Context7. O [Atlassian Rovo MCP Server](https://support.atlassian.com/rovo/docs/atlassian-remote-mcp-server/) `[external]` existe e dá acesso a Jira e Confluence Cloud. O Context7 não foi conferido. Confiança: alta para o desenho, que coincide com [[wiki/concepts/progressive-disclosure-ia]].

4. **"Rules são do Cursor", e o mercado separou documentação em AGENTS.md e capacidades em skills.** Evidência: fala do autor. A [documentação do Cursor](https://cursor.com/docs/context/rules) `[external]` confirma que o Cursor adota `.cursor/rules` e `AGENTS.md`. "Só do Cursor" é impreciso: o Claude Code tem `.claude/rules/`, como registra [[wiki/concepts/rules-agente]]. Confiança: alta para a correção.

5. **MCP é para o que é remoto; skill é local e tática.** Evidência: definição do autor. Serve como regra de bolso, mas MCP também roda localmente sobre STDIO ([[wiki/concepts/model-context-protocol]]). Confiança: média.

6. **Por padrão, a IA quebra tasks em tamanho humano, pequenas demais para um agente.** Evidência: a primeira quebra separou configurar credencial de instalar o SDK; o autor pediu uma task por fase. Na task, só contexto de alto nível, porque ela depois vira plano. Confiança: média, um caso.

7. **A IA consegue estimar esforço e apontar o que dá para paralelizar.** Evidência: o agente deu estimativas e sugestões, mas uma delas dependia de um client que ainda não existia, e o autor a descartou. Nenhuma estimativa foi comparada com o tempo real. Confiança: baixa para a estimativa.

8. **Abrir contexto novo a cada fase e ficar em no máximo 30% de uma janela de 200.000 tokens.** Evidência: a conversa de quebra chegou a 44%, e o autor afirma que qualquer prompt ali "vai começar a alucinar". Os planos ficaram em 31%, 34% e 37%, acima da própria meta. Não há medição. A wiki registra outras faixas: ~40% em [[wiki/concepts/dumb-zone]] e ~60% no vídeo anterior do mesmo autor. Confiança: alta para a direção, baixa para o número.

9. **Planejar com modelo melhor e executar com modelo mais barato, em agente novo.** Evidência: plano com Sonnet e execução com Composer, "bem mais rápido e mais barato". A [tabela atual do Cursor](https://cursor.com/docs/models) `[external]` lista Composer 2.5 a US$ 0,50/2,50 por milhão de tokens (entrada/saída), contra US$ 3/15 do Claude 4.6 Sonnet; a variante Fast custa os mesmos US$ 3/15. O vídeo não diz qual versão usou, e a página não traz números de velocidade. Ver [[wiki/concepts/modelo-por-leverage-tarefa]]. Confiança: alta para o padrão, média para o preço na época do vídeo.

10. **Cada lacuna de plano vira melhoria na documentação, até o "Nirvana".** Evidência: a rule com os comandos corretos de migration. O autor diz que levou dias para montar o contexto e que a documentação cobre só o que é específico do projeto. Confiança: média.

11. **Só paralelize quando as tasks não dependem de infraestrutura comum ainda inexistente.** Evidência: no início, "um vai tentar criar coisa do outro". Depois, um bug independente (login com e-mail em maiúsculas) foi feito em worktree enquanto a feature rodava. Confiança: alta.

12. **Worktree é "meio que uma nova branch", e o Cursor devolve a mudança à branch principal.** Evidência: demonstração com apply. A descrição é imprecisa: a [documentação do Git](https://code.googlesource.com/git/+/refs/tags/v2.29.2/Documentation/git-worktree.txt) `[external]` define worktree como uma árvore de trabalho adicional do mesmo repositório. A [documentação atual do Cursor](https://cursor.com/docs/configuration/worktrees) `[external]` fala em checkouts isolados e em `/apply-worktree`, sem detalhar conflitos. A interface mostrada pode ser de versão antiga. Confiança: alta para a correção.

13. **A geração que entra agora já chega com mentalidade de paralelização.** Evidência: opinião, sem dados. O próprio autor admite que trocar de contexto "não é uma coisa boa". Ver o limite de atenção em [[wiki/concepts/paralelismo-de-tarefas-ia]]. Confiança: baixa.

14. **Dias de trabalho em minutos, com 100% de segurança.** Evidência: nenhuma medição. O vídeo diz "alguns minutos" na abertura e "uma hora que ia levar 7 dias" no meio, não mostra testes da última task e admite que faltou escrever testes no plano. Confiança: baixa, tratar como chamada de vídeo.

## Tensões com a wiki

- **Plano horizontal.** As tasks demonstradas (setup, persistência, core services, APIs REST) têm a forma que [[wiki/concepts/rpi-workflow]] lista como anti-padrão e que [[wiki/concepts/plano-vertical]] evita: nada ponta a ponta é testável no meio. O autor não comenta esse ponto.
- **Research sem fase própria.** O modo de plano pesquisa e planeja na mesma sessão, o que [[wiki/concepts/rpi-workflow]] marca como anti-padrão, apesar de o autor citar RPI. O custo aparece nos 31% a 37% de contexto ao fim de cada plano.
- **Migrations em paralelo.** A task de persistência rodou migrations enquanto o bug era tratado em worktree. O vídeo não mostra o banco compartilhado, limitação registrada em [[wiki/concepts/worktree-paralelismo]].

## Entities

- [[wiki/entities/valdemar-neto]]: autor, pela autoapresentação.
- [[wiki/entities/cursor]]: ferramenta central.
- [[wiki/entities/stripe]]: vendor da integração.
- Sem página própria: Confluence, Jira, Atlassian, Notion, Context7, FakeFlix.

## Concepts

[[wiki/concepts/design-doc]], [[wiki/concepts/rpi-workflow]], [[wiki/concepts/progressive-disclosure-ia]], [[wiki/concepts/rules-agente]], [[wiki/concepts/skills-agente]], [[wiki/concepts/agents-md-vs-claude-md]], [[wiki/concepts/model-context-protocol]], [[wiki/concepts/janela-de-contexto]], [[wiki/concepts/plan-mode]], [[wiki/concepts/modelo-por-leverage-tarefa]], [[wiki/concepts/worktree-paralelismo]], [[wiki/concepts/paralelismo-de-tarefas-ia]], [[wiki/concepts/arquitetura-modular]].

## Open Questions

- A meta de 30% tem alguma medição, ou é só experiência do autor?
- Tasks por camada são aceitáveis quando o plano de cada uma é revisado, ou o custo aparece só na integração?
- Quanto tempo a feature levou de fato, contando revisão, testes e a construção prévia do contexto?
- O PDF do design doc prometido no vídeo não foi ingerido.

## Raw Quotes

> "O importante é criar o contexto para começar."

> "Cada fase deve ser uma task, para facilitar o desenvolvimento."

> "Não é muita documentação, é só as principais, as coisas que não são normais."
