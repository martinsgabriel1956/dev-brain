---
type: source
title: "Fatores Não Técnicos que Explicam Código Ruim de Bons Desenvolvedores"
aliases: ["código ruim não é sempre dev ruim", "por que bons devs escrevem código ruim", "4 fatores código ruim bernardo lobato"]
date_created: 2026-09-15
date_updated: 2026-09-15
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/fatores-nao-tecnicos-codigo-ruim-bons-desenvolvedores-bernardo-lobato.md
source_url: ""
author: "Bernardo Lobato"
date_published: ""
date_ingested: 2026-09-15
source_count: 0
tags: [tech-debt, carreira, code-review, contexto-organizacional, incentivos, metricas, goodharts-law]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Vídeo curto e reflexivo de Bernardo Lobato argumentando contra a simplificação "código ruim = dev ruim". Propõe um framework de quatro fatores não técnicos que podem levar um profissional experiente a entregar um código abaixo do que ele seria capaz de produzir em condições ideais: (1) pressão de prazo, (2) contexto do projeto (legado, dependências, restrições de infraestrutura), (3) conhecimento incompleto e o fator tempo (evolução do próprio dev), e (4) incentivos organizacionais que recompensam volume/velocidade sem recompensar qualidade. A conclusão evita cair no extremo oposto (normalizar qualquer código ruim como "culpa do contexto"): o ponto central é reconhecer quando se está tomando dívida técnica **conscientemente** e torná-la visível — registrar o tradeoff no backlog — em vez de deixá-la como problema implícito do futuro.

## Key Claims

**Claim:** Julgar código de um projeto legado como "ruim" isoladamente, sem considerar o contexto em que foi produzido, é uma armadilha comum mesmo entre desenvolvedores experientes — comparar aquele código com o que se escreveria "começando do zero hoje" é uma comparação injusta.
**Evidence:** Anedota do autor: viu colegas criticando código de um projeto legado sabendo que os profissionais responsáveis eram excelentes — usa isso como gatilho para o resto do vídeo. Reivindica que "100% dos devs já caíram" nessa armadilha.
**Confidence:** média — é observação pessoal/anedótica do autor, sem estudo ou dado citado, mas coerente com [[wiki/concepts/contexto-organizacional-para-arquitetura]], já registrado na wiki com fontes independentes (Fowler 2003, Conway 1968).

**Claim:** Pressão de prazo (ex.: feature que levaria duas semanas sendo exigida em dois dias) pode levar um desenvolvedor experiente a uma decisão racional de reduzir escopo de testes e qualidade — o erro não é tomar esse atalho, é não convertê-lo em dívida técnica explícita e tratada depois com rigor.
**Evidence:** Descrito em termos idênticos ao Quadrante de Fowler ([[wiki/concepts/quadrante-de-fowler]]) — dívida Prudente+Deliberada — mas sem citar Fowler nominalmente ou usar o vocabulário de quadrante.
**Confidence:** alta como reformulação — o raciocínio já está bem documentado e triangulado em [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] e [[wiki/sources/5-principles-that-changed-me-as-a-programmer]].

**Claim:** Profissionais especialistas em uma linguagem tendem a transportar padrões idiomáticos dessa linguagem (nomes, estrutura de classes) para outra linguagem em que atuam com menos frequência, produzindo código que "soa inadequado" na linguagem de destino.
**Evidence:** Afirmação genérica do autor, sem exemplo nomeado de linguagem específica nem caso real citado.
**Confidence:** baixa/média — plausível e consistente com o argumento central de [[wiki/sources/go-is-not-java]] (padrões de OOP/Java forçados em Go), mas a fonte não faz essa conexão explicitamente nem cita nenhum caso.

**Claim:** O mesmo código escrito pelo mesmo profissional cinco anos atrás tende a ser pior do que o código que ele escreve hoje — isso é evidência de aprendizado contínuo, não motivo de vergonha.
**Evidence:** Reflexão pessoal do autor, sem dado ou estudo citado.
**Confidence:** média — afirmação razoável mas não verificável a partir da fonte; não há contradição com nada já registrado na wiki.

**Claim:** Se a organização recompensa fechar tickets e cumprir deadline sem avaliar qualidade, e não recompensa redução de complexidade/dívida técnica/cobertura de testes, mesmo bons profissionais racionalmente vão otimizar o próprio trabalho para o que é medido, não para o que é ideal tecnicamente.
**Evidence:** Argumento por analogia direta ("se sou avaliado pela quantidade de tarefas, vou entregar mais tarefas") — não cita estudo, mas o mecanismo descrito é uma instância direta da [[wiki/concepts/goodharts-law|Lei de Goodhart]], já registrada e triangulada na wiki com outros casos (story points forçados, métricas de output infladas por IA).
**Confidence:** alta pela convergência com [[wiki/concepts/goodharts-law]] e [[wiki/concepts/output-vs-outcome]], mesmo sem a fonte nomear o mecanismo.

## Entities & Concepts Touched

- [[wiki/entities/bernardo-lobato]]
- [[wiki/concepts/quadrante-de-fowler]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/contexto-organizacional-para-arquitetura]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/goodharts-law]]
- [[wiki/concepts/output-vs-outcome]]
- [[wiki/concepts/boy-scout-rule]]
- [[wiki/concepts/fatores-nao-tecnicos-qualidade-de-codigo]]
- [[wiki/concepts/julgar-codigo-fora-de-contexto]]

## Open Questions

- A fonte não cita nenhum estudo, número ou caso nomeado em nenhum dos quatro fatores — é uma peça de opinião/reflexão pessoal. Vale reconciliar com fontes mais empíricas se aparecerem (ex.: dados de pesquisa sobre pressão de prazo e qualidade de código).
- O paralelo entre "transportar padrões de linguagem" e o caso concreto de [[wiki/sources/go-is-not-java]] não é feito pela própria fonte — é uma conexão que a wiki está fazendo retroativamente. Não tratar como se o autor tivesse citado esse exemplo.
- O quarto fator (incentivos organizacionais) é, na prática, uma aplicação não nomeada da Lei de Goodhart — a fonte não usa esse vocabulário. Mantido como inferência da wiki, marcado explicitamente acima, não como citação direta do autor.

## Fontes Relacionadas

Esta fonte não traz dado novo quantitativo, mas funciona como uma síntese unificadora: os quatro fatores que ela lista já estão, individualmente, bem mais desenvolvidos em outras fontes da wiki — [[wiki/sources/tech-debt-guia-completo-gestao-metricas]] e [[wiki/sources/5-principles-that-changed-me-as-a-programmer]] (fator 1, dívida deliberada), [[wiki/sources/application-boundary-martin-fowler]] e [[wiki/sources/talk-about-platforms-evan-bottcher]] (fator 2, contexto organizacional), e os casos de [[wiki/concepts/goodharts-law]] já registrados (fator 4, incentivos/métricas). O valor desta fonte é enquadrar os quatro num único framework de "por que bons devs escrevem código imperfeito", em vez de tratá-los como fenômenos separados — nenhuma contradição encontrada com o que já está na wiki.
