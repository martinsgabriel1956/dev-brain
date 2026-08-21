---
type: concept
title: "Lasagna Code"
aliases: ["lasagna code", "codigo lasanha", "código lasanha"]
date_created: 2026-08-14
date_updated: 2026-08-14
source_count: 1
tags: [lasagna-code, anti-patterns, acoplamento, arquitetura, camadas]
skill: tech-mentor-backend
status: stub
---

# Lasagna Code

Anti-padrão da família das "massas" (ao lado de [[wiki/concepts/code-espaguete|espaguete]] e [[wiki/concepts/ravioli-code|ravióli]]): código organizado em **camadas tão entrelaçadas que uma mudança em uma camada obriga a mudar as outras**. A aparência é ordenada — há camadas —, mas o [[wiki/concepts/acoplamento|acoplamento]] entre elas anula o benefício da estratificação.

## Contraste com camadas saudáveis

A [[wiki/concepts/arquitetura-em-3-camadas|arquitetura em camadas]] pressupõe que cada camada dependa só da interface da camada abaixo. No lasagna code as camadas vazam umas nas outras (viola [[wiki/concepts/separation-of-concerns|separação de interesses]] e [[wiki/concepts/dependency-inversion-principle|inversão de dependência]]), então elas deixam de ser substituíveis independentemente. É o oposto do que [[wiki/concepts/clean-architecture|Clean Architecture]] busca com dependências apontando só para dentro.

## Relacionado

[[wiki/concepts/code-espaguete]] · [[wiki/concepts/ravioli-code]] · [[wiki/concepts/big-ball-of-mud]] · [[wiki/concepts/acoplamento]]

## Key Sources

- [[wiki/sources/codigo-espaguete-wikipedia]] — definição do termo na seção de anti-padrões relacionados
