---
type: source
title: "Como Projetar Sistemas: Um Passo a Passo Completo (Estudo de Caso: Encurtador de URLs)"
aliases: ["7 passos system design", "framework de 7 passos para system design", "como projetar qualquer sistema"]
date_created: 2026-08-21
date_updated: 2026-08-21
source_count: 0
tags: [system-design, framework, url-shortener, requisitos-funcionais, requisitos-nao-funcionais, monolito-vs-microsservicos, aws, dynamodb, api-gateway, cognito, entrevista-tecnica]
skill: tech-mentor-system-design
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-projetar-sistemas-encurtador-de-urls-passo-a-passo.md
source_url:
author:
date_published:
date_ingested: 2026-08-21
---

# Como Projetar Sistemas: Um Passo a Passo Completo (Estudo de Caso: Encurtador de URLs)

## TL;DR

Vídeo introdutório de system design que ensina um **framework genérico de 7 passos** (entender o problema → identificar requisitos funcionais/não-funcionais → prever padrões de tráfego → desenhar componentes em alto nível → definir APIs → selecionar stack técnica → considerar restrições de implementação), usando um encurtador de URLs como estudo de caso do início ao fim. Diferente de [[wiki/sources/case-url-shortener]] (que é um deep-dive técnico em decisões específicas do encurtador — Snowflake ID, cache em camadas, analytics async), esta fonte é sobre **o processo em si**: a regra de ouro é "não invente as regras, faça perguntas de esclarecimento", e a tecnologia só entra na etapa 6, depois de todo o raciocínio de requisitos, escala e componentes já estar fechado. Resolve o mesmo requisito de unicidade URL-curta↔URL-longa que a fonte-irmã via uma estratégia de hash com verificação de colisão e novo hash (salt) em caso de conflito — mais simples que a solução Snowflake ID já documentada, mas coerente com o próprio framework: "requisitos não funcionais claros primeiro, tecnologia depois."

## Key Claims

| Claim | Evidência |
|---|---|
| Arquitetura de software é o processo de determinar componentes, definir comunicação entre eles e garantir que atendam requisitos e padrões de qualidade — em entrevista, chamado de *system design* | Definição de abertura do vídeo |
| A palavra-chave ao projetar sistemas é **tradeoff**: prós e contras de cada decisão, pesados contra quais aspectos de qualidade (velocidade, custo, complexidade) importam mais | Tese central repetida ao longo de todo o vídeo, inclusive no fechamento |
| Regra de ouro: "não invente as regras, faça perguntas de esclarecimento" — requisitos não explícitos no enunciado (ex.: precisa de conta de usuário?) devem ser perguntados ao entrevistador, não presumidos | Exemplo concreto: o requisito de registro/login e gerenciamento de URLs só aparece depois de uma pergunta hipotética ao entrevistador |
| Requisitos se dividem em **funcionais** (o que o usuário pode fazer) e **não-funcionais** (qualidade técnica: performance, escalabilidade, disponibilidade, segurança) — os dois tipos devem ser levantados antes de desenhar qualquer coisa | Estrutura central do passo 2, com lista explícita de 4 requisitos funcionais e 4 não-funcionais para o encurtador |
| Proporção leitura:escrita de 100:1 (100M redirects/dia vs. 1M criações/dia) é o dado de escala que justifica investir mais poder de processamento no caminho de redirect do que no de criação | Estimativas do passo 3: 1M URLs criadas/dia, 100M redirects/dia, pico de ~10.000 redirects/s, retenção de 5 anos |
| A escolha entre monolito e microsserviços deve ser guiada pela necessidade real de escalar componentes de forma independente — com leitura 100x mais frequente que escrita, decompor em microsserviços permite escalar só o serviço de redirect, sem escalar a unidade inteira | Comparação monolito ("canivete suíço", escala tudo junto) vs. microsserviços ("caixa de ferramentas", escala cada peça) aplicada diretamente ao caso concreto do encurtador — mesma tese central já registrada em [[wiki/concepts/microsservicos]] e [[wiki/concepts/monolito]], aqui usada como critério de decisão, não como debate abstrato |
| Componentes de alto nível devem ser desenhados **sem nomear tecnologia específica** — só depois de requisitos, escala e componentes estarem claros é que se escolhe a stack | Passo 4 explicitamente evita citar banco de dados ou linguagem; passo 6 é o único ponto do framework em que ferramentas nomeadas (AWS) entram |
| Definição de API deve ocorrer antes da escolha de tecnologia, como contrato entre os componentes já desenhados | Passo 5 lista 6 endpoints (criar URL curta, redirecionar, registrar usuário, login, listar URLs do usuário, editar/deletar URL) só com verbo HTTP e formato de payload, sem stack |
| Numa arquitetura AWS de exemplo, a escolha de NoSQL (DynamoDB) sobre SQL é justificada por dois fatores concretos: dados naturalmente estruturáveis como chave-valor (short-code → URL) e o requisito não-funcional de baixa latência | Comparação explícita SQL (tabelas, joins) vs. NoSQL (chave-valor, menor latência de leitura) aplicada ao caso — mesma distinção documentada em [[wiki/concepts/dynamodb]], aqui usada como critério de decisão end-to-end |
| Redundância de servidores (mínimo dois por microsserviço) é a tática concreta para atender ao requisito não-funcional de resiliência a falhas, permitindo que a aplicação continue rodando mesmo se um servidor cair | Passo 6, ao justificar EC2 + Elastic Load Balancer |
| Ao final do processo, revisar a lista de requisitos originais contra o desenho é a forma de checar completude — e a fonte demonstra isso ao vivo, encontrando uma lacuna real: o requisito de unicidade 1:1 entre URL curta e longa não havia sido tratado nos passos anteriores | Passo 7: checklist explícito de 4 requisitos funcionais (✅ todos) e 4 não-funcionais (3 ✅, 1 pendente) — o autor trata a lacuna encontrada como parte do processo esperado, não como falha grave |
| Resolver a unicidade 1:1: fazer hash da URL longa, truncar para os primeiros caracteres como URL curta e, antes de gravar, checar colisão no banco — se colidir, adicionar um salt e re-hashear até obter um valor único | Solução proposta no passo 7, alternativa mais simples (e com custo de possível retry em colisão) à estratégia Snowflake ID + Base62 já registrada como preferida em [[wiki/sources/case-url-shortener]] |
| Estudar problemas clássicos (encurtador de URL, chat, feed de notícias, sistema de reservas, streaming de vídeo) compensa porque cada um exercita um conjunto diferente de fundamentos, e blocos de raciocínio se tornam reutilizáveis entre eles | Argumento de fechamento nº 1 |
| Justificar cada decisão de arquitetura contra o que se está abrindo mão — não escolher tecnologia por popularidade ou hype — é o que separa quem entende de quem decorou respostas | Argumento de fechamento nº 2 |

