---
type: source
title: "Por Que Você Não Deve Começar Um Projeto com Microsserviços"
aliases: ["monolito primeiro renato augusto", "obsessão por microsserviços", "amazon prime video monolito"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 0
tags: [tech-mentor-backend, microsservicos, monolito, monolito-modular, ddd, bounded-context, yagni, monolith-first, martin-fowler, amazon-prime-video]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/microsservicos-monolito-first-renato-augusto.md"
source_url: ""
author: "Renato Augusto"
date_published: ""
date_ingested: "2026-08-18"
---

## TL;DR

Renato Augusto argumenta que microsserviços viraram um objetivo em si (impulsionado por requisitos de vaga no LinkedIn) em vez de uma ferramenta, e que isso leva projetos a nascerem com uma arquitetura que não deveriam ter. A tese central segue três motivos: (1) microsserviços aumentam a complexidade sistêmica exponencialmente desde o dia 1 (infra, mensageria, observabilidade, CI/CD por serviço) — desperdiçando o tempo que um projeto novo deveria gastar validando valor via MVP, o clássico caso de violação do princípio YAGNI; (2) microsserviços servem para escalar não só o sistema, mas os times — só fazem sentido quando a equipe já é grande o suficiente para ter times dedicados por serviço; (3, motivo principal) no início de um projeto o domínio ainda está sendo descoberto, e decompor em microsserviços sem esse conhecimento gera fronteiras de serviço erradas que exigem retrabalho constante (exemplo didático de e-commerce: estoque e promoções cruzando os limites que pareciam óbvios entre produtos/pedidos/clientes). A resposta a esse terceiro motivo é o Domain-Driven Design — usar bounded contexts para entender o domínio antes de fisicamente distribuir o sistema — e o princípio **Monolith First** de Martin Fowler: começar com um **monolito modular** (módulos = bounded contexts, com fronteiras de contrato explícitas, mas ainda um único deploy/banco/processo) e só extrair microsserviços quando a maturidade do domínio e a necessidade real de escala/time justificarem. Como evidência de que essa não é uma posição periférica, cita o caso da Amazon Prime Video migrando parte do sistema de volta para monolito e reduzindo custos de infraestrutura AWS em mais de 90%.

---

## Reivindicações Principais

**Claim:** A Amazon migrou parte do sistema da Amazon Prime Video de volta para uma arquitetura monolítica (notícia de "menos de 2 anos" antes desta gravação) e reduziu os custos de infraestrutura na AWS em mais de 90%, com menor complexidade sistêmica e mais eficiência operacional.
**Evidência:** Citação de notícia pública, sem link/fonte primária citada na transcrição; caso amplamente reportado na indústria em 2023 (equipe de monitoramento de qualidade de vídeo do Prime Video migrou de microsserviços/serverless para um monolito).
**Confiança:** Alta como fato divulgado publicamente e amplamente conhecido no setor — mas **[external]**, sem fonte primária linkada nesta transcrição; primeira menção do caso na wiki, sem página própria de case study ainda.

**Claim:** Microsserviços aumentam a complexidade sistêmica de forma exponencial desde o primeiro dia de projeto — comunicação entre serviços, pipelines de CI/CD e deploy independentes por serviço, banco de dados próprio por serviço, mensageria (RabbitMQ/SQS/Kafka), observabilidade/tracing/log distribuído, e domínio obrigatório de padrões como CQRS, Event-Driven Architecture, Event Storming e DDD.
**Evidência:** Lista descritiva do autor, sem dado quantitativo.
**Confiança:** Alta — converge diretamente com a tabela "Monolito Modular vs Microsserviços" de `references/architecture-foundations.md` da skill `tech-mentor-backend` (já citada em [[wiki/concepts/microsservicos]]) e com os custos já documentados na wiki em [[wiki/concepts/microsservicos]] ("Custo-Benefício").

**Claim:** Começar um projeto com microsserviços é um caso direto de violar o princípio YAGNI — no início, a prioridade deveria ser validar a ideia via MVP com velocidade máxima, e o tempo gasto configurando infraestrutura distribuída é tempo tirado da construção de funcionalidades essenciais do domínio.
**Evidência:** Argumento do autor, conectando explicitamente microsserviços prematuros ao princípio de Kent Beck/XP.
**Confiança:** Alta — é a primeira fonte na wiki a nomear explicitamente o princípio YAGNI como o mecanismo por trás da recomendação "não comece com microsserviços"; reforça (sem contradizer) o que [[wiki/concepts/yagni]] já registra sobre "microsserviços prematuros" como sinal de over-engineering via [[wiki/sources/underengineering-overengineering-mario-souto]].

**Claim:** Microsserviços existem para escalar times, não só sistemas — cada microsserviço precisa de um time dedicado; não é saudável que todos os programadores mantenham todos os microsserviços. A migração só faz sentido quando a equipe cresce a dezenas/centenas de programadores e o atrito de todo mundo mexendo na mesma base de código vira um problema real.
**Evidência:** Argumento do autor, com analogia ("o programador vira o pato: nada, anda e voa, mas não faz nada direito").
**Confiança:** Alta — converge diretamente com a Lei de Conway e a tabela de critério "Time: 1-5 pessoas vs. 5+ times independentes" já documentada em [[wiki/concepts/microsservicos]] via `references/architecture-foundations.md`.

**Claim:** O motivo principal para não começar com microsserviços é a falta de conhecimento de domínio no início de um projeto — o domínio ainda está sendo descoberto (regras de negócio, processos, entidades em constante evolução), e decompor prematuramente gera microsserviços que não representam corretamente as responsabilidades do sistema, exigindo refatoração de múltiplos serviços e de seus bancos de dados isolados quando o domínio real se revela.
**Evidência:** Exemplo didático de e-commerce: microsserviços de produtos/pedidos/clientes definidos cedo demais não previam que gestão de estoque está fortemente ligada a produtos, ou que promoções afetam tanto produtos quanto pedidos.
**Confiança:** Alta — é a claim mais bem desenvolvida do vídeo, e converge com o argumento já central em [[wiki/concepts/microsservicos]] ("Decomposição Correta": decompor por bounded context, não por camada técnica) e em [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] (DDD como pré-requisito de decomposição, sem o qual não há uma fronteira de entidade única e estável).

**Claim (Monolith First, atribuída a Martin Fowler):** Duas percepções levaram Fowler a formular o princípio Monolith First — (1) quase todas as histórias de microsserviços bem-sucedidas começaram com um monolito que ficou grande e foi quebrado depois; (2) quase todos os sistemas criados do zero já como microsserviços tiveram sérios problemas. Conclusão: não se deve começar um projeto com microsserviços, mesmo com certeza de que o sistema vai crescer o suficiente para valer a pena depois.
**Evidência:** Paráfrase do autor do artigo/bliki de Martin Fowler (não linkado na transcrição), incluindo referência à imagem do blog com "dois caminhos" (dragões no caminho de ir direto para microsserviços vs. monolito modular no caminho de baixo).
**Confiança:** Alta como atribuição — Monolith First é um artigo real e amplamente citado de Fowler (2015, martinfowler.com/bliki/MonolithFirst.html), mas o link não está na transcrição, então a citação exata da imagem/frase fica como **[external]** não verificada diretamente nesta ingestão. Complementa (não contradiz) [[wiki/sources/arquitetura-de-sacrificio]], já presente na wiki, que documenta uma tese adjacente de Fowler (Sacrificial Architecture, 2014): a mesma recomendação de "monolito primeiro, decompor depois" vista por um ângulo diferente (arquitetura descartável vs. sequência de maturidade de domínio).

**Claim:** Um monolito modular bem feito organiza módulos internos = bounded contexts do DDD, cada um com entidades, regras de negócio e testes próprios, podendo até ter esquema de banco de dados próprio mesmo compartilhando a mesma conexão física — e essa é a alternativa correta para a maioria esmagadora dos projetos, sendo mais do que suficiente na maior parte dos cenários.
**Evidência:** Repositório de exemplo em C# citado pelo autor (`src/modules/` com módulos como `administration`, `meetings`, `payments`, `registration`, `user-access`, cada um com camadas de aplicação/domínio/testes) — mistura de Clean Architecture (camadas) com DDD (bounded contexts).
**Confiança:** Alta — converge exatamente com o que já está documentado em [[wiki/concepts/monolito-modular]] (contratos/interfaces entre módulos via Ports & Adapters, sem chamada de função direta entre eles) e com a implementação concreta em Go já registrada nessa mesma página via [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — segunda implementação de referência (Go e C#) do mesmo padrão na wiki.

## Entidades Mencionadas

- [[wiki/entities/renato-augusto]] — autor; primeira fonte deste autor cruzando diretamente DDD + monolito modular + microsserviços (fontes anteriores dele cobriam design patterns, escalabilidade horizontal e system design de forma mais isolada)
- [[wiki/entities/martin-fowler]] — atribuição do princípio Monolith First e da imagem "dois caminhos" (dragões vs. monolito modular) do bliki
- Amazon / Amazon Prime Video — case citado de migração de microsserviços de volta para monolito, redução de >90% em custo de infraestrutura AWS; primeira menção nomeada na wiki, sem entidade própria ainda (candidata a stub se aparecer em outra fonte com mais profundidade)
- Sam Newman — autor citado dos livros *Migrando Sistemas Monolíticos para Microsserviços* e *Criando Microsserviços* (2ª edição); primeira menção nomeada na wiki, sem entidade própria criada nesta ingestão (recomendação bibliográfica, sem claim técnica atribuída a ele nesta fonte)
- Eric Evans — autor citado do livro *Domain-Driven Design* ("o livro azul", precursor do DDD); primeira menção nomeada na wiki, sem entidade própria criada nesta ingestão pelo mesmo motivo

## Conceitos Tocados

- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/monolito]]
- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/bounded-context]]
- [[wiki/concepts/yagni]]
- [[wiki/concepts/monolith-first]] (criado nesta ingestão)
- [[wiki/concepts/escalabilidade-horizontal]]
- [[wiki/concepts/escalabilidade-vertical]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/strangler-fig-pattern]]

