---
type: source
title: "System Design para Cada Nível: Júnior, Pleno e Sênior"
aliases: ["system design por nível", "system design junior pleno senior", "o que é esperado de cada nível em system design"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/system-design-por-nivel-junior-pleno-senior.md
source_url: ""
author: "Augusto Galego"
date_published: ""
date_ingested: 2026-07-27
source_count: 0
tags: [system-design, carreira, entrevistas, senioridade, junior, pleno, senior, arquitetura]
skill: tech-mentor-system-design
status: stable
---

# System Design para Cada Nível: Júnior, Pleno e Sênior

## TL;DR

Vídeo de Augusto Galego argumentando que é impossível definir com precisão o que se espera de system design de um júnior, pleno ou sênior — porque nenhuma empresa concorda na própria definição desses níveis — mas ainda assim traça uma média razoável. Separa duas dimensões que costumam ser confundidas: **como você é entrevistado** (sempre cobra compreensão do todo, num padrão inspirado no Google) vs. **como você trabalha de fato** (júnior/pleno usam pouco system design no dia a dia; só sênior costuma unir a compreensão do sistema inteiro, tipicamente ao desenvolver uma feature nova ou um sistema do zero). A progressão central: júnior precisa **solucionar** o problema e mostrar fundação; pleno precisa **resolver com racional prático** (por que SQL e não NoSQL, com alguma experiência real); sênior precisa **otimizar e liderar a conversa**, discutindo tradeoffs de escala, CAP, sharding, cache e monolito-vs-microsserviços — invertendo o papel reativo típico de entrevistas juniores/plenas.

## Key Claims

- **Entrevista ≠ trabalho real**: entrevistas de system design cobram compreensão do sistema completo (arquitetura, esquemas, tradeoffs, infra, API, escalabilidade, filas) para todos os níveis, seguindo o padrão popularizado pelo Google — mas no trabalho do dia a dia júnior e pleno raramente precisam dessa visão do todo; costumam precisar de visão rasa do todo + profundidade na parte específica que tocam. → [[wiki/concepts/entrevista-system-design]]
- **A compreensão do todo só é exigida no trabalho real a partir de sênior**, tipicamente ao desenvolver uma feature nova ponta a ponta ou um sistema do zero para uma equipe — trabalho raramente delegado a plenos ou júniors. → [[wiki/concepts/niveis-de-senioridade-system-design]]
- **Júnior**: precisa de compreensão básica de servidor/cliente, banco de dados, API, protocolo de comunicação (HTTP/RPC). Não precisa explicar tradeoffs a fundo — basta saber que a peça existe e resolve o problema. Entrevista foca em sistemas simples (encurtador de URL, jogo de xadrez com 2 usuários) e no resultado esperado é: requisitos, features, fluxos read/write, API, esquema simples, tradeoffs básicos, arquitetura de alto nível.
- **Pleno**: além da base de júnior, espera-se compreensão de workers, API Gateway, load balancer, tradeoffs SQL vs. NoSQL, Blob Store, CDN — com racional prático (ligado a experiência real de ter usado essas peças), não apenas "sei que existe". Entrevista adiciona requisitos não funcionais, modelagem de API/esquema mais detalhada, algum nível de estimativa/escalabilidade e identificação de gargalos/fault tolerance. → [[wiki/concepts/estimativas-back-of-envelope]]
- **Autor reconhece que a linha entre pleno e sênior está cada vez mais borrada** na prática de mercado — a progressão de pleno para sênior tende a ser rápida e as expectativas se sobrepõem.
- **Sênior**: exige profundidade, maturidade e julgamento fino sobre tradeoffs (não basta saber que um load balancer existe — isso é dado; o que se avalia é usar essa base para escalar a milhões de usuários). Entrevista foca em tradeoffs de monolito vs. microsserviços, [[wiki/concepts/cap-theorem|teorema de CAP]], escalabilidade, sharding, cache, reader replicas — e o candidato deve **liderar** a conversa, invertendo o papel reativo de júnior/pleno. → [[wiki/concepts/cap-theorem]]
- **"Sênior plus" (tech lead/CTO/staff)**: desenvolver um sistema inteiro do zero para uma equipe trabalhar em cima — decidir SQL vs. NoSQL, serverless vs. servidor dedicado, monolito vs. microsserviços — é tipicamente atribuição desse nível acima de sênior, não de sênior "puro". → [[wiki/concepts/microsservicos]]
- **Estimativas mais precisas são centrais no nível sênior**: com pouco tempo de entrevista, estimar de antemão volume/escala permite identificar gargalos preventivamente (CPU? network?) em vez de reativamente. → [[wiki/concepts/estimativas-back-of-envelope]]
- **Exemplo prático de tradeoff sênior — Netflix e restrição geográfica**: resolvido via CDN regional + identificação global de onde pertence a assinatura do usuário + localização por região. → [[wiki/concepts/cdn]]
- **Cases citados como nível sênior**: Netflix, o matching de motoristas do Uber, iFood, busca do Google, sistemas de recomendação/newsfeed (Twitter e redes sociais) — sistemas complexos demais para desenhar por completo, exigindo escolha de batalhas (quais features atacar).

## Entities

[[wiki/entities/augusto-galego]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/niveis-de-senioridade-system-design]] · [[wiki/concepts/high-level-design]] · [[wiki/concepts/estimativas-back-of-envelope]] · [[wiki/concepts/cap-theorem]] · [[wiki/concepts/load-balancer]] · [[wiki/concepts/cdn]] · [[wiki/concepts/db-sharding]] · [[wiki/concepts/cache]] · [[wiki/concepts/api-gateway]] · [[wiki/concepts/filas-e-workers]] · [[wiki/concepts/comparacao-na-carreira]] · [[wiki/concepts/microsservicos]]

