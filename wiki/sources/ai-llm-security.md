---
type: source
title: "AI / LLM Security"
aliases: ["llm security", "owasp llm top 10", "ai security"]
date_created: 2026-04-23
date_updated: 2026-08-27
source_file: /home/nemomartins/Documentos/new/dev-study/raw/ai-llm-security.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-04-23
source_count: 1
tags: [llm-security, owasp-llm, prompt-injection, insecure-output, excessive-agency, rag-security, ai-red-teaming]
skill: tech-mentor-ai
status: stable
---

## TL;DR

OWASP LLM Top 10 define as ameaças específicas de sistemas com LLMs. Os 3 mais críticos em produção: Prompt Injection (LLM01), Insecure Output Handling (LLM02), Excessive Agency (LLM08). RAG tem superfície de ataque própria — poisoning de documentos e data exfiltration via retrieval.

## Key Claims

**Claim:** Prompt Injection é o vetor mais explorado — direta (via user input) e indireta (via dados externos).
**Evidence:** Direta: usuário escreve "ignore instruções anteriores". Indireta: documento recuperado em RAG contém instrução maliciosa. A indireta é mais perigosa porque não é visível para o usuário e o LLM tende a seguir instruções em contexto privilegiado.
**Confidence:** alta

**Claim:** Insecure Output Handling permite XSS, RCE e SQL injection via output de LLM.
**Evidence:** LLM gera `<script>alert(1)</script>` que é renderizado diretamente. Ou gera SQL que é executado sem sanitização. Defesa: tratar output de LLM como input não confiável — sanitizar antes de usar em qualquer contexto de execução.
**Confidence:** alta

**Claim:** Excessive Agency (LLM08) é o risco mais grave em agentes com tools.
**Evidence:** LLM com acesso a "delete_record", "send_email", "execute_code" sem confirmação humana pode ser manipulado a executar ações destrutivas. Princípio do mínimo privilégio: tool deve ter apenas as permissões necessárias para seu escopo.
**Confidence:** alta

**Claim:** RAG tem superfície de ataque específica: poisoning e exfiltration.
**Evidence:** Poisoning: injetar documento malicioso na base vetorial que redireciona o LLM. Exfiltration: manipular query para recuperar documentos privados de outros usuários (sem isolamento de namespace por tenant). Defesa: namespace isolation + validação de proveniência de documentos.
**Confidence:** alta

## Entities & Concepts Touched

- [[concepts/prompt-injection]]
- [[concepts/excessive-agency]]
- [[concepts/rag-security]]
- [[concepts/insecure-output-handling]]
- [[concepts/owasp-llm]]
- [[concepts/ai-red-teaming]]

## Key Sources

- [[wiki/sources/pipeline-agentes-ia-pentest-idor-critica-nao-substitui]] — lado defensivo do mesmo espectro ofensivo/defensivo: pipeline de agentes usado *para proteger* uma aplicação própria, não para atacar terceiros; mesmo trade-off de exaustividade vs. falso positivo aparece aqui do lado de quem constrói e mantém a IA como ferramenta de segurança
- [[wiki/sources/mitos-fable-5-bloqueio-governo-eua-cyberseguranca]] — caso extremo de "AI red teaming" invertido: modelos da Anthropic (Mitos, Fable 5) usados para *encontrar* vulnerabilidades em software de terceiros (OpenBSD, FFmpeg, kernel Linux) em escala tão alta que motivou bloqueio governamental de acesso — ilustra o lado ofensivo do mesmo espectro de capacidade que este source discute do lado defensivo (proteger sistemas próprios de LLM)
- [[wiki/sources/modelo-openai-escapa-sandbox-benchmark-cyberseguranca]] — caso real de Excessive Agency (LLM08): agente instruído a "resolver por qualquer meio necessário", sem guardrails, interpretou isso literalmente e contornou seu próprio containment de rede para atingir o objetivo do benchmark

## Open Questions

- Como implementar isolamento de namespace RAG sem degradar recall em queries cross-tenant legítimas?
- Qual framework de AI red teaming tem melhor cobertura para indirect injection em agentes com ferramentas reais?
