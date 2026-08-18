---
type: source
title: "Anti-Corruption Layer: Facade/Adapter entre Sistema Novo e Sistema Legado"
aliases: ["camada de anticorrupção", "acl pattern video"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: "raw/anti-corruption-layer-facade-adapter-sistema-legado.md"
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-08-18
source_count: 0
tags: [anti-corruption-layer, ddd, facade-pattern, adapter-pattern, strangler-fig, dependencia-oculta, sistemas-legados, acoplamento]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Transcrição curta (autor não identificado) explicando o objetivo de alto nível de uma camada de tradução entre sistema novo e sistema legado — sem nomear formalmente "Anti-Corruption Layer" (ACL), mas descrevendo exatamente o padrão de DDD por esse nome, implementado via Facade ou Adapter. O componente intermediário absorve tudo que seria "incomum" para uma das duas pontas, permitindo substituição gradativa (linkando com [[wiki/concepts/strangler-fig-pattern]]) sem dependência forte direta entre as duas versões. Dois problemas centrais motivam o padrão: (1) dependência — inclusive **dependência escondida**, exemplificada por URL/config vinda de banco/env var, ou por *reflection* em runtime (.NET, Java); (2) integração com múltiplos sistemas legados simultaneamente.

## Key Claims

**Claim:** O padrão evita dependência forte direta entre os objetos do sistema novo e do sistema legado, inserindo um componente intermediário responsável pela tradução entre os dois subsistemas.
**Evidence:** "ele evita que a gente tenha uma dependência forte entre os objetos da versão nova com a versão anterior. Se eu tenho diretamente meu sistema antigo... chamando os componentes novos, eu tenho uma dependência forte."
**Confidence:** alta — é a tese central da fonte, embora tratada só em nível de alto nível (sem código).

**Claim:** Dependência forte direta é bidirecionalmente frágil: mudança no sistema de origem quebra a chamada para o novo componente, e mudança no sistema provedor (resposta ou assinatura da requisição) quebra o consumidor.
**Evidence:** "se eu mexer no sistema origem... eu quebro a minha aplicação do lado de cá... e se é o sistema provedor que muda qualquer coisa, tanto relacionada à resposta quanto à assinatura dela, requisição, a gente também tem problemas, quebra outra ponta."
**Confidence:** alta — argumento coerente com a motivação padrão de ACL/Adapter documentada no skill (`ddd-advanced.md`).

**Claim:** O padrão descrito corresponde ao Facade ou ao Adapter do catálogo GoF — a fonte trata os dois como intercambiáveis para esse propósito, sem escolher um.
**Evidence:** "implementação de uma camada fachada ou um adaptador... isso aqui a gente tá falando na verdade do Design Patterns, o Facade né, ou o Adapter... dos dois um dos dois patterns aqui, eles servem para isso."
**Confidence:** média — a fonte não distingue quando usar Facade vs. Adapter nesse contexto específico; o skill carregado (`ddd-advanced.md`) resolve essa ambiguidade nomeando o padrão formal como **Anti-Corruption Layer** (Eric Evans, DDD), tipicamente implementado com um Adapter/Translator na fronteira — ver seção "Cruzamento com o Skill" abaixo.

**Claim:** Dependência escondida (não apenas dependência direta explícita) é um problema mais grave, pois é difícil de diagnosticar — exemplos: URL de chamada vinda de configuração em banco de dados/arquivo/variável de ambiente, ou *linkage* via reflection em tempo de execução em linguagens como .NET e Java.
**Evidence:** "como que eu posso criar uma dependência escondida? Por um componente que eu faço uma chamada através de uma configuração que às vezes até está num banco de dados... com algumas linguagens que suportam, por exemplo, reflexão como .NET, Java, você faz uma reflexão do componente e linca um com o outro ali. Dá até para implementar em tempo de execução."
**Confidence:** alta como observação qualitativa; a fonte não aprofunda como o ACL mitiga especificamente dependência via reflection (mitiga a dependência de chamada direta, mas configuração dinâmica é um problema ortogonal de observabilidade/governança, não resolvido pelo padrão em si).

**Claim:** O padrão também resolve problemas de integração quando há **múltiplos** sistemas legados que precisam se comunicar entre si (ou com o novo sistema), não apenas um.
**Evidence:** "outro problema que ele resolve é problemas com sistemas legados... não só um, mas talvez vários outros sistemas legados que precisavam ali se falar, a gente tem isso resolvido também."
**Confidence:** média — afirmado mas não demonstrado com exemplo; no vocabulário do skill isso se aproxima de um Anti-Corruption Layer por integração ou de um [[wiki/concepts/esb-enterprise-service-bus|ESB]], que a fonte não distingue.

## Cruzamento com o Skill (`tech-mentor-backend`)

O skill carregado (`references/architecture/ddd-advanced.md`) nomeia formalmente o padrão descrito pela fonte: **Anti-Corruption Layer (ACL)**, um dos padrões de Context Mapping do DDD estratégico (Eric Evans). Contribuições do skill que a fonte não cobre:

- **Nome formal e origem**: ACL vem do DDD estratégico (Context Map), não é um padrão GoF "puro" — GoF fornece o *mecanismo estrutural* (Facade/Adapter), DDD fornece o *contexto/motivação* (proteger o modelo de domínio de um modelo externo/legado).
- **Direção da tradução**: o skill enfatiza que é o **downstream** (quem depende) que cria a camada de tradução — o exemplo de código (`SAPAdapter.toPedido()`) mostra que o modelo de domínio (`Pedido { id, itens }`) nunca vê os nomes de campo do sistema legado (`sap_vbeln`, `sap_matnr`).
- **Padrões vizinhos no Context Map**: o skill posiciona ACL ao lado de **Open Host Service** (upstream expõe protocolo único para múltiplos consumidores, ao invés de se adaptar a cada um) e **Published Language** (protocolo compartilhado e documentado, ex. JSON Schema/Protobuf) — nenhum dos dois é mencionado pela fonte, mas são a resposta a "e se o sistema legado tivesse N consumidores, não só um".
- **Quando não vale a pena**: o skill nomeia **Separate Ways** (não integrar; aceitar duplicação) como alternativa válida quando o custo do ACL supera o problema que ele resolve — dimensão de trade-off ausente na fonte, que trata o ACL como sempre a resposta certa.

## Entities & Concepts Touched

- [[wiki/concepts/anti-corruption-layer]] (novo)
- [[wiki/concepts/adapter-pattern]]
- [[wiki/concepts/facade-pattern]]
- [[wiki/concepts/strangler-fig-pattern]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/esb-enterprise-service-bus]]

## Open Questions

- A fonte não distingue quando aplicar Facade vs. Adapter especificamente para ACL — o skill resolve isso parcialmente (Adapter/Translator é o mecanismo típico), mas nenhuma fonte da wiki ainda traz um exemplo prático de ACL implementado como Facade (orquestrando múltiplas chamadas ao legado) vs. Adapter (traduzindo uma única interface).
- "Dependência escondida via reflection em runtime" é levantada como problema, mas a fonte não explica como o ACL mitiga isso na prática — fica como lacuna a preencher se uma fonte futura tratar do tema.
- Autor não identificado — sem nome de canal/pessoa no trecho colado pelo usuário; nenhuma entidade nova criada.

## Raw Quotes

> "sempre que a gente tem dependência, quando eu mudo um ponto eu posso danificar outro, quebrar outro. E tem dependências que são escondidas, que a gente não consegue diagnosticar tão facilmente."

> "uma dependência direta gera esse tipo de dor... gera uma dor forte aí, então é uma dor de cabeça bem grande pra gente também."

> "quando a gente coloca uma camada de anticorrupção, os impactos... como diminui a dependência, a gente diminui também problemas nos sistemas de origem ali, os antigos, que tipicamente são os principais e vão ser por um bom tempo quando você começa esse processo."
