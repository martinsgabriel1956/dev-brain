---
type: concept
title: "Harness de Qualidade"
aliases: ["quality harness", "harness ia", "ferramental de qualidade"]
date_created: 2026-05-31
date_updated: 2026-08-11
source_count: 6
tags: [harness, qualidade, pipeline-de-qualidade, tdd, testes, era-agentica, robustez]
skill: tech-mentor-backend
status: stable
---

# Harness de Qualidade

## TL;DR

Conjunto de ferramentas e configurações que envolvem a IA para garantir que o código gerado segue padrões de qualidade — de forma **determinística**, não dependente do julgamento do modelo. É o que transforma a IA de gerador de código potencialmente frágil em amplificador de boas práticas. O diferencial do dev na [[era-agentica]].

## O Problema que Resolve

A IA entrega o que você pediu. Se você pediu apenas "faça um login", ela faz — sem segurança, sem testes, sem considerar N+1, sem pensar em concorrência.

> *"Você não pode confiar tanto nela. Você tem que forçar através de tooling."*

A IA segue **regras impostas por ferramenta** mais consistentemente do que regras pedidas no prompt. Com janela de contexto crescendo, as instruções do início da conversa ficam "perdidas no contexto". Ferramentas não esquecem.

## Componentes do Harness

### TDD obrigatório
Mandar a IA fazer [[tdd]] — o ciclo test-first força código que passa em testes antes de ser aceito. Resultado mais previsível e com menos bugs estruturais. Instrução crítica que precisa acompanhar isso: proibir a IA de deletar ou enfraquecer testes que falham em vez de corrigir o código — ver [[gaming-de-testes-por-ia]].

### Spec-Driven Development obrigatório
Da mesma forma que TDD, [[spec-driven-development]] pode ser imposto: contrato de API (OpenAPI/Swagger, `.proto`, schema GraphQL) definido antes da IA implementar qualquer lado da boundary.

### Linters com regras de código
Configurar linters (ESLint, Biome, etc.) com regras específicas do projeto. A IA vai seguir o que o linter rejeitar — não o que você pediu no prompt.

### [[wiki/concepts/complexidade-ciclomatica|Complexidade ciclomática]]
Ferramentas que medem complexidade ciclomática na pipeline. Feedback objetivo: se a função está complexa demais, não commita.

### Análise estática de segurança
Ferramentas como Semgrep, Bandit, Snyk, CodeQL. Não confiar no julgamento da IA sobre segurança — usar ferramenta determinística.

### Code coverage elevado + [[teste-de-mutacao]]
Coverage alto é mais fácil do que nunca com IA gerando testes. Mutation testing valida que os testes realmente testam comportamento — não apenas executam sem quebrar.

### Testes end-to-end
E2E que testa os fluxos que importam para o negócio. Mais fácil criar o ferramental completo agora que a IA ajuda.

### Revisão automatizada de PR
Ferramentas de code review em PRs. O diferencial humano: saber o que o revisor de IA **não** pega — e adicionar isso nas instruções do revisor automático.

## O Ciclo

```
Harness configurado
    ↓
IA gera código
    ↓
Pipeline roda (linter → testes → coverage → mutation → segurança → E2E)
    ↓
Passa? → commita
Não passa? → IA recebe o erro e corrige
    ↓
Dev revisa o que a ferramenta não detecta (semântica, negócio, arquitetura)
```

O resultado é determinístico: **a ferramenta passou ou não passou** — independente do que a IA acha.

## Harness vs. CLAUDE.md / Skills

`CLAUDE.md` e skills instruem a IA em linguagem natural — ela tenta seguir mas pode esquecer com contexto grande. O harness de qualidade é **executado pelo runtime**, não pelo modelo. É a diferença entre [[hooks-agente|hooks]] e diretrizes no Claude Code: hooks são garantidos.

## Relação com [[robustez-de-sistemas]]

Harness de qualidade é o mecanismo que constrói [[robustez-de-sistemas]] quando a IA está gerando o código. Sem harness, velocidade de geração = velocidade de acumulação de débito técnico.

## O que Acontece Sem Harness: Substituir o Gate Inteiro pela IA

[[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] é o exemplo negativo desta página: em vez de usar a IA *dentro* de um harness determinístico, o autor tentou usar a IA *como* o próprio mecanismo de validação — sem pipeline, sem regra fixa, só o julgamento do modelo sobre o código do aluno. O resultado foi exatamente o previsto por esta página: sem ferramenta determinística ao redor, o comportamento da IA ficou inconsistente entre execuções e entre modelos. Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]].

## O Harness de Uncle Bob Como "Harness Puro": Cinco Peças, Cinco Erros Diferentes

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] descreve o post de [[wiki/entities/uncle-bob]] sobre não ler mais código de agentes como um exemplo direto desta página: a lista que ele cita (teste unitário, cobertura, [[wiki/concepts/teste-de-mutacao|mutation testing]], teste [[wiki/concepts/bdd|Gherkin/BDD]], métrica de qualidade) não é uma lista jogada — cada item pega um tipo de erro que os outros deixam passar. Teste unitário pega erro de lógica de negócio; cobertura pega o que nenhum teste tocou; mutation testing pega se o teste só valida o caminho feliz; Gherkin/BDD pega o pior erro de todos (construir a coisa errada, mesmo que construída certo); métrica de qualidade mostra a tendência do sistema (piorando/melhorando) ao longo do tempo. A fonte fecha com uma regra operacional que complementa esta página: não abandonar a leitura de código de uma vez, e sim por categoria de mudança, marcando cada categoria como confiável só depois de acumular um volume de PRs (~30, na estimativa da fonte) com pouco ou nenhum feedback a dar.

## Confiar no Harness é Gradual, Não Binário

[[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] enquadra o harness com a metáfora de **fazenda industrial vs. jardim**: em vez de cuidar planta por planta (ler cada linha), você mede solo/ar/adubo (as provas objetivas desta página) e cultiva "um ambiente em que código bom é a única possibilidade". Mas a fonte é explícita — como a seção "métrica boa não garante código bom" — que métrica verde dá probabilidade, não garantia. Por isso propõe migrar a confiança no harness **por quadrante de risco** (ver [[wiki/concepts/matriz-risco-dificuldade-review-ia]]), começando onde o erro é pequeno. [[wiki/entities/boris]] complementa: escrever `CLAUDE.md`/`review.md`/skills/docs é o novo trabalho de engenharia que torna o harness legível para os agentes, e automatizar isso ficou barato.

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — metáfora fazenda vs. jardim; confiança no harness migrada por quadrante de risco; docs como o novo trabalho de engenharia (Boris)
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/tdd-sdd-bdd-era-ia]]
- [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] — caso negativo: IA usada como o próprio gate, sem harness ao redor, resultado inconsistente
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — os cinco pilares do harness de Uncle Bob, cada um pegando um tipo de erro diferente; regra operacional de ler por categoria de mudança
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — quatro gates bloqueantes concretos (CCN, cobertura+mutation, tamanho de módulo, dependency structure) para os mesmos componentes já listados nesta página
