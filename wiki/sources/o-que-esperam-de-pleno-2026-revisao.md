---
type: source
title: "O Que Esperam de um Pleno na Programação — Revisão com 4 Anos de IA"
aliases: ["pleno 2026 revisão", "13 itens pleno programação", "o que esperam de pleno 4 anos depois"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/o-que-esperam-de-pleno-2026-revisao.md
source_url: ""
author: "não identificado com confiança (ver Nota de Identificação)"
date_published: ""
date_ingested: 2026-08-19
source_count: 0
tags: [carreira, pleno, mid-level, ia-para-devs, mercado-de-trabalho, soft-skills, testes, system-design, tooling]
skill: tech-mentor-leadership
status: draft
---

## TL;DR

Vídeo em que o apresentador revisita, um a um, os 13 itens de um vídeo próprio de 4 anos atrás sobre "o que esperam de um pleno na programação" (que viralizou, ~51 mil visualizações), motivado por um tweet de [[wiki/entities/erick-wendel]] marcando-o ao encontrar o vídeo antigo. Com ~4,5 anos de agentes de IA escrevendo código no meio do caminho, a releitura é pior do que o apresentador esperava: 6 dos 13 itens viraram commodity (a IA resolve melhor, mais rápido e mais barato — Git avançado e terminal), 3 foram rebaixados de "requisito de pleno" para "requisito de júnior" (estrutura de dados/algoritmos, dominar linguagem/paradigma, design patterns/arquitetura), 2 continuam praticamente inalterados (protocolos de transporte REST/WebSocket/GraphQL, system design), 2 ficaram mais importantes (tooling avançado, testes automatizados) e 1 se transformou (dominar um framework → trafegar por múltiplos frameworks). O item que fecha a lista — soft skills, incluindo code review, feedback, documentação e metodologias ágeis — foi classificado incorretamente no vídeo original como item de menor peso; nesta revisão, o apresentador o reclassifica como **o único item que hoje de fato justifica o salário de um pleno**, resumido na regra "não seja um idiota".

## Nota de Identificação

O texto não permite identificar o apresentador com segurança. Pistas textuais: (1) o vídeo original citado tem ~51 mil visualizações e 4 anos de idade a partir da data deste vídeo; (2) o canal tem um "canal irmão" de vlogs, citado na transcrição como "AI the Internet" — provável erro de ASR sobre um nome real não identificado; (3) menção a uma pessoa chamada Sara aparecendo em vlogs de sexta-feira/fim de semana; (4) patrocínio de uma fintech de nome citado como "High Globe", voltada a transferência internacional de valores para quem trabalha remoto do Brasil para EUA/Europa. Nenhuma dessas pistas bateu com entidades já registradas na wiki ([[wiki/entities/filipe-deschamps]], [[wiki/entities/codigo-fonte-tv]], [[wiki/entities/erick-wendel]]) nem foi confirmada por busca externa. Fonte registrada sem entity de autor dedicada — se a identidade for confirmada numa ingestão futura, esta página deve ser atualizada e a entity correspondente, criada ou vinculada.

## Key Claims

**Claim:** Seis dos 13 requisitos originalmente listados para pleno (Git avançado — merge conflict manual, stash, patch, trunk-based vs. git flow — e comandos básicos de terminal) viraram commodity: a IA resolve isso de forma mais rápida, mais barata e melhor do que a execução manual.
**Evidence:** Relato de primeira pessoa: o apresentador diz não resolver um merge conflict manualmente há "muitos meses"; comandos de terminal (buscar, filtrar, mover, copiar arquivos) hoje são delegados a agentes operando dentro do próprio terminal via linguagem natural.
**Confidence:** média-alta como relato pessoal qualitativo; consistente com [[wiki/concepts/crud-resolvido]] e o eixo mais amplo de comoditização de execução por IA já registrado na wiki, mas sem dado quantitativo de mercado que confirme isso como expectativa consolidada de contratação.

**Claim:** Estrutura de dados/algoritmos, dominar uma linguagem/paradigma de programação, e design patterns/arquitetura — todos originalmente listados como requisito de pleno — foram rebaixados para requisito de júnior: o conceito continua indispensável, mas deixou de ser diferencial de nível intermediário.
**Evidence:** Argumento consistente nos três itens: mesmo com a IA implementando, o pleno ainda precisa do conceito para revisar o que a IA decidiu (ex.: saber que um Redis pode servir de fila FIFO; saber orientar a IA a refatorar três implementações num Abstract Factory).
**Confidence:** média — é reclassificação de opinião do próprio apresentador sobre o próprio vídeo antigo, sem comparação com dado de vaga/mercado atual; alinhado com a tese de [[wiki/concepts/alto-nivel-antes-do-fundamento]] e com o rebaixamento simétrico observado em [[wiki/sources/o-que-sobrou-pro-dev-junior-eric-wendel]].

**Claim:** Tooling avançado (SSH, proxy/interceptação de requisição como Charles Proxy, mock de API) ficou mais importante do que era, porque a IA ainda erra ou falha ao configurar corretamente esse tipo de ferramenta em dispositivos reais.
**Evidence:** Relato de primeira pessoa: o apresentador diz continuar configurando manualmente esse tipo de ferramenta, embora a IA já facilite partes pontuais (adicionar/remover IP de proxy em dispositivos).
**Confidence:** média — relato pessoal isolado, sem comparação com outra fonte da wiki sobre esse tópico específico (tooling de proxy/interceptação não tem página própria ainda).

**Claim:** Testes automatizados ficaram mais importantes para pleno, porque a IA gera volume de código grande demais para revisão humana linha a linha — a validação de qualidade precisa ser determinística (testes + CI), não apenas revisão humana ou revisão de uma IA sobre outra IA.
**Evidence:** Relato de primeira pessoa: o apresentador diz escrever mais testes do que nunca e delegar cada vez menos a escrita autônoma de testes à IA, preferindo planejar quais testes escrever e como rodá-los no CI.
**Confidence:** alta como argumento qualitativo — converge diretamente com [[wiki/concepts/piramide-de-testes]] e com o pilar de testes como "seguro contra decisões ruins da IA" já registrado via [[wiki/sources/roadmap-dev-senior-2026]].

**Claim:** Dominar um único framework (2-3 anos de vivência) deixou de ser suficiente — o mercado passou a esperar trânsito entre múltiplos frameworks/stacks (ex.: dev de Android nativo contribuindo também no projeto iOS nativo; dev de backend contribuindo em frameworks de frontend e backend diferentes).
**Evidence:** Exemplos anedóticos citados pelo apresentador, sem nome de empresa ou fonte de mercado formal.
**Confidence:** baixa-média — puramente anedótico ("amigos meus que são dev backend"), sem dado de vaga ou pesquisa de mercado citado.

**Claim:** Protocolos de transporte (REST, WebSocket vs. polling, GraphQL) e system design (desenhar sistema no quadro branco) são os dois itens do vídeo original que "envelheceram bem" — permanecem como requisito de pleno sem alteração relevante na revisão.
**Evidence:** O apresentador afirma que a diferença entre WebSocket/polling/GraphQL continua sendo conhecimento necessário para revisar a escolha de transporte/infra sugerida pela IA, e que desenhar uma solução no quadro branco continua sendo um "baita conhecimento" para pleno.
**Confidence:** média-alta — consistente com [[wiki/concepts/niveis-de-senioridade-system-design]], que já documenta system design como expectativa estável (não em queda) para pleno/sênior em outras fontes da wiki.

**Claim:** Soft skills (code review, feedback, documentação, metodologias ágeis) foram classificadas incorretamente no vídeo original, colocadas por último como se fossem menos relevantes; nesta revisão, o apresentador as reclassifica como o único item que hoje justifica de fato o salário de um pleno — resumido na regra "não seja um idiota, seja uma pessoa agradável de se trabalhar".
**Evidence:** Autocorreção explícita do próprio apresentador sobre o próprio vídeo antigo — não é uma nova claim externa, é uma reclassificação de peso relativo dentro da mesma lista de 13 itens.
**Confidence:** média como argumento qualitativo — é a tese central e mais forte do vídeo, mas depende inteiramente do julgamento do próprio autor sobre a própria lista antiga, sem triangulação com dado de mercado (ex.: texto de vaga, pesquisa salarial) que confirme "soft skills" como o critério decisivo de contratação/remuneração de pleno em 2026.

## Os 13 Itens: Tabela de Reclassificação

| # | Item (2022) | Reclassificação (2026) |
|---|---|---|
| 1 | Git avançado (merge conflict, stash, patch, git flow/trunk-based) | Commodity — IA resolve |
| 2 | Comandos básicos de terminal | Commodity — IA resolve dentro do próprio terminal |
| 3 | Estrutura de dados e algoritmos | Rebaixado: pleno → júnior |
| 4 | Tooling (SSH, proxy, mock de API) | Ficou **mais** importante |
| 5 | REST/WebSocket vs. polling/GraphQL | Inalterado — atemporal |
| 6 | Dominar linguagem/paradigma de programação | Rebaixado: pleno → júnior (paradigma, não sintaxe) |
| 7 | SQL e bancos de dados | Mantido em pleno, foco desloca de escrever query para conceitos (sharding, indexação, chaves) |
| 8 | Testes automatizados | Ficou **mais** importante |
| 9 | Gerenciamento de dependências | Mantido, com camada nova de segurança de supply chain |
| 10 | Design patterns e arquitetura | Rebaixado: pleno → júnior |
| 11 | Dominar um framework (2-3 anos) | Transformado: framework único → trânsito entre múltiplos frameworks |
| 12 | System design (quadro branco) | Inalterado — atemporal |
| 13 | Soft skills (code review, feedback, docs, ágil) | **Reclassificado de último para o único item que justifica o salário** |

## Entidades e Conceitos Tocados

- [[wiki/entities/erick-wendel]] — gatilho do vídeo (tweet marcando o apresentador)
- [[wiki/concepts/crud-resolvido]]
- [[wiki/concepts/sintaxe-vs-conhecimento-perene]]
- [[wiki/concepts/engenheiro-vs-programador]]
- [[wiki/concepts/fundacao-tecnica]]
- [[wiki/concepts/apagao-de-seniors]]
- [[wiki/concepts/piramide-de-testes]]
- [[wiki/concepts/worktree-paralelismo]]
- [[wiki/concepts/niveis-de-senioridade-system-design]]
- [[wiki/concepts/vaga-junior-vira-pleno]]
- [[wiki/concepts/soft-skills-como-diferencial-de-pleno]] (novo)

## Open Questions

- **Identidade do apresentador não confirmada** — ver Nota de Identificação acima. Requer confirmação humana ou busca externa mais aprofundada numa ingestão futura.
- **Reclassificação é autoavaliação, não dado de mercado** — nenhuma das 13 reclassificações foi cruzada com dado real de vaga/pesquisa salarial de 2026; é inteiramente a opinião do próprio autor revisitando a própria lista. Vale contrastar futuramente com [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] e [[wiki/sources/leetcode-system-design-entrevista-versus-trabalho-real-na-era-da-ia]], que trazem dado de campo mais concreto sobre expectativas por nível.
- **Tensão não resolvida com [[wiki/concepts/vaga-junior-vira-pleno]]:** se estrutura de dados, paradigma de linguagem e design patterns foram rebaixados de pleno para júnior, isso poderia sugerir que a régua de júnior subiu — reforçando o padrão de "vaga júnior exigindo pleno" já documentado. Mas o vídeo não fala de texto de vaga real, então essa conexão é inferência desta ingestão, não afirmação da fonte.
- **Item de tooling (SSH/proxy/mock) ainda não tem página conceito própria na wiki** — mencionado aqui e espalhado em menções soltas de outras fontes (Charles Proxy, mock de API), mas sem uma página dedicada que consolide o tema. Candidato a stub numa ingestão futura se mais fontes tocarem o assunto.
