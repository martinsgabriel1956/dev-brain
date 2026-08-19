---
type: concept
title: "Confiar no Frontend (Client-Side Trust Anti-Pattern)"
aliases: ["confiar no frontend", "nunca confie no cliente", "client-side validation bypass", "trust boundary violation"]
date_created: 2026-07-04
date_updated: 2026-08-19
source_count: 3
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

## Variante: Burlar Regra de Negócio Diretamente na API

[[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] descreve um teste correlato, mas distinto do bypass client-side clássico desta página: em vez de manipular variáveis no DevTools do frontend, o teste consiste em atacar diretamente a API tentando burlar uma regra de negócio que deveria ser reforçada no servidor — exemplo dado: registrar check-in em datas passadas ou futuras que a regra do produto não deveria permitir. A pergunta-guia da fonte é "eu consigo ser malandra no sistema?". O princípio de correção é o mesmo desta página — toda regra de negócio precisa ser revalidada no servidor —, mas o vetor de ataque já pula a camada de UI e vai direto à API, então "nunca confiar no frontend" não é suficiente sozinho: é preciso também não confiar em nenhum parâmetro de requisição que o cliente controla, mesmo vindo de um client legítimo.

## Variante: Restrição de Formulário Client-Side (`maxlength`) Não é Filtro

[[wiki/sources/xss-cross-site-scripting-luiz-viana]] mostra uma aplicação mais estreita do mesmo princípio: no DVWA, um campo de nome tem `maxlength="10"` no HTML, e removê-lo via DevTools basta para digitar um payload de [[wiki/concepts/xss]] maior. Não é uma regra de negócio (preço, saldo) como nos exemplos acima, mas o mecanismo é idêntico — uma restrição imposta só no client-side é conveniência de UI, não segurança; a validação real precisa acontecer no servidor.

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
- [[wiki/sources/testes-de-seguranca-pentest-com-claude-code-pulsar-saas]] — variante de bypass de regra de negócio direto na API (não via DevTools)
- [[wiki/sources/xss-cross-site-scripting-luiz-viana]] — variante em nível de formulário: atributo `maxlength` removido via DevTools para digitar payload de XSS maior que o limite de UI
