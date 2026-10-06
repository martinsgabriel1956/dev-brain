---
type: source
title: "Anti-Corruption Layer em Microsserviços: funcionamento, problemas e requisitos arquiteturais"
aliases: ["acl microsserviços parte 2", "camada de anticorrupção requisitos arquiteturais"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/anti-corruption-layer-microsservicos-requisitos-arquiteturais.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-10-06
source_count: 0
tags: [anti-corruption-layer, microsservicos, strangler-fig, sistemas-legados, requisitos-arquiteturais, transacoes, debito-tecnico, ddd]
skill: tech-mentor-backend
status: draft
---

# Anti-Corruption Layer em Microsserviços: funcionamento, problemas e requisitos arquiteturais

## TL;DR

Continuação de [[wiki/sources/anti-corruption-layer-facade-adapter-sistema-legado]] (mesmo autor, não identificado). Se a parte 1 dava a motivação, esta mostra **como a camada funciona na migração legado → microsserviços** e **quando vale a pena**. A [[wiki/concepts/anti-corruption-layer]] vira o "patinho feio" que absorve a feiura da integração (inclusive acesso ao banco legado), para que nem o legado nem os microsserviços sejam alterados por causa um do outro. [[wiki/concepts/facade-pattern|Facade]] fica do lado do legado (interface estável); [[wiki/concepts/adapter-pattern|Adapters]] do lado dos microsserviços (versões intermediárias, 1..N serviços, coreografia ou orquestração). A camada **não resolve responsabilidade dividida** ([[wiki/concepts/acl-nao-resolve-responsabilidade-dividida]]), custa escala, latência, observabilidade e consistência ([[wiki/concepts/acl-consistencia-transacional-legado-microsservico]]), e tende a virar [[wiki/concepts/acl-permanencia-como-debito-tecnico|débito técnico]]. A decisão é guiada por [[wiki/concepts/acl-requisitos-arquiteturais|requisitos arquiteturais]]: ajuda em time to market, manutenibilidade, integrabilidade e adaptabilidade; degrada performance, escalabilidade e elasticidade. Não usar quando a semântica dos dois sistemas é muito diferente, salvo com versão intermediária ([[wiki/concepts/diferenca-semantica-entre-sistemas]]).

## Key claims

**Claim:** o conceito nasceu no DDD de [[wiki/entities/eric-evans]] para isolar o domínio Core de dependências externas, não para migração; foi trazido ao universo de microservices (referências: microservices.io, Microsoft e o livro de [[wiki/entities/chris-richardson]]).
**Evidence:** "esse padrão ele nasceu lá com o Eric Evans... a iniciativa não era pra gente fazer uma migração... aí eu preciso botar uma camada anticorrupção no meio para garantir que a alteração... não altere o principal."
**Confidence:** alta quanto à origem (coincide com [[wiki/concepts/anti-corruption-layer]] e `[skill: tech-mentor-backend]`, `ddd-advanced.md`); as referências são citadas de memória, não verificadas.

**Claim:** sem a camada, o microsserviço que precisa de dados do banco legado força alterar o legado (passar mais dados, segunda consulta, campo novo), arriscando quebrar tudo que usa aquele método e exigindo re-testar o legado.
**Evidence:** exemplo "pessoa com telefone"; "alterei o método do meu sistema legado que talvez seja utilizado por muitas coisas... vou ter que testar todo o meu legado de novo."
**Confidence:** alta (argumento do autor, coerente).

**Claim:** a camada deve ser **isolada** (microsserviço ou rota dentro de um [[wiki/concepts/api-gateway|API Gateway]]), porque com o tempo os microcomponentes ganham mais responsabilidade que o legado; muitas aplicações, porém, a começam dentro do legado, o que é aceitável se há plano de desligar o legado.
**Evidence:** "com o passar do tempo a gente tende a ter mais responsabilidade lá nos microcomponentes do que no legado... por isso é legal ter isolado."
**Confidence:** média: heurística do autor, sem dados.

**Claim:** a camada é "feia" por natureza, mas a feiura deve ficar do lado legado; alterar tabelas dos microsserviços a partir da camada anula o objetivo da migração (microsserviço autônomo).
**Evidence:** "a minha camada anticorrupção... vai ser feia para caramba... mais pro lado do legado... se começar a ter alterações do lado de cá também em tabelas... é um problema."
**Confidence:** média-alta.

**Claim:** Facade serve ao lado legado (interface comum, "praticamente imutável"); Adapters servem ao lado dos microsserviços (versão intermediária vs. definitiva, parametrização, chamar 1..N serviços, modelo coreografado vs. orquestrado).
**Evidence:** trecho "aqui a gente aplica adapters e a ideia de facade, principalmente daqui pra cá."
**Confidence:** média-alta; **preenche a lacuna** deixada na parte 1 (quando Facade vs. Adapter) com um critério por *lado* da camada, diferente do critério do skill (Adapter = uma interface, Facade = orquestração). Ver [[wiki/questions/acl-facade-vs-adapter-criterio-por-lado-ou-por-chamadas]].

**Claim:** uma camada por subsistema consumidor, mesmo com código duplicado.
**Evidence:** "mesmo que eu tenha código duplicado é recomendável... uma camada de anticorrupção para cada subsistema."
**Confidence:** média; **diverge** da leitura do skill já registrada em [[wiki/concepts/anti-corruption-layer]] (Open Host Service + Published Language no legado para N consumidores). Ver a mesma questão acima.

**Claim:** a camada isola o legado de mudanças tecnológicas (protocolo, versão de runtime/SO) do lado novo.
**Evidence:** exemplo do legado binário monolítico que não suporta HTTP.
**Confidence:** alta como benefício; ilustrativo.

**Claim:** custos: escalar a camada também, manutenção/infra extra, latência extra, mais observabilidade, e permanência que vira débito técnico.
**Evidence:** seção "Problemas a considerar".
**Confidence:** alta (qualitativo, sem números).

**Claim:** transações fortes atravessando a camada são dolorosas (timeout, rollback nos microsserviços, propagação de contexto transacional); com muita dessa dor, trazer a camada para dentro do legado, ao preço de alterar o legado a cada evolução.
**Evidence:** exemplo SOAP + SQL Server; "não tem uma resposta fácil."
**Confidence:** média: detalhes do SOAP/SQL Server vêm do áudio e **não foram verificados** `[external]`.

**Claim:** matriz de requisitos arquiteturais: atendidos (time to market, manutenibilidade, integrabilidade, adaptabilidade), parcialmente (segurança, testabilidade), impactados parcialmente (disponibilidade, observabilidade, experiência) e totalmente (performance, escalabilidade, elasticidade).
**Evidence:** seção final; ver [[wiki/concepts/acl-requisitos-arquiteturais]].
**Confidence:** média: é um julgamento do autor, não medição; a terminologia "atendido/parcial/inferido" é dele e é um pouco ambígua no áudio.

## Cruzamento com o skill (`tech-mentor-backend`)

`[skill: tech-mentor-backend]` (`references/architecture/ddd-advanced.md`, `architecture-patterns-all.md`): confirma ACL como padrão de Context Map e o par Strangler Fig + ACL. O skill **não** cobre a matriz de requisitos arquiteturais, o custo transacional nem a permanência como débito; essas contribuições são só desta fonte. O skill sugere Open Host Service/Published Language para N consumidores, enquanto o autor prefere uma ACL por consumidor.

## Entities & concepts touched

- Novos: [[wiki/concepts/acl-requisitos-arquiteturais]], [[wiki/concepts/acl-consistencia-transacional-legado-microsservico]], [[wiki/concepts/acl-permanencia-como-debito-tecnico]], [[wiki/concepts/acl-nao-resolve-responsabilidade-dividida]], [[wiki/concepts/diferenca-semantica-entre-sistemas]], [[wiki/entities/chris-richardson]], [[wiki/entities/eric-evans]], [[wiki/questions/acl-facade-vs-adapter-criterio-por-lado-ou-por-chamadas]]
- Existentes: [[wiki/concepts/anti-corruption-layer]], [[wiki/concepts/strangler-fig-pattern]], [[wiki/concepts/facade-pattern]], [[wiki/concepts/adapter-pattern]], [[wiki/concepts/saga-pattern]], [[wiki/concepts/distributed-transactions]], [[wiki/concepts/tech-debt]], [[wiki/concepts/observabilidade]], [[wiki/concepts/requisitos-funcionais-e-nao-funcionais]], [[wiki/concepts/bounded-context]], [[wiki/concepts/choreography]], [[wiki/concepts/orchestration]], [[wiki/concepts/mainframe]], [[wiki/concepts/microsservicos]]

## Open questions

- Facade vs. Adapter: critério por lado (autor) ou por nº de chamadas (skill)? Registrado como pergunta.
- Uma ACL por consumidor (autor) vs. OHS + Published Language (skill): qual vale quando o legado é compartilhado?
- Como a camada tratará dependências escondidas (config dinâmica, reflection)? Continua sem resposta (já aberta na parte 1).
- "Inferido" vs. "parcial" na matriz: leitura minha do áudio; o autor não define os termos formalmente.
- Autor, canal e vídeo anteriores não identificados; as referências (Microsoft, livro de Richardson) não têm título/URL.

## Raw quotes

> "a camada anticorrupção não vai resolver as responsabilidades dos dois, ela ajuda a resolver a questão aqui de alterações no sistema A que eu não poderia fazer."

> "essa aqui é um patinho feio... não é um bichinho bonitinho... ela vai ser feia para caramba, mas é mais pro lado do legado."

> "a camada anticorrupção literalmente ajuda nesse sentido: eu quebro esse acoplamento do conhecimento da conexão entre os dois sistemas."

> "a palavra mágica para todo trabalho de arquitetura é um bom planejamento: desenhar bem, pensar no máximo de situações possíveis."
