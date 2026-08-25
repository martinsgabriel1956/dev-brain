---
type: concept
title: "Antipadrão da Senha (Password Antipattern)"
aliases: ["password antipattern", "antipadrão da senha", "compartilhamento de senha entre sistemas"]
date_created: 2026-08-24
date_updated: 2026-08-24
source_count: 1
tags: [antipadrao, autenticacao, autorizacao, oauth2, seguranca, historia]
skill: tech-mentor-security
status: stub
---

# Antipadrão da Senha (Password Antipattern)

Antipadrão em que sistemas ou usuários se autenticam entre si trocando usuário e senha — um mecanismo criado quase exclusivamente para pessoas se autenticarem a um sistema, não para um sistema se identificar a outro. Antes do [[wiki/concepts/oauth2|OAuth]] existir (contexto de 2006), era assim que se dava acesso de um serviço terceiro aos seus dados: você entregava sua própria senha (ex.: senha do Flickr) para o serviço terceiro, que passava a se conectar como se fosse você.

## Por que é um antipadrão

- **Perda de identidade real do serviço**: quem audita não consegue distinguir se a requisição partiu de você ou do serviço terceiro que você autorizou — ambos usam a mesma credencial.
- **Acesso irrestrito**: o serviço que recebe sua senha pode fazer *tudo* que você pode fazer, não só o que era necessário para a integração (contraste com [[wiki/concepts/oauth2|escopo limitado]] do OAuth).
- **Revogação destrutiva**: a única forma de cortar o acesso de um serviço específico é trocar a senha na origem — o que quebra o acesso de **todos** os outros serviços já conectados com aquela senha, exigindo reconectar cada um manualmente.
- **Rotação de credenciais inviável**: sem tokens individuais por integração, não há como rotacionar credenciais de um vínculo sem afetar os demais.

## Relação com o OAuth

O [[wiki/concepts/oauth2|OAuth]] nasceu, em 2006-2007, especificamente para resolver este antipadrão: em vez de entregar a identidade (senha), o usuário passa a delegar uma autorização limitada, temporária e revogável independentemente — um token com escopo específico, no lugar da senha completa. Ver [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] para o contexto histórico completo (Twitter, Magnolia, RFC 5849/6749).

## Distinção do ROPC

Não confundir com o [[wiki/concepts/ropc-resource-owner-password-credentials|ROPC]] — antipadrão relacionado mas distinto: no antipadrão da senha, o usuário entrega a senha diretamente ao *serviço terceiro*, que passa a agir como ele; no ROPC, é a própria API/cliente OAuth que recebe a senha do usuário e a repassa por baixo dos panos ao provedor de identidade, quebrando a garantia de que a senha nunca deveria passar pelo client.

## Key Sources

- [[wiki/sources/historia-oauth2-antipadrao-senha-bernardo-lobato]] — origem histórica do termo e do problema que motivou a criação do OAuth
