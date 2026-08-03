---
type: source
title: "Vibe coding, .env exposto, IDOR, account takeover e RCE numa loja feita com IA"
aliases: ["loja do lucas pentest", "env exposto idor account takeover rce", "geraldo alcantara loja ia"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia.md
source_url: ""
author: "Geraldo Alcântara"
date_published: ""
date_ingested: 2026-07-31
source_count: 0
tags: [pentest, appsec, vibe-coding, idor, account-takeover, secrets-management, rce, upload-arbitrario, attack-surface, owasp, dirsearch, burp-suite]
skill: tech-mentor-security
status: stable
---

# Vibe coding, .env exposto, IDOR, account takeover e RCE numa loja feita com IA

## TL;DR

Vídeo educacional (ambiente de laboratório controlado, autorizado) de Geraldo Alcântara, pentester, demonstrando uma cadeia completa de ataque contra uma loja fictícia ("Lucas") construída inteiramente com ferramentas de vibe coding (Cursor, Lovable, Claude Code). A partir de um único `.env` exposto publicamente — encontrado via brute force de diretórios com dirsearch —, a cadeia percorre: credenciais vazadas → login → IDOR em pedidos (dados de outros clientes) → IDOR no perfil expondo uma "chave de integração" → account takeover completo via essa chave (sem senha) → escalonamento a admin por enumeração de IDs sequenciais no Burp Intruder → RCE via upload de plugin malicioso sem validação. Todo o processo levou menos de 10 minutos. Fecha com cinco recomendações de mitigação.

## Key Claims

- **Vulnerabilidades em código gerado por IA são mensuráveis e crescentes.** Citando pesquisa (não detalhada pela fonte além do número): 35 CVEs em código gerado por IA só em março, mais que a soma dos 7 meses anteriores; segundo a Veracode, 45% das amostras de código gerado por IA carregam vulnerabilidades do OWASP Top 10. [external: números citados de cabeça na fala, sem link — Veracode publica relatórios anuais "State of Software Security" com esse tipo de estatística, mas a fonte não fornece a citação exata]. → [[wiki/concepts/vibe-coding]]
- **`.env` publicamente acessível é o ponto de entrada de toda a cadeia.** Encontrado com dirsearch (brute force de diretórios/arquivos comuns), sem nenhuma autenticação exigida. Continha secret key, chaves do Stripe e um usuário de teste esquecido em produção. → [[wiki/concepts/secrets-management]], [[wiki/concepts/attack-surface]]
- **IDOR em pedidos:** ID sequencial e simples na URL do pedido permite acessar dados de outro cliente (nome, e-mail, endereço, token de download) sem checagem de ownership. → [[wiki/concepts/idor]]
- **IDOR no perfil como vetor de account takeover:** o ID do perfil na URL também é sequencial; trocar o ID expõe o perfil (e a "chave de integração") de outro usuário. Essa chave, sozinha, autentica via `POST /api/login` e gera um cookie de sessão válido — sem senha, sem MFA, sem verificação adicional. Login completo como outro usuário. → [[wiki/concepts/idor]], [[wiki/concepts/account-takeover]]
- **Escalonamento a admin via enumeração automatizada de IDs.** Em vez de repetir manualmente, a checagem é escalada com o Burp Intruder: payload numérico de 1 a 15 no ID do perfil, com "Grep - Extract" capturando o campo `role` de cada resposta. Um ID sem `role: user` revela o perfil do dono da loja com `role: admin` — cuja chave de integração gera um cookie de sessão de administrador. → [[wiki/concepts/idor]], [[wiki/concepts/attack-surface]]
- **RCE via upload de plugin sem validação.** O painel admin permite instalar plugins via upload de arquivo próprio; a ausência de validação de tipo/conteúdo do arquivo permite executar comandos arbitrários no servidor (confirmado com `ls`, `pwd`, leitura de `/etc/passwd`). → [[wiki/concepts/upload-arbitrario-rce]]
- **Cinco mitigações recomendadas:** (1) bloquear acesso a qualquer arquivo iniciado por ponto no servidor; (2) toda leitura de recurso por ID deve verificar ownership contra a sessão ativa, nunca confiar no ID da requisição; (3) upload restrito — validar MIME type no backend, restringir extensões, salvar fora de diretórios públicos, nunca executar dinamicamente arquivo de usuário; (4) ter um dev ou alguém de segurança envolvido no processo de vibe coding, complementado por scanners (ex. OWASP ZAP) e análise estática; (5) nunca commitar credenciais — `.gitignore` desde o primeiro commit. → [[wiki/concepts/secrets-management]], [[wiki/concepts/idor]], [[wiki/concepts/upload-arbitrario-rce]], [[wiki/concepts/hardening-de-servidor]]

## Entities

[[wiki/entities/geraldo-alcantara]] · [[wiki/entities/claude-code]]

## Concepts

[[wiki/concepts/idor]] · [[wiki/concepts/secrets-management]] · [[wiki/concepts/attack-surface]] · [[wiki/concepts/vibe-coding]] · [[wiki/concepts/account-takeover]] · [[wiki/concepts/upload-arbitrario-rce]] · [[wiki/concepts/hardening-de-servidor]] · [[wiki/concepts/autenticacao-e-autorizacao]]

## Conexão com fontes existentes

Complementa diretamente [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] e [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]], que já cobrem IDOR/BOLA, exposição de dados e confiar no frontend — mas de um ângulo distinto: aquelas são relato de processo (dev não-especialista usando IA para testar o próprio sistema) e aula didática, enquanto esta é uma demonstração ofensiva completa, de fora para dentro, contra um sistema construído (não apenas descrito) via vibe coding, encadeando várias falhas pequenas — cada uma isoladamente banal — numa tomada de controle total do servidor. É a primeira fonte da wiki a introduzir account takeover via reuso de credencial de API como cookie de sessão, escalonamento de privilégio por enumeração automatizada de IDs no Burp Intruder, e RCE via upload de plugin administrativo sem validação.

## Open Questions

- **Números de CVE e da Veracode citados sem fonte primária.** A fala menciona "pesquisadores" e "a Veracode" sem nomear o relatório ou vincular a página — não é possível verificar a cifra exata (35 CVEs em março, 45% das amostras) a partir desta fonte isoladamente.
- **Stack técnica da loja fictícia não detalhada.** O vídeo não especifica linguagem/framework do backend, nem como o endpoint `/api/login` valida a chave de integração internamente — não fica claro se a falha é "qualquer chave válida gera cookie sem checar mais nada" ou algo mais específico.
- **Nenhuma menção a rate limiting nas rotas exploradas.** A enumeração via Burp Intruder (15 requisições sequenciais) não encontrou nenhum bloqueio — mas o vídeo não afirma explicitamente a ausência de rate limiting, apenas não a menciona como obstáculo.

## Raw Quotes

Nenhuma citação literal preservada nesta fonte — o conteúdo foi reorganizado em prosa descritiva a partir da transcrição bruta (ver `raw/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia.md`), evitando reprodução extensa e literal do roteiro do vídeo.