## Open Questions

- O caso da Amazon Prime Video é citado de memória, sem link ou dado numérico além do "mais de 90%" — não há página de case study própria na wiki ainda para esse caso específico (diferente dos `case-*.md` existentes, que são exercícios didáticos de entrevista, não histórias reais de empresa); fica registrado apenas dentro de [[wiki/concepts/monolito]] como referência externa, candidato a fonte própria se uma transcrição mais detalhada (ex.: o post técnico original da Amazon) for ingerida depois.
- A citação do artigo Monolith First de Fowler não vem com URL na transcrição — o conteúdo (duas percepções + imagem dos dois caminhos) é consistente com o artigo real conhecido publicamente, mas fica marcado como **[external]** não verificado diretamente nesta ingestão, à espera de uma ingestão futura do artigo original do bliki.
- Sam Newman e Eric Evans aparecem apenas como recomendação bibliográfica de fechamento, sem claim técnica atribuída a eles nesta fonte — não foram criadas entidades próprias; ficam como candidatos a stub caso apareçam com profundidade técnica em outra fonte (mesmo tratamento já dado a Keycloak em [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]]).

## Raw Quotes

> "Muita gente acha que microsserviços são um objetivo, e não uma ferramenta."

> "É como construir uma casa sem ter uma planta completa. Você pode até começar a levantar as paredes, mas a chance de você ter que derrubar uma parte e refazer de novo é enorme."

> "Quase todas as histórias de microsserviços bem-sucedidas começaram com um monolito que ficou muito grande e depois foi quebrado e dividido em microsserviços. [...] Quase todos os casos em que ouvi falar de um sistema que foi criado do zero como um sistema de microsserviços acabaram tendo sérios problemas."

> "Você precisa entender que o monolito é que tem que ser o ponto de partida — para depois que você tiver todo um conhecimento de domínio, depois que você conseguir bater o olho e conseguir enxergar a forma como você consegue separar a tua aplicação, aí sim você começa a tua jornada para microsserviços."
