---
type: concept
title: "Account Takeover (ATO)"
aliases: ["account takeover", "ato", "tomada de conta", "sequestro de conta"]
date_created: 2026-07-31
date_updated: 2026-07-31
source_count: 1
tags: [account-takeover, ato, appsec, autenticacao, fraude, idor]
skill: tech-mentor-security
status: stub
---

# Account Takeover (ATO)

Classe de vulnerabilidade/ataque em que um agente externo consegue autenticar-se como um usuário legítimo sem passar pelo fluxo de login normal desse usuário (sem saber a senha, sem ter o segundo fator). O resultado é controle total sobre a conta — dados, permissões e qualquer ação que o dono legítimo poderia executar.

## Vetor Demonstrado: Reuso de Credencial de API como Cookie de Sessão

[[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]] demonstra um ATO derivado de encadear duas falhas menores: primeiro um [[wiki/concepts/idor]] no endpoint de perfil expõe a "chave de integração" de outro usuário (o ID do perfil na URL é sequencial, sem checagem de ownership); depois, essa chave sozinha — sem senha, sem MFA — é aceita por um endpoint de autenticação (`POST /api/login`) que gera um cookie de sessão válido. Nenhuma das duas falhas isoladamente parece crítica; encadeadas, resultam em login completo como qualquer usuário cujo ID seja adivinhado ou enumerado.

## Por Que É Mais Grave que um IDOR Isolado

Um IDOR que vaza dados (nome, e-mail, endereço) já é sério, mas está limitado ao que aquele endpoint específico retorna. Um IDOR que vaza uma **credencial de autenticação** (chave de API, token, chave de integração) converte a leitura de dados em controle de sessão — o atacante deixa de "ver" a conta e passa a "ser" a conta, com acesso a todos os outros endpoints que a aplicação disponibiliza para aquele usuário.

## Mitigação

- Nenhum endpoint deve expor uma credencial de autenticação (chave de API, token de sessão renovável, secret de integração) sem validar que o requisitante já está autenticado como o dono daquele recurso.
- Endpoints de troca de credencial-por-sessão (`POST /api/login` usando uma API key) deveriam, no mínimo, logar e limitar a taxa de tentativas — reduz a janela de enumeração automatizada (ver caso de escalonamento a admin via Burp Intruder em [[wiki/concepts/idor]]).
- Rotação/expiração de chaves de integração reduz o dano de uma chave já vazada.

## Relação com outros conceitos

- [[wiki/concepts/idor]] — o vetor de exposição da credencial, nesta fonte
- [[wiki/concepts/autenticacao-e-autorizacao]] — ATO quebra a camada de autenticação, não só a de autorização
- [[wiki/concepts/secrets-management]] — mesma lógica de "credencial vazada = comprometida", aplicada a uma chave de API em vez de um `.env`

## Key Sources

- [[wiki/sources/vibe-coding-env-exposto-idor-account-takeover-rce-loja-ia]]
