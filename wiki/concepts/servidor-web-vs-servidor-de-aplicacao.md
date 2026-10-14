---
type: concept
title: "Servidor Web vs. Servidor de Aplicação"
aliases: ['web server vs application server']
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [web, backend, servidor, infra]
skill: tech-mentor-frontend
status: draft
---

# Servidor Web vs. Servidor de Aplicação

- **Servidor web** (Apache, Nginx): função principal é servir arquivos/páginas HTML.
- **Servidor de aplicação** (ex.: servidores Java/J2EE): função principal é **executar programas que cospem HTML**.
- Todo servidor de aplicação é também um servidor web, mas nem todo servidor web é de aplicação.

O servidor mais simples mapeia URL → caminho de arquivo sem checagem, o que é problema de segurança (acesso a arquivos não públicos). Origem: [[wiki/concepts/cgi-common-gateway-interface]]; ver [[wiki/entities/apache-http-server]], [[wiki/concepts/porta-de-rede]], [[wiki/concepts/historia-do-front-end]].

## Key sources

- [[wiki/sources/historia-do-front-end-akita-ep4]]
