---
type: concept
title: "SQLite"
aliases: ["sqlite3", "banco embarcado"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [sqlite, banco-de-dados, embarcado, mobile, backend]
skill: tech-mentor-backend
status: stub
---

# SQLite

Não é um servidor de banco de dados — é uma biblioteca C incluída diretamente no projeto, sem processo próprio, sem instância, sem configuração de rede. O banco inteiro é um único arquivo no disco.

## Limites Técnicos

Tamanho teórico de até 281 TB; na prática, manter abaixo de 1 TB. Leitura extremamente rápida por ser tudo local, sem latência de rede.

## O Limite Que Importa: Concorrência de Escrita

SQLite usa lock global do banco para escrita — uma transação de escrita bloqueia o banco inteiro. Leituras simultâneas funcionam bem em modo **WAL** (Write-Ahead Logging), mas escritas concorrentes são serializadas. Regra objetiva: se mais de dois ou três processos precisam escrever simultaneamente, não use SQLite.

## Quem Usa (Surpreendente)

Todo app Android e iOS tem um SQLite interno. Chrome e Firefox guardam histórico, bookmarks e cookies em SQLite. O gerenciador de pacotes npm usa SQLite. Aviões Airbus usam SQLite em sistemas de aviônica, citado como certificado pela norma **DO-178C** — a certificação mais rigorosa de software embarcado aeronáutico do mundo (claim não verificada nesta ingestão, ver open question na fonte).

## Quando Usar

App mobile/desktop com usuário único, protótipos de MVPs rápidos, testes automatizados onde não se quer subir um servidor, sistemas embarcados.

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
