---
type: source
title: "ACID vs. BASE: As Garantias que os Bancos de Dados Nos Dão"
aliases: ["acid vs base", "atomicidade consistencia isolamento durabilidade", "basically available soft state eventual consistency"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 0
tags: [banco-de-dados, acid, base, consistencia, disponibilidade, system-design, trade-offs]
skill: tech-mentor-system-design
status: stable
source_file: "raw/acid-vs-base-garantias-bancos-de-dados.md"
source_url: ""
author: "desconhecido (vídeo YouTube, mesmo canal de sql-nao-e-banco-de-dados-uncle-bob e curso de System Design)"
date_published: ""
date_ingested: "2026-07-03"
---

## TL;DR

ACID (Atomicidade, Consistência, Isolamento, Durabilidade) é o conjunto de garantias fortes que bancos relacionais oferecem; BASE (Basically Available, Soft State, Eventual Consistency) é o conjunto de garantias mais fracas, mas mais escaláveis e disponíveis, comum em bancos não relacionais. O tradeoff central: consistência forte custa performance/escalabilidade (ex.: garantir e-mail único exige varredura ou índice); disponibilidade/escalabilidade custa a garantia de que toda leitura reflete a escrita mais recente. A escolha depende do domínio — não é uma regra absoluta, e a prática real frequentemente foge do "ideal acadêmico".

---

## Reivindicações Principais

**Claim:** Atomicidade garante que uma transação ocorre por inteiro ou não ocorre — não existe "meia transação" comitada.
**Evidência:** Exemplo de transferência bancária de R$100: debita de uma conta e credita em outra; se uma das duas operações falhar, a operação inteira é cancelada.
**Confiança:** Alta — é a definição formal padrão de atomicidade em bancos relacionais, coincide com o exemplo já registrado em [[wiki/concepts/database-transactions]].

**Claim:** Consistência significa que o banco de dados sempre transita de um estado internamente válido para outro estado internamente válido, respeitando constraints definidos (ex.: estoque não pode ser negativo, loja sempre precisa ter um usuário dono).
**Evidência:** Exemplos de constraints de schema e regras de integridade referencial.
**Confiança:** Alta.

**Claim:** Isolamento garante que transações concorrentes não interferem umas nas outras de forma incorreta, mas isso não significa que operações concorrentes sobre o mesmo dado não competem — o resultado final é consistente com alguma ordem serial válida das transações, não necessariamente o resultado de "ambas terem rodado sem se tocar".
**Evidência:** Exemplo de duas transações concorrentes escrevendo valores diferentes (`0` e `15`) no mesmo saldo — o valor final é um dos dois, nunca uma mistura, mas ambas efetivamente rodaram.
**Confiança:** Alta — e é uma nuance importante que evita a leitura ingênua de "isolamento = as transações nem se veem".

**Claim:** Durabilidade garante que, uma vez confirmado o commit, o dado sobrevive a uma falha de hardware/crash do sistema.
**Evidência:** Analogia de desligar o hardware do banco da tomada e religar — o dado permanece.
**Confiança:** Alta.

**Claim:** BASE (Basically Available, Soft State, Eventual Consistency) é comum em bancos não relacionais (Cassandra, MongoDB, DynamoDB), mas não é uma garantia universal desses bancos — é um padrão de design que tende a aparecer, não uma regra fixa.
**Evidência:** Ressalva explícita da fonte: "não é que eles vão te oferecer essa garantia sempre, é que é comum".
**Confiança:** Alta como ressalva metodológica — evita a simplificação "NoSQL = BASE sempre".

**Claim:** Consistência eventual pode gerar leitura de valor desatualizado logo após uma escrita, porque a propagação entre réplicas não é instantânea (ex.: escrever saldo=150 numa réplica e ler 80 de outra réplica não sincronizada ainda).
**Evidência:** Exemplo de três réplicas com tempo de propagação; comparação com o comportamento de `ConsistentRead` do DynamoDB.
**Confiança:** Alta — consistente com [[wiki/concepts/consistency-models]] (seção Eventual Consistency, exemplo de código DynamoDB `ConsistentRead: false` vs `true`).

**Claim:** Garantir uma regra de consistência forte (ex.: e-mail único) tem custo de performance direto — o banco precisa varrer todos os registros ou manter um índice (provavelmente hash) e consultá-lo antes de cada escrita.
**Evidência:** Exemplo passo a passo do fluxo de criação de usuário com e-mail duplicado.
**Confiança:** Alta — mecanismo real de implementação de constraints `UNIQUE` em bancos relacionais.

**Claim:** A escolha ACID vs. BASE não é uma regra absoluta na prática — bancos relacionais já foram usados onde não precisavam, e bancos não relacionais já foram usados em instituições de pagamento.
**Evidência:** Afirmação anedótica do autor, sem casos nomeados.
**Confiança:** Média — é uma observação qualitativa de experiência pessoal, não documentada com exemplos específicos.

---

## Quadro-Resumo: Quando Usar Cada Garantia

| Quer consistência forte (ACID) | Quer escalabilidade/disponibilidade (BASE) |
|---|---|
| Pagamentos e bancos | Rede social (contagem de likes) |
| Compras, lojas, estoque | Analytics |
| Tickets (ex.: assentos de avião) | Logs |
| — | Cache |
| — | Sistemas de recomendação |

---

## Conceitos

- [[wiki/concepts/acid]] — atomicidade, consistência, isolamento, durabilidade
- [[wiki/concepts/base-basically-available-soft-state-eventual]] — o acrônimo BASE explicado e contraposto ao ACID
- [[wiki/concepts/consistency-models]] — consistência eventual como um dos modelos do espectro
- [[wiki/concepts/cap-theorem]] — a mesma tensão consistência-vs-disponibilidade sob a lente do teorema CAP
- [[wiki/concepts/relational-vs-nosql]] — decisão prática de qual tipo de banco usar
- [[wiki/concepts/database-index]] — índice hash como mecanismo concreto para garantir unicidade sem varredura completa
- [[wiki/concepts/database-transactions]] — mesmo exemplo de transferência bancária usado para ilustrar atomicidade

## Ver também

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]] — mesmo canal/autor; discute arquitetura interna de bancos relacionais (B-tree, WAL, parser, planner)
- [[wiki/sources/cap-pacelc-consistencia]] — aprofundamento em CAP/PACELC e nos 5 modelos de consistência (Linearizability → Eventual)
- [[wiki/sources/modelos-de-consistencia]] — mesmo espectro de consistência eventual, com Vector Clocks e mecanismos de convergência

