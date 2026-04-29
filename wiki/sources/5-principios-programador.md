---
type: source
title: "5 Princípios Que Vão Mudar Você Como Programador"
aliases: ["5 princípios programador", "logs mais importantes que código", "usuários quebram tudo"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 0
tags: [carreira, craftsmanship, logging, testes, tech-debt, naming, staging, producao]
skill: tech-mentor-leadership
status: stable
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/5-principles-that-changed-me-as-a-programmer.md"
source_url: ""
author: "desconhecido (vídeo YouTube)"
date_published: ""
date_ingested: "2026-04-29"
---

## TL;DR

5 princípios aprendidos na dor — não em faculdade. O fio condutor é realidade vs. teoria: o que importa em produção diverge completamente do que se ensina em cursos. Cobre logging estruturado, comportamento de usuários, tech debt deliberado, naming e paridade de ambientes.

---

## Reivindicações Principais

**Claim:** Logs são mais importantes que o código — quando algo quebra em produção, logs determinam se você resolve em minutos ou horas.
**Evidência:** Autor relata 6 horas de debug via SSH + print statements por falta de logging. Problema teria sido trivial com logs estruturados contendo contexto.
**Confiança:** Alta — experiência direta, padrão amplamente validado pela indústria.

**Claim:** Usuários quebrarão toda suposição não testada — edge cases "impossíveis" se tornam comuns assim que alguém começa a usar.
**Evidência:** Emoji em campo de nome derrubou formulário simples. Usuários também submetem SQL injection, strings vazias, spam de cliques, e usam browsers legados.
**Confiança:** Alta — padrão universal de QA.

**Claim:** Tech debt deliberado é uma ferramenta legítima — velocidade importa mais que perfeição na fase de validação de ideias.
**Evidência:** Autor passou semanas arquitetando features que foram descartadas pelo negócio. Conclusão: "A maioria das features falha. Não construa um palácio para algo que pode ser demolido." Alinhado com o Quadrante de Fowler (Prudente + Deliberado).
**Confiança:** Alta.

**Claim:** Naming é de fato a parte mais difícil do desenvolvimento — nomes ruins compõem dívida cognitiva indefinidamente.
**Evidência:** Função `doStuff` — 2h para descobrir que processa payment webhooks. Nomes como `data`, `info`, `manager` criam ambiguidade crescente.
**Confiança:** Alta — citação clássica de Phil Karlton: "There are only two hard things in Computer Science: cache invalidation and naming things."

**Claim:** Ambiente local é uma mentira — produção tem carga, dados, latência e sistema operacional que o laptop nunca terá.
**Evidência:** Deploy funcionou localmente, quebrou em prod: 1 usuário vs. milhares; 10 linhas de teste vs. milhões de rows; localhost vs. latência real; OS local vs. OS diferente.
**Confiança:** Alta — problema clássico de staging parity.

---

## Os 5 Princípios

| # | Princípio | Regra Prática |
|---|---|---|
| 1 | Logs > código | Logue inputs, outputs e erros com contexto |
| 2 | Usuários quebram tudo | Teste o impossível — vazio, null, emoji, concorrência |
| 3 | Tech debt é ferramenta | Ship rápido, refatore se sobreviver |
| 4 | Naming é a parte mais difícil | 5 min no nome = 5h economizadas depois |
| 5 | Local não é produção | Docker + staging + deploy cedo e frequente |

---

## Conceitos

- [[logs-em-producao]] — logs estruturados com contexto como ferramenta de sobrevivência
- [[usuarios-como-agentes-do-caos]] — usuários encontram edge cases que o dev nunca imaginou
- [[tech-debt-como-ferramenta]] — debt deliberado e prudente como estratégia válida
- [[naming]] — nomear claramente como proxy de entendimento do código
- [[paridade-local-producao]] — ambientes locais mentem; staging e Docker aproximam da realidade

---

## Conexões com Outras Sources

- [[habitos-ruins-de-programador]] — hábitos que agravam os 5 problemas acima
- [[9-habitos-programador-junior]] — hábitos que ajudam a evitá-los
- [[conceitos-que-ninguem-ensina]] — princípios práticos que a faculdade não ensina
- [[observabilidade]] — o lado sistêmico do princípio de logging
- [[estilo-de-codigo-convencoes]] — naming e comentários como parte de código legível

---

## Perguntas Abertas

- Qual é o custo mínimo viável de logging para uma aplicação nova sem Prometheus/Grafana?
- Como calibrar quanto tech debt é prudente vs. negligência quando o prazo é real?
- Existe heurística para saber quando um nome está "bom o suficiente"?

---

## Citações

> "O impossível se torna possível no segundo em que alguém chamado Dave começa a digitar."

> "Seu laptop é um mentiroso. É rápido, confiável, perfeito. Produção é lenta, instável, caótica."

> "Se você não consegue nomear algo claramente, você não entende o que esse código faz."
