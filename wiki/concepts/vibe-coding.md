---
type: concept
title: "Vibe Coding"
aliases: ["vibe coding", "vibe-coding", "coding por vibração", "agentic coding", "orquestração de agentes"]
date_created: 2026-04-23
date_updated: 2026-04-26
source_count: 2
tags: [vibe-coding, agentes-ia, produtividade, divida-cognitiva, ai-brainfry, paralelismo-cognitivo]
skill: tech-mentor-ai
status: stable
---

## Definição

Vibe Coding é o padrão de trabalho onde o desenvolvedor orquestra múltiplos agentes de IA em paralelo, submetendo prompts continuamente enquanto aguarda resultados anteriores — criando múltiplas threads de desenvolvimento simultâneas.

O nome captura a sensação: você está "no flow", no ritmo, gerando código em alta velocidade. A paralisia aparece depois.

## O loop do Vibe Coding

```
1. Iniciar feature A → agente trabalha
2. Pensar em melhoria B → iniciar em background
3. Terceira ideia C → iniciar
4. Quarta ideia D → iniciar
...
N. Uma hora depois: 5 coisas iniciadas, metade de 3 implementadas
   Qual era a tarefa principal?
```

Resposta do dev: mais prompts → replanejamento → sensação de produtividade → mais prompts → sem entrega real.

## Por que o planejamento vicia

O looping entre prompt e replanejamento é reforçado positivamente:
- Planejar dá sensação de controle
- Gerar código dá sensação de progresso
- Revisar e finalizar é cognitivamente custoso e menos imediato

O resultado: alta iniciativa, baixa acabativa. Muitas branches abertas, poucos pull requests fechados.

## O gargalo real

> "A produtividade nunca foi o gargalo real. O gargalo real é a coerência, o foco, a finalização e o julgamento — saber o que você está fazendo e por quê."

Vibe Coding resolve o gargalo errado. Gera velocidade onde não havia gargalo; cria paralisia onde havia clareza.

## Quando Vibe Coding funciona

- Prototipagem exploratória sem compromisso de produção
- Tarefas isoladas com escopo claro e curto
- Geração de boilerplate bem definido

## Quando Vibe Coding falha

- Features que exigem decisões de arquitetura
- Qualquer código que vai para produção sem revisão humana compreensiva
- Times onde o entendimento compartilhado é crítico

## Mitigações práticas

**One task at a time** — um agente por vez, finalizar antes de iniciar.

**Definition of done inclui explicabilidade** — se você não consegue explicar o que foi gerado, não está pronto.

**Time-box de orquestração** — máximo de N agentes paralelos por sessão (N=2 é um bom começo).

**Review obrigatório antes de commit** — não aprovar o que não foi lido linha a linha.

## Relação com outros conceitos

- [[concepts/divida-cognitiva]] — vibe coding é o principal vetor de acúmulo de dívida cognitiva
- [[concepts/ai-brainfry]] — vibe coding em excesso leva a brainfry
- [[concepts/agentes-orquestracao]] — orquestração de agentes bem feita é o oposto de vibe coding

## O paradoxo do engenheiro autônomo

Vibe Coding não é exclusivo de quem perde controle. Um dev experiente e autônomo pode entrar no mesmo loop por escolha própria — e o burnout chega sem que ninguém tenha obrigado nada.

Antes: tarefa de 2 dias → termina em 2h → para, paga tech debt.
Agora: termina uma tarefa → 5 agentes já estão em outras → nunca para.

Ver [[sources/ia-salario-ou-carga-de-trabalho]] para o relato de primeira mão.

## Risco de Qualidade no Código Gerado

LLMs geram código para o caminho feliz. Os problemas invisíveis em dev que explodem em prod:
- **N+1 queries** — loops com queries individuais em vez de batch/JOIN (→ [[n-plus-um-detector]])
- **Race conditions** — sequências assíncronas sem considerar concorrência (→ [[property-based-testing]])
- **Memory leaks** — caches sem TTL, filas que nunca esvaziam

Quem não sabe verificar esses problemas não consegue revisar o código que a IA gerou. Ver [[sources/apagao-de-seniors-vibe-coding]] para técnicas práticas de detecção.

## Key Sources

- [[sources/divida-cognitiva-ai-brainfry]]
- [[sources/ia-salario-ou-carga-de-trabalho]]
- [[sources/apagao-de-seniors-vibe-coding]]
- [[sources/roadmap-dev-senior-2026]] — pilar 5: ciclo de degradação via IA → ver [[concepts/ia-ciclo-dependencia]]
- [[sources/por-que-devs-nao-terminam-projetos]] — vibe coding elimina o mecanismo de luta → ver [[concepts/aprendizado-por-luta]]
