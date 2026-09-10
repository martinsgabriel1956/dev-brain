---
type: source
title: "Clean Architecture no Frontend — Diagrama de Camadas Aplicado a uma Tela de Login (Vue.js)"
aliases: ["clean architecture vue login", "diagrama camadas login vue"]
date_created: 2026-09-08
date_updated: 2026-09-08
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/clean-architecture-frontend-vue-diagrama-camadas-login.md
source_url: ""
author: "não identificado no texto — provável Rodrigo Branas (ver Open Questions)"
date_published: ""
date_ingested: 2026-09-08
source_count: 0
tags: [clean-architecture, frontend, vue, solid, design-patterns, dependency-injection, factory-pattern, composite-pattern, composition-root, validation]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Aula introdutória (antes de escrever código) de um curso que aplica Clean Architecture a um projeto Vue.js, usando como primeiro exemplo uma tela de login. Parte do diagnóstico de que frameworks como Vue tornam fácil demais colocar toda responsabilidade (validação, cache, navegação, regra de negócio, chamada de API, tratamento de erro, renderização e controle de estado) dentro de um único componente — o que trava testabilidade e reaproveitamento de código. A aula então desenha, camada por camada (Domínio → Data → Infraestrutura → Presentation → Validation → Main), como extrair cada responsabilidade do componente de login até sobrarem apenas quatro: renderizar UI, controlar estado, navegação e (por ora, deliberadamente) acesso ao local storage. Fecha citando explicitamente SRP, DIP, DI, OCP (via Decorator) e ISP (via cliente HTTP) como os princípios SOLID por trás de cada corte de camada.

## Key Claims

**Claim:** Frameworks reativos (o vídeo usa Vue como exemplo) incentivam colocar toda a lógica de uma tela — validação, cache, navegação, regra de negócio, chamada de API, tratamento de erro, renderização e controle de estado — dentro do próprio componente, porque isso é fácil e rápido de escrever; o preço é perda de manutenibilidade, reaproveitamento e testabilidade unitária (só resta teste de integração, mais lento e acoplado à API real).
**Evidence:** Abertura da aula, usando um diagrama de dependências (draw.io) com o componente de login inicial concentrando ~10 responsabilidades.
**Confidence:** alta — é a tese central e recorrente da aula, sem citação de fonte externa, mas coerente com o restante da wiki sobre Clean Architecture (ver [[wiki/concepts/clean-architecture]]).

**Claim:** O valor de investir em Clean Architecture no frontend não é abstrato — é a aposta de que frameworks são passageiros (o exemplo dado é o jQuery, usado por "todo mundo" e hoje presente só em código legado) e que uma arquitetura bem desenhada permite reaproveitar 70-80% do código ao trocar de framework, restando para reescrever principalmente a camada de controle de estado/reatividade (específica de cada framework) e os testes de UI.
**Evidence:** Comparação explícita Vue-hoje vs. jQuery-décadas-atrás como argumento para a necessidade de isolar regra de negócio de frameworks.
**Confidence:** média-alta — é uma tese defensável e coerente com a genealogia de Clean Architecture documentada em [[wiki/sources/arquitetura-limpa-na-pratica]], mas apresentada aqui sem dado quantitativo, como estimativa do instrutor.

**Claim:** A separação de camadas segue um fluxo de dependência único: Infraestrutura → Data → Domínio (domínio não depende de ninguém); e, paralelamente, Validation → Presentation. A camada de Presentation (que no diagrama concentra tanto UI quanto conversão/tratamento de dados, por causa da reatividade nativa do Vue) depende apenas de interfaces do Domínio (`Authentication`) e da própria Validation (`Validation`) — nunca de implementações concretas.
**Evidence:** Diagrama de camadas apresentado passo a passo: `Authentication` (interface, Domínio) → `RemoteAuthentication` (implementação concreta, Data) → `HttpPostClient` (interface própria da Data, para desacoplar de bibliotecas HTTP) → `AxiosHttpClient` (implementação concreta, Infraestrutura, dependendo da lib Axios).
**Confidence:** alta — é o núcleo estrutural do diagrama, com nomenclatura concreta (`RemoteAuthentication`, `AxiosHttpClient`) característica de projetos de referência de Clean Architecture em TypeScript/JavaScript (ex.: `clean-ts-api`/`clean-react` de Rodrigo Branas — ver Open Questions sobre autoria).

**Claim:** Diferente do fluxo clássico Controller → Use Case → Presenter → View descrito em [[wiki/concepts/clean-architecture]] (baseado no livro de Robert Martin), no contexto de um framework reativo como Vue não faz sentido separar totalmente "Presentation" de "View/UI" — fazer isso abriria mão dos hooks/reatividade nativa do framework, que é justamente o seu ponto forte. A aula reconhece essa divergência explicitamente como uma decisão pragmática, não como violação da Clean Architecture.
**Evidence:** Seção sobre a camada Presentation, contrastando com "projetos mais bem desacoplados" onde Presentation e UI ficam de fato separados.
**Confidence:** alta — é uma posição declarada e justificada pelo instrutor, marcada como decisão pragmática específica de frameworks reativos, não como regra geral de Clean Architecture.

