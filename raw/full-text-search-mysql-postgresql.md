# Full-Text Search: Por Que o LIKE Está Errado (e Como Fazer Busca Inteligente em MySQL e PostgreSQL)

> Transcrição de vídeo em português (autor: Renato Augusto, canal com foco em arquitetura de software — menção explícita ao "Mapa do Arquiteto" no encerramento). Reestruturada em markdown com seções; conteúdo já em português, sem necessidade de tradução.

## Introdução — O Desafio de Entrevista

Imagine uma entrevista para programador em que o entrevistador propõe o seguinte desafio: criar um campo de busca no frontend onde o usuário digita algo e o sistema retorna os resultados mais relevantes.

A primeira intuição da maioria dos programadores é: receber o texto digitado no backend, montar uma query SQL básica usando o operador `LIKE`, e buscar todos os registros equivalentes. Essa intuição está **completamente errada** — o uso do `LIKE` tem baixíssima precisão em relevância e se torna um gargalo sério de performance no banco de dados.

A técnica correta chama-se **Full-Text Search**, disponível tanto em MySQL quanto em PostgreSQL.

## Parte 1 — Os Problemas do LIKE

### Ambiente de teste

Ferramenta usada: DBeaver, com duas conexões — uma MySQL e uma PostgreSQL. Cada banco tem uma tabela de usuários (10.000 registros) e uma tabela de produtos (10.000 registros), simulando um cenário de e-commerce.

### Problema 1 — Falta de relevância

Cenário: buscar usuários chamados "Ana" num sistema qualquer (ex.: bancário).

```sql
SELECT * FROM usuarios WHERE nome LIKE '%Ana%';
```

Resultado: além de "Ana Valentina" e "Ana Costa", a query também retorna "Vanessa", "Adriana" e "Luciana" — porque o `LIKE` com `%` (wildcard/coringa) nas duas pontas busca a sequência de caracteres "A-N-A" em qualquer posição da string, não a palavra "Ana" como unidade de linguagem. `LIKE` não entende idioma, vocabulário ou fronteiras de palavra — ele compara caracteres.

Tentativa de correção: remover o wildcard inicial (`'Ana%'`), forçando a busca a partir do começo da string. Funciona para "Ana", mas quebra para outros casos:

- Buscar `'Maria%'` também retorna "Mariana" (que começa com os mesmos caracteres).
- Buscar `'Júlia%'` também retorna "Juliana".

Ou seja, não existe uma correção estrutural de `LIKE` que resolva o problema de vocabulário — o operador é fundamentalmente baseado em substring matching, não em busca por palavras.

### Comparação com um motor de busca real

Teste no Mercado Livre: pesquisar por "anel" retorna uma lista de anéis relevantes, inclusive um produto anunciado como "Aliança casal e solitário aço dourado noivos e casamento" — que não contém a palavra "anel" no título, mas o motor de busca entendeu que "aliança" é semanticamente equivalente. A relevância se mantém mesmo na página 10 e na última página (42) dos resultados — só perde um pouco de precisão nas últimas páginas.

Repetindo a mesma busca por "anel" numa tabela de produtos local via `LIKE '%anel%'`: o resultado inclui "anel solitário prata 925", "anel masculino", mas também "panela de pressão" e "jogo de panelas antiaderentes" — porque a substring "anel" aparece dentro de "pAANELa" — não, na verdade dentro de "p-ANEL-a" (panela contém "anel" como substring). Zero relevância semântica.

Removendo o wildcard inicial (`'anel%'`) resolve esse caso específico, mas quebra em outros: buscar `'capa%'` retorna "capa de sofá" e "capa transparente" (correto), mas também "capacete" (incorreto).

Além disso, buscas compostas simplesmente não funcionam com `LIKE`: pesquisar `'%anel prata%'` não encontra nada, porque a ordem exata das palavras raramente bate com o texto armazenado. Mesmo pesquisas de uma palavra só falham se o termo não estiver posicionado exatamente onde o usuário esperava (ex.: buscar por "anel" não encontra a "aliança").

### Problema 2 — Performance

Rodando `EXPLAIN ANALYZE` na mesma query com `LIKE '%anel%'`:

- **Loop = 1** sobre **10.000 linhas** (o tamanho total da tabela).
- **Table scan** (no MySQL) / **Seq Scan / sequential scan** (no PostgreSQL): o banco examina registro por registro, sem atalho algum.
- **Custo interno** (MySQL): **1028** — número usado internamente pelo otimizador para estimar o custo da query.

