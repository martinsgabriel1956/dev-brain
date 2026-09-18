---
type: concept
title: "Tentativa e Erro Como Método Científico"
aliases: ["tentativa e erro sistemática", "PDCA=DMAIC=Scrum=metodo cientifico", "melhoria continua como ciclo universal"]
date_created: 2026-09-18
date_updated: 2026-09-18
source_count: 1
tags: [metodo-cientifico, melhoria-continua, agile, engineering-management, epistemologia]
skill: tech-mentor-leadership
status: stub
---

# Tentativa e Erro Como Método Científico

**TL;DR:** Tese central de [[wiki/entities/fabio-akita]]: [[wiki/concepts/ciclo-pdca-deming|PDCA]] (Deming), DMAIC ([[wiki/concepts/six-sigma-dmaic|Six Sigma]]), Kaizen (Toyota), Sprint/retrospectiva ([[wiki/concepts/scrum-master|Scrum]]) e o método científico clássico são, estruturalmente, **o mesmo ciclo** de resolução de problemas desconhecidos — e esse ciclo, popularmente chamado de "tentativa e erro", é o único método conhecido para resolver qualquer problema cuja solução não é conhecida de antemão.

## O Ciclo Comum

Todos os modelos citados compartilham a mesma estrutura:

1. Observar/definir o problema
2. Formular uma hipótese testável (falseável)
3. Executar uma ação (contramedida de curto prazo)
4. Medir/checar o resultado contra a hipótese
5. Ajustar a teoria/hipótese e repetir

No método científico formal, isso aparece como: observação sistemática → teoria científica (fatos + hipóteses testáveis) → verificação → ajuste. Teorias nunca são "provadas", apenas **corroboradas** — e precisam ser falseáveis para contar como ciência de verdade, não como tentativa de confirmar uma crença já formada com poucas evidências selecionadas.

## Tentativa e Erro Não É "Tentar Qualquer Coisa"

A fonte é explícita: tentativa e erro sistemática **não** é agir aleatoriamente e aceitar qualquer resultado. Tem quatro exigências:

1. **Repetição sistemática** — fazer a mesma verificação mais de uma vez, de forma controlada (equivalente ao item "Controle" do DMAIC).
2. **Testar logo** — contrapartida de curto prazo antes de qualquer contramedida de longo prazo (mesma lógica do modelo Toyota).
3. **Obsessão por evitar desperdício** — raiz de toda a metodologia de qualidade (Lean).
4. **Resolver um problema de cada vez, de forma disciplinada** — não copiar solução alheia sem identificar a própria causa raiz.

## Exemplo Concreto: os 5 Porquês

Técnica derivada do PDCA/Kaizen no manual do Modelo Toyota: partindo de um sintoma ("unidades produzidas por hora abaixo da média"), perguntar "por quê" repetidamente até chegar numa causa raiz acionável (ex.: operador caminha 1,5 km para pegar material) — só então definir uma contramedida testável, medir o resultado depois de um período (chamado no texto de "sprint"), e decidir entre consolidar a contramedida como permanente ou buscar nova hipótese.

## Meme do Desenvolvimento de Software

A fonte usa como contraponto cômico o ciclo vicioso "não escrevemos teste porque não temos tempo → não temos tempo porque há muitos bugs → há muitos bugs porque não há testes" como exemplo de um ciclo que **não** é tentativa e erro sistemática — é evitar a causa raiz repetidamente, sem nunca testar a contramedida real (escrever os testes).

## Ver também

- [[wiki/concepts/ciclo-pdca-deming]] — instância específica do ciclo, com os 14 pontos de gestão de Deming
- [[wiki/concepts/six-sigma-dmaic]] — instância específica, com exigências estatísticas mais rígidas (3,4 defeitos por milhão)
- [[wiki/concepts/teoria-das-restricoes-goldratt]] — variante focada em identificar e resolver o "elo mais fraco" da cadeia, um problema de cada vez
- [[wiki/concepts/beira-do-caos]] — a oscilação ordem/caos que esse ciclo implementa na prática
- [[wiki/concepts/scrum-master]] — já documenta que Scrum nasceu nos anos 80, antes do Manifesto Ágil; esta página conecta a estrutura do Sprint diretamente ao PDCA/Kaizen que o antecede historicamente
- [[wiki/concepts/goodharts-law]] — risco de o ciclo de melhoria contínua degenerar em otimizar o número (a métrica do "Check"/"Measure") em vez do problema real

## Key Sources

- [[wiki/sources/aprendizado-gestao-e-beira-do-caos-fabio-akita]] — fonte primária e única desta ingestão
