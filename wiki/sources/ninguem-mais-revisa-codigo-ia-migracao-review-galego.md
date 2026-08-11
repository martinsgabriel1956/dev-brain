---
type: source
title: "Ninguém Mais Revisa o Código da IA — Como Migrar de 'Eu Reviso' para 'Eu Não Reviso' (Galego)"
aliases: ["ninguém revisa código da IA", "migração review manual para automático", "matriz risco dificuldade merge automático galego"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [tech-mentor-leadership, code-review, quality-gate, agentes-ia, uncle-bob, boris, lucas-montano, claude-md, harness, extreme-programming, merge-automatico, augusto-galego]
skill: tech-mentor-leadership
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ninguem-mais-revisa-codigo-ia-migracao-review-galego.md
source_url:
author: Augusto Galego (inferido pelo estilo e pela assinatura "Galego" no áudio)
date_published:
date_ingested: 2026-08-11
---

# Ninguém Mais Revisa o Código da IA — Como Migrar de "Eu Reviso" para "Eu Não Reviso" (Galego)

## TL;DR

Terceiro vídeo de reação ao post de [[wiki/entities/uncle-bob]] ("I read the code" → "eu não reviso mais o código de agentes"), desta vez por [[wiki/entities/augusto-galego]]. Diferente dos dois anteriores ([[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]], focado no debate função-pequena vs. módulo-profundo, e [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]], focado nos quatro gates concretos de CI), esta fonte contribui com o **como transicionar na prática**: uma [[wiki/concepts/matriz-risco-dificuldade-review-ia|matriz de risco × dificuldade]] para decidir, PR a PR, o que já pode ir para merge automático, o que revisar por amostragem e o que ainda exige revisão humana em pares. Costura três vozes — Uncle Bob (métricas objetivas), [[wiki/entities/boris]] (documentação `CLAUDE.md`/`review.md` como o novo trabalho de engenharia) e [[wiki/entities/lucas-montano]] (Quality Gate com baseline) — sob a metáfora de "cultivar um ambiente que produz código bom" (fazenda industrial vs. jardim), e fecha com ceticismo sobre o hype: nenhuma empresa multibilionária foi construída puramente por IA ainda.

## Key Claims

1. **Fable 5 e similares (GPT 5.6 Sol, Química 3) já são melhores que a maioria dos engenheiros na relação qualidade × velocidade** — entregam mais feature, mais rápido, com qualidade adequada; um humano talvez entregue com mais cuidado, mas muito mais devagar. Ver [[wiki/entities/anthropic|Fable (Anthropic)]] e [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]].
2. **O volume de código gerado é a causa mecânica de "ninguém mais revisar"** — não é preguiça nem descuido; é que a quantidade de código excede a capacidade humana de revisão linha a linha, então merges passam sem revisão. Mesma tese de volume registrada em [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] (~10.000 linhas/dia).
3. **Revisar 100% do código continua racional quando o risco é financeiro/multimilionário** — o autor relata que numa empresa de pagamentos ("quem tem alguma coisa tem medo") revisavam todo o código do core business, porque o valor entregue era robustez, não volume de features. Isso não generaliza para a maioria dos casos.
4. **As métricas de Uncle Bob são valiosas porque são objetivas, mas não são suficientes** — cobertura, [[wiki/concepts/teste-de-mutacao|mutation testing]], [[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]], tamanho de módulo e estrutura de dependências dão um *resultado binário* mensurável e, a partir deles, se *infere* qualidade — mas métrica verde não garante código bom; dá só uma probabilidade. Ler o código continua sendo a prova real.
5. **Metáfora organizadora: de jardim para fazenda industrial** — antes se cuidava planta por planta (ler cada linha); agora se mede solo/ar/adubo (as métricas objetivas) e se colhe com trator. A mentalidade a adotar é "cultivar um ambiente em que código bom é a única possibilidade", não "escrever código bom".
6. **A cadeia lógica que justifica documentação: se você sabe explicar por que o código está ruim, você sabe escrever essa explicação — e escrevê-la num `CLAUDE.md`/`review.md`** — é isso que [[wiki/entities/boris]] (criador do Claude Code) argumenta: todo time deveria escrever `CLAUDE.md`, `review.md`, skills e docs que permitam agentes trabalharem produtivamente com zero contexto adicional.
7. **Automação ficou barata, então definir regras/padrões/docs vira parte central do trabalho de engenharia** — Boris: os melhores engenheiros sempre automatizaram processos repetíveis (lint, CI, rotinas); agora análise de dependências, complexidade ciclomática e limites entre serviços se tornam trabalho de primeira classe.
8. **Ninguém é expert em controle de qualidade de código gerado por IA** — expertise leva anos, e o fenômeno é de 2026; existem experts em qualidade de código *ou* em criar IA, mas quase ninguém uniu as duas coisas por muitos anos. O autor pede humildade explícita sobre suas próprias conclusões.
9. **O Quality Gate de [[wiki/entities/lucas-montano]] usa baselines e um agente em babysitting** — mede o estado atual como [[wiki/concepts/ratchet-baseline|baseline]], coloca a IA em loop corrigindo, e só permite merge se o PR cumprir pré-requisitos objetivos; pode usar um revisor de IA que lê o `CLAUDE.md`/`review.md` do projeto como input. Mesma prática documentada em [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]].
10. **[[wiki/entities/paulo-tarso]] (brasileiro, artigo bilíngue) detalha tecnicamente como implementar as métricas** — cobertura, complexidade ciclomática, tamanho de módulos, mutation testing; explicitamente derivado do tweet de Uncle Bob, mas é evidência de gente colocando em prática.
11. **Nada disso é novo: é engenharia de software, descrita em *Extreme Programming* (~1999–2001)** — 25 anos depois, esses conceitos ressurgem porque produzir código ficou barato/rápido/fácil, e o gargalo migrou para a garantia de qualidade.
12. **Matriz de transição risco × dificuldade** (contribuição central da fonte, ver [[wiki/concepts/matriz-risco-dificuldade-review-ia]]):
    - **Baixo risco + baixa dificuldade** → merge automático sem ler o código, *desde que* exista teste garantindo os fluxos que o código toca.
    - **Risco médio + complexidade média** → amostragem (sampling): olhar principalmente testes e docs (que dizem a intenção), mais trechos do código, e usar o que se encontra para melhorar o `CLAUDE.md`/`review.md`.
    - **Alto risco** (autenticação, autorização, pagamentos, senhas, migração de banco, infra, permissões) → revisão manual em pares. A maioria das empresas ainda não tem maturidade de ferramental para abrir mão disso.
