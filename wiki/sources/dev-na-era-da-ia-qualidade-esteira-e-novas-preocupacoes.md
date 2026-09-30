---
type: source
title: "O Dev na Era da IA: Tempo Ganho, Qualidade, Esteira e Novas Preocupações"
aliases: ["dev na era da ia esteira qualidade", "ia na esteira ci/cd determinístico", "retrospectiva de erros de ia", "migração não extinção do desenvolvedor"]
date_created: 2026-09-29
date_updated: 2026-09-29
source_count: 0
tags: [ia, llm, ci-cd, qualidade, determinismo, harness-engineering, retrospectiva, carreira, tech-mentor-testing]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/dev-na-era-da-ia-qualidade-esteira-e-novas-preocupacoes.md
source_url:
author: desconhecido (consultor que atende empresas grandes; continuação de vídeo anterior sobre o mercado e a IA)
date_published:
date_ingested: 2026-09-29
---

# O Dev na Era da IA: Tempo Ganho, Qualidade, Esteira e Novas Preocupações

## TL;DR

Vídeo PT-BR que responde "o que o dev deve encarar agora" a partir de uma tese: a IA **achatou o tempo de gerar código**, mas não necessariamente o **valor** do código ([[wiki/concepts/valor-do-codigo-com-tempo-achatado]]). O tempo ganho deve ser reinvestido no que sempre foi empurrado para frente por causa do time to market — testes, quality gate, CI/CD ([[wiki/concepts/tempo-ganho-com-ia-reinvestido-em-qualidade]]). Sobre IA na esteira, a regra é separar **gerar** a esteira com IA (bom) de **executar** a esteira dependendo de LLM (evitar: custo, lentidão, não determinismo); checagens de comportamento/drift de um produto que usa LLM rodam **periodicamente ou quando o prompt muda**, não a cada commit ([[wiki/concepts/ia-na-esteira-ci-cd]]). Levanta uma pergunta em aberto — como fazer a "retrospectiva de bugs" quando o autor do código é uma LLM ([[wiki/concepts/retrospectiva-de-erros-de-ia]]) — e fecha dizendo que é fase de **migração**, não de extinção, do desenvolvedor ([[wiki/concepts/novo-perfil-dev-ia]]).

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| O dev quase não coda mais, mas saber codar e debugar vale **mais** com IA, não menos | "quanto mais conhecimento você tem agora se torna mais valor" | Média (experiência de campo, sem dado) |
| O que caiu foi o **tempo** de geração de código; não está claro que o **valor** do código caiu na mesma proporção | "esse tempo ele esteja achatado, o valor do código eu não sei se ele se perdeu tanto assim" | Média (argumento, com ressalva do próprio autor: "tem cenários que eu acredito que sim") |
| Antes da IA, qualidade (cobertura de testes, quality gate, melhoria de CI/CD, refatoração) era empurrada porque o produto vinha primeiro, e acumulava até virar crise | "essas necessidades cresciam… se tornavam tão berrantes que isso virava uma crise" | Média (observação de consultoria) |
| Tempo ganho com IA deve ir para qualidade; a IA pode dar o *draft* de testes, mas bons casos de teste exigem conhecimento técnico **e de negócio**, em construção conjunta | "você pode delegar muita coisa para a IA, mas tem que ter uma pitada de conhecimento que é sua" | Alta (coerente com o restante da wiki) |
| Código gera ações **determinísticas**; LLM gera saídas **não determinísticas** — separar as duas preocupações | "código gera ações determinísticas… quando você trabalha com LLM ela gera um valor indeterminado" | Alta |
| Usar IA para **gerar** testes, quality gate e configuração de ferramentas (inclusive para aprender fazendo junto) é bom; a **execução** da esteira não deveria depender de LLM (custo de tokens e lentidão) | "a execução dele não tem que depender de uma LLM para você não ter um consumo de token em alta ou terminar mais lento" | Média (opinião; sem números) |
| Agente na esteira lendo log e apontando erro ao dev "ainda não é legal" | "plugar um agente toda vez que rodar a esteira… eu acho que isso ainda não é legal" | Baixa–média (opinião pessoal; contradiz práticas de "babysit"/review automatizada citadas em outras fontes — ver Contradições) |
| Para produto com LLM, verificações de comportamento/drift/segurança rodam **de tempos em tempos** (ex.: a cada 2 semanas) ou quando o **prompt muda**, desacopladas do disparo por commit | "não é cada commit, mas seja a cada duas semanas… ou quando tiver uma mudança de prompt" | Média (heurística; a cadência de 2 semanas é exemplo do autor) |
| Nem toda *skill* ajuda: algumas "deixam a LLM burra" ou fazem o Claude Code tomar decisões e mover conhecimento para onde não foi pedido; é preciso conter esse comportamento | "tem skill que tá me atrapalhando, tem skill que tá deixando a minha LLM burra" | Média (relato de uso, sem medição) |
| Falta uma cerimônia equivalente à retrospectiva de sprint para **dar feedback à IA** (padrão não seguido? regra de negócio desatualizada?) de modo que o erro não se repita | "como é que a gente dá de maneira eficiente feedback pra IA… para esses erros não serem repetidos" | Alta como problema; **sem solução na fonte** |
| Harness engineering dá uma visão parcial desse problema, mas as preocupações vão além | "o Harness dá uma visão para isso, mas há muito mais preocupações" | Média |
| É uma **migração/mudança de paradigma**, não extinção do dev; conhecimento *enterprise* sobre isso ainda não chegou aos cursos | "não é uma fase de extinção do desenvolvedor, é uma fase de migração" | Média (opinião; sem dado de mercado) |
| Mínimo a saber hoje: tool calling, MCP, bancos vetoriais, como funciona uma LLM e um RAG | lista dita no início | Média (lista curta, sem justificativa detalhada) |

