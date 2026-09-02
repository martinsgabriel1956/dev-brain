---
type: concept
title: "Variáveis de Ambiente (.env, export)"
aliases: ["variáveis de ambiente", "env", ".env", "export", "environment variables", "zshrc", "bashrc"]
date_created: 2026-08-11
date_updated: 2026-09-02
source_count: 2
tags: [linux, shell, variaveis-de-ambiente, env, configuracao, tech-mentor-infra]
skill: tech-mentor-infra
status: stub
---

# Variáveis de Ambiente (.env, export)

Valores nomeados disponíveis para processos e scripts do shell — usados para configuração (URLs de banco, portas, chaves) sem hard-code no código.

## Formas de definir

Segundo [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]:

- **`export PORT=3000`** — cria a variável na instância atual do terminal. `echo $PORT` imprime `3000`; ela vale dentro dos scripts rodados naquela sessão.
- **Arquivo `.env`** — arquivo oculto (começa com ponto) muito usado em aplicações reais para guardar variáveis. Nada de especial nele além do ponto inicial. Ex.: `echo "DATABASE_URL=..." >> .env`.
- **`.zshrc` / `.bashrc`** — arquivos de rc do shell onde variáveis são exportadas automaticamente sempre que o terminal inicia (ex.: configuração feita ao instalar Python). Ver [[wiki/concepts/shell-terminal]].

## Notas

- Arquivos `.env` normalmente **não** vão para o repositório (contêm segredos) — o padrão é versionar um `.env.example` e ignorar o `.env` real. `[skill: tech-mentor-infra]`
- O `$` prefixa a leitura da variável (`$PORT`); a atribuição não usa `$`.

## Atualização Automática por Plataforma de Deploy

Em pipelines de [[wiki/concepts/database-branching]], a `DATABASE_URL` de um ambiente de preview muda a cada deploy (aponta para a branch de banco daquela branch de código). Plataformas com integração nativa (ex.: Vercel↔Neon) atualizam essa variável automaticamente no momento do deploy; sem essa integração, o próprio time precisaria escrever o mecanismo — criar a branch de banco, obter a nova connection string, e escrevê-la na variável de ambiente antes de cada deploy.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] — `DATABASE_URL` atualizada automaticamente pela integração Vercel↔Neon a cada deploy de branch
