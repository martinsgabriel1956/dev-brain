---
type: concept
title: "Rate Limiting"
aliases: ["throttling", "rate limit", "token bucket", "sliding window"]
date_created: 2026-04-23
date_updated: 2026-10-05
source_count: 16
tags: [rate-limiting, token-bucket, sliding-window, redis, throttling, protecao-api, gatekeeper, attack-surface]
skill: tech-mentor-backend
status: stub
---

# Rate Limiting

Mecanismo de controle que limita a frequência de requests para proteger APIs de abuso e sobrecarga.

**Quatro algoritmos:**
| Algoritmo | Precisão | Memória | Bursts |
|---|---|---|---|
| Fixed Window | Média — boundary burst | O(1) | Sim |
| Token Bucket | Alta | O(1) | Controlado |
| Sliding Window Log | Exata | O(N) | Não |
| Sliding Window Counter | ~90% | O(1) | Não |

**Escolha padrão:** Sliding Window Counter para APIs gerais. Token Bucket quando bursts controlados são desejados (upload em lote).

**Implementação:** Redis + Lua script (atomicidade). Hierarquia: global → por IP → por usuário → por endpoint.

## Dimensão de Segurança

Rate limiting é também responsabilidade do [[wiki/concepts/gatekeeper-pattern]] — aplicado na borda antes de chegar nos serviços internos. Reduz [[wiki/concepts/attack-surface]] contra brute force, credential stuffing e DDoS na camada de aplicação.

## Custo Financeiro Direto da Ausência de Rate Limit

Além do risco de segurança, não limitar rotas públicas gera custo direto: um `POST` público sem limite permite criação em massa de registros falsos (custo de armazenamento em banco), e uma API de envio de e-mail sem limite permite que um atacante esgote a cota paga do provedor. Login sem proteção habilita brute force de senha. Rate limiting em rotas sensíveis/caras é tão financeiro quanto defensivo.

## Teste de Rate Limiting em Autopentest: "Resposta Sempre Tem Que Ser Sim"

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] trata rate limiting como um teste de checklist com resultado binário obrigatório: para toda rota mapeada, a pergunta "um usuário tem limite quantitativo de acesso?" precisa responder sim, sem exceção — moldura simples para verificar, rota por rota, que a defesa contra brute force existe antes de publicar o sistema.

## Contornando Rate Limit por Conta: Rotação de Free Tier

[[wiki/concepts/rotacao-de-contas-free-tier]] descreve o lado inverso desta página, visto do ponto de vista de quem sofre o rate limit em vez de quem o implementa: em vez de escalar uma única conta contra o limite do provider, cadastra-se múltiplas contas free tier e um [[wiki/concepts/ai-gateway-llm-router|gateway]] rotaciona entre elas quando a corrente esgota — efetivamente multiplicando a cota disponível ao custo de risco de detecção/banimento pelo provider.

## Rate Limit como Defesa do Ataque Online a Senha

[[wiki/concepts/ataque-online-vs-offline-senha]] situa rate limit (por IP, dispositivo ou usuário) e bloqueio de conta após N tentativas como a defesa específica do ataque online de força bruta contra login — distinto de [[wiki/concepts/password-hashing]], que só protege contra o cenário de banco vazado (ataque offline). Sem rate limit, hash/salt/pepper bem implementados não impedem alguém de simplesmente testar senhas comuns pelo formulário de login público.

## Ausência de Rate Limit + Erro Não Genérico = Brute Force Trivial

[[wiki/sources/brute-force-painel-admin-vibe-coding-pizzaria-burp-ffuf-hydra]] mostra o caso concreto onde a ausência de rate limit não é o único fator: combinada a mensagens de erro de login distintas (user enumeration — "usuário não encontrado" vs. "senha incorreta"), a senha de um painel admin é quebrada em segundos por três ferramentas diferentes (Burp Intruder, ffuf, Hydra), todas usando o mesmo sinal de sucesso na resposta. Reforça que rate limit sozinho é uma de várias camadas — sem ele, nenhuma outra defesa de autenticação online (exceto MFA) impede o brute force de rodar até o fim.

## Duas camadas: proxy + aplicação

No [[wiki/entities/omxterm]] ([[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]]): rate limit no proxy reverso ([[wiki/entities/traefik]], middleware) **e** interno — 10 tentativas de token em 60 s bloqueiam o IP, que passa a ser ignorado. Cobre também o brute force de token e reduz timing attack.

## Caso: Limite de Uploads por IP

Exemplo de endpoint público de escrita: 10 uploads/min por IP; acima disso, **429 Too Many Requests**. Justificativa: alguém fazendo 1.000–10.000 uploads/s. Ressalva (inferência): limite só por IP não cobre ataque distribuído nem usuários atrás de NAT; combinar com limite por usuário/token.

## Código Fonte TV — cinco tipos de armazenamento

Contador de limite de requisições citado como dado de vida curta típico de chave-valor ([[wiki/concepts/chave-valor]]).

## Key Sources


- [[wiki/sources/cinco-tipos-de-armazenamento-de-dados-qual-usar-codigo-fonte-tv]] — contador de rate limit em key-value
- [[wiki/sources/omxterm-terminal-web-pty-websocket-ssh-deploy-docker-traefik-otavio-miranda]] — rate limit em duas camadas (Traefik + app: 10 tentativas/60 s)
- [[wiki/sources/estimativas-back-of-envelope]] — Framework de 4 passos: (1) clarificar escopo — DAU, read/write ratio, pico vs média; (2) estimar QPS; (3) estimar storage; (4) estimar bandwidth. O objetivo é ordem de grandeza para evitar...
- [[wiki/sources/rate-limiting]]
- [[wiki/sources/brute-force-painel-admin-vibe-coding-pizzaria-burp-ffuf-hydra]] — ausência de rate limit como condição necessária para brute force de login com Burp Intruder, ffuf e Hydra
- [[wiki/sources/armazenamento-seguro-de-senhas-hash-salt-pepper-galego]] — rate limit + bloqueio de conta como defesa do ataque online, ao lado de MFA
- [[wiki/sources/rotacao-de-contas-free-tier-llm-router-hostinger]] — rotação de contas free tier como forma de contornar rate limit por conta individual
- [[wiki/sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]]
- [[wiki/sources/autenticacao-moderna-senha-sessao-jwt-oauth-mfa-passkeys]] — brute force e credential stuffing no login sem rate limiting
- [[wiki/sources/reacao-artigo-visual-algoritmos-load-balancing]] — o mesmo dilema estrutural (dropar a requisição vs. enfileirar e aceitar latência maior) aparece em load balancing sob carga, espelhando a escolha entre rejeitar (429) e enfileirar em rate limiting
- [[wiki/sources/back-pressure-producer-consumer-filas-bounded-admission-control]] — rate limit aplicado no **produtor** (não na borda de uma API pública): trava a taxa de produção na mesma capacidade que o consumidor consegue processar, como controle de [[wiki/concepts/back-pressure]]
- [[wiki/sources/historia-do-captcha-do-teste-de-turing-ao-turnstile]] — CAPTCHA/[[wiki/concepts/servico-de-resolucao-de-captcha]] só encarece a ação; limites por identidade/IP seguem necessários em camadas com [[wiki/concepts/bot-detection]]
- [[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]] — Instagram simplificado: 10 uploads/min por IP com 429 como defesa contra spam em endpoint público de escrita
- [[wiki/sources/requisicao-http-anatomia-metodos-headers-body-status-code-middleware]] — 429 Too Many Requests como o status do rate limit (ver [[wiki/concepts/http-status-code]])
