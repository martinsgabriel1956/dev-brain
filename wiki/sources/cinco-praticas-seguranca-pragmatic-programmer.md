---
type: source
title: "Cinco Práticas de Segurança do Pragmatic Programmer"
aliases: ["cinco práticas segurança", "pragmatic programmer segurança", "segurança para devs"]
date_created: 2026-06-10
date_updated: 2026-06-10
source_count: 0
tags: [security, appsec, attack-surface, least-privilege, secure-defaults, secrets-management, sast, waf, pragmatic-programmer]
skill: tech-mentor-security
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/cinco-praticas-seguranca-pragmatic-programmer.md
source_url: ""
author: "Não identificado — CTO (vídeo YouTube)"
date_published: ""
date_ingested: 2026-06-10
---

# Cinco Práticas de Segurança do Pragmatic Programmer

## TL;DR

Segurança é cultura, não feature. As cinco práticas do Pragmatic Programmer para devs: minimizar superfície de ataque, princípio do menor privilégio, defaults seguros, criptografar dados sensíveis, aplicar updates de segurança rapidamente. Bônus: credenciais nunca no código — sem exceção.

---

## Key Claims

**1. Segurança é responsabilidade de todo dev — não só do time de segurança.**
A última palavra é do especialista, mas segurança começa nas decisões cotidianas: não commitar senha no GitHub, usar MFA, não clicar em phishing.

**2. Minimizar a área de superfície de ataque.**
Complexidade de código, inputs do usuário, endpoints públicos não autenticados, URLs públicas de S3, IDs sequenciais expostos, serviços internos acessíveis — tudo isso é superfície. Reduzir ao mínimo necessário.
→ [[concepts/attack-surface]]

**3. Inputs são vetores de ataque — sanitize sempre.**
O exemplo clássico (Bobby Tables / SQL Injection): um campo de nome que contém `Robert'; DROP TABLE students;--` executado sem sanitização destrói o banco. Todo input do usuário (nome, e-mail, senha, arquivo) deve ser sanitizado.
→ [[concepts/sql-injection]]

**4. URLs públicas de S3 não são seguras porque "ninguém vai adivinhar o ID".**
URLs não são senhas: ficam no histórico do browser, do roteador, em caches de rede. Recursos sensíveis no S3 sempre precisam de autenticação — sem exceção.

**5. IDs sequenciais em endpoints públicos permitem varredura trivial.**
`/api/imagens/123` → troca para 124, 125, 126... A pessoa varre todos os registros sem autenticação. Nunca exponha recursos identificáveis por ID sequencial sem autenticação.

**6. Outputs também são vetores — inclusive o tempo de resposta.**
Logs com dados sensíveis são vulnerabilidade. O exemplo de timing attack: um algoritmo que verifica senha letra a letra tem tempo de resposta proporcional ao número de letras corretas. Com medição de latência é possível descobrir a senha testando 26+26+26 combinações em vez de 26^n.
→ [[concepts/timing-attack]]

**7. Princípio do menor privilégio: permissão exata, nada além.**
Backend com read-only no banco limita o dano mesmo se comprometido. Banco de dados dentro de VPC inacessível de fora. Acesso externo via bastion host.
→ [[concepts/principio-do-menor-privilegio]]

**8. Defaults seguros: o estado padrão deve ser o mais seguro.**
Campo de senha mostra asteriscos por padrão. Deleção de recursos exige confirmação explícita. Onboarding exige troca de senha + 2FA na primeira semana.
→ [[concepts/secure-by-default]]

**9. Criptografar dados sensíveis — nunca inventar criptografia própria.**
PII, dados bancários — use algoritmos estabelecidos e bibliotecas consolidadas.

**10. Aplicar updates de segurança o mais rápido possível.**
Dependabot alerta sobre CVEs em dependências. SAST (ex: SonarQube) detecta padrões vulneráveis no código estaticamente. WAF opera em tempo real na borda.
→ [[concepts/sast]], [[concepts/waf]]

**11. Credenciais jamais no código.**
Se commitou uma credencial: altere-a imediatamente. Use `.env` local (gitignored), `.env.example` para template, e ferramentas de secrets management em produção (GitHub Secrets, AWS Secrets Manager).
→ [[concepts/secrets-management]]

---

## A História "Puramente Fictícia"

Um CTO técnico implementou um sistema com problemas progressivamente piores:
1. `.env` com credenciais de banco commitado na codebase
2. Credenciais hardcoded diretamente no backend em múltiplos pontos
3. Credenciais do banco hardcoded **no frontend**, com requisições diretas ao banco retornando dados no browser do usuário

Resultado: CTO demitido, dev principal promovido a CTO, equipe contratada para reescrever o backend.

---

## Conceitos Centrais

- [[concepts/attack-surface]]
- [[concepts/defense-in-depth]]
- [[concepts/principio-do-menor-privilegio]]
- [[concepts/secure-by-default]]
- [[concepts/sql-injection]]
- [[concepts/timing-attack]]
- [[concepts/sast]]
- [[concepts/waf]]
- [[concepts/secrets-management]]

---

## Questões Abertas

- O source menciona "Pragmatic Programmer" como referência das 5 práticas — vale verificar o capítulo exato (provavelmente cap. "Bend or Break" ou o apêndice de segurança da edição 20th anniversary).
- A distinção entre SAST e DAST não é abordada — apenas SAST é mencionado.

---

## Contradições com o Wiki Existente

Nenhuma contradição. Complementa `attack-surface.md` (já existente) com exemplos concretos: S3 público, IDs sequenciais, outputs como vetores, timing attacks. Complementa `defense-in-depth.md` com a visão do dev cotidiano.
