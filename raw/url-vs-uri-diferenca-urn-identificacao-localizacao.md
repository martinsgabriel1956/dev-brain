---
title: "URL vs URI: qual é a diferença (e onde entra a URN)"
source_type: transcrição de vídeo (EN, fala corrida) — traduzida para PT-BR
author: ""
date_ingested: 2026-10-09
---

# URL vs URI: qual é a diferença (e onde entra a URN)

> Transcrição limpa (pontuação e parágrafos) e **traduzida do inglês para o português**. Autor/canal não identificado. O original descreve exemplos de endereço "falados" (sem mostrar a string literal); nada foi inventado além disso.

## Abertura: a confusão

Se você trabalha com APIs, aplicações web ou até com redes básicas, provavelmente já ouviu dois termos usados quase como sinônimos: **URL** e **URI**. É aí que começa a confusão. Um desenvolvedor chama algo de URL, outro chama de URI, e os dois parecem estar falando exatamente da mesma coisa. Qual é a diferença real?

O jeito mais fácil de entender: **URI é o conceito mais amplo, e URL é um tipo particular de URI.**

## URI e URL

**URI** significa *Uniform Resource Identifier* (identificador uniforme de recurso). Sua função é simplesmente **identificar um recurso**. Esse recurso pode ser uma página web, uma imagem, um endpoint de API, um arquivo ou outra coisa.

**URL**, ou *Uniform Resource Locator* (localizador uniforme de recurso), vai um passo além: diz **onde o recurso está localizado e como acessá-lo**. Num endereço web comum, ele informa qual protocolo usar, qual host contatar e qual recurso você quer alcançar. Isso é uma URL.

Como uma URL identifica um recurso, ela também é uma URI. Então **toda URL é uma URI, mas nem toda URI precisa ser uma URL.**

## URN: identificar pelo nome

Aqui a terminologia fica mais interessante. Pense no **ISBN** de um livro. O ISBN identifica um livro específico, mas não diz ao seu computador onde o livro está nem como obtê-lo pela rede. Ele identifica o recurso **por nome**, em vez de dar uma localização. Isso se aproxima do que chamamos de **URN** (*Uniform Resource Name*, nome uniforme de recurso).

Então:

- **URI** é a categoria geral.
- **URL** e **URN** são formas de identificar recursos dentro dessa categoria.
- A **URL** diz *onde* e *como* acessar algo.
- A **URN** dá ao recurso um **nome persistente**.
- Ambas são URIs, porque ambas identificam um recurso.

## No desenvolvimento de software

Suponha um endpoint de API para um cliente (customer). Você pode ter um endereço que aponta para o recurso "cliente" e, depois, acrescentar um parâmetro de consulta (query parameter) para pedir um cliente específico. Essa string inteira é uma URI e, como diz como localizar o recurso via HTTP, **também é uma URL**.

Por isso se ouve "API URL", "endpoint URL" ou simplesmente "URI", mesmo quando todos se referem à mesma coisa. No dia a dia de desenvolvimento, os termos parecem intercambiáveis.

## Referência relativa

Há outro detalhe que confunde: uma URI **não precisa conter uma localização de rede completa**. Dentro de um site, por exemplo, você pode se referir a outro recurso com uma **referência relativa**, em vez de escrever o endereço completo.

A ideia importante: **URI é sobre identificação; URL é especificamente sobre localizar o recurso.**

## Analogia: identidade e endereço

Outra forma de lembrar: pense na identidade e no endereço de uma pessoa. Um **nome** identifica a pessoa; um **endereço** diz onde encontrá-la. Estão relacionados, mas não são a mesma coisa. Aqui vale a mesma ideia: a **URI identifica** o recurso; a **URL identifica o recurso e fornece um meio de localizá-lo**.

## Uso cotidiano

No desenvolvimento web moderno, a palavra **URL** é usada para quase qualquer endereço web, e isso é perfeitamente normal na conversa do dia a dia: a barra de endereço do navegador é associada a URLs, desenvolvedores falam em "parâmetros de URL" e frameworks usam termos como "roteamento de URL". Tecnicamente, porém, URL é um termo **mais específico** dentro do conceito mais amplo de URI.

Quando alguém pergunta "qual é a URL desta página?", está perguntando **onde o recurso pode ser encontrado**. Quando alguém fala em URI, usa o termo mais amplo para **identificar** esse recurso.

## Conclusão

O importante é não ficar preso à terminologia; basta lembrar a relação:

- Uma **URI identifica** um recurso.
- Uma **URL identifica** um recurso **e diz onde e como acessá-lo**.
- Logo, uma **URL também é uma URI**.

Numa aplicação web ou API comum, os endereços com que você lida normalmente são URLs, e muitas vezes são descritos de forma mais geral como URIs. Entendida essa relação, a diferença fica fácil de lembrar.
