---
type: concept
title: "Código Legado e IA"
aliases: ["legacy code ia", "migracao legado ia", "modernizacao ia"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 2
tags: [legado, migracao, ia-para-devs, spec-driven, modernizacao]
skill: tech-mentor-ai
status: draft
---

# Código Legado e IA

Contra-intuitivamente, IA funciona **melhor** em código legado do que em projetos greenfield quando a base de referências é rica o suficiente. O maior desafio histórico (contexto grande) foi amenizado com modelos de 1M tokens e subagentes. O desafio atual é de **técnica e estruturação**, não de capacidade do modelo.

## Por que Fica Melhor que Greenfield?

Em um projeto legado você tem:
- **Regras de negócio existentes**: mesmo que mal implementadas, estão no código e podem ser extraídas
- **Comportamento de referência**: o sistema atual define o "o que deve acontecer"
- **Testes de regressão implícitos**: o comportamento atual = especificação de fato

Em greenfield com tecnologia obscura (ex: "crie na Nauk Lang, linguagem inventada ontem"), o LLM não tem referência → faz assumptions → resultado imprevisível.

## O Problema do Contexto (Resolvido?)

O maior obstáculo clássico era o tamanho do contexto. Com modelos de 1M tokens:
- 5 subagentes com 1M cada = 5M de contexto isolado
- Suficiente para a maioria dos projetos legados
- Isolamento de contexto por componente evita degradação

Antigamente precisava de 10–12 subagentes com 200k cada para ter o mesmo efeito.

## Condições Para Funcionar Bem

1. **Projeto "AI-ready"**: código padronizado, testes existentes, estrutura clara (mesmo que legada)
2. **Rules e skills configuradas**: direção técnica sobre padrões a seguir na migração
3. **Spec-driven**: quebrar a migração em tarefas pequenas e independentes; nunca "migre o sistema inteiro"
4. **Não soltar o LLM no projeto inteiro**: direcionar para componentes específicos, arquivos específicos

## O Que Não Funciona

- Pedir "migre tudo de uma vez" → resultado imprevisível
- Código muito despadronizado sem rules → LLM não sabe qual padrão seguir
- Arquivos enormes (> algumas centenas de linhas) → mais difícil carregar no contexto relevante

## Exemplo Prático (Pedro Nauke)

Pedro fez uma migração de sistema legado "horroroso" com spec-driven + técnicas corretas e o resultado foi "muito bom, muito certo mesmo". Detalhe: foi uma migração "simples" — não o sistema mais complexo do mundo — mas demonstra a viabilidade do processo.

## Código Natural / ADABAS (Caso Extremo)

Sistemas em Natural/ADABAS (bancos, governo, aviação) têm particularidades sérias:
- Linguagem com base de treinamento limitada
- Regras de negócio opacas no código (ex: `if amanhã for feriado` sem documentação)
- Nenhuma documentação de intenção

Para esses casos, a abordagem de **reconstruir a partir da documentação oficial** (leis, specs regulatórias) pode ser mais eficaz do que tentar extrair lógica do código.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-02-mercado-perfil-profissional]]
- [[wiki/sources/formacao-ia-devs-aula-06-qa]]
