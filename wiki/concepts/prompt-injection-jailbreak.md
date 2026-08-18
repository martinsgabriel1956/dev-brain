---
type: concept
title: "Prompt Injection vs. Jailbreak"
aliases: ["prompt injection", "jailbreak", "jailbreaking", "owasp top 10 llm"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [seguranca, prompt-injection, jailbreak, owasp, llm-security, guardrails]
skill: tech-mentor-security
status: stub
---

# Prompt Injection vs. Jailbreak

Duas classes de ataque frequentemente confundidas em segurança de LLM:

- **Jailbreak** — sugestionar a IA a se comportar fora do esperado pelo dono do sistema (tom, personagem, conteúdo). Exemplo: um usuário força a IA a responder sempre "como uma galinha", ou a produzir discurso de ódio, e depois alega ter sido "atendido" daquela forma por uma empresa. O dano é de imagem/comportamento, não necessariamente de dados.
- **Prompt injection** — ataque mais grave: consegue extrair dados sensíveis do contexto do agente e/ou fazer a IA executar operações destrutivas dentro do sistema (ex.: comandos, chamadas de tool com efeito colateral), comprometendo segurança da aplicação, servidores e infraestrutura.

## Mitigações

- **[[wiki/concepts/ai-safety-guardrails|Guardrails]]** — validação antes e depois de cada chamada ao agente, e antes e depois de cada chamada de tool.
- **Isolamento entre agentes** — numa pipeline multiagente, impedir que contexto contaminado por injection num agente se propague para os demais (ver [[wiki/concepts/design-patterns-ia]]).
- **[[wiki/concepts/agent-containment|Agent Containment]]** — sandboxing como última linha de defesa quando input/output filters falham.
- **Proteção de dados sensíveis** — ofuscação de dados antes de entrarem no pipeline de IA, especialmente relevante na camada de observabilidade (logs não devem gravar dados sensíveis crus).

## OWASP Top 10 para LLM e IA Generativa

Assim como existe o OWASP Top 10 tradicional para aplicações web, existe uma versão específica para LLM/IA Generativa, cobrindo as principais falhas de segurança a observar ao desenvolver agentes e aplicações com IA (prompt injection costuma liderar essa lista).

## Relação com Outros Conceitos

- [[wiki/concepts/alucinacao-llm]] — falha de qualidade/confiabilidade, categoria distinta de ataque intencional, mas frequentemente listada ao lado de prompt injection em frameworks de risco de LLM.
- [[wiki/concepts/secrets-management]] — prompt injection bem-sucedida pode ser o vetor de exfiltração de segredos que o agente tinha acesso legítimo para ler.

## Key Sources

- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — distinção jailbreak vs. prompt injection, guardrails, proteção de dados sensíveis e OWASP Top 10 LLM
