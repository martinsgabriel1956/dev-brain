---
type: concept
title: "LOAD_FILE / INTO OUTFILE — Leitura e Escrita de Arquivos via SQL Injection"
aliases: ["load_file mysql", "into outfile", "file read sql injection", "sqli para rce"]
date_created: 2026-09-30
date_updated: 2026-09-30
source_count: 1
tags: [sql-injection, mysql, file-read, rce, appsec, pentest]
skill: tech-mentor-security
status: draft
---

# LOAD_FILE / INTO OUTFILE — Leitura e Escrita de Arquivos via SQL Injection

[[wiki/concepts/sql-injection]] não se limita a manipular linhas de tabela — em bancos como o MySQL, uma injeção bem-sucedida pode ser usada para acessar o **sistema de arquivos do servidor** através de funções SQL nativas.

## Leitura: `LOAD_FILE`

A função `LOAD_FILE()` do MySQL lê um arquivo do servidor e retorna seu conteúdo como resultado de query — se o usuário do banco tiver permissão e a configuração permitir. Um exemplo clássico de alvo é `/etc/passwd`, o arquivo Linux que lista os usuários do sistema.

**Proteção nativa:** a opção `secure_file_priv` do MySQL restringe de onde arquivos podem ser lidos/escritos. Se estiver desativada ou mal configurada, um atacante consegue ler arquivos de qualquer parte do sistema a que o processo do banco tenha acesso.

**Impacto:** arquivos de configuração frequentemente contêm senhas de outros bancos de dados, chaves de API e outras credenciais; em casos mais graves, chaves privadas SSH podem dar acesso direto a outro sistema.

## Automação com SQLMap

```bash
sqlmap -u "https://alvo.com/pagina?id=1" -p id --file-read=/etc/passwd
```

`--file-read` instrui o [[wiki/concepts/sqlmap]] a tentar ler o arquivo via injeção, usando `LOAD_FILE` ou função equivalente do SGBD detectado, salvando o conteúdo localmente se bem-sucedido.

## Escrita: `INTO OUTFILE`

Se a leitura já é crítica, a **escrita** é o passo seguinte e mais perigoso: a instrução `INTO OUTFILE` permite gravar o resultado de uma query como um arquivo no servidor, também condicionada às mesmas permissões (`secure_file_priv`, permissões do usuário do banco no sistema de arquivos).

**Caminho para RCE:** se o usuário do banco tem permissão de escrita num diretório servido pela aplicação web, é possível gravar um arquivo executável (ex.: um webshell) e, a partir daí, conseguir execução remota de comandos (RCE) no servidor — o passo mais crítico possível de uma cadeia de exploração de SQLi.

> Nota de verificação: [[wiki/sources/sql-injection-sqlmap-luiz-viana]] descreve esse caminho de RCE via `INTO OUTFILE` mas não o demonstra na prática (a demonstração ao vivo do vídeo cobre apenas `--file-read`). Tratar a etapa de escrita/RCE como claim plausível, não verificada nesta fonte.

## Relação com Outros Conceitos

- [[wiki/concepts/sql-injection]] — vulnerabilidade de base que habilita esse acesso ao sistema de arquivos
- [[wiki/concepts/sqlmap]] — automatiza a leitura via `--file-read`
- [[wiki/concepts/principio-do-menor-privilegio]] — a defesa mais direta: um usuário de banco sem permissão de arquivo no SO (ou com `secure_file_priv` restritivo) não consegue `LOAD_FILE`/`INTO OUTFILE`, mesmo com SQLi bem-sucedido

## Key Sources

- [[wiki/sources/sql-injection-sqlmap-luiz-viana]] — demonstração de `--file-read=/etc/passwd` via SQLMap (Lesson 7 do laboratório) e explicação do risco de escrita via `INTO OUTFILE` como caminho para RCE
