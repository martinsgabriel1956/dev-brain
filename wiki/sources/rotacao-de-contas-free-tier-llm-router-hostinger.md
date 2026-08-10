---
type: source
title: "Achei um Esquema pra Rodar Cloud Code de Graça (Rotação de Contas Free Tier via LLM Router)"
aliases: ["esquema illuminati cloud code de graça", "nine router", "rotação de contas free tier llm"]
date_created: 2026-08-05
date_updated: 2026-08-05
source_count: 0
tags: [tech-mentor-ai, ai-gateway, llm-router, free-tier, claude-code, openrouter, fallback, token-economics, vendor-lock-in, hostinger]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/rotacao-de-contas-free-tier-llm-router-hostinger.md
source_url:
author: desconhecido (canal de vídeo, tom informal "boteco de tecnologia", patrocínio Hostinger)
date_published:
date_ingested: 2026-08-05
---

# Achei um Esquema pra Rodar Cloud Code de Graça (Rotação de Contas Free Tier via LLM Router)

## TL;DR

Transcrição de vídeo demonstrando o "Nine Router" (nome ouvido foneticamente, grafia não confirmada) — um AI Gateway/proxy local, compatível com as APIs da Anthropic e OpenAI, que permite (1) plugar múltiplos providers de LLM (Cloud Code, Gemini CLI, Cursor, Codex, Llama, Qwen, Kiro, OpenRouter) atrás de uma única URL/chave, (2) mapear o modelo que uma ferramenta como o Claude Code "acha" que está usando para qualquer outro modelo real (ex.: GLM 5.2, MiMo), e (3) cadastrar várias contas free tier do mesmo provider e rotacioná-las automaticamente quando o token de uma esgota — driblando o limite de free tier de cada conta individual e, segundo o autor, "quebrando o lockin" de ferramentas como o Claude Code (usá-las de graça com modelos não-Anthropic). O vídeo também testa ao vivo uma funcionalidade de compressão de contexto ("Token Saver") e conclui, com dados de uso reais, que ela piorou o resultado no caso de teste (Ruby on Rails): custo e tokens consumidos aumentaram (de $0,81/705k tokens de input para 2,2 milhões de tokens de input) em vez de diminuir. O autor reconhece abertamente, ao final, que a prática de rotacionar contas free tier é arriscada para uso profissional — provedores como Gemini CLI e Claude Code têm detecção de abuso e podem banir a conta.

## Key Claims

1. **O Nine Router é um AI Gateway/proxy self-hosted, compatível com a API da Anthropic e da OpenAI** — funciona como drop-in replacement: basta apontar `ANTHROPIC_BASE_URL` e a chave gerada pelo proxy no `claude-settings.json`, sem precisar logar na ferramenta cliente (Claude Code) com uma conta real. Este é o mesmo padrão "AI Gateway" documentado em `references/ai/ai-gateway.md` (skill tech-mentor-ai) — troca só a `base_url`, código/config do cliente não muda. [skill: tech-mentor-ai]
2. **Rotação de múltiplas contas free tier do mesmo provider** — diferente de [[wiki/concepts/roteamento-automatico-de-modelo]] (que escolhe o modelo mais adequado à tarefa), aqui a rotação escolhe entre **credenciais/contas equivalentes** do mesmo tipo, avançando para a próxima conta quando a corrente esgota a cota de free tier — mecanismo mais próximo de round-robin de rate limit do que de model routing por qualidade.
3. **Mapeamento de modelo "espelhado"** — o Claude Code acredita estar chamando um modelo Anthropic (ex.: Haiku 4.5), mas o proxy redireciona a chamada para um modelo completamente diferente (ex.: GLM 5.2 via OpenRouter, ou MiMo da Xiaomi via Kiro) — o cliente não tem visibilidade de que o modelo real mudou.
4. **Fallback com ordem de tentativa ("try in order")** — se a chamada a um modelo/conta falhar, o gateway tenta o próximo da lista configurada, e repete até um responder; o autor considera essa a opção mais simples e a que funcionou "uma maravilha", em oposição a uma opção de "penalização" cujo mecanismo exato ele não entendeu.
5. **Teste ao vivo do "Token Saver" mostrou resultado oposto ao esperado, no caso testado** — com um prompt idêntico (gerar uma API CRUD em Ruby on Rails 7 com SQLite e testes passando), a versão sem compressão de output gastou $0,81 (705k tokens de input, 4,8k de output, 748,8k de leitura de cache) contra $ muito maior e **2,2 milhões de tokens de input** (12,8k de output, 2,6 milhões de leitura de cache) e 7 minutos de execução com a compressão de output ativada. O autor testou também a opção "Caveman" (skill de compressão de linguagem) e relata que também piorou o consumo de tokens no seu caso de uso.
6. **Fallback silencioso entre modelos compartilha o mesmo contexto de conversa** — ao trocar de modelo por falha de um provider, o histórico de conversa não se perde, permitindo sessões efetivamente mais longas do que a janela de contexto nativa de qualquer modelo individual sozinho.
7. **O autor reconhece o risco real da prática, sem minimizá-lo** — provedores como Gemini CLI e Claude Code têm mecanismos de detecção de uso não-oficial da ferramenta, podendo bloquear/banir a conta; a recomendação explícita do autor é que essa prática serve para estudo e projetos pessoais de baixo orçamento, não para uso profissional/produção com garantia de continuidade.
8. **Distinção que o autor faz entre "grátis" e "pirata"** — o argumento é que a ferramenta cliente (Claude Code) permanece de uso legítimo/gratuito porque seu "lockin" é apenas exigir uma URL compatível com o formato Anthropic; o proxy não quebra autenticação nem contorna pagamento de um serviço específico, apenas redireciona para modelos de terceiros que o próprio usuário já tem acesso via suas próprias contas — o autor situa isso como "imoral, mas não ilegal", não como pirataria.

