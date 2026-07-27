---
title: "Contract Test"
author: "Martin Fowler"
source_url: "https://martinfowler.com/bliki/ContractTest.html"
date_published: 2011-01-12
date_ingested: 2026-07-27
note: "Resumo/paráfrase em PT-BR preparado para a wiki, não é tradução literal do artigo original. Para o texto exato, consultar a source_url."
---

# Contract Test — resumo comentado

Bliki entry curto de Martin Fowler. O artigo foi originalmente publicado sob o nome "Integration Contract Test" e depois renomeado para "Contract Test", já que esse nome mais curto acabou se tornando o termo mais usado na indústria.

## O problema que motiva o artigo

Um dos usos mais comuns de um [[test-doubles|Test Double]] é para substituir a comunicação com um serviço externo — serviços externos tendem a estar sujeitos a redes lentas e não confiáveis, e podem ser eles mesmos não confiáveis. Faz sentido, então, isolar o código que fala com esse serviço atrás de um dublê de teste.

O problema é que testar contra um dublê sempre deixa uma dúvida no ar: o dublê realmente se comporta como o serviço real? Se o dublê "mentir", os testes passam mas o sistema pode quebrar em produção.

## A solução: dois conjuntos de testes rodando em paralelo

Fowler propõe manter os testes normais contra os dublês (rápidos, rodam a cada build) e, separadamente, manter um segundo conjunto de testes — os **contract tests** — que verificam se todas as chamadas feitas contra o dublê retornariam os mesmos resultados que uma chamada equivalente contra o serviço externo real.

Pontos práticos que ele destaca:

- **Frequência de execução**: contract tests não precisam rodar em todo pipeline de deploy, porque o serviço externo muda no seu próprio ritmo, normalmente bem mais lento que o do time consumidor. Rodar uma vez por dia costuma ser suficiente.
- **Falha não deve quebrar o build automaticamente**: uma falha no contract test deve disparar uma tarefa de reconciliação — atualizar o código/testes do lado do consumidor, ou abrir uma conversa com o time responsável pelo serviço sobre a mudança de contrato.
- **Serviços críticos em produção**: quando o serviço externo é crítico, uma mudança de contrato não detectada pode quebrar a aplicação em produção e forçar uma correção de emergência + conversa urgente com o time fornecedor. Nesses casos vale investir em comunicação próxima com quem mantém o serviço.
- **Consumer-Driven Contracts reduz o risco**: compartilhar os contract tests com o time fornecedor, para que ele os rode no próprio pipeline de build, permite detectar incompatibilidades antes mesmo do deploy — antecipando o problema em vez de descobri-lo depois que o contrato já mudou.
- **Ambiente de teste, não produção**: contract tests normalmente rodam contra uma instância de teste do serviço externo, não contra produção. Testar diretamente contra produção exige coordenação explícita com o fornecedor.
- **O que o contract test valida**: o formato da chamada e da resposta (o "contrato"), não valores específicos de dado. É comum que os stubs usados nos testes normais sejam um snapshot de uma resposta real capturada em determinada data — o contract test garante que o *formato* daquele snapshot continua válido, mesmo que os dados em si estejam desatualizados.
- **Como construir os dublês**: o artigo recomenda o padrão [[wiki/concepts/test-doubles|SelfInitializingFake]] como uma forma eficaz de implementar esse tipo de dublê que sabe se autovalidar contra o serviço real.

## Metadados do artigo

- Publicado em 12 de janeiro de 2011; nome original "Integration Contract Test", renomeado depois para "Contract Test" (nome mais curto e mais adotado pela indústria).
- Termos correlatos citados por Fowler no bliki: `TestDouble`, `SelfInitializingFake`, `ConsumerDrivenContracts`.
