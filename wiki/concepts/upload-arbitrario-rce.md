---
type: concept
title: "Upload Arbitrário → RCE"
aliases: ["arbitrary file upload", "upload malicioso", "rce via upload", "unrestricted file upload"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [rce, upload, appsec, mime-type, plugin, code-execution, owasp]
skill: tech-mentor-security
status: stub
---

# Upload Arbitrário → RCE

Vulnerabilidade onde a aplicação aceita um arquivo enviado por um usuário sem validar suficientemente seu conteúdo/tipo, e em algum ponto do fluxo esse arquivo é executado, interpretado ou tratado como código pelo servidor — resultando em Remote Code Execution (RCE).

## Padrão Demonstrado: Sistema de Plugins Sem Validação

[[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] documenta o caso mais direto dessa classe: um painel administrativo com uma funcionalidade de "instalar plugin" que aceita upload de um arquivo arbitrário e o executa como parte da aplicação. Sem nenhuma validação de conteúdo, um arquivo malicioso é aceito e instalado, resultando em execução de comandos arbitrários no servidor (confirmado com `ls`, `pwd`, leitura de `/etc/passwd`). Nesse caso, o acesso administrativo já havia sido obtido via [[wiki/concepts/account-takeover]] — o upload foi a etapa final da cadeia, não a inicial.

## Por Que "Só Validar a Extensão" Não Basta

Extensão de arquivo é metadado controlado pelo cliente — renomear `shell.php` para `foto.jpg` não muda o conteúdo. A validação precisa cobrir, no mínimo:

- **MIME type real do conteúdo**, verificado no backend (não confiar no `Content-Type` enviado pelo cliente nem só na extensão do nome do arquivo).
- **Allowlist de extensões**, restrita ao estritamente necessário para a funcionalidade (ex.: só `.jpg`/`.png` para upload de foto de perfil) — nunca aceitar qualquer extensão "por via das dúvidas".
- **Armazenamento fora de diretórios servidos publicamente/executáveis** — um arquivo malicioso salvo onde o servidor web não o interpreta como código não gera RCE, mesmo que o upload em si tenha passado.
- **Nenhuma execução dinâmica de arquivo vindo de usuário** — sistemas de "plugin" ou "extensão" que executam código enviado por upload são, por definição, um vetor de RCE se o autor do upload não for de confiança absoluta (o que inclui: qualquer usuário cuja conta pode ter sido comprometida via [[wiki/concepts/account-takeover]]).

## Relação com outros conceitos

- [[wiki/concepts/account-takeover]] — nesta fonte, o pré-requisito que deu acesso ao painel onde o upload malicioso foi possível
- [[wiki/concepts/secrets-management]] — parte da mesma cadeia de ataque, na origem
- [[wiki/concepts/attack-surface]] — uma funcionalidade de "plugin custom" é superfície de ataque de alto risco por definição; deveria exigir camadas extras de confiança/validação, não as mesmas de um upload comum

## Key Sources

- [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]
