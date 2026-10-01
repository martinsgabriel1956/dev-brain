---
type: source
title: "Vertical Slice — Organizando o Código por Funcionalidade (Bernardo Lobato)"
aliases: ["vertical slice bernardo lobato", "vertical slice por funcionalidade", "architecture sinkhole vertical slice"]
date_created: 2026-10-01
date_updated: 2026-10-01
source_count: 0
tags: [vertical-slice, arquitetura-em-camadas, architecture-sinkhole, coesao, acoplamento, dominio, extracao-de-servico, microsservicos, backend]
skill: tech-mentor-backend
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/vertical-slice-organizar-codigo-por-funcionalidade-bernardo-lobato.md"
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: "2026-10-01"
---

## TL;DR

Vídeo de [[wiki/entities/bernardo-lobato]] sobre o [[wiki/concepts/vertical-slice-architecture]] como resposta ao [[wiki/concepts/architecture-sinkhole]] do padrão em camadas ([[wiki/concepts/arquitetura-em-3-camadas]]): em vez de separar por responsabilidade técnica (controller/service/repository), separa-se **por intenção/funcionalidade** — cada *slice* tem controller, validação, domínio, regra de negócio e acesso a dados. A tese mais forte é a do **domínio**: não é preciso um único `Usuário` centralizado; cada slice pode ter a sua própria representação do usuário ([[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]]), eliminando o efeito colateral entre autenticação e gestão de perfil e os conflitos entre times. Ganhos: [[wiki/concepts/coesao]] alta, baixo [[wiki/concepts/acoplamento]], testes mais simples, aderência à jornada do usuário. Riscos: slices que se chamam como clientes ([[wiki/concepts/acoplamento-entre-slices]]) e novos devs que "unificam" os modelos. Uso: features em crescimento orgânico, módulos delicados e **extração para serviço** ([[wiki/concepts/extracao-de-slice-para-servico]]) — caminho intermediário rumo a [[wiki/concepts/microsservicos]]. Não é bala de prata e pode ser mesclado com outros estilos.

---

## Reivindicações Principais

**Claim:** O padrão em camadas separa por responsabilidade técnica, obrigando a navegar por vários arquivos/pastas para entender ou alterar uma funcionalidade, e produz o Architecture Sinkhole (request atravessa camadas sem lógica própria só para respeitar camadas fechadas).
**Evidência:** Argumento do autor, remetendo a vídeo anterior do canal sobre camadas; sem medição.
**Confiança:** Média-alta. O custo de navegação é medido em [[wiki/concepts/navigation-paradox]] (7–13 arquivos vs 1–3) [[wiki/sources/clean-architecture-ia-custo-real]]. O nome e a origem do antipadrão não são verificados aqui — ver [[wiki/concepts/architecture-sinkhole]].

