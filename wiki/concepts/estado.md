---
type: concept
title: "Estado"
aliases: ["state", "program state", "estado do sistema"]
date_created: 2026-05-13
date_updated: 2026-07-21
source_count: 2
tags: [estado, state, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Estado

O que o sistema precisa **lembrar** para tomar decisões ao longo de sua execução. É a memória operacional do programa em um dado momento.

## Definição operacional

Estado é qualquer variável cujo valor influencia o comportamento futuro do sistema. Sem estado, o sistema tomaria as mesmas decisões independentemente do histórico.

## Exemplo clássico: contador de tentativas

No caixa eletrônico, o sistema não bloqueia o cartão na primeira senha errada nem na segunda — decide baseado em **quantas vezes o usuário já errou**. Esse contador é o estado:

```python
tentativas = 0  # estado inicial

while tentativas < MAX_TENTATIVAS:
    if senha_correta(...):
        return True
    tentativas += 1  # mutação de estado

bloquear_cartao()  # decisão baseada no estado acumulado
```

## Tipos de estado (expandir com novos sources)

- **Local:** existe dentro de uma função (ex: `tentativas` acima)
- **Compartilhado:** acessível por múltiplas partes do sistema
- **Persistido:** salvo em banco de dados entre sessões

## Relação com outros conceitos

- É o que diferencia fluxos com memória de fluxos sem memória
- Complicações de estado compartilhado são a raiz de muitos bugs de concorrência
- Em frontend: gerenciado por useState, Zustand, Redux etc.
- [[wiki/concepts/maquina-de-estados-ui]] — aplicação deste conceito especificamente a componentes de interface (loading, erro, sucesso), incluindo o anti-padrão de estados mutuamente exclusivos coexistindo

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]]
- [[wiki/sources/5-boas-praticas-uiux-ux-pilot]]
