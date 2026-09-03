---
type: concept
title: "Microsserviços"
aliases: ["microsservicos", "microservices", "arquitetura de microsserviços", "decomposição por domínio"]
date_created: 2026-07-24
date_updated: 2026-09-01
source_count: 19
tags: [microsservicos, arquitetura, bounded-context, distributed-monolith, circuit-breaker, resiliencia]
skill: tech-mentor-backend
status: draft
---

# Microsserviços

Estilo arquitetural em que o sistema é dividido em serviços pequenos e independentes, cada um responsável por uma parte específica do negócio (ex.: pagamentos, usuário, notificações). Cada microsserviço roda isolado, tem seu próprio banco de dados se bem implementado, e pode ser desenvolvido, implantado e escalado independentemente dos demais. A comunicação entre serviços acontece via API (REST, RPC) ou mensageria assíncrona (filas, eventos).

Raízes em arquitetura orientada a serviços do início dos anos 2000; popularizou-se a partir de 2014 com o artigo de Martin Fowler e James Lewis, e virou hype ao longo da década seguinte — inclusive como efeito manada, com projetos adotando o estilo desde o início sem necessidade real de escala ou de times separados. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## O Artigo Original de 2014 (Fowler & Lewis)

[[wiki/sources/microsservicos-martin-fowler-james-lewis]] é o artigo-fonte que cunhou a definição hoje citada universalmente: um estilo de desenvolver uma aplicação única como um conjunto de pequenos serviços, cada um rodando no próprio processo, comunicando-se via mecanismos leves (tipicamente API HTTP), construídos em torno de **capacidades de negócio**, implantáveis por esteira totalmente automatizada, com o mínimo de gerenciamento centralizado. Os autores enumeram nove características comuns (não uma definição formal e obrigatória, já que nem toda arquitetura de microsserviços tem todas): Componentização via Serviços, Organização em Torno de Capacidades de Negócio, Produtos não Projetos, Endpoints Inteligentes e Tubos Burros ("smart endpoints, dumb pipes" — em oposição a ESBs, citando a frase de Jim Webber de que ESB significa "Erroneous Spaghetti Box"), Governança Descentralizada, Gerenciamento de Dados Descentralizado ([[wiki/concepts/circuit-breaker|Polyglot Persistence]]), Automação de Infraestrutura, Design for Failure e Design Evolutivo.

Ponto frequentemente perdido em resumos populares do artigo: os próprios autores **não** afirmam que microsserviços sejam definitivamente "o futuro" da arquitetura de software — encerram com "otimismo cauteloso", reconhecendo que fronteiras de serviço mal definidas são caras de refatorar entre processos (ao contrário de bibliotecas em processo), que complexidade pode simplesmente se deslocar do interior de um componente para as conexões confusas entre eles, e que um time pouco habilidoso constrói um sistema ruim independentemente do estilo escolhido — as verdadeiras consequências de uma decisão arquitetural, segundo eles, só ficam evidentes anos depois.

## Origem no Debate sobre SOA e a Lei de Conway

O artigo posiciona a decomposição por capacidade de negócio como reação direta à [[wiki/concepts/contexto-organizacional-para-arquitetura|Lei de Conway]] em ação: quando a gestão divide o time por camada técnica (times de UI, de lógica de servidor, de banco), cada mudança simples vira um projeto entre times, e a lógica de negócio acaba forçada para dentro de qualquer camada com acesso mais fácil — "lógica em todo lugar". A citação central de Melvin Conway (1968) — "qualquer organização que projeta um sistema produzirá um design cuja estrutura é uma cópia da estrutura de comunicação da organização" — é o mesmo argumento que, em outro artigo de Fowler de 2003, já aparecia aplicado à própria noção de fronteira de aplicação; ver [[wiki/concepts/application-boundary]].

Quanto a SOA: o artigo reconhece mérito na comparação (microsserviços é próximo do que "advocates de SOA" já defendiam), mas argumenta que o rótulo "SOA" acumulou significados contraditórios demais — na prática, a maioria das implementações chamadas de "SOA" tinha foco em ESBs integrando monolitos, com governança centralizada que ativamente inibia mudança. Daí a necessidade de um termo mais preciso.

## Decomposição Correta

O critério correto é decompor por **[[wiki/concepts/ddd-strategic|bounded context]]** (domínio de negócio), não por camada técnica. "Serviço de dados" + "Serviço de API" é um [[wiki/concepts/distributed-monolith|distributed monolith]] técnico disfarçado de microsserviços; "Orders Service" + "Payments Service" é decomposição real por domínio, com dados isolados e deploy independente.

