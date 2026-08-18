---
type: source
title: "CQRS e Event Sourcing — Full Cycle (Wesley Williams)"
aliases: ["CQRS e Event Sourcing Full Cycle"]
date_created: 2026-08-17
date_updated: 2026-08-17
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cqrs-event-sourcing-full-cycle-wesley-williams.md
source_url: ""
author: "Wesley Williams"
date_published: ""
date_ingested: 2026-08-17
source_count: 0
tags: [cqrs, event-sourcing, arquitetura, ddd, agregado, datomic, command-sourcing, greg-young, solid]
skill: tech-mentor-backend
status: stable
---

# CQRS e Event Sourcing — Full Cycle (Wesley Williams)

## TL;DR

Vídeo do canal [[wiki/entities/full-cycle|Full Cycle]], apresentado por [[wiki/entities/wesley-willians|Wesley Williams]], introduzindo CQRS e Event Sourcing a partir de um exemplo de agregado em [[wiki/concepts/ddd|DDD]] (ordem de serviço → pedido → cliente → indicação). Argumenta que a rigidez de sempre carregar o agregado inteiro para leitura motiva separar o sistema em um lado de comandos (mutações, via agregados) e um lado de leitura (consultas livres, otimizadas, possivelmente com views materializadas ou bancos de natureza diferente — documento, grafo). Atribui a criação do CQRS a **Greg Young**, baseado num conceito anterior, CQS. Introduz Event Sourcing como o complemento natural: eventos como fatos imutáveis do passado, cujo replay reconstrói o estado atual — usa a conta bancária (saldo = soma de créditos/débitos) como analogia central, e cita o banco de dados **Datomic** (usado pelo Nubank) como exemplo de banco imutável append-only. Apresenta uma ideia pouco aplicada na prática atribuída a Greg Young, o **Command Sourcing**: armazenar os comandos (não só os eventos), permitindo re-simular decisões de negócio sob condições de contexto diferentes (ex.: cenário de juros altos vs. baixos). Fecha com o erro mais comum ao adotar CQRS — reaproveitar os mesmos models entre comando e leitura, o que fere o Single Responsibility Principle — e a regra de que Commands retornam `void`.

## Claims Principais

| Claim | Confiança |
|---|---|
| CQRS foi criado por Greg Young, baseado num conceito anterior chamado CQS (Command Query Separation) | Alta — consistente com a literatura padrão já registrada em [[wiki/concepts/cqrs]] |
| A motivação prática para CQRS nasce da rigidez de agregados em DDD: carregar um agregado inteiro (ordem → pedido → cliente → indicação) só para exibir uma parte dos dados é ineficiente; separar leitura do modelo de domínio resolve isso | Alta |
| O lado de leitura pode usar bancos de natureza diferente do lado de escrita — orientado a documentos, "novo SQL", ou orientado a grafo — dependendo do formato de exibição necessário | Alta — consistente com a "fragmentação física do banco" já registrada em [[wiki/concepts/cqrs]] via [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]] |
| Um comando é disparado sem esperar o resultado ("fire and forget"); a verificação de sucesso/falha é responsabilidade de outro mecanismo (leitura, fila, mensageria) | Alta |
| Não é consenso se Event Sourcing exige CQRS ou vice-versa — o autor considera que não é obrigatório usar Event Sourcing só porque se usa CQRS, mas nota que "muitos autores" recomendam a combinação | Média — opinião do apresentador, citada sem nomear os autores |
| O Datomic (banco usado pelo Nubank) nunca sobrescreve/exclui um registro — uma alteração cria uma nova versão da linha, preservando todo o histórico, o que garante auditoria nativa | Alta — consistente com [[wiki/concepts/datomic]] e [[wiki/entities/nubank]] já registrados na wiki |
| Reconstruir o estado a partir do replay de eventos permite remodelar o banco (mudar de modelagem) sem perda de informação, já que os eventos originais preservam tudo que aconteceu | Alta |
| **Command Sourcing** (ideia de Greg Young, raramente aplicada na prática segundo o autor): armazenar os comandos originais, não só os eventos resultantes, permite re-executar o mesmo comando sob um contexto de negócio diferente e observar resultados diferentes — útil para simulação de decisões de negócio | Média — o próprio autor descreve como uma ideia pouco vista em aplicações reais |
| O erro mais comum ao adotar CQRS é reaproveitar o mesmo model/DTO entre o lado de comando e o lado de leitura — isso fere o Single Responsibility Principle (SRP) do SOLID, já que comando e leitura mudam por razões diferentes | Alta |
| Comandos bem implementados retornam `void` — a resposta não é o objetivo do fluxo de escrita | Alta — consistente com a regra já registrada em [[wiki/concepts/command-bus]] |

## Entidades

- [[wiki/entities/full-cycle]] — canal/apresentador do vídeo
- [[wiki/entities/wesley-willians]] — apresentador
- [[wiki/entities/nubank]] — citado como exemplo de uso do Datomic
- [[wiki/entities/greg-young]] — criador do CQRS e autor da ideia de Command Sourcing (nova entidade, ver stub criado nesta ingestão)

## Conceitos

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/datomic]]
- [[wiki/concepts/command-bus]]

## Open Questions

- O vídeo não nomeia diretamente os "muitos autores" que recomendam combinar CQRS com Event Sourcing — tratado como claim de confiança média, mesma cautela já aplicada em [[wiki/sources/cqrs-e-event-sourcing-explicado-na-pratica]].
- Command Sourcing (armazenar comandos, não só eventos, para permitir "replay contrafactual" sob outro contexto de negócio) é uma ideia interessante mas não documentada em nenhuma outra fonte já ingerida na wiki — vale investigar se existe literatura/implementação real disso além da menção à talk de Greg Young.

## Contradições com a Wiki Existente

Nenhuma contradição. Esta fonte reforça e complementa [[wiki/concepts/cqrs]] e [[wiki/concepts/event-sourcing]]: nomeia explicitamente Greg Young como criador do CQRS (já citado indiretamente em [[wiki/sources/cqrs-dicionario-programador-codigo-fonte-tv]]), ancora a motivação de CQRS num exemplo concreto de agregado DDD, e adiciona duas contribuições novas à wiki — o exemplo do Datomic/Nubank aplicado à explicação de Event Sourcing (já existia como entidade/conceito separado, agora conectado à narrativa didática) e o conceito de **Command Sourcing**.

## Citações Brutas Preservadas

> "Não seria muito interessante se parte do meu sistema tivesse... e mantivesse exatamente essa linha que a gente está falando de agregados... eu garanto a consistência dos meus dados, das minhas informações, e tudo mais?"

> "O que que é um evento? No final das contas, é algo que já aconteceu: a porta aberta, a ordem inserida, o produto comprado."

> "Se eu mudo o nome de Wesley para Wesley Williams, ele [Datomic] cria um novo registro fazendo a modificação daquela linha... eu tenho um histórico de tudo que aconteceu, sempre."

> "Você já imaginou ter todos os comandos armazenados? [...] o mesmo comando pode gerar resultados diferentes de acordo com a época da empresa."

> "Todo comando, no final do dia, ele vai retornar void — por isso que é mais rápido, porque eu só mando a solicitação e não quero saber o que aconteceu com ela depois."

## Key Sources (páginas que citam esta fonte)

- [[wiki/concepts/cqrs]]
- [[wiki/concepts/event-sourcing]]
- [[wiki/concepts/ddd]]
- [[wiki/concepts/command-bus]]
- [[wiki/entities/full-cycle]]
- [[wiki/entities/wesley-willians]]
- [[wiki/entities/greg-young]]
