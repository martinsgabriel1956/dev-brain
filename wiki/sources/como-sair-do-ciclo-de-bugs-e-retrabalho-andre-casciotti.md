---
type: source
title: "Como sair do ciclo de bugs e retrabalho (André Casciotti)"
aliases: ["ciclo de bugs e retrabalho", "3 passos para lidar com bug", "causa raiz, evidenciar, provar"]
date_created: 2026-10-14
date_updated: 2026-10-14
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/como-sair-do-ciclo-de-bugs-e-retrabalho-andre-casciotti.md
source_url: ""
author: "André Casciotti"
date_published: ""
date_ingested: 2026-10-14
source_count: 1
tags: [bugs, retrabalho, causa-raiz, debugging, testes, pressao, carreira, testing]
skill: tech-mentor-testing
status: stable
---

## TL;DR

Vídeo do quadro "Próximo Nível" de [[wiki/entities/andre-casciotti]]. Tese: o [[wiki/concepts/ciclo-de-bugs-e-retrabalho]] (pressão → pressa → correção e teste "de qualquer jeito" → bug volta ou nasce outro → mais pressão) está **normalizado** e é alimentado pelo piloto automático do dev, sobretudo do experiente ([[wiki/concepts/armadilha-da-certeza-do-dev-experiente]]). A saída é parar e respirar antes de mexer e seguir [[wiki/concepts/tres-passos-para-lidar-com-bug]]: (1) achar a [[wiki/concepts/causa-raiz]] em vez de corrigir o sintoma, olhando o fluxo de negócio inteiro; (2) [[wiki/concepts/evidenciar-o-problema]] antes de alterar (simular o erro, com log, tela ou conversa com QA/usuário, sem depender do banco de produção); (3) [[wiki/concepts/provar-que-corrigiu]] repetindo o mesmo teste, depois fazer a [[wiki/concepts/analise-de-impacto-da-correcao]] (reuso, entrada/saída) e, se possível, escrever um teste unitário. Fecho: tudo isso é [[wiki/concepts/analise-de-requisitos-aplicada-a-bugs|análise de requisitos]] aplicada a bugs.

## Key Claims

**Claim:** O ciclo de bugs/retrabalho é um dos problemas que mais afetam o dia a dia e ao mesmo tempo um dos mais invisíveis, porque foi normalizado ("é normal voltar bug") e passa de geração em geração.
**Evidence:** experiência do autor em dezenas de empresas e comentários de seguidores. **Confidence:** média (anedótico, mas coerente com [[wiki/concepts/medo-do-prazo-vs-medo-do-bug]] e [[wiki/concepts/risco-ocupacional-do-dev]]). Ver [[wiki/concepts/ciclo-de-bugs-e-retrabalho]].

**Claim:** A maior parte do retrabalho vem dos **bugs**, não de reuso ruim ou de features meia-boca; o ciclo se retroalimenta porque o dev culpa a pressão e não quer reclamar para proteger o emprego.
**Evidence:** argumento qualitativo. **Confidence:** média-baixa (sem dado). [external] estudos sobre custo de defeitos não foram consultados nesta ingestão.

**Claim:** Antes de mexer, **pare e respire**: correr coloca um risco novo no código; o dev não controla os outros, deve mudar o que pode.
**Evidence:** opinião do autor. **Confidence:** média. Liga a [[wiki/concepts/foco-no-que-esta-ao-seu-alcance]] e [[wiki/concepts/escolhas-conscientes-sob-pressao]].

**Claim:** Sintomas são fáceis de corrigir, causas raiz não; consertar só o ponto onde estourou o erro (um `if` para nulo/zero) gera novos bugs, bugs de negócio silenciosos (campo bloqueado, seção não exibida) e **empilha gambiarra** no código.
**Evidence:** exemplos (registro não gravado três etapas antes; regra de negócio no lugar errado; valor R$ 1.000 que vira 5 milhões). **Confidence:** alta como princípio, coerente com [[wiki/concepts/causa-raiz]]. Ver [[wiki/concepts/tres-passos-para-lidar-com-bug]].

**Claim:** Para achar a causa raiz, três perguntas antes de editar: o estado faz sentido neste ponto? como é o fluxo de negócio todo? por que o código está assim (a "tartaruga na árvore")?
**Evidence:** passo a passo do autor. **Confidence:** média-alta; aproxima-se de [[wiki/concepts/hipotese-e-validacao]] e [[wiki/concepts/entender-contexto-da-demanda]].

**Claim:** O dev **experiente** erra mais no passo de evidenciar: tem o código mapeado, gera certezas, altera e testa com confiança excessiva (ou nem testa) e comete "bugs idiotas".
**Evidence:** relato próprio; contraste com iniciante. **Confidence:** média (opinião). Ver [[wiki/concepts/armadilha-da-certeza-do-dev-experiente]].