---

## Conexões com Outras Sources

- [[wiki/sources/banco-de-dados]] — fundamentos gerais de banco de dados, incluindo ACID e NoSQL
- [[wiki/sources/escalabilidade-vertical-horizontal-system-design]] — sharding e replicação como pré-condição para o tradeoff ACID/BASE se tornar relevante

---

## Perguntas Abertas

- A fonte cita que bancos NoSQL já foram usados "em instituições de pagamento" — quais mecanismos (ex.: transações multi-documento, compensação, saga pattern) permitem isso sem violar corretude financeira?
- Existe um ponto de escala objetivo (número de usuários, taxa de escrita) a partir do qual a troca de ACID por BASE deixa de ser opcional e passa a ser necessária?

---

## Citações

> "A parte difícil não é escrever código... a atomicidade significa: vai ser subtraído 100 da minha conta e adicionado 100 na conta da outra pessoa; caso alguma dessas operações não funcione, a operação inteira vai ser cancelada."

> "Ninguém te falou que era garantido a consistência aqui... isso nos dá uma escalabilidade boa e nos dá uma flexibilidade no geral."

> "Naturalmente, tem coisas que são mais adequadas para a gente ter uma corretude forte, e coisas que a gente pode ter aquele jeitinho — não faz tanta diferença se não estiver perfeitamente correto."