## O Percurso Didático de Problemas: Deadlock → 2PC → Saga → CQRS

Uma aula constrói, problema por problema, o percurso que leva um microsserviço de banco compartilhado a uma arquitetura madura: banco compartilhado entre serviços causa [[wiki/concepts/deadlock]] → isolar banco por serviço ([[wiki/concepts/database-per-service]]) resolve o deadlock mas quebra atomicidade entre serviços (o "A" do [[wiki/concepts/acid]]) → [[wiki/concepts/two-phase-commit]] resolve a atomicidade mas não escala além de poucos serviços → [[wiki/concepts/saga-pattern]] via fila ([[wiki/entities/rabbitmq]]) e [[wiki/concepts/event-driven-architecture]] resolve o gargalo ao custo de compensação manual → escalar o banco separando leitura e escrita ([[wiki/concepts/cqrs]] com [[wiki/concepts/read-replicas]]) introduz replication lag. Reforça o argumento central desta página de que microsserviços trazem complexidade operacional real (consistência distribuída, latência de rede) que precisa ser resolvida com padrões específicos, não é "só separar em serviços menores". Ver [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]].

## Custo-Benefício

**Benefícios:** escalabilidade seletiva (escalar só o serviço que precisa), times menores e autônomos trabalhando em paralelo, maior resiliência (falha de um serviço não derruba necessariamente o sistema inteiro).

**Custos:** complexidade operacional bem maior — consistência de dados distribuída, latência de rede entre serviços, observabilidade sobre múltiplos serviços, orquestração de deploy, e padrões de resiliência obrigatórios ([[wiki/concepts/circuit-breaker]], retry, timeout) para lidar com falhas parciais que não existiam num processo único.

Segundo `references/architecture-foundations.md` da skill `tech-mentor-backend`, monolito modular é o ponto de partida correto para ~90% dos casos — o caminho arquitetural saudável é monolito bem modularizado → extrair microsserviço quando há necessidade real (escala diferente, time separado, deploy independente), não o inverso.

