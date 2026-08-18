---
type: source
title: "Sistema de Mentoria em Golang: Monolito Modular Construído em Live"
aliases: ["veleiro do Lucas Badico", "monolito modular em Go ao vivo", "clone do Calendly em Go"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 0
tags: [go, golang, monolito-modular, grpc, localstack, aws, mentoria, build-in-public, calendly, dynamodb]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/sistema-mentoria-golang-monolito-modular-live-lucas-badico.md"
source_url: ""
author: "Lucas Badico"
date_published: ""
date_ingested: "2026-08-18"
---

## TL;DR

Lucas Badico ([[wiki/entities/lucas-badico]]) apresenta o sistema que constrói em live streams: o "motor" da própria escola de mentoria, em [[wiki/concepts/go-fundamentos|Go]], organizado como [[wiki/concepts/monolito-modular]] com módulos internos (appointment, payment, chatbot, journey) que expõem handlers HTTP e gRPC e podem ser extraídos individualmente para microsserviço no futuro, sem reescrever regra de negócio — só trocar o transporte e clonar o banco de dados. O primeiro módulo implementado é `appointment`, um clone do Calendly que resolve duas dores reais de mentoria: falta de visibilidade de sessões para o mentorado e ~R$50 retidos por mentoria numa plataforma de pagamento subutilizada. Stack: Go no core, PostgreSQL/PostGIS como banco principal, DynamoDB via [[wiki/concepts/localstack|LocalStack]] para desenvolvimento local de AWS, HTTP para clientes externos e gRPC para comunicação interna, com apenas três dependências externas (Gorilla Mux, pacote gRPC do Google, GORM) — o resto vem da standard library.

---

## Reivindicações Principais

**Claim:** Monolito modular resolve o problema prático de "microsserviços demais para um time pequeno cuidar" mantendo o isolamento por módulo — a extração futura para microsserviço é feita módulo por módulo, trocando só a "injeção" no entry point e clonando o banco de dados daquele módulo.
**Evidência:** Descrição da estrutura real do projeto (`app/cmd`, `internal`, `modules/appointment`) e do mecanismo de injeção do handler HTTP no `main.go`; nenhum benchmark ou caso de extração já realizado — é plano declarado, não resultado observado.
**Confiança:** Média-alta — a mecânica descrita (remover import/injeção, criar novo entry point, clonar banco e migrar) é coerente com a prática documentada em [[wiki/concepts/monolito-modular]] e com o critério de extração tardia em [[wiki/concepts/microsservicos]], mas ainda não foi testada em produção pelo autor.

**Claim:** Go, na prática deste projeto, exigiu poucas dependências externas — apenas Gorilla Mux (roteamento HTTP), o pacote gRPC oficial do Google e GORM — com o restante coberto pela standard library.
**Evidência:** Observação direta do autor sobre o próprio código do "Core"; contrastado com o módulo separado ("bot"), que precisou de mais dependências externas.
**Confiança:** Alta como relato de primeira mão sobre este projeto específico; consistente com o padrão mais amplo já documentado em [[wiki/concepts/go-ecossistema]] via [[wiki/sources/golang-profissional-sem-grandes-frameworks]] (mesmo autor, mesma tese: "repetir código é melhor que acoplar a uma lib grande").

**Claim:** O core expõe handlers HTTP (para clientes externos/frontend) e gRPC (para comunicação interna entre módulos/serviços) porque não existe hoje solução boa de gRPC direto no browser.
**Evidência:** Justificativa técnica direta do autor, sem citar grpc-web ou Connect (alternativas reais para gRPC no browser) como tendo sido avaliadas.
**Confiança:** Média-alta — a limitação de gRPC nativo em browsers é real e documentada (exige proxy tipo grpc-web/Envoy), mas a fonte não menciona essas soluções intermediárias, então a alegação de "não ter solução boa" é uma simplificação.

**Claim:** Calendly, no plano gratuito, limita a um único tipo de evento e sincronização com um único calendário — insuficiente para quem precisa de múltiplos tipos de mentoria e múltiplos calendários (pessoal, comercial, futuro profissional).
**Evidência:** Relato de uso pessoal direto do autor como cliente pago/gratuito do produto.
**Confiança:** Média — plausível e específico, mas não verificado independentemente contra a documentação atual do Calendly (limites de plano mudam com o tempo).

**Claim:** Configurar uma stack local de AWS via LocalStack (para Lambdas e DynamoDB) levou 6 horas e foi o primeiro vídeo do projeto.
**Evidência:** Relato direto de primeira mão sobre o próprio processo de setup.
**Confiança:** Alta como relato pessoal; não generalizável como estimativa de esforço padrão de LocalStack (depende de quantos serviços AWS estão sendo emulados).

---

## Entidades Mencionadas

- [[wiki/entities/lucas-badico]] — autor, dev mentor, criador de conteúdo
- Nest.js (framework citado como referência de monolito modular bem implementado, mencionado sem entusiasmo do autor) — sem página própria na wiki

## Conceitos Tocados

- [[wiki/concepts/monolito-modular]]
- [[wiki/concepts/microsservicos]]
- [[wiki/concepts/database-per-service]]
- [[wiki/concepts/go-arquitetura]]
- [[wiki/concepts/go-ecossistema]]
- [[wiki/concepts/grpc]]
- [[wiki/concepts/dynamodb]]
- [[wiki/concepts/localstack]]
- [[wiki/concepts/redis]]
- [[wiki/concepts/mentoria-tecnica]]
- [[wiki/concepts/build-in-public]]
- [[wiki/concepts/hexagonal-architecture]]

## Open Questions

- Não fica claro como o event bus / comunicação entre módulos será feita quando não for chamada direta via interface — a fonte menciona só a extração futura via gRPC, sem mecanismo de eventos de domínio in-process, diferente do padrão descrito em [[wiki/concepts/monolito-modular]] (event bus interno que "vira Kafka").
- Autenticação/autorização e observabilidade são citadas explicitamente como desafios **ainda não resolvidos** ("arquitetura modular tá só embrionária") — candidatos naturais para uma fonte de acompanhamento futura quando essas lives acontecerem.
- Não há detalhe de como o Redis será usado "além de cache" nos módulos futuros — a fonte promete isso sem especificar caso de uso (rate limiting? pub/sub? distributed lock?).
- Escolha de GORM contradiz parcialmente a recomendação de [[wiki/concepts/go-ecossistema]] (sqlc/sqlx preferidos a GORM em produção com queries críticas) — não é uma contradição direta de fato, mas um trade-off que a fonte não discute.

## Raw Quotes

> "Eu queria pegar a ideia de monolito modular que eu vi muitos projetos aplicando, inclusive o Nest, que eu não gosto tanto, mas ele implementa essa ideia muito bem — eu falei: eu quero aplicar isso em Go."

> "Digamos que payment eu preciso delegar para um time específico que vai trabalhar só com payment e vai querer ter todo o controle do payment isolado: eu só removo a injeção do payment desse entry point, faço um novo entry point só para payment, e eles estão isolados."

> "Consigo pensar em três libs do Go que eu tô usando no projeto: um é o Gorilla Mux, para HTTP; outro é o pacote de RPC do próprio Google; e outro é o GORM."

> "A arquitetura modular tá só embrionária — a gente tem que resolver como vamos lidar com logs, como vamos lidar com observabilidade, como vamos lidar com autorização e autenticação."
