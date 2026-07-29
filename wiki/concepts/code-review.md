---
type: concept
title: "Code Review"
aliases: ["revisão de código", "pull request review", "PR review"]
date_created: 2026-07-03
date_updated: 2026-07-29
source_count: 10
tags: [code-review, qualidade, carreira, júnior, mentoria, grill-me, babysitting-de-agentes, quality-gate, under-engineering]
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
- Limpar o próprio histórico com [[wiki/concepts/rebase-vs-merge|rebase local]] antes de abrir o PR — commits atômicos e mensagens claras reduzem o esforço de quem revisa; merge fica reservado para a integração final na branch compartilhada.

## Depois de receber comentários

A crítica é ao código, não à pessoa — ver [[wiki/concepts/inteligencia-emocional]]. Reagir defensivamente atrapalha mais do que ajuda. Vale manter um registro dos apontamentos recorrentes para não repetir o mesmo erro no próximo PR.

## Depois do merge

O trabalho não termina no merge: validar manualmente em produção após o deploy faz parte do ciclo — ver [[wiki/concepts/pensamento-em-producao]].

## Code review como método de treino de design, não só de correção

[[wiki/sources/filosofia-do-design-de-software-introducao]] (John Ousterhout) argumenta que code review é o veículo prático recomendado para aplicar princípios de design abstratos: é mais fácil ver problemas de design no código de outra pessoa do que no próprio. A ferramenta concreta são os [[wiki/concepts/red-flags-de-design|red flags de design]] — sinais de que um trecho está mais complicado do que precisa. Isso é um ângulo diferente do já documentado nesta página (que foca em regra de negócio e comunicação): aqui code review é também prática deliberada de reconhecimento de complexidade desnecessária, que compõe ao longo do tempo com a experiência de quem revisa. O livro completo, ingerido em [[wiki/sources/filosofia-do-design-de-software-livro-completo]], fecha o catálogo com 14 red flags nomeados (ver tabela em [[wiki/concepts/red-flags-de-design]]) — checklist prático concreto para usar durante revisão, além da regra "regra de negócio primeiro" já documentada nesta página.

## Code review como antídoto a dívida cognitiva em times com IA

Em times que usam IA generativa/agêntica pesadamente, [[wiki/concepts/divida-cognitiva]] prescreve code review como um dos três checkpoints regulares para reconstruir entendimento compartilhado — junto com retrospectivas. A régua concreta: **nenhuma mudança gerada por IA vai para produção sem que ao menos uma pessoa consiga explicar totalmente o que ela faz e por quê**, não apenas confirmar que os testes passaram. Isso é mais estrito do que o critério de "regra de negócio primeiro" já documentado acima — aqui o objetivo não é só corrigir bug de escopo, é garantir que a teoria do programa (ver [[wiki/concepts/teoria-do-programa-naur]]) não se perca entre a geração pela IA e o merge.

## Por Que o "Looking Good to Me" Aumentou com Agentes Autônomos

[[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] descreve o mecanismo por trás da degradação do code review na era de agentes com harness próprio: quando o agente rodava de forma mais incremental (ex.: Claude Code via CLI sendo corrigido passo a passo), o dev participava do processo de criação e revisava naturalmente ao longo do caminho. Com agentes que rodam por mais tempo, escrevem os próprios testes automatizados e entram em loops longos, não sobra tempo de revisar tudo antes de concluir a tarefa com qualidade — e, como "ninguém gosta de ler código", a tendência é aprovar sem ler linha a linha (o "looking good to me" superficial). A mitigação proposta não é revisar mais, mas inverter quem audita quem: a skill [[wiki/concepts/skills-agente|Grill Me]] ([[wiki/entities/matt-pocock]]) faz a IA entrevistar o dev sobre decisões de implementação até garantir entendimento mútuo, como substituto parcial da leitura linha a linha.

## Babysitting: o Agente Fecha o Próprio Loop de Revisão

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] descreve um padrão que reorganiza quem participa do ciclo de code review quando o volume de PRs gerados por IA excede a capacidade humana de revisar: depois de abrir o PR, o próprio agente entra em **babysitting** — checando repetidamente se o CI está verde e se revisores (Copilot, ferramenta externa, ou humano) deixaram comentários, endereçando-os e resolvendo as conversas no GitHub, até o PR estar pronto para merge sem intervenção humana no meio do processo. Isso não elimina a revisão humana (que continua acontecendo via comentários no PR), mas remove o humano do loop de "verificar se o CI passou e corrigir o óbvio" — liberando tempo de revisão para julgamento de mais alto nível. O autor identifica essa mudança como a origem de um novo gargalo: **o humano vira o gargalo do próprio processo de revisão**, porque não é possível paralelizar a leitura de código na mesma proporção em que os agentes paralelizam a geração — "não consigo entregar quatro tarefas ao mesmo tempo se precisar ler 10.000 linhas de código por dia". A resposta proposta não é revisar mais rápido, mas colocar [[wiki/concepts/quality-gate|quality gates]] automatizados com [[wiki/concepts/ratchet-baseline|ratchet]] para barrar regressões antes mesmo de chegarem à revisão humana, partindo da premissa de que "como qualquer controle de qualidade, o humano é falho".

