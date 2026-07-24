---
type: concept
title: "Entrevista de System Design (Whiteboard Interview)"
aliases: ["system design interview", "whiteboard interview", "lousa branca", "entrevista de arquitetura"]
date_created: 2026-07-20
date_updated: 2026-07-24
source_count: 2
tags: [system-design, entrevistas, arquitetura, carreira]
skill: tech-mentor-system-design
status: draft
---

# Entrevista de System Design (Whiteboard Interview)

Etapa de entrevista técnica em grandes empresas em que o candidato precisa desenhar, ao vivo, a arquitetura de um sistema (ex.: "como você faria um Twitter", "como você criaria um encurtador de URL"). Diferente da [[wiki/concepts/entrevista-tecnica-coding|entrevista de coding]] (que avalia resolução de algoritmo), aqui o que está em jogo é repertório de arquitetura, maturidade técnica e capacidade de propor um sistema escalável e disponível. **System design não é design system** — são coisas diferentes.

## Estrutura recomendada da sessão (40–50 minutos)

A ordem importa tanto quanto o conteúdo — desenhar antes de levantar requisitos é um erro clássico porque faltam elementos e passa a impressão de que o candidato não está engajando com o entrevistador.

1. **Levantar requisitos, não presumir.** Perguntar explicitamente quais são as funcionalidades *core* (essenciais) vs. auxiliares. O foco do desenho deve estar nas core; auxiliares ficam para o final, se sobrar tempo.
2. **Plano de capacidade.** Ver [[wiki/concepts/estimativas-back-of-envelope]] — requisições por segundo/minuto, picos de acesso, banda necessária, custo de armazenamento em disco (dia/ano/5 anos) e replication factor.
3. **Modelagem de dados e API.** Mostrar repertório de bancos de dados (RDBMS, chave-valor, busca) por caso de uso — sem se aprofundar em modelagem complexa — e modelar a [[wiki/concepts/contrato-de-api|API]]: endpoints principais, request/response, protocolo (HTTP, gRPC).
4. **Só então desenhar o [[wiki/concepts/high-level-design|high-level design]].** O desenho na lousa é a última etapa, não a primeira — e o entrevistador avalia se o desenho é coerente com tudo que foi levantado antes.

## Regra de ouro: só cite tecnologia que você domina

Depois do desenho, entrevistadores tendem a perguntar detalhes cada vez mais específicos sobre qualquer tecnologia citada (ex.: citar Prometheus como stack de métricas pode levar a perguntas sobre como funciona seu sistema de alarmes, o banco de dados interno, consultas em PromQL). Citar algo que você não domina de verdade é um risco alto — se for citar mesmo assim, faça um disclaimer explícito ("o time onde trabalhei usava isso, mas não tenho profundidade nela").

## O objetivo estrutural é levar você a dizer "não sei"

Assim como na [[wiki/concepts/entrevista-tecnica-coding|entrevista de coding]], o entrevistador desce o nível de dificuldade das perguntas até encontrar o limite real de conhecimento do candidato. Isso é esperado, não reprovável — o erro é tentar "sabonetear" (enrolar) a resposta em vez de admitir a lacuna e demonstrar interesse em aprender sobre o tema.

## Relação com outros conceitos

- [[wiki/concepts/estimativas-back-of-envelope]] — o plano de capacidade é etapa obrigatória, não opcional
- [[wiki/concepts/high-level-design]] — o desenho final da sessão
- [[wiki/concepts/modelagem-de-dados]] e [[wiki/concepts/contrato-de-api]] — etapas intermediárias antes do desenho
- [[wiki/concepts/entrevista-tecnica-coding]] — mesma estrutura de "levar o candidato ao limite", formato diferente (algoritmo vs. arquitetura)
- [[wiki/concepts/arquitetura-de-software]] — o repertório que a sessão avalia
- [[wiki/concepts/simulador-de-system-design]] — ferramenta de prática que simula tráfego sobre o desenho e pontua com IA, pensada para treinar o mesmo repertório fora do contexto de entrevista

## Practicar Fora do Contexto de Entrevista

[[wiki/sources/system-design-simulador-hotel-booking-replit]] argumenta que esse repertório não serve só para passar em entrevista — é a competência que sobra quando a IA escreve o código, inclusive para quem está apenas [[wiki/concepts/vibe-coding|vibe codando]] um projeto sem saber programar. Isso motivou a criação de um [[wiki/concepts/simulador-de-system-design]] como produto: um playground onde o mesmo repertório de gargalo, cache, escalabilidade e mensageria é treinado com feedback em tempo real, em vez de só desenhado numa lousa estática.

## Key sources

- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