13. **Guideline de transição: erre quando o erro é pequeno** — não adotar merge sem review na empresa inteira de um dia pro outro; começar pelo canto de baixo risco e avançar aos poucos. "Quem tem coisa tem medo, e você deve ter medo — isso é bom."
14. **Ceticismo com o hype** — o autor ainda não viu nenhuma empresa multibilionária construída só com Fable rodando milhões de agentes em paralelo. Se isso fosse equivalente a milhões de devs por 10 anos, "cadê o Figma 2, o Photoshop 2?" — logo, calma.

## Entidades Mencionadas

- [[wiki/entities/augusto-galego]] — autor (voz "Galego"); relato próprio de empresa de pagamentos revisando 100% do código.
- [[wiki/entities/uncle-bob]] — post que origina os três vídeos de reação; lista de métricas objetivas.
- [[wiki/entities/boris]] — criador do Claude Code; argumento de `CLAUDE.md`/`review.md`/skills/docs como o novo trabalho de engenharia (nova entidade).
- [[wiki/entities/lucas-montano]] — Quality Gate com baseline e babysitting por agente.
- [[wiki/entities/paulo-tarso]] — artigo bilíngue detalhando implementação das métricas (nova entidade).
- [[wiki/entities/abacus-ai]] — patrocinador; Custom Router para rotear entre Fable/GPT 5.6 Sol/Gemini 3.5/Química.
- [[wiki/entities/anthropic]] — preferência por `AGENTS.md` sobre `CLAUDE.md` mencionada de passagem; Boris é da Anthropic.

## Conceitos Tocados

- [[wiki/concepts/matriz-risco-dificuldade-review-ia]] (novo)
- [[wiki/concepts/code-review]]
- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/harness-de-qualidade]]
- [[wiki/concepts/claude-md]]
- [[wiki/concepts/ratchet-baseline]]
- [[wiki/concepts/teste-de-mutacao]]
- [[wiki/concepts/complexidade-ciclomatica]]

## Open Questions

- A fonte não linka o tweet original de Uncle Bob nem o artigo de Paulo Tarso, nem cita o handle/URL de "Boris" (referido só como "criador do Claude Code") — mesma cautela de atribuição já registrada em [[wiki/entities/uncle-bob]]. Tratar nomes e citações como aproximações do áudio, não como citação verificada.
- O número "300 milhões de agentes em paralelo" e o enquadramento "milhões de devs por 10 anos" são retóricos, não medidos — servem ao argumento cético, não como estimativa.
- A afirmação de que Fable/Sol/Química "já são melhores que a maioria dos engenheiros" é assertiva de opinião do autor, sem benchmark citado nesta fonte (contraste com os dados de SWE-bench citados em [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]]).

## Citações Cruas

> "I read the code. Eu leio o código."

> "A gente não vê código como um jardinzinho olhando planta por planta; a gente vê como uma fazenda industrial — mede solo, ar, adubo, e colhe com trator."

> "Eu estou cultivando um ambiente que vai produzir código bom — é diferente de eu produzir código bom."

> "Quem tem alguma coisa tem medo. Você deve ter medo. Isso é bom."

> "Cadê o Figma 2? Cadê o Photoshop 2? Cadê a empresa multibilionária inteiramente construída em cima de IA? Ela não está aqui hoje. E se não está, vamos com calma."
