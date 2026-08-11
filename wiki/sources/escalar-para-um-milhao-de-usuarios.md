---
type: source
title: "Desenho para Escalar até 1 Milhão de Usuários"
aliases: ["escalar para um milhão de usuários", "scale to 1 million users", "desenho de escala system design interview"]
date_created: 2026-08-10
date_updated: 2026-08-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/escalar-para-um-milhao-de-usuarios.md
source_url: ""
author: "Augusto Galego (inferido)"
date_published: ""
date_ingested: 2026-08-10
source_count: 0
tags: [system-design, escalabilidade, load-balancer, cache, cdn, nosql, replicacao, filas, stateless, multi-region, spof, entrevistas]
skill: tech-mentor-system-design
status: stable
---

# Desenho para Escalar até 1 Milhão de Usuários

## TL;DR

Aula (autoria inferida: Augusto Galego, mesma trajetória e curso pago da fonte irmã [[wiki/sources/anatomia-entrevista-system-design-bigtech]]) que reconstrói, passo a passo, o capítulo canônico "scale from zero to millions of users" do livro *System Design Interview* de Alex Xu (ByteByteGo). Parte do desenho mais simples possível — um usuário → um servidor web — e vai adicionando **uma peça por gargalo**: banco de dados (persistência), múltiplos servidores + [[wiki/concepts/load-balancer]] (SPOF do servidor), replicação write/read (SPOF e gargalo do banco), [[wiki/concepts/cache-layer|cache]] (latência do banco), [[wiki/concepts/cdn]] (arquivos estáticos), servidores [[wiki/concepts/stateless]] + NoSQL para sessões, [[wiki/concepts/filas-e-workers|filas e workers]] (jobs pesados assíncronos), tooling de observabilidade e, por fim, replicação multi-região por data center com roteamento por geolocalização. O fio condutor é o [[wiki/concepts/single-point-of-failure|single point of failure (SPOF)]]: cada evolução do desenho existe para eliminar um SPOF ou destravar o próximo gargalo — e a mensagem final é que esse ferramental básico já basta para servir milhões de usuários, muitas vezes até sem múltiplos data centers.

## Key Claims

- **Começa do mínimo: usuário (app mobile ou browser) → um único servidor web que roda a aplicação e responde requests.** É o mínimo que funciona na web, e às vezes é suficiente. → [[wiki/concepts/high-level-design]]
- **Quase toda aplicação precisa de um banco de dados** — (1) para armazenar grandes volumes que não cabem no servidor e (2) porque o servidor pode cair/resetar e perderíamos os dados sem persistência. → [[wiki/concepts/relational-vs-nosql]]
- **A escolha SQL vs NoSQL importa mais que o produto específico; por padrão, SQL.** Opte por [[wiki/concepts/nosql|NoSQL]] quando há dependência de latência super baixa, esquema flexível (logs, JSON, dados sem esquema fixo) ou throughput muito alto (ex.: armazenar todos os requests recebidos — quantidades enormes num período curto). → [[wiki/concepts/nosql]]
- **Escalar verticalmente (máquina maior) não escala bem: há um teto físico e o servidor é um [[wiki/concepts/single-point-of-failure|SPOF]].** "Você nunca vê uma Netflix rodando num único servidor." → [[wiki/concepts/escalabilidade-vertical]]
- **Como os dados já estão no banco (e não no servidor), dá para distribuir a aplicação em múltiplos servidores (cluster) lendo/escrevendo no mesmo banco** — escala horizontal, mais robusta e com mais vazão. → [[wiki/concepts/escalabilidade-horizontal]]
- **Com múltiplos servidores, entra o load balancer** para direcionar cada request ao servidor certo (com diferentes técnicas de redirecionamento). Depois disso, os servidores deixam de ser o gargalo — o gargalo e SPOF passa a ser o banco. → [[wiki/concepts/load-balancer]]
- **Escala-se o banco por replicação: um banco de escrita (writes) e réplicas só de leitura (reads)**, porque a maioria das apps lê muito mais do que escreve. Escrever em dois bancos ao mesmo tempo geraria inconsistência / race condition, daí o split. → [[wiki/concepts/replicacao-de-banco]] · [[wiki/concepts/read-replicas]]
- **Se o banco de escrita cair, promove-se uma réplica de leitura a banco de escrita** — como todos compartilham os mesmos dados, a promoção resolve o SPOF do write. → [[wiki/concepts/replicacao-de-banco]]
- **Cache entre servidores e banco reduz a lentidão inerente do banco (network, buscas):** consulta a cache antes do banco; se faltar, vai ao banco. Mas a cache é um SPOF — exige boa política de invalidação (expiração) e a aplicação precisa tolerar a cache indisponível. → [[wiki/concepts/cache-layer]]
- **Arquivos estáticos grandes (filme, foto, logo, HTML) viram gargalo de rede; a solução é servi-los de uma CDN.** Estático = não muda (ou muda muito infrequentemente); o usuário requisita direto da CDN, aliviando o serviço e dando impressão de velocidade (a primeira página chega mais rápido). → [[wiki/concepts/cdn]]
- **O cluster de backend deve ser stateless:** se o login/estado ficar num servidor e o próximo request cair em outro, o usuário aparece deslogado. Sessões (sticky sessions), preferências e dados muito acessados vão para um NoSQL de auxílio — que **não pode** viver dentro de nenhum servidor web, pois eles podem cair. → [[wiki/concepts/stateless]] · [[wiki/concepts/sticky-session]]
- **Computações pesadas (processar vídeo/imagem, gerar PDF) vão para filas + workers no modelo publisher/subscriber:** a app publica jobs na fila, um subscriber os puxa e um worker (thread em outra máquina, lambda) processa em sequência, aliviando os servidores web para responderem rápido. → [[wiki/concepts/filas-e-workers]]
- **Tooling de observabilidade** (login, métricas, monitoramento, health checks, logs de erro) roda fora dos servidores principais — comum no desenho, ainda que pouco falado. → [[wiki/concepts/observabilidade]]
- **Diversificação global (multi-região):** replica-se todo o conjunto (cluster + cache) em mais de um data center (ex.: AWS US East 1 e EU Central 1), com load balancer roteando por geolocalização; exceção é o NoSQL de sessões, compartilhado entre regiões. Mesmo sem múltiplos data centers, o desenho já atinge ~1 milhão de usuários. → [[wiki/concepts/escalabilidade-horizontal]]

