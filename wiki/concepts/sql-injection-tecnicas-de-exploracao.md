---
type: concept
title: "Técnicas de Exploração de SQL Injection (Blind, Error-based, UNION-based)"
aliases: ["blind sql injection", "boolean-based blind", "time-based blind", "error-based sql injection", "union-based sql injection"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [sql-injection, blind-injection, union-based, error-based, boolean-based, time-based, appsec, pentest]
skill: tech-mentor-security
status: draft
---

# Técnicas de Exploração de SQL Injection

Uma vez confirmado que um parâmetro é vulnerável a [[wiki/concepts/sql-injection]] (por exemplo, ao quebrar a query com uma aspa simples), a técnica usada para *extrair dados* depende do que a aplicação revela ao atacante. Ferramentas como [[wiki/concepts/sqlmap]] testam essas técnicas e escolhem automaticamente a mais adequada com base no comportamento observado.

## Error-based

O banco é forçado a emitir uma mensagem de erro que **contém informação útil** — nome de tabelas, dados da query, tipo do SGBD. Se a aplicação exibe erros de banco de dados na tela (como uma mensagem de sintaxe SQL crua), essa é normalmente a técnica mais rápida e direta, já que o próprio erro vaza dados.

## UNION-based

Quando o resultado da query original aparece na tela, é possível anexar um `SELECT` customizado ao `SELECT` original usando `UNION`, combinando as duas consultas em uma única resposta. Isso permite extrair diretamente as informações desejadas (nomes de tabela, colunas, dados), sem depender de inferência — é a técnica mais direta quando a página exibe múltiplos campos de um registro.

## Blind (boolean-based e time-based)

Chamada de "cega" porque **a query é executada, mas a resposta não é visível** diretamente — nem como dado na tela, nem como mensagem de erro. A extração acontece por inferência, um bit de informação por vez:

- **Boolean-based blind:** o atacante envia condições que retornam verdadeiro ou falso (ex.: "a primeira letra do nome da tabela é 'a'?") e observa se o comportamento da página muda (conteúdo diferente, elemento presente/ausente) entre os dois casos. Repetindo esse processo, os dados são reconstruídos caractere a caractere.
- **Time-based blind:** quando nem o conteúdo da página varia de forma observável, a confirmação vem pelo **tempo de resposta**. O atacante envia uma condição acoplada a um comando de sleep condicional — se a condição for verdadeira, o banco demora artificialmente alguns segundos a mais para responder. A ausência de atraso indica falso; o atraso indica verdadeiro. Mesma lógica bit-a-bit do boolean-based, mas usando latência como canal de sinal em vez de conteúdo da resposta.

## Outras (stacked queries, inline queries)

Técnicas mais específicas — como empilhar múltiplas instruções SQL numa única query (stacked queries) — também são testadas por ferramentas como o SQLMap, mas são menos universais que as quatro acima (dependem de o driver/SGBD permitir múltiplos statements por chamada).

## Como o SQLMap escolhe a técnica

[[wiki/sources/sql-injection-sqlmap-luiz-viana]] descreve a lógica adaptativa: se há erro visível → error-based; se o resultado aparece na tela → UNION-based; se nada aparece → boolean-based ou time-based blind. O SQLMap testa e prioriza conforme o que a aplicação efetivamente revela, em vez de aplicar sempre a mesma técnica.

## Relação com Outros Conceitos

- [[wiki/concepts/sql-injection]] — vulnerabilidade de base; esta página cobre apenas a fase de *exploração/extração* após a injeção já confirmada
- [[wiki/concepts/sqlmap]] — ferramenta que automatiza a escolha e execução dessas técnicas
- [[wiki/concepts/load-file-into-outfile-mysql]] — uma vez explorada a injeção (por qualquer uma dessas técnicas), pode ser usada para ler/escrever arquivos no servidor, não só extrair linhas de tabela

## Key Sources

- [[wiki/sources/sql-injection-sqlmap-luiz-viana]] — demonstração de boolean-based blind no Lesson 1 do laboratório, com explicação de error-based, UNION-based e time-based como alternativas escolhidas conforme o comportamento da aplicação
