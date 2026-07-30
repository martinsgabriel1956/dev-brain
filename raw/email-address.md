---
date: 2026-07-30
tags: [rfc-5322, email, sintaxe, validacao, internacionalizacao, smtp, dns]
skill: tech-mentor-backend
source_url: https://en.wikipedia.org/wiki/Email_address
level: fundamental
---

# Endereço de E-mail (Wikipedia, EN → traduzido)

> Tradução/adaptação em Markdown do artigo "Email address" da Wikipedia em inglês. Fonte original: https://en.wikipedia.org/wiki/Email_address

## Introdução

Um endereço de e-mail identifica a caixa de destino de mensagens eletrônicas. O formato moderno segue padrões estabelecidos pela IETF (Internet Engineering Task Force) na década de 1980, especificamente a **RFC 5322** e a **RFC 6854**. A estrutura básica é composta por uma parte local (local-part), o símbolo `@` e um domínio.

## Estrutura básica

O formato é `local-part@domain`. Endereços como `jane.smith@example.com` demonstram esse design de dois componentes. Embora os padrões RFC definam a parte local como *case-sensitive* (sensível a maiúsculas/minúsculas), sistemas de recebimento tipicamente entregam mensagens de forma *case-independent*, tratando variações como `Jane.Smith` e `jane.smith` como equivalentes.

## Regras da parte local (local-part)

A parte local pode conter até **64 octetos** e pode incluir:

**Formato sem aspas (unquoted):**
- Letras (A-Z, a-z)
- Dígitos (0-9)
- Caracteres especiais: `!#$%&'*+-/=?^_\`{|}~`
- Pontos (`.`), desde que não sejam o primeiro caractere, o último, nem consecutivos

**Formato com aspas (quoted)** permite caracteres adicionais, incluindo espaços e caracteres especiais como parênteses e colchetes, com regras específicas de escape.

### Casos especiais

A parte local `postmaster` é universalmente case-insensitive e deve rotear para os administradores do domínio. Comentários entre parênteses são tecnicamente permitidos, mas raramente usados na prática.

### Sub-addressing (endereçamento com tags)

Serviços que suportam sub-addressing permitem endereçamento baseado em tags: `joeuser+tag@example.com` roteia para a mesma caixa de entrada que `joeuser@example.com`. Essa convenção, formalmente chamada de "subaddressing" na RFC 5233, suporta filtragem de e-mail e controle de spam. Provedores importantes que implementam isso: Gmail, Outlook.com, Yahoo Mail Plus, Apple iCloud e Proton Mail.

## Regras do domínio

O componente de domínio segue regras estritas de hostname:

- Máximo de **255 octetos** no total
- Labels de DNS limitados a **63 caracteres** cada
- Letras (A-Z, a-z), dígitos (0-9) e hífens (`-`)
- Hífens não podem ser o primeiro nem o último caractere
- TLDs (top-level domains) não podem ser totalmente numéricos

A regra **LDH** (Letters, Digits, Hyphen) governa a composição padrão de domínios. Domínios também podem usar endereços IP entre colchetes: `jsmith@[192.168.2.1]` ou formato IPv6 `jsmith@[IPv6:2001:db8::1]`, embora isso apareça principalmente em spam.

## Exemplos válidos

Endereços padrão incluem:
- `simple@example.com`
- `very.common@example.com`
- `x@example.com` (parte local de uma única letra é permitida)
- `user.name+tag+sorting@example.com`
- `name/surname@example.com`
- `admin@example` (domínios sem ponto/TLD são desencorajados pela ICANN)

Endereços complexos mas válidos permitem strings entre aspas: `"jane..doe"@example.org` permite pontos consecutivos dentro das aspas, ao contrário do formato sem aspas.

## Exemplos inválidos

Padrões proibidos incluem:
- `abc.example.com` (falta o `@`)
- `a@b@c@example.com` (múltiplos `@` fora de aspas)
- `1234567890123456789012345678901234567890123456789012345678901234+x@example.com` (excede o limite de 64 caracteres da parte local)
- `i.like.underscores@but_they_are_not_allowed_in_this_part` (underscores proibidos no domínio)

## Internacionalização (EAI — Email Address Internationalization)

O grupo de trabalho Email Address Internationalization produziu as RFCs 6530-6533, habilitando codificação UTF-8 tanto na parte local quanto no domínio. Esse avanço suporta caracteres não-ASCII essenciais para:

- Latim com diacríticos: `éléonore@example.com`
- Grego: `δοκιμή@παράδειγμα.δοκιμή`
- Chinês tradicional: `我買@屋企.香港`
- Japonês: `二ノ宮@黒川.日本`
- Cirílico: `медведь@с-балалайкой.рф`
- Devanágari: `संपर्क@डाटामेल.भारत`

A negociação da extensão **SMTPUTF8** habilita esse suporte. A aprovação do domínio ".bharat" pela Índia em sete escritas exemplifica a implementação prática de internacionalização.

## Transporte de mensagens

A transmissão de e-mail usa o **Simple Mail Transfer Protocol (SMTP)**, definido nas RFC 5321 e RFC 5322. Agentes de usuário de e-mail (MUA) e agentes de transferência de e-mail (MTA) consultam o DNS por registros **MX**, que contêm as informações do servidor de e-mail do destinatário. Na ausência de registros MX, registros A ou AAAA especificam o host de e-mail diretamente.

A parte local não tem significado para sistemas de retransmissão intermediários — apenas o host final da caixa de entrada a interpreta. Uma única caixa de entrada pode receber e-mail para múltiplos endereços através de aliases, listas de distribuição, sub-addressing e configurações catch-all.

Os cabeçalhos de e-mail e o endereço de envelope podem divergir, o que permite spoofing de e-mail em esquemas de spam e phishing.

## Validação e verificação

Técnicas de validação incluem:

- **Links de verificação**: hyperlinks temporários enviados ao endereço do usuário ativam contas
- **Padrões formais**: orientação da RFC 3696; muitos sites impõem restrições arbitrárias sobre caracteres válidos
- **Ferramentas algorítmicas**: modelos heurísticos e estatísticos para validação em massa
- **Reputação do remetente**: avaliação de confiabilidade baseada em histórico de IP e de endereço
- **Verificação no navegador**: validação de formulário HTML5

Correção sintática não garante que a caixa de entrada exista. Verificação por *callback* checa a existência real da caixa de entrada, mas gera risco de ataques de *directory harvest* e de denúncias de spam.

## Limitações práticas

Apesar de os padrões técnicos permitirem uma ampla gama de caracteres especiais, muitas organizações restringem as opções. O Windows Live Hotmail, por exemplo, aceita apenas alfanuméricos, pontos, underscores e hífens. Isso reflete uma prática de mercado que prioriza interoperabilidade sobre conformidade estrita com a especificação.

A RFC 5321 recomenda que hosts "evitem definir caixas de entrada" que exijam o formato quoted-string, reconhecendo que endereços entre aspas, embora válidos, permanecem incomuns em implementações do mundo real.
