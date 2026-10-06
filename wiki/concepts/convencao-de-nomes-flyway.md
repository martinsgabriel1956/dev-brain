---
type: concept
title: "Convenção de Nomes do Flyway"
aliases: ["V1__", "versioned migrations", "db/migration"]
date_created: 2026-10-06
date_updated: 2026-10-06
source_count: 1
tags: [flyway, migrations, convencao, spring-boot]
skill: tech-mentor-backend
status: draft
---

# Convenção de Nomes do Flyway

Os scripts ficam em `src/main/resources/db/migration` (caminho padrão `classpath:db/migration`) e seguem `V<versão>__<descrição>.sql`:

| Parte | Regra |
|---|---|
| `V` | maiúsculo, obrigatório |
| `<versão>` | número que define a ordem (`1`, `2`...) |
| `__` | **dois** underscores, obrigatório |
| `<descrição>` | livre (`create_cliente`, `cpf_cliente`) |

Sem o prefixo `V<n>__`, o [[wiki/entities/flyway]] não reconhece o arquivo como migration. Exemplos do demo: `V1__create_cliente.sql`, `V2__cpf_cliente.sql`.

## Notas `[skill: tech-mentor-backend]`

- Versões com ponto (`V2.1__...`) são aceitas; `R__` indica migrations repetíveis. **[external, não verificado]**
- `out-of-order: false` impede aplicar versão menor que já passou.
- Convenção de versão sobre time grande (duas pessoas criando a mesma `V3`) não é tratada na fonte.

## Key sources

- [[wiki/sources/migrations-flyway-spring-boot-versionamento-de-banco]]
