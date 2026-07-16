---
type: concept
title: "Code Review"
aliases: ["revisão de código", "pull request review", "PR review"]
date_created: 2026-07-03
date_updated: 2026-07-16
source_count: 4
tags: [code-review, qualidade, carreira, júnior, mentoria, grill-me]
skill: tech-mentor-leadership
status: draft
---

# Code Review

Processo de revisão do código de um pull request por outra pessoa antes de ele ir para produção. Existe para pegar problemas de regra de negócio, legibilidade e padrão antes que virem custo em produção — não para avaliar a pessoa.

## Prioridade na revisão

1. **Regra de negócio primeiro:** o código faz o que a tarefa pedia? Código limpo que não resolve o pedido do PO não serve.
2. **Estilo e padrão depois:** formatação, nomes, convenções específicas da empresa.

Inverter essa ordem — obcecar por estilo antes de confirmar que a funcionalidade está correta — é o erro mais comum em quem está aprendendo a revisar.

## Por que o primeiro code review de um júnior costuma vir cheio de comentários

Na maioria dos casos não é sobre competência: é sobre desconhecimento do padrão específico daquela empresa (framework, convenções, jeito de estruturar código). Leva tempo até internalizar esse padrão — e enquanto isso, comentários recorrentes são esperados, não um sinal de fracasso.

Quem revisa também costuma ter pouco tempo e pouca prática em dar feedback com tato — comentários secos refletem falta de tempo, não intenção de humilhar.

## Antes de abrir o PR

- Confirmar com o PO/time que não há outra prioridade na fila.
- Testar em [[wiki/concepts/paridade-local-producao|ambiente externo]] (dev/homologação), não só localmente.
- Revisar o próprio código (com IA ou colega mais experiente) pedindo explicação do "porquê" de cada sugestão — ver [[wiki/concepts/dependencia-ia]] para o risco de fazer isso sem entender.

## Depois de receber comentários

A crítica é ao código, não à pessoa — ver [[wiki/concepts/inteligencia-emocional]]. Reagir defensivamente atrapalha mais do que ajuda. Vale manter um registro dos apontamentos recorrentes para não repetir o mesmo erro no próximo PR.

## Depois do merge

O trabalho não termina no merge: validar manualmente em produção após o deploy faz parte do ciclo — ver [[wiki/concepts/pensamento-em-producao]].

## Code review como método de treino de design, não só de correção

[[wiki/sources/filosofia-do-design-de-software-introducao]] (John Ousterhout) argumenta que code review é o veículo prático recomendado para aplicar princípios de design abstratos: é mais fácil ver problemas de design no código de outra pessoa do que no próprio. A ferramenta concreta são os [[wiki/concepts/red-flags-de-design|red flags de design]] — sinais de que um trecho está mais complicado do que precisa. Isso é um ângulo diferente do já documentado nesta página (que foca em regra de negócio e comunicação): aqui code review é também prática deliberada de reconhecimento de complexidade desnecessária, que compõe ao longo do tempo com a experiência de quem revisa.

## Code review como antídoto a dívida cognitiva em times com IA

Em times que usam IA generativa/agêntica pesadamente, [[wiki/concepts/divida-cognitiva]] prescreve code review como um dos três checkpoints regulares para reconstruir entendimento compartilhado — junto com retrospectivas. A régua concreta: **nenhuma mudança gerada por IA vai para produção sem que ao menos uma pessoa consiga explicar totalmente o que ela faz e por quê**, não apenas confirmar que os testes passaram. Isso é mais estrito do que o critério de "regra de negócio primeiro" já documentado acima — aqui o objetivo não é só corrigir bug de escopo, é garantir que a teoria do programa (ver [[wiki/concepts/teoria-do-programa-naur]]) não se perca entre a geração pela IA e o merge.

## Por Que o "Looking Good to Me" Aumentou com Agentes Autônomos

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] descreve o mecanismo por trás da degradação do code review na era de agentes com harness próprio: quando o agente rodava de forma mais incremental (ex.: Claude Code via CLI sendo corrigido passo a passo), o dev participava do processo de criação e revisava naturalmente ao longo do caminho. Com agentes que rodam por mais tempo, escrevem os próprios testes automatizados e entram em loops longos, não sobra tempo de revisar tudo antes de concluir a tarefa com qualidade — e, como "ninguém gosta de ler código", a tendência é aprovar sem ler linha a linha (o "looking good to me" superficial). A mitigação proposta não é revisar mais, mas inverter quem audita quem: a skill [[wiki/concepts/skills-agente|Grill Me]] ([[wiki/entities/matt-pocock]]) faz a IA entrevistar o dev sobre decisões de implementação até garantir entendimento mútuo, como substituto parcial da leitura linha a linha.

## Relacionado

- [[wiki/concepts/definicao-de-pronto]] — code review é um dos critérios de "pronto"
- [[wiki/concepts/mentoria-tecnica]] — quem revisa está, na prática, mentorando
- [[wiki/concepts/sindrome-do-impostor]] — reação emocional comum a comentários de review
- [[wiki/concepts/red-flags-de-design]] — heurística concreta para o que procurar durante a revisão
- [[wiki/concepts/divida-cognitiva]] — code review como checkpoint contra fragmentação de entendimento compartilhado em times com IA

## Key Sources

- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — code review como checkpoint de entendimento compartilhado, requisito mínimo de "uma pessoa entende totalmente" antes do deploy
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — "looking good to me" como sintoma de agentes autônomos de longa duração; skill Grill Me como mitigação
