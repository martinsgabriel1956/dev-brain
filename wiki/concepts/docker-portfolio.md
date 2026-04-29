---
type: concept
title: "Docker no Portfólio"
aliases: ["docker compose portfolio", "dockerfile multi-stage portfolio"]
date_created: 2026-04-25
date_updated: 2026-04-25
source_count: 1
tags: [docker, portfolio, backend, deploy, multi-stage]
skill: tech-mentor-leadership
status: stub
---

# Docker no Portfólio

Configurar Docker e Docker Compose numa aplicação de portfólio demonstra que o candidato trabalha com as ferramentas que qualquer empresa de backend vai exigir no dia a dia.

## O mínimo esperado

```yaml
# docker-compose.yml — sobe todo o ambiente com um comando
services:
  app:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: postgres:16
    environment:
      POSTGRES_DB: app
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
  db_test:
    image: postgres:16
    environment:
      POSTGRES_DB: app_test
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
```

## O plus: Dockerfile com multi-stage build

```dockerfile
# stage 1: build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# stage 2: runtime — imagem enxuta sem devDependencies
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/server.js"]
```

Multi-stage build resulta em imagem menor e mais segura — só o necessário para rodar.

## Bônus: incluir observabilidade no Compose

Adicionar Jaeger ou similar ao `docker-compose.yml` demonstra maturidade além do básico (ver [[observabilidade]]).

## Relações

- [[portfolio-backend-junior]]
- [[observabilidade]]

## Key sources

- [[wiki/sources/diferenciais-portfolio-backend-junior]]
