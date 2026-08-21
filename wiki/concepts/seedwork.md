---
type: concept
title: "Seedwork"
aliases: ["seed work", "framework mínimo reconstruído por time"]
date_created: 2026-07-19
date_updated: 2026-08-21
source_count: 2
tags: [testes, reuso, frameworks, kent-beck, xunit, arquitetura, application-boundary]
skill: tech-mentor-backend
status: stable
---

# Seedwork

Termo cunhado por [[wiki/entities/martin-fowler]] (a partir de uma discussão originada num post de Michael Feathers) para descrever uma alternativa a frameworks reutilizáveis tradicionais: em vez de estender um framework compartilhado de forma controlada, cada time parte de uma funcionalidade mínima ("seed") e a modifica livremente conforme sua necessidade. A consequência é que não há como receber atualizações comuns depois — uma vez que o time "faz crescer" o seedwork, ele é dono daquilo, para o bem e para o mal. Ver a fonte primária em [[wiki/sources/seedwork-martin-fowler]].

## Por que existe

Reuso de frameworks completos é difícil de acertar — frameworks bem "amadurecidos" funcionam bem, mas chegar lá é raro, e frameworks mal ajustados adicionam complexidade que atrapalha mais do que ajuda. Seedwork não é o ideal (é essencialmente reuso via copiar-e-colar, que Fowler reconhece ser normalmente criticável), mas é mais fácil de criar e usar do que um framework robusto — o critério não é se é elegante, é se é útil.

## Reuso entre aplicações é mais difícil que reuso interno

Segundo [[wiki/sources/seedwork-martin-fowler]], Fowler generaliza o argumento: evitar duplicação **dentro** de uma aplicação é vital e alcançável; reuso **entre** aplicações é muito mais difícil, porque uma [[wiki/concepts/application-boundary|ApplicationBoundary]] é, antes de tudo, uma construção social — mesma tese que ele desenvolve, no mesmo dia (11 de setembro de 2003), em [[wiki/sources/application-boundary-martin-fowler]]. O artigo também cita o "DLL-hell" da Microsoft e problemas reais de dependências quebradas como prova de que até o reuso maduro (bibliotecas compartilhadas versionadas) é difícil de acertar quando os cronogramas de atualização de diferentes times não se alinham.

## Tensão com Under-Engineering

[[wiki/concepts/under-engineering]] lista "copy-paste sem estrutura" como sintoma de engenharia insuficiente. Seedwork defende esse mesmo padrão como pragmático — a diferença está no contexto: copy-paste é um problema quando existe alternativa madura sendo evitada por atalho; é uma solução razoável quando a alternativa realista é "nenhum framework compartilhado disponível". Ver detalhamento em [[wiki/sources/seedwork-martin-fowler]].

## Exemplo concreto na wiki: o framework de testes de Kent Beck

[[wiki/entities/kent-beck]] construía frameworks de teste em Smalltalk para si e seus clientes, e preferia que cada time reconstruísse o próprio (levava poucas horas) em vez de compartilhar um único framework — isso é, na prática, um Seedwork, segundo o próprio Fowler. Esse padrão foi o antecessor direto do [[wiki/entities/junit]], que rompeu esse modelo ao se tornar o primeiro framework de testes amplamente compartilhado e reutilizado fora do Smalltalk. Ver [[wiki/sources/xunit-martin-fowler]].

## Ver também

- [[wiki/entities/kent-beck]]
- [[wiki/entities/junit]]
- [[wiki/entities/c3-project]]
- [[wiki/concepts/application-boundary]]
- [[wiki/concepts/under-engineering]]

## Key Sources

- [[wiki/sources/seedwork-martin-fowler]] — fonte primária, ingerida em 2026-08-21
- [[wiki/sources/xunit-martin-fowler]]
