---
type: concept
title: "Microsoft SQL Server"
aliases: ["sql server", "mssql", "sqlserver"]
date_created: 2026-07-27
date_updated: 2026-07-27
source_count: 1
tags: [sql-server, banco-de-dados, relacional, microsoft, backend]
skill: tech-mentor-backend
status: stub
---

# Microsoft SQL Server

Banco relacional cuja escolha faz mais sentido operacional do que técnico: quando a empresa já respira Windows, .NET, Excel e Power BI, a integração nativa elimina fricção que existiria com outros bancos.

## Limites por Edição

- **Express (gratuita)**: 10 GB de tamanho máximo por banco, 1 socket/4 cores de CPU, 1 GB de RAM para buffer pool. Degradação sensível acima de ~50 usuários simultâneos escrevendo ativamente.
- **Standard (paga)**: eleva o teto para 128 GB de memória e remove o limite de tamanho de banco. Para médias empresas, aguenta 200–1.000 conexões simultâneas dependendo do hardware.

## Diferencial Real

O **SSMS** (SQL Server Management Studio) é a ferramenta gráfica de administração de bancos mais completa disponível. Integração nativa com Power BI/Excel via Power Query, e SSIS para ETL.

## Quem Usa

Empresas de médio porte com stack Microsoft, mercado financeiro com Excel conectado via Power Query, ERPs como SAP em algumas configurações.

## Key Sources

- [[wiki/sources/como-escolher-banco-de-dados-historia-acid-cap]]
