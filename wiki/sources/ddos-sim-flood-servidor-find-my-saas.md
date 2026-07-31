---
type: source
title: "Como um SYN Flood de 260 Milhões de Requests Derrubou meu SaaS"
aliases: ["find my saas ddos", "syn flood mano davin", "under attack mode cloudflare incidente"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/ddos-sim-flood-servidor-find-my-saas.md
source_url: ""
author: "Davin (canal Mano Davin / Find My SaaS)"
date_published: ""
date_ingested: 2026-07-31
source_count: 0
tags: [ddos, syn-flood, cloudflare, under-attack-mode, traefik, coolify, docker, file-descriptors, syn-cookies, tcp, post-mortem, incident-response, vps, hostinger]
skill: tech-mentor-security
status: stable
---

## TL;DR

Relato pessoal (post-mortem em primeira pessoa) de um SYN flood de 260 milhões de requests em um único dia contra um SaaS pequeno (Find My SaaS), atrás de Cloudflare com Traefik (via Coolify) como proxy reverso. Três falhas se combinaram: modo Under Attack do Cloudflare desativado, um bug de CPU/memory leak no Traefik 3.6.16 (atualizado automaticamente pelo Coolify) que impedia o processamento de tráfego legítimo, e ausência de monitoramento que teria antecipado o problema em ~20 minutos. Servidor não foi recuperado — a solução final foi provisionar uma VPS nova do zero com infraestrutura defensiva (firewall → Docker → proxy, nessa ordem) e checklist de hardening (SYN cookies, limite de file descriptors, versão do proxy travada, Under Attack automático, rotação de IP).

## Key Claims

**Claim:** Um SYN flood mantém conexões TCP em estado de handshake incompleto (o autor cita `CLOSE_WAIT`/estado análogo a `SYN_RECV` e ~30.000 sockets alocados no kernel), esgotando recursos do servidor sem tráfego de aplicação legítimo.
**Evidence:** `ss -s` mostrou 34.000 conexões TCP nesse estado e 30.000 sockets alocados; comportamento consistente com a definição de ataque volumétrico/protocolo (L3/L4) descrita em `references/appsec-ddos-waf.md` do skill tech-mentor-security ("Protocol (L4): SYN flood → SYN cookies no load balancer") e com o mecanismo do [[wiki/concepts/tcp-three-way-handshake]] (handshake que nunca completa o terceiro ACK).
**Confidence:** alta para o mecanismo geral de SYN flood (confirmado pelo skill); média para os números específicos de estado TCP citados de memória pelo autor (ele mesmo hesita ao pronunciar "2400 FIN", provavelmente `SYN_RECV`).

**Claim:** SYN cookies no kernel evitam que memória seja alocada para uma conexão TCP antes do handshake terminar, sendo defesa direta contra SYN flood.
**Evidence:** Citado como parte do checklist pós-incidente do autor; consistente com a entrada do skill tech-mentor-security (`appsec-ddos-waf.md`): "Protocol (L4): SYN flood → SYN cookies no load balancer" como mitigação padrão de camada de protocolo.
**Confidence:** alta — mecanismo técnico padrão de Linux (`net.ipv4.tcp_syncookies`), confirmado pelo skill.

**Claim:** O modo "Under Attack" do Cloudflare, quando desativado, deixa o tráfego malicioso passar normalmente pelo CDN/WAF até a origem, mesmo com Cloudflare configurado na frente do domínio.
**Evidence:** O autor confirma via dashboard do Cloudflare que os 260 milhões de requests passaram *pelo* Cloudflare (não foram direto ao IP real) — ou seja, o CDN estava na frente, mas sem a camada de desafio adicional que o Under Attack Mode ativa. Consistente com o modelo de camadas de defesa do skill (`Internet → CDN/WAF → API Gateway → Load Balancer → Application`): ter o WAF/CDN na frente não é suficiente se o modo de mitigação agressiva não está ligado.
**Confidence:** alta — comportamento do produto é verificável e consistente com a arquitetura de defesa em camadas já documentada em [[wiki/concepts/waf]].

**Claim:** Um bug de CPU constante (35%) e memory leak (4,7 GB em 40 minutos) no proxy reverso (Traefik 3.6.16), atualizado automaticamente pelo Coolify, impediu o processamento de tráfego legítimo mesmo antes do pico do ataque, agravando o incidente.
**Evidence:** Observação direta do autor via `htop` e comportamento do container após downgrade (a versão anterior, 3.3, também apresentou memory leak no mesmo setup). Este é um bug de terceiros (Traefik), não documentado nos skills consultados — não há como verificar a claim contra fonte oficial do projeto Traefik nesta ingestão.
**Confidence:** média — relato de primeira mão consistente internamente (dois downgrades, dois vazamentos observados), mas sem confirmação de changelog/issue tracker do Traefik nesta ingestão; risco de causa raiz real ser configuração específica do setup do autor, não bug universal da versão.

**Claim:** Auto-update de proxy reverso em produção é um risco de disponibilidade — uma versão nova pode introduzir regressão severa (CPU/memory leak) sem aviso, e o Coolify atualiza o Traefik semanalmente por padrão.
**Evidence:** Comportamento observado diretamente pelo autor (Coolify atualizou o Traefik durante o próprio incidente) e virou o primeiro item do checklist pós-incidente ("nunca mais travei a versão do Traefik"). Consistente com o princípio geral de imutabilidade/controle de mudança em produção, mas não há uma claim específica sobre Coolify nos skills consultados.
**Confidence:** alta para o comportamento observado (fato de primeira mão, verificável no próprio painel do Coolify); não verificado contra documentação oficial do Coolify nesta ingestão.

**Claim:** O limite default de file descriptors do Docker é baixo demais para suportar picos de conexão, e deve ser configurado explicitamente (autor cita 65.000 soft/hard).
**Evidence:** Recomendação do autor no checklist pós-incidente, ligada ao fato de que a aplicação atingiu o limite de file descriptors durante o ataque e entrou em loop de falha. Não há seção específica sobre `ulimit`/`nofile` em `references/container-hardening.md` do skill tech-mentor-security consultado nesta ingestão — claim tratada como conhecimento geral de Linux/Docker, não verificada contra o skill.
**Confidence:** média — mecanismo plausível e amplamente documentado fora desta wiki (limite default do Docker realmente é conservador), mas o valor exato (65.000) não foi cruzado com nenhuma fonte nesta ingestão. `[external]` para o valor numérico específico.

## Entities & Concepts Touched

- [[wiki/concepts/ddos-syn-flood]]
- [[wiki/concepts/waf]]
- [[wiki/concepts/tcp-three-way-handshake]]
- [[wiki/concepts/reverse-proxy]]
- [[wiki/concepts/coolify]]
- [[wiki/entities/hostinger]]
- [[wiki/entities/mano-davin]]

## Open Questions

- O bug específico de CPU/memory leak no Traefik 3.6.16 não foi verificado contra o changelog ou issue tracker oficial do projeto — candidato a nota de rodapé se uma fonte técnica dedicada ao Traefik for ingerida no futuro.
- O valor de 65.000 file descriptors (soft/hard) é recomendação do autor, não confirmada contra a documentação oficial do Docker ou contra `references/container-hardening.md` do skill (que não cobre `ulimit`/`nofile` nesta versão).
- O autor menciona "ferramentas de segurança" que permitiriam descobrir o IP real de um servidor atrás de Cloudflare em segundos, sem nomear qual — não verificável nesta ingestão.
