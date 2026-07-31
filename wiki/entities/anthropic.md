---
type: entity
title: "Anthropic"
aliases: ["Anthropic", "Antrópica"]
date_created: 2026-06-02
date_updated: 2026-07-31
source_count: 17
tags: [anthropic, claude, llm, harness, mcp, ia-para-devs, custo-de-ia, loop-engineering, claude-tag, slack]
skill: tech-mentor-ai
status: stable
---

# Anthropic

Empresa de IA fundada em 2021, criadora da família de modelos Claude e do harness Claude Code. Responsável por diversas specs que viraram padrão de mercado: rules, skills, MCP (Model Context Protocol), subagents.

## Modelos Principais (2026)

| Modelo | Uso recomendado |
|---|---|
| Fable | Segundo [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]], modelo mais forte da Anthropic no Artificial Analysis (pontuação 60) — recomendado para tarefas de alta complexidade/incerteza (arquitetura, quebra de feature complexa); também o mais caro e mais lento da família. Ver nota de ambiguidade com "Fable 5" em [[wiki/concepts/modelo-frontier]] |
| Opus 4.7 / 4.8 | Frontend, design, review de código; alternativa quase tão forte quanto Fable para tarefas complexas, a menor custo |
| Sonnet 4.6 / Sonnet 5 | Uso geral — menos recomendado para tarefas exigentes por Nauke; citado como bom fallback para tarefas simples/background |
| Haiku | Tarefas simples, custo baixo |

## Harness: Claude Code

Ver [[wiki/entities/claude-code]]. Principal harness de codificação da Anthropic; considerado o mais inovador do mercado em 2026 com features como: dream consolidation, scheduler, tool search lazy load, memória, worktrees.

## Specs que Viraram Padrão

- **Rules** (CLAUDE.md / project rules)
- **Skills** (conjuntos de instruções reutilizáveis)
- **MCP** (Model Context Protocol) — protocolo aberto para tools/resources
- **Subagents** — ver [[wiki/concepts/subagentes]]

## Relação com Google

Google fez investimento bilionário na Anthropic (cifra não confirmada na fonte; sugestão de verificar). Irônico dado que a Google também tem seu próprio harness (AntiGravity) e modelos (Gemini).

## Preços Históricos

Opus caiu de $15.75/M (input) para ~$5/M — movimento que tornou o uso do Opus mais acessível e aumentou sua adoção.

## Tokenizador e Token Tax

O tokenizador do Claude usa [[byte-pair-encoding]] com foco em inglês, resultando no pior multiplicador de custo para idiomas não-ingleses entre os principais provedores (OpenAI, Google). Português paga ~1.62× mais tokens que inglês — ver [[token-tax-multilingual]]. Não é intenção maliciosa; é consequência do corpus de treinamento ser predominantemente em inglês.

Demonstração via [[entities/vercel-ai-sdk]] com Claude 3.5 Haiku: o prompt `"Hello World"` (2 palavras) já consome 11 tokens de entrada — contra apenas 4 no Gemini 2.0 Flash Lite do Google para o mesmo prompt. Contagens de tokens de entrada/saída não são comparáveis entre provedores porque cada um usa um vocabulário de tokenizer próprio — ver [[tokenizacao]].

**Claim não verificado — mudança de tokenizer no Sonnet 5:** [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] afirma que a Anthropic mudou o tokenizer no Sonnet 5, dificultando o rastreio do custo real por tarefa (o preço por token cai, mas a mesma tarefa passa a gerar mais tokens no tokenizer novo). Confiança baixa: a fonte não cita changelog oficial nem cruza com outra fonte da wiki; é um claim diferente do token tax multilíngue documentado acima (BPE com viés para inglês), e não deve ser confundido com ele.

## Custo do Ultra Review / Ultra Plan em Teste Pessoal