**Claim:** Evidenciar = **simular o erro antes de alterar**; a evidência pode ser log, mensagem/print do usuário ou comportamento na tela, não só debug; conversar com QA ensina a explorar e testar, e com o usuário ensina negócio.
**Evidence:** exemplos de QA e usuário. **Confidence:** média-alta. Ver [[wiki/concepts/evidenciar-o-problema]].

**Claim:** Falta de acesso ao banco de produção (compliance, LGPD) raramente é impeditivo; dá para simular em outro ambiente com a informação que dispara o problema.
**Evidence:** argumento do autor. **Confidence:** média; [skill: tech-mentor-testing] concorda que reprodução deve usar dados sintéticos/mascarados (ver `test-data-management.md`). Ver [[wiki/concepts/lgpd]].

**Claim:** **Debug não é prova** de correção: passar pelo ponto sem exception não diz o que o usuário vê; debug diagnostica, o teste repetido prova.
**Evidence:** exemplo do campo bloqueado após "corrigir" com F5/F10/F11. **Confidence:** alta (lógica). Ver [[wiki/concepts/provar-que-corrigiu]].

**Claim:** Prova = **mesmo teste antes e depois** da correção; depois checar impactos (consumidores do trecho, mudança de entrada/saída); teste unitário detecta mudança de contrato e mapeia consumos, e é prova empírica repetível.
**Evidence:** descrição do método. **Confidence:** alta; [skill: tech-mentor-testing] `test-strategy-risk-architecture.md` recomenda "adicione testes para qualquer bug novo ANTES de corrigir (evita regressão)", o mesmo princípio formalizado em [[wiki/sources/test-driven-bug-fixing-xunitpatterns]]. Ver [[wiki/concepts/analise-de-impacto-da-correcao]].

**Claim:** Provar dá trabalho e gera desculpas ("só testo em produção"); o custo de falhar é a reputação do dev e o transtorno do negócio (ex.: preço errado em produção).
**Evidence:** exemplo hipotético do autor (promoção no Mercado Livre). **Confidence:** exemplo ilustrativo, não caso verificado.

**Claim:** Os três passos são **análise de requisitos** aplicada a bugs, e servem de workflow de trabalho: causa raiz → evidenciar → provar → publicar.
**Evidence:** fecho do vídeo; divulga o curso "Dev que Resolve". **Confidence:** média; o autor tem interesse comercial. Ver [[wiki/concepts/analise-de-requisitos-aplicada-a-bugs]].

## Entities

[[wiki/entities/andre-casciotti]] (autor; menciona o curso "Dev que Resolve", sem página própria).

## Concepts

Novos: [[wiki/concepts/ciclo-de-bugs-e-retrabalho]], [[wiki/concepts/tres-passos-para-lidar-com-bug]], [[wiki/concepts/evidenciar-o-problema]], [[wiki/concepts/provar-que-corrigiu]], [[wiki/concepts/analise-de-impacto-da-correcao]], [[wiki/concepts/armadilha-da-certeza-do-dev-experiente]], [[wiki/concepts/analise-de-requisitos-aplicada-a-bugs]].
Ligados: [[wiki/concepts/causa-raiz]], [[wiki/concepts/debugging]], [[wiki/concepts/reprodutibilidade-de-bugs]], [[wiki/concepts/production-bugs]], [[wiki/concepts/plano-de-testes-escrito]], [[wiki/concepts/testar-proprio-codigo]], [[wiki/concepts/tdd]], [[wiki/concepts/medo-do-prazo-vs-medo-do-bug]], [[wiki/concepts/escolhas-conscientes-sob-pressao]], [[wiki/concepts/foco-no-que-esta-ao-seu-alcance]], [[wiki/concepts/risco-ocupacional-do-dev]], [[wiki/concepts/hipotese-e-validacao]], [[wiki/concepts/entender-contexto-da-demanda]], [[wiki/concepts/lgpd]], [[wiki/concepts/inseguranca-na-entrega]].

## Open Questions

- Sem dados sobre quanto do retrabalho vem de bugs; a afirmação é do autor.
- Como aplicar "simular o erro" em bugs intermitentes/concorrência ou que dependem de estado de produção? Só tocado de leve ([[wiki/concepts/reprodutibilidade-de-bugs]]).
- O vídeo não trata observabilidade (logs/traces) como pré-requisito para evidenciar; só cita log.
- "Dev que Resolve" não detalhado (conteúdo do curso só enumerado).

## Raw quotes

> "Saber que é importante é muito diferente de fazer."

> "O debug é uma ótima ferramenta para diagnosticar o problema, não para provar que você corrigiu."

> "Você corrige um ponto e quebra outro porque você não prova que corrigiu, você acha que corrigiu."
