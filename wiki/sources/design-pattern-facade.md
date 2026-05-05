---
type: source
title: "Facade — Padrão de Projeto Estrutural (Refactoring Guru)"
aliases: ["refactoring guru facade", "facade pattern guru"]
date_created: 2026-05-05
date_updated: 2026-05-05
source_count: 0
tags: [design-patterns, structural, facade, gof, subsistema, encapsulamento]
skill: tech-mentor-backend
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/design-pattern-facade.md
source_url: https://refactoring.guru/pt-br/design-patterns/facade
author: "Refactoring Guru"
date_published: ""
date_ingested: 2026-05-05
---

# Facade — Padrão de Projeto Estrutural (Refactoring Guru)

Artigo canônico do Refactoring Guru sobre o padrão Facade. Fonte primária com estrutura, pseudocódigo, aplicabilidade e relações com outros padrões.

## TL;DR

[[facade-pattern]] fornece uma interface simplificada para um subsistema complexo. O cliente fala com a Fachada; o subsistema não sabe que ela existe. O principal risco é virar um [[god-object]] se acumular responsabilidades demais.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Facade isola o cliente da complexidade do subsistema | Exemplo do VideoConverter: cliente chama um método, internamente orquestra 6 classes de terceiros | Alto |
| O subsistema não está ciente da fachada | "As classes do subsistema não estão cientes da existência da fachada. Elas operam dentro do sistema e trabalham entre si diretamente." | Alto |
| Facade pode virar God Object | "Uma fachada pode se tornar um objeto deus acoplado a todas as classes de uma aplicação." | Alto |
| Facade ≠ Adapter | Facade define *nova* interface para um subsistema; Adapter torna interface *existente* utilizável para um objeto | Alto |
| Facade ≠ Mediator | Facade simplifica acesso sem introduzir nova funcionalidade; Mediator centraliza comunicação e componentes só conhecem o mediador | Alto |

## Estrutura

```
Cliente → Facade → [Sub1, Sub2, Sub3, ...]
               ↗ (opcional)
    Facade Adicional
```

**Participantes:**
- **Fachada** — sabe onde direcionar pedidos e como operar as partes
- **Fachada Adicional** — evita que a fachada principal acumule funcionalidades não relacionadas
- **Subsistema** — não conhece a fachada; objetos se comunicam entre si diretamente
- **Cliente** — só fala com a fachada

## Pseudocódigo Central

```
class VideoConverter
    method convert(filename, format): File
        file = new VideoFile(filename)
        sourceCodec = (new CodecFactory).extract(file)
        destinationCodec = format == "mp4"
            ? new MPEG4CompressionCodec()
            : new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Cliente:
conversor = new VideoConverter()
mp4 = conversor.convert("funny-cats.ogg", "mp4")
```

## Aplicabilidade

1. Quando você precisa de interface simples para subsistema complexo que cresce com o tempo
2. Para estruturar subsistema em camadas — uma fachada por camada reduz acoplamento entre camadas

## Relações com Outros Padrões

- [[adapter-pattern]] — Facade define nova interface; Adapter torna interface existente utilizável. Adapter = 1 objeto; Facade = subsistema inteiro
- [[abstract-factory]] — alternativa ao Facade quando a preocupação é esconder *como* os objetos são criados
- [[flyweight-pattern]] — Flyweight: muitos objetos pequenos; Facade: um objeto representa subsistema inteiro
- [[mediator-pattern]] — ambos organizam colaboração, mas Mediator centraliza (componentes só conhecem o mediador); Facade simplifica (subsistema se comunica diretamente internamente)
- [[singleton-pattern]] — uma fachada pode ser convertida em Singleton (geralmente um único objeto fachada é suficiente)
- [[proxy-pattern]] — ambos armazenam buffer de entidade complexa, mas Proxy mantém a mesma interface do objeto real

## Entidades Mencionadas

- [[refactoring-guru]] — fonte primária

## Questões em Aberto

- Quando faz sentido ter uma Fachada Adicional vs dividir a fachada principal em múltiplas classes de serviço?
- Como testar uma fachada que inicializa o subsistema internamente (sem injeção de dependência)?
