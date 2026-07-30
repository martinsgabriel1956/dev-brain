---
type: source
title: "Mitos e Fable 5: os modelos de IA bloqueados pelo governo dos EUA por poder de cybersegurança"
aliases: ["mitos anthropic", "fable 5 bloqueio", "projeto glasswing", "mitos vs fable 5", "bloqueio governo eua ia cyberseguranca"]
date_created: 2026-07-24
date_updated: 2026-07-29
source_count: 1
tags: [ai-safety, cybersegurança, anthropic, red-teaming, jailbreak, export-controls, china, japao, nsa, vulnerabilidades, ai-red-teaming]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/mitos-fable-5-bloqueio-governo-eua-cyberseguranca.md
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: 2026-07-24
---

## TL;DR

Vídeo (Código Fonte TV) sobre uma nova classe de modelos de IA especializados em cybersegurança — "Mitos" e "Fable 5" da Anthropic, e o GPT 5.6 da OpenAI — capazes de encontrar vulnerabilidades de software em escala tão alta (dezenas de anos de idade, em núcleo de SO, bibliotecas críticas) que o governo dos EUA decidiu bloquear o acesso público a esses modelos, temendo tanto o uso ofensivo quanto o vazamento de capacidade estratégica para fora dos EUA. A Anthropic restringiu o Mitos a um consórcio fechado (projeto Glasswing, ~150 organizações em 15 países), mas mesmo com salvaguardas o Fable 5 foi jailbreakeado em centenas de tentativas por pesquisadores independentes. Em paralelo, Japão (Sakana AI/Fugo) e China (360/Tulong Fang, Zhipu AI/GLM 5.2) já afirmam ter capacidade equivalente, sinalizando que a vantagem de "só os EUA têm isso" pode ser temporária — o que levanta a questão de países como o Brasil não terem acesso a ferramentas equivalentes de defesa.

## Key Claims

1. **Mitos (Anthropic, anunciado abril de 2026) é descrito no próprio preview card como um modelo de IA "extremamente avançado" em segurança e programação, com "preocupações suficientes para não ser lançado ao público em geral"** — treinado em três etapas: pré-treinamento em larga escala, fine-tuning com feedback humano, e alinhamento de segurança inspirado na abordagem da Anthropic (regras explícitas + redução de respostas perigosas). Avaliação inclui red teaming, avaliação de segurança/utilidade e testes específicos de cybersegurança — metodologia descrita como "mais rigorosa" que versões anteriores, mas não claramente diferenciada, na fonte, do que outras empresas (ex.: OpenAI) já fazem.
2. **Projeto Glasswing: acesso ao Mitos restrito a um consórcio fechado**, inicialmente ~50 parceiros (AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JP Morgan, Linux Foundation, Microsoft, Nvidia, entre outras), ampliado no início de junho de 2026 para ~150 organizações em 15 países. A Mozilla, mesmo fora do consórcio oficial, usou o Mitos para corrigir bugs no Firefox.
3. **Escala de vulnerabilidades encontradas pelo Mitos**: uma falha de 27 anos no OpenBSD (permitia travar o sistema remotamente com uma única conexão), uma falha de 16 anos no FFmpeg, múltiplas brechas no núcleo do Linux, e mais de 10.000 falhas de gravidade alta/crítica reportadas pelos parceiros do Glasswing — números descritos como recorde histórico para uma única ferramenta.
4. **Mitos nunca foi liberado ao público geral, mas ficou famoso apenas por reputação** — a maioria das pessoas que fala sobre ele nunca teve acesso direto. Há relatos (não verificados de forma independente na fonte) de acesso indevido via credenciais vazadas relacionadas ao Mitos preview.
5. **Fable 5 (Anthropic, lançado 5 de junho de 2026) e Mitos 5 sofreram bloqueio formal do governo americano**: Mitos 5 bloqueado totalmente; Fable 5 bloqueado para não-americanos e empresas não-americanas, incluindo funcionários não-americanos da própria Anthropic. Fable 5 tem salvaguardas reforçadas para exploração de vulnerabilidades, biologia, química e técnicas de destilação de modelo.
6. **Jailbreak do Fable 5 documentado por terceiros**: um laboratório de IA italiano realizou 7.828 tentativas de jailbreak no Fable 5 e no Opus (modelo anterior da Anthropic); no Fable 5, conseguiram ultrapassar as salvaguardas em 702 tentativas — evidência citada na fonte de que guardrails de segurança, mesmo reforçados, não são impenetráveis.
7. **Motivação do bloqueio governamental, segundo a fonte**: a NSA identificou que sistemas confidenciais americanos foram comprometidos "em questão de horas", não semanas, usando esses modelos. O senador Mark Warner (citado na fonte) declarou publicamente que a ferramenta "invadiu quase todos os nossos sistemas classificados... não em semanas, mas em horas".
8. **O padrão de bloqueio se estende a qualquer empresa que lance capacidade equivalente dentro dos EUA**: o GPT 5.6 da OpenAI, lançado em preview em 26 de junho de 2026, também foi bloqueado para acesso público antes mesmo de ampla divulgação — sugerindo uma política de bloqueio por categoria de capacidade, não específica de uma empresa.
9. **Outros países já reivindicam capacidade equivalente**, sugerindo que a vantagem americana pode não ser exclusiva por muito tempo:
   - Japão — **Sakana AI** lançou o **Fugo**, um "pool" de outros modelos (não um modelo próprio treinado do zero) combinando modelos abertos e fechados; em benchmarks internos (da própria Sakana AI e de um laboratório parceiro), superou o Fable 5 e alguns benchmarks do Mitos preview.
   - China — **360** (gigante de segurança cibernética sediada em Pequim) lançou o **Tulong Fang**, um modelo de IA projetado explicitamente para "enfrentar o Mitos da Anthropic", digitalizando e descobrindo vulnerabilidades de software automaticamente.
   - China — **Zhipu AI** lançou o **GLM 5.2**, também posicionado para competir diretamente com o Mitos.
