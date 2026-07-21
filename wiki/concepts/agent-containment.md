---
type: concept
title: "Agent Containment (Contenção de Agentes de IA)"
aliases: ["agent containment", "contenção de agente", "sandboxing de agente de ia", "ai jail"]
date_created: 2026-07-20
date_updated: 2026-07-21
source_count: 3
tags: [agent-containment, sandboxing, security, defense-in-depth, principio-do-menor-privilegio, ai-safety, harness]
skill: tech-mentor-security
status: stable
---

# Agent Containment (Contenção de Agentes de IA)

Camada de defesa que isola o processo de um agente de IA (coding agent, LLM com tool calling) do restante do sistema, limitando o que ele pode ler, escrever e acessar mesmo que seja comprometido ou instruído a agir de forma maliciosa. É a última linha de defesa dentro do modelo de guardrails de LLM: **input filters** (detectar intenção maliciosa) → **output filters** (grounding, PII, policy) → **containment** (sandboxing, circuit breaker) — ver [[wiki/sources/ai-safety-guardrails]].

## Por Que Existe

Conforme [[wiki/concepts/harness]] descreve: "a LLM apenas orquestra, o harness executa" — quando um agente pede para rodar `npm install`, `grep` ou um script qualquer, é o processo local do harness que executa o comando na máquina do usuário, não um sandbox remoto do provedor. Isso significa que qualquer dependência comprometida por um ataque de [[wiki/concepts/supply-chain-security|supply chain]] roda com os mesmos privilégios do agente — incluindo acesso a credenciais AWS, chaves SSH e o restante do filesystem do usuário.

## Exemplo Concreto: AI Jail

[[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] descreve o **AI Jail**, ferramenta de [[wiki/entities/fabio-akita]] construída sobre o [[wiki/entities/bubblewrap]] (o mesmo sandbox usado pelo Flatpak para isolar apps de desktop no Linux). Mecanismo:

- A pasta `home` do usuário é substituída por um diretório temporário vazio dentro da cela — credenciais (`~/.aws/credentials`, chaves SSH) ficam invisíveis.
- Apenas o diretório do projeto atual é exposto, com granularidade de leitura/escrita configurável por subpasta (ex.: `.claude/` como somente leitura).
- O arquivo de configuração da cela é comitável no repositório — qualquer dev que clonar o projeto herda a mesma política de isolamento, tornando a contenção parte do projeto e não uma escolha individual.
- Flags: `--dry-run` (audita sem executar), `--lockdown` (corta rede + read-only, para código de terceiros não confiável), `--bootstrap` (gera permissões automáticas para o Claude Code).

## Sem Porta dos Fundos vs. Sandbox com Opt-out

O ponto mais importante levantado pela fonte: o sandbox nativo do [[wiki/entities/claude-code]] (desde outubro de 2025) usa o mesmo stack técnico (Bubblewrap/Sandbox-exec), mas permite que o próprio agente reexecute um comando bloqueado pulando a restrição — um padrão de retry ativado por padrão. O AI Jail não tem esse mecanismo: o processo roda inteiramente dentro do `bwrap`, sem flag de escape. A diferença não é o mecanismo de isolamento, é **quem controla a saída da cela** — o usuário/configuração, ou o próprio agente.

## Contenção Como Uma de Três Camadas

A fonte propõe empilhar contenção de sessão com duas outras camadas independentes — ver [[wiki/concepts/defense-in-depth]]:

1. **Sessão** (AI Jail) — isola o processo em execução agora.
2. **Código** (Git com push manual) — permite reverter dano ao filesystem do projeto via `git checkout`, mesmo que a cela falhe.
3. **Sistema operacional imutável** — ver [[wiki/concepts/sistema-operacional-imutavel]] — garante que, mesmo se algo escapar da cela, a raiz do sistema volta ao estado original no próximo reboot.

## Recomendação Oficial: Sandbox para Loops Não Interrompidos

A própria Anthropic recomenda usar algum mecanismo de sandbox (VM, container ou dev container) sempre que o [[wiki/entities/claude-code]] roda em um loop não interrompido — sem um humano aprovando cada passo, como em automações de longa duração (`/go`, ver [[wiki/concepts/gerenciamento-de-sessoes-claude-code]]). A justificativa é a mesma da contenção de sessão descrita acima: sem alguém revisando cada ação em tempo real, o isolamento do processo passa a ser a única barreira prática contra um comando destrutivo ou uma dependência maliciosa.

## Relação com Outros Conceitos

- [[wiki/concepts/principio-do-menor-privilegio]] — a contenção é PoLP aplicado ao próprio agente de IA, não só a serviços/usuários humanos.
- [[wiki/concepts/defense-in-depth]] — contenção é uma camada entre várias, nunca a única linha de defesa.
- [[wiki/concepts/attack-surface]] — reduzir o que o agente enxerga do filesystem reduz diretamente sua superfície de ataque efetiva.
- [[wiki/concepts/harness]] — explica por que a execução local de tool calls é o vetor que a contenção precisa mitigar.

## Key Sources

- [[wiki/sources/ai-safety-guardrails]] — containment como terceira camada do modelo de guardrails de LLM (input filters → output filters → containment)
- [[wiki/sources/ai-jail-sandbox-para-agentes-de-ia-akita]] — implementação concreta via Bubblewrap, comparação com o sandbox nativo do Claude Code
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — recomendação oficial da Anthropic de usar VM/container/dev container para loops de agente não interrompidos
