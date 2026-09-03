---
type: concept
title: "WebAssembly (Wasm)"
aliases: ["webassembly", "wasm", "tinygo", "syscall/js", "go para wasm"]
date_created: 2026-08-28
date_updated: 2026-08-28
source_count: 1
tags: [webassembly, wasm, golang, tinygo, performance, browser, compiladores]
skill: tech-mentor-security
status: draft
---

# WebAssembly (Wasm)

Formato binário de baixo nível, pré-compilado, que o navegador executa direto na CPU sem passar pela interpretação/JIT do motor JavaScript. Existe como alvo de compilação para código escrito em linguagens como C, Rust ou Go — não é escrito à mão.

## Por que existe (o gargalo que resolve)

JavaScript é single-threaded e sua VM não é otimizada para computação numérica pesada e sustentada (ex.: matemática densa de um algoritmo de compressão). Cargas assim travam a thread principal e o navegador acusa "página não responde". Wasm entrega instruções já compiladas para baixo nível — o navegador não perde tempo traduzindo, executa direto, muito mais rápido para esse tipo de carga.

## Compilando Go para Wasm com TinyGo

O compilador Go padrão gera Wasm, mas com overhead grande (runtime completo embutido). **TinyGo** é um compilador alternativo pensado para ambientes restritos (microcontroladores como Arduino, e Wasm), gerando binários bem menores.

A ponte entre o Go compilado e o JavaScript do navegador é a biblioteca **`syscall/js`**:

- Uma função Go é empacotada com `js.FuncOf(...)` para virar chamável a partir do JavaScript.
- `js.Global()` acessa o objeto `window` (escopo global da página no navegador) — é assim que a função Go registrada fica acessível, por exemplo, como `window.minhaFuncao(...)`.
- O programa Go precisa de um `select{}` vazio no final do `main()` para não terminar — se a goroutine principal sair, o runtime encerra e o JavaScript perde a capacidade de chamar qualquer função registrada.
- É necessário incluir também o arquivo de runtime `wasm_exec.js` (fornecido pelo TinyGo) junto do `.wasm` gerado — ele funciona como a camada de interpretação/glue code entre o binário Wasm e o navegador; sem ele, o navegador não sabe como carregar e executar o `.wasm`.

## Caso de uso documentado nesta wiki

[[wiki/sources/hospedando-site-completo-em-url-fragment-brotli-webassembly]] usa exatamente esse pipeline (Go → TinyGo → Wasm + `syscall/js`) para rodar, no navegador e sem servidor, um descompressor de [[wiki/concepts/brotli]] — necessário porque o navegador só descomprime Brotli nativamente quando o servidor manda o header HTTP `Content-Encoding: br`, o que não existe num site inteiramente hospedado dentro do [[wiki/concepts/fragment-identifier-url]] de uma URL (não há servidor envolvido, então não há header algum).

A documentação oficial do TinyGo para esse fluxo é escassa; a fonte cita ter recorrido a um guia de blog de terceiros para viabilizar a implementação — um ponto de fricção real, não hipotético, de usar essa combinação de ferramentas.