Um table scan/seq scan não é performático porque escala linearmente (e pior) com o número de registros **e** com o número de usuários simultâneos: 1 usuário pesquisando = 10.000 comparações; 3 usuários simultâneos = 30.000; 10 usuários = 100.000; 100 usuários = 1.000.000. O crescimento é multiplicativo entre tamanho da tabela e número de pesquisas concorrentes — isso vira gargalo real de banco de dados à medida que a base de usuários ou de registros cresce.

## Parte 2 — Full-Text Search no MySQL

### Criando o índice

Full-Text Search exige um tipo de índice específico — não um índice comum:

```sql
CREATE FULLTEXT INDEX search_idx ON products (name, description);
```

O índice pode cobrir múltiplas colunas (ex.: nome **e** descrição do produto) — importante porque o termo pesquisado pode estar na descrição e não no nome.

### Consultando com MATCH ... AGAINST

```sql
SELECT * FROM products
WHERE MATCH(name, description) AGAINST('fone bluetooth');
```

- `MATCH` recebe as colunas que compõem o índice full-text.
- `AGAINST` recebe o termo pesquisado pelo usuário.

Resultado: os fones bluetooth aparecem primeiro; produtos com apenas "fone" (ex.: "AirPods Pro 2ª geração", que tem "fone" na descrição mas não "bluetooth") ou apenas "bluetooth" (ex.: "caixa de som bluetooth portátil") aparecem depois, com relevância decrescente. O MySQL monta um **ranqueamento interno de relevância** — os IDs retornados aparecem fora de ordem sequencial porque o critério de ordenação é relevância textual, não a ordem física da tabela.

Trocando a busca para "fone vermelho": o motor prioriza corretamente os fones vermelhos antes de fones de outras cores, mesmo que todos contenham a palavra "fone". O mesmo teste com `LIKE` simplesmente não encontra nada para buscas compostas como essa.

### Por baixo dos panos — tokenização e índice invertido

Ao criar o índice full-text, o MySQL:

1. **Tokeniza** o conteúdo das colunas: quebra o texto em palavras individuais, descarta preposições e palavras de baixo valor semântico (stop words), e mantém apenas os termos relevantes.
2. Constrói um **índice invertido**: uma estrutura que mapeia cada palavra (token) para a lista de registros (IDs) onde ela aparece. Exemplo simplificado: a palavra "anel" aponta para os registros 1 e 2; a palavra "capacete" aponta para os registros 8, 9 e 10.

Quando o usuário pesquisa por "panela de pressão", o motor:
- Descarta a preposição "de".
- Busca a interseção dos registros que contêm "panela" **e** "pressão" no índice invertido.
- Retorna essa interseção como os resultados mais relevantes.

Esse é o motivo estrutural pelo qual a busca funciona com palavras fora de ordem, distantes entre si no texto, e por que ela consegue ranquear por relevância: o motor nunca mais olha para a tabela original durante a busca — ele consulta apenas o índice invertido.

### Performance do Full-Text Search no MySQL

Rodando `EXPLAIN ANALYZE` na query com `MATCH ... AGAINST`:

- **Custo interno**: **0.35** (contra 1028 do `LIKE`) — diferença de ordens de grandeza.
- **Linhas examinadas**: **419** (contra 10.000 do `LIKE`) — o motor consulta apenas os registros já indexados como relevantes, não a tabela inteira.

Full-Text Search resolve, simultaneamente, o problema de relevância **e** o problema de performance.

## Parte 3 — Full-Text Search no PostgreSQL

PostgreSQL oferece uma implementação mais avançada de Full-Text Search, com suporte real a idioma, vocabulário, plural/singular e sinônimos configuráveis.

### Baseline — o mesmo problema com LIKE

Rodando a mesma busca `WHERE name LIKE '%anel%'` no Postgres: mesmo resultado embaralhado e sem relevância. `EXPLAIN ANALYZE` mostra um **Seq Scan** (equivalente ao table scan do MySQL) e um tempo de execução de **~4,9 ms** — rápido apenas porque é uma máquina local; não é representativo de um ambiente de produção real.

### Consultando sem índice (baseline lento)

```sql
SELECT * FROM products
WHERE to_tsvector('portuguese', coalesce(name, '') || ' ' || coalesce(description, '') || ' ')
      @@ to_tsquery('portuguese', 'capa');
```

- `to_tsvector(idioma, texto)`: converte o texto em um **tsvector** — a representação interna baseada em lexemas usada para busca full-text.
- `coalesce(coluna, '')`: concatena nome e descrição (protegendo contra `NULL`) para formar o texto pesquisável.
- `@@`: operador de correspondência (match) entre um `tsvector` e uma `tsquery`.
- `to_tsquery(idioma, termo)`: converte o termo pesquisado numa `tsquery`.