**Claim:** A camada de validação de formulário deve ser desacoplada do framework via uma interface própria (`Validation`, definida na camada de Presentation) e implementações concretas (`RequiredFieldValidation`, `EmailFieldValidation`) compostas através do design pattern **Composite** (`ValidationComposite`), em vez de usar diretamente uma lib de formulários do framework (ex.: VeeValidate/Vue Hook Forms) com schema de validação embutido na tela.
**Evidence:** Seção "Validation" do diagrama — motivo dado: trocar de framework (Vue → Angular/React) exigiria reescrever toda a validação se ela estivesse amarrada à lib de formulários do framework.
**Confidence:** alta — exemplo concreto e nomeado, coerente com a lógica de isolamento do resto do diagrama.

**Claim:** A camada Main atua como *composition root*: o único ponto do sistema que se acopla a todas as outras camadas (via um design pattern Factory, ex.: `LoginFactory`) para permitir que as demais fiquem desacopladas entre si — chamado no vídeo de "composição grude" (tradução informal de *composition root*). Como o domínio não depende de ninguém e as demais camadas têm dependência única entre si, só o Main tem uma dependência de "muitos para muitos", o que o torna difícil de desenhar no diagrama sem poluí-lo.
**Evidence:** Seção final do diagrama — decisão explícita de apontar o Main só para as camadas (Data, Validation, Infraestrutura), não para componentes individuais, para não poluir o diagrama.
**Confidence:** alta — mecanismo já documentado na wiki de forma inline (ver [[wiki/concepts/clean-architecture]] e [[wiki/concepts/dependency-injection]], que já citavam "composition root" sem página própria); esta fonte é a primeira a dar o exemplo concreto do padrão Factory cumprindo esse papel no frontend.

**Claim:** Os cortes de camada mapeiam diretamente para princípios SOLID específicos: SRP (10 responsabilidades → 4 no componente final), DIP (interface de fronteira/"boundary" na própria camada de Presentation, invertendo a direção normal da dependência — mesmo mecanismo usado entre Data e Infraestrutura via `HttpClient`), DI (Main/Factory injeta as implementações concretas em vez do componente criá-las), OCP (citado só brevemente, com Decorator como pattern relacionado, prometido para aula futura) e ISP (prometido para quando o cliente Axios for implementado — interface `HttpClient` gorda com `get/post/put/delete` força implementações/mocks desnecessários quando só `post` é usado).
**Evidence:** Seção de fechamento do diagrama, com cada princípio associado a uma decisão de design já mostrada.
**Confidence:** alta para SRP/DIP/DI (exemplificados no próprio diagrama); média para OCP/ISP (citados como promessa de aprofundamento futuro, sem exemplo de código nesta aula).

## Entidades e Conceitos Mencionados

- **Conceitos centrais:** [[wiki/concepts/clean-architecture]], [[wiki/concepts/single-responsibility-principle|SRP]], [[wiki/concepts/dependency-inversion-principle|DIP]], [[wiki/concepts/dependency-injection|DI]], [[wiki/concepts/open-closed-principle|OCP]], [[wiki/concepts/interface-segregation-principle|ISP]], [[wiki/concepts/factory-pattern|Factory]], [[wiki/concepts/decorator-pattern|Decorator]], Composite (Composição — ver novo stub [[wiki/concepts/composite-pattern]]), Composition Root (ver novo stub [[wiki/concepts/composition-root]]).
- **Tecnologias citadas:** Vue.js, Vue Router, Axios, Node.js (API externa consumida pelo front, desenvolvida em outro curso do mesmo autor), draw.io (ferramenta de diagrama).
- **Pessoas/entidades:** nenhuma citada nominalmente no áudio — ver Open Questions sobre autoria provável.

## Open Questions

- **Autoria não identificada no texto:** o instrutor não se nomeia na transcrição. A nomenclatura das classes do exemplo (`RemoteAuthentication`, `HttpPostClient`, `AxiosHttpClient`, `ValidationComposite`, `EmailValidation`, `RequiredFieldValidation`, uso do termo "composição grude" para composition root, e a menção de uma API em Node desenvolvida "em outro curso") é idêntica à nomenclatura dos repositórios públicos `clean-ts-api` e `clean-react` de [[wiki/entities/rodrigo-branas]], que já tem página na wiki (associada até agora só à Formação IA para Devs). É uma correspondência de padrão muito forte, mas fica registrada como inferência, não confirmação — nenhuma fala da transcrição cita o nome do instrutor.
- Os princípios OCP e ISP são citados apenas como promessa de aprofundamento futuro (aulas seguintes do mesmo curso), sem exemplo de código nesta aula — não há como avaliar a claim de forma independente ainda; ficam registrados como "confidence média" até uma eventual aula seguinte ser ingerida.
- O curso completo (próximas aulas, com código) não foi ingerido — esta fonte cobre só a aula de introdução/diagrama.
