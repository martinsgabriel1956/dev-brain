---
type: source
title: "Teorema CAP — O P Não É Uma Opção, É a Pré-condição da Escolha entre C e A"
aliases: ["cap theorem pedro camaforte", "p é pré-condição do cap", "cap por serviço entrevista"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-10-01
source_count: 0
tags: [system-design, entrevistas, cap-theorem, sistemas-distribuidos, consistencia, disponibilidade, microsservicos]
skill: tech-mentor-system-design
status: stable
---

# Teorema CAP — O P Não É Uma Opção, É a Pré-condição da Escolha entre C e A

## TL;DR

Vídeo de [[wiki/entities/pedro-camaforte]] sobre o [[wiki/concepts/cap-theorem]] para entrevistas de system design. Tese central: o diagrama de triângulo "escolha 2 de 3" (CP, CA ou AP à vontade) **é um erro didático**. A **tolerância a partição não é uma terceira opção independente** — é a **pré-condição que ativa o dilema**: só há o que escolher entre consistência e disponibilidade *porque* a rede pode falhar entre os nós ([[wiki/concepts/particao-como-pre-condicao-do-cap]]). O caso "CA" só existe num sistema de um nó único, que não é distribuído e portanto não entra em entrevista. A escolha C vs. A é guiada por **feeling de produto** ([[wiki/concepts/feeling-de-produto-em-consistencia-vs-disponibilidade]]) e, no nível sênior, **não é global**: serviços diferentes do mesmo sistema escolhem diferente (booking = C, search = A) ([[wiki/concepts/cap-por-servico]]). Esta é a ponta "didática de entrevista" do tema, complementar à fonte de incidente real [[wiki/sources/github-2018-cap-pacelc-particao-video]] e à fonte teórica [[wiki/sources/cap-pacelc-consistencia]].

## Key Claims

| Claim | Evidência na fonte | Confiança |
|---|---|---|
| P é pré-requisito, não opção: só se escolhe entre C e A depois de uma falha entre nós | Exemplo do e-commerce com réplica EUA→Brasil: sem a falha de sincronização, o dilema "mostrar desatualizado vs. não mostrar" não existe | Alta (consistente com [[wiki/sources/cap-theorem]]) |
| "Partição" = falha de comunicação entre servidores, **não** "muitos servidores" | Esclarecimento explícito do autor contra uma confusão comum | Alta |
| CA só existe no cenário hipotético de nó único, que não é sistema distribuído | Sistema simples: usuário → servidor → um banco | Alta |
| Escolher disponibilidade = mostrar dado possivelmente desatualizado; escolher consistência = recusar até sincronizar | Produto deletado nos EUA ainda visível no Brasil vs. página "indisponível" | Alta |
| Consistência para ingressos, assentos (cinema/avião), estoque e transações financeiras; disponibilidade para o resto (feeds, perfil, comentários, dashboards) | Lista de domínios "que mais caem em entrevistas" | Média — heurística de entrevista, o próprio autor admite exceções |
| A escolha é de produto ("feeling"), não só técnica | Instagram/YouTube: recarregar resolve; não vale travar a feature | Média (opinião do autor) |
| Em microsserviços cada serviço pode ter sua própria escolha (booking C, search A) | Sistema de ingressos de cinema com dois serviços | Alta (alinhado ao próprio Brewer [external], ver Notas) |
| Entender o CAP **antes** de desenhar a arquitetura guia ferramentas e padrões | Afirmação de abertura/fechamento | Média |

## Conceitos

- [[wiki/concepts/cap-theorem]] — enunciado e CP vs. AP
- [[wiki/concepts/particao-como-pre-condicao-do-cap]] — **novo**: por que o P é fixo e o triângulo engana
- [[wiki/concepts/cap-por-servico]] — **novo**: granularidade da escolha em microsserviços
- [[wiki/concepts/feeling-de-produto-em-consistencia-vs-disponibilidade]] — **novo**: critério de produto para escolher C ou A
- [[wiki/concepts/disponibilidade-no-teorema-cap]] — definição de disponibilidade (ver divergência em Notas)
- [[wiki/concepts/eventual-consistency]], [[wiki/concepts/consistency-models]] — o que o lado "A" aceita em troca
- [[wiki/concepts/reservation-pattern]], [[wiki/concepts/pessimistic-locking]] — mecanismos citados para o serviço de booking
- [[wiki/concepts/microsservicos]], [[wiki/concepts/niveis-de-senioridade-system-design]], [[wiki/concepts/pacelc]]

## Entidades

- [[wiki/entities/pedro-camaforte]] — autor
- [[wiki/entities/eric-brewer]] — formulador do CAP (descrito na fonte como VP de infraestrutura do Google)
- [[wiki/entities/google]]

## Notas, divergências e contexto [external]

1. **Definição de disponibilidade divergente.** O vídeo diz que "toda requisição recebe uma resposta, positiva ou negativa", incluindo um 404 ou "erro". A wiki ([[wiki/concepts/disponibilidade-no-teorema-cap]]) e a definição formal de Gilbert & Lynch exigem resposta **sem erro**, e um nó que recusa para preservar consistência é indisponível no CAP. A fonte se contradiz de leve: o exemplo "página de produtos indisponíveis" é, ele mesmo, a escolha por consistência. Registrado em [[wiki/questions/disponibilidade-cap-resposta-de-erro-vs-resposta-sem-erro]].
2. **"Escolha 2 de 3" foi criticada pelo próprio Brewer.** [external] Em "CAP Twelve Years Later" (2012) Brewer escreve que a formulação "2 of 3" "was always misleading", que o CAP "prohibits only a tiny part of the design space: perfect availability and consistency in the presence of partitions, which are rare", e que a escolha C vs. A "can occur many times within the same system at very fine granularity", variando por subsistema, operação, dado ou usuário. Isso valida as duas teses do vídeo (P como pré-condição e escolha por serviço). A fonte sugere que a confusão vem da maneira como Brewer explicou; na prática, foi o próprio Brewer quem a corrigiu depois. URL: https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/
3. **O que o vídeo não cobre (lacuna frente à skill):** [[wiki/concepts/pacelc]] (latência vs. consistência sem partição — "partições são raras" é a razão pela qual o dilema do dia a dia é outro), níveis intermediários de [[wiki/concepts/consistency-models]] (read-your-writes, causal) e quórum. A fonte trata consistência como binária.
4. **Consistência no vídeo = linearizável.** "Mesmo dado em qualquer nó, não considerando latência nem tempo de replicação" descreve [[wiki/concepts/linearizability]], não a "consistência" de ACID — homônimos que o vídeo não distingue.
5. Atribuição "VP de infraestrutura do Google" vem do autor do vídeo; não verificada nesta sessão.
6. Trecho ininteligível na transcrição ("esqueci um assento aqui nessa palavra", provavelmente "acento") não afeta o conteúdo.

## Citações

> "O P não é uma terceira opção independente de consistência e disponibilidade, ele é a pré-condição que ativa a escolha entre C e A."

> "A gente não vai impedir um vídeo do YouTube de carregar porque algum comentário não tá sincronizado."

## Perguntas em aberto

- Como combinar, no serviço de booking, consistência forte do CAP com a UX do [[wiki/concepts/reservation-pattern]]? (o vídeo remete a outro vídeo da série: [[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]])
- Quando duas features do mesmo fluxo têm escolhas diferentes (busca vs. compra), como o usuário percebe a inconsistência entre elas (descrição velha na busca, nova no checkout)?
