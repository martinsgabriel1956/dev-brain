---
type: concept
title: "Validação de Entrada"
aliases: ["input validation", "validação de dados", "nunca confie no client"]
date_created: 2026-07-09
date_updated: 2026-11-16
source_count: 11
tags: [validacao, seguranca, backend, regra-de-negocio, arquitetura-em-camadas, celebrate, joi, schema-validation]
skill: tech-mentor-backend
status: stub
---

# Validação de Entrada

O backend nunca pode confiar no que vem do cliente. Quantidade negativa, e-mail malformado, preço recalculável a partir do que o cliente mandou — tudo isso precisa ser barrado ou recalculado antes de tocar a regra de negócio.

## Caso concreto: validação de e-mail

"E-mail malformado" não é um conceito único — [[wiki/sources/email-address]] mostra que a spec formal (RFC 5322/5321) e a prática de mercado divergem em pontos que uma validação ingênua costuma errar:

- A parte local é *tecnicamente* case-sensitive pela RFC, mas todo provedor trata como case-insensitive na prática — validar case-sensitivity estrita rejeita endereços válidos por convenção de mercado.
- `user+tag@domain.com` (sub-addressing, RFC 5233) é sintaxe formalmente válida e suportada por Gmail, Outlook.com, Yahoo Mail Plus, iCloud e Proton Mail — uma regex que rejeita `+` na parte local está rejeitando endereços reais.
- Correção sintática (regex, HTML5 form validation) **não prova** que a caixa existe. A única validação confiável de existência é um link de confirmação enviado ao próprio endereço — callback verification direta (conectar na caixa e checar) existe mas arrisca directory harvest attacks e denúncias de spam.

## Separação em camadas

Uma forma comum de organizar essa proteção:

| Camada | Responsabilidade |
|---|---|
| Controller | Entende de HTTP — parse, status codes |
| Service | Entende de regra de negócio — validação, cálculo |
| Banco | Guarda os dados |

Essa separação evita que a regra crítica se espalhe por múltiplos lugares do código. Quando a regra fica espalhada, o sistema pode começar a se contradizer — dois pontos de entrada validando a mesma coisa de formas diferentes.

## Validação de Schema como Middleware (Celebrate + Joi)

Em Node/Express, uma forma concreta de aplicar essa camada é um middleware de validação de schema entre a rota e o handler: **Celebrate** (usando **Joi** para descrever o schema) verifica, antes de qualquer lógica rodar, se cada segmento da requisição (params, query, body) bate com o tipo/formato esperado — ex.: `celebrate({ [Segments.PARAMS]: Joi.object({ id: Joi.number() }) })` garante que `id` só pode ser número. Se vier fora do formato (ex.: uma tentativa de [[wiki/concepts/sql-injection]] como `1 OR 1=1`), a requisição é rejeitada com erro antes de tocar o banco. Ver demonstração completa em [[wiki/sources/injecao-sql-aula-modulo-seguranca]].

Essa camada **não substitui** a query parametrizada (placeholders `$1`/`$2`) — é defesa adicional na borda, mesma lógica de "nunca confiar no client" já descrita acima.

## Por Que Validação de Formato Não Basta Contra SQL Injection

[[wiki/sources/sql-injection-guia-completo-solucoes-galego]] argumenta que validar apenas o *formato* de um campo (ex.: Zod garantindo que um e-mail "parece" um e-mail) é uma defesa fraca contra [[wiki/concepts/sql-injection]] quando usada isoladamente, por dois motivos: (1) o comportamento interno do validador é opaco — não se sabe qual regex/máquina de estados ele usa, e até e-mails sintaticamente válidos podem ser estranhos o suficiente para escapar de uma checagem ingênua; (2) campos de texto livre (ex.: descrição de produto) só validados como "é uma string" não barram um payload SQL embutido no meio do texto. A validação de formato pega casos estreitos (um parâmetro numérico, como no exemplo Celebrate/Joi acima) — não generaliza para qualquer input.

## Relação com outros conceitos

- [[wiki/concepts/contrato-de-api]] — o contrato define o formato esperado; a validação garante que ele é respeitado em runtime
- [[wiki/concepts/autenticacao-e-autorizacao]] — validação de identidade/permissão é uma forma específica de validação de entrada
- [[wiki/concepts/sql-injection]] — validação de schema é camada adicional, não substituta, da parametrização de query
- Ver detalhamento em `references/api-design.md` e `references/cors-security.md` (tech-mentor-backend) para validação na borda (input sanitization, output encoding)

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], os valores de `req.body` vão direto para o INSERT, sem validação no servidor. Só valem o `required` e o `type="url"` do navegador, que qualquer requisição feita fora da página ignora.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], `Number()` e `String()` nos params e no query servem só para calar o TypeScript, e nada é validado (`items=abc` vira `NaN`, filtro sem `city` procura "undefined"). Mesma lacuna do [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta|dia 5 de Mayk]].

Em [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]], o formulário React envia `'0'` como UF ou cidade e `[0, 0]` como posição quando nada é escolhido: sem `required`, sem checagem antes do `api.post`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]], UF e cidade são digitadas livremente e comparadas por igualdade exata no back-end: "rio do sul" não acha "Rio do Sul".

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], a validação finalmente chega ao back-end com celebrate e Joi (`abortEarly: false`, 400 com todas as mensagens). Ficam brechas: o arquivo grava antes de validar, a imagem não é obrigatória (500), e `uf` aceita "s".

## Na NLW #2, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]], a página de estudo confere só se os filtros existem (`if (!filters.subject || !filters.weekday || !filters.time)`), não se são números válidos. O cadastro não confere nada antes de gravar. Validar tipo e formato e usar placeholders `?` fecharia a injeção.

## Key sources

- [[wiki/sources/10-conceitos-fundamentais-backend]]
- [[wiki/sources/injecao-sql-aula-modulo-seguranca]] — exemplo prático de validação de schema (Celebrate/Joi) como camada extra contra SQL Injection
- [[wiki/sources/email-address]] — sintaxe formal RFC 5322 de e-mail vs. práticas reais de validação de provedores
- [[wiki/sources/sql-injection-guia-completo-solucoes-galego]] — validação de formato como defesa fraca isolada contra SQLi: comportamento opaco do validador e campos de texto livre não cobertos
- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — 'valide, pesquise, entenda a regra de negócio'; preço/estoque negativos como entrada/estado inválido
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: sem validação no servidor no Ecoleta
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: coerção de tipos no lugar de validação
- [[wiki/sources/nlw-1-diego-fernandes-dia-3-front-end-react-typescript-leaflet-ecoleta]]: front-end sem validação: '0' e [0,0] vão para a API
- [[wiki/sources/nlw-1-diego-fernandes-dia-4-mobile-react-native-expo-ecoleta]]: texto livre comparado por igualdade
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: celebrate/Joi no POST e o que ficou de fora
- [[wiki/sources/nlw-2-dia-5-banco-de-dados-sqlite-proffy]]: NLW #2, dia 5: só checa presença dos filtros
