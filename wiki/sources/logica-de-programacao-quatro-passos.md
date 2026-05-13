---
type: source
title: "Lógica de Programação: Como Qualquer Problema Vira Código"
aliases: ["quatro passos para resolver problemas", "problema vira código"]
date_created: 2026-05-13
date_updated: 2026-05-13
source_count: 1
tags: [logica-de-programacao, decomposicao, separacao-de-responsabilidades, estado, fluxo-logico]
skill: cs-fundamentals
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/logica-de-programacao-quatro-passos.md
source_url: ""
author: ""
date_published: ""
date_ingested: 2026-05-13
---

# Lógica de Programação: Como Qualquer Problema Vira Código

## TL;DR

Qualquer problema de programação pode ser resolvido em quatro passos: entender o problema (incluindo cenários de erro), decompô-lo em partes menores, criar o fluxo lógico antes de abrir o editor, e só então traduzir esse fluxo em código. O código é uma tradução — não uma criação.

## Claims principais

| Claim | Evidência | Confiança |
|---|---|---|
| O código deve ser uma tradução de decisões já tomadas, não uma criação | O exemplo do caixa eletrônico: cada linha do Python corresponde a uma decisão mapeada no fluxo | Alta |
| Ignorar cenários de erro no passo 1 leva a descobri-los no pior momento | "Quem pula esse passo acaba descobrindo essas decisões no meio do código" | Alta |
| Estado é o que o sistema precisa lembrar para tomar decisões | Contador de tentativas: o sistema decide bloquear baseado em quantas vezes o usuário errou | Alta |
| A lógica é independente da linguagem; só a sintaxe muda | O mesmo fluxo do caixa poderia ser escrito em Java, JS ou Python | Alta |

## Os Quatro Passos

1. **Entender o problema** — caminho feliz + o que pode dar errado + como o sistema reage a cada erro
2. **Quebrar em etapas menores** — [[separacao-de-responsabilidades]]: cada parte cuida de uma coisa só
3. **Criar o [[fluxo-logico]]** — escrever ou desenhar as decisões antes de abrir o editor
4. **Traduzir em código** — cada linha corresponde a uma decisão já tomada

## Exemplo central: autenticação do caixa eletrônico

Demonstra [[decomposicao-de-problemas]] (caixa dividido em 5 módulos independentes), [[estado]] (contador de tentativas), [[caminho-feliz]] vs [[edge-case]], e [[fluxo-de-controle]] (if + while).

```python
MAX_TENTATIVAS = 3

def autenticar(cartao, senha):
    if not cartao_existe(cartao):
        devolver_cartao()
        exibir_mensagem("Cartão não reconhecido.")
        return False

    tentativas = 0

    while tentativas < MAX_TENTATIVAS:
        senha_digitada = solicitar_senha()
        if senha_correta(cartao, senha_digitada):
            return True
        tentativas += 1

    bloquear_cartao(cartao)
    exibir_mensagem("Cartão bloqueado após 3 tentativas.")
    return False
```

## Entidades e conceitos tocados

- [[decomposicao-de-problemas]]
- [[separacao-de-responsabilidades]]
- [[fluxo-logico]]
- [[estado]]
- [[caminho-feliz]]
- [[edge-case]]
- [[fluxo-de-controle]]
- [[traducao-logica-para-codigo]]
- [[logica-de-programacao]]

## Questões abertas

- O próximo vídeo aborda estruturas de dados: onde fica o contador de tentativas? Como o sistema sabe o saldo?
- Não aborda como o fluxo lógico escala para sistemas com múltiplos módulos interagindo.

## Quotes relevantes

> "O código não vai ser uma criação — ele vai ser simplesmente uma tradução."

> "Quem pula esse passo acaba descobrindo essas decisões no pior momento possível — no meio do código ou quando ele já está pronto."

> "O estado é basicamente o que o sistema precisa lembrar quando está tomando algumas decisões."