[[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] nomeia esse trade-off com um vocabulário próprio, complementar ao já registrado: microsserviços resolvem **complexidade local** (código de cada serviço pequeno, isolado, baixa carga cognitiva) ao custo de nova **complexidade global** (comunicação entre serviços, deploy orquestrado, consistência distribuída, monitoramento fragmentado) — a mesma conta de custo operacional já documentada acima, agora com um mecanismo concreto de meio-termo: em vez de saltar direto para microsserviços, é possível recombinar módulos de domínio em diferentes processos de deploy a partir do mesmo codebase ([[wiki/concepts/composicao-de-modulos|composição de módulos]] via [[wiki/concepts/monorepo-backend|monorepo]]), adiando o momento em que vale pagar o preço de repositórios/pipelines/infraestrutura separados.

## Microsserviços Não Compõem

[[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] nomeia uma limitação estrutural específica de microsserviços, não registrada antes nesta forma: eles **não compõem** — não é possível colocar vários microsserviços dentro de uma mesma app/processo, porque cada um vive em codebase/repositório/pipeline próprios. Em contraste, módulos de domínio organizados num monorepo (ver [[wiki/concepts/arquitetura-modular]] e [[wiki/concepts/composicao-de-modulos]]) podem ser recombinados em "infinitas" apps diferentes a partir do mesmo código. É um argumento novo a favor da tese central desta página (monolito modular como ponto de partida correto): a componibilidade é uma vantagem que microsserviços perdem estruturalmente ao se dividirem em codebases separados.

## Microsserviços São Só um Codebase Singular Menor

[[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] traz um ângulo complementar ao argumento acima: internamente, um microsserviço continua sendo um **codebase singular** — a mesma limitação estrutural de um monolito tradicional, só que menor. A transição de monolito para microsserviços não mudou como padrões como [[wiki/concepts/clean-architecture]]/[[wiki/concepts/hexagonal-architecture]] são aplicados dentro de cada serviço; quem resolve isso é a [[wiki/concepts/arquitetura-modular|arquitetura modular]], que divide o mesmo codebase em módulos com tipos e responsabilidades explícitos (ver [[wiki/concepts/tipos-de-modulos]]).

## Microsserviços como Eixo de Aprendizado (Não Só Estilo Arquitetural)

[[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] argumenta que o valor de estudar microsserviços vai além de saber implementá-los em produção: o estudo funciona como um eixo unificado que amarra, de forma organizada e com propósito definido, uma dezena de conceitos avançados e dispersos de arquitetura — [[wiki/concepts/circuit-breaker|circuit breaker/retry/timeout]], [[wiki/concepts/observabilidade]], [[wiki/concepts/saga-pattern|saga pattern/consistência eventual]], [[wiki/concepts/mensageria|comunicação assíncrona]], contratos de API versionados, e cultura de times autônomos. Cada um desses conceitos se aplica integralmente dentro de um monólito ou backend único — não são exclusividade de sistemas distribuídos. O relato de primeira mão do autor: usar o hype de microsserviços de 2014 como norte de estudo, vindo de uma bagagem de sistemas distribuídos, foi o que o trouxe de volta ao mercado depois de quase 10 anos preso a monólitos legados.

## Reaproveitando Peças Prontas do Ecossistema

Mesmo fora de uma arquitetura de microsserviços completa, dá para reaproveitar componentes prontos desse ecossistema — ex.: Keycloak como serviço de autenticação/autorização (incluindo federação), evitando reinvestir tempo em um requisito já resolvido por software livre estabelecido. Ver [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]].

## Opinião Estável ao Longo da Carreira: Microsserviços Exigem Justificativa

[[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] (Chris Kiehl) lista, entre as opiniões que **não** mudaram em 6 anos de carreira, que "monólitos são pretty good na maioria das circunstâncias" e "microsserviços exigem justificativa" — reforço direto e independente do argumento central já documentado nesta página (monolito modular como ponto de partida correto, extração só com necessidade real).

## Decisão Atribuída a Sênior-Plus

[[wiki/concepts/niveis-de-senioridade-system-design]] situa a decisão monolito vs. microsserviços — junto de SQL vs. NoSQL e serverless vs. servidor dedicado — como tipicamente atribuída a "sênior plus" (tech lead/CTO/staff), no contexto de desenvolver um sistema inteiro do zero para uma equipe trabalhar em cima. Em entrevista, essa mesma decisão aparece como um dos principais focos de discussão de tradeoffs no nível sênior.

## O Mesmo Princípio de Extração Tardia no Frontend

[[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] reforça, do lado frontend, a mesma tese de ponto de partida: [[wiki/concepts/monolito-modular-frontend|monolito modular]] com fronteiras por domínio é a base, [[wiki/concepts/vertical-slice-architecture|vertical slice]] isola funcionalidades complexas dentro do módulo, e só se migra para [[wiki/concepts/microfrontend-baseado-em-rotas|builds separados]] ou [[wiki/concepts/microfrontends-parciais|microfrontends distribuídos]] com necessidade real — nunca por hype ou pela imagem "arquitetura distribuída = madura" vendida em posts de LinkedIn.

## Sharding de Banco Como Consequência, Não Ponto de Partida

[[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] fecha o argumento pelo lado da persistência: não faz sentido tentar fazer [[wiki/concepts/sharding]] de um monolito inteiro com centenas de tabelas, porque não existe uma única entidade central óbvia para servir de shard key. A ordem correta é decompor primeiro por [[wiki/concepts/ddd|DDD]]/bounded context, e só então shardear o banco de dados de um microsserviço específico (onde a entidade principal — usuário, pedido, paciente — já está isolada). Reforça, de um ângulo de banco de dados, a mesma tese já central desta página: decomposição primeiro, escala de infraestrutura depois.

## O ESB Como o "Antigo Barramento Central" Que "Smart Endpoints, Dumb Pipes" Rejeita

[[wiki/concepts/esb-enterprise-service-bus|ESB]] não é só uma referência histórica dentro do artigo de Fowler/Lewis — é a peça concreta que a filosofia de microsserviços rejeitava na prática: em vez de concentrar transformação de mensagens e orquestração num barramento central, cada serviço vira responsável pela própria lógica, comunicando-se por mecanismos leves. Isso não significa que o ESB tenha desaparecido: em empresas com grande legado tecnológico, ele continua sendo a peça que integra sistemas de épocas diferentes enquanto a migração para uma arquitetura mais distribuída acontece de forma incremental.

## O Pré-requisito Organizacional: Plataforma e Fim do Acoplamento de Backlog

Times pequenos e autônomos — um dos benefícios centrais de microsserviços — só se sustentam se a infraestrutura for self-service. [[wiki/sources/talk-about-platforms-evan-bottcher]] mostra o lado organizacional: sem uma [[wiki/concepts/plataforma-digital|plataforma digital]] com [[wiki/concepts/sensible-defaults-paved-road|sensible defaults]], a autonomia dos times de serviço vira ou [[wiki/concepts/backlog-coupling|acoplamento de backlog]] (dependência de times de infra por silo técnico) ou arrasto por diversificação tecnológica (cada time reinventa sua stack). É a mesma Lei de Conway do artigo original de 2014, agora aplicada à camada de entrega/infra.

## O Caso Amazon Prime Video: Monolito Reduzindo Custo em >90%

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] cita o caso (amplamente reportado, sem link primário na fonte) da equipe de monitoramento de qualidade de vídeo do Amazon Prime Video migrando de volta de microsserviços/serverless distribuído para um monolito, reduzindo custos de infraestrutura AWS em mais de 90% — com menor complexidade sistêmica e mais eficiência operacional. Funciona como contraponto concreto ("nem as gigantes de tecnologia estão imunes ao custo de microsserviços prematuros ou superdimensionados") ao argumento já central desta página; ver [[wiki/concepts/monolito]] para a claim completa e as ressalvas de verificação.

## Monolith First (Martin Fowler): a Formalização da Sequência

[[wiki/concepts/monolith-first]] é o princípio de Fowler que nomeia formalmente a sequência já documentada nesta página em "Custo-Benefício": quase toda história de microsserviços bem-sucedida começou como monolito que cresceu e foi quebrado depois; quase todo sistema criado do zero já como microsserviços teve sérios problemas. [[wiki/sources/microsservicos-monolito-first-renato-augusto]] conecta essa observação diretamente à falta de conhecimento de domínio no início de um projeto — o mesmo argumento central da seção "Decomposição Correta" acima.

## Critério Prático de Decisão: Proporção Leitura:Escrita

[[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] usa um exemplo concreto e mensurável para decidir monolito vs. microsserviços, em vez de tratar a escolha como debate abstrato: um encurtador de URL com proporção leitura:escrita de 100:1 (100M redirects/dia vs. 1M criações/dia) justifica decompor em microsserviços porque permite escalar só o serviço de redirect, sem escalar a unidade inteira junto — a mesma vantagem de "escalabilidade seletiva" já registrada acima em Custo-Benefício, aqui ancorada num número de tráfego específico em vez de um argumento genérico.

## Origem Histórica: de SOA/ESB (2005) ao Nome Consolidado (2012)

[[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] completa, por um ângulo mais antigo, a linha do tempo que o artigo de Fowler/Lewis (2014) já documenta acima: em 2005, Peter Rogers cunhou o termo "microweb service" numa conferência (Web Services Edge), propondo serviços enxutos e REST como contraponto direto ao [[wiki/concepts/esb-enterprise-service-bus|SOA/ESB]] então dominante — barramento central, serviços robustos/genéricos, [[wiki/concepts/soap|SOAP]] com XML verboso. Só em 2012 um grupo de arquitetos consolidou o nome "microsserviços", no mesmo ano em que a apresentação "Microservices — Java, the Unix Way" (Polônia) trouxe a analogia com a filosofia Unix — processos pequenos, responsabilidade única, composição para resolver problemas maiores. A fonte não relaciona essa apresentação de 2012 ao artigo formal de Fowler/Lewis (2014) — em aberto se são desenvolvimentos independentes convergindo no mesmo nome.

A mesma fonte formaliza, de maneira mais enxuta que as nove características de Fowler/Lewis, três requisitos práticos para um serviço contar como microsserviço: **standalone** (funciona sozinho), **deploy independente** (entrega não depende de outra aplicação) e **funcionalidade útil** dentro de um domínio — compatível com o critério de extração já citado acima em "Custo-Benefício" (`references/architecture-foundations.md` da skill).

## O Desafio Menos Discutido: Capacitação do Time

Além dos desafios técnicos já listados em "Custo-Benefício" (consistência distribuída, latência, observabilidade), [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] destaca um desafio organizacional pouco coberto nos materiais sobre o tema: sob pressão de prazo, desconhecimento do time ou falha na gestão técnica, é comum implementar só parte das estratégias de descentralização — parar no meio do caminho e abrir mão de práticas essenciais, como banco por serviço ou compartilhamento correto de bibliotecas de código. Segundo o autor, essa é a diferença real entre projetos com chance de dar certo e projetos fadados a serem reescritos assim que a complexidade cresce — reforça, por um ângulo de capacitação/gestão de time (não só arquitetura técnica), o mesmo padrão já central nesta página de "distributed monolith como sintoma de microsserviços malfeitos".

A mesma fonte reafirma a regra de acesso exclusivo via API (nunca via banco compartilhado) como o ponto mais importante a reter sobre o modelo — mas sinaliza que um vídeo futuro da série vai relativizar essa regra se aplicada sem cuidado; até essa fonte ser ingerida, a wiki trata "database per service" como regra praticamente absoluta (ver [[wiki/concepts/database-per-service]]).

## Key Sources

- [[wiki/sources/microsservicos-historia-soa-esb-bernardo-lobato]] — origem histórica (Peter Rogers 2005, SOA/ESB como contraponto, "Microservices — Java, the Unix Way" 2012), três requisitos práticos (standalone, deploy independente, funcionalidade útil), e o desafio de capacitação de time como diferença entre projetos que dão certo e os que fracassam
- [[wiki/sources/como-projetar-sistemas-encurtador-de-urls-passo-a-passo]] — critério de decisão monolito vs. microsserviços ancorado na proporção leitura:escrita (100:1) de um caso concreto (encurtador de URL)
- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária: MicroservicePremium, os quatro caminhos práticos de execução, e o contra-argumento reconhecido por Fowler a favor de começar direto com microsserviços em substituições de sistema
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — caso Amazon Prime Video, princípio Monolith First de Fowler nomeado explicitamente, YAGNI como mecanismo por trás da recomendação de não começar com microsserviços
- [[wiki/sources/arquitetura-de-sacrificio]] — Fowler **desaconselha** microsserviços como arquitetura de sacrifício (distribuição + assincronia = amplificadores de complexidade); melhor monolito primeiro, desmontado gradualmente depois
- [[wiki/sources/tecnologias-hype-passado-soap-xml-esb-jquery-cobol]] — ESB como contraponto histórico direto ao "smart endpoints, dumb pipes"; por que ESBs continuam essenciais em empresas com grande legado mesmo perdendo espaço em projetos novos
- [[wiki/sources/microsservicos-martin-fowler-james-lewis]] — artigo original de 2014 (James Lewis e Martin Fowler) que cunhou a definição do termo; nove características comuns, "smart endpoints and dumb pipes", Lei de Conway, Design for Failure, e a postura de "otimismo cauteloso" dos próprios autores
- [[wiki/sources/microsservicos]] — decomposição por bounded context, distributed monolith como anti-pattern, padrões de resiliência obrigatórios
- [[wiki/sources/talk-about-platforms-evan-bottcher]] — o pré-requisito organizacional: plataforma self-service para sustentar times autônomos sem acoplamento de backlog
- [[wiki/sources/vale-a-pena-estudar-microsservicos-mesmo-sem-usar]] — microsserviços como guia/eixo de aprendizado de arquitetura, hype de 2014 em perspectiva histórica, relato pessoal de carreira, Keycloak como peça pronta reaproveitável
- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — microsserviço como "codebase singular menor", mesma limitação estrutural do monolito tradicional que só a arquitetura modular resolve
- [[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] — "microsserviços exigem justificativa" como opinião estável (não mudou em 6 anos), reforçando a mesma tese por um ângulo independente
- [[wiki/sources/system-design-por-nivel-junior-pleno-senior]] — monolito vs. microsserviços como decisão de sênior-plus, e como tópico de tradeoff cobrado em entrevista sênior
- [[wiki/sources/arquitetura-frontend-microfrontends-monolito-modular-vertical-slice]] — mesmo princípio de extração tardia (monolito modular → vertical slice → builds separados) aplicado à arquitetura frontend
- [[wiki/sources/microsservicos-do-zero-deadlock-2pc-saga-cqrs]] — percurso didático incremental deadlock → database-per-service → 2PC → Saga Pattern → CQRS, construindo problema por problema
- [[wiki/sources/sharding-charging-fragmentacao-banco-de-dados]] — sharding de banco como consequência da decomposição por DDD, não como técnica aplicável a um monolito inteiro
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]] — microsserviços eliminam o [[wiki/concepts/code-espaguete]] por impossibilidade estrutural (serviço não chama função de outro), mas a troca chamada-de-função→chamada-de-rede traz latência e overhead que só compensam com razão real de hardware/escala; o [[wiki/concepts/monolito-modular]] como etapa anterior que facilita a extração futura
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — tática concreta de extração: clonar o banco de dados compartilhado e rodar migração isolada a partir dele, no momento em que um módulo (ex.: payment) ganha time dedicado — ver [[wiki/concepts/database-per-service]]
- [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] — vocabulário complexidade local vs. global, e [[wiki/concepts/composicao-de-modulos|composição de módulos]] via monorepo como meio-termo concreto antes de pagar o preço de microsserviços de fato
- [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] — "microsserviços não compõem" como limitação estrutural frente à componibilidade de [[wiki/concepts/arquitetura-modular|arquitetura modular]]; dois motivos concretos (virtualização + aprendizado de décadas) para o retorno de monolitos modulares
