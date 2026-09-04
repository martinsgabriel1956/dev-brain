---
type: source
title: "Local-First vs Offline-First"
aliases: ["local first vs offline first", "quem é a autoridade do dado"]
date_created: 2026-09-04
date_updated: 2026-09-04
source_count: 0
tags: [local-first, offline-first, crdt, lww, cap-theorem, sistemas-distribuidos, system-design]
skill: tech-mentor-system-design
status: draft
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/local-first-vs-offline-first.md
source_url:
author:
date_published:
date_ingested: 2026-09-04
---

# Local-First vs Offline-First

## TL;DR

"Funciona sem rede" não distingue local-first de offline-first — as duas funcionam offline. A distinção real é **qual cópia do dado é a autoridade**. Em offline-first, o servidor é a fonte da verdade e o local é só um cache subordinado (a escrita só é definitiva quando o servidor aceita). Em local-first, o dispositivo local é uma réplica primária (o servidor é uma cópia secundária, um "relay" que pode cair sem impedir a convergência entre réplicas). Isso muda o que sobra quando a empresa fecha (cache inútil vs. arquivo seu) e exige uma estratégia de resolução de conflito (LWW, mais simples e com risco de perda silenciosa de dados; ou CRDT, mais complexo mas convergente por construção). Local-first é uma decisão de arquitetura sobre dar **posse** do dado ao usuário — errada para domínios que dependem de autoridade central (banco, e-commerce, rede social, apps de corrida).

## Key Claims

| Claim | Evidência |
|---|---|
| "Funciona offline" não diferencia as duas arquiteturas | Ambas as afirmações ("abre no modo avião e edita") são verdadeiras para offline-first e local-first |
| A pergunta que separa as duas é qual cópia é a autoridade | Definição central do vídeo |
| Offline-first: local é cache subordinado ao servidor; escrita só é definitiva quando servidor aceita | Fluxo descrito: grava em cache local (ex. IndexedDB) → envia ao servidor quando a rede volta → servidor é fonte da verdade |
| Local-first: dispositivo local é réplica primária; servidor é cópia secundária ("relay") | Notebook e celular como réplicas primárias que convergem entre si; relay pode cair sem impedir a convergência |
| Edição concorrente offline em dois dispositivos exige resolução de conflito | Cenário do app logado em dois dispositivos offline editando simultaneamente |
| LWW é a abordagem mais simples, mas pode causar perda silenciosa de dados | Última escrita sobrescreve alterações anteriores sem aviso |
| CRDT é alternativa mais complexa a LWW | Mencionado por contraste, sem detalhar mecanismo (ver [[wiki/sources/crdt-colaboracao-tempo-real]] para profundidade) |
| Se a empresa fecha, offline-first perde o dado (era só cache); local-first mantém (arquivo local seu) | Teste de pensamento central do vídeo |
| Local-first é uma decisão errada para domínios que dependem de autoridade central | Exemplos dados: banco, e-commerce, rede social, app de corrida |
| A escolha se resume a: se divergirem, quem tem razão — servidor (offline-first/resiliência) ou a convergência entre réplicas (local-first/posse) | Framing final do vídeo |

## Conceitos

- [[wiki/concepts/local-first]] — revisado nesta ingestão: contradição com a definição anterior da wiki, ver Open Questions
- [[wiki/concepts/offline-first]] — novo, criado nesta ingestão
- [[wiki/concepts/last-write-wins]] — novo, criado nesta ingestão
- [[wiki/concepts/crdt]] — mencionado por contraste a LWW
- [[wiki/concepts/cap-theorem]] — paralelo estrutural: escolher quem é autoridade sob divergência é análogo a escolher C vs. A sob partição

## Entidades

_Nenhuma entidade identificável — autor/canal não mencionados no texto fornecido._

## Open Questions

- **Contradição terminológica com a wiki existente**: [[wiki/concepts/local-first]] já documentava "local-first" com um significado bem diferente (dado calculado no servidor, entregue ao cliente sem persistência, validado por HMAC na volta — ver [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]). Essa fonte usa "local-first" no sentido canônico do termo (Ink & Switch / Kleppmann): dispositivo local como réplica primária e autoritativa, servidor como réplica secundária opcional. São conceitos genuinamente diferentes usando o mesmo nome. Registrado em [[wiki/questions/local-first-definicoes-conflitantes]].
- O vídeo cita CRDT apenas por contraste, sem detalhar o mecanismo de convergência — a wiki já tem profundidade sobre isso em [[wiki/concepts/crdt]] e [[wiki/sources/crdt-colaboracao-tempo-real]].
- Vector clocks (mecanismo relacionado a resolução de conflito e causalidade, já presente em [[wiki/sources/vector-clocks]]) não são mencionados nesta fonte — possível lacuna a explorar em ingestão futura sobre local-first (como CRDTs/vector clocks se combinam na prática em sync engines como Automerge/Y.js).

## Key Sources

_Este é o documento primário._
