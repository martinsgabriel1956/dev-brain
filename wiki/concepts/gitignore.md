---
type: concept
title: ".gitignore"
aliases: ["gitignore", "git ignore", ".gitkeep"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [git, versionamento, repositorio]
skill: lang-dynamic
status: stub
---

# .gitignore

Arquivo com padrões de caminhos que o [[wiki/concepts/git]] não deve rastrear: dependências instaladas, builds, bancos locais, segredos e arquivos de usuário. O `!` reabre uma exceção dentro de um padrão ignorado. O `.gitkeep` é só uma convenção (o Git não versiona pastas vazias), um arquivo vazio que mantém a pasta no repositório.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]), o `server/.gitignore` de [[wiki/entities/diego-fernandes]]:

- **`node_modules`,** que "não é legal a gente subir" (ver [[wiki/concepts/package-json]]).
- **`uploads/*` com `!uploads/.gitkeep`,** para manter a pasta sem os arquivos dos usuários.
- **`*.sqlite`,** para "que a pessoa crie o banco do zero".

**O efeito colateral da aula:** os SVGs dos itens de coleta foram postos em `uploads/` no dia 2. Com `uploads/*` ignorado, quem clona o repositório fica sem os ícones. A correção é separar os assets do projeto (versionados) dos uploads de usuários (ignorados).

**Outros itens comuns:** `.env` (segredos, ver [[wiki/concepts/variaveis-de-ambiente]]), `dist/` e `build/`, `.DS_Store`, logs e `coverage/`. O GitHub mantém modelos por linguagem (github/gitignore).

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: gitignore do server do Ecoleta
