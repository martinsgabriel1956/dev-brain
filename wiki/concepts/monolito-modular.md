---
type: concept
title: "Monolito Modular"
aliases: ["monolito modular", "modular monolith", "majestic monolith", "bounded modules"]
date_created: 2026-08-10
date_updated: 2026-09-01
source_count: 8
tags: [monolito-modular, monolito, arquitetura, ports-adapters, migracao, backend]
skill: tech-mentor-backend
status: draft
---

# Monolito Modular

Arquitetura em que o sistema continua sendo **um único artefato** (um deploy, um banco, um runtime), mas é internamente dividido em **módulos com fronteiras explícitas**. Os módulos **não** chamam funções internas uns dos outros: comunicam-se por **contratos/interfaces** ([[wiki/concepts/hexagonal-architecture|Ports & Adapters]]), do mesmo jeito que uma classe expõe getters/setters para o mundo externo. Isso captura o benefício de isolamento dos [[wiki/concepts/microsservicos]] — e o fim do [[wiki/concepts/code-espaguete]] — **sem** os contras da comunicação via rede e do overhead de DevOps distribuído.

## Por que existe

É a resposta à pergunta "dá para aproveitar alguns prós de microsserviços sem alguns contras?". Prós desejados: melhor isolamento + coibir o código-sopa. Contras evitados: comunicação via protocolos de rede (mais lenta que chamada de função, só justificável por razão de hardware/escala) e DevOps complexo. O objetivo prático é **fazer os desenvolvedores tropeçarem menos uns nos outros** mantendo a code base razoável de manter. Ver [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]].

## Etapa de transição MVP → empresa madura

O monolito modular é a **etapa intermediária** entre um [[wiki/concepts/monolito]] pequeno de MVP e o eventual salto para microsserviços. Como as interfaces entre módulos já estão expostas, extrair um módulo depois (ex.: mover IA para GPUs próprias) é só trocar o **transporte**: chamada de função → gRPC. Convergente com o skill `tech-mentor-backend`: comece como módulo no monolito; extraia quando o módulo tiver time dedicado, SLA independente ou escala diferente — extrair *antes* de ter módulo bem definido gera **distributed monolith**.

## Implementação Concreta em Go

[[wiki/entities/lucas-badico]] aplica o padrão em Go num sistema de mentoria construído em live: `app/` é o Core, dividido em `cmd/` (entry points HTTP e [[wiki/concepts/grpc|gRPC]] separados), `internal/` (recursos compartilhados) e `modules/` (um pacote por módulo, ex. `appointment/`, futuramente `payment/` e `journey/`), cada módulo com sua própria fatia de `handler/`, `model/`, `repository/` e `service/`. A extração de um módulo é literal: remover a injeção do handler daquele módulo no `main.go` do entry point atual, criar um novo entry point exclusivo para ele, e clonar o banco de dados compartilhado para rodar migração isolada a partir dali — ver [[wiki/concepts/database-per-service]]. Ver [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]].

## Segunda Implementação de Referência: C# (`src/modules/`)

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] cita um segundo exemplo público de referência, em C#, ao lado da implementação em Go de [[wiki/entities/lucas-badico]] documentada acima: um repositório com `src/modules/` contendo módulos como `administration`, `meetings`, `payments`, `registration`, `user-access`, cada um seguindo a mesma estrutura de camadas — aplicação (use cases), domínio (entidades) e testes (unidade/integração). A fonte descreve essa estrutura como "uma mistura de Clean Architecture com DDD": o DDD delimita os bounded contexts (os módulos), e a Clean Architecture separa cada módulo internamente em camadas.

## Monolith First (Martin Fowler): o Enquadramento Formal desta Etapa

[[wiki/concepts/monolith-first]] nomeia formalmente o papel do monolito modular nesta sequência: é o "caminho de baixo" na imagem do bliki de Fowler (módulos = bounded contexts bem definidos), em oposição ao "caminho de cima" de ir direto para microsserviços sem conhecimento de domínio suficiente (ilustrado com dragões). Só depois que o monolito modular atinge maturidade suficiente para se identificar bounded contexts bem definidos é que faz sentido estrangular o monolito e extrair módulos para [[wiki/concepts/microsservicos]] — mesma tese já documentada acima em "Etapa de transição MVP → empresa madura".

## Monolito é uma Escolha de Deploy: Separação de Execução via Múltiplos Entrypoints