## Conexão com outras fontes

Esta fonte complementa diretamente [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]] (Wesley Willians/Full Cycle): aquela descreve a **estrutura de uma sessão** de entrevista de system design (requisitos → capacidade → modelagem → desenho); esta descreve **como essa mesma estrutura é avaliada de forma diferente por nível de senioridade**, e adiciona a distinção — ausente na fonte anterior — entre o que é cobrado na entrevista e o que é usado de fato no trabalho do dia a dia. Também conecta com [[wiki/sources/comparacao-na-carreira-dev]] e [[wiki/sources/roadmap-dev-senior-2026]] no tema mais amplo de "ninguém concorda no que define cada nível de carreira" — aqui aplicado especificamente ao eixo de system design.

## Open Questions

- O autor admite abertamente que a categorização é subjetiva e baseada na própria experiência de 12 anos (5 deles em empresa "gringa") — não há dados de mercado, pesquisa salarial ou levantamento cross-empresa citados para sustentar os limites entre júnior/pleno/sênior.
- O vídeo termina com pitch de um curso pago do próprio autor — o conteúdo educacional gratuito é genuíno, mas o enquadramento dos três níveis pode estar calibrado, ainda que involuntariamente, para tornar o curso relevante a um público amplo (do júnior ao sênior).
- Não fica claro se as expectativas descritas se aplicam igualmente a empresas brasileiras de menor porte ou apenas ao padrão de entrevista "estilo Google" adotado por empresas maiores/gringas, que é o pano de fundo explícito do autor.

## Raw Quotes

> "Ninguém, nenhuma empresa sequer concorda na definição de o que é um júnior, o que é um pleno, o que é um sênior."

> "Um júnior que de fato é júnior não desenha sistemas completos, raramente escreve os próprios testes, e não tira uma feature da cabeça dele fazendo o design de todo o sistema da feature."

> "Para pleno já não cola tanto: sua decisão precisa ter um racional do porquê você tá escolhendo um tradeoff aqui."

> "Não tô vendo se você sabe o que é um load balancer, se você sabe que ele existe — isso é meio que dado. Tô vendo se você consegue usar sua compreensão para montar um sistema que escala para milhões de usuários."

> "Para júnior e para pleno a entrevista é muito mais reativa. Para sênior é muito mais esperado que você inverta o papel, lidere a conversa."
