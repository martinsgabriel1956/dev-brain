---
type: concept
title: "Confiar no Frontend (Client-Side Trust Anti-Pattern)"
aliases: ["confiar no frontend", "nunca confie no cliente", "client-side validation bypass", "trust boundary violation"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 1
tags: [appsec, trust-boundary, business-logic, client-side-security, owasp]
skill: tech-mentor-security
status: stable
---

# Confiar no Frontend (Client-Side Trust Anti-Pattern)

Anti-padrão raiz por trás de várias vulnerabilidades: assumir que uma regra de negócio validada apenas no frontend (botão desabilitado, renderização condicional, preço calculado no cliente) é suficiente, porque "o usuário não teria como burlar a interface". Qualquer estado ou lógica que roda no cliente pode ser lido e manipulado por quem controla o dispositivo — isso é especialmente verdade em aplicações CSR, onde toda a lógica de UI é JavaScript executando na máquina do próprio usuário.

## Demonstração do bypass

Em uma tela com botão de saque desabilitado por saldo insuficiente:

1. Localizar no código a condição de renderização que decide entre "indisponível" e o botão ativo.
2. Colocar um breakpoint nessa condição via DevTools e recarregar a página.
3. No momento da pausa, alterar manualmente as variáveis em memória (o valor do saldo, uma flag booleana) para forçar a condição a avaliar como "disponível".
4. O botão passa a aparecer habilitado — a UI foi enganada porque toda a decisão estava no cliente.

A requisição real ao backend só falha se o servidor **reconfere** o saldo verdadeiro no momento do saque. Se o backend confiasse no valor recebido do cliente (como um preço calculado no frontend de um e-commerce e enviado no corpo da requisição), o ataque teria sucesso — bastaria interceptar a requisição e trocar o valor.

## Correção

Toda regra de negócio (preço, saldo, permissão, limite) deve ser **recalculada e revalidada no servidor**, independentemente do que a UI mostra ou do que o cliente envia. O frontend pode (e deve) validar para dar feedback rápido ao usuário, mas nunca é a fonte de verdade — essa responsabilidade é sempre do backend.

## Relação com outras vulnerabilidades desta fonte

Este é o princípio subjacente que também explica por que [[wiki/concepts/idor]] (checar ownership no servidor, não confiar no ID vindo da requisição) e [[wiki/concepts/mass-assignment]] (whitelist de campos no servidor, não confiar no shape do body) funcionam como defesas: em ambos os casos, a mitigação é mover a decisão de segurança do que o cliente envia para o que o servidor valida.

## Ver também

- [[wiki/concepts/attack-surface]] — toda superfície onde o cliente influencia uma decisão de negócio é um ponto a proteger no servidor

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