10. **Assimetria geopolítica levantada pela fonte**: países sem modelo próprio de cybersegurança nesse nível (o exemplo citado é o Brasil) não têm hoje acesso a uma ferramenta equivalente ao Mitos 5 para proteger os próprios sistemas — ao mesmo tempo em que outros países já constroem essa capacidade, que pode servir tanto para defesa quanto como arma ofensiva.
11. **Janela temporal do evento**: toda essa escalada (do preview do Mitos ao bloqueio de Fable 5, Mitos 5 e GPT 5.6, mais o surgimento de concorrentes no Japão e na China) aconteceu em menos de 3 meses — do anúncio do Mitos em abril de 2026 até o momento da gravação do vídeo.

## Entidades e Conceitos Tocados

- [[wiki/entities/anthropic]]
- [[wiki/concepts/modelo-frontier]]
- [[wiki/sources/ai-llm-security]]
- [[wiki/sources/ai-safety-guardrails]]
- [[wiki/sources/pentest-redteam]]
- [[wiki/sources/bug-bounty]]
- [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]
- [[wiki/concepts/compliance]]
- [[wiki/entities/sakana-ai]]

## Contradições / Reforços com o Resto da Wiki

**Reforço direto:** [[wiki/sources/ai-safety-guardrails]] já registrava que jailbreak e guardrails são um jogo de gato-e-rato estrutural (nunca 100% robusto); a evidência quantitativa desta fonte (702 sucessos em 7.828 tentativas no Fable 5) é o dado empírico mais concreto que a wiki tem até agora sobre a taxa de sucesso de jailbreak em um modelo frontier específico.

**Reforço direto:** [[wiki/sources/kimi-k3-china-mercado-ia-open-source]] já discutia a tese de que a vantagem americana em IA não é permanente e que a China está fechando a distância rapidamente — esta fonte adiciona um ângulo novo e mais específico: a corrida não é só em capacidade geral de modelo, mas especificamente em cybersegurança ofensiva/defensiva, com Japão entrando também na disputa (Sakana AI), o que a fonte anterior não cobria.

**Novo ângulo não coberto antes:** nenhuma fonte da wiki registrava até agora o padrão de **bloqueio governamental de acesso a modelos de IA por risco de cybersegurança nacional** (Mitos 5, Fable 5, GPT 5.6) — isso é distinto de export controls de hardware (já coberto em [[wiki/sources/kimi-k3-china-mercado-ia-open-source]]) e merece ser tratado como um mecanismo de política pública novo e específico para modelos de "dual-use" em segurança ofensiva.

**Continuação posterior:** [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] mostra o **GLM 5.2** (aqui citado como concorrente chinês do Mitos, via Zhipu AI) do lado defensivo — supostamente hospedado internamente pela própria OpenAI, sem guardrails, para investigar um incidente real depois que modelos com guardrail padrão se recusaram a ajudar. Reforça o tema desta fonte de que a capacidade de cybersegurança de ponta não fica confinada a um único laboratório ou país.

## Open Questions

- Os nomes "Mitos" e "Fable 5" não correspondem a nomenclatura pública confirmada de produtos da Anthropic conhecida até o momento da ingestão — a transcrição é de áudio-para-texto automático e pode conter erros de transcrição sobre o nome real dos modelos/projetos citados (ex.: possível confusão com codinomes internos ou nomes foneticamente parecidos). Tratar os nomes citados como não verificados externamente.
- Números específicos (10.000+ falhas encontradas, 7.828 tentativas de jailbreak, 702 sucessos, 150 organizações em 15 países) vêm de citação de fala no vídeo, sem link para a fonte primária (paper, press release, ou estudo do laboratório italiano) — não verificados de forma independente nesta ingestão.
- Não fica claro na fonte se o bloqueio a não-americanos dentro da própria Anthropic é uma política formal documentada publicamente ou uma descrição de segunda mão do apresentador do vídeo.
- O nome completo do "laboratório de IA da Itália" que testou jailbreak no Fable 5 e no Opus não foi citado na fonte — não é possível linkar a uma entidade específica.
