---
type: source
title: "4 Hábitos Ruins de Programador (e Como Corrigir)"
aliases: ["hábitos ruins dev", "bad habits programmer", "for web developers artigo"]
date_created: 2026-04-22
date_updated: 2026-04-22
source_file: /home/nemomartins/Documentos/new/dev-study/raw/habitos-ruins-de-programador.md
source_url: ""
author: "Felipe (canal YouTube) comentando artigo de 'Dano' — 'For Web Developers'"
date_published: 2026-04-22
date_ingested: 2026-04-22
source_count: 0
tags: [carreira, hábitos, craftsmanship, testes, commits, definição-de-pronto, liderança]
skill: tech-mentor-leadership
status: stable
---

# 4 Hábitos Ruins de Programador (e Como Corrigir)

## TL;DR

Transcrição de vídeo comentando artigo "For Web Developers" (autor "Dano"). Apresenta 4 hábitos ruins que prejudicam a qualidade e produtividade do dev — não relacionados à falta de conhecimento técnico, mas a comportamentos e processos. Framing central: você não **é** um programador ruim, você pode **estar** com hábitos ruins.

**Origem:** artigo "For Web Developers" por "Dano" (link na descrição do vídeo original). Speaker: Felipe (mesmo canal dos vídeos anteriores).

---

## Os 4 Hábitos

| # | Hábito Ruim | Correção |
|---|---|---|
| 1 | Dizer sim para tudo | Calibrar compromissos; deixar pessoas assumirem riscos próprios |
| 2 | Definição fraca de "pronto" | Código legível + documentado + testado = pronto |
| 3 | Não testar o próprio código | Escrever testes automatizados cobrindo happy path E erros |
| 4 | Commits/PRs gigantescos | Commit atômico: alteração de código + teste que a valida juntos |

---

## Claims Principais

| Claim | Evidência | Confiança |
|---|---|---|
| Dizer sim para tudo fragmenta o foco e derruba produtividade | Cada interrupção tem custo de retomada de contexto | Alta |
| Sempre dar a resposta cria dependência — inibe surgimento de líderes | Pessoas param de pensar por conta própria quando sabem que podem terceirizar | Alta |
| Código que só você entende não está pronto — é rascunho | Se outro dev não consegue entender facilmente, precisa de refatoração | Alta |
| Testar só o caminho feliz é equivalente a concordar com a própria opinião | Você precisa de evidência contrária, não confirmação | Alta |
| PR gigante desanima revisão — ninguém sabe onde começar | Sensação de não saber quando vai terminar inibe até o início | Alta |
| Commit atômico = alteração + teste que a valida, na mesma unidade | Cada commit vira uma unidade funcional com valor próprio | Alta |

---

## Framing importante da source

> "Você não é um programador ruim. Você pode ter hábitos de um programador ruim."

Distinção entre **ser** e **estar** — identidade vs. comportamento. Hábitos são mutáveis; identidade é fixa. Framing que remove paralisia e aponta para ação.

---

## Conceitos Abordados

- [[dizer-sim-para-tudo]]
- [[definicao-de-pronto]]
- [[testar-proprio-codigo]]
- [[atomic-commits]]

## Conceitos Relacionados (wiki existente)

- [[mentoria-tecnica]] — destravar líderes vs. criar dependência
- [[flexibilidade-tecnica]] — não ser o único ponto de desempate
- [[extreme-ownership]] — calibrar risco por nível de senioridade

---

## Quotes Relevantes

> "Uma promessa é uma dívida. O tempo vai estourar e os juros são extremamente caros."

> "Quando disser sim para outros, certifique-se de não estar dizendo não para si mesmo." — Paulo Coelho (citado no artigo original)

> "Testar só o caminho feliz é tão besta quanto concordar com a sua própria opinião."

> "Transforme o commit numa unidade de alteração funcional, não num diário."

---

## Questões Abertas

- Qual o tamanho ideal de um PR? Existe um número de linhas como referência?
- Como dizer não sem parecer não-colaborativo numa empresa onde a cultura é de "sempre ajudar"?
