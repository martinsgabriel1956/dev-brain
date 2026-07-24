---
type: source
title: "System Design na Prática: Simulador e Hotel Booking com Replit"
aliases: ["simulador de system design replit", "hotel booking system design", "system design simulator"]
date_created: 2026-07-24
date_updated: 2026-07-24
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/system-design-simulador-hotel-booking-replit.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-24
source_count: 0
tags: [system-design, replit, vibe-coding, cache, load-balancer, escalabilidade-horizontal, mensageria, saas]
skill: tech-mentor-system-design
status: stable
---

# System Design na Prática: Simulador e Hotel Booking com Replit

## TL;DR

Vídeo (autoria não identificada no texto colado) que argumenta que [[wiki/concepts/entrevista-system-design|system design]] é a competência de programação que a IA menos substitui, e demonstra isso construindo um SaaS — um [[wiki/concepts/simulador-de-system-design|simulador de system design]] — com agentes do [[wiki/entities/replit|Replit]], seguido de uma sessão prática desenhando um sistema de reserva de hotel dentro do próprio simulador: identifica gargalo no banco de dados, corrige com [[wiki/concepts/cache]], [[wiki/concepts/load-balancer]], [[wiki/concepts/escalabilidade-horizontal|réplicas de banco]] e uma fila via Kafka, terminando com uma nota de IA (58/100) que aponta acertos e lacunas do desenho.

## Key Claims

- **A tese central**: num mundo em que IA escreve cada vez mais código, saber desenhar o sistema (não a linguagem escolhida, nem quem digitou o código) é a maior contribuição humana restante na construção de software — e é "a única coisa que não é impactada pela inteligência artificial". → [[wiki/concepts/entrevista-system-design]]
- **Definição operacional de software bom vs. ruim**: quão lento é, quantos erros expõe ao usuário, e se uma mudança se propaga corretamente por todas as camadas (exemplo citado: informação que "some" ao trocar de tela, ou duplo clique que dispara requisição duplicada cancelando a anterior).
- **OLTP vs. OLAP** citados como conceitos que o system design força a aprender: OLTP para operações transacionais rápidas do dia a dia, OLAP para consulta/agregação/exploração de grandes volumes. → [[wiki/concepts/analytics-pipeline]]
- **Metodologia de criação de produto**: começar com uma única funcionalidade, pensar em dados de entrada/saída, depois no fluxo de uso — e lançar com monetização desde o dia um (assinatura ou pagamento único), com escopo mínimo sendo exatamente a funcionalidade pela qual alguém pagaria. → [[wiki/concepts/mvp]]
- **Autocrítica de escopo**: admite que incluir o "simulador de caos" (queda de data center/AZ) no primeiro prompt foi um erro de escopo — o produto deveria ter focado exclusivamente no simulador central antes de expandir, e falta um tutorial guiado. → [[wiki/concepts/over-engineering]], [[wiki/concepts/mvp]]
- **Fluxo de trabalho com agentes Replit**: uma sessão principal roda uma tarefa maior enquanto subtarefas paralelas rodam em ambientes isolados que a interface chama de "workers" — hipótese explícita de que isso é `git worktree` por baixo dos panos, com merge automático de volta à sessão principal. → [[wiki/concepts/worktree-paralelismo]]
- **Testes end-to-end automáticos do agente**: o agente escreve o teste, roda do início ao fim, verifica se o resultado bate com o pedido, e itera em loop até passar — apontado como diferencial de qualidade do harness do Replit.
- **Exercício prático (hotel booking)**: client → app server → SQL database primeiro satura o banco (bottleneck flag, availability caindo a 55%); cache resolve porque a maioria dos hóspedes lê os mesmos quartos populares (read-heavy); load balancer inserido sem aprofundar no algoritmo; réplicas de banco (escalabilidade horizontal) removem o alerta do banco mas deslocam o gargalo para o app server; fila de mensageria (Kafka) proposta para aliviar o app server, mas sem nenhum consumidor definido no desenho. → [[wiki/concepts/gargalo]], [[wiki/concepts/cache]], [[wiki/concepts/load-balancer]], [[wiki/concepts/escalabilidade-horizontal]], [[wiki/concepts/mensageria]]
- **Kafka citado como possível over-engineering** para um sistema de reserva de hotel — usado no exercício mesmo assim, mas com a ressalva explícita de que a escolha de mensageria depende do critério priorizado (volume de dados, facilidade de integração, ou alta disponibilidade). → [[wiki/concepts/over-engineering]], [[wiki/concepts/mensageria]]
- **Nota final de IA (58/100)**: duas IAs avaliadoras em consenso reconhecem load balancer, cache e database como acertos; apontam como faltantes réplicas de SQL e invalidação de cache; e notam que Kafka, logs e métricas foram adicionados ao desenho sem justificativa clara de consumo — avaliação coerente, já que nada no exercício efetivamente consumia essas mensagens/logs.

## Entities

[[wiki/entities/replit]] · [[wiki/entities/augusto-galego]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/simulador-de-system-design]] · [[wiki/concepts/cache]] · [[wiki/concepts/load-balancer]] · [[wiki/concepts/escalabilidade-horizontal]] · [[wiki/concepts/gargalo]] · [[wiki/concepts/mensageria]] · [[wiki/concepts/over-engineering]] · [[wiki/concepts/mvp]] · [[wiki/concepts/worktree-paralelismo]] · [[wiki/concepts/vibe-coding]] · [[wiki/concepts/analytics-pipeline]]

## Conexão com outras fontes

Reforça diretamente [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] na tese de que system design é repertório que não se aprende decorando sintaxe, mas com o giro adicional de aplicar isso fora do contexto de entrevista — como prática de "vibe coding melhor". A prática de identificar gargalo antes de escalar (banco satura → cache → réplica → fila) converge exatamente com o framework já documentado em [[wiki/concepts/gargalo]] ("não escale prematuramente, identifique o gargalo, escale a camada certa") e com a ordem de mitigação (cache primeiro, depois réplicas, depois sharding/fila) já descrita em [[wiki/concepts/gargalo]] e [[wiki/concepts/cache]]. O padrão de workers paralelos com merge automático também converge com [[wiki/concepts/worktree-paralelismo]], adicionando um data point de que pelo menos um harness comercial (Replit) parece implementar esse padrão nativamente na UI, sem expor o termo "worktree" ao usuário.

## Open Questions

- O vídeo é visivelmente patrocinado pelo Replit — a avaliação da qualidade do harness (testes end-to-end automáticos, resolução de conflitos entre workers) não é verificável de forma independente a partir do texto, e não há comparação com concorrentes (Cursor, Devin, Claude Code) nesta fonte especificamente.
- Não fica claro no material se o "worker" do Replit é de fato implementado com `git worktree` — é uma inferência do autor ("provavelmente"), não uma confirmação técnica.
- O produto (simulador de system design) está em estágio de protótipo/MVP em construção durante o próprio vídeo — não há dado de uso real, retenção ou conversão de pagamento.

## Raw Quotes

> "Não é a linguagem de programação que a IA escolheu para ti... no final do dia o que importa é se tu sabe basicamente fazer um desenho do teu sistema."

> "A gente identificou um gargalo, o SQL database tá piscando em vermelho, tá na capacidade máxima."

> "O mesmo número de tráfego, mas o uso do database caiu — esse é o poder do caching num sistema de leitura intensa."

> "Pode ser um over engineering aqui, mas para um sistema de bucagem de hotel talvez não seja."

> "Ambos juízes concordam que a gente fez certo load balancer, o cash, o database... mas tá faltando SQL Replica, Rows Cash Invalidation."
