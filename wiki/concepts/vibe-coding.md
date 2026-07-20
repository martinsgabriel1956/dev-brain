---
type: concept
title: "Vibe Coding"
aliases: ["vibe coding", "vibe-coding", "coding por vibração", "agentic coding", "orquestração de agentes"]
date_created: 2026-04-23
date_updated: 2026-07-19
source_count: 7
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
- [[mvp|MVPs]], documentação e testes — tarefas repetitivas de baixo esforço intelectual que a IA executa rápido e de forma confiável com um bom prompt, validando hipóteses de negócio (ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]])

## O Limite Não É Técnico, É de Julgamento

Vender um sistema puramente vibe-coded como pronto para produção é uma ilusão — e desonesto quando quem vende já tem conhecimento técnico e ignora os riscos, ou não tem e finge que a IA resolveu tudo. O que a IA não supre sozinha:

- Arquitetura e integrações entre sistemas
- Segurança sem brechas exploráveis
- [[wiki/concepts/contexto-organizacional-para-arquitetura|Contexto organizacional]]: maturidade de plataforma, processo, know-how da empresa
- Análise de custo real vs. disposição do cliente a pagar

O uso saudável da IA por um arquiteto é para brainstorm, alternativas e explicar trade-offs — nunca para substituir o [[wiki/concepts/pensamento-critico|pensamento crítico]] sobre o negócio. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Quando Vibe Coding falha

- Features que exigem decisões de arquitetura
- Qualquer código que vai para produção sem revisão humana compreensiva
- Times onde o entendimento compartilhado é crítico

## Mitigações práticas

**One task at a time** — um agente por vez, finalizar antes de iniciar.

**Definition of done inclui explicabilidade** — se você não consegue explicar o que foi gerado, não está pronto.

**Time-box de orquestração** — máximo de N agentes paralelos por sessão (N=2 é um bom começo).

**Review obrigatório antes de commit** — não aprovar o que não foi lido linha a linha.

**RFC como fonte da verdade + skill "Grill Me" invertendo quem revisa quem** — [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] documenta uma mitigação de duas pernas: (1) [[wiki/concepts/rfc-request-for-comments|RFC]] escrita antes de codar, como norte que evita que a IA viole arquitetura; (2) a skill **Grill Me** ([[wiki/entities/matt-pocock]]), que faz a IA entrevistar o dev sobre decisões de implementação até entendimento mútuo — em vez do dev ler linha a linha o código gerado, é a IA que audita o entendimento do dev. É uma resposta direta ao mesmo sintoma já documentado nesta página ("a gente para de revisar código gerado pela IA, depois para até de revisar as próprias regras do sistema") quando os agentes passaram a rodar por mais tempo com harness próprio, sem deixar janela de revisão incremental.

## Ratchet de Baseline como Mitigação Mecânica (Não Depende de Disciplina)

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] documenta uma mitigação de natureza diferente das duas anteriores (RFC e Grill Me, que dependem de disciplina humana de planejar/entender): o padrão [[wiki/concepts/ratchet-baseline]], que bloqueia mecanicamente, via CI, qualquer PR que piore métricas de qualidade em relação a uma baseline congelada. A vantagem declarada pelo autor é que isso permite deixar a IA escrever ~100% do código gerado por múltiplos agentes em paralelo sem depender de o dev revisar linha a linha — o controle de qualidade vira parte do pipeline, não do julgamento de quem está no flow do vibe coding.

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

## Vibe Coding como Hype em Formação

Citado como exemplo de hype tecnológico em formação (junto com MCP) no momento de [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]] — um assunto que "pipocava" repetidamente em múltiplos canais simultaneamente. Ver [[wiki/concepts/avaliar-hype-tecnologico]] para o modelo de decisão sobre quando vale a pena embarcar num hype como este.

## "Specs to Code" É Vibe Coding com Outro Nome

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] argumenta que o movimento "specs to code" (nunca olhar o código gerado, só editar a especificação e reexecutar) é, na prática, vibe coding disfarçado de disciplina: mesmo padrão de decadência progressiva do código a cada rodada, só que sem a sensação óbvia de estar "no flow". A saída proposta pelo autor não é abandonar [[wiki/concepts/spec-driven-development|SDD]], mas reintroduzir disciplina de design — [[wiki/entities/fred-brooks|design concept]] compartilhado, [[wiki/concepts/ddd|linguagem ubíqua]] e [[wiki/concepts/modulo-profundo|módulos profundos]] — antes de qualquer geração de código.

## Key Sources

- [[sources/divida-cognitiva-ai-brainfry]]
- [[sources/ia-salario-ou-carga-de-trabalho]]
- [[sources/apagao-de-seniors-vibe-coding]]
- [[sources/roadmap-dev-senior-2026]] — pilar 5: ciclo de degradação via IA → ver [[concepts/ia-ciclo-dependencia]]
- [[sources/por-que-devs-nao-terminam-projetos]] — vibe coding elimina o mecanismo de luta → ver [[concepts/aprendizado-por-luta]]
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — onde vibe coding brilha (MVP, docs, testes) vs. onde exige julgamento humano (arquitetura, segurança, contexto de negócio)
- [[wiki/sources/como-identificar-o-proximo-hype-tecnologico]] — citado como exemplo de hype em formação, no momento do vídeo
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] — "specs to code" como vibe coding disfarçado
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — RFC + skill Grill Me como mitigação prática à perda de janela de revisão incremental
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — ratchet de baseline como mitigação mecânica via CI, alternativa/complemento à disciplina de RFC e Grill Me
