---
type: source
title: "3 Tipos de Acoplamento que Atrapalham o Teste Unitário (André Casciotti)"
aliases: ["acoplamento e teste unitário", "new, herança e static impedem teste"]
date_created: 2026-10-05
date_updated: 2026-10-05
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/tres-tipos-de-acoplamento-que-impedem-teste-unitario-andre-casciotti.md
source_url: ""
author: "André Casciotti (canal Próximo Nível / Dev que Resolve)"
date_published: ""
date_ingested: 2026-10-05
source_count: 0
tags: [testes, teste-unitario, acoplamento, injecao-de-dependencia, heranca, metodo-estatico, dotnet, mock]
skill: tech-mentor-testing
status: draft
---

# 3 Tipos de Acoplamento que Atrapalham o Teste Unitário (André Casciotti)

## TL;DR

[[wiki/entities/andre-casciotti]] mostra, com debugger em C#/.NET, **três acoplamentos que impedem o teste unitário** ([[wiki/concepts/acoplamento-que-impede-teste-unitario]]): (1) **`new` de classe de infraestrutura** dentro do método ([[wiki/concepts/acoplamento-desejavel-vs-indesejavel]]), (2) **herança** de uma classe base que embute tecnologia ([[wiki/concepts/heranca-vs-composicao]]) e (3) **classe/método estático** ([[wiki/concepts/metodo-estatico-e-testabilidade]]). Nos três o teste "sai pela rede" (MongoDB, `HttpClient`) e quebra, violando a premissa de [[wiki/concepts/teste-unitario-sem-io]]. Cura comum: **interface + injeção de dependência** ([[wiki/concepts/dependency-injection]]) e mock no teste. Tese final: **o primeiro passo é saber identificar**; fazer teste unitário força, com o tempo, a escrever código menos acoplado.

## Key Claims

- **O `new` de uma classe concreta acopla o método a ela**; no teste, `ClienteMongoRepository` não tem a collection preenchida nem connection string, então o teste quebra antes de chegar na regra (erro tipo "Value cannot be null (collection)"). Evidência: demo no debugger. → [[wiki/concepts/acoplamento-que-impede-teste-unitario]]
- **Teste unitário não pode fazer I/O de rede nem de disco** — deve rodar em qualquer máquina e no servidor de build, que muitas vezes não alcança a rede interna. Evidência: argumento do autor (build server, colega sem MongoDB local). → [[wiki/concepts/teste-unitario-sem-io]]
- **Nem todo `new` é problema:** tipos do runtime (`List`) e classes de **domínio** são dependências desejáveis; **serviços/utilitários/infraestrutura** devem ficar atrás de interface. → [[wiki/concepts/acoplamento-desejavel-vs-indesejavel]]
- **Mockar a `IMongoCollection` é o reflexo errado:** o teste não depende dela, a dependência nem está visível; a correção é injetar a abstração do repositório. → [[wiki/concepts/acoplamento-que-impede-teste-unitario]]
- **Herança de uma `BaseService` com `ChamarApi` impede troca/mock** — o teste chama `HttpClient` real e falha com "host não é conhecido". Herança está superestimada (herança do ASP/VB6 → .NET, uso indiscriminado). Solução: classe de infraestrutura em outra camada + interface injetada (**composição**). → [[wiki/concepts/heranca-vs-composicao]]
- **Mover o código para `ApiHelper` estático não resolve:** o consumidor depende diretamente da classe/método, sem como substituir. Estático "vale para a aplicação toda" e vive com ela. Solução: classe instanciável injetada no construtor. → [[wiki/concepts/metodo-estatico-e-testabilidade]]
- **Camada *cross* e classes estáticas não são proibidas** — o que não se pode é furar limites / misturar contexto de tecnologia com contexto de negócio. → [[wiki/concepts/metodo-estatico-e-testabilidade]]
- **Círculo vicioso:** sem teste unitário, abusa-se do que impede o teste; com teste, o acoplamento "vai sumindo naturalmente". → [[wiki/concepts/testes-como-aprendizado]], [[wiki/concepts/hard-to-test-code]]
- **Fundamentos primeiro:** entender o runtime da linguagem (statics, herança, instanciação) para não acoplar sem perceber. → [[wiki/concepts/alto-nivel-antes-do-fundamento]]

## Entities

[[wiki/entities/andre-casciotti]] (a transcrição o grafa "André Casac"; quadro/canal citado com nome incerto — ver cabeçalho do raw) · exemplo de banco: [[wiki/concepts/mongodb]]

## Concepts

[[wiki/concepts/acoplamento-que-impede-teste-unitario]] · [[wiki/concepts/teste-unitario-sem-io]] · [[wiki/concepts/acoplamento-desejavel-vs-indesejavel]] · [[wiki/concepts/heranca-vs-composicao]] · [[wiki/concepts/metodo-estatico-e-testabilidade]] · [[wiki/concepts/acoplamento]] · [[wiki/concepts/dependency-injection]] · [[wiki/concepts/hard-to-test-code]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/singleton-pattern]] · [[wiki/concepts/ports-adapters]] · [[wiki/concepts/separation-of-concerns]] · [[wiki/concepts/composition-root]]

## Divergências e confiança

- **Alta** para o mecanismo (dependência concreta + I/O real = teste que quebra fora da máquina do dev): demonstrado no debugger e coerente com o catálogo xUnitPatterns ([[wiki/sources/hard-to-test-code-xunitpatterns]], "Highly Coupled Code / Hard-Coded Dependency").
- **Média** para "estático = problema": o autor reconhece que classes estáticas e camadas *cross* têm usos válidos. **[inferência]** Métodos estáticos **puros** (sem I/O nem estado) não prejudicam o teste; o problema demonstrado é o estático que embute infraestrutura.
- **[skill: tech-mentor-testing]** O reflexo "mockar o `IMongoCollection`" corresponde ao alerta clássico de não mockar tipos de terceiros e preferir um adaptador próprio (ver [[wiki/concepts/ports-adapters]]); a fonte não cita a regra por nome.
- Afirmação de que o comportamento vale para JavaScript/Java/C# é do autor; a semântica de `static` varia por linguagem (**não verificada**).
- Sem contradição com a wiki; complementa [[wiki/sources/tres-estagios-de-acoplamento-observer-pattern-na-pratica]] (estágio 2: chamada estática/explícita) e [[wiki/sources/3-erros-que-minam-confianca-como-dev-andre-casciotti]] (mock sem saber DI = conhecimento na hora errada).

## Open Questions

- E o **quarto tipo (acoplamento por processo)** citado e não explicado.
- Como testar o próprio `ClienteMongoRepository`? (teste de integração com banco real — ver [[wiki/concepts/testes-integracao-banco-real]]; a fonte só trata unitário.)
- Como migrar herança/estáticos em legado sem testes? (ver Michael Feathers em [[wiki/concepts/hard-to-test-code]].)

## Raw quotes worth keeping

- "Acoplamento mata teste unitário, porque você começa a ter muita dependência e, para fazer o teste, precisa ir carregando essas dependências."
- "Quando a gente faz teste unitário esse problema vai naturalmente desaparecendo, porque como acoplamento impede o teste você se vê forçado a aprender a fazer código melhor."
- "Antes de tentar corrigir qualquer coisa é aprender a identificar."
