---
type: source
title: "Shopify Trocou Redis por MySQL e Segurou US$ 5,1 Milhões por Minuto na Black Friday"
aliases: ["shopify redis mysql", "shopify skip locked", "shopify grande rollback"]
date_created: 2026-07-07
date_updated: 2026-07-07
source_count: 0
tags: [mysql, redis, skip-locked, concorrencia, deadlock, connection-pooling, black-friday, shopify, grande-rollback, e-commerce, backend]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/shopify-redis-para-mysql-skip-locked-black-friday.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-07
---

# Shopify Trocou Redis por MySQL e Segurou US$ 5,1 Milhões por Minuto na Black Friday

## TL;DR

A Shopify substituiu a reserva de estoque baseada em [[wiki/concepts/redis]] + [[wiki/concepts/mysql]] por um modelo 100% MySQL usando [[wiki/concepts/skip-locked]] — cada unidade de estoque virou uma linha real na tabela. Corrigiram três problemas clássicos de banco relacional (chave primária mal desenhada, gap locking, ordem de execução divergente) e, mesmo assim, bateram num teto de escalabilidade que só foi resolvido instrumentando **tempo de conexão segurada por operação** — descobrindo que o gargalo real não era a reserva de estoque, e sim partes antigas do checkout monopolizando conexões. Resultado: -50% leituras, -33% transações, CPU do banco <50% nos picos, segurando US$ 5,1 milhões/minuto na Black Friday de 2025.

## Key Claims

| Claim | Evidência | Confiança |
|---|---|---|
| A arquitetura antiga usava Redis para reserva rápida e MySQL como fonte única de verdade do estoque, sincronizados por duas escritas não-atômicas | Fluxo descrito na fonte: reservar no Redis → confirmar pagamento → atualizar MySQL → limpar Redis; sem garantia de ordem entre as duas escritas | Alta |
| `SELECT ... FOR UPDATE SKIP LOCKED` (MySQL 8+, disponível desde 2018) permite workers pularem linhas já travadas por outro processo, eliminando fila/contenção | Modelo consistente com [[wiki/concepts/distributed-lock]] e a referência de `tech-mentor-backend/distributed-locking.md`; suportado também pelo PostgreSQL 9.5+ | Alta |
| Migraram de "estoque como coluna numérica" para "estoque como N linhas físicas na tabela" — reservar 3 unidades = mover 3 linhas específicas numa única transação atômica | Analogia da fonte: de "placa com número" para "caixas reais numa prateleira" | Alta |
| Para produtos com estoque muito grande, usam pool limitado a 1.000 linhas por produto/local, com reposição automática e trava de concorrência no processo de reabastecimento | Estratégia explicitada na fonte para evitar criar milhões de linhas de uma vez | Alta |
| Bateram em três problemas clássicos de banco: chave primária mal desenhada (deadlock), gap locking padrão do MySQL bloqueando espaços vazios ao redor da linha, e operações rodando em ordens diferentes entre si | Analogia da fonte: gap locking como "segurança que fecha o corredor inteiro em vez do apartamento" | Alta |
| Mesmo com locks e queries otimizadas, o sistema bateu um teto de escalabilidade com CPU baixa e latência ok — o gargalo não estava em nenhuma query isolada | Analogia da fonte: "motor bom, carro não passa de 80km/h" — indício de gargalo sistêmico, não localizado | Alta |
| O diagnóstico correto veio de etiquetar cada operação SQL por origem e medir **tempo de conexão segurada por operação**, não a latência de queries individuais | Distinção central da fonte: "não estava olhando qual query tava lenta, estava olhando quem tá monopolizando uma conexão" | Alta |
| O gargalo real não era a reserva de estoque — era código legado no checkout segurando conexões por tempo desproporcional; a reserva só expôs o sintoma | Analogia da fonte: "vizinho sem noção que estaciona na sua vaga" | Alta |
| Após limpar o caminho do checkout e revisar a configuração padrão do MySQL (não tocada há anos), resultado foi -50% leituras, -33% transações, CPU do banco <50% nos picos de Black Friday | Métricas citadas diretamente na fonte | Alta |
| A Shopify segurou US$ 5,1 milhões em vendas por minuto na Black Friday de 2025, atendendo ~14% dos e-commerces americanos | Números citados na fonte como contexto de escala | Média (não há link para o artigo original nesta ingestão) |
| O caso referencia a [[wiki/entities/37signals]] e o **Solid Queue** — fila de processamento 100% sobre banco relacional, sem broker externo — como inspiração/precedente para a ideia de que "você provavelmente não precisa do que acha que precisa" | Menção direta na fonte ao case de saída do cloud da 37signals/Basecamp | Média |
| Esse tipo de gargalo (tempo de conexão segurada, não latência de query) não é diagnosticável perguntando a uma IA "otimize esta query" — exige instrumentação e uma pergunta que só quem entende a arquitetura sabe formular | Argumento explícito da fonte sobre o papel do engenheiro vs. ferramenta de IA | Média (opinião do autor da fonte, não dado bruto) |

## Concepts & Entities Touched

[[wiki/concepts/skip-locked]] · [[wiki/concepts/redis]] · [[wiki/concepts/mysql]] · [[wiki/concepts/distributed-lock]] · [[wiki/concepts/deadlock]] · [[wiki/concepts/connection-pooling]] · [[wiki/concepts/cache]] · [[wiki/concepts/grande-rollback]] · [[wiki/concepts/solid-queue]] · [[wiki/entities/shopify]] · [[wiki/entities/37signals]] · [[wiki/sources/skip-locked-fencing-token]] · [[wiki/sources/como-arquitetar-com-cache-e-redis]] · [[wiki/sources/uuid-primary-key-mysql]] · [[wiki/sources/listen-notes-boring-tech-one-person-company]]

## Open Questions

- O artigo original da Shopify não foi linkado nesta transcrição — falta a fonte primária (URL do engineering blog da Shopify) para verificar números e detalhes técnicos exatos (nome real da PK mal desenhada, versão exata do MySQL).
- Como exatamente a Shopify instrumentou "tempo de conexão segurada por operação"? A fonte não detalha a ferramenta (APM, tracing customizado, `performance_schema` do MySQL?).
- O pool de 1.000 linhas por produto/local — como a reposição automática decide o tamanho do lote e evita esgotar durante o refill?
- Existe conflito em potencial com [[wiki/concepts/skip-locked]], que já documenta o mesmo padrão a partir de outra fonte ([[wiki/sources/skip-locked-fencing-token]]) focada em filas de job — vale reconciliar os dois casos de uso (fila de trabalho vs. reserva de estoque) na página de conceito.
- Vale checar se "Thirty-Seven Signals" (mal transcrito no áudio original) é de fato a referência pretendida pela fonte, ou se seria outra empresa — mantido como interpretação de melhor esforço.
