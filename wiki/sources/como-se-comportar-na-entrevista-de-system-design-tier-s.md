---
type: source
title: "Como se Comportar na Entrevista de System Design (Fechamento da Série Tier S)"
aliases: ["fechamento série tier s", "comportamental em entrevista de system design", "desenvolvedor 1 vs desenvolvedor 2", "como aplicar os 7 conceitos na entrevista"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-se-comportar-na-entrevista-de-system-design-tier-s.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-09-04
source_count: 0
tags: [system-design, entrevistas, comportamental, soft-skills, comunicacao, carreira, tier-s]
skill: tech-mentor-system-design
status: stable
---

# Como se Comportar na Entrevista de System Design (Fechamento da Série Tier S)

## TL;DR

Sétimo e último vídeo da série Tier S de [[wiki/entities/pedro-camaforte]] (depois de [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s|escalar leituras]] e [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s|race condition]]), que fecha o arco não com mais um conceito técnico, mas com a tese central de toda a série: dominar os sete conceitos de system design é necessário mas não suficiente para passar em entrevistas de vagas Tier S (R$20-50k+), porque o entrevistador não está avaliando se o candidato decorou a técnica certa — todos os outros candidatos também sabem — e sim como ele comunica seu raciocínio e reage a feedback. A fonte demonstra que os sete conceitos da série (escalar leituras/escritas, real-time updates, URLs pré-assinadas etc.) cobrem a maioria das features de qualquer sistema clássico de entrevista (Instagram, WhatsApp, YouTube), ilustra o erro mais comum — desenhar antes de levantar requisitos — com um exemplo contrastado (encurtador de URL com 3 servidores desnecessários para 100 usuários), e prescreve um roteiro de 3-4 etapas (requisitos funcionais/não funcionais → entidades → APIs → design com aprofundamento opcional) validado pelo framework de 4 etapas já documentado em [skill: tech-mentor-system-design] `system-design.md`. Fecha com uma tabela de dois perfis de candidato (que assume vs. que pergunta; que é monólogo vs. que colabora) e recomendações práticas de treino (design meetings no trabalho, gravar-se resolvendo desafios, mock interview com um par mais sênior).

## Key Claims

