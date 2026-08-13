---
type: concept
title: "Code Review"
aliases: ["revisão de código", "pull request review", "PR review"]
date_created: 2026-07-03
date_updated: 2026-08-13
source_count: 17
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

## De "Estilo Bonito" Para "Prova Objetiva": o Argumento Numérico por Trás da Mudança

[[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] dá o argumento quantitativo por trás da mesma mudança já descrita acima (babysitting, humano como gargalo): se metade do diff médio de um PR já não é mais digitado por humano — a fonte cita um survey do Pragmatic Engineer com taxa de aceitação de código de IA entre 30% e 55%, crescente —, a pergunta que orienta a revisão deixa de ser sobre estilo ("esse for loop está bonito?") e passa a ser sobre prova objetiva: o código passa em critérios que rodam no CI em segundos, sem exigir leitura humana? Isso não substitui os critérios já documentados nesta página (regra de negócio primeiro, entendimento compartilhado) — desloca o *primeiro* filtro, antes da revisão humana começar, para os quatro gates concretos descritos em [[wiki/concepts/quality-gate]] ([[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]], cobertura+[[wiki/concepts/teste-de-mutacao|mutation testing]], tamanho de módulo, [[wiki/concepts/acoplamento|estrutura de dependências]]).

## O Gargalo Migra da Escrita para a Revisão (dados Faros AI)

[[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] dá o número que fecha o argumento de "humano como gargalo" já descrito acima em *babysitting*: enquanto a produção individual dobra com IA (~2x PRs mergeados por dev), o **tempo de code review sobe 91%** e não escala junto — a revisão exige julgamento e contexto que a IA não substitui. É o núcleo do [[wiki/concepts/paradoxo-da-aceleracao]]: acelerou-se a etapa errada. Detalhe importante para quem revisa: **código gerado por IA não é mais fácil de revisar — às vezes é mais difícil**, porque é tecnicamente válido (passa nos testes) mas pode ser arquiteturalmente errado (ver [[wiki/concepts/ia-como-amplificador]] e [[wiki/concepts/gaming-de-testes-por-ia]]). Métrica de outcome para vigiar o gargalo: se o último PR levou **mais de uma semana** para mergear, o problema é o processo, não a pessoa — adicionar mais PRs piora (ver [[wiki/concepts/output-vs-outcome]]).

## O Tempo de Revisão Não Escala Com o Tamanho do PR

[[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] argumenta que a razão mecânica por trás de PRs grandes ficarem mal revisados não é preguiça — é que quem revisa dedica, na prática, a mesma janela de tempo (~20-30 min) tanto para um PR de 200 quanto de 2.000 linhas, porque a jornada de trabalho já está alocada em outras tarefas. O resultado é que a mesma quantidade absoluta de bugs encontrados representa uma cobertura proporcionalmente muito menor no PR grande — o review não "escala" com o tamanho do PR. Nos extremos, isso quebra de duas formas: um PR de ~20.000 linhas recebe efetivamente zero revisão real, e dedicar 5 horas contínuas a um único PR deixa de ser "rápido" (quase um dia de trabalho perdido, com o ciclo de idas e vindas empurrando o merge para semanas depois).

**Tamanho ótimo sugerido:** ~100-300 linhas como heurística grosseira (podendo ser menor para código mais complexo) — reconhecendo explicitamente que contagem de linhas não captura complexidade cognitiva real. Existe uma dinâmica social nos dois extremos: PR de 10 linhas tende a gerar *bikeshedding* (revisor quer "sentir que contribuiu" e sugere trocas de nome, comentários, `for` vs. `while`); PR de 1.000 linhas tende a receber um "looks good to me" superficial sem revisão de fato — o mesmo sintoma já descrito acima em "Por Que o Looking Good to Me Aumentou com Agentes Autônomos", aqui com uma causa puramente de volume, não de agente autônomo.

## Cadência de Revisão e "Inventário É Custo"

A mesma fonte aplica o princípio lean/toyotista de [[wiki/concepts/inventario-e-custo|inventário é custo]] (via [[wiki/entities/principles-of-product-development-flow|Reinertsen]]) a PRs abertos: um PR parado é código que não está gerando valor, e cada dia de espera adiciona custo de troca de contexto (*context switching*) para quem abriu o PR — sem falar no risco de o trabalho ter seguido um caminho errado sem que ninguém tenha percebido ainda. Recomendação prática: revisar PRs abertos **todos os dias**, idealmente **duas vezes** (início e fim do expediente), para nunca deixar um PR passar a noite parado sem necessidade.

Duas técnicas concretas para reduzir esse inventário sem sacrificar qualidade:

- **Fast follow** — em vez de negar um PR funcional que só precisa de ajustes menores (reabrindo o ciclo de idas e vindas), aprovar e mergear, e abrir um segundo PR **menor**, só com as correções. Mantém o inventário principal limpo e o PR de correção é mais rápido e barato de revisar.
- **Draft PR** — abrir um PR ainda incompleto mas encaminhado, para alguém validar a direção antes de terminar o trabalho — poda um caminho errado antes de virar retrabalho de dias/semanas.

Também cita **checklists de PR** (ex.: "criei testes de integração", "testei localmente", "testei em staging") como camada adicional de qualidade usada por algumas empresas antes do merge.

## Relacionado

- [[wiki/concepts/definicao-de-pronto]] — code review é um dos critérios de "pronto"
- [[wiki/concepts/mentoria-tecnica]] — quem revisa está, na prática, mentorando
- [[wiki/concepts/sindrome-do-impostor]] — reação emocional comum a comentários de review
- [[wiki/concepts/red-flags-de-design]] — heurística concreta para o que procurar durante a revisão
- [[wiki/concepts/divida-cognitiva]] — code review como checkpoint contra fragmentação de entendimento compartilhado em times com IA
- [[wiki/concepts/rebase-vs-merge]] — rebase local antes do PR, merge para integrar
- [[wiki/concepts/inventario-e-custo]] — PR aberto como inventário parado; base do argumento de cadência de revisão diária

## Ler por Categoria de Mudança, Não Tudo de Uma Vez

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] propõe uma regra operacional para revisar código gerado por agentes em volume, como alternativa a ler cada PR por completo ou parar de ler completamente: escolher uma categoria de mudança (ex.: um CRUD de admin), ler todo PR daquela categoria, e quando o volume acumulado (a fonte estima ~30 PRs) gerar pouco ou nenhum feedback a dar — com o [[wiki/concepts/harness-de-qualidade|harness]] daquela área já confiável — marcar a categoria como pronta e avançar para a próxima. O objetivo não é parar de revisar, é reduzir a superfície de revisão manual conforme a confiança em cada fatia do sistema é conquistada, com um agente de code review ajudando durante todo o processo. Ver [[wiki/entities/uncle-bob]] para a citação original e [[wiki/concepts/harness-de-qualidade]] para o que precisa estar em pé antes de uma categoria poder ser considerada confiável.

## Quando o Review Deixa de Ser Obrigatório por PR

[[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] trata o volume de código de IA como a razão mecânica pela qual "ninguém mais revisa" — e propõe não abandonar review, mas *estratificá-lo* pela [[wiki/concepts/matriz-risco-dificuldade-review-ia|matriz risco × dificuldade]]: merge automático em baixo risco (desde que haja teste), amostragem em risco médio, revisão manual em pares em alto risco (auth, pagamentos, migração de banco). É a versão por-eixo-de-risco da mesma ideia de [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] de ganhar confiança por categoria, e o contraponto de gestão ao gargalo medido em [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]].

## Estratificar por Porte da Empresa (Accountability × Substituibilidade)

[[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] adiciona um eixo *organizacional* às estratificações já documentadas (por [[wiki/concepts/matriz-risco-dificuldade-review-ia|risco × dificuldade]] e por categoria de mudança): o porte da empresa muda o *porquê* de revisar.

- **Projeto de um homem só:** revisar cada linha da IA é uma **red flag** — sinal de que não há [[wiki/concepts/quality-gate|quality gate]] no pipeline; o *accountability* já é 100% do dev, então o certo é [[wiki/concepts/harness-de-qualidade|harness]] (testes E2E, orquestração de testes, agente revisor) em vez de leitura linha a linha.
- **Time grande:** o review sobrevive **não por desconfiança do código** (que já é escrito por IA), mas por **contexto** — o revisor lê arquitetura, aderência a padrões do projeto e cobertura de requisitos, e testa localmente o PR. O review vira "o QA dos próprios devs".

A tensão que explica a diferença: responsabilizar cada dev pelo que coloca em prod funciona em empresa média, mas empresa grande recusa isso porque aumenta o [[wiki/concepts/bus-factor|bus factor]] e reduz substituibilidade — grande empresa quer processos, não heróis. Daí a fonte falar em "várias verdades": review forte em time grande, opcional em time médio, dispensável em projeto solo. O autor ([[wiki/entities/lucas-montano]]) leva a ponta solo ao extremo, fazendo *push force* direto em produção via SSH+Claude Code quando o custo de downtime é baixo.

## Key Sources

- [[wiki/sources/como-nao-ser-humilhado-no-primeiro-code-review]]
- [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] — estratificação do review por porte da empresa; accountability individual × substituibilidade; review em time grande como QA de contexto (arquitetura/padrões/requisitos)
- [[wiki/sources/filosofia-do-design-de-software-introducao]]
- [[wiki/sources/cognitive-debt-margaret-storey]] — code review como checkpoint de entendimento compartilhado, requisito mínimo de "uma pessoa entende totalmente" antes do deploy
- [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] — "looking good to me" como sintoma de agentes autônomos de longa duração; skill Grill Me como mitigação
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — babysitting de PR pelo próprio agente (loop de CI + comentários + resolução de conversas); humano como gargalo de revisão em escala
- [[wiki/sources/underengineering-overengineering-mario-souto]] — tipos genéricos (`any`) e primitivos soltos em vez de enum como itens recorrentes de review, ligados a under-engineering
- [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]] — arquivo dedicado `review` separado do CLAUDE.md; `/code-review --ultra` para revisões complexas
- [[wiki/sources/database-migrations-sql-cru-vs-orm-drizzle]] — migrations de banco tratadas com o mesmo processo de PR/review que código de aplicação
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — catálogo completo dos 14 red flags do livro, checklist prático para revisão
- [[wiki/sources/git-rebase-na-pratica]] — mecânica de rebase local usada para chegar a um histórico limpo antes do PR
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — regra operacional de ler por categoria de mudança até acumular confiança, em vez de revisar tudo ou nada
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — argumento quantitativo (taxa de aceitação de código de IA, dados de benchmark) para deslocar o primeiro filtro de revisão de estilo para prova objetiva em CI
- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] — +91% no tempo de code review (Faros AI); a revisão como gargalo que não escala junto com a produção
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — matriz risco × dificuldade para estratificar review (merge automático / amostragem / revisão manual em pares); erre quando o erro é pequeno
- [[wiki/sources/potencial-programador-atitude-mindset]] — review como palco de [[wiki/concepts/ownership-proativo|ownership]] (ir atrás da própria aprovação) e o anti-padrão do revisor que sugere melhoria sem colocar a mão no código
- [[wiki/sources/pull-requests-por-que-falham-alternativas-sem-pr]] — tempo de revisão não escala com tamanho do PR; tamanho ótimo ~100-300 linhas; cadência diária/2x-dia via inventário-é-custo; fast follow e draft PR
