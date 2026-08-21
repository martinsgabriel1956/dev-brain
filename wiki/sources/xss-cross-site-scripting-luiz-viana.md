---
type: source
title: "XSS Cross-Site Scripting na Prática (Luiz Viana)"
aliases: ["xss na pratica luiz viana", "dvwa xss reflected stored dom", "cross-site scripting demonstracao"]
date_created: 2026-08-19
date_updated: 2026-08-19
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/xss-cross-site-scripting-luiz-viana.md
source_url: ""
date_published: ""
date_ingested: 2026-08-19
source_count: 0
tags: [xss, appsec, dvwa, pentest, bug-bounty, owasp, output-encoding, csp, cookie-theft]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo prático de Luiz Viana (especialista em hacking/pentest) sobre XSS — define os três tipos (reflected, stored, DOM-based) e demonstra, no laboratório DVWA, como cada um se comporta em quatro níveis crescentes de segurança (low/medium/high/impossible). O fio condutor é mostrar filtros de segurança do lado do servidor sendo contornados: troca de tag (`<script>` bloqueada, `<img onerror=...>` não), manipulação de restrição client-side (`maxlength` removido via DevTools) e uso de fragmento de URL (`#`) para manter payload fora da visão do servidor num cenário DOM-based. Fecha reforçando que a mitigação real é sanitização/output encoding, com CSP como camada complementar (e contornável se mal configurado).

## Key Claims

**Claim:** XSS ocorre quando a aplicação insere dados do usuário na página HTML sem validação/sanitização, permitindo que o navegador interprete input como código executável.
**Evidence:** Exemplo do campo de busca ("você pesquisou por notebook") — o servidor reflete o parâmetro de busca diretamente na resposta HTML; substituindo o termo por `<script>alert(1)</script>`, o navegador executa o script como parte legítima da página.
**Confidence:** alta — consistente com a definição já documentada em [[wiki/concepts/xss]] e com `references/appsec-attacks-deep.md` da skill `tech-mentor-security`.

**Claim:** DOM-based XSS é o tipo mais difícil de detectar porque o payload nunca passa pelo servidor — nem logs de servidor nem um WAF conseguem observá-lo.
**Evidence:** No laboratório de seleção de idioma do DVWA, o JavaScript client-side lê o parâmetro da URL e monta o dropdown diretamente no DOM sem nenhuma etapa de servidor envolvida. No nível medium, o filtro que bloqueia `<script>` roda apenas no servidor; usando um fragmento de URL (`#`) — que por definição do protocolo HTTP nunca é enviado na requisição — o payload nunca chega ao filtro, mas ainda é lido e processado pelo JavaScript do navegador.
**Confidence:** alta — mecanismo consistente com a definição de "URL fragment" (RFC 3986) e com a lista de vetores DOM XSS documentada na skill (`innerHTML` vs `textContent`, `location.hash`).

**Claim:** Filtros de sanitização baseados em bloquear a tag `<script>` são insuficientes — tags alternativas com atributos de evento (`<img src=x onerror=...>`, `<body onload=...>`) contornam o filtro e ainda executam JavaScript.
**Evidence:** Em três dos quatro laboratórios demonstrados (DOM medium/high, Reflected medium/high, Stored medium/high), o filtro remove especificamente a substring `<script>` mas deixa passar `<img>`/`<body>` com atributos de evento (`onerror`, `onload`, `onmouseover`), que dispara execução de JS sem nunca conter a palavra "script" na tag.
**Confidence:** alta — mesmo padrão descrito em `references/appsec-attacks-deep.md` (blocklist de tags é frágil; a defesa correta é output encoding/allowlist, não busca por substring).

