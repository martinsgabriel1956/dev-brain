---
type: concept
title: "Under-Engineering"
aliases: ["underengineering", "engenharia insuficiente", "fazer menos do que deveria"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 1
tags: [under-engineering, over-engineering, qualidade, anti-pattern, tech-debt, acoplamento, ci-cd]
skill: tech-mentor-leadership
status: draft
---

# Under-Engineering

Fazer menos do que o problema exige: pular estrutura, validação, testes ou automação que o projeto de fato precisa — o oposto de [[wiki/concepts/over-engineering]]. Segundo [[wiki/sources/underengineering-overengineering-mario-souto]] e, de forma independente, [[wiki/sources/como-evitar-over-engineering-david-farley]] (David Farley), under-engineering é o problema mais comum na indústria — mais do que over-engineering, que recebe mais atenção por ser mais visível e mais fácil de apontar como "exagero".

## Sinais (segundo o card discutido na fonte)

- **Tight coupling** — responsabilidades diferentes emaranhadas no mesmo módulo/arquivo. Ver [[wiki/concepts/acoplamento]].
- **Hardcode** — valores de configuração fixos no código em vez de externalizados. Ver [[wiki/concepts/secrets-management]].
- **Ausência de checks automatizados e de validação de erros** — nenhum gate impedindo que um problema óbvio chegue à produção. Ver [[wiki/concepts/quality-gate]] e [[wiki/concepts/pipeline-de-qualidade]].
- **Copy-paste sem estrutura** — duplicação de código sem extrair um ponto único de mudança.
- **Falta de flexibilidade suficiente** — o código atende exatamente o caso de hoje e quebra ao primeiro desvio pequeno.

## Por que é mais comum do que over-engineering

Um projeto não precisa ser "grande" ou "complexo" para sofrer de under-engineering. O exemplo central da fonte é um formulário simples, feito na mão, sem lib de terceiros, sem CI, sem variável de ambiente: parece pequeno demais para justificar disciplina de engenharia, mas é exatamente aí que os sintomas acima aparecem — porque ninguém "sente falta" de estrutura até que outra pessoa mexa no código sem avisar, ou até que algo quebre em produção e não haja como reverter rápido.

Isso conecta com a observação já registrada em [[wiki/concepts/over-engineering]] de que o "triângulo de ferro" (rápido, barato, bom — escolha dois) é um mito: a disciplina mínima que evita under-engineering (usar libs testadas, CI com lint e teste, variáveis de ambiente, deploy reversível) não torna a entrega mais lenta — ela é o que permite entregar rápido *e* com segurança de reverter quando algo dá errado.

## Antídotos concretos (exemplos da fonte)

| Sintoma | Antídoto | Exemplo da fonte |
|---|---|---|
| Reinventar algo já resolvido | Usar lib madura e documentada | React Hook Form/Formik em vez de gerenciamento de formulário na mão |
| Sem suporte a ambiente/navegador | Usar framework/metaframework com isso embutido | Next.js em vez de build próprio sem polyfill |
| Hardcode de configuração | Variáveis de ambiente, configuráveis sem redeploy manual | Chave de API e valores públicos configurados na Vercel |
| Sem rede de segurança de deploy | Plataforma gerenciada com rollback | Vercel (redeploy de build anterior por qualquer pessoa do time) |
| Sem check automatizado no PR | CI mínimo (lint + teste) como required status check | Workflow de ~31 linhas de GitHub Actions + branch protection |
| Acoplamento entre responsabilidades | Separar por responsabilidade, mesmo que aos poucos | Login vs. criação de conta em arquivos diferentes |

Nenhum desses antídotos exige over-engineering — nenhum é microsserviço, é abstração especulativa ou é 100% de cobertura de teste. É o "caminho mínimo" citado na fonte: nem de menos, nem de mais.

## Relação com Tech Debt

O atalho que gera under-engineering (não configurar CI, hardcodar um valor "só dessa vez", colar código sem extrair) é, na prática, a forma mais silenciosa de tomar débito técnico — sem a decisão consciente que caracteriza débito Prudente do [[wiki/concepts/tech-debt-como-ferramenta|Quadrante de Fowler]]. Ver a citação da fonte: "o mais rápido é muito relativo... você vai pagar por esse mais rápido que você fez três dias atrás."

## Relacionado

- [[wiki/concepts/over-engineering]] — extremo oposto, mesmo card/tweet como origem da lista de sintomas nesta fonte
- [[wiki/concepts/yagni]] — princípio que, quando ignorado, é listado como sinal de over-engineering; under-engineering é o erro de julgamento na direção contrária
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/secrets-management]]
- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/tech-debt-como-ferramenta]]

## Key Sources

- [[wiki/sources/underengineering-overengineering-mario-souto]]
