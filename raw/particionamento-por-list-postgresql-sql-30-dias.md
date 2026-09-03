# Particionamento por LIST no PostgreSQL — Playlist "Como ser bom em SQL em apenas 30 dias" (dia 13)

Transcrição de vídeo em português, limpa e organizada em Markdown a partir de fala bruta.

---

Vamos falar hoje sobre particionamento por LIST na tua tabela no banco de dados, para que tu tenha essa noção e saiba como fazer uma busca performática se o teu banco de dados está enorme, tu tem milhões de registros numa tabela e não sabe o que fazer.

Isso aqui faz parte da playlist que eu estou fazendo de "como ser bom em SQL em apenas 30 dias". No vídeo do dia 12 (já lançado, com 476 visualizações) eu trabalhei com tabelas com milhões de registros e expliquei como usar particionamento por RANGE nessas tabelas: mostrei função, criação de índices e como definir um determinado particionamento. Recomendo assistir o dia 12 antes deste vídeo.

## Particionamento por LIST

Nesse vídeo do dia 12 a gente trabalhou com o particionamento por RANGE. Agora vou mostrar uma outra opção: o particionamento por LIST.

O particionamento por lista é interessante quando existe um **conjunto conhecido de valores** dentro da tua tabela. Por exemplo: vendas divididas por estado. Uma tabela de vendas por estado com, digamos, 10 milhões de registros — aí eu uso a estratégia de particionamento por LIST.

### Criando a tabela particionada

Ambiente: DBeaver, banco de dados chamado "YouTube", com os esquemas criados nas aulas anteriores da playlist.

```sql
CREATE TABLE venda_estado (
  id BIGINT GENERATED ALWAYS AS IDENTITY,
  uf CHAR(2) NOT NULL,
  dt_venda DATE NOT NULL,
  vl_total NUMERIC(12,2) NOT NULL,
  PRIMARY KEY (id, uf)
) PARTITION BY LIST (uf);
```

Chave primária composta (`id`, `uf`) desta vez, diferente do exemplo do dia 12.

### Criando as partições por estado

Diferente da aula 12 (onde a `partition function` foi usada), aqui cada partição é criada separadamente com `CREATE TABLE ... PARTITION OF ... FOR VALUES IN (...)`:

```sql
CREATE TABLE venda_estado_sc PARTITION OF venda_estado
  FOR VALUES IN ('SC');

CREATE TABLE venda_estado_rs PARTITION OF venda_estado
  FOR VALUES IN ('RS');

CREATE TABLE venda_estado_pr PARTITION OF venda_estado
  FOR VALUES IN ('PR');
```

(No vídeo, o autor errou o nome da tabela do RS na primeira tentativa — `DROP TABLE venda_estado_rs;` e recriou corretamente.)

### Partição DEFAULT (catch-all)

Se chegar um INSERT para um estado que não tem partição própria, e não existir uma partição padrão, a inserção falha. Por isso se cria uma partição `DEFAULT`:

```sql
CREATE TABLE venda_estado_outros PARTITION OF venda_estado
  DEFAULT;
```

Qualquer UF que não seja SC, RS ou PR cai automaticamente nessa partição.

### Testando com INSERTs

```sql
INSERT INTO venda_estado (uf, dt_venda, vl_total)
VALUES ('SC', '2026-08-01', 123.00);

INSERT INTO venda_estado (uf, dt_venda, vl_total)
VALUES ('RS', '2026-08-01', 123.00);

INSERT INTO venda_estado (uf, dt_venda, vl_total)
VALUES ('SP', '2026-08-01', 3123.00);
```

- O registro de SC vai para `venda_estado_sc`.
- O registro de RS vai para `venda_estado_rs`.
- O registro de SP (sem partição própria — só SC, RS e PR foram criadas) vai automaticamente para `venda_estado_outros` (a partição DEFAULT).

### Conferindo

```sql
SELECT * FROM venda_estado WHERE uf = 'SC';
```

Retorna o mesmo resultado que consultar direto a partição filha (`SELECT * FROM venda_estado_sc`), mas via a tabela "guarda-chuva" (`venda_estado`) o PostgreSQL já roteia a query para a partição certa.

## Conclusão

Esse é o particionamento por LIST: útil quando existe um conjunto conhecido e finito de valores para a coluna de particionamento (ex.: estado/UF, categoria, tenant, status), diferente do particionamento por RANGE (dia 12), que é voltado a intervalos contínuos (ex.: datas). Pensar em qual contexto usar cada um dentro da própria solução é o que traz o ganho de performance em tabelas muito grandes.