## Tipos genéricos como item recorrente de review

[[wiki/sources/underengineering-overengineering-mario-souto]] cita dois apontamentos de review que se repetem na prática e que a fonte conecta a [[wiki/concepts/under-engineering]] (falta de flexibilidade/robustez, não excesso dela): tipos genéricos demais (`any` em TypeScript) em vez de tipos específicos, e passar tipos primitivos (string) onde um enum representaria melhor um conjunto fechado de valores (ex.: tipos de pagamento passados como string solta). O ponto não é "tipar tudo por tipar" — é que a ausência de tipo específico é, na prática, ausência de validação, o mesmo sintoma de under-engineering que aparece em "ausência de checks automatizados".

## Arquivo Dedicado de Review no Claude Code

A recomendação oficial da Anthropic para o [[wiki/entities/claude-code]] é manter um arquivo separado (`review`) com instruções pertinentes só a code review — critérios do que checar, o que ignorar — mantendo informações gerais do projeto no [[wiki/concepts/claude-md|CLAUDE.md]]. Separar os dois evita que o contexto de review fique diluído entre regras de projeto e critérios de revisão, e vice-versa. O Claude Code também expõe um comando `/code-review`, recomendado com o effort "ultra" para revisões de código substancial e complexo.

## Migrations de Banco Como Código Sujeito a Review

O critério "regra de negócio primeiro" e a exigência de pull request/versionamento não se limitam a código de aplicação: [[wiki/concepts/database-migration|migrations de banco de dados]] deveriam passar pelo mesmo processo. Rodar DDL manualmente contra o banco (SSH direto na cloud, sem PR nem git) quebra o requisito básico de auditabilidade e reprodutibilidade que qualquer outra mudança de código já tem — mesmo quando quem executa é uma pessoa experiente administrando o banco. Ver [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]].

## Relacionado

- [[wiki/concepts/definicao-de-pronto]] — code review é um dos critérios de "pronto"
- [[wiki/concepts/mentoria-tecnica]] — quem revisa está, na prática, mentorando
- [[wiki/concepts/sindrome-do-impostor]] — reação emocional comum a comentários de review
- [[wiki/concepts/red-flags-de-design]] — heurística concreta para o que procurar durante a revisão
- [[wiki/concepts/divida-cognitiva]] — code review como checkpoint contra fragmentação de entendimento compartilhado em times com IA
- [[wiki/concepts/rebase-vs-merge]] — rebase local antes do PR, merge para integrar

## Key Sources

- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]]
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — code review como checkpoint de entendimento compartilhado, requisito mínimo de "uma pessoa entende totalmente" antes do deploy
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — "looking good to me" como sintoma de agentes autônomos de longa duração; skill Grill Me como mitigação
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — babysitting de PR pelo próprio agente (loop de CI + comentários + resolução de conversas); humano como gargalo de revisão em escala
- [[wiki/sources/underengineering-overengineering-mario-souto]] — tipos genéricos (`any`) e primitivos soltos em vez de enum como itens recorrentes de review, ligados a under-engineering
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — arquivo dedicado `review` separado do CLAUDE.md; `/code-review --ultra` para revisões complexas
- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — migrations de banco tratadas com o mesmo processo de PR/review que código de aplicação
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — catálogo completo dos 14 red flags do livro, checklist prático para revisão
- [[wiki/sources/git-rebase-na-pratica]] — mecânica de rebase local usada para chegar a um histórico limpo antes do PR
