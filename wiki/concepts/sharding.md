---
type: concept
title: "Sharding"
aliases: ["database sharding", "particionamento horizontal", "shard", "shard key"]
date_created: 2026-06-26
date_updated: 2026-08-03
source_count: 3
tags: [system-design, banco-de-dados, sharding, escalabilidade, distribuido]
skill: tech-mentor-system-design
status: stub
---

# Sharding

Estratégia de escalar banco de dados horizontalmente **dividindo os dados em múltiplos bancos** (shards). Cada shard contém um subconjunto dos dados — nenhum shard tem tudo.

```
Shard 1: usuários 1–1.000.000
Shard 2: usuários 1.000.001–2.000.000
Shard 3: usuários 2.000.001–3.000.000
```

A chave que determina qual shard recebe qual dado é chamada de **shard key**.

## Por que sharding existe

Bancos de dados são [[stateless-nao]] por natureza — eles *são* o estado. [[escalabilidade-vertical]] tem teto físico. [[replicacao-de-banco]] ajuda com leitura, mas escrita ainda vai para um único primário. Sharding divide tanto leitura quanto escrita.

## Trade-offs

| Vantagem | Desvantagem |
|---|---|
| Escala leitura e escrita | Queries cross-shard são complexas e lentas |
| Sem teto teórico de dados | Joins entre shards são proibidos ou caros |
| Cada shard é menor e mais rápido | Re-sharding (redistribuir dados) é doloroso |
| Falha de um shard não derruba todo o sistema | Shard key mal escolhida cria hot spots |

## Escolha da shard key

A escolha da shard key é crítica:

- **Distribuição uniforme** — evita hot spots onde um shard recebe 80% do tráfego
- **Colocalização de dados relacionados** — queries que acessam dados do mesmo usuário devem ir para o mesmo shard
- **Imutabilidade** — a shard key não deve mudar após a inserção

## Boa Shard Key ≠ Boa Distribuição

Uma shard key pode passar em todos os critérios formais (alta afinidade de relacionamento, alta cardinalidade) e ainda gerar hotspot, se o **método de distribuição** escolhido não for aleatório. Exemplo: fragmentar `user_id` em 3 faixas fixas (0–1M, 1M–2M, 2M–2.5M) usa uma chave boa, mas o shard com a faixa mais recente de IDs sofre mais tráfego que os demais — porque, na maioria dos sistemas reais, usuários cadastrados mais recentemente tendem a ser os mais ativos (usuários antigos podem já ter abandonado a plataforma). Esse é um padrão de distribuição chamado **range-based sharding**: raramente recomendado como padrão de mercado, porque intervalos fixos tendem a concentrar tráfego onde o acesso real não é uniforme no tempo — mesma razão pela qual fragmentar por `created_at` (coluna cronológica) sempre concentra hotspot no shard mais recente. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Problema da Celebridade (Hotspot por Entidade)

Mesmo com uma boa shard key e boa distribuição, uma única entidade com alcance desproporcional (ex.: um usuário extremamente popular numa rede social) pode sobrecarregar sozinha o shard onde caiu — o volume de interações nas publicações dessa entidade não é comparável ao de um usuário comum. Soluções citadas: distribuir manualmente os dados dessa entidade entre vários shards, ou isolar um **shard dedicado** só para ela (ou um grupo de entidades de alto alcance), podendo escalá-lo verticalmente à parte dos demais. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Tabelas Sem Relação Direta com a Shard Key: Shard Global

Nem toda tabela tem FK para a entidade escolhida como shard key (ex.: num sistema hospitalar shardeado por paciente, a tabela "fornecedor de medicamento" não tem relação direta com paciente). Duas abordagens: criar um **shard global** com as tabelas comuns sem relacionamento direto, ou **replicar** essas tabelas em todos os shards via mensageria/replicação de dados — nos dois casos, essas tabelas contornam o roteador de hash e vão direto para qualquer shard. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Sharding Pressupõe Decomposição por DDD/Microsserviços

Não faz sentido tentar fazer sharding de um monolito inteiro com centenas de tabelas: o resultado é fragmentar poucas tabelas centrais e replicar dezenas de outras em todo shard. A ordem correta é primeiro decompor o sistema em [[wiki/concepts/microsservicos]] guiados por [[wiki/concepts/ddd|DDD]] (bounded contexts) e só então aplicar sharding no banco de dados de um microsserviço específico, onde uma única entidade/shard key central faz sentido. Ver [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]].

## Quando usar

- Volume de dados supera a capacidade de um único servidor
- Writes por segundo ultrapassam o limite do banco primário
- [[replicacao-de-banco]] não é suficiente (só escala reads)

## Alternativas antes do sharding

1. [[escalabilidade-vertical]] — mais RAM/CPU no banco (mais simples)
2. [[replicacao-de-banco]] — read replicas para aliviar leitura
3. [[cache]] — reduzir hits ao banco antes de distribuí-lo

> **Regra:** sharding é complexo. Esgote as alternativas primeiro.

## Relação com outros conceitos

- [[replicacao-de-banco]] — a outra estratégia de escalar banco; complementar ao sharding
- [[cap-theorem]] — sharding força decisões sobre consistência vs disponibilidade
- [[escalabilidade-horizontal]] — sharding é a escalabilidade horizontal aplicada ao banco de dados
- [[gargalo]] — banco é o gargalo mais comum; sharding é o último recurso para ele

- [[wiki/concepts/control-plane]] — camada de coordenação necessária para mover dados/usuários entre shards
- [[wiki/concepts/large-scale-architecture]] — sharding como técnica central do princípio "dividir para conquistar"

## Key sources

- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]]
- [[wiki/sources/large-scale-vs-complex-architecture]] — sharding citado como exemplo de técnica que escala TPS/resiliência sem necessariamente tornar a arquitetura "complexa" em alto nível; movimentação de usuário entre shards como caso concreto que exige control plane
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — distinção entre boa shard key e boa distribuição (range-based por faixa fixa de `user_id` vs. por `created_at`), problema da celebridade, shard global para tabelas sem FK à shard key, e sharding como passo posterior à decomposição por DDD/microsserviços