[[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] relata um teste pessoal do autor com o Ultra Review e o Ultra Plan da Anthropic: gastou cerca de 150 (unidade monetária não especificada na fonte) só testando, com o Ultra Review consumindo ~30 por execução — e um bug fazia a ferramenta crashar depois de já ter consumido o saldo disponível, sem entregar resultado, obrigando a adicionar mais crédito para completar e ver o output. Tratado como relato de experiência individual, não como benchmark de custo oficial da Anthropic.

## Venda Enterprise no Brasil e Subsídio de Produto

Segundo [[wiki/sources/kimi-k3-china-mercado-ia-open-source]], a Anthropic já vende para Enterprise no Brasil — sinal, na leitura da fonte, de que a empresa sabe que não há vantagem competitiva sustentável apenas em vender token/API, daí o Claude Code ser frequentemente subsidiado com promoções e créditos gratuitos recorrentes. Ligado à tese de [[wiki/concepts/corrida-preco-qualidade-llm]]: concorrência de modelos open source (Kimi, DeepSeek) pressiona preço para baixo no mercado como um todo.

## Bug de Billing no Claude Max 20 (String "hermes" no Git History)

[[wiki/sources/hermes-agent-open-claw-learning-loop]] relata um segundo incidente de billing (o primeiro está na seção "Custo do Ultra Review" acima): um usuário do Claude Max 20 (US$200/mês) teve o uso extra consumido por um bug na detecção de ferramentas de terceiros da Anthropic, disparado ao encontrar a string "hermes" (de `hermes.md`, convenção real para specs de prompt de sistema em projetos de agentes) no Git history do usuário. Um representante da Anthropic (citado como "Tarik" na fonte, não confirmado externamente) admitiu publicamente o bug — "bug na detecção de ferramentas de terceiros e na forma como incluímos o status do Git no prompt do sistema" — e ofereceu reembolso aos afetados.

## Dreaming in Claude

Feature anunciada pela Anthropic dias antes da publicação de [[wiki/sources/hermes-agent-open-claw-learning-loop]]: permite revisar sessões passadas de agentes Claude, extrair padrões e curar memórias ao longo do tempo — resposta direta ao mesmo padrão de "learning loop com skill/memória persistente" que projetos open source como [[wiki/entities/hermes-agent]] e [[wiki/entities/open-claw]] já implementavam. Sem página própria na wiki ainda; candidata a stub caso surja fonte dedicada.

## Pesquisa de Interpretabilidade: J-Space e Jacobian Lens

Pesquisa publicada pela própria Anthropic identificando um espaço interno no Claude ([[wiki/concepts/j-space-interpretabilidade]]) — padrões de ativação vinculáveis a palavras que o modelo processa mas nunca verbaliza no output, lidos via uma técnica nova chamada Jacobian Lens. A própria Anthropic é cautelosa e nega que isso prove consciência ou experiência subjetiva — trata como uma "maquinaria mental" estruturalmente análoga (não equivalente) à divisão consciente/inconsciente humana. Ver [[wiki/sources/jspace-cerebro-cloud-antropic]].

## Mitos e Fable 5: Modelos de Cybersegurança Bloqueados pelo Governo dos EUA

Segundo [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]], a Anthropic desenvolveu uma classe de modelos especializados em cybersegurança ofensiva/defensiva — o **Mitos** (anunciado abril de 2026) e depois **Fable 5** e **Mitos 5** — capazes de encontrar vulnerabilidades de software em escala inédita (falha de 27 anos no OpenBSD, 16 anos no FFmpeg, brechas no núcleo do Linux, 10.000+ falhas de gravidade alta/crítica via o consórcio fechado **Glasswing**, que cresceu de ~50 para ~150 organizações em 15 países entre abril e junho de 2026). A capacidade foi julgada perigosa o suficiente para que a Anthropic nunca liberasse o Mitos ao público, e para que o governo dos EUA bloqueasse formalmente o acesso ao Fable 5 e ao Mitos 5 — inclusive para funcionários não-americanos da própria Anthropic — depois que a NSA relatou sistemas confidenciais comprometidos "em questão de horas". Mesmo com salvaguardas reforçadas, um laboratório italiano conseguiu contornar o Fable 5 em 702 de 7.828 tentativas de jailbreak — nuance que qualifica a robustez real dos guardrails da empresa (ver [[wiki/sources/ai-safety-guardrails]]).

## Claude Tag: Claude Integrado ao Slack

