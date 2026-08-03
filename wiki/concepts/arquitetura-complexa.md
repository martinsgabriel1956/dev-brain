---
type: concept
title: "Arquitetura Complexa"
aliases: ["complex architecture", "complexidade arquitetural"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 1
tags: [system-design, arquitetura, complexidade, legado, poliglota, over-thinking]
skill: tech-mentor-system-design
status: stub
---

# Arquitetura Complexa

Arquitetura marcada por componentes interdependentes, tecnologia poliglota e múltiplos tipos de comunicação convivendo (SOAP, REST, batch, mensageria assíncrona). Ao contrário da [[wiki/concepts/large-scale-architecture]], a complexidade **não depende de volume/tráfego** — acontece em qualquer tamanho de sistema, de 100 a 1 milhão de usuários.

## Causa mais comum: legado convivendo com o novo

A forma mais frequente de complexidade arquitetural aparece em empresas enterprise antigas (décadas no mercado) que precisam **modernizar sem desligar o passado** — refatoração gradual em vez de substituição. Exemplo típico: workloads que migraram de mainframe para AS/400, depois para Linux, depois para Windows, sem nunca eliminar completamente as camadas anteriores. Isso gera dependências cruzadas entre plataformas heterogêneas que precisam se comunicar por múltiplos protocolos diferentes.

Startups recentes tendem a ter menos desse tipo de complexidade — mesmo quando grandes, não carregam o mesmo peso de decisões antigas incompatíveis com o modelo atual.

## Regra de negócio complexa

Regras de negócio ficam complexas majoritariamente pelo mesmo motivo: "eu atendia isso no passado, não posso desligar, não tenho como reescrever tudo e parar de entregar novas funcionalidades". Ver [[wiki/concepts/codigo-legado-ia]] e [[wiki/concepts/refactor-vs-rewrite-matrix]] para estratégias de lidar com esse tipo de legado.

## Anti-pattern associado: over-thinking

Distinto do [[wiki/concepts/over-engineering]] (excesso de ferramental/tecnologia, mais associado a large scale), o **over-thinking** é excesso de pensamento que não simplifica regras e decisões — gerando complexidade artificial mesmo sem pressão de escala ou legado real.

## Sem métrica objetiva de classificação

Não há um checklist confiável para dizer se uma arquitetura "é complexa" — é relativo ao observador. Os patterns de mitigação (ver [[wiki/concepts/accidental-complexity]] e [[wiki/concepts/essential-complexity]] para a distinção mais formal de Fred Brooks) ajudam independentemente da classificação.

## Relação com outros conceitos

- [[wiki/concepts/accidental-complexity]] / [[wiki/concepts/essential-complexity]] — distinção mais formal (Fred Brooks) sobre origem da complexidade; a "complexidade de legado" descrita aqui é majoritariamente acidental (decisão de não migrar tudo), mas pode ter núcleo essencial (regra de negócio genuinamente complexa).
- [[wiki/concepts/large-scale-architecture]] — eixo independente; uma arquitetura pode ser as duas coisas, uma delas ou nenhuma.

## Key Sources

- [[wiki/sources/large-scale-vs-complex-architecture]]
