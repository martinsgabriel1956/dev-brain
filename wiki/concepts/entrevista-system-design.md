---
type: concept
title: "Entrevista de System Design (Whiteboard Interview)"
aliases: ["system design interview", "whiteboard interview", "lousa branca", "entrevista de arquitetura"]
date_created: 2026-07-20
date_updated: 2026-07-27
source_count: 4
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

## O Mesmo Formato, Profundidade Diferente por Nível

[[wiki/concepts/niveis-de-senioridade-system-design]] argumenta que a estrutura de sessão descrita acima é aplicada de forma quase idêntica para júnior, pleno e sênior (herança do padrão popularizado pelo Google) — o que muda entre os níveis não é o formato, é a profundidade esperada: júnior demonstra fundação e resolve um sistema simples (encurtador de URL, jogo de xadrez com 2 usuários); pleno soma requisitos não funcionais e racional prático de tradeoffs; sênior discute escalabilidade, CAP e sharding em profundidade e **lidera** a conversa em vez de apenas reagir a ela. Importante: essa cobrança na entrevista não reflete necessariamente o uso real de system design no trabalho — júnior e pleno usam pouco no dia a dia, enquanto a compreensão do sistema inteiro só se torna central a partir de sênior.

## O Pipeline Completo ao Redor da Sessão (Padrão BigTech)

[[wiki/sources/anatomia-entrevista-system-design-bigtech]] situa a sessão de system design dentro de um pipeline maior de 5 etapas comum a empresas que seguem o padrão bigtech: entrevista de RH → entrevista técnica/questionário → LeetCode ou take-home → **entrevista de system design** → reunião final de fit com engineering manager/equipe. Argumenta que preparar-se para o padrão mais exigente (bigtech) cobre automaticamente entrevistas menos rigorosas. Detalha também o *porquê* de cada etapa da sessão em si (requisitos funcionais/não funcionais, BOE, design de API, esquema híbrido SQL+NoSQL, HLD, tradeoffs) do ponto de vista do que o entrevistador está avaliando — não é decorar caixinhas, é compreensão do problema exposta em voz alta. Resume com "garbage in, garbage out": a solução só é tão boa quanto a compreensão do problema que a precede.

## Key sources

- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]]
