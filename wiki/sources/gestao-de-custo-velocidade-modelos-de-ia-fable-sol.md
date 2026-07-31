---
type: source
title: "Fable, Sol e a Gestão de Custo e Velocidade na Escolha de Modelos de IA"
aliases: ["fable e sol gestao de custo", "roteador customizado abacus", "modelo por tarefa fable sol"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [llm, model-routing, custo, velocidade, anthropic, openai, abacus, artificial-analysis, opencode]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/gestao-de-custo-velocidade-modelos-de-ia-fable-sol.md
source_url: ""
author: "desconhecido"
date_published: 2026-07-31
date_ingested: 2026-07-31
---

## TL;DR

Vídeo em português (autor não identificado na transcrição) argumenta que o paradigma antigo de "usar sempre o modelo de ponta" (Opus, em planos de US$200/mês, às vezes múltiplas contas) quebra com o Fable (Anthropic) e o Sol/GPT 5.6 (OpenAI): são os dois modelos mais inteligentes do mercado segundo o Artificial Analysis, mas também os mais caros (~70× o custo por tarefa do DeepSeek V4) e mais lentos. A recomendação central é substituir "um modelo para tudo" por uma decisão de roteamento em três eixos — inteligência, velocidade, custo — primeiro testada manualmente tarefa a tarefa, depois automatizada via skill/subagentes no Claude Code ou via um roteador customizado de terceiros (demonstrado na Abacus, ferramenta patrocinadora, com fallback para uso via OpenCode).

## Key Claims

1. **Fable (Anthropic) e Sol/GPT 5.6 (OpenAI) são, segundo o Artificial Analysis, os dois modelos com maior pontuação de inteligência do mercado (60 e 59), destacados dos demais.** [[wiki/entities/anthropic]] e [[wiki/entities/openai]] — confiança média: número específico do índice não é verificável de forma independente nesta ingestão (sem link direto ao dashboard do Artificial Analysis na fonte), mas a existência de "Sol" como apelido de um modelo OpenAI de cybersegurança já era registrada em [[wiki/entities/openai]] antes desta fonte (seção "Incidente de Segurança"), o que dá suporte cruzado ao nome.
2. **Os mesmos dois modelos perdem em velocidade para modelos mais leves** (GLM, Grok, Gemini Flash citados como exemplos) e **custam ordens de magnitude mais por tarefa** — a fonte cita o DeepSeek V4 pontuando 44 (vs. 59-60 de Fable/Sol) a um custo por tarefa ~70× menor. Confiança média: o número "70×" e o valor "4 centavos por tarefa" vêm de leitura de gráfico narrada em vídeo, sem captura de tela ou link para os dados brutos do Artificial Analysis.
3. **O paradigma de "um modelo só, o tempo todo" (rodar Opus 24/7, comprar contas extras de US$200 quando estoura) deixou de ser viável financeiramente com o salto de preço do Fable/Sol** — a fonte estima que rodar o Fable "o dia inteiro, 40 horas por semana" estouraria um plano de US$200/mês. Confiança média: é uma estimativa de ordem de grandeza do autor, não um cálculo publicado com metodologia.
4. **A recomendação estruturada é decidir modelo por três variáveis — inteligência, velocidade, custo — mapeadas em três "camadas" de uso**: modelos de fronteira (Fable, Sol, e também GPT 5.5/Opus 4.8 citados como alternativas quase tão boas) para tarefas de alta complexidade/incerteza (arquitetura, quebra de feature complexa, bugs difíceis); modelos rápidos (Gemini Flash, citado com 70 no coding index) para tarefas simples e urgentes; modelos de fallback mais baratos (Sonnet, Kimi, DeepSeek) para tarefas simples/background. Isso é consistente com a heurística já documentada em [[wiki/concepts/modelo-por-leverage-tarefa]] (Fable para planejamento → Opus para quebra de tarefas → Sonnet para implementação), mas adiciona um eixo de velocidade que aquela página não cobria explicitamente.
5. **A decisão de roteamento pode ser tomada manualmente (trocando de modelo no Claude Code por tarefa) ou automatizada via skill + subagentes** (um subagente por modelo, skill decide qual acionar) — reforça diretamente o padrão já descrito em [[wiki/concepts/roteamento-automatico-de-modelo]], mas aplicado especificamente ao Claude Code em vez de a um produto comercial como a Adapta.
6. **Demonstração prática: "Custom Router" na Abacus.AI** — dentro da assinatura, é possível criar um roteador próprio a partir de um template ("Frontier"), definindo categorias e o modelo associado a cada uma. Configuração mostrada no vídeo: Frontier/problem solving → Fable; Complexo → Opus 4.8; categoria extra → GPT 5.5; Velocidade → Gemini Flash; Balanceado → Kimi; Fallback → Sonnet 5. A chave de API gerada pelo router pode ser usada em outras ferramentas (ex.: OpenCode, conectando via tela de "connect provider"), do mesmo modo como já foi mostrado em vídeo anterior do canal a conexão com Anthropic e com Kimi via OpenCode.
7. **A fonte apresenta esse tipo de roteamento customizado como não específico da Abacus** — o mesmo conceito é dito ser implementável via OpenRouter, via ferramentas similares no Cursor, via skill própria no Claude Code, ou via script local — sem vendor lock-in inerente ao padrão.

## Entidades e Conceitos Tocados

- [[wiki/entities/anthropic]]
- [[wiki/entities/openai]]
- [[wiki/entities/abacus-ai]]
- [[wiki/entities/artificial-analysis]]
- [[wiki/entities/deepseek]]
- [[wiki/entities/google]]
- [[wiki/entities/moonshot-ai]]
- [[wiki/concepts/roteamento-automatico-de-modelo]]
- [[wiki/concepts/modelo-por-leverage-tarefa]]
- [[wiki/concepts/corrida-preco-qualidade-llm]]
- [[wiki/concepts/modelo-frontier]]
- [[wiki/entities/claude-code]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/concepts/modelo-por-leverage-tarefa]] já documentava, a partir de [[wiki/sources/20-melhores-praticas-claude-code-segundo-anthropic]], a ideia de escalonar modelo por alavancagem de tarefa (Fable para planejamento, Opus para quebra de spec, Sonnet para implementação). Esta fonte confirma o mesmo padrão de forma independente, mas amplia a heurística: em vez de só "quanto maior o impacto, mais forte o modelo", introduz explicitamente velocidade como terceiro eixo (não só custo x qualidade) e traz dados concretos de benchmark (Artificial Analysis) para justificar a escolha. Recomendação: fundir os dois modelos mentais na página de conceito.

