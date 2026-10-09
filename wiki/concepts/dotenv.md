---
type: concept
title: ".env (dotenv)"
aliases: [".env", "dotenv", "arquivo env"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_count: 1
tags: [security, dotenv, configuracao, secrets-management]
skill: tech-mentor-security
status: draft
---

# .env (dotenv)

Arquivo de texto dedicado (`.env`, nome começa no ponto) com pares `NOME_EM_MAIUSCULAS=valor` e comentários com `#`, que guarda as [[wiki/concepts/variavel-de-ambiente|variáveis de ambiente]] de um [[wiki/concepts/ambiente-de-execucao|ambiente]]. Mesma aplicação, um `.env` por ambiente. Vale em dev/staging e projetos pequenos; em produção crítica, prefira [[wiki/concepts/secret-manager]].

## Regras

- Nunca versionar nem servir publicamente (testar `/.env` na URL); ver [[wiki/concepts/secrets-management]] e [[wiki/concepts/secret-scanning]].
- Apagar do código não apaga do histórico do git.
- Sem duplicar chaves (vale a última) e sem coexistir com o mesmo valor hardcoded.
- Só configuração de servidor — ver [[wiki/concepts/configuracao-vs-regra-de-negocio]].
- Apagar o arquivo após subir o serviço não funciona se a runtime o lê a cada requisição.

## Key Sources

- [[wiki/sources/dotenv-arquivo-env-boas-praticas-secret-manager]]
