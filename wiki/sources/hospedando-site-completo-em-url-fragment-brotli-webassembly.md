---
type: source
title: "Hospedando um Site Completo Dentro de uma URL (Fragment + Brotli + WebAssembly)"
aliases: ["site inteiro na url", "hospedagem sem servidor via fragment", "brotli wasm url hosting", "gambiarra site na url michel leonardo"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/hospedando-site-completo-em-url-fragment-brotli-webassembly.md
source_url: ""
author: "Michel Leonardo"
date_published: ""
date_ingested: 2026-08-28
source_count: 0
tags: [xss, webassembly, brotli, golang, tinygo, base64, url, fragment-identifier, gambiarra, hospedagem-sem-servidor]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo de Michel Leonardo (YouTube) parte de um ataque [[wiki/concepts/xss]] reflexivo clássico para levantar a pergunta: se o navegador executa um script escondido na URL, será que aceita renderizar uma página inteira? A resposta é sim — usando o [[wiki/concepts/fragment-identifier-url]] (a parte depois do `#`, que nunca é enviada ao servidor e tolera até ~2 MB no Firefox) como "disco" para guardar um site HTML/CSS/JS minificado, comprimido com [[wiki/concepts/brotli]] e codificado em [[wiki/concepts/base64-encoding]] (variante URL-safe). Como não há servidor para mandar o header `Content-Encoding: br`, o navegador se recusa a descomprimir nativamente — a solução é escrever o próprio descompressor Brotli em Go, compilá-lo para [[wiki/concepts/webassembly]] via TinyGo e rodá-lo no cliente via `syscall/js`. Um esquema de "multipart" (inspirado em jogos que pediam para trocar de CD) contorna o limite de 2 MB dividindo o payload em vários links quando necessário. É uma demonstração técnica funcional de hospedagem estática sem servidor, sem nuvem e sem custo — não um exploit contra terceiros.

## Key Claims

**Claim:** XSS reflexivo funciona porque o servidor devolve o input do usuário (ex.: parâmetro de busca na URL) direto na resposta HTML sem sanitizar, e o navegador da vítima executa esse conteúdo como código por confiar na origem.
**Evidence:** Analogia do "robô que só repete o que recebe" e exemplo do campo de busca refletindo `<script>alert(1)</script>` na página de resultado.
**Confidence:** alta — consistente com a definição já estabelecida em [[wiki/concepts/xss]] e com a categoria "Reflected XSS" documentada em `references/appsec-attacks-deep.md` (skill `tech-mentor-security`).

**Claim:** Servidores web (ex.: Nginx) limitam o tamanho de parâmetros de query string a poucos KB (4–8 KB citados no vídeo), especificamente como mitigação contra DDoS — o que torna parâmetros de URL inviáveis para carregar um payload do tamanho de um site completo.
**Evidence:** Citado como motivação direta para abandonar query parameters e migrar para o fragment identifier.
**Confidence:** média-alta — o limite de tamanho de header/URL em servidores como Nginx é real e configurável (`large_client_header_buffers`), mas o vídeo não cita a diretiva exata nem uma fonte primária da documentação do Nginx; o valor "4-8 KB" é uma generalização, não uma constante universal.

**Claim:** O fragment identifier (`#...`) de uma URL nunca é enviado ao servidor pelo navegador — é resolvido inteiramente client-side — e navegadores modernos como o Firefox toleram até ~2 MB de dados ali antes de erro.
**Evidence:** Comportamento citado como conhecido/testado empiricamente pelo autor; é também a premissa central que viabiliza toda a técnica (sem ela, o resto do pipeline não faz sentido).
**Confidence:** alta quanto ao mecanismo (não-envio do fragment ao servidor é comportamento padrão de HTTP/browser, coerente com RFC 3986 e com o vetor de DOM XSS já documentado via [[wiki/sources/xss-cross-site-scripting-luiz-viana]]); o número exato de "2 MB" é afirmação do autor sem citação de spec formal — navegadores não publicam um limite fixo garantido para tamanho de URL, então tratar como ordem de grandeza observada, não constante documentada.

**Claim:** O navegador só ativa a descompressão nativa de Brotli quando o servidor envia o header HTTP `Content-Encoding: br` junto do conteúdo — sem esse header (por exemplo, por não haver servidor algum, como neste projeto), o conteúdo comprimido em Brotli fica ilegível para o navegador mesmo que o algoritmo seja suportado nativamente.
**Confidence:** alta — mecanismo de negociação de content-encoding é comportamento documentado do protocolo HTTP, e a lacuna descrita (sem servidor, sem header, sem auto-descompressão) é logicamente necessária dado o resto do projeto.

**Claim:** Descomprimir Brotli em JavaScript puro, no cliente, é inviável para payloads grandes porque a computação é densa e roda numa única thread — trava a aba do navegador ("página não responde"); a solução adotada foi implementar o descompressor em Go e compilá-lo para WebAssembly via TinyGo, comunicando com o JavaScript via `syscall/js`.
**Evidence:** Descrição do pipeline completo: função Go decoder exposta via `js.Global().Set("decoder", ...)`, necessidade de um `select{}` vazio ao final do `main()` para não encerrar o programa e perder a função registrada, e inclusão obrigatória do `wasm_exec.js` do TinyGo como glue code para o navegador saber executar o `.wasm`.
**Confidence:** alta quanto ao mecanismo do `syscall/js` (consistente com a forma documentada de interoperabilidade Go↔JS em Wasm); a afirmação de que "JS puro trava" é plausível dado que JS é single-threaded, mas o vídeo não apresenta benchmark comparativo — é uma justificativa de design, não uma medição.

**Claim:** Base64 padrão não pode ser usado direto numa URL porque usa `+`, `/` e `=`, que têm significado estrutural na URL e quebram o link; a solução é Base64URL, que troca esses caracteres por `-`/`_` e descarta o padding.
**Confidence:** alta — comportamento padrão e bem documentado de codificação binary-to-text em URLs (RFC 4648 §5).

**Claim:** Quando o payload comprimido excede o limite prático do fragment identifier (~2 MB), a solução é fragmentar o conteúdo em múltiplos links marcados como partes sequenciais ("multipart"), que o JavaScript da página reconstrói na memória do navegador antes de descomprimir.
**Evidence:** Analogia com jogos antigos que pediam troca de CD quando o conteúdo excedia a capacidade de uma mídia.
**Confidence:** alta quanto ao mecanismo descrito (é uma escolha de engenharia direta, sem alegação técnica arriscada); não testado quanto a robustez (ex.: o que acontece se o usuário colar as partes fora de ordem) — não abordado na fonte.

## Entities & Concepts Touched

- [[wiki/entities/michel-leonardo]]
- [[wiki/concepts/xss]]
- [[wiki/concepts/fragment-identifier-url]]
- [[wiki/concepts/brotli]]
- [[wiki/concepts/webassembly]]
- [[wiki/concepts/base64-encoding]]
- [[wiki/concepts/compactacao-de-texto]]
- [[wiki/concepts/waf]]
- [[wiki/concepts/attack-surface]]

## Open Questions

- O vídeo não cita a fonte primária/URL do guia de blog de "Artur C" usado para viabilizar TinyGo + Wasm — não é possível verificar ou linkar essa referência.
- Não há discussão de como a técnica se comporta com SEO, compartilhamento social (crawlers de preview não executam JS/Wasm) ou acessibilidade — o site só existe depois de o navegador rodar o pipeline completo no cliente.
- Falta um teste explícito de limite superior: quantos "CDs"/partes o esquema multipart suporta na prática antes de ficar inviável para um humano colar manualmente.

## Raw Quotes

> "O robô não filtra o texto, ele só repete o que recebe."

> "Tudo que vem depois desse hashtag nunca é enviado pro servidor. O navegador simplesmente não manda."

> "A gente tá com pacote comprimido nas mãos, mas o navegador cruza os braços e se recusa a descomprimir."
