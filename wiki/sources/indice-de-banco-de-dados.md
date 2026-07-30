---
type: source
title: "Índice do Banco de Dados"
aliases: ["indice de banco de dados", "database index explicado", "b-tree hash composto parcial full-text spatial"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 0
tags: [banco-de-dados, index, b-tree, hash, postgresql, performance, system-design]
skill: tech-mentor-data
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/indice-de-banco-de-dados.md
source_url: ""
author: "Canal não identificado no áudio (série 'conceitos importantes da programação em pouco tempo'); menciona ter curso de system design)"
date_published: ""
date_ingested: 2026-07-29
---

## TL;DR

Transcrição de vídeo curto (série de conceitos rápidos) explicando o que é um índice de banco de dados e por que ele existe: uma estrutura de dados adicional (tipicamente B-tree) que troca espaço em disco e velocidade de escrita por velocidade de busca. Percorre os principais tipos — B-tree (padrão, bom para range), hash (match exato, O(1), sem suporte a range/ordenação/prefixo), composto, único vs. não único, parcial/filtered, full-text (índice invertido) e espacial (geolocalização) — e fecha com a regra de ouro: o índice certo é ditado pelo padrão de acesso da aplicação, não criado por padrão em toda coluna.

## Key Claims

- **Toda chave primária já vem com índice.** No Postgres isso é garantido — a PK (tipicamente um ID sequencial) já tem índice criado automaticamente; não é preciso criar um à parte. [confiança: alta, comportamento documentado do Postgres]
- **Sem índice, a busca é O(n) — table scan linha por linha.** Buscar um ID específico ou um nome sem índice na coluna força o banco a escanear a tabela inteira, sequencialmente, até achar (ou não achar) o valor. Ver [[wiki/concepts/database-index]].
- **Índice de B-tree é o padrão do Postgres, e o mais comum entre bancos relacionais.** A fonte demonstra visualmente a inserção sequencial de IDs (1 a 5) reorganizando a árvore a cada inserção, e depois uma busca pelo ID 7 resolvida em 3 comparações (>4? sim → direita; >6? sim → direita → encontrado) em vez de 7 comparações lineares — ilustração direta de O(log n) vs. O(n). Ver [[wiki/concepts/arvore]].
- **Índice tem custo de espaço e de escrita, não só benefício de leitura.** A estrutura adicional ocupa espaço em disco junto aos dados, e cada inserção precisa reordenar a árvore — custo computacional real. É por isso que a resposta para "por que não indexamos tudo?" é: só vale a pena se há buscas suficientes sobre aquela coluna para compensar o custo de escrita. Ver [[wiki/concepts/time-space-tradeoff]].
- **B-tree é bom para range queries porque valores próximos ficam fisicamente próximos na estrutura.** Buscar "todos os IDs entre 1 e 3" ou "todas as linhas criadas entre data X e data Y" (índice em `created_at`) tira proveito direto dessa localidade — hash não tem essa propriedade.
- **Índice hash serve só para igualdade exata (`=`), com complexidade média O(1).** Não funciona para range, ordenação ou prefixo (`LIKE 'Augus%'` não bate num índice hash). Onde faz sentido, é mais rápido que B-tree para esse caso específico. Ver [[wiki/concepts/hashmap]].
- **Índice composto continua sendo uma B-tree por baixo — "composto" e "estrutura de dados" são eixos independentes.** Um índice em `(name, email)` é uma única B-tree ordenada pela combinação das colunas, não duas estruturas separadas.
- **Único/não único é ortogonal a composto e a B-tree/hash.** É um constraint sobre o conteúdo do índice (permite ou não duplicatas), não sobre sua estrutura de dados ou quantas colunas cobre.
- **Índice parcial (partial/filtered) indexa só um subconjunto da tabela via condição `WHERE`.** Reduz tamanho do índice e custo de manutenção quando só um subset é comumente consultado — ex.: indexar apenas pedidos com `status = 'pending'`, ignorando o histórico. Ver [[wiki/concepts/database-index]] para o exemplo equivalente em SQL.
- **Full-text index constrói um índice invertido (palavra → onde aparece), com armazenamento pesado por mapear tokens individuais.** Caso de uso específico (busca em documentos/texto completo) mas, quando existe, compensa o custo de armazenamento. Ver [[wiki/concepts/indice-invertido]] e [[wiki/concepts/full-text-search]].
- **Índice espacial serve geolocalização/coordenadas** (ex.: "restaurantes a 2km desta posição") e é "perfeitamente inútil" fora desse caso de uso. Ver [[wiki/concepts/geohash]] e [[wiki/concepts/redis-geo]].
- **Regra de ouro: o índice é ditado pelo padrão de acesso, não criado por padrão.** Exemplo dado: busca por username numa rede social é muito mais frequente que criação de usuário novo — compensa indexar. A escolha entre B-tree (permite match parcial/prefixo) e hash (só match exato) também depende da necessidade da feature, não de uma regra fixa.
- Menciona, sem aprofundar, **covering index** e **clustered index** como tipos adicionais fora do escopo do vídeo.

## Entidades Mencionadas

- Sfia (patrocinador — cadeira ergonômica) — sem relação técnica, contexto publicitário apenas.

## Conceitos Relacionados

- [[wiki/concepts/database-index]]
- [[wiki/concepts/arvore]] — B-tree como estrutura subjacente do índice padrão
- [[wiki/concepts/hashmap]] — mecanismo do índice hash
- [[wiki/concepts/indice-invertido]] — mecanismo do full-text index
- [[wiki/concepts/full-text-search]]
- [[wiki/concepts/geohash]] — índice espacial
- [[wiki/concepts/redis-geo]]
- [[wiki/concepts/time-space-tradeoff]] — trade-off central de qualquer índice
- [[wiki/concepts/postgresql]] — B-tree como padrão do Postgres

## Contradições e Tensões com a Wiki

Nenhuma contradição encontrada. A fonte é consistente e mais didática/visual (demonstração passo a passo da B-tree se reordenando e da busca binária) que o material já registrado em [[wiki/concepts/database-index]] e nas fontes que o alimentam, mas não introduz nenhum claim técnico divergente. Reforça, com um exemplo visual próprio, o que já estava documentado sobre B-tree como padrão, hash como match exato O(1), e GIN/índice invertido para full-text — ver [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]], [[wiki/sources/full-text-search-mysql-postgresql]] e a skill `tech-mentor-data` (`references/databases/relational.md`, que cobre os mesmos tipos — B-tree, Hash, GIN, partial, composite — com exemplos SQL adicionais como `CREATE INDEX CONCURRENTLY` e índice funcional `LOWER(email)`, não mencionados nesta fonte).

## Quotes Brutas Preservadas

> "O índice que você vai criar, ele vai ser ditado pelo padrão de acesso — com que frequência você acessa esses dados e como que essas buscas são feitas."

> "Eu encontrei ele em três etapas, escaneando apenas três coisas, ao invés de ter que escanear sete linhas na minha tabela." — demonstração da busca do ID 7 na B-tree.