## Entidades

Nenhuma entidade (pessoa/organização) identificada explicitamente na transcrição — autor/canal não citado.

## Conceitos

- [[wiki/concepts/entrevista-system-design]] — nova variante do framework de sessão (7 passos, ênfase em "tecnologia só depois dos requisitos"), demonstrada ao vivo sobre um caso concreto
- [[wiki/concepts/arquitetura-de-software]] — definição de abertura reaproveitável como referência central do conceito
- [[wiki/concepts/microsservicos]] — decisão monolito vs. microsserviços aplicada como critério prático (proporção leitura:escrita) em vez de debate abstrato
- [[wiki/concepts/monolito]] — mesma aplicação prática, lado do monolito
- [[wiki/concepts/escalabilidade-horizontal]] — redundância de servidores (mínimo dois por microsserviço) como tática de resiliência, não só de volumetria
- [[wiki/concepts/api-gateway]] — Amazon API Gateway como ponto de entrada único da stack de exemplo
- [[wiki/concepts/dynamodb]] — escolha de NoSQL justificada por estrutura chave-valor + baixa latência
- [[wiki/concepts/http-redirect-301-302]] — menção rápida ao uso de 301/302 no redirect, sem aprofundar o tradeoff (que já está coberto na fonte-irmã)
- [[wiki/concepts/load-balancer]] — Amazon Elastic Load Balancer como resposta a servidores redundantes
- [[wiki/concepts/estimativas-back-of-envelope]] — estimativas de tráfego (1M criações/dia, 100M redirects/dia, proporção 100:1) como etapa formal do framework

## Open Questions

- **Autor/canal não identificado.** A transcrição não cita nome, canal ou afiliação. Diferente de outras fontes de system design já na wiki (ex.: [[wiki/entities/renato-augusto]]), não há elementos estilísticos suficientes aqui para inferir autoria com confiança — fica em aberto.
- **A solução de unicidade proposta (hash + truncamento + retry em colisão) não é comparada em custo/latência com a alternativa Snowflake ID + Base62** já registrada como preferida em [[wiki/sources/case-url-shortener]] — a fonte atual não entra em profundidade suficiente sobre taxa de colisão esperada com hash truncado em alta escala (100M/dia), que é justamente o ponto fraco que a fonte-irmã usa para descartar essa abordagem.
- **Cognito e Amplify não têm página própria na wiki ainda.** São citados como peças da stack de exemplo (autenticação gerenciada e hospedagem de front end), mas sem profundidade suficiente nesta fonte para justificar criação de stub — candidatos a página própria se uma fonte futura entrar em detalhe operacional sobre qualquer um dos dois.

## Key Sources

_Este é o documento primário._
