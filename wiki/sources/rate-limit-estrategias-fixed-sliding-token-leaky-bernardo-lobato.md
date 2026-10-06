---
type: source
title: "Rate Limit: estratégias de implementação (fixed, sliding, token bucket, leaky bucket)"
aliases: ["rate limit estratégias bernardo lobato", "rate limit parte 2"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rate-limit-estrategias-fixed-sliding-token-leaky-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [rate-limiting, fixed-window, sliding-window, token-bucket, leaky-bucket, kong, client-rate-limit, bursts]
skill: tech-mentor-backend
status: draft
---

# Rate Limit: estratégias de implementação (fixed, sliding, token bucket, leaky bucket)

Parte 2 de [[wiki/sources/rate-limit-arquitetura-onde-aplicar-estado-compartilhado-bernardo-lobato]] (parte 1: onde aplicar e estado compartilhado).

## TL;DR

[[wiki/entities/bernardo-lobato]] compara quatro algoritmos de [[wiki/concepts/rate-limiting]] pelo **comportamento que produzem**, não por sofisticação: [[wiki/concepts/fixed-window-rate-limit]] (cota por janela; simples, mas com [[wiki/concepts/burst-na-fronteira-da-janela]]), [[wiki/concepts/sliding-window-rate-limit]] (últimos 60 s; preciso, mais estado), [[wiki/concepts/token-bucket]] (taxa média + pico controlado; permite [[wiki/concepts/rate-limit-pesos-por-endpoint]]) e [[wiki/concepts/leaky-bucket]] (saída com taxa controlada; protege recurso pouco elástico, ex.: legado). Caso real: token bucket com pesos (10.000 tokens/h por cliente; 1 token no portal, ~1000 na sincronização) controlou picos sem mudar a API e ensinou clientes via 429. Também apresenta o [[wiki/concepts/client-rate-limit]] (limitar as próprias chamadas a APIs de parceiros). Síntese em [[wiki/concepts/rate-limit-escolha-de-algoritmo]]. A parte 3 (produção: estado compartilhado, concorrência, indisponibilidade do limiter) é só proposta.

## Key claims

**Claim:** fixed window permite 200 requisições em ~2 s quando o cliente concentra 100 no fim de uma janela e 100 no início da próxima, sem violar a regra.
**Evidence:** exemplo 10:00:59 / 10:01:00 do vídeo.
**Confidence:** alta; `[skill: tech-mentor-backend]` (`rate-limiting.md`) descreve o mesmo "boundary burst". Ver [[wiki/concepts/burst-na-fronteira-da-janela]].

**Claim:** fixed window continua adequado para cota contratual e para barreira simples em API pública/login (inclusive contra força bruta); Kong suporta por consumidor, credencial, IP, serviço, rota.
**Evidence:** "se contratualmente devemos entregar X requisições por minuto... esse pode ser o modelo ideal"; menção à documentação do Kong.
**Confidence:** alta no raciocínio; suporte do Kong é relato do áudio `[external, não verificado]`.

**Claim:** sliding window elimina a fronteira fixa ao contar "os últimos 60 s", ao custo de mais memória, I/O e lógica (contador simples não basta), pior em arquitetura distribuída.
**Evidence:** "um simples array com contador não resolve mais."
**Confidence:** alta. `[skill: tech-mentor-backend]` distingue **Sliding Window Log** (O(N), exato) de **Sliding Window Counter** (O(1), ponderado, ~90% de precisão, escolha padrão); o vídeo não faz essa distinção e o custo descrito vale para o log. Ver [[wiki/concepts/sliding-window-rate-limit]].

**Claim:** token bucket acumula tokens até a capacidade (100 tokens/s de reposição, balde de 200: até 200 requisições de uma vez) e controla taxa média com picos limitados.
**Evidence:** exemplo numérico do vídeo.
**Confidence:** alta; coincide com o skill (capacidade + refill rate, bursts até a capacidade).

**Claim:** o custo por requisição pode variar por endpoint (peso 10 vs. 1), protegendo recursos caros sem tratar tudo como uniforme.
**Evidence:** exemplo de pesos e o caso real da sincronização. O skill menciona rate limit por custo de operação.
**Confidence:** alta. Ver [[wiki/concepts/rate-limit-pesos-por-endpoint]].

**Claim:** no caso real, 10.000 tokens/h por cliente com peso 1 (portal) e ~1000 (sincronização) controlou os picos sem alterar o código da API, isolou o portal e levou clientes a ajustar processos por causa dos 429.
**Evidence:** relato em primeira pessoa, número de clientes aproximado ("uns 10").
**Confidence:** média (relato único, sem métricas). Ver [[wiki/concepts/http-429-too-many-requests]].

**Claim:** leaky bucket serve para transformar entrada irregular em saída previsível, útil quando o backend é pouco elástico (legado); não está atrelado a HTTP (PDF, imagem, e-mail, relatório).
**Evidence:** exemplo do serviço de ~100 req/s.
**Confidence:** alta; o autor ressalva que a "fila" é só didática, **não** processamento assíncrono nem event sourcing. Skill: fila FIFO com taxa constante, overflow descarta ou devolve 429. Nuance: a parte 1 só usava a analogia.

**Claim:** além de limitar quem chama a API, convém limitar as **próprias chamadas** a APIs de terceiros (client rate limit), pois não se conhece a capacidade do parceiro nem se pode validar o controle dele.
**Evidence:** exemplos iFood e ingresso.com.
**Confidence:** média-alta; exemplos ilustrativos, não descrevem sistemas reais desses produtos. Ver [[wiki/concepts/client-rate-limit]].

**Claim:** os algoritmos não são melhores ou piores entre si; a escolha segue o comportamento desejado.
**Evidence:** tabela e fechamento. **Confidence:** alta (posição do autor; alinhada ao skill, que dá Sliding Window Counter como padrão geral e Token Bucket para bursts controlados).

## Entidades

[[wiki/entities/bernardo-lobato]], [[wiki/entities/kong]], [[wiki/concepts/redis]] (citado como próximo passo).

## Conceitos

[[wiki/concepts/rate-limiting]], [[wiki/concepts/fixed-window-rate-limit]], [[wiki/concepts/sliding-window-rate-limit]], [[wiki/concepts/token-bucket]], [[wiki/concepts/leaky-bucket]], [[wiki/concepts/burst-na-fronteira-da-janela]], [[wiki/concepts/rate-limit-pesos-por-endpoint]], [[wiki/concepts/client-rate-limit]], [[wiki/concepts/rate-limit-escolha-de-algoritmo]], [[wiki/concepts/rate-limit-estado-compartilhado]], [[wiki/concepts/http-429-too-many-requests]].

## Open questions

[[wiki/questions/rate-limit-producao-atomicidade-fail-open-e-janela-distribuida]]; contabilização de falhas e chave de identificação continuam em [[wiki/questions/rate-limit-contabilizar-requisicao-falha-e-chave-de-identificacao]].

## Quotes

- "Cada uma representa seu próprio comportamento que deve ser utilizado para resolver o problema que você já tem... não temos bala de prata."
- "O token bucket não trata todo o pico como um problema... admite a existência e permite que o sistema defina quanto desses bursts ele consegue consumir."
- "Transformar uma entrada potencialmente irregular em uma saída mais previsível."