## Entidades Mencionadas

- [[wiki/entities/anthropic]] — provider de origem cujo formato de API (Claude Code / Anthropic API) é o "contrato" que o proxy imita para permitir o drop-in replacement.
- [[wiki/entities/claude-code]] — ferramenta cliente usada na demonstração; seu lockin de modelo é o que o esquema descrito contorna.
- [[wiki/entities/hostinger]] — patrocinadora do vídeo; provedora de VPS usada para o deploy "com um clique" do proxy.
- [[wiki/entities/openrouter]] *(nova)* — um dos providers plugáveis no gateway, citado como preferência pessoal do autor.
- [[wiki/entities/google]] — mencionado via Gemini CLI, um dos providers com free tier e com mecanismo de detecção de uso de ferramenta citado.
- [[wiki/entities/openai]] — citado como referência de compatibilidade de API (formato OpenAI, análogo ao formato Anthropic).

## Conceitos Tocados

- [[wiki/concepts/ai-gateway-llm-router]] *(nova)*
- [[wiki/concepts/rotacao-de-contas-free-tier]] *(nova)*
- [[wiki/concepts/roteamento-automatico-de-modelo]]
- [[wiki/concepts/context-window]]
- [[wiki/concepts/vendor-lock-in-cloud]]
- [[wiki/concepts/proxy-pattern]]
- [[wiki/concepts/rate-limiting]]

## Open Questions

- O nome real do produto não pôde ser confirmado — "Nine Router" é a transcrição fonética mais provável do áudio; pode corresponder a um nome grafado de forma diferente pelo fabricante. Marcado explicitamente na nota de rodapé de `raw/rotacao-de-contas-free-tier-llm-router-hostinger.md`. Se uma fonte futura confirmar o nome exato, esta página e a de [[wiki/concepts/ai-gateway-llm-router]] devem ser atualizadas.
- A fonte não detalha o mecanismo técnico da opção "penalize" (o próprio autor admite não entender) — fica como lacuna, sem verificação independente possível a partir desta fonte.
- A conclusão de que o "Token Saver" piorou o consumo é derivada de um único teste anedótico (uma tarefa Ruby on Rails), sem repetição nem controle de variância entre chamadas de modelo — o próprio autor reconhece isso ("pode ser que pro seu caso de uso funcione"). Contraste interessante com o comportamento esperado de técnicas de *prompt/context compression* documentadas em `references/ai/token-economics.md` (skill tech-mentor-ai), que normalmente reduzem, não aumentam, o consumo — hipótese não explorada na fonte é que a compressão de output de comandos (`git diff`, `grep`, `ls`) pode ter interagido mal com o agente, levando-o a re-executar comandos ou re-ler contexto perdido, inflando tokens em vez de economizá-los.
- Não há detalhe de como o proxy detecta que uma conta "esgotou" (rate limit HTTP 429? erro de quota specific?) nem qual é o intervalo de retry entre contas.

## Raw Quotes

> "Eu posso ter três contas do Gemini, posso ter, por exemplo, três contas da Anthropic. E ele tem um esquema que, quando acaba o token de uma, ele joga pra outra; acabou de outra, ele joga pra outra. É praticamente uma disqueteira para nós que somos velhos. E isso não é pirataria, tá? Isso pode ser imoral, mas não é nada ilegal."

> "Enquanto o meu Cloud Code tá conectado no Haiku 4.5, eu mapeei o GLM 5.2, mas eu posso simplesmente mapear com outros modelos."

> "No primeiro resultado gastou... olha isso, olha a quantidade de tokens: 2,2 milhões de tokens de input, 12.800 de output, 2,6 milhões de leitura de cache... para mim, que sou programador Ruby on Rails, isso não funcionou."

> "A gente sabe que o Gemini CLI e o próprio Cloud Code eles têm meio que um detector para saber se você tá usando alguma ferramenta, alguma coisa assim, e acaba bloqueando seu acesso e acaba perdendo conta... na prática, para você que trabalha no dia a dia, eu sendo bem sincero eu não confiaria 100%."
