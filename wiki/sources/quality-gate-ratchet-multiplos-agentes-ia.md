---
type: source
title: "Quality Gate e Ratchet: Qualidade de Código com Múltiplos Agentes de IA"
aliases: ["quality gate ratchet", "catraca de baseline", "strawberry quality gate"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 0
tags: [tech-mentor-testing, quality-gate, ratchet, ci-cd, code-review, babysitting-de-agentes, jscpd, eslint]
skill: tech-mentor-testing
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/quality-gate-ratchet-multiplos-agentes-ia.md
source_url: ""
author: "criador de conteúdo não identificado com confiança (membro/palestrante do Stubborn Club; autor do app desktop Strawberry)"
date_published: ""
date_ingested: 2026-07-19
---

# Quality Gate e Ratchet: Qualidade de Código com Múltiplos Agentes de IA

## TL;DR

Vídeo pessoal (sem roteiro fechado) de um desenvolvedor que descreve, com exemplo concreto de pull request real, o setup de **quality gate** que montou para garantir qualidade de código quando praticamente 100% do código do seu projeto (um app desktop de LLM local chamado "Strawberry", Electron + React + llama.cpp) é escrito por agentes de IA rodando em paralelo. A peça central é o padrão **ratchet** ("catraca"): uma baseline de métricas (violações de ESLint, % de duplicação, % de cobertura, arquivos acima do limite de tamanho) é congelada, e uma regra de ouro bloqueia qualquer PR que piore qualquer uma dessas métricas — mesmo que só uma violação, uma linha ou 0,1 ponto percentual. O vídeo detalha o pipeline de CI concreto por trás disso (`npm audit` com dois níveis de severidade, lint, coverage, um script de quality gate de 581 linhas que usa `jscpd` para duplicação) e o padrão de **"babysitting"**: o próprio agente de IA, depois de abrir o PR, fica em loop verificando se o CI está verde e se há comentários de revisores, endereçando-os até poder mergear. Fecha argumentando que o gargalo real deixou de ser a geração de código pela IA e passou a ser a capacidade humana de revisar — o que exige "catracas" automatizadas porque revisor humano é falho.

## Key Claims

1. **Definição de qualidade de código (Google) já embute décadas de padrões estabelecidos** — arquitetura hexagonal, design patterns e afins são, na prática, formas de "vender" qualidade de código; quem trabalha na área há tempo já conhece esse vocabulário.
2. **A revisão de código migrou de "copiloto" para "múltiplos agentes autônomos gerando PRs em paralelo"** — o volume de código gerado (no exemplo do autor, um PR de ~800 linhas em 16 arquivos) torna inviável revisão manual linha a linha em escala.
3. **Uncle Bob (citado via Twitter) argumenta que programadores são lentos, mas não deveriam abrir mão de qualidade por isso** — a recomendação concreta dele, citada como gatilho para o setup do autor, é colocar análise estática/qualidade de código diretamente no pull request. Ver [[wiki/entities/uncle-bob]].
4. **"Babysitting" de PR — o agente de IA fica em loop até o PR poder ser mergeado**: verifica se o CI está verde, se revisores (Copilot, ferramenta externa, ou humano) deixaram comentários, endereça os comentários e resolve as conversas no GitHub. O autor recomenda explicitamente criar e customizar uma skill dedicada para esse fluxo.
5. **Quality gate como "regra de ouro" ratchet** — uma vez definida uma baseline de métricas (ESLint violations, % duplicação, % cobertura não coberta, arquivos acima do limite de tamanho), nenhum PR pode piorar nenhuma métrica, nem que seja por 0,1 ponto percentual. O repositório só pode melhorar ou empatar a partir da baseline congelada — padrão chamado de **ratchet** ("catraca": só anda num sentido).
6. **A IA já é capaz de resolver a regressão sozinha, sem instrução detalhada de arquitetura** — quando um arquivo cresce além do limite (exemplo real: `local-llm-service.js` de 1000 para 1140 linhas), modelos como Claude Opus 4.7 ou GPT-5.5 já conseguem propor modularização coerente com boa arquitetura, porque já foram treinados nos livros de referência de boas práticas — não é mais necessário descrever manualmente esses princípios no prompt.
7. **Modelos de IA "preguiçosos" por incentivo econômico do provedor, não por limitação técnica** — a tese do autor é que, se o modelo acertasse de primeira, o provedor de IA queimaria menos tokens por tarefa; deixar o modelo entregar output imperfeito e corrigir em loop (via babysitting) gera mais consumo de tokens ao longo do ciclo, o que não seria comercialmente vantajoso para a empresa de IA evitar.
8. **Custo elevado do Ultra Review / Ultra Plan da Anthropic em teste pessoal** — o autor relata ter gasto ~150 (unidade monetária não especificada) testando essas ferramentas, com um bug que fazia o Ultra Review crashar após consumir o saldo (sem entregar resultado), exigindo adicionar mais crédito para completar a execução.
9. **Métricas reais do projeto Strawberry no momento do vídeo**: 483 violações de ESLint em 120 arquivos, 2,2% de duplicação de código, 7% de cobertura de testes, 19 arquivos acima do limite de tamanho (o maior, `app.js`, com 4600 linhas) — apresentadas como baseline atual, não como estado ideal; o plano do autor é abrir PRs de refatoração dedicados para melhorar essa baseline aos poucos.
10. **Pipeline de CI concreto**: `npm ci` (instalação determinística) → `npm audit --audit-level critical` (bloqueia merge) → `npm audit --audit-level high` (avisa, não bloqueia) → `npm run lint` → `npm run test:coverage` (Jest) → script de quality gate (581 linhas, compara `metrics-summary.json` coletado contra `baseline.json`) → comentários automáticos no PR + upload de artefatos (coverage, relatórios) para que o **próprio agente de IA** tenha acesso a eles durante o babysitting.
11. **Coleta de métricas de duplicação via `jscpd`** — o script de quality gate roda `jscpd` como subprocesso e constrói o sumário de duplicação a partir do output; o autor é explícito que não há nada de excepcional na implementação, é composição de ferramentas prontas.
12. **Comentários no código voltam a fazer sentido explicitamente para agentes de IA** — o autor descreve estar "voltando atrás" da posição clássica de código autoexplicativo sem comentários: como AI harnesses buscam arquivos específicos via grep e leem o conteúdo sob demanda, um comentário explicando o quê e o porquê de um trecho é mais eficiente para o agente do que documentação externa (ex.: README gigante) que pode não ser recuperada na busca.
13. **Manutenibilidade, confiabilidade, testabilidade e eficiência seguem como eixos de qualidade** — o autor cita SonarQube e GitHub Code Quality como alternativas prontas ao script caseiro para medir complexidade, duplicação e coverage.
14. **O humano, não a IA, é o gargalo do próprio processo** — o autor identifica que fazer babysitting manual de PRs é o que limita sua capacidade de entregar múltiplas tarefas em paralelo; a resposta não é revisar mais, mas se "blindar dos próprios erros como revisor" via controle de qualidade automatizado, partindo da premissa de que qualquer controle de qualidade humano é falho.

## Entidades Mencionadas

- [[wiki/entities/uncle-bob]] — citação via Twitter sobre programadores serem lentos mas não deverem abrir mão de qualidade; recomendação de análise estática no PR
- [[wiki/entities/anthropic]] — custo do Ultra Review / Ultra Plan em teste pessoal do autor

## Conceitos Tocados

- [[wiki/concepts/quality-gate]]
- [[wiki/concepts/pipeline-de-qualidade]]
- [[wiki/concepts/ratchet-baseline]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/codebase-legibilidade-ia]]
- [[wiki/concepts/comentarios-o-que-nao-o-como]]
- [[wiki/concepts/skills-agente]]
- [[wiki/concepts/capital-de-tokens]]

