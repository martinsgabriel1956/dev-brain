---
title: "Self Initializing Fake"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/SelfInitializingFake.html"
date_published: 2009-08-04
date_ingested: 2026-08-21
note: "Tradução/paráfrase em PT-BR do artigo original (bliki entry, texto curto), a partir de extração de conteúdo via ferramenta de fetch (não HTML bruto). Para o texto exato em inglês, consultar a source_url."
---

# Self Initializing Fake (Fake Autoinicializável)

Ao testar sistemas que chamam serviços remotos, desenvolvedores enfrentam um desafio: esses serviços costumam ser lentos e não confiáveis. Usar um test double resolve esse problema, mas exige popular o double com os dados esperados.

Um **self-initializing fake** resolve isso de forma elegante. Na primeira invocação, o fake repassa a chamada para o serviço remoto real e armazena em cache os dados retornados. Chamadas subsequentes recuperam a cópia em cache em vez de chamar o serviço de novo. Embora seja parecido com caching comum, essa abordagem evita as complexidades de invalidação de cache — uma vantagem significativa.

Fowler esclarece a terminologia: isso se qualifica como um **fake**, e não um **stub**, porque fakes operam de forma autônoma, sem exigir configuração de fixtures.

## Lidando com mudanças no serviço

A abordagem se mostra particularmente valiosa quando os dados remotos mudam. Em um cenário envolvendo um banco de dados controlado por outro sistema, os dados mudavam com frequência. Porém, como testes automatizados normalmente não precisam de dados atuais, guardar valores mais antigos funcionou bem para fins de teste.

Josh Price encontrou uma situação relacionada, em que dados remotos supostamente estáticos ocasionalmente mudavam, sinalizando que atualizações no sistema eram necessárias. O time dele implementou uma suíte de testes especializada, que exigia que os self-initializing fakes verificassem periodicamente se os valores em cache ainda correspondiam às respostas atuais do serviço remoto.

O pipeline de build deles empregava uma estratégia eficiente: os estágios iniciais rodavam contra os fakes (mais rápido), enquanto estágios posteriores testavam contra o serviço real (mais lento). Um desafio prático envolvia parâmetros irrelevantes que mudavam entre chamadas, mas não afetavam o resultado — esses eram removidos das buscas por URL.

## Créditos

Josh Price, Darren Cotterill e Gerard Meszaros contribuíram com ideias para este artigo.
