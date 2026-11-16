---
type: concept
title: "Variáveis de Ambiente (.env, export)"
aliases: ["variáveis de ambiente", "env", ".env", "export", "environment variables", "zshrc", "bashrc"]
date_created: 2026-08-11
date_updated: 2026-11-16
source_count: 6
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], `image_url` é montada com `http://localhost:3333` fixo no código; a URL base deveria vir de variável de ambiente.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], a `baseURL` do Axios é `http://localhost:3333` fixo. No CRA, o lugar é `REACT_APP_API_URL`; no Vite, `VITE_*`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], o IP `192.168.1.13` aparece fixo no app e no back-end. No Expo, a saída é `EXPO_PUBLIC_API_URL` ou derivar do `hostUri` em desenvolvimento.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], a terceira troca manual de URL base na semana (agora .12) reforça o caso para configuração por ambiente.

## Key Sources

- [[wiki/sources/comandos-basicos-linux-todo-dev-precisa-conhecer-galego]]
- [[wiki/sources/database-branching-testes-neon-fernanda-kipper]] — `DATABASE_URL` atualizada automaticamente pela integração Vercel↔Neon a cada deploy de branch
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: URL base fixa no código
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: baseURL do front-end fixa no código
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: IP fixo no app e na API
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: mais uma URL fixa trocada à mão
