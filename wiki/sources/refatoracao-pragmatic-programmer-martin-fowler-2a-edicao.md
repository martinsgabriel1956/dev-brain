---
type: source
title: "Refatoração: Pragmatic Programmer, Martin Fowler e a 2ª Edição de Refactoring"
aliases: ["essência e acidente refatoração", "2ª edição Refactoring Fowler", "seis situações para refatorar"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_file: "raw/refatoracao-pragmatic-programmer-martin-fowler-2a-edicao.md"
source_url: ""
author: "não identificado (vídeo YouTube, português)"
date_published: ""
date_ingested: 2026-07-27
source_count: 0
tags: [refactoring, martin-fowler, pragmatic-programmer, thoughtworks, essential-complexity, accidental-complexity, craftsmanship, tech-debt]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Vídeo que cruza três fontes sobre refatoração: um capítulo do *Pragmatic Programmer*, uma palestra de Martin Fowler sobre a 2ª edição de *Refactoring* (20 anos depois da primeira) e uma entrevista de Fowler com uma brasileira da Thoughtworks. Usa o motivo da segunda edição — código Java datado (ex.: a classe `Vector`) e exemplos por demais atrelados a orientação a objetos — como prova da distinção entre [[wiki/concepts/accidental-complexity|acidente]] (tecnologia, que muda) e [[wiki/concepts/essential-complexity|essência]] (princípios, que ficam). Destaca a troca do exemplo didático de locadora de vídeos por um sistema de peças de teatro, escolhido por ser um domínio mais permanente. Retoma a analogia de jardinagem do *Pragmatic Programmer* (em oposição à analogia de construção civil) para explicar por que o código degrada com o tempo, define refatoração como o próprio Fowler a define (mudança estrutural pequena que não altera comportamento), lista as duas motivações de Fowler para refatorar e as seis situações do *Pragmatic Programmer*, e fecha com três dicas de Fowler para refatorar com segurança.

## Key Claims

**Claim:** A segunda edição de *Refactoring* existe porque a primeira ficou desatualizada tecnicamente (Java antigo, ex. classe `Vector` em desuso) e porque refatorações estavam demais atreladas ao paradigma orientado a objetos, apesar de refatoração valer para qualquer paradigma.
**Evidence:** Atribuído diretamente a uma resposta de Martin Fowler numa entrevista com uma brasileira da Thoughtworks; a nova edição passou a usar JavaScript em vez de Java.
**Confidence:** média-alta — atribuição nomeada e motivo específico (a classe `Vector`), mas paráfrase de fala, sem citação textual, e a entrevista primária não foi lida diretamente nesta ingestão (apenas relatada de segunda mão pelo autor do vídeo).

**Claim:** O exemplo didático central do livro mudou de uma locadora de vídeos (1ª edição) para um sistema de gestão de peças de teatro (2ª edição), escolhido deliberadamente por ser um domínio mais permanente da atividade humana.
**Evidence:** Justificativa atribuída a Fowler: peças de teatro existem desde a Grécia Antiga, enquanto locação de fitas de vídeo já é tecnologia obsoleta — a troca aumenta a durabilidade didática do livro.
**Confidence:** média — plausível e coerente com o argumento essência/acidente do próprio vídeo, mas não verificado contra o texto do livro nesta ingestão.

**Claim:** Desenvolvimento de software se assemelha mais a jardinagem do que a construção civil — analogia atribuída ao *Pragmatic Programmer*. Software é algo vivo que degrada ("decaying") com o tempo (débito técnico), e refatoração é o equivalente a podar plantas daninhas e galhos em excesso para manter o sistema saudável.
**Evidence:** Contraste explícito com a analogia de construção civil, descrita no vídeo como menos adequada porque prédios não têm a mesma natureza de crescimento orgânico e imprevisível do código.
**Confidence:** média-alta — atribuição a fonte nomeada (Pragmatic Programmer), consistente com o enquadramento de degradação de design já presente em [[wiki/concepts/refatoracao]] via [[wiki/sources/o-que-e-refatoracao-quando-usar]].

**Claim:** Refatoração, segundo Fowler, é definida como uma alteração estrutural tão pequena que isoladamente pareceria não valer a pena (ex.: renomear uma variável) — o valor aparece apenas na soma de muitas pequenas alterações ao longo do tempo.
**Evidence:** Exemplo dado: mudar o nome de uma variável altera a estrutura do código sem alterar seu comportamento; comparação com cortar grama — atividade de rotina, não esporádica.
**Confidence:** alta — consistente com a definição já registrada em [[wiki/concepts/refatoracao]] (mudança de estrutura interna sem alteração de comportamento externo).

**Claim:** Fowler aponta duas motivações centrais para refatorar: (1) quando o desenvolvedor entende melhor o código e quer refletir esse entendimento na estrutura; (2) quando uma alteração planejada seria difícil de fazer no estado atual do código, e a refatoração facilita essa mudança futura. A recomendação é alternar continuamente entre adicionar funcionalidade e refatorar.
**Evidence:** Paráfrase direta atribuída a Fowler, sem citação textual.
**Confidence:** média-alta — consistente com [[wiki/concepts/dois-chapeus-kent-beck]] (alternância consciente entre os dois modos), embora a fonte primária (livro ou palestra) não tenha sido conferida diretamente.

**Claim:** O *Pragmatic Programmer* lista seis situações em que vale a pena refatorar: duplicação (DRY), falta de ortogonalidade/acoplamento excessivo, conhecimento desatualizado sobre requisitos, mudança de prioridades ao ser usado por usuários reais, oportunidade de melhoria de performance, e — a mais contraintuitiva — quando um teste está passando (o que dá segurança para o teste de regressão detectar quebras).
**Evidence:** Lista apresentada como extraída diretamente do livro, sem citação textual literal.
**Confidence:** média — atribuição nomeada e específica, mas paráfrase; a sexta situação ("quando um teste passa" como motivo positivo para refatorar, não apenas pré-requisito) é um ângulo pouco comum e vale confirmar contra o texto original numa ingestão futura do livro.

**Claim:** Fowler dá três dicas práticas para que a refatoração traga mais benefício que dano: (1) nunca misturar adicionar funcionalidade com refatorar no mesmo momento; (2) sempre ter testes para as refatorações e rodá-los com frequência; (3) avançar em passos pequenos e deliberados ("baby steps"), nunca fazendo várias refatorações ao mesmo tempo.
**Evidence:** Paráfrase atribuída a Fowler; a primeira dica é explicitamente ligada ao ciclo RED-GREEN-REFACTOR do TDD.
**Confidence:** alta — as três dicas reforçam, sem contradizer, o que já está registrado em [[wiki/concepts/refatoracao]] (passos pequenos, testes como rede de segurança) e em [[wiki/concepts/dois-chapeus-kent-beck]].

## Essência vs. Acidente Aplicado a Livros Técnicos

```
Acidental (muda, tem prazo de validade):
  linguagem/tecnologia do exemplo didático (Java → JavaScript)
  domínio do exemplo didático (locadora de vídeos → peças de teatro)
  classes/APIs específicas que saem de uso (ex.: Vector em Java)

Essencial (não muda, por isso o livro de 20 anos continua relevante):
  definição de refatoração (mudança estrutural sem alterar comportamento)
  necessidade de testes como rede de segurança
  passos pequenos e deliberados
  alternância consciente entre adicionar funcionalidade e refatorar
```

## Entities & Concepts Touched

- [[wiki/concepts/refatoracao]]
- [[wiki/concepts/essential-complexity]]
- [[wiki/concepts/accidental-complexity]]
- [[wiki/concepts/dois-chapeus-kent-beck]]
- [[wiki/concepts/entropia-de-software]] (novo)
- [[wiki/concepts/livros-recomendados-programador]]
- [[wiki/concepts/tdd]]
- [[wiki/entities/martin-fowler]]
- [[wiki/entities/thoughtworks]] (novo)

## Open Questions

- O vídeo afirma que a Thoughtworks "foi fundada também pelo Martin Fowler". Isso **contradiz** o que já está registrado em [[wiki/entities/martin-fowler]] (Chief Scientist da Thoughtworks, não fundador — a empresa foi fundada por Roy Singham em 1993, com Fowler entrando anos depois). Tratado como possível erro/imprecisão do autor do vídeo, não como fato verificado; sinalizado também na entity.
- A entrevistadora brasileira da Thoughtworks não é identificada pelo nome na transcrição — não foi possível criar uma entity específica para ela.
- Todas as atribuições a Martin Fowler nesta fonte são paráfrases de fala (o autor do vídeo relatando o conteúdo de uma palestra e de uma entrevista que assistiu), não citações textuais diretas nem transcrição da fonte primária — vale revisitar com a palestra/entrevista originais ou com o texto da 2ª edição do livro numa ingestão futura.
- Não fica claro no vídeo se as "seis situações para refatorar" do Pragmatic Programmer vêm do mesmo capítulo que a analogia de jardinagem, ou de seções diferentes do livro.