**Claim:** Restrições de input só no client-side (ex.: atributo HTML `maxlength`) não impedem um payload maior — são contornáveis via DevTools antes mesmo de qualquer requisição ser enviada.
**Evidence:** No Stored XSS nível medium/high do DVWA, o campo de nome tem `maxlength="10"` no HTML; removendo esse atributo pelo inspecionador de elementos, é possível digitar um payload maior que passa a ser processado pelo filtro real (do lado do servidor) normalmente.
**Confidence:** alta — instância específica do princípio geral já documentado em [[wiki/concepts/confiar-no-frontend]] ("toda regra validada só no frontend é contornável"), aqui aplicado a uma restrição de tamanho de campo em vez de uma regra de negócio.

**Claim:** No nível "impossible" do DVWA, a sanitização de fato neutraliza todos os payloads testados (incluindo os que passavam em "high") porque o navegador recebe texto encodado, não código interpretável.
**Evidence:** Nenhum dos payloads (remoção de `maxlength`, `<img onerror>`, `<body onload>`) executa no nível impossible — o vídeo generaliza esse resultado como o critério que define mitigação real: "output encoding" transforma `<`, `>`, `"` em entidades HTML antes de renderizar, e o navegador simplesmente exibe o texto ao invés de interpretá-lo.
**Confidence:** alta — consistente com a seção "Como Prevenir" já documentada em [[wiki/concepts/xss]] (output encoding como defesa primária).

**Claim:** Um cookie de sessão sem a flag `HttpOnly`, ou um token guardado em `localStorage`, é diretamente exfiltrável por um payload de XSS bem-sucedido.
**Evidence:** O vídeo cita `document.cookie` como alvo típico do payload de XSS para roubo de sessão, generalizando para "efetuar qualquer ação com a sessão ativa daquele site" — mesmo mecanismo já documentado em [[wiki/concepts/xss]] (seção "Roubo de Token Via XSS").
**Confidence:** alta — já triangulado por múltiplas fontes prévias na wiki ([[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]], [[wiki/sources/refresh-token-pattern-access-token-de-curta-duracao]]).

**Claim:** Content Security Policy (CSP) é uma camada complementar de defesa contra XSS, mas não substitui sanitização — um CSP mal configurado ainda permite bypass.
**Evidence:** Citado brevemente no fechamento do vídeo, sem exemplo prático de bypass específico (fora do escopo desta demonstração).
**Confidence:** média — claim correta e consistente com a skill, mas não demonstrada tecnicamente na fonte (apenas mencionada).

## Entities & Concepts Touched

- [[wiki/concepts/xss]]
- [[wiki/concepts/dvwa]]
- [[wiki/concepts/bug-bounty]]
- [[wiki/concepts/waf]]
- [[wiki/concepts/confiar-no-frontend]]
- [[wiki/concepts/attack-surface]]
- [[wiki/concepts/sast]]
- [[wiki/concepts/sessoes-http-cookies]]
- [[wiki/concepts/sql-injection]]
- [[wiki/entities/luiz-viana]]
- [[wiki/entities/solyd]]

## Open Questions

- A fonte não demonstra tecnicamente um bypass de CSP mal configurado — apenas menciona que é possível; um exemplo concreto (ex.: `unsafe-inline`, wildcard de domínio) ficaria melhor documentado com uma fonte dedicada.
- Não fica claro no vídeo por que o filtro do DVWA nível medium do Stored XSS bloqueia até tentativas de tag duplicada (`<scr<script>ipt>`) mas ainda deixa passar `<img onerror>` — presumivelmente a blocklist é específica para a substring `script`, mas o código-fonte do laboratório não é mostrado para confirmar.

## Raw Quotes

> "XSS é basicamente quando o atacante consegue injetar código client JavaScript numa página legítima e quando você acessa essa página o código executa no seu navegador como se fosse parte do site."

> "Esse tipo [DOM-based] é especialmente perigoso porque acontece totalmente no lado do cliente, então nem sempre o ataque vai aparecer nos logs do servidor e também um WAF nem conseguiria detectar."

> "O que seria a sanitização: ao invés dele ser mostrado como código, ele seria mostrado como texto encodado — nesse caso aqui ele tá como código, o navegador simplesmente executa."
