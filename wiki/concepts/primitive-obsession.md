---
type: concept
title: "Primitive Obsession"
aliases: ["uso exacerbado de tipos primitivos", "obsessão por primitivos"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [primitive-obsession, code-smells, tipagem, validacao, clean-code]
skill: tech-mentor-backend
status: stub
---

# Primitive Obsession

Representar conceitos de domínio (e-mail, dinheiro, CPF, etc.) usando tipos primitivos crus (`string`, `int`) em vez de um tipo dedicado. O problema não é o primitivo em si — é que uma `string` não carrega informação sobre **se já foi validada**, então o sistema não tem como garantir, em nenhum ponto de uso, que aquele dado está num estado consistente.

## Consequência prática

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] usa e-mail como exemplo: se `email` é sempre `string`, uma função como `send_email()` não sabe se o valor recebido já foi validado em algum ponto anterior do fluxo. Isso leva a dois cenários ruins, ambos comuns:

- **Validação duplicada** — cada função que recebe o dado revalida por segurança, espalhando a mesma lógica de validação por vários lugares.
- **Validação inconsistente** — confia-se (sem garantia real) que um único ponto central já validou, mas nada no tipo impede que um valor não validado chegue por outro caminho.

## Correção: tipo dedicado + validação por construção

Criar um tipo próprio para o conceito, validado no momento em que o dado entra no sistema, e convertido de volta ao formato necessário (string, int) só na saída.

```python
class Email:
    def __init__(self, value: str):
        if "@" not in value:
            raise ValueError("email inválido")
        self.value = value

# a partir daqui, qualquer função que recebe um Email
# não precisa mais validar — a validação já aconteceu na construção
def send_email(to: Email, body: str): ...
```

O exemplo mais forte citado na fonte é **dinheiro**: em vez de circular como `string` ou `int` cru pelo sistema inteiro, cria-se um tipo dedicado (classe/value object) para dinheiro, convertido na entrada e "castado" de volta na saída — o mesmo padrão de "parse, don't validate" aplicado a qualquer dado sensível a formato e regras de negócio.

## Relacionado

[[wiki/concepts/code-smells]] · [[wiki/concepts/naming]] · [[wiki/concepts/data-clumps]] (agrupar dados relacionados também reduz a superfície de validação repetida)

## Key Sources

- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]]