**Claim:** Vertical Slice separa por **negócio/funcionalidade**, não por tecnologia; cada slice contém tudo (controller, validação, domínio, regras, dados, mensageria) e funciona completa e isoladamente.
**Evidência:** Exemplo de duas slices — autenticação e gestão de perfil — sobre as mesmas entidades.
**Confiança:** Alta. [external] Jimmy Bogard: "Minimize coupling between slices, and maximize coupling in a slice"; cada slice decide como cumprir o request (https://www.jimmybogard.com/vertical-slice-architecture/).

**Claim:** Um modelo de domínio centralizado infla (ex.: `Usuário` servindo autenticação, perfil, seguidores, entregas), gera autoacoplamento entre módulos e efeito colateral de qualquer mudança; com vários times, os mesmos arquivos são editados ao mesmo tempo.
**Evidência:** Exemplo didático assumidamente simplificado ("não levar ao pé da letra"); relato de experiência do autor sobre conflitos entre equipes.
**Confiança:** Média — plausível e coerente com [[wiki/concepts/bounded-context]] (duas classes `Produto`) e com [[wiki/concepts/modelo-de-dominio-anemico]]; sem dado quantitativo. Ver [[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]].

**Claim:** Cada slice pode ter **sua própria representação** de usuário e seguir **seu próprio padrão de arquitetura**.
**Evidência:** Slice de auth só com `username`/senha/token; slice de perfil com nome, documento, endereços.
**Confiança:** Alta (coincide com Bogard [external]). Custo implícito: duplicação de campos entre slices — não discutido no vídeo (ver "Questões em Aberto").

**Claim:** Benefícios: alta coesão, baixo acoplamento, mais fácil manter/testar/entender, jornada do usuário mais aderente ao código, testes de integração facilitados porque o mesmo time cuida de funcionalidades próximas.
**Evidência:** Argumento do autor.
**Confiança:** Média (benefícios organizacionais dependem de o time ser dono da feature de ponta a ponta).

**Claim:** Slices podem chamar-se mutuamente **sem compartilhar código**, como cliente/request; sem atenção isso reintroduz autoacoplamento.
**Evidência:** Aviso explícito do autor ("pegadinha").
**Confiança:** Alta como alerta; o vídeo não prescreve o mecanismo (HTTP interno, evento, mediator). Ver [[wiki/concepts/acoplamento-entre-slices]].

**Claim:** Aplicável a features de crescimento orgânico, módulos delicados (cálculo complexo, algoritmo proprietário) e à **extração de funcionalidade para serviço** (ex.: auth → serviço externo), validando o isolamento por uso e testes antes de extrair.
**Evidência:** Exemplo de autenticação/autorização.
**Confiança:** Alta — mesma lógica de extração tardia de [[wiki/concepts/monolito-modular]] e [[wiki/concepts/strangler-fig-pattern]]. Ver [[wiki/concepts/extracao-de-slice-para-servico]].

**Claim:** Não é bala de prata; exige disciplina e acompanhamento (devs novos tendem a re-unificar modelos); pode ser mesclado com outros estilos no mesmo projeto.
**Evidência:** Relato do autor, "mais de uma vez".
**Confiança:** Alta; [external] Bogard também condiciona a abordagem à maturidade do time em refatoração.

---

## Entidades

- [[wiki/entities/bernardo-lobato]] — autor do vídeo.

## Conceitos

- [[wiki/concepts/vertical-slice-architecture]] — conceito central.
- [[wiki/concepts/architecture-sinkhole]] — antipadrão das camadas fechadas (novo).
- [[wiki/concepts/dominio-centralizado-vs-modelo-por-slice]] — tese do domínio (novo).
- [[wiki/concepts/acoplamento-entre-slices]] — risco principal (novo).
- [[wiki/concepts/extracao-de-slice-para-servico]] — slice como passo antes do serviço (novo).
- [[wiki/concepts/arquitetura-em-3-camadas]], [[wiki/concepts/coesao]], [[wiki/concepts/acoplamento]], [[wiki/concepts/bounded-context]], [[wiki/concepts/microsservicos]], [[wiki/concepts/monolito-modular]], [[wiki/concepts/strangler-fig-pattern]], [[wiki/concepts/feature-sliced-architecture]], [[wiki/concepts/clean-architecture]].

## Questões em Aberto

- Como evitar duplicação de regras de negócio entre slices quando duas features compartilham invariantes reais (ex.: validação de senha)? O vídeo só diz "não unifique"; [[wiki/concepts/vertical-slice-architecture]] sugere extrair para `shared/` após o segundo caso. Tensão não resolvida.
- Mecanismo recomendado para uma slice chamar outra (síncrono vs evento) — não coberto; ver [[wiki/concepts/comunicacao-assincrona]].
- Como o "mesmo usuário" persiste: tabela única com projeções por slice, ou dados separados? Não abordado.
- Terminologia: o autor chama camadas de "verticais" e slices de "horizontais"; a convenção corrente é o inverso (anotado no raw).

## Citações Preservadas

> "Não precisamos de um único domínio representando a classe de usuário no nosso sistema."

> "Esse modelo não é uma bala de prata."
