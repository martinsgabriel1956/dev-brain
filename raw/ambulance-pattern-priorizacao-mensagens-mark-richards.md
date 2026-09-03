---
date: 2026-09-02
tags: [tech-mentor, system-design, arquitetura, filas, priorizacao, mensageria, mark-richards, developer-to-architect]
skill: tech-mentor-system-design
level: intermediário
source_url: https://www.developertoarchitect.com/lessons/lesson56.html
video_url: https://www.youtube.com/watch?v=XBVX9sEydnU
author: Mark Richards
---

# The Ambulance Pattern (Lição 56 — Developer to Architect / Software Architecture Monday)

*(Tradução e limpeza de transcrição em inglês. Vídeo curto de ~5 minutos, canal "Software Architecture Monday" de Mark Richards.)*

## Contexto

O nome vem de uma cena comum no trânsito: você está dirigindo e, de repente, vê uma ambulância se aproximando pelo retrovisor. A maioria dos carros percebe a ambulância e se afasta para deixá-la passar. Esse é exatamente o conceito do padrão: como dar a algumas requisições uma prioridade maior do que outras, garantindo que elas "furem a fila" igual a ambulância fura o trânsito.

O cenário de referência: dois tipos de requisição chegando em um componente de serviço, que por sua vez enfileira essas requisições antes de repassá-las a outro componente de serviço. Um tipo (vermelho) é de alta prioridade; o outro (verde/amarelo) é o fluxo normal do dia a dia.

Mark Richards apresenta duas técnicas de implementação — uma que não funciona bem, e uma melhor — e explica por que a primeira falha na prática.

## Técnica 1 — Prioridade na Mensagem (não recomendada)

A ideia mais óbvia é usar um campo de prioridade no header da própria mensagem: um valor numérico, ou algo como baixo/médio/alto. As mensagens vindas da fonte de alta prioridade são marcadas como "alta"; o restante, como "média".

Na prática, mensagens marcadas como alta prioridade sempre vão para a cabeça da fila — e isso é o problema. Assim que mensagens de alta prioridade começam a chegar, elas passam a **sempre furar a fila**, o que desacelera ou até paralisa completamente o processamento das mensagens normais. Isso é especialmente grave quando o sistema está esperando por uma resposta síncrona dessas mensagens normais: elas podem sofrer timeout porque nunca chegam a ser processadas enquanto houver tráfego de alta prioridade.

Ou seja: prioridade dentro da mensagem resolve o problema de "chegar na frente", mas cria um novo problema de **inanição (starvation)** do fluxo normal.

## Técnica 2 — Fila de Priorização (recomendada)

A alternativa melhor é **dividir a fila em duas**: uma fila para o fluxo normal (amarelo) e uma fila dedicada de alta prioridade (vermelho). Em vez de competir pela posição dentro de uma única fila, cada tipo de mensagem tem seu próprio canal.

Com essa separação, mensagens normais continuam fluindo pelo canal padrão sem interrupção, enquanto mensagens de alta prioridade são roteadas para a fila dedicada e processadas em paralelo — sem que uma dependa da outra. O resultado: as duas classes de mensagem podem ser processadas **ao mesmo tempo**, sem que a chegada de tráfego prioritário trave o fluxo normal.

## Refinamento — Fila + Instância Dedicada

Uma evolução da técnica 2 é combinar a fila de priorização com uma **instância de serviço dedicada** para a fila de alta prioridade. Em vez de um único componente de serviço escutando as duas filas, o componente é dividido em duas instâncias: uma escuta apenas a fila de alta prioridade, a outra escuta apenas a fila normal.

Isso dá processamento verdadeiramente paralelo — útil sobretudo para escalabilidade e para lidar com gargalos: se o componente de serviço vira um bottleneck, já existe uma instância dedicada isolada para tratar o tráfego crítico, sem competir por recursos com o tráfego normal. Richards observa que, sem cuidado, essa instância dedicada tende a ficar ociosa a maior parte do tempo — uma forma simples de configurar isso é fazer com que qualquer instância do componente possa, via configuração (idealmente em runtime), escutar a fila de alta prioridade ou a fila normal, permitindo redistribuir capacidade dinamicamente em vez de reservar hardware fixo e ocioso.

## Conclusão

- **Não usar** prioridade embutida na própria mensagem/header como mecanismo de priorização — ela garante que a mensagem prioritária sempre vá para a frente, mas ao custo de starvation do fluxo normal.
- **Usar** filas fisicamente separadas (uma normal, uma de alta prioridade) para permitir processamento paralelo genuíno.
- Opcionalmente, **dedicar instâncias de serviço** a cada fila para isolar ainda mais o tráfego crítico e facilitar o scaling independente de cada canal.
