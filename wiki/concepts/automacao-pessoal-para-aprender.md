---
type: concept
title: "Automação Pessoal para Aprender"
aliases: ["side project de automação", "automação caseira", "pratica em prod pessoal"]
date_created: 2026-07-03
date_updated: 2026-08-17
source_count: 2
tags: [aprendizado, pratica-deliberada, carreira, automacao, autonomia]
skill: tech-mentor-leadership
status: draft
---

# Automação Pessoal para Aprender

Estratégia de criar pequenos programas — rodando na própria máquina do dev, fora da infraestrutura e do pipeline de entrega da empresa — que resolvem um problema manual e repetitivo real (do próprio dev, do time ou da empresa), usando a tecnologia que se quer aprender como implementação. Diferente de um exercício de curso, o problema é real e tem contexto real; diferente de aplicar a mudança direto em produção, o risco é baixo porque o programa é independente.

## Por que funciona melhor que praticar em curso

Um exercício de curso é deliberadamente simplificado por razões didáticas — boa arquitetura, responsabilidades bem divididas, ausência de restrição de prazo ou política interna. Uma automação pessoal, mesmo pequena, ainda carrega o contexto real do trabalho: um problema que ninguém mais vai resolver, dados reais, e a necessidade de fazer a coisa funcionar de verdade — não só "passar no exercício".

## Por que funciona melhor que aplicar direto em produção

- **Sem pressão de entrega** — um programa independente não tem prazo de negócio; se travar numa parte, dá para parar e voltar depois sem custo para ninguém além do próprio dev.
- **Sem dependência de infraestrutura ou aprovação** — roda na própria máquina, sem precisar de acesso a servidor, licença, ou autorização de terceiros para experimentar.
- **Liberdade de arquitetar do próprio jeito** — dá para errar, tentar de novo, aplicar um padrão arquitetural novo (ex: Clean Architecture, arquitetura hexagonal) sem afetar ninguém além de quem está aprendendo.

## Formatos comuns

| Tipo de automação | O que força a praticar |
|---|---|
| Web scraper | Parsing de texto/HTML, pattern matching — conceitos básicos de qualquer linguagem nova |
| Gerador de relatório | Consulta a dados, geração de gráfico/planilha — bom pretexto para testar um framework SPA ou uma lib de exportação nova |
| Importador de dados (ex: ler Excel e gravar na base) | Modelagem de dados, tratamento de entrada externa |

## Constância em vez de volume

A recomendação prática associada é reservar um bloco pequeno e fixo de tempo (10–20 minutos/dia) fora do expediente, em vez de tentar resolver tudo de uma vez — o ganho vem da repetição regular, não da intensidade de uma única sessão. Alinhado ao teto cognitivo diário documentado em [[wiki/concepts/pratica-deliberada]].

## Relação com o risco assumido

Quando a automação pessoal cresce e o dev quer levá-la para dentro do trabalho oficial (aplicar a mesma tecnologia num sistema real da empresa), o cálculo de risco muda — deixa de ser "sem custo para ninguém" e passa a exigir assumir a responsabilidade pelo resultado. Ver a tensão registrada em [[wiki/concepts/autonomia-responsabilidade]].

## Ver também

- [[wiki/concepts/pratica-deliberada]] — a automação pessoal é uma forma concreta de estruturar prática deliberada com feedback real
- [[wiki/concepts/autonomia-responsabilidade]] — onde termina o espaço "sem pedir permissão" e começa a exigência de alinhamento formal
- [[wiki/concepts/aprendizado-passivo]] — o oposto: consumir curso/vídeo sem nunca construir nada com as próprias mãos
- [[wiki/concepts/projeto-impossivel]] — variante de escala: onde a automação pessoal cobre tecnologia nova em setup pequeno, o projeto impossível cobre especificamente conceitos que só existem em escala e não cabem numa automação isolada

## Key Sources

- [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]]
- [[wiki/sources/como-nunca-mais-esquecer-o-que-voce-estuda-programacao]] — introduz o conceito irmão de maior escala, [[wiki/concepts/projeto-impossivel]]
