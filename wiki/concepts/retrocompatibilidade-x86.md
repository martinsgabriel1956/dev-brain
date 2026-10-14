---
type: concept
title: "Retrocompatibilidade do x86"
aliases: ["backward compatibility x86", "legado Intel 8080"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_count: 1
tags: [lang-systems, x86, intel, retrocompatibilidade, historia, hardware]
skill: lang-systems
status: draft
---

# Retrocompatibilidade do x86

O x86 é historicamente retrocompatível por motivos econômicos: há programas dos anos 80 rodando dos quais **não existe mais código-fonte, só o binário**, e ninguém vai recompilá-los; por isso muitas instruções remetem ao 8080 e a processadores Intel dos anos 70/80. Importante sobretudo em indústrias tradicionais com dinheiro para financiar a compatibilidade ([[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]). Exemplo de [[wiki/concepts/dependencia-de-caminho-em-tecnologia]] e de por que o [[wiki/concepts/assembly]] só é portável dentro da mesma família de [[wiki/concepts/isa-instruction-set-architecture|ISA]] (x86 32 → x64, mas não → ARM/RISC-V). [external] linhagem 8080 → 8086 é conhecida; "muitas instruções" é aproximação do autor.

## Key sources

- [[wiki/sources/por-que-c-e-alto-nivel-abstracao-portabilidade-hardware]]