## Open Questions

- **Identidade do autor não confirmada** — a transcrição não permite identificar nome, sobrenome ou canal com confiança; ele se refere de passagem ao próprio Instagram e a uma comunidade paga ("Stubborn Club" — grafia incerta, transcrita como "stupid button club"), a mesma já registrada em [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]]. Não é possível confirmar se é a mesma pessoa de outras fontes já ingeridas que também citam o Stubborn Club — o estilo (vídeo solo, primeira pessoa) é diferente do formato de podcast em dupla do CDF Café ([[wiki/entities/codigo-fonte-tv]]). Nenhuma entidade nova foi criada para evitar atribuição incorreta.
- **Nome completo do app/projeto incerto** — a transcrição corta o nome como "strawberry h..."; mantido como "Strawberry" por ser a parte clara e repetida na fala.
- **Unidade monetária do gasto com Ultra Review/Ultra Plan não especificada** — o autor diz "gastei 150" sem confirmar se são reais, dólares ou créditos da plataforma; tratado como valor aproximado não conversível.
- **Nome do produto concorrente citado de forma incerta** ("Mitos"/"mito") no contexto do lançamento do Ultra Review/Ultra Plan — mesma classe de problema de transcrição já registrada em outras fontes desta wiki (ex.: nome de framework em [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]]); não foi possível confirmar a que produto o autor se referia.
- Esta fonte é fortemente prática/ferramental (scripts reais, métricas reais, pipeline de CI detalhado) — complementar, não sobreposta, a [[wiki/sources/gate-de-qualidade-definicoes-formais]] (puramente teórica) e a [[wiki/sources/rfcs-grill-me-e-o-risco-da-preguica-no-vibe-coding]] (foco em RFC e na skill Grill Me como mitigação de perda de entendimento, não em métricas automatizadas de código).

## Raw Quotes

> "Cada PR pode adicionar código, mas não pode aumentar nenhuma das métricas — nem por uma violação, nem por uma linha, nem por 0,1 ponto percentual."

> "Isso aqui normalmente se chama de ratchet, que é catraca: a catraca tu só anda num sentido — uma vez que tu congelou ali o teu baseline, o repositório só pode melhorar a partir dali, ou empatar."

> "Não seria mais vantajoso pra IA [a empresa de IA] se o modelo fizesse de primeira — eles têm capacidade de já fazer de primeira."

> "Eu sempre fui a favor de tu não escrever comentários no código porque o teu código é a tua própria documentação, mas agora no mundo de agentes de IA eu tô voltando um pouco atrás nisso aí."

> "Eu acabei virando o gargalo da IA — eu fazer o babysit das coisas básicas do PR é o gargalo. Eu não consigo entregar quatro tarefas ao mesmo tempo se eu precisar ler 10.000 linhas de código por dia."

> "Como qualquer controle de qualidade, o humano é falho — então tu tem que colocar catracas, tem que colocar portões, para barrar automaticamente quando a qualidade cair."
