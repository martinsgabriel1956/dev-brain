---
type: concept
title: "Monolito Modular"
aliases: ["monolito modular", "modular monolith", "majestic monolith", "bounded modules"]
date_created: 2026-08-10
date_updated: 2026-08-18
source_count: 5
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

## Garantias

Contratos entre módulos garantem [[wiki/concepts/separation-of-concerns]] e [[wiki/concepts/encapsulamento]]. Relacionado a [[wiki/concepts/contrato-de-api]] (aqui o "contrato" é in-process, não necessariamente HTTP). Ver também a variante frontend em [[wiki/concepts/monolito-modular-frontend]].

## Key sources

- [[wiki/sources/monolith-first-martin-fowler]] — fonte primária de Monolith First: MicroservicePremium, YAGNI e dificuldade de bounded contexts como os dois argumentos que justificam o monolito modular como etapa inicial
- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — segunda implementação de referência (C#), enquadramento formal via Monolith First de Fowler
- [[wiki/sources/arquitetura-de-sacrificio]] — boa modularidade é o que permite *sacrificar módulos individuais* em vez do sistema inteiro conforme ele cresce (Fowler)
- [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]
- [[wiki/sources/sistema-mentoria-golang-monolito-modular-live-lucas-badico]] — implementação concreta em Go (módulos com handler/model/repository/service, entry points HTTP e gRPC separados) e extração via clone de banco
