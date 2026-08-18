---
type: concept
title: "Spec-Driven Development"
aliases: ["SDD", "spec driven", "desenvolvimento orientado a especificação", "planning-first"]
date_created: 2026-06-02
date_updated: 2026-08-18
source_count: 17
tags: [spec-driven, planejamento, ia-para-devs, harness, agente, qualidade, loop-engineering]
skill: tech-mentor-ai
status: stable
---

# Spec-Driven Development

Abordagem de desenvolvimento com IA em que **o planejamento e a especificação da tarefa ocorrem antes da execução**. O dev atua como "gerente" — define o quê e o porquê; a IA executa o como. É o que diferencia o nível L3 (gerente) do L2 (babysitting) na [[wiki/concepts/niveis-adocao-ia-l0-l4|escala de adoção]].

## Por Que é Necessário

No modelo tradicional (L2), o dev instrui a IA em micro-steps sucessivos: "cria o endpoint", "agora adiciona a validação", "agora persiste no banco". Isso:
- Maximiza o idle (esperando cada resposta)
- Impede paralelismo
- Gera contexto poluído de vai-e-vem
- Produz resultado inconsistente (sem visão do todo)

Com spec-driven, uma spec bem escrita é enviada de uma vez para execução autônoma. O dev pode paralelizar outras tarefas enquanto a execução corre.

## O Processo

### 1. Planejamento (Plan Mode)
Criar uma especificação estruturada da tarefa usando [[wiki/concepts/xml-markdown-prompts|XML+Markdown template]]. Iterar com o LLM para refinar:
- Requisitos funcionais
- Contratos de API
- Critérios de aceite
- Restrições (faça/nunca faça)
- Considerações de UI/UX
- Questões técnicas abertas

### 2. Limpeza de Contexto
Após o planejamento, fazer `/clear` para começar a execução com contexto limpo. O planejamento (240–400k tokens) fica registrado no arquivo de spec, não no contexto.

### 3. Execução
Enviar a spec ao agente em modo não assistido (YOLO). O agente usa as [[wiki/concepts/tool-call|tool calls]] do [[wiki/concepts/harness]] para ler o projeto, implementar e executar testes, sem intervenção do dev.

### 4. Revisão
Revisar o resultado final (PR level) + resultado prático (testes passando, comportamento correto), não linha a linha do código.

## Fluxo com Agentes Especializados

Para problemas complexos (múltiplos domínios, semanas de trabalho), o SDD usa agentes especializados com [[wiki/concepts/human-in-the-loop|human-in-the-loop]] em cada etapa:

```
Ideia → [Agente PRD] → PRD aprovado
     → [Agente Tech Spec] → Tech Spec aprovada
     → [Decomposição] → Lista de tarefas aprovada
     → [Execução isolada por tarefa] → [QA] → Done
```

- O [[wiki/concepts/agente-prd|Agente de PRD]] faz perguntas iterativas para refinar requisitos
- O agente de [[wiki/concepts/tech-spec|Tech Spec]] consome PRD + rules + análise do código
- Cada tarefa recebe PRD + Tech Spec + descrição isoladamente (não o projeto inteiro)
- Para projetos grandes: [[wiki/concepts/task-looper|task looper]] automatiza a execução das tarefas

> "PRD não é um documento feito para a empresa, é um documento feito para a IA." — [[wiki/entities/pedro-nauke]]

## Onde Ficam os Padrões de Arquitetura

Padrões globais (framework, linguagem, infraestrutura) ficam nas [[wiki/concepts/rules-agente|rules]], não no PRD ou Tech Spec. O PRD e a Tech Spec **referenciam** as rules, não as repetem.

## Quando Usar SDD

- Features novas complexas (múltiplos arquivos, múltiplos domínios)
- Refactoring de larga escala
- Migrações entre tecnologias ou versões
- Tarefas que normalmente levariam semanas de trabalho humano

Para tarefas menores, use [[wiki/concepts/plan-mode|Plan Mode]].

## Relação com Documentação

A spec não é uma "living documentation" permanente. É produzida para guiar uma execução e pode ser arquivada ou descartada após o merge. O código + testes + PR description documentam a decisão de forma mais duradoura.

## Ferramentas de Suporte

- **Compose** (Pedro Nauke): orquestrador spec-driven open source
- **Cairo**: harness com spec-driven nativo
- **Claude Code Plan Mode**: `/plan` ou Shift+Tab para entrar no modo de planejamento sem executar
- **TLC Spec Driven** (Tech Leads Club): skill instalável globalmente que conduz as quatro fases (specify → design → tasks → execute) via perguntas iterativas; se um PRD já existir, a skill usa-o como ponto de partida e só pergunta o que não estiver claro. Fases são opcionais — projeto pequeno pode pedir só spec + tasks, pulando o design.
- **Spec Kit** (GitHub): mesma família de princípios, considerado mais engessado/opinativo que a alternativa acima
- **Spec Writer** (skill pessoal, autor não identificado): skill em 6 etapas (validar inputs → entrevista → sumarizar → gerar documento → validar contra os [[wiki/concepts/criterios-de-uma-boa-spec|7 critérios de qualidade de spec]] → escrever output) que converte uma feature de um PRD já existente numa tech spec granular (technical overview, componentes, decisões técnicas, contratos de API, migration, estratégia de teste). Sem relação confirmada com "TLC Spec Driven" — nomes, etapas e critério de validação são diferentes. Ver [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]]

