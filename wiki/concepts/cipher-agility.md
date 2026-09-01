---
type: concept
title: "Cipher Agility"
aliases: ["cipher agility", "agilidade de cifra", "crypto agility"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [cipher-agility, jose, jwt, algorithm-confusion, seguranca, design-de-seguranca]
skill: tech-mentor-security
status: draft
---

# Cipher Agility

Filosofia de design de sistemas de segurança em que o protocolo suporta **múltiplos algoritmos criptográficos** e permite trocar entre eles sem reescrever ou reimplantar a aplicação — normalmente através de um metadado que o próprio artefato (ex.: um token) carrega, instruindo o verificador sobre qual algoritmo usar. É o princípio de design por trás do [[wiki/concepts/jwa|JWA]] no ecossistema [[wiki/concepts/jose|JOSE]].

## A faca de dois gumes

Em teoria, cipher agility é positiva: permite migrar de um algoritmo que se tornou obsoleto (por avanço criptoanalítico ou por poder computacional) para um mais moderno, sem quebra de compatibilidade retroativa. Na prática, ela introduz uma complexidade perigosa: **se o servidor confia no metadado que instrui qual algoritmo usar sem impor uma whitelist própria**, um atacante que controla esse metadado (ex.: o header de um [[wiki/concepts/jwt|JWT]], que trafega pelo cliente) pode forçar a aceitação de um algoritmo mais fraco ou inexistente. Esse é exatamente o mecanismo do ataque de **[[wiki/concepts/algorithm-confusion]]**.

O ponto de falha não é a cipher agility em si, mas a **transferência implícita de responsabilidade**: a especificação delega ao desenvolvedor a decisão de quais algoritmos são seguros, e muitos desenvolvedores não versados em segurança seguem a configuração default da biblioteca, que historicamente aceitava algoritmos fracos (ou `none`) por compatibilidade.

## O oposto: cipher rigidity

A resposta de design oposta é a **cipher rigidity** (rigidez de cifra): fixar de antemão um conjunto único, não-negociável, de algoritmos modernos por versão do protocolo — sem permitir que o remetente escolha o algoritmo em tempo de execução. É a abordagem adotada pelo [[wiki/concepts/paseto|PASETO]] como alternativa ao JWT/JOSE.

## Relação com outros conceitos

- [[wiki/concepts/jwa]] — mecanismo concreto que implementa cipher agility no ecossistema JOSE
- [[wiki/concepts/algorithm-confusion]] — ataque que explora cipher agility sem whitelist no verificador
- [[wiki/concepts/paseto]] — design oposto (cipher rigidity) adotado como mitigação estrutural
- [[wiki/concepts/principio-menor-privilegio]] — mesmo princípio geral de segurança por design (menos opções, menos superfície de erro) aplicado a outro domínio

## Key Sources

- [[wiki/sources/jose-jws-jwe-jwk-jwa-algorithm-confusion-paseto]]