## Entities

[[wiki/entities/augusto-galego]]

## Concepts

[[wiki/concepts/single-point-of-failure]] · [[wiki/concepts/escalabilidade-vertical]] · [[wiki/concepts/escalabilidade-horizontal]] · [[wiki/concepts/load-balancer]] · [[wiki/concepts/replicacao-de-banco]] · [[wiki/concepts/read-replicas]] · [[wiki/concepts/cache-layer]] · [[wiki/concepts/cdn]] · [[wiki/concepts/nosql]] · [[wiki/concepts/stateless]] · [[wiki/concepts/sticky-session]] · [[wiki/concepts/filas-e-workers]] · [[wiki/concepts/high-level-design]]

## Conexão com outras fontes

Esta fonte é a versão "desenho ao vivo" do mesmo esqueleto que [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] já cobre (vertical vs horizontal, LB, stateless, CDN, replicação) — mas organizada como uma **narrativa incremental guiada por SPOF/gargalo**, no formato exato do capítulo de Alex Xu. Complementa [[wiki/sources/anatomia-entrevista-system-design-bigtech]] (mesmo autor inferido): aquela explica *o que o entrevistador avalia* em cada etapa da sessão; esta entrega *o artefato* (o desenho de escala) que a etapa de HLD produz. O mesmo vocabulário de peças (load balancer, cache, CDN, filas, workers, blob store) reaparece em [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] e no exercício prático de [[wiki/sources/system-design-simulador-hotel-booking-replit]], onde a lógica "escalar uma camada só desloca o gargalo para a próxima" é demonstrada empiricamente — exatamente a dinâmica que esta aula percorre camada a camada.

## Open Questions

- **Autoria inferida, não confirmada:** a transcrição não nomeia autor/canal. A inferência para Augusto Galego se apoia na coincidência com [[wiki/entities/augusto-galego]] (mesmo curso pago de "mais de um ano de produção", 90+ aulas, política de reembolso de um mês sem perguntas, foco em system design para bigtech/gringa). Se errada, corrigir fonte e entidade.
- **Fonte didática e canônica, não original:** é uma releitura fiel do capítulo 1 de *System Design Interview* (Alex Xu). O valor para a wiki é consolidar a narrativa incremental por SPOF, não trazer claims novos — quase tudo aqui já existe em fontes anteriores.
- **Simplificações do modelo pub/sub:** a aula usa "publisher/subscriber" para descrever uma fila de jobs (worker puxa e processa). Tecnicamente isso é mais próximo de *competing consumers* / job queue do que de pub/sub de eventos (fan-out) — distinção registrada em [[wiki/concepts/filas-e-workers]] e [[wiki/concepts/pub-sub]].

## Raw Quotes

> "Você nunca vai ver uma aplicação tipo uma Netflix rodando em um único servidor."

> "O nosso servidor é um single point of failure. Se o servidor cair, a nossa aplicação cai."

> "Como todos eles compartilham dos mesmos dados, a gente pode simplesmente promover ele para um banco de dados de escrita."

> "A nossa aplicação precisa estar apta a lidar com o fato de que a cache às vezes não responde."

> "Se a nossa página inicial do site tá numa CDN, o usuário recebe a primeira página muito mais rápido do que se ela tiver no nosso servidor."

> "Muito provavelmente, mesmo sem usar múltiplos data centers, a gente já teria chegado no milhão de usuários ali sendo servidos."
