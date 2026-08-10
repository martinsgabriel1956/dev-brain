---
type: source
title: "Observer: Padrão de Projeto na Prática, com TypeScript e Deno (Código Fonte TV)"
aliases: ["observer codigo fonte tv", "observer deno typescript video", "youtube notification observer example"]
date_created: 2026-08-06
date_updated: 2026-08-06
source_count: 0
tags: [design-patterns, behavioral, observer, gof, pub-sub, typescript, deno, video]
skill: tech-mentor-backend
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/design-pattern-observer-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: 2026-08-06
---

# Observer: Padrão de Projeto na Prática, com TypeScript e Deno (Código Fonte TV)

## TL;DR

Vídeo didático em português sobre o padrão [[wiki/concepts/observer-pattern]], parte de uma série do canal sobre design patterns (que já cobriu [[wiki/concepts/strategy-pattern]], [[wiki/concepts/facade-pattern]] e [[wiki/concepts/singleton-pattern]]). Implementa o padrão duas vezes em TypeScript/Deno: primeiro um exemplo genérico de aquecimento (`Subject`/`Observer` com `subscribe`/`unsubscribe`/`unsubscribeAll`/`notify`/`notifyAll`), depois um exemplo mais próximo do mundo real — notificação de vídeo novo do YouTube, com **dois tipos de observer diferentes** (`Subscriber` e `Feed`) reagindo ao mesmo evento de formas distintas.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Observer é conhecido por vários nomes equivalentes | "pode ser conhecido por vários nomes: Event Subscriber, Listener, Publish-Subscribe, ou apenas Pub/Sub" | Médio — o vídeo trata esses termos como sinônimos; a wiki já registra uma distinção mais fina entre Observer e Pub/Sub (ver Contradições abaixo) |
| Definição GoF citada: dependência um-para-muitos, notificação automática | "o Observer define uma dependência um-para-muitos entre objetos, para que, quando um objeto mudar de estado, todos os seus dependentes sejam notificados e atualizados automaticamente" | Alto |
| Um mesmo evento pode ter mais de um tipo de observer reagindo de formas diferentes | Exemplo do YouTube: `Subscriber` (notificação pessoal ao inscrito) e `Feed` (atualização de URL do feed do canal) implementam a mesma interface `IObserver`, mas cada `update` faz algo estruturalmente diferente | Alto |
| TypeScript permite inicializar atributos direto no construtor sem atribuição manual campo a campo | Comentário do autor ao implementar a classe `Video`: "recurso presente também em outras linguagens, como Dart" | Alto |
| `unsubscribeAll` pode ser implementado zerando o array em vez de usar `filter` | Escolha explícita do autor sobre a implementação mais direta para remover todos os observers de uma vez | Médio — é uma escolha de implementação, não uma regra do padrão |
| Observer é usado amplamente em sistemas de Pub/Sub mais complexos, citando Kafka como exemplo | Frase de encerramento do vídeo | Baixo — citação solta, sem detalhamento de como o Kafka se relaciona estruturalmente com o Observer descrito no vídeo |

## Estrutura do Exemplo

**Exemplo 1 (genérico):**
```
IObserver { update(): void }
ISubject { subscribe, unsubscribe, unsubscribeAll, notify, notifyAll }
Observer implements IObserver — construtor recebe id, update() faz console.log
Subject implements ISubject — array de IObserver[]
```

**Exemplo 2 (YouTube):**
```
IObserver { update(video: Video): void }
Video — classe de dados pura (id, title, thumbnail, link)
Subscriber implements IObserver — update() notifica um inscrito específico
Feed implements IObserver — update() atualiza a URL do feed do canal
VideoNotification implements ISubject — mesmo contrato do Subject, mas passa Video para os observers
```

## Relação com [[wiki/concepts/observer-pattern]]

Esta fonte reforça a implementação canônica já documentada na página de conceito (interface `Subscriber`/`update`, array de observers no subject) e adiciona um ângulo que a página ainda não cobria explicitamente: **múltiplos tipos de observer para o mesmo evento**, cada um com sua própria lógica de reação (`Subscriber` vs. `Feed`), reforçando que "não existe só um tipo de observer" ao lidar com esse padrão — mesmo evento, reações estruturalmente diferentes por tipo de assinante.

## Entidades Mencionadas

- [[wiki/entities/codigo-fonte-tv]] — canal/autor do vídeo
- [[wiki/entities/gang-of-four]] — citada como fonte da definição formal do padrão

## Contradições / Questões em Aberto

- O vídeo trata Observer, Event Subscriber, Listener, Publish-Subscribe e Pub/Sub como sinônimos ("pode ser conhecido por vários nomes"). Isso está em tensão direta com [[wiki/sources/design-pattern-observer]] (Refactoring Guru), já na wiki, que registra uma distinção estrutural explícita: Observer tem comunicação **direta** publicadora→assinante, enquanto Pub/Sub usa um **broker intermediário**. O vídeo não aborda essa distinção — não chega a contradizer tecnicamente (o exemplo dele é, de fato, Observer direto, sem broker), mas simplifica a nomenclatura de um jeito que colide com o que já está registrado. Mantido como open question em vez de correção silenciosa.
- A citação de Kafka como "sistema que utiliza Pub/Sub" no encerramento não é aprofundada — não fica claro se o autor está equiparando o modelo de tópicos do Kafka ao Observer direto do vídeo ou reconhecendo a diferença de broker. Vale revisitar se uma fonte futura tratar Kafka e Observer explicitamente.
- O vídeo não discute ordem de notificação, tratamento de erro dentro de um `update()` (um observer que lança exceção interrompe os demais?), nem memory leaks por observers não removidos — mesmas lacunas já registradas como open questions em [[wiki/sources/design-pattern-observer]].

## Quotes Preservadas

> "O Observer define uma dependência um-para-muitos entre objetos, para que, quando um objeto mudar de estado, todos os seus dependentes sejam notificados e atualizados automaticamente." (citando a Gang of Four)

> "Não existe só um tipo de observer quando a gente tá lidando com esse design pattern."

> "No mundo real, esse método `update` pode ser alguma coisa muito mais complexa — não é só um `console.log`."
