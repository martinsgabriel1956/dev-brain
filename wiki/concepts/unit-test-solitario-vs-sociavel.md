---
type: concept
title: "Unit Test Solitário vs. Sociável"
aliases: ["solitary unit test", "sociable unit test", "teste unitário solitário", "teste unitário sociável"]
date_created: 2026-07-07
date_updated: 2026-08-31
source_count: 6
tags: [testes, unit-test, tdd, martin-fowler, terminologia]
skill: tech-mentor-testing
status: stable
---

# Unit Test Solitário vs. Sociável

Distinção de Martin Fowler dentro do próprio "unit test": nem todo teste unitário isola tudo ao redor da unidade testada.

## Definição-raiz: o que faz um teste ser "de unidade"

Antes de solitário vs. sociável, há uma definição mais básica que as duas variações compartilham — fonte primária isolada em [[wiki/sources/unit-test-xunitpatterns]]: o que classifica um teste como "unit test" **não é a técnica usada** (isolar dependências com double ou não), é o **tamanho do SUT**. Um unit test exercita "um subconjunto muito pequeno do sistema geral" — possivelmente um único objeto ou método, "irreconhecível a quem não está envolvido em construir o software". A fonte contrasta isso com **customer test** (derivado dos requisitos, verificável pelo cliente) — os dois termos se definem um pelo oposto do outro. Solitário e sociável são duas formas de exercitar esse mesmo SUT pequeno, não duas definições concorrentes de "unidade".

## As duas variantes

- **Solitário**: todo elemento do programa fora da unidade sob teste (todo **DOC**, no vocabulário de [[wiki/sources/test-double-xunitpatterns-meszaros|Meszaros]] — ver definição isolada em [[wiki/sources/depended-on-component-doc-xunitpatterns]]) é substituído por um [[test-doubles|dublê]]. É o unit test "puro" no sentido mais restrito.
- **Sociável**: a unidade sob teste colabora com objetos reais internos do próprio processo — só dependências externas (rede, banco, serviços de terceiros) viram double.

## Por que isso importa: a segunda confusão em cima de "integration test"

Parte da comunidade adotou a definição restrita de unit test (só o solitário conta) e, com isso, passou a chamar de **"teste de integração"** o que é na verdade um **unit test sociável**. Isso empilha em cima da confusão já existente entre [[teste-de-integracao-estreito-vs-amplo|integração estreita e ampla]] — agora "integration test" pode significar três coisas diferentes dependendo de quem fala.

## Relação com as escolas de TDD

A distinção mapeia quase diretamente para as duas escolas descritas em [[tdd]]:

| Escola de TDD | Tipo de unit test predominante |
|---|---|
| London (Outside-In / Mockist) | Solitário — mocka todo colaborador ainda não existente |
| Detroit (Inside-Out / Classicist) | Sociável — usa objetos reais do domínio, mocka só I/O externo |

Na taxonomia de Meszaros, o eixo é **entrada indireta** (Stub/Mock controlam o que o SUT recebe) vs. **saída indireta** (Spy/Mock verificam o que o SUT dispara) — a escola London tende a Mocks (verifica interação), a Detroit tende a objetos reais + Stub só para I/O. Ver [[wiki/concepts/indirect-input-output]] e [[wiki/sources/test-double-xunitpatterns-meszaros]].

## Como Fowler resolve na própria escrita

Continua usando "unit test" para os dois casos, qualificando com **"solitary"** ou **"sociable"** apenas quando a distinção muda o argumento. Não adota um termo novo para substituir "unit test" (diferente do que faz com "integration test", que ele troca por "system test"/"narrow integration test").

## Ver também

- [[tdd]] — escolas London/Detroit como manifestação prática dessa distinção
- [[test-doubles]] — o mecanismo que torna um teste solitário
- [[teste-de-integracao-estreito-vs-amplo]] — confusão irmã sobre o termo "integration test"
- [[wiki/entities/martin-fowler]]

## Key Sources

- [[wiki/sources/integration-test-martin-fowler]]
- [[wiki/sources/test-double-xunitpatterns-meszaros]] — vocabulário entrada/saída indireta que distingue o double que torna um teste solitário
- [[wiki/sources/depended-on-component-doc-xunitpatterns]] — fonte primária isolada do termo DOC, o "todo elemento fora da unidade" que define solitário
- [[wiki/sources/indirect-input-xunitpatterns]] — fonte primária isolada da metade "entrada" desse eixo
- [[wiki/sources/control-point-xunitpatterns]] — fonte primária isolada do termo control point, o mecanismo formal de comando ao SUT usado tanto no double quanto no exercise SUT
- [[wiki/sources/teste-unitario-integracao-e2e-opiniao]] — exemplo do teste de `add` que "sociabiliza" ao passar a chamar `db.save` real via SQLite, deixando de ser solitário
- [[wiki/sources/unit-test-xunitpatterns]] — fonte primária isolada da definição-raiz de "unit test": critério é o tamanho do SUT, não a técnica de isolamento; contraste formal com customer test