- **Dominar os conceitos técnicos é necessário mas não suficiente**: para vagas Tier S remotas, centenas de candidatos concorrem tendo estudado os mesmos meses de System Design — o que separa os poucos aprovados não é o repertório técnico (citar Redis, Elasticsearch etc. "qualquer um pode fazer"), mas a maneira de pensar e comunicar o raciocínio. Reforça, com framing de concorrência explícito ("centenas de pessoas para a mesma vaga"), a mesma tese já central em [[wiki/concepts/entrevista-system-design]].
- **Os 7 conceitos da série cobrem a maioria das features de qualquer sistema clássico de entrevista**: o autor mapeia explicitamente Instagram (upload → URL pré-assinada; feed/likes → escalar leituras; notificações → real-time), WhatsApp (troca de mensagens real-time, persistência, escalar escritas) e YouTube (upload → URL pré-assinada; views → escalar escritas; vídeo viral → escalar leituras; métricas → escalar escritas) de volta aos vídeos anteriores da série. Reconhece explicitamente que sempre haverá alguma feature com "sisteminha" específico não coberto — não é uma decomposição exaustiva, é uma heurística de ponto de partida.
- **O primeiro passo mental é identificar o desafio central do problema proposto** (ex.: YouTube é conhecido por upload de vídeo → pensar em URL pré-assinada de cara) — mas isso é só o ponto de partida; como o candidato desenvolve esse desafio a partir daí é o que a fonte trata como o diferencial real.
- **Erro clássico ilustrado com contraste concreto**: um candidato que já sai desenhando servidores/load balancer para um encurtador de URL sem perguntar a escala-alvo pode estar sobre-arquitetando um sistema de 100 usuários com a mesma complexidade de um de milhões — mesmo que o desenho final esteja tecnicamente correto e escale, isso tende a desclassificar, porque o candidato presumiu em vez de perguntar. *Confiança: alta* — bate diretamente com o Passo 1 ("Clarify Requirements") do framework de 4 etapas em [skill: tech-mentor-system-design] `system-design.md`, que lista escopo/escala/RNF/constraints como perguntas obrigatórias antes de desenhar qualquer coisa, e nomeia esse mesmo erro explicitamente: "a arquitetura correta é derivada da escala, não o contrário — um sistema de 100 QPS não precisa de Kafka". → [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]]
- **A entrevista é uma conversa, não um monólogo**: o entrevistador espera participação ativa — o candidato pode e deve perguntar diretamente sobre escala/requisitos em vez de presumir silenciosamente, inclusive propondo um número e pedindo confirmação ("vou considerar 1 milhão de usuários simultâneos, o que você acha?").
- **Roteiro de 3-4 etapas antes de desenhar**: (1) requisitos funcionais (features) e não funcionais (qualidades: escala, latência, durabilidade) — negociados em conversa direta com o entrevistador, sem precisar saber os números de antemão; (2) entidades principais do domínio (≤2 minutos de conversa); (3) APIs/interfaces relacionando as features aos endpoints (ex.: `POST /urls` com URL original + expiração opcional → URL encurtada; `GET /{código}` → redirect); (4) só então o desenho de fato, com aprofundamento em algum tópico como etapa opcional escolhida pelo entrevistador (mais comum em vagas de staff). *Confiança: alta, com nuance de ordenação* — o framework de 4 etapas em [skill: tech-mentor-system-design] `system-design.md` (Clarify Requirements → Estimativas Back-of-Envelope → High-Level Design → Deep Dive) valida a mesma lógica central ("nunca desenhar componentes antes de ter os requisitos"), mas usa uma ordenação ligeiramente diferente da fonte: a skill insere **estimativas de capacidade** como etapa 2 (antes de entidades/APIs), enquanto esta fonte pula estimativas numéricas explícitas e vai direto de requisitos para entidades e depois APIs. As duas non são incompatíveis — a fonte é mais informal/conversacional, a skill é mais estruturada — mas a etapa de estimativas de capacidade fica implícita aqui, não nomeada como passo distinto. → [[wiki/concepts/estimativas-back-of-envelope]], [[wiki/concepts/high-level-design]], [[wiki/concepts/contrato-de-api]]
- **Regra central: sempre explicar o porquê de cada decisão e o tradeoff que ela traz**, nunca apenas nomear a tecnologia escolhida ("vou usar Postgres aqui" sem dizer por quê é insuficiente). *Confiança: alta* — quase idêntica à "regra de ouro" documentada em [skill: tech-mentor-system-design] `system-design.md`: "nunca diga 'depende' sem completar 'depende de X, e dado que X é Y, a escolha é Z porque...'" — mesmo princípio, formulação diferente (a fonte enquadra como comunicação/comportamento, a skill como disciplina técnica de decisão).
- **O design é desenvolvido em paralelo com o entrevistador, com pausas para feedback** — pedir explicitamente a opinião do entrevistador sobre a decisão tomada, aceitar correções sem ficar defensivo. O entrevistador já conhece a solução esperada; o que avalia é como o candidato recebe incentivo/correção e se adapta.
- **O comportamental pesa mais do que o conhecimento técnico específico na hora de diferenciar candidatos** — não porque o técnico não importe (é pré-requisito), mas porque, entre centenas de candidatos igualmente preparados tecnicamente, o comportamental é o que resta como diferencial. Reforça, num contexto de entrevista técnica específica (system design), a mesma tese mais geral de [[wiki/concepts/soft-skills-como-diferencial-de-pleno]] (soft skills como o que resta quando a IA comoditiza o técnico) — aqui aplicada à seleção entre humanos, não à comparação humano vs. IA.
- **Dois perfis contrastados de candidato**: Desenvolvedor 1 (reprova) assume e já sai fazendo, fica defensivo com feedback, só cita tecnologia sem explicar, faz da entrevista um monólogo. Desenvolvedor 2 (passa) pergunta antes de agir, recebe feedback aberto e se adapta, explica o raciocínio por trás de cada decisão, colabora com o entrevistador. A tabela binária é uma simplificação didática — a fonte não trata como "personalidades fixas", mas como espectro de comportamento treinável.
- **Recomendações concretas de prática**: organizar design meetings reais no trabalho atual (propor arquitetura, se pronunciar, liderar a discussão); pegar desafios do canal (Uber, YouTube, WhatsApp, citados mas não aprofundados na série) e se gravar resolvendo, depois reassistir para identificar o que melhorar; pedir mock interview a um par mais sênior, que faça perguntas como um entrevistador real faria. *Convergência* com [[wiki/concepts/seis-passos-mock-interview]] (mesmo mecanismo geral — simular o formato real, não só o conteúdo — aplicado lá a coding interview e aqui a system design).
- **Calibração de expectativa realista**: o autor levou 4 anos para conseguir seu primeiro emprego no exterior — apresentado deliberadamente para normalizar que o resultado (salário Tier S) não vem em semanas, e sim de prática incremental e rejeição repetida ao longo do tempo.

