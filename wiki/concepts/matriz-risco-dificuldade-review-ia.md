---
type: concept
title: "Matriz Risco × Dificuldade para Revisão de Código de IA"
aliases: ["matriz risco dificuldade", "quando revisar código de IA", "migração review manual para automático", "sampling de code review", "merge automático por risco"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 1
tags: [code-review, quality-gate, agentes-ia, merge-automatico, risco, gestao-de-mudanca, era-agentica]
skill: tech-mentor-leadership
status: draft
---

# Matriz Risco × Dificuldade para Revisão de Código de IA

## TL;DR

Framework de **transição** — não de estado final — proposto em [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] para times que hoje revisam 100% do código e querem migrar gradualmente para deixar parte do código de IA passar sem revisão linha a linha. Em vez de um interruptor "revisa tudo" → "não revisa nada", classifica cada pull request por dois eixos objetivos — **risco** (impacto se der errado) e **dificuldade/complexidade** (probabilidade de a IA errar) — e aplica um regime de revisão diferente a cada quadrante. É a peça de *gestão de mudança* que complementa o [[wiki/concepts/harness-de-qualidade|harness de qualidade]] (as ferramentas) e o [[wiki/concepts/quality-gate|quality gate]] (o portão): decide *onde* confiar no harness primeiro.

## Os Três Regimes

| Risco | Dificuldade | Regime de revisão | Pré-condição |
|---|---|---|---|
| Baixo | Baixa | **Merge automático sem ler o código** | Existe teste garantindo os fluxos que o código toca. Sem o teste, não há merge automático. |
| Médio | Média | **Amostragem (sampling)** | Olhar principalmente testes e docs (dizem a intenção) + trechos do código; usar o que se encontra para melhorar o `CLAUDE.md`/`review.md`. |
| Alto | — | **Revisão manual em pares** | Sempre. Autenticação, autorização, pagamentos, senhas, migração de banco, infra, permissões. |

### 1. Baixo risco + baixa dificuldade → merge automático

Alta probabilidade de a IA acertar (baixa dificuldade) e, se errar, o dano é pequeno (baixo risco). É o primeiro tipo de PR a permitir merge sem revisão humana do código — **desde que** haja um teste garantindo que os fluxos com os quais o código interage continuam funcionando. Sem esse teste, o merge automático está fora de questão. Esse pré-requisito é o que liga a matriz ao harness: o teste é a prova objetiva que substitui o olho humano.

### 2. Risco médio + complexidade média → amostragem

Aqui não se lê tudo nem se ignora tudo — pega-se **amostras**. A fonte recomenda olhar **principalmente testes e documentação**, porque teste e doc expressam a *intenção*, e a IA segue a intenção quase à risca (com erros pontuais). Além disso, olhar trechos do código e usar o que se encontra como *feedback para o processo*: melhorar o `CLAUDE.md`/`review.md` para que o próximo lote de PRs já venha melhor. É sampling estatístico aplicado a review, com efeito de mão dupla — encontra defeitos e calibra o [[wiki/concepts/harness-de-qualidade|harness]].

### 3. Alto risco → revisão manual em pares, sempre

Independente da dificuldade. Mudanças de alto risco — autenticação, autorização, pagamentos, senhas, migração de banco de dados, mudanças de infraestrutura, permissões — são revisadas manualmente, em pares ou mais pessoas. A justificativa não é filosófica: a maioria das empresas ainda **não tem a maturidade de ferramental** (não de "ser adulto", mas de sofisticação do harness) para abrir mão da revisão humana onde o custo do erro é catastrófico. Coincide com o relato da própria fonte sobre a empresa de pagamentos que revisava 100% do core business (ver [[wiki/entities/augusto-galego]]).

## Princípio de Fundo: erre quando o erro é pequeno

A matriz existe para operacionalizar uma regra de gestão de risco: **a melhor forma de errar é errar quando o erro é pequeno e inconsequente.** Por isso a adoção começa pelo quadrante baixo/baixo e avança conforme a confiança no harness cresce — nunca "a empresa inteira de um dia pro outro". Ecoa a categorização incremental descrita em [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] (marcar uma *categoria* de mudança como confiável só depois de ~30 PRs com pouco feedback), aplicada agora sobre os eixos risco/dificuldade em vez de categoria funcional.

## Relação com Outras Páginas

- É a camada de *decisão humana* acima do [[wiki/concepts/quality-gate|quality gate]] (o portão automático) e do [[wiki/concepts/harness-de-qualidade|harness]] (as ferramentas). O gate diz "passou/não passou"; a matriz diz "para este PR, o gate verde é suficiente, ou ainda preciso ler?".
- O regime de amostragem usa o [[wiki/concepts/claude-md|CLAUDE.md / review.md]] como destino do aprendizado — cada defeito amostrado vira regra escrita, não correção pontual.
- Complementa o [[wiki/concepts/code-review]] tradicional: não o substitui, mas define quando ele deixa de ser obrigatório por PR.

## Key Sources

- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — origem da matriz risco × dificuldade e dos três regimes (merge automático / amostragem / revisão manual em pares)
