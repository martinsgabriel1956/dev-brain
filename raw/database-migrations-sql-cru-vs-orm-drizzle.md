# Database Migrations — SQL Cru vs. ORM (Drizzle)

Transcrição de vídeo (autor não identificado no material fornecido). Patrocínio (Abacus AI) omitido por ser publicidade sem relevância técnica.

---

## O ponto central: por que não migrar na mão

Existem várias maneiras de fazer migrações de banco de dados. A maneira errada — no risco de ser um pouco polêmico — é dar SSH na cloud e executar comandos manualmente: criar tabelas, criar colunas, mudar tipo de coluna, adicionar foreign key etc. Isso é considerado simplesmente errado, e não deveria ser feito em hipótese alguma.

O motivo: comandos executados na mão, vivendo só na máquina de quem administra o banco (um DBA, por exemplo), não são revisáveis, auditáveis, reproduzíveis nem automatizáveis. Se não é nada disso, não é robusto nem profissional o suficiente.

Importante: isso não significa nunca criar um arquivo de migration manual. A recomendação é que arquivos e scripts de migração estejam sujeitos aos mesmos processos do código — pull requests, code review, e dentro de um controle de versionamento (git). Tratar migrations com a mesma seriedade que se trata código.

## O que é uma migração

Exemplo: uma tabela `users` já em produção, com `id`, `nome`, `email` e 300 usuários. Ao perceber a necessidade de um campo `data_nascimento`, é preciso migrar o schema — adicionar essa coluna.

Isso pode ser feito manualmente (`ALTER TABLE users ADD COLUMN nascimento ...`), mas o problema é que esse comando teria que ser executado à mão em cada ambiente (local, stage, produção), sem reprodutibilidade. Se for necessário reverter e reaplicar depois, perde-se o registro do que foi executado e como.

Por isso o padrão de migração pensa em par: **migrate up** e **migrate down**. Se a migração de adicionar `data_nascimento` não der certo, o migrate down reverte (remove a coluna). Cada migração recebe um número/versão sequencial. Sem esse controle, cada pessoa roda o que quiser no banco e não há versão nem histórico.

Fazendo isso de forma reprodutível: a migration 1 tem seu up/down, a migration 2 tem seu up/down, e assim por diante. O próprio banco armazena internamente em que versão está (ex.: versão 003), permitindo migrar para cima ou para baixo de forma determinística.

## Demonstração 1 — Migrations cruas com Postgres

Setup: projeto com `docker-compose` que sobe um Postgres (`postgres:16-alpine`, user/password `demo`) local via `docker compose up`.

Estrutura: arquivos de migração numerados (`migration 1`, `migration 2`, `migration 3`), cada um com um `up` e um `down`:

- **Migration 1**: cria a tabela `users` com `id` e `email`; insere dois usuários. `down`: `DROP TABLE users`.
- **Migration 2**: adiciona coluna `username`. `down`: remove (drop) a coluna `username`.
- **Migration 3**: popula `username` dos usuários existentes e adiciona constraint de unicidade. `down`: dropa a constraint de unicidade e nulifica/remove os usernames criados.

Sempre a lógica de down é reverter exatamente o que o up fez.

Normalmente a empresa mantém um script `migrate` cuja função é identificar em qual versão o Postgres está e aplicar todas as migrations pendentes até a versão alvo. É possível ignorar esse script e migrar manualmente uma a uma sabendo a versão atual, mas não há motivo para isso — o objetivo é reprodutibilidade. Esse tipo de script é simples o bastante para ser gerado por IA, e depois testado localmente (up, down, diferentes cenários) para validar o comportamento.

Demonstração prática:
1. Rodar um script de query (`SELECT email FROM users ORDER BY id`) antes de migrar → erro, pois a tabela `users` não existe.
2. Rodar `migrate` → aplica a migration 001, depois 002, depois 003.
3. Rodar a query novamente → retorna `id`, `email`, `username` populados pelas três migrations.
4. Rodar `rollback` três vezes → desfaz as três migrations, uma por vez. A query volta a falhar (tabela não existe).
5. Rodar `migrate` (aplica as três) seguido de `rollback` uma vez e depois `migrate` novamente → o script detecta a versão atual e aplica apenas a migration pendente (pula as que já estavam aplicadas), demonstrando que ele rastreia estado/versão corretamente.

Modelo mental: migrations são operações sequenciais (1, 2, 3, 4, 5...) cuja aplicação em sequência resulta num estado final do banco — nesse exemplo, uma tabela `users` com `id`, `name`, `email` etc.

## Demonstração 2 — ORM (Drizzle)

A maioria das empresas não trabalha com migrations cruas em SQL — trabalha com uma ORM. Uma ORM cria uma camada de abstração sobre o banco, permitindo lidar com o schema em código (TypeScript, Python etc.) em vez de pensar diretamente em SQL.

Diferença chave de fluxo: com SQL cru, escreve-se a migração diretamente. Com ORM, o fluxo é invertido — descreve-se o **estado final** desejado do schema, e a ORM deriva os arquivos de migration a partir da diferença entre o estado atual e o estado descrito. Na maioria dos casos não é necessário escrever migrations manualmente; ocasionalmente é preciso ajustar algo manualmente quando o gerado não sai como esperado.

Projeto de exemplo usa **Drizzle** (`drizzle-orm` + `drizzle-kit`). O schema é declarado em TypeScript: uma `pgTable` chamada `user`, com `id` (serial, primary key), `email` (texto, not null, unique) e `username` (texto, not null, unique).

Fluxo:
1. `npm run generate` (que roda `drizzle-kit generate`) lê o schema declarado e, comparando com o histórico interno (journal + snapshots), gera os arquivos de migration necessários. Sem nenhuma migration prévia, gera a migration `0`, que cria a tabela `users` com as constraints declaradas.
2. `npm run migrate` (via `drizzle-kit migrate` ou script próprio) aplica a migration no banco.
3. Queries são feitas via API do Drizzle (varia de ORM para ORM).
4. Ao alterar o schema — por exemplo adicionar um campo `decimal` chamado `novo` — rodar `generate` novamente cria uma nova migration que adiciona esse campo. Removendo o campo do schema e rodando `generate` de novo, é gerada uma migration que dropa a coluna/constraint.

O valor central da ORM: basta declarar o estado final desejado do schema; a ferramenta deriva a migration necessária a partir dos arquivos internos (journals, snapshots, migrations) para levar o banco daquele estado atual até o estado descrito.

## Cuidados e limites

Mesmo com ORM, migrations continuam podendo dar problema — um migrate up ou down pode falhar, ou uma alteração pode travar uma tabela grande. Exemplo pessoal do autor: alterar a tabela `users` (com ~100.000 usuários) para adicionar um campo derivado de outro (ou criar uma chave) resultou em um `lock` que travou a tabela por ~5 minutos em produção.

O vídeo não é uma aula extensa sobre migrations — é uma introdução ao básico. Em sistemas de produção reais, é essencial entender bem sobre banco de dados para evitar esse tipo de erro: por exemplo, adicionar uma constraint de unicidade em uma tabela com muitos usuários pode causar problemas de performance/lock. É recomendado testar em staging com dados similares aos de produção — o fato de a ORM ter gerado a migration não garante que ela está correta ou que não vai quebrar nada em escala.

Conclusão: leve migrations a sério. A recomendação final é que fiquem versionadas na codebase, sujeitas a pull request e code review, e executadas por scripts reproduzíveis que também vivem na codebase. Isso não elimina todos os problemas, mas facilita identificar a origem e a solução quando algo dá errado — ao contrário de rodar scripts direto no banco de produção.
