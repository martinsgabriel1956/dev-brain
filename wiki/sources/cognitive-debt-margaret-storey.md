---
type: source
title: "Cognitive Debt (Margaret-Anne Storey, fonte primária)"
aliases: ["cognitive debt storey", "dívida cognitiva storey", "teoria do programa naur", "theory of programs"]
date_created: 2026-07-16
date_updated: 2026-07-16
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/cognitive-debt.md
source_url: "https://margaretstorey.com/blog/2026/02/09/cognitive-debt/"
date_published: "2026-02-09"
date_ingested: 2026-07-16
source_count: 0
tags: [divida-cognitiva, tech-debt, peter-naur, theory-of-programs, code-review, ia-agentica, liderança-tecnica]
skill: tech-mentor-leadership
status: stable
---

## TL;DR

Fonte primária que cunha "cognitive debt": dívida técnica mora no código, dívida cognitiva mora na cabeça dos desenvolvedores. Fundamenta o conceito na teoria de Peter Naur de que "um programa é uma teoria" que vive na mente de quem o constrói — teoria essa que se fragmenta entre várias pessoas, não reside numa só. IA generativa/agêntica pode gerar código compreensível linha a linha sem que ninguém no time retenha o *porquê* das decisões. Estudo de caso: equipe de alunos trava na 7ª/8ª semana não por débito técnico, mas porque ninguém consegue explicar as decisões de design do próprio sistema. Prevenção: exigir compreensão humana antes do deploy, documentar o porquê (não só o quê), checkpoints regulares de entendimento compartilhado.

## Key Claims

**Claim:** Dívida técnica e dívida cognitiva são categorias distintas porque o "onde mora" o problema é diferente — uma no código, outra nas pessoas.
**Evidence:** "This framing suggests the problem resides in the code itself" (dívida técnica) vs. dívida cognitiva como "the burden compounded from going fast lives in the brains of the developers." Mesmo quando a IA produz código compreensível linha a linha, desenvolvedores podem perder a compreensão do propósito do programa, de como suas intenções foram implementadas, ou de como modificá-lo.
**Confidence:** alta

**Claim:** A base teórica do conceito é Peter Naur (1985): um programa é uma teoria que vive na mente do(s) desenvolvedor(es), não apenas o código-fonte ou a documentação.
**Evidence:** "A program is a theory that lives in the minds of the developer(s)", abrangendo o que o programa faz e como pode evoluir. Essa compreensão tipicamente se fragmenta entre várias mentes, em vez de residir numa única pessoa — o que já torna dívida cognitiva um risco coletivo/organizacional mesmo sem IA envolvida, e a IA acelera esse risco ao gerar código mais rápido do que qualquer time consegue internalizar a teoria por trás dele.
**Confidence:** alta

**Claim:** Times acumulam dívida cognitiva mais rápido que dívida técnica quando usam IA generativa/agêntica intensamente, e o sintoma é indistinguível de dívida técnica até uma investigação mais profunda.
**Evidence:** Estudo de caso de curso de empreendedorismo: equipe de estudantes bate numa parede por volta da 7ª/8ª semana. Diagnóstico inicial da própria equipe foi "dívida técnica"; investigação mais profunda revelou que "ninguém na equipe conseguia explicar por que certas decisões de design haviam sido tomadas ou como diferentes partes do sistema deveriam funcionar juntas" — o entendimento compartilhado havia desaparecido, não o código.
**Confidence:** alta

**Claim:** Prevenção de dívida cognitiva exige práticas concretas de time, não apenas disciplina individual.
**Evidence:** Três estratégias citadas: (1) exigir que ao menos uma pessoa entenda totalmente cada mudança gerada por IA antes do deploy; (2) documentar não apenas o que mudou, mas por quê; (3) checkpoints regulares para reconstruir entendimento compartilhado via code review e retrospectivas.
**Confidence:** alta

**Claim:** Sinais de alerta de dívida cognitiva em progresso são observáveis antes de virar crise.
**Evidence:** Hesitação de membros do time em fazer mudanças por medo de consequências não previstas; dependência crescente de "conhecimento tribal" concentrado em uma ou duas pessoas; o sistema ficando cada vez mais opaco com o tempo.
**Confidence:** alta

**Claim:** Medir dívida cognitiva, identificar práticas eficazes de prevenção em ambientes aumentados por IA, e entender como ela escala em times distribuídos são questões de pesquisa ainda em aberto.
**Evidence:** A autora encerra o post afirmando explicitamente que o tema demanda investigação séria nessas três frentes, sem propor uma métrica validada.
**Confidence:** alta — é uma afirmação da própria autora sobre o estado da pesquisa, não uma inferência externa.

## Entities & Concepts Touched

- [[wiki/concepts/divida-cognitiva]]
- [[wiki/concepts/comprehension-debt]]
- [[wiki/concepts/teoria-do-programa-naur]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/code-review]]
- [[wiki/entities/margaret-storey]]
- [[wiki/entities/peter-naur]]

## Open Questions

- Nenhuma métrica concreta de dívida cognitiva é proposta na fonte — a própria autora trata "medir dívida cognitiva" como pergunta de pesquisa em aberto, não como algo resolvido.
- Como o requisito "ao menos uma pessoa entende totalmente cada mudança gerada por IA" escala quando o volume de mudanças geradas por agentes supera a capacidade de revisão humana do time — tensão não resolvida na fonte, mas already presente em [[wiki/concepts/comprehension-debt]] (rubber-stamping sob pressão).
- A correção de afiliação institucional de Margaret-Anne Storey (University of Victoria, Canada Research Chair — não UBC, como a wiki tinha registrado antes desta ingestão) foi feita a partir do rodapé desta fonte primária; vale reconfirmar contra o site institucional se a página mudar no futuro.
