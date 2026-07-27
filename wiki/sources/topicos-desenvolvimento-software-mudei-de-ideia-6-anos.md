---
type: source
title: "Tópicos de desenvolvimento de software sobre os quais mudei de ideia após 6 anos na indústria"
aliases: ["thoughts after 6 years", "chris kiehl 6 anos", "mudei de ideia 6 anos"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 0
tags: [carreira, opiniao, arquitetura, kiss, yagni, dry, tipagem-estatica, microsservicos, monolito, code-review, entrevistas]
skill: tech-mentor-leadership
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/topicos-desenvolvimento-software-mudei-de-ideia-6-anos.md"
source_url: "https://chriskiehl.com/article/thoughts-after-6-years"
author: "Chris Kiehl"
date_published: 2021-01-23
date_ingested: 2026-07-27
---

## TL;DR

[[wiki/entities/chris-kiehl]] (autor do blog Blogomatano, também escreveu o livro *Data-Oriented Programming in Java*) lista, em formato de post curto, opiniões de engenharia de software que mudaram — e que não mudaram — depois de 6 anos de carreira. Divide em três blocos: (1) opiniões que se inverteram (linguagens tipadas > dinâmicas em times mistos, arquitetura importa mais que quase tudo, "boas práticas" são contextuais, design de sistemas escalável sem necessidade real é sinal de engenheiro ruim, DRY é meio e não fim, RDBMS > NoSQL por padrão); (2) opiniões adquiridas ao longo do caminho (ordem de prioridade **YAGNI, SOLID, DRY**; entrevistas técnicas estão "completamente quebradas"; ~90% dos PMs poderiam desaparecer sem perda de eficiência); (3) opiniões que permaneceram estáveis (cobertura de código não mede qualidade; monólitos são bons na maioria dos casos; microsserviços exigem justificativa).

## Key Claims

- **Tipagem estática ganha em time, não sozinho**: em times com níveis de experiência variados, linguagens tipadas ajudam mais do que quando o autor trabalhava sozinho ou com pares homogêneos — o tipo vira uma forma de comunicação e de contenção de erro entre pessoas com contextos diferentes. Relacionado a [[wiki/concepts/tipagem-com-jsdoc]] (tipagem forte sem TypeScript, mesmo espírito de "tipo como comunicação").
- **Arquitetura importa mais que quase tudo**: "uma implementação porca de uma boa abstração não causa dano líquido à base de código; uma abstração ruim ou uma camada faltando faz tudo apodrecer" — o dano de uma decisão arquitetural errada é estrutural e não se corrige com esforço de implementação. Ecoa diretamente [[wiki/concepts/arquitetura-de-software]] ("decisão arquitetural errada não se corrige com refatoração pontual").
- **"Boas práticas" são contextuais, não leis universais**: segui-las cegamente, sem avaliar o contexto, "faz de você um idiota" (linguagem do autor). Mesmo espírito do teste KISS já documentado em [[wiki/concepts/kiss]] ("qual requisito real justifica isso agora?").
- **Projetar para escala que não existe é sinal de mau engenheiro**: afirmação direta e sem ressalva, alinhada ao vínculo já registrado entre ignorar YAGNI e over-engineering em [[wiki/concepts/yagni]] e [[wiki/concepts/over-engineering]].
- **DRY é meio, não fim**: "DRY é sobre evitar um problema específico, não um objetivo em si mesmo" — closest reading é que duplicação acidental (coincidência) não deveria virar abstração só para "não repetir", distinção que a wiki ainda não tinha registrado explicitamente sobre DRY (diferente de KISS/YAGNI, que já têm páginas dedicadas).
- **Ordem de prioridade explícita — YAGNI, SOLID, DRY, nessa ordem**: primeiro decidir se algo deve existir (YAGNI), depois como estruturá-lo bem (SOLID), só depois eliminar repetição (DRY). Essa hierarquia é uma contribuição nova — nenhuma fonte anterior na wiki havia ordenado esses três princípios entre si.
- **RDBMS > NoSQL como padrão geral**: posição direta, sem elaboração de trade-off no texto original (post é uma lista curta, não um ensaio).
- **Entrevistas técnicas estão "completamente quebradas"**: depois de conduzir mais de 100 entrevistas como entrevistador, o autor afirma que o processo é falho e admite não ter solução — mesmo sintoma (processo de entrevista imperfeito), ângulo diferente do já coberto em [[wiki/sources/leetcode-como-se-preparar-entrevistas-coding-anthony-mays]] (que foca em como o candidato deveria se preparar, não em como o processo em si é falho do lado do entrevistador).
- **Cobertura de código ≠ qualidade de código**: opinião estável (não mudou em 6 anos) — alerta explícito contra usar % de cobertura como proxy de qualidade.
- **Monólitos são bons na maioria dos casos; microsserviços exigem justificativa**: reforça diretamente o argumento central de [[wiki/concepts/microsservicos]] de que monolito modular é o ponto de partida correto para a maioria dos casos, e que microsserviços só se justificam com necessidade real (escala diferente, time separado, deploy independente).
- **Lápis e papel como ferramenta de programação subutilizada**: opinião pessoal sem elaboração no texto — planejar fora do editor antes de codar.

## Entities

[[wiki/entities/chris-kiehl]]

## Concepts

[[wiki/concepts/kiss]] · [[wiki/concepts/yagni]] · [[wiki/concepts/arquitetura-de-software]] · [[wiki/concepts/microsservicos]] · [[wiki/concepts/over-engineering]] · [[wiki/concepts/code-review]]

## Open Questions

- A skill `tech-mentor-leadership` (referenciada em `/home/nemomartins/Documentos/new/skills/tech-mentor-leadership/SKILL.md` conforme as instruções do projeto) **não está acessível neste ambiente/máquina** — o caminho não existe no filesystem local. Este ingest foi feito sem carregar a skill; calibração de domínio, nomenclatura e taxonomia foi feita por analogia com fontes já ingeridas do mesmo domínio ([[wiki/sources/verdades-duras-programador-20-anos-pedro-nauck]]). Recomenda-se re-ingerir ou revisar esta fonte quando a skill estiver disponível — sinalizado também como candidato a `lint the wiki` (skill drift).
- O post é uma lista curta sem elaboração de trade-offs — várias afirmações (RDBMS > NoSQL, arquitetura > tudo) são categóricas no texto original, sem o raciocínio por trás. Se uma fonte futura do mesmo autor ou tema aprofundar algum desses pontos, vale expandir aqui.
- Nenhuma página existente na wiki cobre DRY como conceito dedicado (só aparece mencionado dentro de [[wiki/concepts/kiss]] e [[wiki/concepts/yagni]]) — esta fonte é a primeira a tratar DRY com uma claim própria ("meio, não fim"). Candidato a stub de `wiki/concepts/dry.md` se uma próxima fonte aprofundar o tema.

## Raw Quotes

*(Fonte traduzida do inglês para PT-BR em `raw/topicos-desenvolvimento-software-mudei-de-ideia-6-anos.md` — para o texto original, ver `source_url`.)*

> "A shitty implementation of a good abstraction causes no net harm to the code base. A bad abstraction or missing layer causes everything to rot."

> "So called 'best practices' are contextual and not broadly applicable. Blindly following them makes you an idiot."

> "DRY is about avoiding a specific problem, not an end goal unto itself."

> "YAGNI, SOLID, DRY. In that order."
