---
type: concept
title: "systemd"
aliases: ["systemd", "systemctl", "unit file", "init system"]
date_created: 2026-07-20
date_updated: 2026-07-20
source_count: 1
tags: [linux, systemd, processos, infra, deploy]
skill: tech-mentor-infra
status: stub
---

# systemd

Sistema de init e gerenciador de serviços da maioria das distribuições Linux modernas (Ubuntu, Debian, Fedora, RHEL). É o processo PID 1 — ancestral de todos os outros processos — e é responsável por subir, manter vivo, reiniciar e derrubar serviços de forma padronizada, via unidades (`.service`) e o comando `systemctl`.

## Por que usar em vez de rodar o processo direto no terminal

Um processo iniciado direto num terminal SSH (`node server.js &`) morre quando a sessão SSH cai, não reinicia sozinho se travar, e não sobe automaticamente no boot da máquina. Uma unidade systemd resolve os três problemas: fica desacoplada da sessão do operador, tem política de restart configurável, e é habilitada para iniciar no boot.

## Uso em deploy manual num host único

Em um deploy [[wiki/concepts/blue-green-deploy|blue/green]] feito à mão numa VPS (sem Kubernetes), systemd é o que garante que cada instância da aplicação (ex.: uma unidade para a versão "blue" na porta 3001, outra para "green" na porta 3002) continue rodando de forma confiável entre trocas de tráfego feitas no [[wiki/concepts/reverse-proxy|reverse proxy]] — o roteamento e o ciclo de vida do processo são responsabilidades completamente separadas.

## Key Sources

- [[wiki/sources/deploy-blue-green-na-pratica-vps-nginx]] — systemd citado como ferramental de administração dos processos Node na VPS, sem detalhamento das unidades
