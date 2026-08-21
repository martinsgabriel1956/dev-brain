---
type: concept
title: "SQL Injection"
aliases: ["sql injection", "sqli", "injeção sql", "bobby tables"]
date_created: 2026-06-10
date_updated: 2026-08-19
source_count: 7
tags: [security, sql-injection, owasp, input-sanitization, appsec, attack-surface]
skill: tech-mentor-security
status: stable
---

# SQL Injection

Vulnerabilidade que permite a um atacante injetar código SQL arbitrário através de inputs do usuário, executado diretamente pelo banco de dados. É o #1 histórico do OWASP Top 10 e ilustra o princípio de que **todo input do usuário é um vetor de ataque**.

## O Exemplo Clássico (Bobby Tables)

```sql
-- Input do usuário: Robert'; DROP TABLE students;--
-- Query construída ingenuamente:
INSERT INTO students (name) VALUES ('Robert'; DROP TABLE students;--)

-- O banco executa:
INSERT INTO students (name) VALUES ('Robert');
DROP TABLE students;
-- O resto é comentário
```

O campo de nome destruiu a tabela inteira. A tira do xkcd popularizou esse exemplo com o personagem "Little Bobby Tables".

## Por Que Acontece

O código concatena input diretamente na query SQL sem sanitizar ou separar dados de código:

```typescript
// ❌ Vulnerável
const query = `SELECT * FROM users WHERE name = '${userInput}'`

// ✅ Parameterizado — input nunca é interpretado como SQL
const query = 'SELECT * FROM users WHERE name = $1'
db.query(query, [userInput])
```

## Como Prevenir

**1. Queries parametrizadas / prepared statements**
O banco recebe a query e os dados separadamente — o input nunca é interpretado como código SQL.

**2. ORM com parametrização automática**
Prisma, TypeORM, Sequelize parametrizam por padrão. Ainda assim, evite raw queries com interpolação.

**3. Sanitização e validação de input**
Validar tipo, comprimento e formato antes de usar — não como substituto para parametrização, mas como camada adicional. Exemplo prático em Node/Express: middleware **Celebrate** com schemas **Joi** valida o tipo do parâmetro (ex.: `Joi.number()` numa rota `/users/:id`) e rejeita a requisição *antes* de qualquer query rodar — ver [[wiki/sources/injecao-sql-aula-modulo-seguranca]].

**4. Princípio do menor privilégio no banco**
Se o usuário da aplicação só tem SELECT, mesmo uma injeção bem-sucedida não consegue DROP ou DELETE. Ver [[principio-do-menor-privilegio]].

## SQL Injection é um Caso de um Princípio Maior

Todo input do usuário — nome, e-mail, senha, parâmetros de URL, cabeçalhos HTTP, arquivos enviados — pode conter código malicioso. A regra geral é: **nunca confie em dados externos; sempre sanitize e valide na fronteira do sistema**.

O mesmo princípio se aplica a: XSS (injeção HTML/JS), Command Injection (shell), SSTI (template engines), XXE (XML).

## Papel Histórico no Armazenamento de Senhas

A popularização do SQL Injection nos anos 90 foi o gatilho que expôs o padrão de armazenar senhas em **plaintext**. Quando um atacante ganhava acesso ao banco via SQLi, recebia as senhas literalmente como o usuário havia digitado — e as reutilizava em outros serviços. Esse ciclo levou à adoção de [[concepts/password-hashing]] como resposta. O caso [[entities/rockyou]] (2009) mostrou que décadas depois empresas ainda não tinham aprendido a lição.

## "Eliminar SQL Elimina SQL Injection"? Não Exatamente

Uma thread analisada em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] propõe eliminar SQL dos sistemas para eliminar SQL Injection ("if there is no SQL, você não tem engine de SQL"). Isso é uma simplificação: a defesa real é **parametrização de queries**, não a ausência de uma linguagem SQL. Uma API REST sobre Postgres (como Supabase) ou um ORM mal usado com raw query interpolada continuam vulneráveis — o vetor de ataque é a concatenação de input não confiável em qualquer camada que gere SQL, não a existência do SQL em si.

**Nota de nomenclatura**: não confundir "Bobby Tables" (o meme do xkcd, citado acima) com "Bob Tables" — possível título de um blog post atribuído a Uncle Bob sobre eliminar SQL de sistemas. São referências distintas que soam parecidas.

## Relação com Outros Conceitos

- [[attack-surface]] — inputs são a superfície de ataque mais explorada
- [[principio-do-menor-privilegio]] — reduz o impacto de uma injeção bem-sucedida
- [[xss]] — injeção de código em contexto diferente (HTML/JS em vez de SQL)
- [[concepts/password-hashing]] — resposta ao problema exposto pelos vazamentos via SQLi
- [[wiki/concepts/orm]] — parametriza por padrão, mas raw queries interpoladas continuam vulneráveis

## Teste de Injeção como Rotina de Autopentest

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] agrupa SQL Injection e XSS sob a mesma pergunta de teste — "meu sistema está confiando demais em mim?" — e descreve a prática mínima de tentar inserir queries e scripts maliciosos diretamente dentro de requisições reais contra o próprio sistema, como parte de um checklist de segurança conduzido com apoio (não substituição) de um agente de IA.

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — Bobby Tables como exemplo central de sanitização de input
- [[sources/seguranca-armazenamento-senhas-banco-de-dados]] — contexto histórico: SQLi nos anos 90 como vetor que expôs o plaintext
- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — contradiz a simplificação "eliminar SQL elimina SQL attacks"
- [[wiki/sources/injecao-sql-aula-modulo-seguranca]] — demonstração ao vivo (Express + `pg`) do ataque via query string e via parâmetro de rota, correção via placeholders `$1`/`$2`, e camada extra de validação de schema com Celebrate/Joi
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — teste manual de injeção como parte de checklist de autopentest
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — SQLi no campo de e-mail do login (`' or 1=1`) como vetor clássico contra formulários de autenticação
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — citado como exemplo canônico de padrão inseguro presente nos dados de treinamento (snippets do Stack Overflow com concatenação de string em query) que um LLM pode reproduzir com a mesma fluência de um padrão parametrizado e seguro, sem o "alerta interno" que um dev experiente tem ao ver esse padrão
- [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — citado como par de XSS na mesma frente de treino prático de exploração ([[wiki/concepts/dvwa]]/bug bounty), embora a fonte foque em XSS
