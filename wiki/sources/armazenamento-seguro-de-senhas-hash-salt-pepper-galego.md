---
type: source
title: "Armazenamento Seguro de Senhas: Hashing, Salting e Peppering (Galego)"
aliases: ["hash salt pepper galego", "introdução hashing senhas galego"]
date_created: 2026-08-26
date_updated: 2026-08-26
source_count: 0
tags: [segurança, criptografia, password-hashing, hashing, salt, pepper, argon2, mfa, rate-limiting, identity-provider]
skill: tech-mentor-security
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/armazenamento-seguro-de-senhas-hash-salt-pepper-galego.md
source_url: ""
author: "Augusto Galego"
date_published: ""
date_ingested: 2026-08-26
---

# Armazenamento Seguro de Senhas: Hashing, Salting e Peppering (Galego)

## TL;DR

Vídeo introdutório (autor explicitamente se declara não-especialista em cripto/segurança) sobre por que nunca armazenar senha em plaintext. Estrutura a explicação em torno de **dois modelos de ameaça** — ataque online (tentativa de login repetida) vs. ataque offline (vazamento do banco) — e mostra que hash + salt + pepper defende contra o offline, enquanto rate limit + MFA defende contra o online. Fecha com uma escada de recomendações práticas por nível de terceirização: lib consagrada (Argon2) → framework de auth (Better Auth) → identity provider completo (Clerk/Auth0/Cognito) → eliminar senha (Magic Link/login social).

## Contexto de Autoria

Autor identificado como [[wiki/entities/augusto-galego]] — autorreferência direta ("cupom galego") e estilo consistente com outras fontes já atribuídas a ele nesta wiki (conteúdo técnico introdutório com disclaimers explícitos de não-especialista, recomendação de curso pago próprio de System Design no encerramento).

## Key Claims

1. **Dois modelos de ameaça distintos para senha**: ataque online (adivinhação repetida via login) e ataque offline (banco de dados vazado). Hash/salt/pepper não impedem o ataque online — se o atacante puder tentar infinitamente, "alguma hora o login há de funcionar". Rate limit, bloqueio de conta após N tentativas e MFA são as defesas específicas do ataque online; hash/salt/pepper são a defesa do ataque offline. **Evidência**: explicação central do vídeo, ~primeiros 3 minutos de conteúdo técnico. Ver [[wiki/concepts/ataque-online-vs-offline-senha]] (novo).
2. **Hashing sozinho não basta** porque é determinístico — mesma senha, mesmos parâmetros, mesmo hash — o que habilita ataque de senhas pré-computadas e revela quando dois usuários compartilham senha. Consistente com [[wiki/concepts/hashing]] e [[wiki/concepts/ataque-pre-computacao]] já registrados.
3. **Função de hash para senha deve ser propositalmente lenta e cara em memória** — ao contrário de um hashmap de uso geral, que deve ser rápido. Argon2id citado como recomendação atual. Consistente com [[wiki/concepts/cpu-hard]], [[wiki/concepts/memory-hard]] e [[wiki/concepts/argon2]].
4. **Salt não precisa ser secreto**, só único por usuário e gerado por lib (não à mão) — consistente com [[wiki/concepts/salt]].
5. **Pepper é controverso por causa do blast radius do erro**: errar com o pepper no secrets manager (perdê-lo, trocar por engano, deploy errado) invalida **todas** as senhas do aplicativo de uma vez — nenhum usuário consegue mais logar, sem possibilidade de reconstrução. Esse framing específico do "risco de tudo-ou-nada" do pepper (vs. o registro já existente de [[wiki/concepts/pepper]], que fala de rotação) é um ângulo novo — reforça a mesma conclusão mas com ênfase na irreversibilidade do erro operacional, não só no custo de rotação planejada.
6. **Escada de recomendações práticas por terceirização crescente**: (a) usar lib consagrada de Argon2, nunca implementar hash/salt na mão; (b) usar framework de auth de mais alto nível como **Better Auth** — novo, não registrado na wiki; (c) terceirizar totalmente com identity provider — **Clerk**, **Auth0**, **Cognito** — nenhum desses três tinha página própria na wiki; (d) eliminar senha via **Magic Link** ou login social (Google/GitHub) — preferência pessoal do autor para SaaS B2C. Ver [[wiki/concepts/identity-provider-terceirizacao-autenticacao]] (novo).
7. **Cálculo do espaço de busca de senha** apresentado de forma didática: 26 (minúsculas) → 52 (+ maiúsculas) → 62 (+ dígitos) → mais ainda (+ caracteres especiais), como justificativa para políticas de complexidade de senha — o autor nota que essa exigência é "um pouco controversa" sem entrar no mérito.
8. **Menção qualitativa a computação quântica**: já existem testes com >1000 qubits, mas também já existem algoritmos de hashing considerados resistentes a ataque quântico — tratado en passant, sem detalhe técnico (o autor evita entrar em pós-quântica a fundo). Cruzar com [[wiki/concepts/post-quantum-cryptography]] e [[wiki/concepts/grover-algorithm]] já registrados com mais profundidade.

## Conceitos Tocados

[[wiki/concepts/hashing]], [[wiki/concepts/salt]], [[wiki/concepts/pepper]], [[wiki/concepts/argon2]], [[wiki/concepts/password-hashing]], [[wiki/concepts/cpu-hard]], [[wiki/concepts/memory-hard]], [[wiki/concepts/rainbow-table]], [[wiki/concepts/ataque-pre-computacao]], [[wiki/concepts/mfa-multifator-autenticacao]], [[wiki/concepts/rate-limiting]], [[wiki/concepts/ataque-online-vs-offline-senha]] (novo), [[wiki/concepts/identity-provider-terceirizacao-autenticacao]] (novo)

## Entidades

[[wiki/entities/augusto-galego]]

## Conexão com a Wiki Existente

Esta fonte **não contradiz** [[wiki/sources/seguranca-armazenamento-senhas-banco-de-dados]] (Renato Augusto) — cobre essencialmente o mesmo território técnico (plaintext → hash → salt → pepper/Argon2), mas com dois ângulos que a fonte anterior não tinha:

- A **distinção explícita online vs. offline** como eixo organizador de toda a explicação, algo que a fonte anterior não enquadrava dessa forma.
- A **escada de recomendação prática** terminando em identity providers nomeados (Clerk/Auth0/Cognito) e passwordless — a fonte anterior falava de Argon2id + pepper como estado da arte, mas não chegava a discutir terceirização completa da autenticação.

## Open Questions

1. Data de publicação do vídeo não identificada na transcrição — `date_published` deixado em branco.
2. "Better Auth" é citado no áudio como "Better Off" (erro de transcrição/pronúncia) — mantido como Better Auth por ser o framework real conhecido nesse espaço; se o usuário confirmar outro nome, corrigir.
3. Skill drift confirmado novamente: caminho de skills do `CLAUDE.md` (`/home/nemomartins/...`) não existe nesta máquina; usado o caminho real (`/home/gabriel-martins/Documentos/skills/`), consistente com ingestões anteriores.

## Raw Quotes

> "não existe armazenar a senha em texto plano, tá errado em todas as circunstâncias, em todas as situações"

> "quando a gente tá guardando uma senha, a gente quer que esse cálculo seja mais lento e mais difícil"

> "se você perder esse valor [pepper], nenhum usuário vai conseguir fazer login, você vai quebrar a produção para 100% dos usuários"

> "eu pessoalmente prefiro fazer um login via Google, via GitHub, via algo nesse sentido, porque eu elimino um pouco da dor de cabeça disso daqui"
