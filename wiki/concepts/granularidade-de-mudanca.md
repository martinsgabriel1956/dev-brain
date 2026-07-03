---
type: concept
title: "Granularidade de Mudança"
aliases: ["mudança pequena vs mudança grande", "small batches", "barreira de implementação"]
date_created: 2026-07-03
date_updated: 2026-07-03
source_count: 1
tags: [arquitetura, carreira, mudanca-organizacional, coesao, granularidade]
skill: tech-mentor-leadership
status: draft
---

# Granularidade de Mudança

Princípio de que **o tamanho de uma mudança determina o tamanho da barreira para implementá-la**: quanto maior o escopo de uma mudança (técnica, de processo ou de arquitetura), maior o tempo, a complexidade e o esforço de convencimento necessários para aplicá-la. A implicação prática é separar mudanças grandes em partes pequenas e coesas em vez de tentar aplicar tudo de uma vez.

## Por que mudança grande gera barreira grande

- **Demora mais** — reescrever um processo ou uma arquitetura estabelecida há anos é lento, mesmo quando o estado atual é ruim.
- **É mais complexa** — uma migração de monólito para microsserviços, por exemplo, é um projeto inteiro, ainda mais quando o sistema atual já está em produção gerando receita.
- **É mais difícil de vender** — "parece boa ideia, mas não é viável" é a resposta padrão para propostas grandes; o argumento necessário para convencer cresce proporcionalmente ao tamanho da mudança.

Esse tipo de mudança só tende a funcionar quando vem de quem tem autoridade formal para impor um "top-down" (CTO, diretor de tecnologia, dono da empresa). Para quem não tem esse tipo de autoridade, insistir numa mudança grande de uma vez tende a travar por atrito, não por a ideia estar errada.

## A alternativa: separar em partes coesas

O princípio vem diretamente da arquitetura de software: quanto mais granular, mais simples e mais fácil de manter. Aplicado a mudanças de processo ou tecnologia:

- Separe a mudança em pedaços pequenos que ainda façam sentido isoladamente — o mesmo critério de [[wiki/concepts/coesao]] usado para desenhar módulos de código se aplica a desenhar mudanças organizacionais.
- Parar para pensar em como dividir já reforça o entendimento do que está sendo aplicado — força a entender o conceito de verdade, em vez de copiar um pedaço sem sentido.
- Mudanças pequenas são mais rápidas de aplicar, mais simples de reverter se derem errado, e geram menos atrito porque muitas vezes nem afetam o usuário final ou a empresa diretamente — só o time, ou só quem propôs.

Exemplo do vídeo-fonte: em vez de tentar impor Scrum ou Kanban inteiros de uma vez, começar só por dailies — desde que a prática seja aplicada com o propósito original, e não copiada superficialmente.

## O requisito de valor real

Separar em partes pequenas não é suficiente por si só — cada parte ainda precisa gerar valor real (para quem propõe, para o time, ou para a empresa). Trocar uma linguagem de produção só porque se aprendeu um recurso legal dela, ou adotar mensageria assíncrona sem necessidade, são mudanças pequenas que ainda assim não valem a pena, porque não resolvem um problema de verdade — ver [[wiki/concepts/cargo-cult-tecnologico]].

## Ver também

- [[wiki/concepts/coesao]] — o critério para saber onde cortar uma mudança em partes que ainda fazem sentido isoladamente
- [[wiki/concepts/cargo-cult-tecnologico]] — mudança pequena ou grande, o erro persiste se não houver valor real de contexto por trás
- [[wiki/concepts/arquitetura-de-software]] — granularidade como princípio arquitetural aplicado além do código

## Key Sources

- [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]]
