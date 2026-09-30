---
type: concept
title: "reCAPTCHA"
aliases: ["recaptcha", "no captcha recaptcha", "reCAPTCHA v3"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 1
tags: [seguranca, captcha, google, bot-detection]
skill: tech-mentor-security
status: draft
---

# reCAPTCHA

Família de CAPTCHAs criada em 2007 e comprada pelo [[wiki/entities/google]] em 2009.

- **v1 (2007):** duas palavras — uma de **controle** (resposta conhecida) e uma **desconhecida** que o [[wiki/concepts/ocr]] não leu no arquivo do [[wiki/entities/new-york-times]]. Acertar a de controle faz o sistema assumir que a outra também está certa; a resposta vira **voto**, e maioria de votos define a palavra. Aproveitava as ~500 mil horas/dia de trabalho humano dos [[wiki/concepts/captcha]].
- **"Não sou um robô" (2014):** checkbox que só observa comportamento; desafio de imagem só se parecer bot. Engenharia reversa (2016): usa **idade do cookie** e **fingerprint do navegador**; um cookie com >9 dias garantia passar, e a imagem foi vencida com YOLO (~100%). Ver [[wiki/concepts/sessoes-http-cookies]].
- **v3 (2018):** invisível, **score 0–1**; o desenvolvedor decide a ação por faixa (ex.: <0,2 bloqueia, <0,5 confirma por e-mail). Sem teste real — depende de [[wiki/concepts/seguranca-por-obscuridade]].

## Key sources

- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]]
