---
type: source
title: "Como um Painel Admin de Site 'Vibe Coded' é Invadido em Segundos (Burp, ffuf, Hydra)"
aliases: ["brute force painel admin pizzaria", "invasao painel admin vibe coding", "burp ffuf hydra brute force login"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/brute-force-painel-admin-vibe-coding-pizzaria-burp-ffuf-hydra.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-09-08
source_count: 0
tags: [pentest, brute-force, credential-stuffing, user-enumeration, rate-limiting, account-lockout, mfa, captcha, vibe-coding, attack-surface, burp-suite, ffuf, hydra, dirsearch]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo de laboratório autorizado (autor/canal não identificados) usa como pretexto um site fictício de pizzaria gerado por IA ("vibe coded", com painel administrativo pedido explicitamente no prompt) para demonstrar, ponta a ponta, como um painel admin não linkado publicamente é encontrado por fuzzing de diretórios (dirsearch) e depois invadido por brute force de senha usando três ferramentas equivalentes — Burp Intruder, ffuf e Hydra —, todas habilitadas pela mesma falha de origem: mensagens de erro de login diferentes para "usuário não existe" vs. "senha incorreta" (user enumeration), sem rate limit, sem account lockout, sem CAPTCHA e sem MFA. Fecha com seis mitigações padrão de defesa contra brute force online.

## Key Claims

**Claim:** Pedir a uma IA generativa "um site de pizzaria com painel para gerenciar pedidos" tende a produzir exatamente o que foi pedido — inclusive o painel exposto — sem os controles de acesso e anti-automação que o pedido não mencionou.
**Evidence:** O autor descreve o fluxo de prompt → site funcional publicado em menos de um minuto, e enquadra o problema como "a IA é treinada para te dar aquilo que você pediu, não aquilo que você precisa" — o código gerado "é educado demais com estranhos": responde a qualquer requisição bem formada, sem julgar intenção.
**Confidence:** média-alta como enquadramento qualitativo (consistente com o padrão já documentado em [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]); não há medição quantitativa nesta fonte.

**Claim:** O painel administrativo (`/admin`, redirecionado a partir de `/dashboard`) não estava linkado em nenhuma página pública do site, mas foi descoberto em segundos por fuzzing de diretórios (dirsearch) contra uma wordlist de conteúdo web comum.
**Evidence:** Comando demonstrado (`dirsearch -u <alvo> -w .../Web-Content/<wordlist>.txt`) contra uma wordlist do pacote SecLists retorna dois caminhos: `admin` e `dashboard`. `/dashboard` redireciona para `/admin`, confirmando o painel ativo e acessível sem autenticação prévia para carregar a tela de login.
**Confidence:** alta — mecanismo padrão de fuzzing de diretórios, tecnicamente idêntico ao já registrado em [[wiki/concepts/attack-surface]] via [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] (mesma ferramenta, dirsearch, usada para achar um `.env`).

**Claim:** A tela de login do painel vaza qual usuário existe através de mensagens de erro distintas — "usuário não encontrado" vs. "senha incorreta" — permitindo user enumeration antes mesmo de qualquer tentativa de quebra de senha.
**Evidence:** Teste manual demonstrado: usuário `teste` + senha qualquer → "usuário não encontrado"; usuário `admin` (sugerido pelo placeholder do próprio campo) + senha qualquer → "senha incorreta". A diferença de resposta confirma que `admin` é uma conta válida.
**Confidence:** alta — comportamento observado diretamente na demonstração, e é uma categoria de falha conhecida (resposta não genérica de autenticação).

**Claim:** Com o usuário confirmado e nenhuma defesa de rate limit, account lockout, CAPTCHA ou MFA em vigor, a senha do admin foi encontrada por brute force em três ferramentas diferentes (Burp Intruder, ffuf, Hydra), todas usando a mesma wordlist de senhas e o mesmo sinal de sucesso: a ausência da frase de erro (ou, no caso do Burp, um status code 302 de redirecionamento em vez de 200).
**Evidence:** Burp Intruder — ataque Sniper variando só o parâmetro `password`, com Grep Match na string de erro; uma única requisição retorna 302 sem a frase de erro, revelando a senha correta. ffuf — requisição do Burp exportada como arquivo, campo de senha substituído por `FUZZ`, rodado com `-w <wordlist> -fr "senha incorreta"` (filtra da saída qualquer resposta que contenha a frase de erro, sobrando só o acerto). Hydra — `hydra -l admin -P <wordlist> -s 8080 127.0.0.1 http-post-form "/admin:username=^USER^&password=^PASS^:senha incorreta"`, usando a própria frase de erro como critério de falha. As três ferramentas convergem para a mesma senha e confirmam login válido no painel administrativo completo (faturamento, usuários, pedidos).
**Confidence:** alta — demonstração técnica direta e reproduzível, com sintaxe de comando explicada parâmetro a parâmetro para as três ferramentas.

**Claim:** Seis mitigações eliminam ou reduzem drasticamente essa classe de ataque: rate limiting, account lockout, CAPTCHA, mensagens de erro genéricas (não diferenciar "usuário inexistente" de "senha incorreta"), MFA, e política de senha forte.
**Evidence:** Cada mitigação é justificada individualmente: rate limit e lockout atacam o volume de tentativas; CAPTCHA dificulta automação (o autor reconhece que "na maioria das vezes" dá para contornar, mas ainda assim vale a pena); resposta genérica dificulta (não elimina) user enumeration; MFA protege mesmo com credenciais corretas comprometidas, pois depende de um fator sob controle exclusivo do usuário; senha forte reduz o espaço de busca efetivo do brute force.
**Confidence:** alta como lista de controles — é o conjunto padrão de defesa contra brute-force online, já presente e detalhado em [[wiki/concepts/ataque-online-vs-offline-senha]] e [[wiki/concepts/rate-limiting]].

## Entidades e Conceitos Tocados

- [[wiki/concepts/attack-surface]]
- [[wiki/concepts/rate-limiting]]
- [[wiki/concepts/ataque-online-vs-offline-senha]]
- [[wiki/concepts/mfa-multifator-autenticacao]]
- [[wiki/concepts/account-takeover]]
- [[wiki/concepts/vibe-coding]]
- [[wiki/concepts/autenticacao-e-autorizacao]]
- [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]]

