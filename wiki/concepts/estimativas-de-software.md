---
type: concept
title: "Estimativas de Software"
aliases: ["software estimation", "por que subestimamos tarefas", "estimativa de tarefas"]
date_created: 2026-07-29
date_updated: 2026-08-10
source_count: 2
tags: [carreira, gestao-de-projetos, planejamento, produtividade]
skill: tech-mentor-leadership
status: draft
---

# Estimativas de Software

## TL;DR

Segundo [[wiki/sources/14-habitos-desenvolvedores-altamente-produtivos]] (Hábito 11, "Não subestime"), desenvolvedores subestimam tarefas cronicamente por cinco razões comportamentais recorrentes — não por falta de técnica. A fonte cita o livro *Software Estimation: Demystifying the Black Art* de Steve McConnell como referência técnica para mitigar o problema, mas reconhece: estimativa 100% precisa é impossível, o objetivo realista é se aproximar cada vez mais dela.

## As cinco razões para subestimar (segundo a fonte)

1. **Queremos impressionar os outros** — estimar baixo para parecer mais rápido/competente do que estimar de forma realista.
2. **Esquecemos que não é só código** — a estimativa mental vai direto para "tempo de codar", ignorando compilação, testes, documentação, reuniões, resolução de conflitos, revisão de comentários.
3. **Não nos concentramos em uma coisa só** — trabalhar em múltiplos projetos simultâneos gera custo cognitivo real de reorientação de contexto a cada troca.
4. **Acreditamos que todos são iguais** — tratar estimativa como tempo médio de equipe, ignorando que é uma medida estritamente individual (o tempo que a pessoa X leva não é o tempo que a pessoa Y leva para a mesma tarefa).
5. **Não conseguimos lidar com a pressão** — pressão vinda de cliente/gerente/CTO é repassada para baixo, e é difícil comunicar que "não vai ser tão rápido assim" sob essa pressão.

## Recomendações práticas (McConnell, citado pela fonte)

- Dividir tarefas grandes em unidades de no máximo 2 dias de esforço — melhora precisão.
- Estimar em três cenários: pior caso, caso mais provável, melhor caso.
- Ao usar linguagem/ferramenta nova (vs. familiar), adicionar 20–40% de esforço extra.
- Documentar e comunicar as suposições por trás da estimativa, não só o número final.
- Para projetos pequenos, estimativa "de baixo para cima" (feita por quem vai executar o trabalho) tende a ser mais precisa que estimativa "de cima para baixo".
- Tratar a conversa de estimativa como resolução conjunta de problema com os stakeholders, não como negociação adversarial — "você e as partes interessadas estão do mesmo lado da mesa".

## Nota sobre feedback loop

A fonte destaca um ponto frequentemente ignorado: sem medir o tempo real gasto e comparar com a estimativa original, não existe *feedback loop* — e sem feedback loop, a habilidade de estimar não melhora com a experiência, só a ilusão de que melhora.

## Relação com outros conceitos

- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]] — story points/T-shirt sizing/poker planning são citados na fonte atual como técnicas alternativas de estimativa, sem escolha de uma única "correta"; a outra fonte aprofunda por que forçar meta numérica de story points corrompe a métrica (Lei de Goodhart).
- [[wiki/concepts/tech-debt-como-ferramenta]] — subestimar cronicamente é um dos gatilhos comuns de dívida técnica não deliberada (pressão de prazo forçando atalhos).

## Key Sources

- [[wiki/sources/14-habitos-desenvolvedores-altamente-produtivos]] — Hábito 11
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — foco complementar: mensurar o *erro* da estimativa (gap planejado × entregue por sprint) importa mais do que acertar a estimativa; sem isso a empresa não sabe sua capacidade real
