---
type: concept
title: "CORS"
aliases: ["cross-origin resource sharing", "erro de cors"]
date_created: 2026-09-30
date_updated: 2026-11-03
source_count: 1
tags: [cors, navegador, seguranca, http, origem]
skill: tech-mentor-networking
status: stub
---

# CORS

Erro de CORS **não é bug aleatório**: é o **navegador** aplicando uma política de segurança porque a *origem* que fez a requisição difere da origem do servidor. A correção correta é **configurar o servidor para permitir aquela origem específica** (allowlist), não procurar gambiarra no cliente.

- Origem = esquema + host + porta. A política em si está em [[wiki/concepts/same-origin-policy]].
- Bloqueio de CORS não é defesa contra [[wiki/concepts/csrf]]: a política restringe sobretudo a leitura, e um formulário entre origens continua sendo enviado (inferência da wiki a partir de [[wiki/sources/csrf-cross-site-request-forgery]], que não cita CORS).
- [external] É imposto pelo navegador: Postman/curl não sofrem CORS. Requisições "não simples" disparam um preflight `OPTIONS` (https://developer.mozilla.org/docs/Web/HTTP/CORS).
- Configuração frouxa (`*` com credenciais ou reflexo da origem) vira falha: [[wiki/concepts/cors-misconfiguration]].
- Diagnóstico: comparar headers na aba Network ([[wiki/concepts/debug-de-requisicao-http]]); relacionados [[wiki/concepts/http-headers]], [[wiki/concepts/sessoes-http-cookies]].

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — CORS como política do navegador e correção no servidor
