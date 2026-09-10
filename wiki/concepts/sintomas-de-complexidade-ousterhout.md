---
type: concept
title: "Sintomas de Complexidade (Ousterhout)"
aliases: ["change amplification", "cognitive load burden", "unknown unknowns", "sintomas de complexidade de software"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_count: 1
tags: [complexidade, design, ousterhout, arquitetura, deteccao]
skill: tech-mentor-backend
status: stub
---

# Sintomas de Complexidade (Ousterhout)

## TL;DR

Três manifestações práticas usadas por [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 2) para reconhecer que um sistema está complexo demais, mesmo sem uma métrica objetiva de complexidade: **change amplification**, **cognitive load** e **unknown unknowns**. São os sintomas — não a causa (dependências + obscuridade); servem como checklist prático para saber se um trecho de código precisa de atenção.

## Os três sintomas

- **Change amplification** — uma mudança que parecia logicamente localizada num único pedaço do código exige, na prática, alterar vários outros lugares (classes, arquivos de configuração) com os quais havia dependência oculta. É o sintoma mais visível para quem chega numa base de código nova: a mudança "devia ser simples" e não é.
- **Cognitive load** — quanto conhecimento um dev precisa ter na cabeça para completar uma tarefa com segurança. Interfaces com muitos métodos, parâmetros com efeitos colaterais não óbvios, ou padrões inconsistentes aumentam o cognitive load mesmo quando o código é curto.
- **Unknown unknowns** — o pior dos três: não é óbvio quais partes do código precisam ser mudadas, nem quais informações são necessárias para fazer a mudança com segurança. Ao contrário dos outros dois, é difícil de perceber até já ter causado um bug.

## Como reconhecer na prática

[[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] discute change amplification e (pelo caminho inverso) o sintoma de conhecimento mal documentado como os primeiros sinais que dois engenheiros experientes procuram ao entrar numa base de código nova: se uma mudança que parecia isolada em uma classe se espalha para dependências desconhecidas, isso é change amplification na prática; se o tempo de onboarding é longo porque "a documentação sou eu" (ninguém mais sabe explicar o sistema), isso é sintoma de unknown unknowns não resolvidos — o conhecimento necessário para mudar o sistema com segurança nunca foi capturado em lugar nenhum, nem no código, nem em documentação.

## Relação com outros conceitos

- [[wiki/concepts/ocultamento-de-informacao]] — vazamento de informação (information leakage) é uma causa estrutural comum de change amplification: se a mesma decisão de design está espalhada por vários módulos, mudar essa decisão exige tocar em todos eles.
- [[wiki/concepts/modulo-profundo]] — módulos rasos aumentam cognitive load, porque o leitor precisa rastrear mais peças pequenas simultaneamente.
- [[wiki/concepts/red-flags-de-design]] — os red flags catalogados no livro são heurísticas concretas para detectar as causas por trás desses três sintomas antes que eles apareçam na prática.
- [[wiki/concepts/comprehension-debt]] — cognitive load e comprehension debt descrevem fenômenos próximos, um do lado do design humano-clássico (Ousterhout) e outro do lado de código gerado por IA.

## Key Sources

- [[wiki/sources/filosofia-design-software-podcast-eduardo-matos-otavio-santana-mauricio-linhares]] — change amplification e unknown unknowns discutidos como os primeiros sinais práticos de complexidade crescente, com exemplos de onboarding e mudança em base de código nova
