---
type: source
title: "O Que É Refatoração (e Quando Usar)"
aliases: ["refatoração bernardo lobato", "quando refatorar", "two hats refactoring video"]
date_created: 2026-07-15
date_updated: 2026-07-15
source_file: "raw/o-que-e-refatoracao-quando-usar.md"
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-07-15
source_count: 0
tags: [refactoring, clean-code, craftsmanship, tech-debt, testes, kent-beck, martin-fowler, god-object]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Vídeo introdutório de uma possível série sobre refatoração. Define refatoração como o processo de mudar a estrutura interna de um sistema sem alterar seu comportamento externo, e explora dois pilares: (1) nunca refatorar e adicionar funcionalidade ao mesmo tempo — os "dois chapéus" de Kent Beck; (2) a estrutura interna pode mudar livremente. Usa uma God Class (`OrderProcessor`) crescendo sprint a sprint como exemplo de como o design degrada sob pressão de prazo. Defende testes automatizados baratos (base da pirâmide) como pré-requisito de segurança, passos pequenos que nunca deixam o sistema num estado inconsistente por muito tempo, e distingue refatoração oportunista (aproveitando trabalho que já seria feito) de refatoração planejada. Cita Martin Fowler para a política de bugs encontrados durante a refatoração: bug já conhecido fica como está; bug novo pode ser corrigido, só com certeza absoluta de que é real.

## Key Claims

**Claim:** Refatoração e adição de funcionalidade são atividades mutuamente exclusivas no tempo — nunca devem ser feitas simultaneamente.
**Evidence:** Metáfora dos "dois chapéus" de Kent Beck: com o chapéu de funcionalidade, o progresso é medido acrescentando testes e fazendo-os passar (comportamento muda); com o chapéu de refatoração, o objetivo é só reestruturar, sem alterar resultados esperados dos testes existentes (comportamento não muda). A troca pode levar minutos ou horas, mas precisa ser consciente.
**Confidence:** alta — citação direta e nomeada de fonte primária (Kent Beck / Extreme Programming), consistente com [[wiki/concepts/tdd]] (RED-GREEN-REFACTOR também separa fases).

**Claim:** Um design bem pensado degrada gradativamente sob pressão de prazo, sprint a sprint, até virar uma God Class que ninguém quer tocar — não por incompetência do último desenvolvedor, mas porque ele está seguindo o padrão que já estava ali.
**Evidence:** Exemplo narrado: `OrderProcessor` limpo na Sprint 1 (recebe pedido, cobra, salva) → um `if` de frete internacional "rapidinho" na Sprint 5 sob prazo → Sprint 20, após 3 mudanças de escopo e 2 trocas de equipe, virou God Class que valida cupom, calcula imposto, checa fraude e dispara evento pro Kafka.
**Confidence:** média — exemplo ilustrativo/hipotético do autor, não um caso real auditado, mas consistente com o padrão já documentado em [[wiki/concepts/god-object]] via outras fontes.

**Claim:** A garantia de segurança para refatorar sem introduzir bugs é cobertura de testes automatizados baratos e rápidos — a base da pirâmide de testes, não E2E.
**Evidence:** Testes end-to-end são citados explicitamente como custosos e lentos demais para o ciclo de refatoração. Se a funcionalidade não tem testes, a recomendação é escrevê-los primeiro, só para aquele escopo, para mapear o comportamento real antes de mexer na estrutura.
**Confidence:** alta — consistente com [[wiki/concepts/piramide-de-testes]], sem contradição com outras fontes da wiki sobre testes.

**Claim:** Refatoração deve avançar em passos pequenos que nunca deixam o sistema num estado externamente inconsistente por muito tempo; uma branch dedicada de refatoração de longa duração, divergindo da main, é uma red flag.
**Evidence:** Argumento: se a refatoração levar módulo inteiro numa branch separada enquanto a main segue evoluindo normalmente, o merge eventual (se acontecer) é extremamente arriscado, e há alta chance de terminar com um código que não entrega nem a refatoração nem a funcionalidade nova.
**Confidence:** alta — argumentado com lógica clara, consistente com práticas de trunk-based development já presentes na wiki (não citadas nominalmente no vídeo, mas o raciocínio é o mesmo).

**Claim:** Bug conhecido e priorizado, encontrado durante a refatoração, deve ser deixado como está — a meta é reproduzir exatamente o comportamento externo pré-refatoração. Bug novo pode ser corrigido no mesmo momento, mas só com certeza absoluta de que é um bug real.
**Evidence:** Atribuído a Martin Fowler, no livro *Refatorando: Aperfeiçoando o Design de Códigos Existentes*.
**Confidence:** média-alta — atribuição nomeada e livro identificado, mas sem citação textual direta (paráfrase do autor do vídeo).

**Claim:** Refatoração acelera a entrega de longo prazo, de forma contraintuitiva — investir no design interno reduz o tempo necessário para adicionar features futuras.
**Evidence:** Autor cita gráficos do livro de Fowler mostrando queda no tempo de entrega de feature quando o design é mantido bom continuamente, versus aumento de tempo quando o design degrada.
**Confidence:** média — gráficos mencionados mas não reproduzidos com dados no texto-fonte (é uma transcrição de fala, sem acesso às imagens exibidas na tela).

## Refatoração Oportunista vs. Planejada

```
Oportunista (mais comum, recomendada):
  aproveita trabalho que já seria feito de qualquer forma
  ex: imediatamente antes de adicionar feature parecida a algo existente
  → evita duplicar método e ter que sincronizar duas cópias no futuro

Planejada (mais rara):
  revisões de código e processos dedicados
  não detalhado no vídeo (fica para vídeo futuro da série)
```

## Entities & Concepts Touched

- [[wiki/concepts/refatoracao]] (novo)
- [[wiki/concepts/dois-chapeus-kent-beck]] (novo)
- [[wiki/concepts/god-object]]
- [[wiki/concepts/piramide-de-testes]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/boy-scout-rule]]
- [[wiki/concepts/single-responsibility]]
- [[wiki/entities/martin-fowler]]
- [[wiki/entities/kent-beck]]
- [[wiki/entities/bernardo-lobato]]

## Open Questions

- O vídeo promete uma série futura cobrindo code smells, catálogo de técnicas de refatoração de Fowler, e "como refatorar com segurança usando testes" em maior profundidade — a definição e o "quando usar" aqui ficam propositalmente na superfície.
- Não fica claro no vídeo qual é o limiar objetivo entre "refatoração oportunista que vale a pena terminar agora" e "isso já é grande demais, vira débito técnico" — o autor reconhece que é uma questão de bom senso, sem heurística concreta.
- A citação do livro de Fowler sobre bugs conhecidos vs. desconhecidos durante refatoração é parafraseada, não citada textualmente — vale confirmar a formulação exata numa ingestão futura do próprio livro.
