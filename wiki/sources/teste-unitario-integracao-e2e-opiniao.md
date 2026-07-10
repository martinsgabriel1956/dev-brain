---
type: source
title: "Testes Unitários, Integração e E2E — uma conversa opinativa"
aliases: ["opinião sobre pirâmide de testes", "alocação de recursos em testes"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/teste-unitario-integracao-e2e-opiniao.md
source_url: ""
author: "criador de conteúdo (canal não identificado na transcrição)"
date_published: 2026-07-10
date_ingested: 2026-07-10
source_count: 0
tags: [testes, pirâmide, unitário, integração, e2e, mocks, alocação-de-recursos, opinião]
skill: tech-mentor-testing
status: stable
---

# Testes Unitários, Integração e E2E — uma conversa opinativa

## TL;DR

Vídeo deliberadamente opinativo (não um tutorial) sobre os três níveis clássicos de teste. A tese central: teste nunca previne bug 100% — só previne a *regressão* de bugs que alguém já pensou em testar. A escolha de quanto investir em cada camada é, antes de tudo, um problema de alocação de recursos, não uma pirâmide fixa a ser seguida. O autor defende que o *sweet spot* de valor está em testes de integração que validam uma regra de negócio de ponta a ponta (ex.: criar e depois buscar um recurso), e que testes E2E ganham valor desproporcional em código legado sem dono, mas perdem valor em produtos que mudam de UI/fluxo com frequência (startups em pivot constante).

## Key Claims

**Claim:** 100% de cobertura de teste não garante ausência de bugs — só garante que um comportamento específico, já pensado, não regride.
**Evidence:** Exemplo do integer overflow em Java: se o autor do teste não sabe que overflow pode ocorrer, nenhum caso de teste vai cobrir esse cenário, não importa quantas vezes a mesma linha seja executada nos testes. É possível ter "500% de testagem" e zero testes relevantes.
**Confidence:** alta

**Claim:** Bom teste precisa ser determinístico, conciso, relevante, compreensível e durável — e testes unitários "de livro" (ex.: `add(2,3) == 5`) frequentemente falham no critério de relevância.
**Evidence:** Testes flaky (não determinísticos) devem ser deletados, não mantidos. Testar `add` com número negativo e com zero é conciso e compreensível, mas raramente relevante — o autor considera que, nesse exemplo, só testar decimais/fracionados e os limites do tipo numérico seria de fato útil.
**Confidence:** alta

**Claim:** Mockar o banco de dados num teste unitário permite verificar que `db.save` foi chamado, mas não verifica que o dado foi de fato persistido — para isso, o teste precisa deixar de ser puramente unitário (ex.: usar SQLite real) e vira teste de integração.
**Evidence:** Assertion sobre chamada de mock (`db.save` foi chamado com X) não é o mesmo que buscar o dado de volta no banco para confirmar persistência.
**Confidence:** alta

**Claim:** Teste de integração que moca o próprio banco de dados pode "não integrar muito bem" — se o double não foi pensado com os mesmos problemas do banco real, o teste não valida nada sobre o banco.
**Evidence:** Recomendação de ter um banco de dados dedicado a testes (mesmo motor de produção, dados isolados) em vez de mock, aceitando o custo de mais tempo (criar o banco no CI).
**Confidence:** alta

**Claim:** Testes E2E ganham valor extremo em código legado sem dono conhecido — permitem refatorar um "monolito espaguete" com confiança — mas perdem valor em produtos que pivotam com frequência e mudam a UI constantemente.
**Evidence:** Testes E2E dependem de seletores de UI (ex.: id de campo de formulário) que quebram quando a interface muda, mesmo que o comportamento do sistema continue correto. Quanto mais frágil e mudança de fluxo, menos duráveis os testes E2E se tornam.
**Confidence:** alta

**Claim:** Em sistemas com dependências externas (ex.: provedor de pagamentos, fornecedor), "ponta a ponta" é ambíguo — pode significar bater nos ambientes de staging reais dessas dependências, ou mockar as pontas e testar só o sistema próprio, com suítes separadas testando cada dependência externa isoladamente.
**Evidence:** O autor descreve como opção viável: testar o PSP separadamente, testar o fornecedor separadamente, e mockar ambos no teste do sistema principal — mais caro e complexo, mas justificável em fluxos cruciais (signup, login).
**Confidence:** média (o autor reconhece que nunca viu duas empresas fazerem E2E da mesma forma)

**Claim:** O maior valor de um teste (de qualquer camada) está em validar que um caso de uso segue a regra de negócio esperada — ex. criar e buscar um usuário, aplicar desconto e conferir o preço resultante, ou validar que apenas usuário admin pode criar produto.
**Evidence:** Descrito como o "sweet spot" pessoal do autor: teste de integração que exercita o fluxo de criação seguido de leitura, validando a regra de negócio de ponta a ponta sem precisar mockar toda a stack.
**Confidence:** alta

## Conceitos & Entities Tocados

[[wiki/concepts/piramide-de-testes]] · [[wiki/concepts/criterios-de-bom-teste]] · [[wiki/concepts/test-doubles]] · [[wiki/concepts/teste-de-integracao-estreito-vs-amplo]] · [[wiki/concepts/unit-test-solitario-vs-sociavel]] · [[wiki/concepts/testar-proprio-codigo]] · [[wiki/concepts/testes-integracao-banco-real]] · [[wiki/concepts/gaming-de-testes-por-ia]] · [[wiki/concepts/contract-testing]] · [[wiki/concepts/tdd]]

## Open Questions

- O autor não identifica o canal/nome próprio na transcrição — entidade de autoria não pôde ser criada com confiança.
- Qual seria, na prática do autor, o critério objetivo para decidir quando vale mockar um PSP externo vs. testar contra o staging real dele?
- A afirmação de que "teste de integração acaba testando um pouco da infraestrutura, mas às vezes passa mesmo sem a infra funcionar" fica em aberto — não há detalhamento de como mitigar esse blind spot.