[[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] traz um mecanismo concreto que reformula a fronteira entre "monolito" e "não-monolito": num exemplo em NestJS, o mesmo codebase tem dois `main.ts` — um inicializa todos os módulos de domínio (content, identity, billing) como o monolito completo, outro (`video-processor-worker-main`) inicializa **só** o módulo de processamento de vídeo, rodando como processo/build Docker separado. Nenhum microsserviço isolado foi criado (sem repositório, pipeline ou infraestrutura próprios) — é o mesmo codebase modularizado de forma que um módulo roda totalmente separado sem precisar importar o outro. A tese central da fonte: **monolito é uma escolha de deploy, não uma propriedade fixa do codebase**.

**Limite desse estágio**: como os módulos ainda compartilham o mesmo codebase/deploy-base, uma mudança num módulo (ex.: identity) pode forçar redeploy de um processo que nem depende diretamente dele (ex.: o worker de vídeo). Esse é exatamente o ponto em que a fonte recomenda evoluir para [[wiki/concepts/composicao-de-modulos|composição de módulos]] via [[wiki/concepts/monorepo-backend|monorepo]] — reestruturar em `packages/` (módulos de domínio puros) + `apps/` (bootstraps), permitindo compor módulos em combinações arbitrárias sem essa dependência de redeploy cruzado. A mesma fonte também nomeia um nível intermediário de granularidade, [[wiki/concepts/servicos-de-dominio|serviços de domínio]] (monolitos menores agrupados por domínio), entre o monolito único e o monolito modular clássico documentado acima.

## Monolito Modular vs. Arquitetura Modular: uma Distinção Formal

[[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] formaliza, com nomes próprios, a mesma distinção da seção acima: **monolito modular** é um único deploy carregando todos os módulos (mesmo com `main.ts` alternativos para submódulos isolados, como já documentado); **[[wiki/concepts/arquitetura-modular|arquitetura modular]]** é o nível seguinte — múltiplos monolitos/apps, cada um compondo um subconjunto arbitrário dos módulos a partir do mesmo codebase via monorepo. A fonte lista **10 princípios** nomeados para escalar essa arquitetura (limites bem definidos, componibilidade, independência, isolamento de estado, comunicação explícita, substituibilidade, deploy independente, escala independente, monitoramento, falhas isoladas) — ver página dedicada em [[wiki/concepts/arquitetura-modular]] para a lista completa. Argumento novo: microsserviços **não compõem** (não cabem vários dentro da mesma app/processo, por viverem em codebases diferentes), enquanto módulos de domínio num monorepo podem ser recombinados infinitamente — essa é, segundo a fonte, a razão pela qual "ninguém fala sobre arquitetura modular", mesmo sendo onde está a escala real.

## Três Tipos de Módulo Dentro do Monolito Modular

[[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] (mesmo autor, mesmo exemplo de código "Fake Flix") nomeia o que costuma virar módulo dentro de um monolito modular: **módulos de domínio** (billing, content, identity — abrangentes, do tamanho de um microsserviço ou maiores), **módulos de infraestrutura pura** (HTTP, logger, persistência — genéricos, plugáveis em qualquer módulo de domínio sem alteração) e **módulos de feature**, que o autor evita por perderem o bounded context e gerarem acoplamento ao compartilhar entidades. Dentro de cada módulo de domínio, o autor separa ainda **Core** (lógica de negócio) de **Supporting Infrastructure** (controllers/repositórios — infraestrutura contextual, não genérica) — ver taxonomia completa em [[wiki/concepts/tipos-de-modulos]].

## Garantias

Contratos entre módulos garantem [[wiki/concepts/separation-of-concerns]] e [[wiki/concepts/encapsulamento]]. Relacionado a [[wiki/concepts/contrato-de-api]] (aqui o "contrato" é in-process, não necessariamente HTTP). Ver também a variante frontend em [[wiki/concepts/monolito-modular-frontend]].

## Key sources

- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária de Monolith First: MicroservicePremium, YAGNI e dificuldade de bounded contexts como os dois argumentos que justificam o monolito modular como etapa inicial
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — segunda implementação de referência (C#), enquadramento formal via Monolith First de Fowler
- [[wiki/sources/arquitetura-de-sacrificio]] — boa modularidade é o que permite *sacrificar módulos individuais* em vez do sistema inteiro conforme ele cresce (Fowler)
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — implementação concreta em Go (módulos com handler/model/repository/service, entry points HTTP e gRPC separados) e extração via clone de banco
- [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] — "monolito é uma escolha de deploy": múltiplos entrypoints (`main.ts`) fazendo bootstrap de diferentes subconjuntos de módulos a partir do mesmo codebase; limite (redeploy cruzado) e evolução para [[wiki/concepts/composicao-de-modulos]] via monorepo
- [[wiki/sources/os-10-principios-arquitetura-modular-valdemar-neto]] — distinção formal monolito modular vs. [[wiki/concepts/arquitetura-modular|arquitetura modular]], os 10 princípios para escalar arquitetura modular, argumento de que microsserviços não compõem
- [[wiki/sources/tres-tipos-de-modulos-arquitetura-modular-valdemar-neto]] — os três tipos de módulo (domínio, infraestrutura pura, feature) e a estrutura interna Core/Supporting Infrastructure/Infraestrutura Pura