## Pontos didáticos

- **Dois momentos da IA na esteira:** *construção* (IA gera testes, gates, YAML de pipeline — pode e deve) vs. *execução* (a cada build — deve ser determinística e barata). Ver [[wiki/concepts/ia-na-esteira-ci-cd]].
- **Dois tipos de esteira com LLM:** (1) esteira de um sistema comum → 100% determinística; (2) esteira de um produto que **chama** LLM → continua determinística no build, mais uma verificação **agendada / disparada por mudança de prompt** de comportamento e segurança.
- **Sprint retro clássica vs. retro com IA:** antes → "lições aprendidas" para o time; agora → a lição precisa virar **instrução/regra/skill/harness** que a IA de fato lê ([[wiki/concepts/retrospectiva-de-erros-de-ia]]).
- **Como usar IA para aprender:** fazer junto, passo a passo, perguntar cada termo desconhecido — não delegar o entendimento.

## Entidades Mencionadas

- [[wiki/entities/fred-brooks]] — citado ("o saudoso") como quem responde muito do que se vive hoje; a fala **não** especifica obra ou frase (provável *No Silver Bullet*, mas isso é inferência — ver Open Questions)
- [[wiki/entities/claude-code]] — usado como exemplo de ferramenta cujo comportamento é preciso conter
- GitHub — citado como exemplo de ferramenta que o dev talvez não domine e pode aprender junto com a IA ([[wiki/entities/github]])

## Conceitos Tocados

- [[wiki/concepts/valor-do-codigo-com-tempo-achatado]] (novo)
- [[wiki/concepts/tempo-ganho-com-ia-reinvestido-em-qualidade]] (novo)
- [[wiki/concepts/ia-na-esteira-ci-cd]] (novo)
- [[wiki/concepts/retrospectiva-de-erros-de-ia]] (novo)
- [[wiki/concepts/harness]]
- [[wiki/concepts/harness-de-qualidade]]
- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/ci-cd]]
- [[wiki/concepts/pipeline-de-ci]]
- [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]
- [[wiki/concepts/drift-detection]]
- [[wiki/concepts/llm-evals-testing]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/novo-perfil-dev-ia]]
- [[wiki/concepts/ia-como-amplificador]]
- [[wiki/concepts/closed-loop-skill-learning]]

## Contradições e imprecisões da fonte

- **Agente lendo log da esteira "não é legal" vs. wiki:** [[wiki/concepts/quality-gate]] e [[wiki/concepts/skills-agente]] documentam o padrão *babysit* (agente monitora o próprio PR/CI e corrige) e [[wiki/concepts/harness-de-qualidade]] lista revisão automatizada de PR como componente. A tensão é de **posição no fluxo**: babysit/review rodam *depois* do gate determinístico e sem bloquear o merge por julgamento da LLM; o autor rejeita LLM como **executor** do gate. Não é contradição factual — registrada como diferença de ênfase.
- **"Drift" no sentido de LLM:** aqui significa mudança de comportamento do modelo/prompt ao longo do tempo (behavior drift), não *infrastructure drift* de Terraform, que é o único uso hoje em [[wiki/concepts/drift-detection]]. Página atualizada para separar os dois sentidos.
- **"LRAP" na transcrição:** interpretado como RAG por contexto; não confirmável pelo áudio.
- **Frase de Fred Brooks:** a fonte não a cita; qualquer ligação com uma obra específica é inferência.
- **Sem dado empírico:** todas as afirmações (proporção de código gerado por LLM, custo de tokens, frequência ideal de 2 semanas) vêm da experiência do autor, sem métricas ou fontes.

## Open Questions

- **Como institucionalizar a retrospectiva com IA?** A fonte formula a pergunta mas não a responde. Caminhos plausíveis na wiki: regras/skills atualizadas após cada bug ([[wiki/concepts/closed-loop-skill-learning]], [[wiki/concepts/skills-agente]]), novos gates determinísticos ([[wiki/concepts/quality-gate]]), casos adicionados ao golden dataset de evals ([[wiki/concepts/llm-evals-testing]]) — ver [[wiki/concepts/retrospectiva-de-erros-de-ia]].
- **Qual a cadência certa** das verificações periódicas de comportamento de LLM? "A cada 2 semanas" é exemplo, não regra; depende de risco, custo e frequência de mudança de modelo/prompt.
- **Como medir** que uma skill está piorando o modelo em vez de ajudar? A fonte só relata a sensação; evals com/sem a skill seriam o caminho.
- **A qual obra de Fred Brooks** o autor se refere (se a alguma)?
- Quais problemas "muito além do harness" o autor tem em mente? Ficam sem enumeração ("é um começo").

## Raw Quotes

> "O código gera ações que são determinísticas; quando você trabalha com LLM ela gera um valor… coisas que são indeterminadas."

> "Você pode delegar muita coisa para a IA, mas tem que ter uma pitada de conhecimento que é sua."

> "A execução dele não tem que depender de uma LLM para você não ter um consumo de token em alta ou mesmo terminar mais lento."

> "Talvez esse disparo por exemplo não seja cada commit, mas seja a cada duas semanas… ou quando tiver uma mudança de prompt."

> "Como é que a gente dá de maneira eficiente feedback pra IA que tá gerando esse código para toda vez que você for gerar algo novo você não cair no mesmo erro?"

> "Isso não é uma fase de extinção do desenvolvedor, é uma fase de migração. Estamos passando por uma mudança de paradigma muito grande."