## Entities

[[wiki/entities/pedro-camaforte]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]] · [[wiki/concepts/estimativas-back-of-envelope]] · [[wiki/concepts/high-level-design]] · [[wiki/concepts/contrato-de-api]] · [[wiki/concepts/comunicacao-tecnica]] · [[wiki/concepts/soft-skills-como-diferencial-de-pleno]] · [[wiki/concepts/seis-passos-mock-interview]] · [[wiki/concepts/niveis-de-senioridade-system-design]]

## Conexão com outras fontes

Sétima e última entrada da série de [[wiki/entities/pedro-camaforte]], depois de [[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]] (1º vídeo, escalar leituras) e [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]] (6º vídeo, concorrência). Diferente daquelas duas — cada uma cobrindo um conceito técnico específico —, esta é a única da série sem conteúdo técnico novo: é puramente sobre comportamento e comunicação, fechando o arco da série ao amarrar os sete conceitos técnicos anteriores num framework de aplicação prática. Corrobora diretamente [[wiki/concepts/entrevista-system-design]] (mesma "regra de ouro" de nunca desenhar sem levantar requisitos, mesmo enquadramento de "conversa, não monólogo") e adiciona uma tabela binária de perfil comportamental que a página de conceito ainda não tinha de forma explícita. A convergência entre o roteiro de 3-4 etapas desta fonte e o framework de 4 etapas de [skill: tech-mentor-system-design] `system-design.md` é forte mas não idêntica — a diferença de ordenação (estimativas de capacidade explícitas vs. implícitas) é a única discrepância real registrada. O autor menciona pretender gravar um vídeo futuro aplicando o framework completo sobre o Uber — candidato a ingestão futura que continuaria esta série mesmo após seu "fechamento" formal.

## Open Questions

- **Vídeo futuro sobre Uber mencionado pelo autor**: "estou planejando trazer para o canal o sistema do Uber [...] destrinchando ele, aplicando cada uma das estratégias na prática" — não hospedado no canal no momento da ingestão desta fonte; candidato a ingestão futura que estenderia a série mesmo após este fechamento.
- **Números concretos de capacidade não são exemplificados nesta fonte** (ao contrário do framework da skill, que lista números para decorar — 1M QPS, latência de RAM/SSD/HDD/rede) — a fonte trata a etapa de estimativa como implícita dentro do levantamento de requisitos não funcionais, sem detalhar o cálculo back-of-envelope. Não é uma contradição, mas um gap de profundidade que outras fontes da wiki (ex.: [[wiki/concepts/estimativas-back-of-envelope]]) já cobrem separadamente.

## Raw Quotes

> "Comunicar a sua ideia, o seu processo de raciocínio, aí isso é o que diferencia — o quão bem você comunica as suas ideias e o quão bem você explica o porquê de cada decisão que você tá tomando."

> "Isso aqui não é um monólogo, isso aqui é uma conversa. Você vai conversar com o entrevistador, ele não tá aqui só para ficar te observando enquanto você vai fazendo, vai desenhando as coisas — vocês vão conversar."

> "Sempre explique o porquê das suas tomadas de decisões e sempre explique o tradeoff que alguma decisão que você tomou vai trazer."

> "Ele já sabe a solução que precisa ser feita, ele já sabe qual que é a resposta mais adequada que você precisa entregar. O que ele vai estar avaliando é como você se comunica, como você se comporta, como você responde a certos incentivos da parte dele."

> "O que mais vai importar e pesar durante a entrevista, por incrível que pareça, é o seu comportamental, e não o quanto você sabe de alguma ferramenta ou de alguma tecnologia."

> "Um salário desses não se alcança de uma semana para outra [...] eu demorei 4 anos para conseguir meu primeiro trabalho pro exterior."