## Conexão com fontes existentes

Esta fonte é o par técnico de [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]: as duas usam exatamente o mesmo pretexto narrativo (aplicação "vibe coded" com painel/funcionalidade pedida explicitamente ao prompt, sem controles de segurança que o prompt não mencionou) e a mesma primeira ferramenta de recon (dirsearch, fuzzing de diretórios). A diferença é o alvo da cadeia: a fonte anterior explora IDOR/`.env` exposto até RCE; esta fonte foca inteiramente em **brute force de login online** — ela é a demonstração prática e ferramental que [[wiki/concepts/ataque-online-vs-offline-senha]] só descrevia de forma teórica antes desta ingestão (o conceito já existia com uma fonte, mas sem exemplo de ferramenta real rodando o ataque; agora tem três: Burp Intruder, ffuf, Hydra).

Também reforça [[wiki/concepts/rate-limiting]] e [[wiki/concepts/attack-surface]] com um caso concreto onde a ausência combinada de rate limit + mensagens de erro genéricas é suficiente para tornar a senha do admin trivialmente descobrível, independente de qual ferramenta de brute force é usada — a defesa (ou sua ausência) é agnóstica à ferramenta do atacante.

## Open Questions

- **Autor/canal não identificado no texto da transcrição.** Sem nome de apresentador ou canal, não é possível criar entidade nem verificar se a wordlist "menções ao curso Early Access" aponta para o mesmo criador de outra fonte já na wiki (nenhuma correspondência óbvia encontrada nas entidades existentes).
- **Wordlists específicas usadas não são nomeadas com precisão** — o autor promete indicar as "melhores" wordlists ao final, mas a transcrição fornecida não captura essa parte explicitamente (referências genéricas a SecLists, `dark` como nome de arquivo de wordlist de senha usado nos exemplos).
- **Ataque testado apenas contra usuário `admin` já assumido como válido** — o vídeo menciona que, num cenário real, seria necessário primeiro rodar brute force nos usuários para mapear contas válidas via diferença de resposta, mas não demonstra essa etapa (pula direto para brute-force de senha com usuário fixo).
