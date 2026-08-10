---
type: concept
title: "Governança de Código Gerado por IA"
aliases: ["paradoxo da ia no codigo", "governar codigo de ia"]
date_created: 2026-07-03
date_updated: 2026-08-06
source_count: 6
tags: [ia-no-processo-de-engenharia, arquitetura, carreira]
skill: tech-mentor-leadership
status: draft
---

# Governança de Código Gerado por IA

Paradoxo: quanto mais a IA gera código automaticamente, mais uma organização precisa de [[wiki/concepts/engenheiro-vs-programador|engenheiros]] capazes de julgar, revisar e assumir responsabilidade por esse código — não menos.

## O argumento

Ferramentas como Copilot, Cursor e Claude já escrevem código funcional a partir de uma descrição, e tendem a melhorar. Isso comoditiza a tarefa clássica do programador: transformar requisito claro em código funcional. Mas o trabalho do engenheiro — entender se o requisito faz sentido, decidir arquitetura, avaliar trade-offs, governar a complexidade do sistema como um todo — exige contexto, julgamento sobre incerteza e responsabilidade sobre consequências. A IA não faz isso.

> "Sem governança, a IA gerando código é como dar uma metralhadora para quem não sabe mirar."

## Quem perde o emprego, quem não perde

A IA ameaça quem permanece só na camada de execução e não evolui para julgamento e governança. Cria mais demanda por quem pensa, decide e governa o sistema. O autor não trata isso como verdade universal — depende da linguagem, de quão legado é o projeto, e de quão bem a IA já resolve aquele tipo de tarefa especificamente.

## Relação com outros conceitos

- [[wiki/concepts/engenheiro-vs-programador]] — a distinção de mentalidade que determina de que lado desse paradoxo alguém fica
- [[wiki/concepts/complexidade-acidental]] — código gerado sem revisão arquitetural tende a acumular complexidade acidental em volume maior e mais rápido do que código escrito manualmente
- [[wiki/concepts/pensamento-em-producao]] — código gerado ainda precisa sobreviver a produção; a IA não assume esse risco
- [[wiki/concepts/divida-cognitiva]] — falta de governança é o mecanismo pelo qual código gerado vira dívida cognitiva coletiva

## Quando quem gera o ticket não é técnico

[[wiki/sources/atrofia-cognitiva-ia-programacao]] descreve uma falha de governança mais severa que um dev usar IA para resolver seu próprio ticket: alguém **fora do time técnico** conectando o repositório do projeto a uma IA e gerando tickets com detalhamento técnico no backlog — sem nenhum engenheiro tendo formulado ou revisado o problema antes de virar tarefa. Isso quebra a premissa central da governança de código gerado por IA: não há humano exercendo julgamento em nenhum ponto do fluxo, nem na geração do requisito nem na geração do código.

## Vender Vibe Coding Como Produção é Falta de Governança

[[wiki/sources/vibe-coding-limites-maturidade-profissional]] descreve outro caso limite: construir um sistema inteiramente por [[wiki/concepts/vibe-coding|vibe coding]] e vendê-lo como pronto para produção — seguro, moderno, testado — sem nenhuma revisão arquitetural, de segurança ou de contexto de negócio. Isso é falta de governança na ponta de saída (venda ao cliente), não só na ponta de entrada (geração do requisito): o risco recai sobre quem comprou confiando na promessa de qualidade.

## Substituir Software Determinístico pela IA é a Ausência Mais Estrutural de Governança

[[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] descreve uma variante distinta dos casos limite já registrados nesta página: não é falta de revisão humana sobre código gerado, é usar a IA para substituir a própria camada de decisão/registro que um sistema determinístico deveria ter. O autor tentou trocar scripts de validação (software tradicional, regra fixa) por julgamento de LLM — e a "governança" que faltou não foi revisão de PR, foi a decisão arquitetural de manter a IA como camada de interpretação e deixar o processamento lógico com o software tradicional. Argumento central da fonte: a IA torna mais evidente, não menos, a importância de quem sabe construir sistemas previsíveis — o oposto da narrativa de que a IA substitui o engenheiro.

## Paralelismo Multiplica o Risco de "Gambiarra", Não Só o Ganho de Produtividade

[[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] aplica o mesmo paradoxo ao contexto específico de paralelismo via [[wiki/concepts/worktree-paralelismo|worktree]]: a mesma capacidade que permite rodar três bug fixes e uma feature em paralelo, cada um numa instância separada de agente, é capacidade de gerar mais código ruim mais rápido — "garbage in, garbage out". O antídoto apontado pela fonte é o mesmo já documentado nesta página como pré-requisito estrutural: documentação boa e regras de negócio bem definidas antes de multiplicar agentes, não depois.

## Dados Concretos: Segurança Degrada com Iteração, Não Só com Falta de Revisão

[[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] traz o contraponto quantitativo mais forte já registrado nesta página: não é só que código gerado por IA nasce mais vulnerável (~2,77x mais falhas de segurança que código humano, segundo CodeRabbit e Veracode) — pedir para a IA **refinar** o próprio código repetidamente piora a segurança, não melhora. Um paper testando 400 amostras ao longo de 40 rodadas de refinamento mediu 37,6% de aumento em vulnerabilidades críticas depois de apenas 5 iterações, mesmo com um prompt pedindo explicitamente foco em segurança a cada rodada. Isso reforça o argumento central desta página de outro ângulo: a ausência de governança não é só "ninguém revisou o código gerado" — é que o próprio ato de iterar sem checkpoints de revisão introduz risco continuamente, mesmo quando alguém está "melhorando" o código de boa fé. Ver [[wiki/concepts/degradacao-de-seguranca-iterativa-ia]] para o mecanismo detalhado e a mitigação de processo proposta (SAST no delta, limite de iterações, testes de segurança como contrato prévio).

## Key Sources

- [[wiki/sources/engenheiro-vs-programador-mercado-ia]]
- [[wiki/sources/codigo-gerado-por-ia-mais-falhas-seguranca-degradacao-iterativa]] — dados quantitativos de degradação de segurança em refinamento iterativo com IA
- [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] — caso de governança arquitetural: IA substituindo a camada de decisão determinística em vez de apenas interpretar
- [[wiki/sources/atrofia-cognitiva-ia-programacao]] — caso limite: pessoa não técnica gerando tickets via IA conectada ao repositório, sem nenhum julgamento de engenharia no fluxo
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — caso limite: vender sistema vibe-coded como pronto para produção sem revisão humana
- [[wiki/sources/git-worktree-paralelismo-ia-codex-claude-abacus]] — paralelismo via worktree multiplica tanto o ganho de produtividade quanto o risco de código mal fundamentado