Produto que integra o Claude ao Slack via @menção ("Claude Tag"), lançado com anúncio oficial destacando que **65% do código do time de produto da Anthropic é criado pela nova versão do Claude Tag** (número não totalmente esclarecido quanto a escopo — ver open questions em [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]]). Diferente de um bot simples de resposta a @menção (já commodity há anos), o produto introduz: (1) memória multiplayer por canal, compartilhada entre todos os membros do time, não por usuário individual — ver [[wiki/concepts/agent-memory-tres-camadas]]; (2) modo "ambient", proativo, sem exigir @menção explícita; (3) execução assíncrona de tarefas longas (horas/dias). Gerou tese de Andrej Karpathy de que seria a "terceira reformulação da interface de LLM" — ver [[wiki/concepts/paradigmas-interface-llm]] para o framework completo e o contraponto de Gergely Orosz.

## Anthropic Ultrapassa a OpenAI em Gasto no Cartão Corporativo (Abril 2026)

Segundo [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]], em abril a Anthropic passou a OpenAI pela primeira vez em % de empresas americanas usando cartão corporativo para seus serviços: Anthropic subiu para 34,4%, OpenAI caiu para 32,3% (fonte primária do dado não identificada na transcrição — provavelmente um relatório agregado de gasto corporativo tipo Ramp; tratar como não confirmado externamente). Lido pelo apresentador como evidência de que a Anthropic está ganhando fatia do mercado B2B/enterprise, historicamente dominado por Google e depois pela OpenAI.

## Guia Oficial "Getting Started with Loops"

Guia oficial publicado pela Anthropic definindo quatro níveis de autonomia para loops agênticos — turn-based, goal-based, time-based e proactive — cada um entregando progressivamente mais responsabilidade de decisão ao agente (ver [[wiki/concepts/loop-engineering]] para a lista completa). Publicado cerca de um ano depois do [[wiki/concepts/ralph-loop|Ralph Loop]] de [[wiki/entities/geoffrey-huntley]] (julho de 2025) ter demonstrado, de forma deliberadamente simples, que o próprio conceito de "loop até terminar" era viável — segundo [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]], a Anthropic institucionalizou um ano depois algo que começou como uma técnica quase de piada.

## Key Sources

- [[wiki/sources/html-vs-markdown-para-agentes-de-ia]]
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] — venda Enterprise no Brasil, subsídio de produto como resposta à concorrência open source — citada de passagem como tendo "divulgado algo parecido" sobre preferir HTML a Markdown na saída de agentes; a fonte não linka o material original, então tratar como não verificado
- [[wiki/sources/formacao-ia-devs-aula-03-llm]]
- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/claude-code-guia-pratico-full-cycle]]
- [[wiki/sources/custo-tokens-portugues-vs-ingles]]
- [[wiki/sources/palantir-ceo-token-tax-nvidia-scam-ia]] — claim não verificado de mudança de tokenizer no Sonnet 5; contexto do Departamento de Guerra dos EUA na crítica do CEO da Palantir
- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/multiplos-agentes-worktrees-subagentes-claude-code]]
- [[wiki/sources/observabilidade-ponta-a-ponta-opentelemetry-ia-amsterdam]] — citada de passagem: erros `503` frequentes da API do Claude ("modelo ocupado, tente novamente") como exemplo do "novo normal" de sistemas caindo, exigindo estratégias de retry no lado do cliente
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — custo elevado do Ultra Review/Ultra Plan em teste pessoal, incluindo bug de crash que consumiu saldo sem entregar resultado
- [[wiki/sources/hermes-agent-open-claw-learning-loop]] — bug de billing no Claude Max 20 disparado pela string "hermes" no Git history; anúncio do Dreaming in Claude
- [[wiki/sources/jspace-cerebro-cloud-antropic]] — pesquisa de interpretabilidade (J-Space, Jacobian Lens): espaço interno de ativações vinculáveis a palavras nunca verbalizadas no output
- [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] — Mitos e Fable 5, modelos de cybersegurança bloqueados pelo governo dos EUA; consórcio Glasswing; jailbreak documentado do Fable 5
- [[wiki/sources/harness-engineering-voce-e-o-harness-nao-o-modelo]] — guia oficial "Getting Started with Loops" (quatro níveis de autonomia de loop)
- [[wiki/sources/claude-tag-slack-terceiro-paradigma-llm]] — lançamento do Claude Tag (Claude integrado ao Slack); dado de gasto em cartão corporativo ultrapassando a OpenAI em abril de 2026
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Fable como modelo mais forte no Artificial Analysis, mas ~70× mais caro por tarefa que o DeepSeek V4; caso de roteamento manual/automatizado no Claude Code
