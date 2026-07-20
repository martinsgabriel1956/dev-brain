---
type: source
title: "Under-Engineering vs Over-Engineering — Mário Souto (DevSoutinho)"
aliases: ["under vs over engineering mario souto", "a arte de fazer menos ou mais do que deveria"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 0
tags: [under-engineering, over-engineering, yagni, acoplamento, hardcode, code-review, ci-cd, tech-debt, secrets-management, build-vs-buy]
skill: tech-mentor-leadership
source_file: /home/nemomartins/Documentos/new/dev-study/raw/underengineering-overengineering-mario-souto.md
source_url: ""
author: "Mário Souto"
date_published: ""
date_ingested: "2026-07-19"
status: stable
---

# Under-Engineering vs Over-Engineering — Mário Souto (DevSoutinho)

## TL;DR

Vídeo de Mário Souto (canal DevSoutinho) usando um tweet/card como ponto de partida para discutir sinais de over-engineering e de under-engineering. Argumenta que under-engineering — fazer menos do que o projeto exige — é o problema mais comum no dia a dia, mais do que over-engineering. Percorre exemplos concretos e pessoais: não reinventar bibliotecas maduras (formulário, CSS), não hardcodar configuração, evitar acoplamento entre responsabilidades (login vs. criação de conta), e usar CI (lint + teste via GitHub Actions, com branch protection) como rede de segurança mínima. Fecha oferecendo o próprio repositório como referência de setup copiável.

---

## Reivindicações Principais

**Claim:** Under-engineering é mais comum na indústria do que over-engineering.
**Evidência:** Opinião pessoal do autor, sem dado quantitativo.
**Confiança:** Média — esta é a mesma tese já registrada em [[wiki/concepts/over-engineering]] a partir de [[wiki/sources/como-evitar-over-engineering-david-farley]] (David Farley). Este vídeo é uma segunda fonte, independente, chegando à mesma conclusão — reforça a tese por convergência, mas ambas seguem sendo opinião de praticante, não estudo controlado.

**Claim:** Ao construir algo bem resolvido por bibliotecas maduras (ex.: gerenciamento de formulário, suporte a navegador/polyfill, CSS), a recomendação prática é usar uma lib documentada e mantida por terceiros (React Hook Form, Formik, Tailwind CSS) em vez de implementar do zero — mesmo em casos aparentemente simples ("é só um formulário").
**Evidência:** Argumento do autor com exemplo hipotético (formulário de trabalho) e comparação com [[wiki/entities/react|React]] + React Hook Form.
**Confiança:** Alta como heurística prática — consistente com o espírito de [[wiki/concepts/yagni]] (não construa infraestrutura que já existe pronta e testada) e já registrado de forma equivalente em [[wiki/entities/react]] (tabela de ecossistema lista "Formulários → React Hook Form + Zod").

**Claim:** Um tweet/card (fonte não identificada) lista sinais de over-engineering — uso prematuro de microsserviços e micro-frontends, ignorar YAGNI, otimização prematura, apresentações excessivas, especulação de features, 100% de cobertura de teste — e sinais de under-engineering — tight coupling, hardcode, ausência de checks automatizados e validação de erros, copy-paste sem estrutura, falta de flexibilidade.
**Evidência:** Card mostrado em tela durante o vídeo, não capturado em texto pela transcrição em áudio; vários termos do card ficaram ilegíveis/garbled na transcrição automática (ex.: possíveis menções a suporte de navegador e boilerplate não identificadas com segurança).
**Confiança:** Baixa quanto à autoria e à redação exata do card (fonte primária não verificada, [external] não confirmado); média-alta quanto à categorização geral, que é consistente com listas similares comuns na indústria e com o que já está documentado em [[wiki/concepts/over-engineering]] (sintomas) e agora em [[wiki/concepts/under-engineering]].

**Claim:** Usar plataformas hospedadas (Vercel para deploy/rollback em time, Supabase como banco de dados gerenciado) é mais barato, em tempo e risco, do que montar a mesma infraestrutura na mão — mesmo pagando por elas (~$20/mês citado para o plano em time da Vercel).
**Evidência:** Anedota pessoal do autor sobre seu próprio projeto.
**Confiança:** Alta como relato de experiência direta; não generalizável sem considerar trade-offs de vendor lock-in (não discutidos na fonte).

**Claim:** Um pipeline mínimo de CI (lint + teste automatizado, ~31 linhas de YAML no GitHub Actions) configurado como *required status check* via regra de proteção de branch é suficiente para destravar boa parte dos sintomas de under-engineering listados (ausência de checks automatizados, validação de erros).
**Evidência:** Demonstração direta do próprio repositório do autor durante o vídeo (não visível na transcrição em áudio, apenas descrita verbalmente).
**Confiança:** Alta quanto ao padrão geral (workflow de lint + teste + branch protection exigindo status check é prática padrão de mercado); a contagem exata de linhas (31) não foi verificada de forma independente.

**Claim:** Acoplamento (ex.: lógica de login e de criação de conta no mesmo arquivo) é um sinal de under-engineering que se resolve com separação de responsabilidades, mas essa separação é "um pouco filosófica" e se desenvolve com prática, não com regra fixa.
**Evidência:** Exemplo do próprio código do autor.
**Confiança:** Média-alta — coerente com [[wiki/concepts/acoplamento]], mas o próprio autor reconhece que não aplicou a separação até o fim no exemplo mostrado (ficou registrado como debt consciente, não como solução implementada).

**Claim:** "Mais rápido" é relativo — um atalho (hardcode, código copiado, acoplamento) é mais rápido apenas no momento em que é feito; o custo aparece depois, o que caracteriza débito técnico.
**Evidência:** Argumento qualitativo do autor.
**Confiança:** Alta como formulação — consistente com o Quadrante de Fowler já documentado em [[wiki/concepts/tech-debt-como-ferramenta]] (débito Prudente vs. Imprudente).

## Identificação do autor/canal — nota de transcrição

O nome do canal, dito na abertura do vídeo, foi transcrito automaticamente como "canal da Absolut" — foneticamente próximo, mas provavelmente uma transcrição incorreta de "canal do Soutinho" (apelido usado pelo autor para o canal **DevSoutinho**). Essa hipótese é reforçada pelo fato de, mais adiante na mesma transcrição, o nome do projeto pessoal do autor aparecer como "DevSoltinho" — quase certamente o mesmo "DevSoutinho" (erro de reconhecimento de fala "Sou" → "Sol"). **[external]** Busca na web confirma Mário Souto como Staff Software Engineer (à época da ingestão, na Nubank), Google Developer Expert, GitHub Star e Microsoft MVP, dono do canal **DevSoutinho** no YouTube, com histórico de produção de conteúdo educacional em parceria com o Grupo Alura — o que também explica a semelhança fonética "canal da Absolut" / "canal d'Alura" como hipótese alternativa não descartável. Não é possível, a partir apenas do áudio transcrito, decidir com certeza entre as duas hipóteses; fica registrado como questão em aberto abaixo. `raw/` não foi alterado — a correção fica registrada aqui.

---

## Conceitos Abordados

- [[wiki/concepts/under-engineering]] — tema central do vídeo, página criada nesta ingestão
- [[wiki/concepts/over-engineering]] — contraponto discutido a partir do mesmo card/tweet
- [[wiki/concepts/yagni]] — citado explicitamente como um dos sinais de over-engineering quando ignorado ("ignorar regra do YAGNI")
- [[wiki/concepts/acoplamento]] — exemplo de login vs. criação de conta no mesmo arquivo
- [[wiki/concepts/code-review]] — cultura de review, tipos genéricos (`any`) vs. tipos específicos/enum
- [[wiki/concepts/pipeline-de-qualidade]] — exemplo concreto de pipeline mínima (lint + teste) como GitHub Actions
- [[wiki/concepts/quality-gate]] — branch protection com required status checks como implementação concreta de gate
- [[wiki/concepts/tech-debt-como-ferramenta]] — "mais rápido é relativo" como formulação do custo futuro do atalho
- [[wiki/concepts/secrets-management]] — configuração via variável de ambiente na Vercel em vez de hardcode, incluindo chave de API de terceiro

## Entidades

- [[wiki/entities/mario-souto]] — autor, criado nesta ingestão
- [[wiki/entities/react]] — citado como exemplo de biblioteca madura (React Hook Form) preferível a implementação própria de formulário

## Questões em Aberto

- **Identidade exata do "canal" citado na abertura** — "canal do Soutinho" (DevSoutinho) vs. possível referência à Alura, dado o histórico do autor de produzir conteúdo com o Grupo Alura. Não resolvido com certeza a partir da transcrição em áudio.
- **Conteúdo exato do tweet/card usado como base do vídeo** — vários termos citados na fala ficaram irreconhecíveis na transcrição automática (garbled), incluindo possíveis menções a suporte de navegador e boilerplate. Autoria do tweet não identificada. Vale revisitar se o vídeo original (ou o tweet) for encontrado com URL.
- **Contagem exata de linhas do workflow de CI (31 linhas) e nome do repositório** — mencionados verbalmente, não confirmados em texto/código nesta transcrição.
- Nem todo o card foi corretamente entendido pela transcrição automática (ex.: um trecho sobre "beautiful scrate"/suporte a navegador ficou impreciso) — a interpretação registrada na wiki é a mais plausível dado o contexto, não uma transcrição literal confiável.

## Raw Quotes

> "Under [engineering]... basicamente a arte de fazer mais que você deveria ou de fazer menos do que você deveria e lidar com seu sofrimento todos os dias."

> "Eu diria para você usar alguma coisa que tenha documentação e que não seja você que criou."

> "O mais rápido ele é muito relativo. Ele é mais rápido no momento que você tá fazendo, porque pode ser que daqui três dias dê um problema e você vai pagar por esse mais rápido que você fez três dias atrás."

> "Qualidade é uma coisa que você pode ter no seu projeto sem você tá fazendo de menos ou fazendo de mais — você tem uma base, você tem um caminho mínimo para poder trabalhar."
