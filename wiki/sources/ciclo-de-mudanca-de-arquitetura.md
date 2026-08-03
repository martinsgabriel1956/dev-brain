---
type: source
title: "O Ciclo de Mudança de uma Arquitetura"
aliases: ["ciclo de mudança de arquitetura", "AS-IS TO-BE ciclo", "ciclo de migração arquitetural"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ciclo-de-mudanca-de-arquitetura.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-03
source_count: 0
tags: [arquitetura, migração, as-is, to-be, poc, strangler-fig, ciclo-de-vida]
skill: tech-mentor-system-design
status: stable
---

## TL;DR

Transcrição curta (aula/vídeo em português, já no idioma original) descrevendo o ciclo operacional de uma mudança de arquitetura: avaliar 100% o AS-IS (tecnologia + regras de negócio) → desenhar o TO-BE → validar com uma POC testada na escala real esperada (não uma fração dela) → migrar incrementalmente convivendo com os dois sistemas via padrões de coexistência → migração concluída vira o novo AS-IS, reiniciando o ciclo. A tese central é que assertividade importa porque o ciclo inteiro consome tempo real do negócio — descobrir "no meio do caminho" que a arquitetura escolhida está errada não é neutro, é retrabalho caro.

## Key Claims

**Claim:** Antes de desenhar o TO-BE, é preciso entender 100% o AS-IS — não só a tecnologia, mas as regras de negócio, os problemas e o que já funciona bem.
**Evidence:** A fonte enfatiza que pular essa etapa (ir direto para "vamos usar Event Sourcing/CDC/Outbox") é o erro que gera retrabalho: a escolha de padrão exige alinhamento com o negócio, não só com a tecnologia.
**Confidence:** alta

**Claim:** Uma POC de migração de arquitetura precisa ser testada na escala real esperada, não numa fração dela — testar 500 TPS quando a necessidade real é 10.000 TPS é um teste inválido.
**Evidence:** Exemplo dado na fonte: se o sistema precisa suportar 10.000 transações por segundo, a POC deve testar próximo desse número (1.000, 5.000, 10.000, e se possível 15.000) para revelar como o comportamento muda com a carga — principalmente quando a mudança envolve a camada de banco de dados. Isso complementa (não substitui) a definição já registrada em [[wiki/concepts/prova-de-conceito]] de POC como "escopo mínimo, timeboxed, descartável": a fonte adiciona que "mínimo" não pode significar "escala irrealista" quando o que está sendo validado é justamente comportamento sob carga.
**Confidence:** alta

**Claim:** POC não é MVP — o MVP vem depois da POC ter sucesso nos testes, não antes.
**Evidence:** A fonte distingue explicitamente as duas etapas: POC valida se a abordagem técnica funciona sob as condições reais esperadas; só depois disso começa o trabalho de entrega incremental (migração) que geraria os primeiros resultados de valor.
**Confidence:** média — a fonte não formaliza a definição de MVP usada, apenas a ordem relativa (POC → sucesso → migração incremental → resultados).

**Claim:** Migração de arquitetura exige um período de coexistência entre o sistema legado (A) e o novo sistema (B), com padrões específicos para reescrita, decomposição de serviço e comunicação entre os dois ambientes.
**Evidence:** A fonte não nomeia os padrões especificamente, mas descreve a necessidade central: rotas/funcionalidades migram aos poucos, e é preciso evitar que um sistema afete o outro enquanto ainda precisam conversar. Isso mapeia diretamente para o padrão já documentado na wiki em [[wiki/sources/strangler-fig]] (Transform/Coexist/Eliminate, proxy de roteamento, CDC para sincronização de dados).
**Confidence:** alta (conceito geral confirmado por fonte prévia mais detalhada; esta fonte não traz padrões nomeados adicionais)

**Claim:** O fim de uma migração de arquitetura não é um estado terminal — o TO-BE recém-implantado vira o novo AS-IS, reiniciando o ciclo como um fluxo contínuo de melhoria arquitetural.
**Evidence:** A fonte encerra descrevendo explicitamente esse loop: "isso vai virar o seu novo AS-IS. E aí vira um trabalho, um fluxo contínuo de melhoria de arquitetura." Ecoa o argumento já registrado em [[wiki/concepts/arquitetura-de-software]] (via [[wiki/sources/filosofia-do-design-de-software-introducao]]) de que design arquitetural é processo contínuo, não fase única — aqui aplicado especificamente ao nível de ciclo de migração, não de decisão de design dentro de um projeto já em andamento.
**Confidence:** alta

## Entities & Concepts Touched

- [[wiki/concepts/ciclo-de-mudanca-de-arquitetura]]
- [[wiki/concepts/prova-de-conceito]]
- [[wiki/concepts/strangler-fig-pattern]]
- [[wiki/concepts/ciclo-da-desgraca-software]]
- [[wiki/concepts/refactor-vs-rewrite-matrix]]
- [[wiki/concepts/arquitetura-de-software]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/outbox-pattern]]
- [[wiki/concepts/saga-pattern]]

## Open Questions

- A fonte cita "arquitetura de coreografia" e "arquitetura de orquestração" como exemplos de decisão de TO-BE, mas não aprofunda quando usar cada uma — ver [[wiki/concepts/saga-pattern]] para o detalhamento que falta aqui.
- Nenhuma métrica de "quando parar" a fase de coexistência é dada (ex.: % de tráfego migrado, critério de corte para desligar o legado) — [[wiki/sources/strangler-fig]] cobre isso com mais profundidade (fase "Eliminate" ao atingir 100%).
- Como a assertividade exigida na escolha do TO-BE se concilia com a natureza iterativa de arquitetura defendida em [[wiki/concepts/arquitetura-de-software]] (design como processo contínuo)? A fonte parece tratar "trocar de ideia no meio do caminho" como estritamente custoso, mas não distingue mudança de rumo por má POC (validação funcionando como pretendido) de mudança de rumo por design imaturo.

## Quotes

> "É muito importante que você seja assertivo, porque o trabalho leva um tempo. E se você perceber no meio do caminho que esse caminho não é o certo... isso vai fazer com que você perca muito tempo para conseguir fazer uma entrega de valor de fato para o negócio."

> "Se é 10.000 [TPS], teste pelo menos 10.000. [...] Você não precisa testar 100%. Não estou falando de fazer um MVP, porque o MVP vem depois dos testes."

> "Isso vai virar o seu novo AS-IS. E aí vira um trabalho, um fluxo contínuo de melhoria de arquitetura."