## Execução com Subagentes Paralelos a Partir do Breakdown de Tasks

Na fase de execução, o agente pode ler o breakdown de tasks e despachar autonomamente [[wiki/concepts/subagentes|múltiplos subagentes]] em paralelo — um por grupo de tasks que não têm dependência entre si — em vez de executar tudo sequencialmente na mesma janela de contexto. Exemplo de campo: um projeto de ~40 tasks teve fase de research feita via subagentes e fase de implementação com 4 subagentes rodando em paralelo, cada um cobrindo um subconjunto de tasks identificado no breakdown como paralelizável. Ver [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]].

## Estado: Registro de Decisões Pós-Planejamento

Distinto da spec (o que fazer) e do design (como), um projeto spec-driven também produz um artefato de **estado**, que registra as decisões tomadas pelo agente *durante* a execução (não durante o research). Serve para dar continuidade quando o trabalho precisa ser retomado numa janela de contexto nova — "continua o projeto tal" funciona porque o estado documenta o porquê das decisões já tomadas — e para permitir que o trabalho seja fatiado em múltiplos pull requests sem perder rastreabilidade. É um artefato complementar à [[wiki/concepts/memoria-de-longo-prazo-ia|memória de longo prazo]] (que salva o *research*, antes da implementação começar): o estado salva o que aconteceu *depois*.

## Origem Não-IA do Termo: SDD como Contrato de Boundary

Antes de virar sinônimo de "spec para agentes de IA", SDD (também lido como Schema-Driven Development) já era prática comum entre times humanos: especificar o contrato de uma *boundary* — o limite entre dois serviços ou entre frontend e backend — antes de qualquer lado escrever código. Os artefatos variam por protocolo:

| Protocolo | Artefato de spec |
|---|---|
| REST | OpenAPI/Swagger — ver [[documentacao-api-swagger]] |
| gRPC | arquivos `.proto` (Protobuf) — geram stubs tanto no produtor quanto no consumidor |
| GraphQL | schema GraphQL |

O objetivo é o mesmo do SDD para agentes: acordar o contrato primeiro evita o retrabalho clássico de "o Lego não encaixou" quando dois lados desenvolvem em paralelo sem alinhar a interface.

## Diferença de Prompt Engineering

| Prompt Engineering | Spec-Driven Development |
|---|---|
| Foco: como estruturar um prompt | Foco: como estruturar o processo completo |
| Escala: tarefa individual | Escala: feature/sprint |
| Artefato: um prompt | Artefato: spec + tasks + contexto do projeto |
| Autonomia: baixa (L2) | Autonomia: alta (L3) |

## Critério de Granularidade Confirmado em Campo

A engenheira do Cursor (2026) articula o critério para tamanho de task para agente:

> "A menor quantidade de trabalho mais a maior quantidade que um agente consegue fazer sem esbarrar em outro agente."

Na prática: uma feature completa com migration, schema e API repository é feita junta — para que o agente entregue de ponta a ponta sem dependência bloqueante de outro agente. Cada feature dispara ~5 agents simultâneos. A coordenação antes era entre devs paralelos; agora é entre agentes paralelos — o trabalho de coordenação não acabou, mudou de objeto.

## Crítica: "Specs to Code" Sem Disciplina de Design Degenera em Vibe Coding

