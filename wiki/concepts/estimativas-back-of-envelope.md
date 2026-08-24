---
type: concept
title: "Estimativas Back-of-Envelope"
aliases: ["back of envelope", "estimativas de escala", "capacity estimation"]
date_created: 2026-04-22
date_updated: 2026-08-21
source_count: 6
tags: [system-design, estimativas, entrevista, escala, capacity-planning]
skill: tech-mentor-system-design
status: stub
---

# Estimativas Back-of-Envelope

Cálculos rápidos de escala para validar decisões arquiteturais e identificar gargalos antes de desenhar o sistema.

## Template

```
Usuários ativos × frequência de ação = requests/s
Requests/s × tamanho médio = bandwidth
Requests/s × latência = concorrência (Little's Law → [[concepts/littles-law]])
Storage = volume × retenção × fator de replicação
```

## Exemplo Uber

```
5M motoristas × 1 update/4s    = 1.25M writes/s  → Redis, não PostgreSQL
1M corridas/hora (pico)        = 278 matches/s
278 matches × 10 ETA calls     = 2.780 routing/s  → 1-2 nós OSRM
Kafka: 1.25M msg × 50 bytes    = 60MB/s           → 10 partitions ok
Redis GEO: 5M × 70 bytes       = 350MB            → cabe em 1 instância
```

## Por que Fazer em Entrevista

Mostra que a escolha de tecnologia é baseada em números, não em preferência. "Redis porque é mais rápido" é fraco. "Redis porque PostgreSQL não suporta 1.25M writes/s" é arquitetura.

Em [[wiki/concepts/entrevista-system-design|entrevistas de system design]], esse "plano de capacidade" costuma ser explicitamente esperado como etapa da sessão — não algo opcional para quem quer impressionar: requisições por segundo/minuto, picos de acesso, banda necessária e replication factor em disco.

## Precisão Aumenta com o Nível de Senioridade

[[wiki/concepts/niveis-de-senioridade-system-design]] observa que estimativas de capacidade raramente são cobradas de júnior, aparecem "em algum nível" para pleno, e se tornam centrais e mais precisas para sênior — porque com pouco tempo de entrevista (1–2h), estimar de antemão o volume/escala esperado permite identificar gargalos (CPU? network?) preventivamente, antes de escolher onde investir profundidade (sharding, cache, réplicas).

## BOE Mede Noção de Escala, Não Precisão

[[wiki/sources/anatomia-entrevista-system-design-bigtech]] reduz o BOE a três perguntas centrais — requests/segundo, volume de dados armazenados, banda necessária — e enquadra o objetivo como validar se uma solução "de VPS de R$ 20" ainda serve ou se é preciso cache/replicação/particionamento. Reforça a mesma ideia de "cálculo de padeiro/guardanapo": não precisa ser preciso, precisa ser razoável o suficiente para orientar a arquitetura.

## Key Sources

- [[sources/case-uber]]
- [[wiki/sources/5-dicas-entrevistas-lousa-branca-system-design]]
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]]
- [[wiki/sources/anatomia-entrevista-system-design-bigtech]]
- [[wiki/sources/system-design-entrevista-cinema-draw-io]] — exemplo prático de omitir a etapa de propósito: o apresentador explicitamente não aprofunda BOE no rascunho, chamando escala/RPS de pergunta "mais para senioridades mais altas" fora do escopo do exercício
- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — a proporção leitura:escrita (100:1) como o número que efetivamente direciona uma decisão arquitetural (monolito vs. microsserviços), não só um dado de capacidade genérico
