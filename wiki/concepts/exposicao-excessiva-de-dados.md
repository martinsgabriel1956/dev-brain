---
type: concept
title: "Exposição Excessiva de Dados (Excessive Data Exposure)"
aliases: ["excessive data exposure", "over-exposure", "data exposure", "vazamento de dados por api"]
date_created: 2026-07-04
date_updated: 2026-07-04
source_count: 1
tags: [data-exposure, api-security, appsec, data-privacy, owasp]
skill: tech-mentor-security
status: stable
---

# Exposição Excessiva de Dados (Excessive Data Exposure)

Vulnerabilidade onde o backend devolve a entidade completa do banco em vez de projetar apenas os campos que o frontend de fato precisa exibir. O bug não está em nenhum campo específico vazando sozinho — está em buscar/serializar o objeto inteiro e assumir, incorretamente, que "o frontend só vai usar o que precisa".

## O padrão do bug

```
GET /products/42
→ retorna o produto e os dados do vendedor
→ o vendedor inclui nome e foto (o que a UI mostra)
→ mas também e-mail, CPF, telefone, endereço, senha criptografada
   (porque a query trouxe a entidade Seller inteira)
```

Nenhum desses campos extras aparece na tela — mas todos chegam no payload da resposta, visíveis em qualquer inspeção de rede.

## Correção

Nunca confiar que o cliente vai ignorar campos não exibidos. Projetar explicitamente a resposta com só o necessário:

```typescript
// VULNERÁVEL — expõe o Seller inteiro
const product = await db.product.findUnique({
  where: { id },
  include: { seller: true }
})

// CORRETO — projeta só os campos públicos do vendedor
const product = await db.product.findUnique({
  where: { id },
  include: { seller: { select: { name: true, avatarUrl: true } } }
})
```

## Ver também

- [[wiki/concepts/data-privacy]] — princípio geral de minimização de dados (PII, DLP)
- [[wiki/concepts/idor]] — falha relacionada de exposição, mas por falta de checagem de ownership em vez de falta de projeção de campos

## Key Sources

- [[wiki/sources/vulnerabilidades-comuns-seguranca-apps]]
