---
title: "Application Boundary"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/ApplicationBoundary.html"
date_published: 2003-09-11
date_ingested: 2026-07-20
note: "Tradução para PT-BR do artigo original (bliki entry, texto curto). Para o texto exato em inglês, consultar a source_url."
---

# Fronteira de Aplicação (Application Boundary)

Um dos problemas não resolvidos do desenvolvimento de software é decidir quais são os limites de um determinado software. (Um navegador é parte do sistema operacional ou não?) Muitos defensores da Arquitetura Orientada a Serviços (SOA) acreditam que as aplicações estão desaparecendo — e que, no futuro, o desenvolvimento de software corporativo será sobre montar serviços entre si.

Eu não acho que as aplicações estão desaparecendo, pelas mesmas razões que tornam tão difícil traçar as fronteiras de uma aplicação. Essencialmente, **aplicações são construções sociais**:

- Um corpo de código que os desenvolvedores enxergam como uma unidade única
- Um conjunto de funcionalidades que os clientes de negócio enxergam como uma unidade única
- Uma iniciativa que quem controla o dinheiro enxerga como um orçamento único

Todas essas são questões sociais. Podemos traçar fronteiras de aplicação de centenas de maneiras arbitrariamente diferentes. Mas é da nossa natureza agrupar coisas e organizar grupos de pessoas em torno desses agrupamentos. Há pouca ciência em como isso funciona, e de muitas formas essas fronteiras são traçadas primariamente por relações humanas e política, mais do que por considerações técnicas e funcionais. Para pensar sobre isso com mais clareza, acho que precisamos reconhecer esse fato incômodo.

(Se você tem interesse em pensar mais a fundo sobre aplicações e como elas se inter-relacionam, vale a pena olhar a seção de design estratégico de Domain-Driven Design.)

## Metadados do artigo

- Publicado em 11 de setembro de 2003. Bliki entry curto e antigo de Fowler.
- Tema central: fronteiras de aplicação (application boundaries) não são um problema técnico resolvível objetivamente — são construções sociais, moldadas por como devs, negócio e financiadores percebem "uma unidade única" de código/funcionalidade/orçamento.
- Contexto histórico: publicado em 2003, no auge do discurso de que SOA tornaria as "aplicações" obsoletas em favor de composição de serviços. Fowler discorda dessa previsão.
- Referência cruzada citada pelo próprio Fowler: a seção de design estratégico ("strategic design") de Domain-Driven Design, como leitura complementar para quem quer aprofundar em como aplicações se inter-relacionam.
