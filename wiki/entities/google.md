---
type: entity
title: "Google"
aliases: ["Google DeepMind", "Gemini"]
date_created: 2026-07-03
date_updated: 2026-08-13
source_count: 5
tags: [google, gemini, llm, storage, organização]
skill: tech-mentor-ai
status: stub
---

## Quem É

Empresa de tecnologia, criadora da família de modelos **Gemini** (ex.: Gemini 2.0 Flash Lite) e do harness AntiGravity. Concorrente direta da [[entities/anthropic]] e da [[entities/openai]] no mercado de LLMs, com tokenizer e vocabulário próprios — o mesmo prompt gera contagens de tokens diferentes das dos outros provedores. Ver [[tokenizacao]].

---

## Gemini Flash como Referência de Velocidade

[[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] cita o **Gemini 3.5 Flash** como exemplo de modelo otimizado para o eixo de velocidade em [[wiki/concepts/modelo-por-leverage-tarefa]] — pontuação 70 no coding index do [[wiki/entities/artificial-analysis|Artificial Analysis]], recomendado para tarefas simples e urgentes (ex.: bug fix rápido) em vez dos modelos de fronteira (Fable, Sol), mais lentos.

## Gemini CLI e Detecção de Uso Não-Oficial de Ferramenta

[[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] cita o Gemini CLI (junto com o Claude Code) como tendo um mecanismo de detecção de uso da ferramenta fora do padrão esperado, que pode bloquear/banir a conta — citado como o principal risco prático de [[wiki/concepts/rotacao-de-contas-free-tier|rotacionar múltiplas contas free tier]] do Gemini atrás de um AI Gateway.

## Membro Fundador da OpenID Foundation (2007) e Adotante do OIDC

Google, junto com Yahoo, Facebook e AOL, fundou em 2007 a OpenID Foundation, criada para padronizar o ecossistema caótico e incompatível do protocolo [[wiki/concepts/openid-legado|OpenID original]]. Anos depois, é citada como uma das big techs (junto com Microsoft e Apple) que adotaram em massa o [[wiki/concepts/openid-connect|OpenID Connect]], tornando-o base de praticamente todo botão de login social ("Entrar com Google"). Ver [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]].

## Google Drive como Exemplo de Armazenamento em Nuvem

Citada (ao lado de Dropbox e iCloud) como serviço de nuvem de referência em [[wiki/sources/tipos-de-armazenamento-de-dados]]: arquivos ficam em servidores remotos, criptografados e **duplicados em vários data centers** — geo-redundância que sobrevive à falha de um centro inteiro. Trade-off: espaço grande exige assinatura. Contraste com o [[wiki/concepts/nas-network-attached-storage|NAS]], em que o hardware é do próprio usuário.

## Key Sources

- [[wiki/sources/tokens-llm-fundamentos-typescript]]
- [[wiki/sources/tipos-de-armazenamento-de-dados]] — Google Drive como exemplo de nuvem com geo-redundância
- [[wiki/sources/openid-connect-oidc-autenticacao-alem-do-oauth]] — membro fundador da OpenID Foundation (2007); adotante em massa do OpenID Connect
- [[wiki/sources/gestao-de-custo-velocidade-modelos-de-ia-fable-sol]] — Gemini 3.5 Flash como modelo de referência para tarefas que exigem velocidade
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — Gemini CLI citado como um dos providers com detecção de uso não-oficial e risco de banimento por rotação de contas free tier
