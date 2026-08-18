---
type: concept
title: "Divisão de Tarefas em Partes Menores"
aliases: ["quebrar tarefa em partes menores", "duas perguntas de decomposição", "critério de parada da decomposição"]
date_created: 2026-07-23
date_updated: 2026-08-18
source_count: 2
tags: [carreira, decomposicao-de-tarefas, junior, planejamento, estimativa]
skill: tech-mentor-leadership
status: draft
---

# Divisão de Tarefas em Partes Menores

Técnica para tornar uma tarefa que parece difícil em algo executável: dividir repetidamente até conseguir responder duas perguntas de teste. Diferente da [[wiki/concepts/arvore-de-decomposicao]] — que decompõe um **problema vago** em dimensões de investigação (onde, quando, para quem) — esta técnica decompõe uma **tarefa já definida** (um cartão de board, uma atividade de cronograma) em subtarefas executáveis, com um critério de parada operacional.

## As Duas Perguntas de Teste

Depois de dividir uma tarefa, pergunte:

1. **Eu tenho segurança para fazer isso, do jeito que está descrito?**
2. **Eu consigo dar um prazo para essa tarefa?**

Se a resposta a ambas for sim, a tarefa está no nível de granularidade certo para executar. Se não, divida em duas partes e repita o teste para cada parte, recursivamente.

## Por Que Essas Duas Perguntas Funcionam

Segurança indica compreensão — só é possível se sentir seguro para executar algo que já faz sentido. Conseguir dar um prazo indica que o escopo é conhecido o suficiente para ser mensurável. A analogia usada na fonte: ninguém consegue estimar quanto tempo leva para construir uma casa do zero (terreno vazio, fundação desconhecida), mas qualquer pessoa consegue estimar quanto tempo leva para pintar uma parede já pronta — mesmo sem ser pintor profissional. A diferença não é a dificuldade técnica da tarefa em si, é a clareza do escopo.

## O Limite Inferior — Regra da Divisibilidade Entre Pessoas

Existe um risco oposto: dividir demais. O critério de parada é perguntar se a subtarefa atual ainda pode ser dividida **entre duas pessoas diferentes** sem gerar conflito (ex.: duas pessoas mexendo no mesmo método vão gerar conflito de merge — nesse ponto, a tarefa já não é mais divisível de forma útil). Se a resposta for não, a tarefa já está simples o suficiente e subdividir mais atrapalha em vez de ajudar.

Essa regra serve como régua dupla:

- **Raso demais** → ainda não respondeu as duas perguntas de teste (segurança + prazo).
- **Fundo demais** → a tarefa já não é divisível entre pessoas diferentes.

## Exemplo do Processo

```
Alterar um cadastro (não sei bem o que precisa mudar)
├── Parte do banco de dados (nova query)
│   ├── Ainda não seguro/sem prazo → divide de novo
│   ├── Montar a query
│   └── Conectar no banco (ex.: Dapper)
└── Parte da tela (novo campo)
    └── Seguro + com prazo → pronto para executar
```

## Quando a Divisão Sozinha Não Basta — Sistemas Ainda Desconhecidos

[[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] adiciona um pré-requisito a este processo, em escala de sistema (não de tarefa de board já definida): quando o próprio problema envolve algo que a equipe nunca fez, tentar aplicar diretamente as duas perguntas de teste ("tenho segurança?", "consigo dar um prazo?") tende a falhar, porque a insegurança não vem da tarefa ser mal descrita — vem de uma incerteza de fundo ainda não resolvida (viabilidade técnica desconhecida). Nesses casos, a fonte recomenda [[wiki/concepts/reducao-de-incerteza-antes-de-estimar|reduzir a incerteza primeiro]] (testar as partes menos conhecidas via PoC) e só então desenhar o sistema e aplicar esta técnica de quebra em subtarefas — a mesma fonte reforça "tarefas pequenas e bem definidas" e "priorizar o menos conhecido" como boas práticas de quebra, ecoando as duas perguntas de teste já registradas acima.

## Relação com Outros Conceitos

- [[wiki/concepts/arvore-de-decomposicao]] — decompõe problemas vagos em dimensões de investigação; esta técnica decompõe tarefas já definidas em subtarefas executáveis, com critério de parada explícito
- [[wiki/concepts/estimativa-como-habilidade-treinavel]] — a segunda pergunta de teste ("consigo dar um prazo?") é o mesmo músculo de estimativa que se treina deliberadamente
- [[wiki/concepts/organizacao-pessoal-do-trabalho]] — a lista de subtarefas gerada por esta divisão é o material bruto da lista de tarefas priorizada
- [[wiki/concepts/reducao-de-incerteza-antes-de-estimar]] — pré-requisito para esta técnica funcionar quando o sistema em si (não só a tarefa) envolve algo desconhecido

## Key Sources

- [[wiki/sources/como-lidar-com-tarefas-dificeis-sendo-junior]]
- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — "tarefas pequenas e bem definidas" e "priorizar o menos conhecido" como boas práticas complementares, em escala de desenho de sistema
