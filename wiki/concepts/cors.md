---
type: concept
title: "CORS"
aliases: ["cross-origin resource sharing", "erro de cors"]
date_created: 2026-09-30
date_updated: 2026-11-16
source_count: 5
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

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], o CORS "define [...] quais endereços externos vão ter acesso" à API, com `app.use(cors())` aberto em desenvolvimento e o domínio do front-end em produção. A nuance: é o navegador que aplica a regra; Insomnia e React Native não são afetados, e CORS não substitui autenticação.

## Na NLW #2, dia 2 (Diego Fernandes)

`app.use(cors())` para o front em `localhost:3000` chamar a API em `:3333`. A aula atribui o bloqueio ao servidor ("por padrão, ele permite apenas [...] o mesmo endereço"), mas quem aplica é o navegador; `cors()` sem opções libera `*`. Ver [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]].

Em [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]], o CORS aparece como coluna da lista Public APIs e é definido como "uma requisição dentro de uma outra requisição", bloqueada "para poder evitar [...] que você execute um script dentro de um outro lugar". Não é isso: o navegador aplica a same-origin policy, e o CORS é o servidor liberando a leitura por outra origem (`Access-Control-Allow-Origin`). Executar script alheio é [[wiki/concepts/xss]]. "CORS: yes" na lista quer dizer que a API pode ser chamada direto do front.

Em [[wiki/sources/frontpush-modules-js-import-export-default]], o ESM no navegador "precisa estar rodando em um servidorzinho" (Live Server). O motivo é o CORS: scripts módulo são buscados com as regras de CORS, e a página aberta por `file://` tem origem `null`.

## Key sources
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — CORS como política do navegador e correção no servidor
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: cors() no Express; não é controle de acesso
- [[wiki/sources/nlw-2-diego-fernandes-dia-2-api-rest-node-express-knex-proffy]]: NLW #2, Diego, dia 2: cors() para o front em :3000
- [[wiki/sources/frontpush-api-e-protocolo-http-metodos-get-post-put-delete]]: FrontPUSH, JavaScript aula 13: CORS mal definido ("requisição dentro de requisição")
- [[wiki/sources/frontpush-modules-js-import-export-default]]: FrontPUSH, JavaScript aula 17: módulos exigem servidor por causa do CORS
