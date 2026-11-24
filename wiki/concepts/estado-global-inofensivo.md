---
type: concept
title: "Estado Global Inofensivo (Constantes e Config)"
aliases: ["constantes globais", "config read-only", "global aceitável"]
date_created: 2026-10-06
date_updated: 2026-11-24
source_count: 2
tags: [estado-global, configuracao, imutabilidade, constantes]
skill: tech-mentor-backend
status: draft
---

# Estado Global Inofensivo (Constantes e Config)

Nem todo estado global é ruim: se nada o altera, é só constante. Exemplos do vídeo: `port = 3000`, `MAX_UPLOAD_SIZE`, configuração exportada de módulo.

- Único risco: outro ponto do código mutar o valor.
- Versão defensiva: carregar a config **uma vez** no start e expor como objeto **read-only** ([[wiki/concepts/imutabilidade]]). Opinião do autor: geralmente desnecessário; pode valer com time/IA que mude config sem critério.

Critério prático: o valor é mutável por requisição? Então é [[wiki/concepts/estado-global-em-servidor]] problemático. Constante de processo, não.

## No JavaScript Ninja, semana 4, vídeo 03 (Fernando Daciuk)

Em [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]], o global "é algo ruim" sem ressalva: conflito de nomes e memória presa. A exceção desta página (constante, nunca mutada) não aparece; ela não colide se tiver nome único e não cresce ([[wiki/concepts/poluicao-do-escopo-global]]).

## Key sources

- [[wiki/sources/estado-global-stateless-side-effects-reprodutibilidade-galego]]
- [[wiki/sources/javascript-ninja-escopo-de-variaveis-e-funcoes]]: JavaScript Ninja, semana 4, vídeo 03: global como erro de design, sem a exceção da constante
