---
type: source
title: "5 Dicas para Passar em Entrevistas de Lousa Branca / System Design"
aliases: ["5 dicas system design", "entrevista lousa branca", "whiteboard interview full cycle"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/5-dicas-entrevistas-lousa-branca-system-design.md
source_url: ""
author: "Wesley Willians (Full Cycle)"
date_published: ""
date_ingested: 2026-07-20
source_count: 0
tags: [entrevistas, system-design, whiteboard-interview, carreira, arquitetura]
skill: tech-mentor-system-design
status: stable
---

# 5 Dicas para Passar em Entrevistas de Lousa Branca / System Design

## TL;DR

Vídeo do canal Full Cycle (Wesley Willians) com cinco dicas práticas para sessões de "lousa branca" / [[wiki/concepts/entrevista-system-design|system design interview]] em grandes empresas: gerenciar o tempo (40–50 min), não desenhar nada antes de perguntar, levantar requisitos core vs. auxiliares, montar um [[wiki/concepts/estimativas-back-of-envelope|plano de capacidade]], modelar dados e API antes do desenho, e só então ir para a lousa. Reforça também nunca citar tecnologia que não se domina, e que o objetivo de todo entrevistador é levar o candidato a admitir "não sei" em algum ponto — o que é esperado, não reprovável.

## Key Claims

- **System design é diferente de design system** — distinção terminológica que o vídeo faz questão de marcar logo de início. → [[wiki/concepts/entrevista-system-design]]
- **Gestão de tempo é crítica**: sessões de whiteboard/system design costumam durar 40–50 minutos; começar a desenhar sem contexto suficiente é um erro clássico porque faltam elementos e passa a impressão de que o candidato não está fazendo perguntas.
- **Comece pelos requisitos, não pela solução**: todo sistema tem funcionalidades "core" e funcionalidades auxiliares — o candidato deve perguntar explicitamente ao entrevistador quais são as funcionalidades core, e focar o desenho nelas. Funcionalidades auxiliares só se sobrar tempo.
- **Plano de capacidade é esperado como parte da resposta**: requisições por segundo/minuto, picos de acesso, banda necessária, custo/volume de armazenamento em disco por dia/ano/5 anos, e replication factor. → [[wiki/concepts/estimativas-back-of-envelope]]
- **Modelagem de dados deve mostrar repertório, não profundidade**: usar RDBMS, chave-valor e banco de busca em partes diferentes do mesmo sistema conforme o caso de uso, sem se aprofundar em modelagem complexa. → [[wiki/concepts/modelagem-de-dados]]
- **Modelagem de API é parte avaliada**: principais endpoints, chamadas internas entre sistemas, request/response, códigos de retorno e escolha de protocolo (HTTP vs. gRPC). → [[wiki/concepts/contrato-de-api]]
- **O desenho na lousa é a última etapa, não a primeira**: só depois de requisitos, plano de capacidade e modelagem é que o candidato desenha o [[wiki/concepts/high-level-design|high-level design]] — e o entrevistador avalia se o desenho é coerente com tudo que foi dito antes.
- **Nunca cite tecnologia que você não domina de verdade**: o entrevistador tende a descer o nível de detalhe da pergunta (ex.: Prometheus → como funciona o alarme, o banco de dados interno, PromQL) até encontrar o limite real de conhecimento. Se precisar citar algo que não domina, fazer disclaimer explícito de que foi uma tecnologia usada pelo time, não algo que o candidato manja a fundo.
- **O objetivo estrutural de toda entrevista técnica é levar o candidato a dizer "não sei"** — isso é esperado e normal, e a resposta recomendada é admitir a lacuna e demonstrar interesse em aprender, em vez de "sabonetear" (enrolar) a resposta.

## Entities

[[wiki/entities/wesley-willians]] · [[wiki/entities/full-cycle]]

## Concepts

[[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/estimativas-back-of-envelope]] · [[wiki/concepts/high-level-design]] · [[wiki/concepts/modelagem-de-dados]] · [[wiki/concepts/contrato-de-api]] · [[wiki/concepts/entrevista-tecnica-coding]] · [[wiki/concepts/arquitetura-de-software]]

## Conexão com outras fontes

Esta fonte complementa [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]]: as duas descrevem o mesmo padrão estrutural de entrevista técnica — o entrevistador reduz o nível da pergunta até achar o limite do candidato, e admitir "não sei" é esperado, não um sinal de fracasso. A diferença é o formato: lá é resolução de algoritmo ao vivo, aqui é desenho de arquitetura de sistema distribuído. O conceito de [[wiki/concepts/estimativas-back-of-envelope]] já documentado na wiki (fonte anterior de system design) aparece aqui reforçado como etapa obrigatória, não opcional, da sessão.

## Open Questions

- O vídeo é claramente promocional do MBA em Arquitetura Full Cycle — as dicas são generalistas e não citam fontes primárias (livros, artigos, benchmarks) para as afirmações sobre duração de sessão ou expectativas de entrevistadores.
- Não há dados sobre quão universais essas práticas são fora do contexto de entrevistas brasileiras/remotas — o vídeo fala de "grandes empresas" sem nomear quais.

## Raw Quotes

> "Não tente sair desenhando nada de cara, porque vão faltar elementos."

> "Comece pelos requisitos... pergunte para as pessoas que estão te entrevistando quais são as funcionalidades core."

> "Nunca, absolutamente nunca, coloque tecnologias que você não teve experiência."

> "Todos esses tipos de entrevista têm um único objetivo: fazer você falar 'não sei'... e tá tudo bem."
