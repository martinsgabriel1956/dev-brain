---
type: source
title: "Injeção de SQL — Aula do Módulo de Segurança"
aliases: ["sql injection aula", "sr jackson sql", "celebrate joi validation", "aula seguranca sql injection"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/injecao-sql-aula-modulo-seguranca.md
source_url: ""
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [sql-injection, appsec, owasp, input-validation, celebrate, joi, express, node-postgres, prepared-statement]
skill: tech-mentor-security
status: stable
---

## TL;DR

Aula prática (Express + `pg`, sem ORM) demonstrando SQL Injection ao vivo: concatenar `name`/`email` direto na query permite bypass via `' OR '1'='1'` (query string) e via `1 OR 1=1` (parâmetro de rota), retornando todos os usuários em vez do usuário filtrado. Correção: placeholders parametrizados do `pg` (`$1`, `$2`) — o valor nunca é interpretado como SQL. Camada adicional: middleware **Celebrate** (com schemas **Joi**) valida tipo/formato do input *antes* da query rodar, rejeitando o ataque na borda.

## Key Claims

**Claim:** Concatenar input do usuário direto numa query SQL permite que uma condição sempre-verdadeira (`OR '1'='1'`) bypasse o filtro pretendido e retorne todos os registros da tabela.
**Evidence:** Demonstração ao vivo: endpoint `GET` com `name`/`email` via query string, montando `SELECT * FROM users WHERE name = '${name}' AND email = '${email}'`. Passar `' OR '1'='1'` em ambos os campos faz a query virar `WHERE name = '' OR '1'='1' AND email = '' OR '1'='1'` — sempre verdadeira — retornando os 4 usuários do banco de teste em vez de 0 ou 1.
**Confidence:** alta — reproduzido ao vivo no vídeo com `console.log` da query final montada.

**Claim:** O mesmo ataque funciona através de parâmetro de rota (`/users/:id`), não só via query string — o vetor é qualquer input não tratado, independente de onde ele entra na requisição.
**Evidence:** Segundo endpoint no vídeo usa `id` como parâmetro de rota; passar `1 OR 1=1` no lugar de um ID numérico normal retorna todos os usuários pelo mesmo mecanismo de condição sempre-verdadeira.
**Confidence:** alta

**Claim:** Passar valores como segundo parâmetro (array) do `pg`, com placeholders `$1`/`$2` na string da query, neutraliza o ataque — o banco trata o valor como dado, nunca como código SQL.
**Evidence:** Reescrita do primeiro endpoint usando `db.query('SELECT * FROM users WHERE name = $1 AND email = $2', [name, email])`. Repetindo o ataque (`' OR '1'='1'`), a aplicação retorna vazio (nenhum usuário com esse nome literal); passando dados reais, volta a funcionar normalmente.
**Confidence:** alta — mesma técnica documentada em [[wiki/concepts/sql-injection]] e confirmada pela referência da skill (`appsec-owasp.md`: `db.query('SELECT * FROM users WHERE email = $1', [email])`).

**Claim:** Celebrate (middleware) + Joi (schema) formam uma camada de validação de schema que roda antes da query, rejeitando input malformado (ex.: string onde se espera número) com erro, sem nunca chegar ao banco.
**Evidence:** Middleware `celebrate({ [Segments.PARAMS]: Joi.object({ id: Joi.number() }) })` aplicado à rota do parâmetro `id`. Repassar o ataque (`1 OR 1=1`) agora falha na validação (erro de schema) antes de tocar o banco; passar apenas o número volta a funcionar.
**Confidence:** alta — reproduzido ao vivo.

**Claim:** A defesa contra SQL Injection é agnóstica de linguagem/stack — o princípio (nunca concatenar, sempre parametrizar) se aplica a Python, Java (`PreparedStatement`) e a qualquer ORM que exponha raw query.
**Evidence:** Fala explícita do instrutor: "isso aqui funciona com qualquer tecnologia [...] funciona no Python, tem o [equivalente] no Java [...] mesmo usando ORM, numa query mais complexa você pode precisar escrever SQL na mão, e aí tem que tomar cuidado para não cair na mesma forma [de concatenar]".
**Confidence:** média — afirmação de princípio geral, sem demonstração no próprio vídeo fora do stack Node/Express/pg.

## Entities & Concepts Touched

- [[wiki/concepts/sql-injection]]
- [[wiki/concepts/validacao-de-entrada]]

Ver também (fonte irmã sobre o mesmo tema, camada de validação/sanitização): [[wiki/sources/input-validation-output-encoding]].

## Open Questions

- O vídeo não aprofunda o princípio do menor privilégio no usuário de banco (só menciona de passagem que, sem restrição de permissão, um `DROP TABLE` via injeção seria possível) — já coberto em [[wiki/concepts/sql-injection]] via [[principio-do-menor-privilegio]].
- Não fica claro no áudio se "Celebrate" segue mantido/ativamente atualizado como biblioteca — vale confirmar estado do projeto antes de recomendar em produção nova.
