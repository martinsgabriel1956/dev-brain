---
type: concept
title: "Modelos Frontier"
aliases: ["frontier models", "modelos de ponta", "modelos comerciais avancados"]
date_created: 2026-06-02
date_updated: 2026-08-11
source_count: 6
tags: [modelos, frontier, llm, openai, anthropic, google]
skill: tech-mentor-ai
status: draft
---

# Modelos Frontier

Os modelos de linguagem mais capazes disponíveis no mercado em um dado momento — geralmente comerciais e fechados, com bilhões de parâmetros e treinamento proprietário em escala massiva. São o padrão de referência para tarefas de codificação profissional.

## Modelos Frontier para Codificação (2026)

| Modelo | Provider | Destaque |
|---|---|---|
| Fable | Anthropic | Segundo [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]], modelo de uso geral mais forte da Anthropic para arquitetura/planejamento no Artificial Analysis (pontuação 60); ver nota de ambiguidade abaixo sobre a relação com "Fable 5" (cybersegurança) |
| Sol / GPT 5.6 | OpenAI | Modelo mais forte da OpenAI no Artificial Analysis (pontuação 59); "Sol" é apelido informal, não nome oficial confirmado |
| Opus 4.7 / Opus 4.8 | Anthropic | Top em design/frontend; preferido para review; citado como alternativa quase tão boa quanto Fable para tarefas de alta complexidade |
| GPT-5.5 | OpenAI | Melhor reasoning para tarefas novas/complexas |
| GPT-5.4 | OpenAI | Melhor custo-benefício que 5.5 para muitas tarefas |
| Gemini 3.5 Flash | Google | Citado com pontuação 70 no coding index — rápido e forte para tarefas simples/urgentes |
| DeepSeek V4 | DeepSeek | Pontuação 44 no coding index a ~1/70 do custo por tarefa do Fable — ver [[wiki/concepts/corrida-preco-qualidade-llm]] |
| Gemini 3.1 | Google | Puxou contexto de 1M tokens; forte em multimodal |
| Kimi K2.6 | Moonshot (open-weight) | Resultado comparável a frontier por fração do preço |
| Kimi K3 | Moonshot (open-weight, lançamento parcial) | 2,8T parâmetros, MoE 896/16 experts, até 75% economia de KV Cache — ver [[wiki/entities/moonshot-ai]] |
| GLM 5.1 | Zhipu AI (open-weight) | MoE barato e eficiente |
| Qwen 3.6 | Alibaba (open-weight) | MoE; muito bom para código |

## Comerciais vs Open-Weight

**Comerciais** (Anthropic, OpenAI, Google): modelo fechado, treinamento opaco, API com compliance enterprise, custo mais alto.

**Open-weight** (Kimi, Qwen, GLM): pesos disponíveis publicamente, treinamento baseado em MoE (mais barato de rodar), preços de API muito menores. Em 2025–2026, passaram de "praticamente inúteis" para "suficientes para muitas tarefas profissionais".

## Como o GPT chegou ao nível de codificação

A OpenAI pegou o modelo O3 (alto reasoning), fez fine-tuning específico para código, e o resultado foi excelente. As versões 5.1, 5.2, 5.3, 5.4, 5.5 evoluíram sobre essa base. Não é um modelo novo — é o mesmo base com melhorias incrementais de fine-tuning e RLHF.

## Degradação e Custo

Ver [[wiki/concepts/degradacao-de-contexto]] para como a qualidade dos modelos frontier cai após ~400k tokens.

Ver [[wiki/sources/formacao-ia-devs-aula-03-llm]] para tabela de preços por token.

## Nota de Ambiguidade: "Fable" de Uso Geral vs. "Fable 5" de Cybersegurança

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] usa "Fable" como o modelo de uso geral mais forte da Anthropic para programação/arquitetura — sem qualquer menção a restrição de acesso ou especialização em cybersegurança. Isso contrasta com a subseção abaixo, onde "Fable 5" é descrito por [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] como um modelo bloqueado pelo governo dos EUA por capacidade ofensiva de cybersegurança. Nenhuma das duas fontes é documentação oficial da Anthropic (ambas são transcrições de vídeo), então a relação entre os dois não está confirmada: pode ser o mesmo modelo em dois contextos de uso (geral vs. cybersegurança), ou duas coisas distintas que compartilham nome por coincidência/erro de transcrição. Tratado como open question em ambas as fontes.

## Subclasse: Modelos Frontier de Cybersegurança (não-públicos)

Além dos modelos frontier de uso geral acima, surgiu em 2026 uma subclasse de modelos frontier especializados em cybersegurança ofensiva/defensiva — capazes de descobrir vulnerabilidades de software em escala industrial (falhas de décadas de idade em OpenBSD, FFmpeg, kernel Linux). Diferem dos modelos da tabela acima por não serem lançados ao público: Mitos e Fable 5 (Anthropic) e Mitos 5 foram restritos a um consórcio fechado (Glasswing) e depois formalmente bloqueados pelo governo dos EUA; o GPT 5.6 (OpenAI) seguiu o mesmo padrão de bloqueio. Japão (Sakana AI/Fugo) e China (360/Tulong Fang, Zhipu AI/GLM 5.2) já reivindicam capacidade equivalente. Ver [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]].

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] — Kimi K3, 2,8T parâmetros, lançamento parcial
- [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] — subclasse de modelos frontier de cybersegurança bloqueados por risco de segurança nacional (Mitos, Fable 5, GPT 5.6)
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Fable e Sol/GPT 5.6 como os dois modelos mais fortes no Artificial Analysis; dados de custo/velocidade comparativos entre modelos de fronteira e alternativas mais baratas
- [[wiki/sources/precificacao-ancoragem-anthropic-opus-5-lancamento]] — reposicionamento da linha Anthropic: Fable como âncora premium, **Opus como "novo Sonnet"**, Grok 4.5 e Kimi K3 no mid-tier abaixo do Opus, tier barato (Haiku) sendo abandonado
