---
type: concept
title: "DDoS e SYN Flood"
aliases: ["syn flood", "ddos", "denial of service distribuído", "under attack mode"]
date_created: 2026-07-31
date_updated: 2026-08-06
source_count: 2
tags: [ddos, syn-flood, tcp, cloudflare, under-attack-mode, syn-cookies, seguranca, rede]
skill: tech-mentor-security
status: draft
---

# DDoS e SYN Flood

Ataque de negação de serviço distribuído (DDoS) que explora o [[wiki/concepts/tcp-three-way-handshake]] em vez de mandar tráfego de aplicação: o atacante envia um volume massivo de pacotes `SYN` e nunca completa o handshake com o `ACK` final. O servidor reserva recursos (memória, um socket) para cada conexão pendente esperando uma confirmação que nunca chega — até esgotar a capacidade da máquina.

Analogia usada em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]: o servidor é uma portaria de prédio; cada `SYN` é alguém tocando o interfone dizendo "vim te visitar", o servidor abre a porta e espera a pessoa entrar. Um SYN flood é milhões de pessoas tocando o interfone ao mesmo tempo e nenhuma entra — a portaria fica de porta aberta pra visitantes que nunca chegam, até travar.

## Onde se encaixa na taxonomia de DDoS

Segundo o skill `tech-mentor-security` (`references/appsec-ddos-waf.md`), DDoS se divide em três camadas:

- **Volumétrico (L3/L4)** — flood de pacotes UDP/ICMP; mitigado por CDN/Shield.
- **Protocol (L4)** — SYN flood; mitigado por **SYN cookies** no load balancer/kernel.
- **Application (L7)** — HTTP flood com aparência legítima; mitigado por WAF + rate limiting + CAPTCHA.

O SYN flood é especificamente o caso de protocolo (L4): ele não precisa parecer tráfego de aplicação válido, só precisa completar o primeiro passo do handshake TCP repetidamente.

## SYN Cookies — a mitigação central

SYN cookies fazem o kernel **não alocar memória** para uma conexão TCP enquanto o handshake não termina — o servidor responde ao `SYN` com um `SYN-ACK` cujo número de sequência é derivado criptograficamente da conexão (em vez de guardar estado em uma fila), e só materializa a conexão de verdade quando o `ACK` final chega e confere. Sem fila de conexões pendentes para o atacante encher, o SYN flood perde o efeito.

## Modo Under Attack (Cloudflare)

Estar atrás de um [[wiki/concepts/waf]]/CDN como Cloudflare não é suficiente por si só: o tráfego malicioso pode passar normalmente pelo Cloudflare até a origem se o modo de mitigação agressiva (Under Attack Mode) não estiver ativo. Esse modo adiciona uma camada de desafio (ex.: verificação JS) antes de rotear o tráfego à origem — sem ele, o CDN funciona só como proxy, não como filtro ativo contra o pico.

## Caso real: Find My SaaS

Em [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]], um SaaS pequeno recebeu 260 milhões de requests em um único dia (vs. 200–400 mil num dia normal) via SYN flood, mesmo com Cloudflare configurado na frente do domínio — porque o Under Attack Mode estava desativado. O incidente foi agravado por um bug de terceiros no proxy reverso ([[wiki/concepts/coolify]]/Traefik) que já consumia CPU e memória antes do pico, e resolvido não recuperando o servidor original, mas provisionando uma instância nova com a ordem de setup invertida: firewall no boot → Docker → proxy por último.

## Precursor: tentativas bloqueadas antes do incidente

Em [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — cronologicamente anterior ao incidente de 260 milhões de requests acima — o mesmo autor relata 157 tentativas maliciosas bloqueadas pelo Cloudflare num total de 230-234 mil requisições nos primeiros 15 dias do Find My SaaS, sem incidente grave: o Under Attack Mode parece ter funcionado nesse momento. Isso sugere que a configuração de proteção foi desativada ou alterada em algum ponto entre essa fonte e o incidente do SYN flood — não esclarecido em nenhuma das duas transcrições, sinalizado como questão aberta em [[wiki/entities/mano-davin]].

## Checklist de mitigação (pós-incidente)

1. Travar a versão do proxy reverso em produção — auto-update pode subir uma versão com regressão.
2. Under Attack Mode ativo (ou com ativação automática configurada) no CDN/WAF.
3. Rotacionar o IP real do servidor se ele já foi exposto (ex.: registro de DNS histórico) — o CDN só protege se o atacante não conseguir contornar indo direto ao IP de origem.
4. Limite de file descriptors do container configurado explicitamente (o default costuma ser conservador).
5. SYN cookies habilitados no kernel.
6. Monitoramento de RAM do proxy, contagem de processos e sockets TCP abertos — permite detectar o ataque antes da perda total de acesso.

## Key sources

- [[wiki/sources/ddos-sim-flood-servidor-find-my-saas]]
- [[wiki/sources/15-dias-depois-lancar-sas-numeros-ataques-vulnerabilidades]] — 157 tentativas maliciosas bloqueadas, precursor ao incidente acima
