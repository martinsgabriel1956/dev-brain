---
type: source
title: "Segurança de rede Wi-Fi em pequeno comércio: isolando clientes com MikroTik"
aliases: ["wifi de clientes isolado", "rede de convidados mikrotik", "segurança de rede pequeno comércio"]
date_created: 2026-10-02
date_updated: 2026-10-02
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/seguranca-rede-wifi-pequeno-comercio-mikrotik-isolamento-clientes.md
source_url: ""
author: "não identificado (canal com comunidade de membros)"
date_published: ""
date_ingested: 2026-10-02
source_count: 0
tags: [networking, seguranca-de-rede, wifi, segmentacao, firewall, mikrotik, pequeno-comercio, client-isolation]
skill: tech-mentor-networking
status: stable
---

## TL;DR

Dar a senha do Wi-Fi da empresa ao cliente o coloca numa [[wiki/concepts/rede-plana]], ao lado de PDV, financeiro, DVR e impressoras, e uma ferramenta de scan (Kali etc.) enxerga tudo. A solução proposta é barata: roteador da operadora com Wi-Fi desligado → [[wiki/entities/mikrotik]] → **um AP por finalidade** (clientes / empresa, depois funcionários), cada um em sua faixa de IP, com [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]]: o que protege é a regra de firewall `forward` + `drop`, não a faixa. Camadas extras: [[wiki/concepts/ip-fixo-em-rede-interna]], [[wiki/concepts/client-isolation]] só nos APs de clientes/funcionários, e [[wiki/concepts/protecao-unidirecional-vs-bidirecional]] (3 redes). Dois APs também evitam a [[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]] (~50) afetar a operação. Serviço vendável: ~2 h de trabalho, ~R$ 600.

## Key Claims

**Claim:** Rede plana + senha compartilhada permite que qualquer cliente escaneie a rede interna.
**Evidence:** Cenário do notebook com Kali/scanner; clínica com 200 pessoas, restaurante com 100+.
**Confidence:** alta — é o comportamento normal de uma LAN L2 única [external; skill tech-mentor-networking, `networking-infra-containers.md` §VLANs: hosts na mesma rede se comunicam direto].

**Claim:** Isolar por faixa de IP sozinho não protege; o firewall é o que protege.
**Evidence:** "Não é só a faixa de IP que protege... o que realmente protege vai ser o seu firewall"; regra `chain=forward src=10.0.0.x dst=192.168.0.x action=drop`.
**Confidence:** alta; a regra exposta cobre só o sentido clientes→rede interna, e a ordem das regras e o tráfego de retorno não foram discutidos (ver [[wiki/concepts/protecao-unidirecional-vs-bidirecional]]).

**Claim:** Um AP, mesmo multi-SSID, degrada acima de ~50 conexões e isso afeta o sistema da empresa; separar AP de clientes e AP da empresa.
**Evidence:** Experiência cotidiana de Wi-Fi público instável; o autor diz valer "independentemente do preço".
**Confidence:** média — o limite de 50 é regra prática do autor e varia por modelo/Wi-Fi 6; o princípio de separar domínio de falha é sólido ([[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]]).

**Claim:** IP fixo na rede interna dá base para regras de firewall; o atacante conectado "não está dentro da rede".
**Evidence:** Tabela de IPs (.10 PDV, .20 financeiro, .30 impressora, .40 DVR, .50+ câmeras).
**Confidence:** média — o ganho real é permitir regras por host; IP fixo isolado não impede quem escolhe um IP livre na mesma LAN ([[wiki/concepts/ip-fixo-em-rede-interna]]).

**Claim:** Client Isolation vai nos APs de clientes/funcionários e **não** no AP da rede interna.
**Evidence:** Ativá-lo na interna impediria PDV↔financeiro↔impressora.
**Confidence:** alta ([[wiki/concepts/client-isolation]]).

## Entities

- [[wiki/entities/mikrotik]] — roteador/firewall barato (5 portas) usado como ponto único de saída e filtro.

## Concepts

[[wiki/concepts/rede-plana]], [[wiki/concepts/segmentacao-de-rede-por-faixa-de-ip-e-firewall]], [[wiki/concepts/client-isolation]], [[wiki/concepts/ip-fixo-em-rede-interna]], [[wiki/concepts/protecao-unidirecional-vs-bidirecional]], [[wiki/concepts/degradacao-de-ap-por-numero-de-conexoes]], [[wiki/concepts/attack-surface]], [[wiki/concepts/defense-in-depth]], [[wiki/concepts/least-privilege]], [[wiki/concepts/blast-radius]], [[wiki/concepts/pentest]], [[wiki/concepts/network-policy]]. Relacionado: [[wiki/sources/zero-trust]] (a rede interna não é confiável por padrão).

## Open Questions

- As "cinco regras" da proteção bidirecional não foram mostradas na fala (só em slide da comunidade).
- Falta tratar: WPA2/WPA3 e troca de senha, VLANs/SSID separados em AP gerenciável (alternativa ao 2º AP físico), regras com tráfego estabelecido/relacionado, DNS/DHCP do guest, acesso do guest ao próprio MikroTik, câmeras/DVR expostos à internet, IoT.
- O autor não cita a LGPD/logs de acesso de visitantes.
- Preço (R$ 200/mês, R$ 600 de serviço) é estimativa do autor para o Brasil, sem fonte.

## Raw quotes

> "Você não está simplesmente acessando a internet. Você está dentro da rede da empresa."
> "Não é só a faixa de IP que protege... Mas o que realmente protege vai ser o seu firewall."
> "A grande maioria deles funciona muito bem para até 50 conexões. A partir de 50 conexões a comunicação começa a degradar."
