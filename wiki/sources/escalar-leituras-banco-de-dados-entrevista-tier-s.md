---
type: source
title: "Como Escalar Leituras de Banco de Dados (System Design para Entrevistas Tier S)"
aliases: ["escalar leituras banco de dados", "read scaling entrevista", "índices connection pooling read replicas cache cdn", "50000 leituras por segundo travando"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/escalar-leituras-banco-de-dados-entrevista-tier-s.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-08-10
source_count: 0
tags: [system-design, entrevistas, banco-de-dados, read-replicas, connection-pooling, cache, cdn, database-index, escalabilidade, backend]
skill: tech-mentor-system-design
status: stable
---

# Como Escalar Leituras de Banco de Dados (System Design para Entrevistas Tier S)

## TL;DR

Primeiro vídeo de uma série de System Design de [[wiki/entities/pedro-camaforte]] (inspirada num artigo de [[wiki/entities/lucas-faria]] sobre "os sete conceitos que mais caem em entrevistas Tier S"), focado em **escalar leituras** de banco de dados para vagas de faixa ~R$30-50k. A tese central é diagnóstica, não de receita: a solução do gargalo depende do **motivo** por trás dele, e os conceitos formam uma **escada de custo crescente** que só se sobe quando o degrau anterior não basta — (1) [[wiki/concepts/database-index]] + [[wiki/concepts/connection-pooling]] resolvem ~80% dos casos e sustentam dezenas a centenas de milhares de req/s; (2) [[wiki/concepts/read-replicas]] escalam leituras horizontalmente quando isso não basta (200-300k+ req/s), ao custo de *replication lag*; (3) [[wiki/concepts/cache]] ataca **hotspots** e **queries caras**, ao custo de invalidação; (4) [[wiki/concepts/cdn]] resolve **arquivos estáticos** por proximidade geográfica. O erro que elimina 90% dos candidatos é pular direto para arquitetura sem **entender o contexto** (volumetria, hotspots, criticidade de dados) — o que separa o pleno ("é só tacar cache e réplicas") do sênior (que primeiro pergunta quantas req/s e se há hotspot). Aplicações read-heavy identificadas por proporção leitura:escrita alta (~100-1000:1): posts, encurtadores de URL.

## Key Claims

- **A solução do gargalo depende do motivo, não é receita fixa.** O framing central do vídeo é diagnóstico: identificar *por que* o banco trava antes de escolher a técnica. → [[wiki/concepts/entrevista-system-design]]
- **Índices + connection pooling resolvem ~80% dos casos iniciais e sustentam dezenas a centenas de milhares de req/s** em hardware moderno, sem mudar nada na arquitetura. Uma tabela sem índice com milhões de linhas pode levar ~500ms; com índice, ~2ms. *Confiança: alta* (consistente com [skill: tech-mentor-system-design] `read-replicas-pooling.md` — otimize antes de escalar). → [[wiki/concepts/database-index]]
- **Connection pooling reutiliza conexões abertas** porque abrir uma nova conexão custa ~5-10ms e o banco tem teto de conexões simultâneas; sob alta carga esse custo vira erro para o usuário. *Confiança: alta* — o vídeo dá 5-10ms de *setup* por conexão; o skill destaca que PostgreSQL não escala bem além de ~200-300 conexões e cada conexão custa ~5-10MB de RAM (dimensões complementares, não conflitantes). → [[wiki/concepts/connection-pooling]]
- **Read replicas = "load balancer de banco de dados"**: separa o primário (só escrita) de réplicas (só leitura), escalando leituras quase infinitamente ao adicionar réplicas. → [[wiki/concepts/read-replicas]], [[wiki/concepts/replicacao-de-banco]]
- **O tradeoff das read replicas é o replication lag** — pode chegar a *segundos*, não só milissegundos. Aceitável para feed de Instagram, potencialmente inaceitável para conta bancária/fintech. Mostrar o conceito sem citar esse tradeoff corta o candidato. *Confiança: média-alta* — o vídeo cita "até segundos"; o skill estima lag típico <100ms em LAN e até segundos sob carga, e lista read-your-writes / session consistency / replicação síncrona como mitigações que o vídeo não detalha. → [[wiki/concepts/read-replicas]]
- **Cache é especialista em dois problemas: hotspots e queries caras.** Hotspot = ponto específico com carga desproporcional (perfil de celebridade com 200k req/s); query cara = joins/agregações pesadas com baixa frequência mas alta latência (leaderboard/dashboard/relatório). Ambos respondem em <1ms via cache. → [[wiki/concepts/cache]], [[wiki/concepts/cache-hot-path]]
- **O problema do cache é a invalidação**, com três estratégias: TTL/expiração (simples, pode servir dado velho), deletar no write (requer coordenação), atualizar no write (requer coordenação). O padrão descrito é **cache-aside**: miss → banco → grava no cache → devolve. → [[wiki/concepts/tradeoff-de-cache]], [[wiki/concepts/cache-aside]]
- **CDN resolve arquivos estáticos por proximidade geográfica**, não é intercambiável com cache/réplica. Reduz latência de ~400-500ms para ~20-50ms para usuários distantes do data center, com impacto em SEO e bounce. → [[wiki/concepts/cdn]]
- **O erro que elimina 90%: atacar arquitetura sem entender o contexto.** O entrevistador pergunta de forma genérica de propósito, para ver se o candidato investiga volumetria, hotspots e criticidade de dados. Pleno responde com solução pronta; sênior faz perguntas primeiro. → [[wiki/concepts/entrevista-system-design]], [[wiki/concepts/niveis-de-senioridade-system-design]]
- **Regra de ouro (árvore de decisão):** arquivos estáticos → CDN; leitura sobrecarregada → índices + pooling (80%); ainda insuficiente → read replicas; hotspots/queries caras → cache. Ciladas: cache antes de otimizar tabelas; implementação sem tradeoffs.

## Exemplo prático — Encurtador de URL

Proporção ~1000 leituras por escrita, ~60.000 req/s. A query de redirecionamento busca por `public_code`, que precisa de **índice** + **connection pooling**. URLs virais recebem **cache com Redis** para tirar carga do banco. Se subir para 200k+ req/s, cria-se **read replicas** do primário. Reforça o encurtador de URL como caso canônico de workload read-heavy. → [[wiki/concepts/database-index]], [[wiki/concepts/redis]]

## Entities

- [[wiki/entities/pedro-camaforte]] — autor do vídeo e da série de System Design para entrevistas Tier S
- [[wiki/entities/lucas-faria]] — autor do artigo "sete conceitos que mais caem em entrevistas Tier S" que serve de base para a série

## Concepts

[[wiki/concepts/database-index]] · [[wiki/concepts/connection-pooling]] · [[wiki/concepts/read-replicas]] · [[wiki/concepts/replicacao-de-banco]] · [[wiki/concepts/cache]] · [[wiki/concepts/cache-aside]] · [[wiki/concepts/tradeoff-de-cache]] · [[wiki/concepts/cache-hot-path]] · [[wiki/concepts/cdn]] · [[wiki/concepts/redis]] · [[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/escalabilidade-horizontal]] · [[wiki/concepts/niveis-de-senioridade-system-design]]

## Open Questions

- O vídeo dá números de throughput ("centenas de milhares de req/s só com índices + pooling") sem especificar hardware, motor de banco ou perfil de query — são estimativas de palco, não benchmarks. Tratar como ordem de grandeza, não valores calibrados.
- A série completa tem sete vídeos; este é o primeiro (leituras). O próximo prometido cobre **escalar escritas** — candidato a futura ingestão para fechar o par leitura/escrita.

## Raw Quotes

> "A solução desse gargalo vai depender do motivo por trás do gargalo, que nem sempre é o mesmo."

> "Read Replica nada mais é do que a gente pegar um banco que tava recebendo tanto a escrita quanto a leitura e separar ele: agora só vai receber escrita, e vão ter réplicas dele pra receber as leituras. É como se fosse um load balancer de banco de dados."

> "Não caia na cilada de sair adicionando cache sem antes otimizar as tabelas, sem antes aplicar connection pooling — é aí que você é eliminado."

> "O erro mais comum que faz os entrevistadores eliminarem 90% dos candidatos é quando o candidato não tenta entender o problema por trás da arquitetura que está sendo pedida."
