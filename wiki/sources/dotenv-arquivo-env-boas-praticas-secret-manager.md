---
type: source
title: "O arquivo .env: o que é, para que serve e boas práticas"
aliases: ["dotenv boas práticas", "arquivo .env vídeo"]
date_created: 2026-10-09
date_updated: 2026-10-09
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/dotenv-arquivo-env-boas-praticas-secret-manager.md
source_url: ""
author: "não identificado"
date_published: ""
date_ingested: 2026-10-09
source_count: 1
tags: [security, secrets-management, dotenv, variavel-de-ambiente, twelve-factor, secret-manager, configuracao]
skill: tech-mentor-security
status: stable
---

## TL;DR

Vídeo em PT-BR sobre o [[wiki/concepts/dotenv|`.env`]]: arquivo dedicado a [[wiki/concepts/variavel-de-ambiente|variáveis de ambiente]] que separa **configuração de servidor** do código (Fator III do [[wiki/sources/twelve-factor-app]]). Vai para ele o que muda por [[wiki/concepts/ambiente-de-execucao|ambiente]] e raramente muda em runtime (hosts, portas, tokens, nível de log, nome do ambiente); **não** vão regras de negócio nem configuração de cliente/usuário ([[wiki/concepts/configuracao-vs-regra-de-negocio]]). Em dev/staging o arquivo basta; em produção crítica prefere-se um [[wiki/concepts/secret-manager|cofre]] (Vault, AWS/Google/Azure) que injeta no ambiente, com auditoria e rotação. Segurança em camadas ([[wiki/concepts/defense-in-depth]]); regra final: **nenhuma senha no código** ([[wiki/concepts/secrets-management]]).

## Key Claims

**Claim:** Hardcode de config no código versionado é o problema original; o `.env` centraliza, facilita troca de ambiente e reduz alteração no código.
**Evidence:** relato de app Python com a senha do banco repetida em cada arquivo e enviada ao GitHub (trocar exigiria Ctrl+F global).
**Confidence:** alta (bate com [[wiki/sources/twelve-factor-app]]).

**Claim:** No `.env` vai o que muda entre ambientes e quase nunca em runtime; regras de negócio, preferências e logo do cliente vão para o banco/painel (com cache).
**Evidence:** exemplos desconto premium, resolução máxima de conversor de vídeo, logo do cliente.
**Confidence:** alta.

**Claim:** Apagar a senha e commitar de novo não resolve: fica no histórico do git.
**Evidence:** afirmação do autor; consistente com [[wiki/concepts/secret-scanning]].
**Confidence:** alta.

**Claim:** Em produção, cofres (Google Secret Manager, AWS Secrets Manager, HashiCorp Vault, Azure Key Vault) injetam variáveis via agente e oferecem criptografia, auditoria, controle de acesso e rotação automática; a app lê primeiro o ambiente e só então o `.env` (fallback).
**Evidence:** descrição funcional do autor; ver [[wiki/concepts/secret-manager]].
**Confidence:** alta. Ressalva [external]: injeção por agente é um de vários modelos (também há SDK/sidecar/External Secrets Operator).

**Claim:** Não vale para projetos pequenos (custo de configuração, necessidade de acesso externo do servidor); não existe bala de prata; segurança é em camadas (analogia das casas com câmera e cerca).
**Evidence:** analogia + trade-offs citados.
**Confidence:** média-alta (opinião fundamentada).

**Claim:** Apagar o `.env` depois de subir o serviço não funciona (PHP lê a cada requisição); ler de variáveis do SO/memória é mais rápido que arquivo (10–20 ms importam em cenários críticos).
**Evidence:** afirmação do autor sem medição.
**Confidence:** média (varia por runtime; muitas linguagens carregam o `.env` uma vez na inicialização — [external]).

**Claim:** `.env` nunca em diretório público; teste `/.env` na URL dos seus sites.
**Evidence:** recomendação final; ver [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]].
**Confidence:** alta.

## Entities

[[wiki/entities/heroku]], [[wiki/entities/hostinger]], [[wiki/entities/amazon-web-services]], [[wiki/entities/google]].

## Concepts

[[wiki/concepts/dotenv]], [[wiki/concepts/variavel-de-ambiente]], [[wiki/concepts/ambiente-de-execucao]], [[wiki/concepts/configuracao-vs-regra-de-negocio]], [[wiki/concepts/secret-manager]], [[wiki/concepts/secrets-management]], [[wiki/concepts/secret-scanning]], [[wiki/concepts/defense-in-depth]], [[wiki/concepts/least-privilege]], [[wiki/concepts/logs-em-producao]], [[wiki/concepts/paridade-local-producao]], [[wiki/concepts/compliance]].

## Open Questions

- O autor diz que o Heroku é o "pai da AWS" e pioneiro do pagamento por uso: impreciso — a AWS (2006) precede o Heroku (2007). O vínculo real é o Heroku ter originado o manifesto 12-factor.
- Como conciliar Fator III (env vars) com secrets que não deveriam ficar em texto puro no ambiente? (a fonte só cobre injeção por agente; ver pergunta similar em [[wiki/sources/twelve-factor-app]]).
- Canal/autor não identificado.

## Quotes

> "O código não deveria ter nenhuma senha. Nenhuma."

> "Configuração deve ser externa, organizada e previsível."
