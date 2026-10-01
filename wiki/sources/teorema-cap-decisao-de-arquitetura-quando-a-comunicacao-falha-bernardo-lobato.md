---
type: source
title: "Teorema CAP — A Decisão de Arquitetura quando a Comunicação Falha (Bernardo Lobato)"
aliases: ["cap theorem bernardo lobato", "cap catálogo netflix reserva de voos", "cap estoque e pedido"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/teorema-cap-decisao-de-arquitetura-quando-a-comunicacao-falha-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-10-01
source_count: 0
tags: [system-design, cap-theorem, sistemas-distribuidos, consistencia, disponibilidade, microsservicos, entrevistas]
skill: tech-mentor-system-design
status: stable
---

# Teorema CAP — A Decisão de Arquitetura quando a Comunicação Falha

## TL;DR

[[wiki/entities/bernardo-lobato]] apresenta o [[wiki/concepts/cap-theorem]] como decisão de arquitetura: história (conjectura de [[wiki/entities/eric-brewer]] em 2000, prova de [[wiki/entities/seth-gilbert]] e [[wiki/entities/nancy-lynch]] em 2002), enunciado ("na partição, não se garante C e A juntas"), e a tese de que **P é intrínseco, não opcional** ([[wiki/concepts/particao-como-pre-condicao-do-cap]]). Diferenciais frente a [[wiki/sources/teorema-cap-p-e-pre-condicao-escolha-entre-c-e-a-pedro-camaforte]]: (1) **CP/AP descrevem comportamento, não rótulo de tecnologia**, e banco gerenciado em nuvem não elimina o CAP ([[wiki/concepts/cap-classificacao-por-comportamento]]); (2) **só é CAP quando há estado compartilhado a coordenar** ([[wiki/concepts/cap-exige-estado-compartilhado]]); (3) consistência do CAP ≠ do ACID ([[wiki/concepts/consistencia-cap-vs-consistencia-acid]]); (4) o CAP decide a falha, não a **reconciliação posterior** ([[wiki/concepts/reconciliacao-pos-particao]]). Exemplos: catálogo Netflix (A), busca de voos (A) vs. compra do bilhete (C) ([[wiki/concepts/cap-por-servico]]).

## Key Claims

| Claim | Evidência na fonte | Confiança |
|---|---|---|
| CAP nasceu como conjectura (Brewer, 2000) e foi provado em 2002 por Gilbert e Lynch (MIT) | Narrativa de abertura | Alta [external: Brewer confirma o keynote PODC 2000; a prova de 2002 não é citada por ele, não verificada aqui] |
| Partição = nós vivos que não se comunicam (cabo, roteador, firewall, entre regiões) | Lista de causas | Alta |
| P é característica intrínseca; "escolha 2 de 3" é enganoso | "Não dá para desligar a tolerância a partições" | Alta (Brewer 2012 [external]) |
| CP = recusar para preservar consistência; AP = responder e aceitar divergência temporária | Servidores A/B | Alta |
| Disponibilidade = todo nó que recebe a requisição responde, mesmo particionado | Definição do vídeo; não inclui "erro" como resposta válida | Alta; alinhado à definição formal, ao contrário do outro vídeo |
| Rótulos CP/AP não resumem uma tecnologia; MongoDB e Cassandra têm garantias configuráveis | Seção de bancos | Média (citados de passagem pelo autor) |
| Banco gerenciado de nuvem abstrai replicação mas não elimina o CAP | Seção AWS/Azure/GCP | Média (argumento do autor) |
| Falha de chamada isolada (A→B fora do ar) não é CAP; precisa de estado compartilhado | Seção de serviços | Média (interpretação do autor; sujeita a debate acadêmico, segundo ele) |
| Netflix: A (dado velho por segundos é aceitável); voos: busca = A, compra = C (evita vender o mesmo assento duas vezes) | Jogo dos exemplos | Alta (heurística; ver [[wiki/concepts/feeling-de-produto-em-consistencia-vs-disponibilidade]]) |
| CAP não resolve a volta ao consistente; isso é saga / 2PC | Fechamento | Alta |

## Conceitos

- [[wiki/concepts/cap-theorem]], [[wiki/concepts/particao-como-pre-condicao-do-cap]], [[wiki/concepts/cap-por-servico]], [[wiki/concepts/feeling-de-produto-em-consistencia-vs-disponibilidade]], [[wiki/concepts/disponibilidade-no-teorema-cap]]
- **Novos:** [[wiki/concepts/cap-exige-estado-compartilhado]], [[wiki/concepts/cap-classificacao-por-comportamento]], [[wiki/concepts/consistencia-cap-vs-consistencia-acid]], [[wiki/concepts/reconciliacao-pos-particao]]
- [[wiki/concepts/acid]], [[wiki/concepts/eventual-consistency]], [[wiki/concepts/consistency-models]], [[wiki/concepts/pacelc]], [[wiki/concepts/microsservicos]], [[wiki/concepts/distributed-transactions]], [[wiki/concepts/saga-pattern]], [[wiki/concepts/two-phase-commit]], [[wiki/concepts/reservation-pattern]], [[wiki/concepts/mongodb]], [[wiki/concepts/dynamodb]]

## Entidades

[[wiki/entities/bernardo-lobato]] (autor), [[wiki/entities/eric-brewer]], [[wiki/entities/seth-gilbert]], [[wiki/entities/nancy-lynch]], [[wiki/entities/netflix]], [[wiki/entities/amazon-web-services]]

## Notas, divergências e [external]

1. **Disponibilidade:** diferente do vídeo de Pedro Camaforte, aqui a definição é a formal; reforça a leitura proposta em [[wiki/questions/disponibilidade-cap-resposta-de-erro-vs-resposta-sem-erro]].
2. **Brewer 2012 [external]** (https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/): confirma o keynote PODC 2000, a escolha C/A em "fine granularity" por subsistema/operação/dado/usuário e a etapa de recuperação pós-partição. Não menciona Gilbert & Lynch. A afirmação do vídeo de que Brewer "endossou" a extrapolação para serviços é sustentada pela granularidade, não por texto explícito sobre serviços.
3. Exemplo do depósito (R$ 50 / R$ 100) é ambíguo na transcrição; só ilustra leitura desatualizada.
4. "Transação distribuída" aparece como contraste; "to face" na transcrição lido como two-phase commit.
5. Lacunas frente à skill: PACELC, quórum e modelos intermediários de consistência (read-your-writes etc.) não aparecem. A afirmação "CP/AP por tecnologia" na skill ([[wiki/concepts/cap-theorem]] / tabela PostgreSQL=CP, Cassandra=AP) é exatamente a simplificação que o vídeo alerta.
6. Mini desafio do autor: aplicar CAP às funcionalidades do seu próprio sistema.

## Citações

> "Não dá para simplesmente desligar a tolerância a partições e fingir que ela não existe."

> "O CAP entra quando existe um estado compartilhado que dois serviços precisam coordenar e o sistema tem que decidir o que fazer quando essa coordenação quebra."

## Perguntas em aberto

- Como o limite "estado compartilhado" se aplica em arquiteturas orientadas a eventos, onde cada serviço mantém cópia local ([[wiki/sources/comunicacao-assincrona-arquiteturas-distribuidas-bernardo-lobato]])?
- Quando a compra (C) falha na partição, qual a UX ideal (fila, reserva temporária — [[wiki/concepts/reservation-pattern]])?
