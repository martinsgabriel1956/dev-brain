---
type: concept
title: "Lei de Goodhart"
aliases: ["Goodhart's Law", "Goodhart's Law Metrics"]
date_created: 2026-07-28
date_updated: 2026-09-18
source_count: 6
tags: [metrics, engineering-management, tomada-de-decisao]
skill: tech-mentor-leadership
status: stable
---

# Lei de Goodhart

**TL;DR:** "Quando uma medida se torna um alvo, ela deixa de ser uma boa medida." (Charles Goodhart). Qualquer métrica, ao ser transformada em meta cobrada de cima para baixo, cria incentivo para otimizar o número em vez do comportamento real que o número deveria representar.

## Mecanismo

Uma métrica só funciona como sinal enquanto ela é **observada**, não **perseguida**. No momento em que vira alvo formal (bônus, cobrança, meta contratual), as pessoas medidas passam a ter incentivo racional para inflar o número por caminhos que não representam a melhoria real que a métrica pretendia capturar.

## Exemplo Central: Story Points Forçados

Quando um PO ou [[wiki/concepts/scrum-master|Scrum Master]] exige que cada pessoa do time entregue 30–40 [[wiki/concepts/story-points]] por sprint, a métrica deixa de medir complexidade relativa entregue e passa a medir a capacidade do time de inflar estimativas para bater a meta — por exemplo, atribuir 20 pontos a um CRUD que leva três horas. A métrica não desaparece, mas perde toda a capacidade preditiva que tinha (ex.: usar velocity histórica para prever prazos), porque o número deixou de refletir a realidade.

Isso é análogo a manter o gráfico de contribuições do GitHub "verdinho" com commits vazios (apagar/colar código só para gerar atividade) — uma métrica de exibição, não de valor real entregue.

## Como Usar Métricas Sem Cair em Goodhart

- Preferir métricas de **tendência do próprio time ao longo do tempo** a metas absolutas impostas externamente — ver [[wiki/concepts/dora-metrics]], que segue o mesmo princípio (não comparar times entre si, não usar para avaliação individual).
- Deixar a métrica **emergir** do processo (ex.: velocity calculada a partir de estimativas honestas via [[wiki/concepts/planning-poker]]) em vez de definir o número desejado primeiro e forçar o processo a produzi-lo.
- Se uma meta precisa existir, negociá-la com quem vai ser medido por ela, entendendo o impacto real na qualidade e na colaboração do time — não impô-la sem consulta.

## Conceitos Relacionados

[[wiki/concepts/story-points]] · [[wiki/concepts/scrum-master]] · [[wiki/concepts/dora-metrics]] · [[wiki/concepts/planning-poker]]

## Caso IA: métricas de output viram alvo e param de medir qualidade

O mesmo mecanismo aparece ao medir produtividade com IA: contagem de PRs e volume de código são métricas de atividade que a IA infla independente de qualidade. Ao tratá-las como alvo de produtividade, 95% dos devs se *sentem* mais produtivos enquanto a qualidade do código cai — a métrica deixou de medir o que deveria. A defesa é a mesma do resto desta página: medir **outcome**, não output (ver [[wiki/concepts/output-vs-outcome]] e [[wiki/concepts/paradoxo-da-aceleracao]]).

## Caso Não Nomeado: Incentivos Organizacionais Moldando Qualidade de Código

[[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]] descreve o mesmo mecanismo desta página sem usar o vocabulário de Goodhart: se a organização recompensa fechar tickets e cumprir deadline sem avaliar qualidade, e não recompensa redução de complexidade ou boa gestão de dívida técnica, "até bons profissionais vão querer otimizar seu trabalho para se adequar àquilo que é medido pela empresa". É o quarto de quatro fatores não técnicos listados na fonte — ver [[wiki/concepts/fatores-nao-tecnicos-qualidade-de-codigo]] para o framework completo, que trata esse mecanismo como uma causa de código abaixo do potencial do dev, não só de estimativa inflada.

## Caso Mais Amplo: "Torturar Números" Para Validar Metodologias Ágeis

[[wiki/sources/agilidade-manifesto-agil-fabio-akita]] estende o mecanismo desta página além de métricas de time: consultorias que vendem metodologias ágeis frequentemente citam números ("funciona no Google", "funciona no Spotify") sem informar as condições de coleta, repetibilidade ou grupo de controle — o autor compara isso a "numerologia": números que contam a história que se quer ouvir não são prova de nada. É a mesma lógica de Goodhart aplicada não a uma métrica de time específica, mas à validação retórica de processos inteiros por empresas de consultoria.

## Caso Histórico: Números de Sucesso da Motorola Não Sustentaram Sucesso de Longo Prazo

[[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]] traz um caso concreto e histórico do mesmo mecanismo em escala de metodologia de gestão inteira, complementando a crítica já registrada acima (via [[wiki/sources/agilidade-manifesto-agil-fabio-akita]]): a Motorola apresentou números de sucesso reais e expressivos com [[wiki/concepts/six-sigma-dmaic|Six Sigma]] entre 1987–1997 (vendas 5x, lucro 20%/ano), mas isso não garantiu sucesso de longo prazo — a empresa perdeu relevância nas décadas seguintes. O ponto não é que os números fossem falsos ou torturados (diferente do exemplo de story points forçados), mas que **números de sucesso passado, mesmo genuínos, não são garantia de metodologia vencedora indefinidamente** — um ângulo adicional ao mecanismo de Goodhart já documentado nesta página, mais próximo de viés de sobrevivência do que de manipulação direta da métrica.

## Key Sources

- [[wiki/sources/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato]]
- [[wiki/sources/agilidade-manifesto-agil-fabio-akita]] — crítica ao uso de números sem controle metodológico para validar metodologias ágeis inteiras, não só uma métrica isolada — incentivos organizacionais (fechar ticket/cumprir deadline sem medir qualidade) como instância não nomeada da lei
- [[wiki/sources/story-points-po-forcando-30-40-pontos-por-sprint]]
- [[wiki/sources/paradoxo-da-aceleracao-ia-produtividade-metricas]] — métricas de output infladas por IA como caso de Goodhart na era da IA
- [[wiki/sources/por-que-code-bases-degradam-estrategias-code-rot]] — aplica a lei a métricas de qualidade: meta de "100% de cobertura" gera testes inúteis, mas 5% de cobertura ainda é sinal legítimo de subteste (a métrica serve como sinal, não como alvo)
- [[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]] — caso histórico Motorola/Six Sigma: números de sucesso genuínos não garantem sucesso de longo prazo
