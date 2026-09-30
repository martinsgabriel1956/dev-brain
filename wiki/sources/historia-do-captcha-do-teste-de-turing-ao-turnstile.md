---
type: source
title: "A História do CAPTCHA: do Teste de Turing ao Turnstile"
aliases: ["história do captcha", "captcha morreu", "captcha video"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [seguranca, captcha, bot-detection, recaptcha, turnstile, proof-of-work, teste-de-turing, anti-bot]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/historia-do-captcha-do-teste-de-turing-ao-turnstile.md
source_url:
author: desconhecido (vídeo em PT-BR)
date_published:
date_ingested: 2026-09-29
---

# A História do CAPTCHA: do Teste de Turing ao Turnstile

## TL;DR

Vídeo que conta a história do [[wiki/concepts/captcha]] de 1996 a hoje e defende a tese de que **o conceito formal de CAPTCHA já morreu**: por definição (paper de 2003) ele só é seguro enquanto existe um problema de IA em aberto, então "já nasce com prazo de validade". Percorre a proposta de Moni Naor (1996), o texto distorcido contra [[wiki/concepts/ocr]], a formalização de 2003, o [[wiki/concepts/recaptcha]] (2007) que aproveitava trabalho humano para digitalizar o [[wiki/entities/new-york-times]], a morte do CAPTCHA de texto pelo [[wiki/entities/google]] (99% de acerto por IA, 2014), o "Não sou um robô" e o reCAPTCHA v3 (score de risco, segurança por [[wiki/concepts/seguranca-por-obscuridade]]), o [[wiki/concepts/cloudflare-turnstile]] com [[wiki/concepts/proof-of-work]] e [[wiki/concepts/proof-of-space]], o [[wiki/concepts/funcaptcha]] do [[wiki/entities/roblox]] e, por fim, o [[wiki/concepts/servico-de-resolucao-de-captcha]] (comprar o humano em que o detector confia).

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Naor (1996) propôs usar um [[wiki/concepts/teste-de-turing]] invertido para provar que o outro lado é humano | manuscrito teórico de 1996 | Alta (consistente com [external] https://en.wikipedia.org/wiki/CAPTCHA) |
| Um CAPTCHA formal tem gerador + testador que confere sem saber a solução; exige (1) automatizável, (2) humano passa com prob. alta, (3) nenhum programa passa mesmo conhecendo o algoritmo | paper de 2003 | Alta |
| Logo todo CAPTCHA baseado em problema de IA em aberto tem validade limitada | dedução da definição | Alta (lógica); é inferência do autor |
| ~200 mi CAPTCHAs/dia × 10 s ≈ 500 mil horas humanas/dia | cálculo do vídeo | Alta (200e6 × 10 s ≈ 555 mil h) |
| reCAPTCHA (2007) usava palavra de controle + palavra desconhecida; respostas viravam votos até haver maioria | descrição do mecanismo | Alta |
| Google comprou o reCAPTCHA em 2009 | vídeo | Alta [external] |
| IA do Google resolvia CAPTCHA de texto com ~99% (2014), matando o formato | vídeo | Média — número citado sem paper na fonte |
| "Não sou um robô" usa idade do cookie e fingerprint; movimento de mouse **não** mostrou efeito nos testes dos pesquisadores | engenharia reversa de pesquisadores (2016) | Média — ver Open Questions |
| Cookie maduro (> 9 dias) garantia passar; um IP gerava dezenas de milhares de cookies/dia; YOLO resolvia desafios de imagem com ~100% | pesquisa de 2016 | Média — número de cookies corrompido na transcrição (~63.000) |
| reCAPTCHA v3 devolve score 0–1 e o desenvolvedor decide a ação; viola o requisito de 2003 (segurança por obscuridade) | descrição + crítica do autor | Alta (descrição); a crítica é opinião fundamentada |
| Turnstile usa proof of work (nonce com hash de zeros à esquerda, 50 mil–2 mi tentativas) e proof of space (tabela em memória + consulta aleatória) | descrição | Alta; nota: prova "navegador real", não "humano" |
| FunCaptcha tem >1.200 variações e cruza resposta + script ofuscado + telemetria | descrição | Média |
| Resolvedores humanos via API (ex.: 2Captcha) tornam o CAPTCHA contornável por custo | descrição | Alta |

## Entidades

- [[wiki/entities/moni-naor]] · [[wiki/entities/google]] · [[wiki/entities/new-york-times]] · [[wiki/entities/cloudflare]] · [[wiki/entities/roblox]] · [[wiki/entities/alan-turing]] (origem do teste de Turing)
- PayPal e Yahoo — primeiros adotantes (sem página própria)

## Conceitos

- [[wiki/concepts/captcha]] (novo) · [[wiki/concepts/recaptcha]] (novo) · [[wiki/concepts/teste-de-turing]] (novo) · [[wiki/concepts/ocr]] (novo)
- [[wiki/concepts/bot-detection]] (novo) · [[wiki/concepts/seguranca-por-obscuridade]] (novo)
- [[wiki/concepts/cloudflare-turnstile]] (novo) · [[wiki/concepts/proof-of-work]] (novo) · [[wiki/concepts/proof-of-space]] (novo) · [[wiki/concepts/funcaptcha]] (novo)
- [[wiki/concepts/servico-de-resolucao-de-captcha]] (novo)
- Tocados: [[wiki/concepts/hashing]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/sessoes-http-cookies]], [[wiki/concepts/engenharia-reversa]], [[wiki/concepts/maquina-de-turing]]

## Open Questions

- **Mouse e reCAPTCHA:** a fonte diz que o movimento do mouse não influenciava o resultado nos testes de 2016; a skill [skill: tech-mentor-security] (`fraud-abuse.md`) lista dinâmica de mouse como sinal clássico de bot detection. Conciliação provável: o teste vale para *aquele* sistema/versão; sinais comportamentais continuam usados por outros vendors. Ver [[wiki/concepts/bot-detection]].
- Imprecisão de escopo: a fonte diz "prova que sou humano? Não" para Turnstile; tanto proof of work quanto proof of space provam **custo/ambiente**, não humanidade.
- Datas/números (13 mi artigos desde 1850, 99%, 63.000 cookies) vêm só da fala; não verificados contra os papers originais.
- Autor e canal do vídeo desconhecidos — confiança na cronologia é a da própria narração.

## Trechos

> "Todo capta pela sua própria definição já nasce com prazo de validade."

> "Isso nem devia se chamar capt mais… não tem mais teste, é só um score de risco."

> "Não vale mais a pena brigar com uma IA de detecção se dá para simplesmente comprar o humano que ela já confia."
