---
type: concept
title: "Token Opaco"
aliases: ["opaque token", "reference token", "token de referência"]
date_created: 2026-09-14
date_updated: 2026-09-14
source_count: 1
tags: [token, autenticacao, autorizacao, seguranca, csprng, stateful]
skill: tech-mentor-security
status: draft
---

# Token Opaco

String de autorização que **não carrega informação útil legível dentro de si**. Funciona como uma chave de referência: o servidor a consulta em uma estrutura de dados própria (banco, cache) para resolver a quem/o que ela se refere — analogia direta com uma chave primária cujas linhas armazenam os dados da sessão/usuário autenticado.

Contraste com o [[wiki/concepts/jwt|token autocontido]] (JWT): o token opaco não tem RFC ou padrão formal de estrutura — por definição, é só uma string cujo significado só o servidor conhece.

## Trade-off Central

- **Vantagem**: controle total sobre revogação — basta apagar/marcar a entrada correspondente no servidor, efeito instantâneo. Isso resolve o problema que o JWT tem por natureza (não dá para revogar antes de expirar sem reintroduzir estado).
- **Desvantagem**: exige consulta ao servidor (banco/cache) a cada validação — não escala tão bem quanto um token autocontido que só verifica assinatura localmente. Também reduz a autonomia do cliente: não há dados embutidos no token para usar diretamente no frontend.

Por isso, tokens opacos são característicos de arquiteturas **stateful** — ver [[wiki/concepts/sessoes-http-cookies]].

## Como Gerar com Segurança

Não existe padrão formal, mas existe um requisito não-negociável: **imprevisibilidade**. Um token gerado de forma sequencial (`1`, `2`, `3`...), via `Math.random()`, hash de timestamp, ou string incremental é quebrável por força bruta — um atacante consegue adivinhar valores vizinhos.

A defesa é gerar o token com um **CSPRNG** (Cryptographically Secure Pseudo-Random Number Generator), com pelo menos **256 bits de entropia**:

- **Node.js**: `crypto.randomBytes`
- **Java**: `SecureRandom`
- **Python**: módulo `secrets` (ou `random` com fonte de entropia segura)

Ver [[wiki/concepts/criptografia]] para o papel do CSPRNG dentro do ecossistema criptográfico mais amplo.

### Por que não UUID v4?

UUIDv4 é "aceitável forçando a barra", mas tem só **122 bits** de aleatoriedade real (dos 128 bits totais, 6 são fixos pela definição de versão/variante) — uma diferença exponencial de dificuldade de quebra frente aos 256 bits recomendados. Ver [[wiki/concepts/uuid]] para a distinção completa entre UUID como identificador (ordenação, unicidade, chave primária) e token como segredo (imprevisibilidade é o requisito, não ordenação).

## Token Não É ID

Um **ID** identifica uma entidade — segurança não é o aspecto relevante, ordenação/unicidade sim. Um **token** autoriza acesso a um recurso — segurança é o aspecto central. Analogia: se o ID é o número do CPF, o token é o crachá com que se passa na catraca da empresa. Consequência prática: algoritmos de geração de ID como Snowflake (otimizados para ordenação temporal e unicidade distribuída) não devem ser reaproveitados como gerador de token.

## Usos Comuns

- **Session token / ID de sessão**: o caso clássico. Detalhado em [[wiki/concepts/sessoes-http-cookies]].
- **[[wiki/concepts/api-key|API Key]]**: autentica uma aplicação (não um usuário).
- Outros usos pontuais: token de reset de senha por e-mail, validação de link temporário, chave de idempotência — todos exigem a mesma disciplina de geração (CSPRNG, alta entropia), por serem segredos de uso único ou curta duração.

## Validação em Escala: Token Introspection

Em sistemas multi-serviço, o Resource Server que não tem acesso direto ao armazenamento do Authorization Server valida um token opaco via **Token Introspection** (RFC 7662): `POST /introspect { token }` retorna `{ active, sub, scope, exp, client_id, ... }`. A revogação correspondente segue RFC 7009 (`POST /revoke`). [skill: tech-mentor-security]

## Relação com outros conceitos

- [[wiki/concepts/jwt]] — o contraponto autocontido: stateless, sem consulta ao servidor, mas sem revogação instantânea
- [[wiki/concepts/sessoes-http-cookies]] — instância mais comum de token opaco (session token)
- [[wiki/concepts/api-key]] — instância de token opaco usada para autenticar aplicações, não usuários
- [[wiki/concepts/uuid]] — contraste de entropia e de propósito (identificador vs. segredo)
- [[wiki/concepts/criptografia]] — CSPRNG como mecanismo de geração segura

## Key Sources

- [[wiki/sources/anatomia-de-um-token-1-opaco-vs-autocontido-bernardo-lobato]] — definição, geração segura, token vs. ID, session token e API key como usos comuns
