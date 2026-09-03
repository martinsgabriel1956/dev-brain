---
type: concept
title: "Serviços de Domínio (Domain Services, granularidade intermediária)"
aliases: ["domain services", "serviços de domínio", "monolitos agrupados por domínio"]
date_created: 2026-09-01
date_updated: 2026-09-01
source_count: 1
tags: [servicos-de-dominio, monolito, microsservicos, arquitetura, backend]
skill: tech-mentor-backend
status: stub
---

# Serviços de Domínio (granularidade intermediária)

Nível de escala arquitetural entre o [[wiki/concepts/monolito|monolito]] tradicional e [[wiki/concepts/microsservicos|microsserviços]]: em vez de quebrar um grande monolito em serviços muito granulares, ele é quebrado em vários monolitos menores, cada um agrupando uma parte específica do domínio inteira (não uma entidade isolada). Cada serviço de domínio pode ter time dono e ser escalado como unidade — mas ainda não permite escalar partes específicas *dentro* do domínio: escalar significa escalar o serviço inteiro, que ainda pode ser grande.

## Posição na Escala de Custo/Granularidade

Custo médio, escala média — trade-off intermediário entre as duas pontas:

| | Monolito único | Serviços de domínio | Microsserviços |
|---|---|---|---|
| Granularidade | Nenhuma | Média | Alta |
| Custo operacional | Baixo | Médio | Alto |
| Flexibilidade de escala | Nenhuma | Parcial (por domínio) | Total (por serviço) |

## Origem

Termo usado em [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] como um dos três caminhos de escala além do monolito tradicional, ao lado de [[wiki/concepts/monolito-modular|monolito modular clássico]] e [[wiki/concepts/composicao-de-modulos|composição de módulos]]. Não tem correspondência direta nomeada em `references/architecture-foundations.md` da skill `tech-mentor-backend` — possivelmente equivalente ao que a skill trataria como "extração parcial por bounded context" antes de chegar a microsserviços completos; open question registrada na fonte até uma referência futura confirmar ou renomear.

## Key Sources

- [[wiki/sources/evoluir-software-sem-pagar-preco-de-microsservicos]] — único registro deste conceito na wiki até o momento
