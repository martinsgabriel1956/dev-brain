---
type: source
title: "CEO da Palantir, o Token Tax e o 'Scam' da IA: Reação à Entrevista com Alex Karp"
aliases: ["palantir ceo token tax", "alex karp cnbc nvidia", "wealth tax token ia", "token maxing sequestra orientação de valor"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 0
tags: [ia, llm, token-economics, finops, palantir, nvidia, harness, tokenizacao, mercado-de-ia, wealth-tax, propriedade-intelectual]
skill: tech-mentor-ai
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/palantir-ceo-token-tax-nvidia-scam-ia.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-07-31
---

# CEO da Palantir, o Token Tax e o "Scam" da IA: Reação à Entrevista com Alex Karp

## TL;DR

Vídeo em português (autor não identificado na transcrição) reage a uma entrevista de ~20 minutos do CEO da [[wiki/entities/palantir-technologies|Palantir]], Alex Karp, na CNBC — nominalmente sobre um novo deal com a [[wiki/entities/nvidia]], mas que a mídia rotulou de "breakdown de nervos televisionado" por virar uma crítica direta ao modelo de cobrança por token da OpenAI e da Anthropic. O autor contextualiza com o caso da [[wiki/entities/xai|xAI]] limitando funcionários a 800 (unidade não especificada na fala) de uso de IA por mês — menos do que o autor afirma gastar pessoalmente — como evidência informal de que o valor prometido pela IA generativa pode não estar se realizando. Extrai três argumentos do "surto" de Karp (imposto/wealth tax sobre tokens, roubo de propriedade intelectual/pesos do negócio, e preço deveria ser sobre valor gerado, não volume de token) e usa o argumento como gancho para explicar por que o custo de IA sobe mesmo com o preço por token caindo (multiplicação via orquestração de agentes/[[wiki/concepts/harness|harness]], troca de harness, e uma mudança de tokenizer no Sonnet 5 da Anthropic) — fechando com quatro recomendações de [[wiki/concepts/finops-para-ia|FinOps]] para times de desenvolvimento em 2026.

## Key Claims

- **xAI limita engenheiros internos a 800 (unidade não especificada) de uso de IA por mês** — Elon Musk teria divulgado essa limitação; o autor destaca a ironia de uma empresa com data centers e modelos próprios ainda assim limitar o consumo interno, e afirma gastar pessoalmente mais do que esse valor. → [[wiki/entities/xai]], [[wiki/entities/elon-musk]]
  - **Confiança: baixa.** A transcrição não especifica se "200" e depois "800" são dólares, créditos ou requisições, nem cita a fonte primária (post do Musk) — tratar como paráfrase de segunda mão, não citação verificada.
- **Alex Karp (CEO da Palantir) deu uma entrevista de ~20 min à CNBC sobre um deal com a Nvidia que a mídia chamou de "breakdown de nervos televisionado"** — a entrevista nominalmente corporativa (parceria Palantir-Nvidia) foi dominada por críticas ao modelo de negócio da OpenAI e da Anthropic. → [[wiki/entities/palantir-technologies]], [[wiki/entities/nvidia]]
  - **Confiança: média.** O autor admite explicitamente não ter assistido à entrevista completa, apenas a um corte de 7min50; claims sobre o conteúdo vêm desse corte, não da fonte primária integral.
- **Três argumentos centrais de Karp contra a cobrança por token**: (1) chamar o custo de token de "wealth tax that does not help the poor, it just punishes" — o consumo cresce sem controle e quem paga é o cliente final; (2) treinar em cima dos workflows/dados do cliente equivale a "roubar os pesos e os alfas do negócio" — o cliente banca o treinamento do produto que pode virar concorrência; (3) se o valor gerado é tão alto quanto anunciado, a cobrança racional seria um percentual do valor gerado (ex.: 10-30% de 1 bilhão de dólares de valor), não por volume de token. → [[wiki/concepts/corrida-preco-qualidade-llm]], [[wiki/concepts/token-maxing]]
- **Sam Altman teria sugerido publicamente (no Twitter/X) que criadores deveriam reservar um percentual do valor criado com IA para devolver aos laboratórios** — citado pelo autor como eco do mesmo racional de "cobrar por resultado, não por token" que Karp defende, ainda que vindo do lado oposto do debate. → [[wiki/entities/openai]]
  - **Confiança: baixa.** Não há link ou citação literal do tweet na fonte; tratar como paráfrase.
- **A Palantir publicou (via post/relatório citado pelo autor) uma crítica direta ao "token maxing"**: "Maximização de tokens sequestra sua orientação de valor e diminui sua força e inteligência institucional [...] há um motivo pelo qual aqueles que vendem tokens se recusam a cobrar com base em valor." Reforça e cita quase literalmente a mesma crítica já registrada em [[wiki/concepts/token-maxing]] via [[wiki/sources/custo-real-ia-tokens-produtividade-demissoes]], mas com uma frase adicional não presente na fonte anterior. → [[wiki/concepts/token-maxing]]
- **Custo por token caiu desde 2022, mas o gasto total sobe** — a explicação central do vídeo para esse paradoxo aparente é que a orquestração de agentes (o [[wiki/concepts/harness|harness]] por trás) multiplica "dezenas de vezes" o volume de tokens consumidos por tarefa, mesmo com preço unitário em queda e qualidade em alta.
- **Troca de harness (Claude Code → OpenCode) motivada por loops de correção supérfluos** — o autor cita devs migrando do Claude Code para o [[wiki/entities/opencode|OpenCode]] alegando que o primeiro entra em loops de "encontrei um bug suspeito → sugere correção → escreve testes → reescreve o código → reescreve os testes", consumindo token sem necessariamente agregar valor proporcional. → [[wiki/concepts/harness]]
  - **Confiança: baixa.** Anedota de comportamento de produto sem link para relato original ou métricas — tratar como impressão de usuário, não benchmark.
- **A Anthropic teria mudado o tokenizer no Sonnet 5** — citado pelo autor como uma das razões pelas quais fica impossível "fechar a conta" do custo real: o preço por token cai, mas a mesma tarefa passa a gerar mais tokens no novo tokenizer, neutralizando parte da economia nominal. → [[wiki/entities/anthropic]]
  - **Confiança: baixa.** Claim não verificado nesta fonte nem cruzado com documentação oficial da Anthropic; a wiki já documenta um fenômeno relacionado mas distinto — o [[wiki/concepts/token-tax-multilingual|token tax multilíngue]] do BPE da Anthropic — que não é a mesma coisa que uma mudança de versão de tokenizer entre modelos. Vale verificação futura com changelog oficial do Sonnet 5.
- **O recurso "By The Way" do Claude Code é citado como sintoma do mesmo problema** — útil para recuperar contexto perdido ao alternar entre múltiplos agentes em paralelo (o autor cita rodar até 8 agentes simultâneos), mas seu próprio uso consome tokens adicionais só para reconstruir o que já deveria estar retido. → [[wiki/entities/claude-code]]
- **Nvidia é tratada como a única parte "correta" nessa dinâmica de mercado** — vende hardware, não custeia os dados do cliente, não retreina modelos em cima do workflow do cliente, e (segundo o autor) provavelmente não cobra por resultado — contraste direto com o argumento de Karp contra OpenAI/Anthropic. → [[wiki/entities/nvidia]]
- **O produto que a Palantir estaria moldando: modelo aberto (open weight, sob controle da própria empresa) + camada de aplicação + compute Nvidia** — ao invés de vender acesso a modelo e deixar o cliente construir e hospedar a aplicação, a Palantir venderia a aplicação pronta e cobraria um percentual do valor entregue. → [[wiki/entities/palantir-technologies]], [[wiki/concepts/camada-de-aplicacao-vs-modelo]]
- **Quatro recomendações de FinOps para devs/times em 2026**: (1) definir budgets de uso de IA por dev/ferramenta/semana/mês com ferramentas de monitoramento de consumo de token e custo de cloud (caso Uber citado como erro por ausência desse controle); (2) medir por métricas de valor (bugs em produção, crash-free sessions, frequência de deploy, tickets atrasados) em vez de dashboards de volume de token; (3) classificar dados por sensibilidade — dado de cliente/estratégico deveria rodar em modelo aberto self-hosted, commodity pode ir para API; (4) para quem prototipa produtos próprios, usar qualquer API livremente na fase de protótipo mas evitar lock-in estrutural em um único provedor de modelo frontier. → [[wiki/concepts/finops-para-ia]]
- **Leitura de mercado do autor por ano**: 2025 foi o ano de adotar IA a qualquer custo; 2026 é o ano da fatura desse custo chegando; 2027 será o ano de focar em finanças, budget, métricas e ownership de infraestrutura de IA.

## Entities

[[wiki/entities/palantir-technologies]] · [[wiki/entities/nvidia]] · [[wiki/entities/xai]] · [[wiki/entities/elon-musk]] · [[wiki/entities/openai]] · [[wiki/entities/anthropic]] · [[wiki/entities/claude-code]] · [[wiki/entities/opencode]] · [[wiki/entities/uber]] · [[wiki/entities/microsoft]] · [[wiki/entities/meta]]

## Concepts

[[wiki/concepts/token-maxing]] · [[wiki/concepts/corrida-preco-qualidade-llm]] · [[wiki/concepts/harness]] · [[wiki/concepts/finops-para-ia]] · [[wiki/concepts/modelo-por-leverage-tarefa]] · [[wiki/concepts/camada-de-aplicacao-vs-modelo]] · [[wiki/concepts/token-tax-multilingual]] · [[wiki/concepts/tokenizacao]]

## Open Questions

- Autoria do vídeo não identificada na transcrição (nenhum nome próprio citado pelo autor sobre si mesmo) — estilo de fala e formato (reação a entrevista + patrocínio de plataforma de pagamento + dicas práticas ao final) é consistente com outros canais brasileiros de tecnologia já presentes na wiki, mas sem confirmação cruzada não deve ser atribuído a um autor específico.
- A unidade do limite de uso da xAI ("200" depois "800" por mês) não é especificada na fala — pode ser dólares, créditos internos ou requisições; tratar como não verificado até confirmação de fonte primária (post do Musk).
- A entrevista de Alex Karp na CNBC não foi assistida na íntegra pelo autor do vídeo (apenas um corte de ~8 minutos de 20) — os três argumentos extraídos (wealth tax, roubo de propriedade intelectual, preço por valor) são uma leitura do corte, não da entrevista completa; vale ingestão futura da entrevista primária se disponível.
- Claim de que a Anthropic mudou o tokenizer no Sonnet 5 não tem confirmação cruzada com documentação oficial ou changelog da Anthropic nesta fonte nem em fontes anteriores da wiki — a wiki documenta um fenômeno relacionado mas distinto ([[wiki/concepts/token-tax-multilingual]]); não assumir que são a mesma coisa.
- O segmento de patrocínio (Amax, plataforma de pagamentos) é um ad-read genérico sobre antifraude/recuperação de carrinho/split de pagamento — sem relação direta com o domínio de IA/LLM do restante do vídeo; não foram criadas páginas de entidade para o patrocinador por não ser central ao tema técnico da fonte.
- Citação atribuída a Sam Altman sobre "reservar percentual do valor criado com IA para os laboratórios" não tem link ou citação literal na transcrição — tratar como paráfrase de segunda mão até confirmação.

## Raw Quotes

> "Maximização de tokens sequestra sua orientação de valor e diminui sua força e inteligência institucional [...] há um motivo pelo qual aqueles que vendem tokens se recusam a cobrar com base em valor." — citado como post/relatório da Palantir

> "That [is] literally against my own interest [to] call [it] out — I'm right." — Alex Karp, CEO da Palantir, à CNBC

> "You could do this with a closed model too, but then the clients have to be able to ask and answer very basic questions: are you keeping the data, are you going to enter our business, what happens in the classified context — when the Department of War goes to you and says 'I need this application'..." — Alex Karp

> "2025 foi o ano de adotar IA a qualquer custo. 2026 é o ano que a fatura tá chegando desse custo. 2027 vai ser o ano da gente olhar pra nossa operação e pensar nas finanças, pensar em budget, pensar em métricas e pensar em ownership."

*(Texto completo em `raw/palantir-ceo-token-tax-nvidia-scam-ia.md`.)*