**Reforço direto:** [[wiki/concepts/roteamento-automatico-de-modelo]] documentava roteamento automático apenas no contexto do produto comercial Adapta ONE (mecanismo de decisão proprietário e opaco). Esta fonte adiciona um segundo caso concreto e mais transparente — o Custom Router da Abacus, onde o usuário define manualmente a categoria → modelo, sem "IA decidindo por trás" — uma variante mais simples (roteamento por categoria fixa, não por classificador aprendido) do mesmo padrão de infraestrutura.

**Reforço direto:** [[wiki/concepts/corrida-preco-qualidade-llm]] já registrava a tese de que a diferença de preço/qualidade entre modelos frontier fechados e modelos mais baratos (incluindo DeepSeek) é uma dinâmica central do mercado de 2025-2026. Esta fonte dá um dado quantitativo novo e específico (~70× de diferença de custo por tarefa entre Fable e DeepSeek V4, com pontuações de 59-60 vs. 44 no coding index) que a página anterior não tinha.

**Consistência de nomenclatura:** o apelido "Sol" para um modelo da OpenAI já constava em [[wiki/entities/openai]] (seção "Incidente de Segurança: Benchmark Interno de Cybersegurança"), onde aparece ao lado do GPT 5.6 como um dos modelos usados no benchmark interno sem guardrails. Esta fonte usa "Sol" e "GPT 5.6" como sinônimos diretos ("o Sol da OpenAI... GPT 5.6"), o que não estava explícito antes — tratado aqui como confirmação parcial, não prova definitiva, já que ambas as fontes são transcrições de vídeo sem link para nomenclatura oficial da OpenAI.

**Tensão não resolvida:** [[wiki/concepts/modelo-frontier]] lista atualmente "Opus 4.7" como o modelo mais capaz da Anthropic e não inclui "Fable" na tabela principal de modelos frontier para codificação (menciona Fable 5 apenas na subseção separada de "modelos frontier de cybersegurança não-públicos", junto com [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]]). Esta fonte, no entanto, trata o Fable como o modelo de uso geral mais forte da Anthropic para tarefas de programação/arquitetura (não como um modelo restrito de cybersegurança) — sugerindo que o nome "Fable" pode estar sendo usado na wiki para duas coisas distintas: (a) o modelo frontier de uso geral mais recente da Anthropic, e (b) a variante/model card especializada em cybersegurança do mesmo nome. Registrado como open question abaixo; a tabela de [[wiki/concepts/modelo-frontier]] foi atualizada para refletir Fable como modelo de uso geral, com nota sobre a ambiguidade.

## Open Questions

- **Ambiguidade "Fable" uso geral vs. "Fable 5" cybersegurança**: não fica claro, cruzando esta fonte com [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]], se "Fable" (aqui) e "Fable 5" (lá) são o mesmo modelo em dois contextos de uso, ou modelos/model cards distintos que compartilham nome. Nenhuma das duas fontes é documentação oficial da Anthropic — tratar a relação entre os dois como não confirmada.
- **Autoria do vídeo não identificada** na transcrição fornecida — não é possível atribuir a um canal/criador específico nesta ingestão, diferente da maioria das fontes recentes da wiki.
- **Números do Artificial Analysis (60, 59, 44, 70×, 4 centavos, 70 no coding index do Gemini Flash) não foram verificados contra o site do Artificial Analysis nesta ingestão** — vieram de leitura de gráfico narrada em áudio, sujeita a erro de transcrição e a defasagem temporal (o vídeo é datado, o dashboard do Artificial Analysis muda continuamente).
- **Não fica claro se "GPT 5.5" e "Opus 4.8"**, citados como alternativas "quase tão boas quanto" Fable/Sol para tarefas de alta complexidade, são versões anteriores estáveis ou também modelos de fronteira recentes — a fonte não datou o lançamento de nenhum dos dois.
- **Segmento patrocinado (Abacus)**: a demonstração do Custom Router é parte de um bloco de patrocínio explícito do canal — tratado aqui como demonstração de um padrão genérico (o autor explicitamente diz que o conceito funciona em outras ferramentas), não como avaliação independente da qualidade do produto Abacus.