[[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] traz uma crítica pontual a uma variante popular do SDD — o movimento "specs to code", onde o dev nunca olha o código gerado, só edita a especificação e "roda o compilador de novo" quando algo está errado. Relato do autor: cada rodada, sem inspeção do código nem investimento deliberado em design, produzia código progressivamente pior — paralelo direto à entropia de software do Pragmatic Programmer, e, segundo ele, "[[wiki/concepts/vibe-coding|vibe coding]] por outro nome".

O ponto não invalida SDD como definido acima (spec como contrato de execução, revisão no nível de PR) — é um alerta específico contra a versão que trata a spec como o único artefato que importa e o código como totalmente descartável. A crítica reforça o item "Revisão" do processo (revisar o resultado prático, não pular a revisão inteiramente) e conecta com [[wiki/concepts/modulo-profundo]]: specs geram código ruim persistentemente quando a base de código não tem estrutura (módulos profundos, interfaces simples) que force a IA a produzir algo revisável.

## Quem Já Faz SDD Já Está Fazendo Harness Engineering

[[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] argumenta que separar spec de execução — escrever a spec antes de pedir para codificar — já é, na prática, a separação clara entre planejar e executar que caracteriza um bom [[wiki/concepts/harness]]: o agente não planeja e executa na mesma passagem. Também funciona como [[wiki/concepts/human-in-the-loop|checkpoint]] humano entre planejar e começar a execução. Quem já pratica SDD, segundo essa leitura, já tem parte da disciplina que "harness engineering" nomeia — mesmo sem ter usado o termo.

## Segunda Fonte Independente Para "Spec É o Artefato Valioso"

[[wiki/sources/cinco-escolas-programacao-com-ia]] cita [[wiki/entities/sean-grove]] (OpenAI) com a mesma inversão de prioridade já documentada acima via [[wiki/entities/pedro-nauke]]: "a especificação é o artefato valioso; o código é só uma projeção dela." Duas fontes/pessoas independentes chegando à mesma tese central do SDD — o código como derivado descartável, a spec como o que de fato precisa ser mantido e revisado com cuidado.

## Gherkin como Spec: o Que Torna Uncle Bob Capaz de Não Ler Código

[[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] traz uma formulação direta do ponto central desta página, a partir de um ângulo diferente: para quem usa [[wiki/concepts/bdd|Gherkin/BDD]], as regras ficam na especificação em Gherkin da mesma forma que ficam na spec em SDD. O que importa não é o formato (Gherkin vs. um documento de spec) — é o momento em que é escrito: **antes** da implementação. É a única peça do sistema que o agente não derivou da própria cabeça; foi o humano, na própria pesquisa, que colocou ali algo imutável que o agente precisa seguir. Isso permite validar tanto a implementação quanto os próprios testes contra essa fonte da verdade — o mesmo papel que a spec cumpre no fluxo descrito acima.

## Teste Comparativo: Breakdown de Tasks Continua Valendo em Loop Agêntico

[[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] reporta um teste comparativo do próprio autor (Pedro Nauke), contrariando a leitura popular de que "spec driven morre" em loops agênticos de long-running tasks: comparou spec driven quebrado em tasks em loop determinístico, spec driven quebrado em tasks em loop agêntico, e execução sem quebra de tasks (spec inteira direto pro loop). Sem breakdown prévio, o resultado piorou tanto na definição de tarefas em runtime quanto na execução — mais demorado. Com artefatos de estado e breakdown definidos previamente (critérios de sucesso, testes, descrição mínima por task), o resultado melhorou, inclusive quando o loop era agêntico. Ver [[wiki/concepts/task-looper]] e [[wiki/concepts/loop-engineering#Loop Determinístico vs. Loop Agêntico]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-01-abertura]]
- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
- [[wiki/sources/formacao-ia-devs-aula-04-agentes-planejamento]]
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — separação spec/execução como a mesma disciplina que "harness engineering" nomeia; SDD como checkpoint humano entre planejar e executar
- [[wiki/sources/formacao-ia-devs-aula-05-qa]]
- [[wiki/sources/product-engineer-vale-do-silicio-2026]]
- [[wiki/sources/loop-engineering-padroes-loop-deterministico-agentico]] — teste comparativo com/sem breakdown de tasks, determinístico/agêntico
- [[wiki/sources/tdd-sdd-bdd-era-ia]] — origem não-IA do termo, contratos de API como boundary (OpenAPI, Protobuf, GraphQL)
- [[wiki/sources/fundamentos-de-software-importam-mais-que-nunca-na-era-da-ia]] — crítica ao "specs to code" sem inspeção de código
- [[wiki/sources/impacto-ia-mercado-frontend]] — SDD como filtro de entrevista no mercado de frontend: "não tem para onde correr"
- [[wiki/sources/loop-engineering-niveis-dev-loop-jogo-mmo]] — SDD como "nível 2" do dev loop (receita humana que dispara vários loops React); base do "loop criador" quando encadeado automaticamente fase a fase via roadmap
- [[wiki/sources/cinco-escolas-programacao-com-ia]] — Sean Grove (OpenAI): "a especificação é o artefato valioso; o código é só uma projeção dela" — segunda fonte independente para a mesma inversão de prioridade já central nesta página
- [[wiki/sources/spec-driven-development-otimizando-contexto-agentes]] — exemplo de campo com skill "TLC Spec Driven": breakdown de tasks com paralelismo executado por 4 subagentes simultâneos; artefato de "estado" para continuidade entre janelas de contexto
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — Gherkin escrito antes da implementação como equivalente funcional da spec: única peça do sistema que o agente não derivou da própria cabeça, usada para validar implementação e testes contra a mesma fonte da verdade
- [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] — skill "Spec Writer" (6 etapas) e framework de 7 critérios de validação de spec (falseabilidade, comportamento, invariantes, edge cases, fronteira, inputs/restrições, decisões de negócio)
