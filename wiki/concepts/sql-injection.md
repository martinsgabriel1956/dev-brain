---
type: concept
title: "SQL Injection"
aliases: ["sql injection", "sqli", "injeção sql", "bobby tables"]
date_created: 2026-06-10
date_updated: 2026-06-11
source_count: 2
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
Validar tipo, comprimento e formato antes de usar — não como substituto para parametrização, mas como camada adicional.

**4. Princípio do menor privilégio no banco**
Se o usuário da aplicação só tem SELECT, mesmo uma injeção bem-sucedida não consegue DROP ou DELETE. Ver [[principio-do-menor-privilegio]].

## SQL Injection é um Caso de um Princípio Maior

Todo input do usuário — nome, e-mail, senha, parâmetros de URL, cabeçalhos HTTP, arquivos enviados — pode conter código malicioso. A regra geral é: **nunca confie em dados externos; sempre sanitize e valide na fronteira do sistema**.

O mesmo princípio se aplica a: XSS (injeção HTML/JS), Command Injection (shell), SSTI (template engines), XXE (XML).

## Papel Histórico no Armazenamento de Senhas

A popularização do SQL Injection nos anos 90 foi o gatilho que expôs o padrão de armazenar senhas em **plaintext**. Quando um atacante ganhava acesso ao banco via SQLi, recebia as senhas literalmente como o usuário havia digitado — e as reutilizava em outros serviços. Esse ciclo levou à adoção de [[concepts/password-hashing]] como resposta. O caso [[entities/rockyou]] (2009) mostrou que décadas depois empresas ainda não tinham aprendido a lição.

## Relação com Outros Conceitos

- [[attack-surface]] — inputs são a superfície de ataque mais explorada
- [[principio-do-menor-privilegio]] — reduz o impacto de uma injeção bem-sucedida
- [[xss]] — injeção de código em contexto diferente (HTML/JS em vez de SQL)
- [[concepts/password-hashing]] — resposta ao problema exposto pelos vazamentos via SQLi

## Key Sources

- [[sources/cinco-praticas-seguranca-pragmatic-programmer]] — Bobby Tables como exemplo central de sanitização de input
- [[sources/seguranca-armazenamento-senhas-banco-de-dados]] — contexto histórico: SQLi nos anos 90 como vetor que expôs o plaintext