Resultado da busca por "capa": retorna "capa transparente", "capa para sofá", "capa anti-chuva verde" e também **"caderno universitário capa dura"** — porque a palavra "capa" está presente na descrição do caderno, e o motor entende que isso é relevante para a busca.

O Postgres também entende variações morfológicas automaticamente:
- Buscar "capas" (plural) retorna os mesmos resultados de "capa".
- Buscar "cadernos" (plural) encontra "caderno" (singular) — mesmo sem a palavra "cadernos" existir literalmente no texto.

Buscas compostas usam `plainto_tsquery` (ou `&` explícito dentro de `to_tsquery`) para indicar onde cada palavra começa e termina:

```sql
SELECT * FROM products
WHERE to_tsvector('portuguese', coalesce(name,'') || ' ' || coalesce(description,'') || ' ')
      @@ to_tsquery('portuguese', 'capa & dura');
```

Sem essa sintaxe, passar múltiplas palavras direto para `to_tsquery` retorna erro — a função precisa saber a fronteira entre os termos.

Rodando `EXPLAIN ANALYZE` nessa versão sem índice: tempo de **~139 ms** — pior do que o próprio `LIKE` (4,9 ms), porque o Postgres está montando o `tsvector` (tokenização + lexemas) **em tempo de execução**, a cada chamada, em vez de consultar uma estrutura pré-computada.

### Criando o índice GIN

```sql
CREATE INDEX search_idx ON products
USING GIN (
  to_tsvector('portuguese', coalesce(name, '') || ' ' || coalesce(description, '') || ' ')
);
```

- `GIN` (Generalized Inverted Index): o tipo de índice usado pelo Postgres para estruturar o índice invertido por baixo dos panos.

Com o índice criado, a mesma consulta cai de **139 ms** para **~0,80 ms** (buscas compostas) e até **~0,3 ms** (buscas de um único termo) — ordens de grandeza mais rápido que o `LIKE`. `EXPLAIN ANALYZE` deixa de mostrar Seq Scan.

Analogia usada na fonte: procurar uma palavra num livro sem índice = ler página por página até o fim. Com índice invertido = ir direto ao índice remissivo no final do livro, que já diz em quais páginas a palavra aparece.

### Lexemas e sinônimos morfológicos

```sql
SELECT to_tsvector('portuguese', 'programador programando programação programadores');
```

Resultado: todas as variações são reduzidas a um único **lexema** — a forma raiz que representa o mesmo contexto semântico (aqui, "program"). É por isso que buscar por qualquer uma das variantes (singular, plural, verbo, substantivo) retorna os mesmos resultados.

Demonstração com "prata" vs. "prateado": buscando `'anel & prata'` e depois `'anel & prateado'`, o Postgres retorna o **mesmo resultado** (o anel de prata) nos dois casos — porque "prateado" e "prata" pertencem ao mesmo lexema interno. Inspecionando `to_tsvector('portuguese', name) FROM products`, o token gerado para o anel de prata mostra um lexema abreviado (algo como `prat`) que cobre ambas as formas.

### Tabela comparativa — LIKE vs. MySQL Full-Text vs. PostgreSQL Full-Text

| Recurso | LIKE | MySQL Full-Text | PostgreSQL Full-Text |
|---|---|---|---|
| Evita full table scan | Não | Sim (índice invertido) | Sim (índice invertido / GIN) |
| Escala para milhões de registros | Não | Sim | Sim |
| Busca por palavra (não substring) | Não | Sim | Sim |
| Ranking de relevância | Não | Sim | Sim |
| Ignora stop words (preposições) | Não | Sim | Sim |
| Busca por múltiplas palavras | Limitada/frágil | Sim | Sim |
| Suporte a idioma/vocabulário | Não | Básico | Avançado |
| Stemming (redução a lexema/raiz) | Não | Limitado | Avançado |
| Entende plural/singular automaticamente | Não | Limitado | Sim |
| Tesauros/sinônimos configuráveis | Não | Não | Sim |
| Peso configurável por campo | Não | Não | Sim (`setweight`/`ts_rank`, mencionado na fonte apenas como recurso existente) |
| Tokenização configurável | Não | Não | Sim |

**Tesauro** = sinônimo, no jargão do Postgres: é possível configurar o dicionário de busca para que termos como "carro", "automóvel" e "veículo" sejam tratados como equivalentes.

## Encerramento

Full-Text Search é apresentado como uma técnica simples de implementar (poucas linhas de SQL) mas que resolve, ao mesmo tempo, o problema de relevância semântica e o problema estrutural de performance que o `LIKE` cria em qualquer sistema de busca real. A fonte encerra com uma chamada para o produto "Mapa do Arquiteto" (mentoria/roadmap de carreira do autor, cobrindo do júnior ao arquiteto de software).
