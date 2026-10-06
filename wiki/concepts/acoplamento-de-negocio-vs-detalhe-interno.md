---
type: concept
title: "Acoplamento de Negócio vs. Detalhe Interno"
aliases: ["acoplamento legítimo vs não saudável", "acoplamento ao status"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [acoplamento, microsservicos, contrato, decisao-arquitetural]
skill: tech-mentor-system-design
status: stub
---

# Acoplamento de Negócio vs. Detalhe Interno

Pergunta-guia de [[wiki/concepts/acoplamento]]: *se eu mudar B, o que preciso mudar em A?*

- **Legítimo:** vem de regra de negócio. Ex.: a matrícula só libera o curso depois que a cobrança confirma o pagamento. O acoplamento deve se restringir ao **contrato** (o *status* confirmado/pendente).
- **Não saudável:** A consulta o banco de B, manipula seus objetos ou chama serviços internos. Mudar o formato do endereço da cobrança (`address` → `street`, `number`, bairro) obriga a alterar a matrícula, embora a única dependência real fosse o status.

**Teste:** um problema numa parte impede outra de funcionar sem haver necessidade de negócio entre elas? Então o acoplamento não é saudável. Complementa [[wiki/concepts/acoplamento-desejavel-vs-indesejavel]] (critério focado em testabilidade). Remédios: contrato explícito, [[wiki/concepts/comunicacao-assincrona]] por eventos, [[wiki/concepts/ports-adapters]].

## Key sources

- [[wiki/sources/introducao-arquitetura-de-software-conceitos-decisoes-kiper-academy]]
