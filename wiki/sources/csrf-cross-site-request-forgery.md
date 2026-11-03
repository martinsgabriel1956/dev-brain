---
type: source
title: "CSRF: Cross-Site Request Forgery"
aliases: ["csrf na pratica", "csrf banco e laboratorio portswigger"]
date_created: 2026-11-03
date_updated: 2026-11-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/csrf-cross-site-request-forgery.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-11-03
source_count: 1
tags: [csrf, same-origin-policy, cookies, samesite, csrf-token, appsec, portswigger, browser-security]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo didático, de autor não identificado, que explica [[wiki/concepts/csrf|CSRF]] em três passos: a [[wiki/concepts/same-origin-policy|same-origin policy]] restringe leitura, mas costuma permitir escrita entre origens; o navegador envia cookies de sessão sozinho; logo, uma página maliciosa consegue disparar uma ação autenticada sem precisar ler a resposta. Mostra um banco de exemplo, resolve um laboratório da [[wiki/entities/portswigger|PortSwigger]] e apresenta duas defesas: [[wiki/concepts/csrf-token|token CSRF]] e [[wiki/concepts/samesite-cookie|`SameSite`]]. O mecanismo confere com MDN, PortSwigger e OWASP. O limite da fonte está nas defesas: omite as ressalvas de `SameSite` e o papel do XSS.

## Key Claims

**Claim:** Uma origem é definida por protocolo, domínio e porta.
**Evidence:** definição dada no vídeo.
**Confidence:** alta. [external] [MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) usa a mesma tupla.

**Claim:** A interação entre origens se divide em escrita e embedding, geralmente permitidos, e leitura, bloqueada por padrão.
**Evidence:** exemplos do vídeo: formulário e redirect (escrita); imagem, style sheet e iframe (embedding); resposta de requisição (leitura).
**Confidence:** alta. [external] É a classificação da MDN, que acrescenta duas ressalvas ausentes no vídeo: alguns pedidos exigem preflight e o embedding vaza parte da informação, como as dimensões de uma imagem.

**Claim:** CSRF não quebra a same-origin policy. Basta a vítima estar logada, porque o navegador anexa os cookies, e o atacante não precisa ler a resposta.
**Evidence:** o script força o envio da transferência; o cookie de sessão vai junto; a escrita entre origens já é suficiente.
**Confidence:** alta. Consistente com [[wiki/concepts/sessoes-http-cookies]] e com a MDN.

**Claim:** Só carregar a página maliciosa basta: um iframe com formulário invisível é enviado por script no carregamento.
**Evidence:** aba de rede e código-fonte do site do atacante no cenário do banco. A vítima ainda precisou abrir o link recebido por e-mail.
**Confidence:** alta para o padrão. O código exibido na tela não está na transcrição, e a configuração de cookie da demonstração é desconhecida (ver Open Questions).

**Claim:** No laboratório, a troca de e-mail é vulnerável porque o POST leva só o novo e-mail no body, sem exigir o e-mail antigo nem token.
**Evidence:** requisição interceptada e código-fonte do formulário, sem nenhum token. O ataque é entregue pelo servidor de exploit da plataforma.
**Confidence:** alta. [external] A descrição bate com [*CSRF vulnerability with no defenses*](https://portswigger.net/web-security/csrf/lab-no-defenses). O nome do laboratório não é dito no vídeo: a identificação é inferência da wiki. O caso também preenche as três condições que a [PortSwigger lista](https://portswigger.net/web-security/csrf): ação relevante, sessão só por cookie e nenhum parâmetro imprevisível.

**Claim:** Um token CSRF único e imprevisível, gerado no backend e exigido nas ações sensíveis, dificulta muito o ataque, porque o atacante teria de adivinhá-lo.
**Evidence:** explicação do vídeo, com o token inserido pelo backend no formulário.
**Confidence:** alta, com lacunas. [external] O [cheat sheet da OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) acrescenta que o token deve ser único por sessão e que XSS derruba todas as mitigações de CSRF.

**Claim:** `SameSite` com valor `lax` ou `strict` pode impedir CSRF, evitando que requisições críticas saiam autenticadas.
**Evidence:** afirmação do vídeo, sem demonstração.
**Confidence:** média. O vídeo usa "pode", mas apresenta o atributo no mesmo nível do token. [external] A OWASP o coloca entre as técnicas de defesa em profundidade, e a [PortSwigger documenta bypasses](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions): ação de estado aceita em GET (contra `Lax`), gadgets no próprio site (contra `Strict`) e domínios irmãos. Detalhes em [[wiki/concepts/samesite-cookie]].

## Entities

[[wiki/entities/portswigger]].

## Concepts

[[wiki/concepts/csrf]], [[wiki/concepts/same-origin-policy]], [[wiki/concepts/csrf-token]], [[wiki/concepts/samesite-cookie]], [[wiki/concepts/sessoes-http-cookies]], [[wiki/concepts/metodos-http]], [[wiki/concepts/pentest]]. Citados só na conferência externa: [[wiki/concepts/cors]], [[wiki/concepts/xss]], [[wiki/concepts/owasp]].

## Open Questions

- **Como o ataque do banco funcionou?** [external] Segundo a [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie), `Lax` explícito não envia cookie em navegação dentro de iframe nem em POST entre sites. A PortSwigger diz que o Chrome aplica `Lax` por padrão desde 2021. Inferência da wiki: a demonstração dependeria de `SameSite=None` ou de um navegador sem esse padrão, mas a transcrição não mostra o cookie.
- **Quais navegadores usam `Lax` por padrão hoje?** A MDN diz apenas "alguns", e a página da PortSwigger trata os demais como adoção futura, sem data. Não foi possível confirmar o estado atual.
- **Origem ou site?** O vídeo define CSRF por "origens diferentes", mas `SameSite` compara sites. [external] A PortSwigger observa que um pedido entre origens ainda pode ser same-site, o que abre o bypass por domínios irmãos.
- **APIs JSON:** o vídeo só cobre formulário. O preflight mudaria o vetor em APIs que exigem `application/json`, mas o detalhe da OWASP chegou apenas em resumo e não foi conferido no texto integral.
- A descrição do vídeo, com os links prometidos, não veio junto da transcrição.

## Quotes

> "Ele não quebra a política de same origin em nenhum momento."

> "A interação não precisou ler a resposta do banco."
