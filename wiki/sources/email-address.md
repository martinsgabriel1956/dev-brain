---
type: source
title: "Endereço de E-mail — Sintaxe RFC 5322, Domínio e Internacionalização (EAI)"
aliases: ["email address", "endereço de email", "rfc 5322", "sintaxe de email", "eai", "smtputf8"]
date_created: 2026-07-30
date_updated: 2026-07-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/email-address.md
source_url: https://en.wikipedia.org/wiki/Email_address
date_published: ""
date_ingested: 2026-07-30
source_count: 0
tags: [email, rfc-5322, sintaxe, validacao, dns, smtp, internacionalizacao, mx-record]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Endereço de e-mail é `local-part@domain`, padronizado pela RFC 5322 (com RFC 6854 e RFC 5321 para transporte). A parte local tem até 64 octetos e é tecnicamente case-sensitive, mas na prática todo provedor trata como case-insensitive. O domínio segue regras de hostname (LDH, labels de até 63 caracteres, máx. 255 octetos). Sub-addressing (`user+tag@domain`) é convenção formal (RFC 5233), não capricho de provedor. Internacionalização (EAI, RFC 6530-6533 + SMTPUTF8) permite UTF-8 completo em ambos os lados do `@`. Correção sintática não garante existência da caixa — validação real depende de MX record + confirmação por link, não de regex.

## Key Claims

**Claim:** A parte local do e-mail é formalmente case-sensitive pela RFC, mas isso é ignorado na prática por convenção universal dos provedores.
**Evidence:** O artigo afirma que embora os padrões RFC designem a local-part como case-sensitive, sistemas de recebimento tipicamente entregam mensagens de forma "case-independent", tratando `Jane.Smith` e `jane.smith` como equivalentes. Isso é uma lacuna entre spec formal e comportamento real de mercado — relevante para quem escreve validação de e-mail assumindo (erroneamente) que a RFC garante case sensitivity universal.
**Confidence:** alta

**Claim:** `user+tag@domain.com` (sub-addressing) é um padrão formal, não uma gambiarra de provedor — está na RFC 5233 e é suportado por Gmail, Outlook.com, Yahoo Mail Plus, Apple iCloud e Proton Mail.
**Evidence:** O `+tag` roteia para a mesma caixa que o endereço sem tag, permitindo filtragem e controle de spam por parte do usuário. Implicação prática: um sistema de validação de e-mail rígido que rejeita `+` na parte local está rejeitando endereços RFC-válidos e usados por múltiplos provedores mainstream.
**Confidence:** alta

**Claim:** Correção sintática de um endereço não implica que a caixa de entrada exista — a única verificação confiável é o link de confirmação (ou callback verification, que tem trade-offs de risco).
**Evidence:** O artigo separa explicitamente validação sintática (regex, HTML5 form validation, RFC 3696) de verificação de existência real. Cita duas abordagens: (1) link de verificação temporário enviado ao endereço — ativa a conta, prova posse; (2) callback verification — checar a caixa diretamente, mas isso arrisca ataques de directory harvest e pode disparar denúncias de spam contra quem faz a checagem.
**Confidence:** alta

**Claim:** A resolução de e-mail depende de registros DNS MX (Mail Exchange); na ausência deles, cai para registros A/AAAA do domínio.
**Evidence:** Mail user agents (MUA) e mail transfer agents (MTA) consultam o DNS por registros MX contendo o servidor de e-mail do destinatário antes de entregar via SMTP (RFC 5321/5322). Isso implica que a parte local do endereço não tem nenhum significado para os sistemas de retransmissão intermediários — só o host final da caixa a interpreta.
**Confidence:** alta

**Claim:** Cabeçalho de e-mail e endereço de envelope (envelope-from/envelope-to, usado pelo SMTP) podem divergir — essa é a base técnica do email spoofing usado em spam e phishing.
**Evidence:** O artigo afirma essa divergência diretamente como o mecanismo habilitador de spoofing, sem exigir nenhuma vulnerabilidade adicional — é uma característica do próprio protocolo SMTP, não um bug.
**Confidence:** média (o artigo afirma o fato mas não detalha o mecanismo SMTP MAIL FROM vs. header From — para aprofundar seria necessário RFC 5321 diretamente ou uma fonte de segurança dedicada, ex. SPF/DKIM/DMARC)

**Claim:** EAI (Email Address Internationalization — RFC 6530-6533 + extensão SMTPUTF8) permite UTF-8 completo tanto na parte local quanto no domínio, cobrindo latim com diacríticos, grego, chinês, japonês, cirílico e devanágari.
**Evidence:** Exemplos dados incluem `δοκιμή@παράδειγμα.δοκιμή` (grego), `我買@屋企.香港` (chinês tradicional), `медведь@с-балалайкой.рф` (cirílico) e `संपर्क@डाटामेल.भारत` (devanágari). A negociação SMTPUTF8 é o mecanismo de extensão SMTP que habilita isso ponta a ponta.
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/validacao-de-entrada]] — a fonte formaliza exatamente o "e-mail malformado" citado de forma genérica nesse conceito: mostra onde a regra RFC termina e onde a prática de mercado diverge
- [[wiki/concepts/contrato-de-api]] — RFC 5322/5321 é um contrato formal de sintaxe entre sistemas, análogo ao contrato de API entre cliente e servidor
- [[wiki/concepts/soberania-digital]] — a aprovação do domínio ".bharat" em sete escritas (Devanágari etc.) pela Índia é um exemplo concreto de internacionalização de infraestrutura de internet puxada por política nacional, tema relacionado

## Open Questions

- O artigo não detalha o mecanismo técnico de SPF/DKIM/DMARC que hoje mitiga o spoofing habilitado pela divergência header/envelope — vale uma fonte dedicada de segurança de e-mail.
- Como sistemas reais (Gmail, Postgres `citext`, bibliotecas de validação) lidam na prática com o limite de 64 octetos da parte local e com EAI — a fonte descreve a spec, não a adoção real dessas duas áreas.
