---
type: concept
title: "Data Clumps"
aliases: ["grupos de dados", "data clump", "parâmetros que deveriam ser um tipo"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [data-clumps, code-smells, coesao, tipagem, clean-code]
skill: tech-mentor-backend
status: stub
---

# Data Clumps

Ocorre quando um conjunto de variáveis que sempre aparece junto (ex.: `nome`, `email`, `idade`) é passado solto — como argumentos separados — em vez de agrupado num tipo nomeado. É um smell de **coesão** ([[wiki/concepts/coesao]]): dados que pertencem conceitualmente juntos deveriam estar estruturalmente juntos.

## Exemplo

```
# data clump — três parâmetros que sempre viajam juntos
def criar_usuario(nome: str, email: str, idade: int): ...
def atualizar_usuario(nome: str, email: str, idade: int): ...

# agrupado — o tipo nomeia o conceito
@dataclass
class Usuario:
    nome: str
    email: str
    idade: int

def criar_usuario(usuario: Usuario): ...
```

## Por que importa (além de legibilidade)

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] destaca o benefício de manutenção ao evoluir o conceito: substituir `idade` por `data_de_nascimento` (calculando idade dinamicamente) é uma mudança localizada na definição de `Usuario` — todo lugar que acessa `usuario.idade` passa a acusar erro automaticamente via type-checker/compilador. Sem o agrupamento, a mesma mudança exige caçar manualmente todos os lugares do código que recebiam `nome`, `email`, `idade` como três parâmetros soltos, sem nenhuma garantia mecânica de já ter encontrado todos.

## Relacionado

[[wiki/concepts/code-smells]] · [[wiki/concepts/coesao]] · [[wiki/concepts/primitive-obsession]] (mesma lógica de dar um tipo nomeado a um conceito, aplicada a um valor único em vez de um agrupamento)

## Key Sources

- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]]
