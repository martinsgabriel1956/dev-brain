---
type: source
title: "Por Que Você Tem Que Aprender a Programar do Jeito Difícil"
aliases: ["programar do jeito difícil", "the hard way", "aprender low level do jeito difícil"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/aprender-a-programar-do-jeito-dificil.md
source_url: ""
author: criador de conteúdo brasileiro não identificado por nome (canal reage a ThePrimeagen reagindo a Theodor; menciona bot de Discord de Tibia e contribuição à API TibiaData)
date_published: desconhecida
date_ingested: 2026-07-28
tags: [carreira, aprendizado, low-level, concorrencia, open-source, entrevistas, confianca]
skill: tech-mentor-leadership
status: stable
---

# Por Que Você Tem Que Aprender a Programar do Jeito Difícil

## TL;DR

Vídeo reagindo a uma corrente de reações (ThePrimeagen reagindo a Theodor) sobre um comentário desencorajador recebido por um dev que construía um jogo do zero sem engine. O autor defende que estudar linguagens e conceitos low level — mesmo sem retorno financeiro imediato — traz dois benefícios centrais: **satisfação pessoal** (o mesmo mecanismo que motiva um maratonista) e **benefício de carreira no longo prazo** (confiança em entrevistas, diferenciação num mercado com muita demanda mas mão de obra desqualificada). Usa como caso pessoal um bot de Discord para o jogo Tibia, cuja otimização via concorrência/paralelismo em Go (de 20 minutos para 2-3 segundos) nunca deu retorno financeiro direto, mas se tornou conhecimento transferível para entrevistas técnicas.

---

## Claims principais

| Claim | Evidência | Confiança |
|---|---|---|
| Objetivo de curto prazo (MVP rápido) justifica ferramentas high-level; objetivo de longo prazo (maestria) justifica estudo low-level | Distinção central do vídeo, sem dado externo citado | Média (opinião, não estudo) |
| Mercado atual tem alta demanda mas mão de obra desqualificada, pressionado por corte de investimento e busca por eficiência | Citação de vídeos de Lucas Montano e Filipe Deschamps, que por sua vez citam um áudio de Fábio Akita | Média (fonte terciária — opinião repassada em cadeia) |
| Estudar coisas difíceis aumenta confiança e reduz nervosismo em entrevistas técnicas | Anedota de candidato reprovado em entrevista na Netflix por nervosismo, que resolveu o problema minutos depois sem pressão | Baixa (anedota de terceiros, sem fonte primária citada) |
| Aprender um pouco de uma linguagem low-level (ex. Rust) já melhora a escrita de código em linguagens de mais alto nível | Reação a um comentário de espectador que relatou essa experiência | Baixa (relato de um único comentário) |
| Contribuição open source não remunerada pode ser decisiva para conseguir o primeiro emprego | Caso pessoal do autor com a API TibiaData | Média (caso próprio, não generalizável) |
| Otimizar um problema real de concorrência (mesmo sem uso prático) transforma o conceito em conhecimento permanente, útil em processos seletivos | Caso pessoal do bot de Discord de Tibia, biblioteca `conc` da Sourcegraph | Média (caso próprio) |

---

## Conceitos abordados

- [[wiki/concepts/aprendizado-por-luta]]
- [[wiki/concepts/autodidata]]
- [[wiki/concepts/contribuir-open-source]]
- [[wiki/concepts/entrevista-tecnica-coding]]
- [[wiki/concepts/concorrencia]]
- [[wiki/concepts/go-concorrencia]]
- [[wiki/concepts/rust-ownership-borrowing-lifetimes]]

## Entidades citadas

- [[wiki/entities/the-primeagen]]
- [[wiki/entities/theodor]]
- [[wiki/entities/lucas-montano]]
- [[wiki/entities/filipe-deschamps]]
- [[wiki/entities/fabio-akita]]

---

## Citações

> "A pessoa que treina pra maratona não tá treinando pra competir com um carro."

> "Conforme você vai entendendo mais como as coisas funcionam, você começa a ter uma percepção melhor do que é realmente necessário usar uma dependência externa ou não. É assim que você amadurece como desenvolvedor."

> "Eu me sentia incomodado de pegar uma biblioteca pronta e magicamente meu código ficar mais rápido — eu queria entender o que estava acontecendo por debaixo dos panos."

> "Não acreditem na ilusão de que virar engenheiro de software é a fórmula mágica pra ganhar dinheiro e ficar milionário da noite pro dia."

---

## Questões abertas

- A identidade de "Theodor" não foi confirmada — pode se referir a um streamer/YouTuber de nome foneticamente parecido (ex. Theo/t3.gg) que também comentou publicamente sobre desenvolver jogos sem engine, mas o vídeo-fonte não fornece sobrenome, canal ou link. Ver nota de incerteza em [[wiki/entities/theodor]].
- O áudio de Fábio Akita é citado em segunda mão (via vídeo de Filipe Deschamps, que por sua vez reage a um vídeo de Lucas Montano) — não há confirmação direta do contexto original em que Akita disse isso.
- O vídeo não cita nenhum estudo controlado sobre a relação entre "estudar low-level" e "conseguir emprego melhor" — toda a argumentação é anedótica (caso próprio do autor + comentários de espectadores).
