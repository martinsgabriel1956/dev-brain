# Lógica de Programação: Como Qualquer Problema Vira Código

**Fonte:** Transcrição de vídeo (YouTube)
**Idioma original:** Português
**Data:** 2026-05-13

---

## Introdução

Você provavelmente já foi a um caixa eletrônico sacar dinheiro, ou pelo menos sabe como esse processo funciona. Pensa comigo: o que acontece quando você coloca o seu cartão e digita a senha errada? Ele te bloqueia na primeira vez? Não — ele te dá mais uma chance, e mais uma, e só na terceira ele te bloqueia.

Alguém decidiu isso. Alguém pensou que depois de três tentativas você teria o bloqueio. Essa decisão existe em algum lugar, escrita em um código rodando em um servidor. E o raciocínio por trás dela é exatamente o mesmo que você vai usar para resolver qualquer problema na programação.

Isso é lógica — e você já entende mais do que imagina.

---

## Os Quatro Passos

Qualquer problema pode ser transformado em código seguindo quatro passos. Eles funcionam para qualquer problema, qualquer linguagem e qualquer nível de experiência.

### Passo 1 — Entender o problema

Faça três perguntas:

1. **O que precisa acontecer?** (caminho feliz)
2. **O que pode dar errado?**
3. **Como o sistema vai reagir a cada erro?**

> Quem pula esse passo acaba descobrindo essas decisões no pior momento possível — no meio do código ou quando ele já está pronto.

### Passo 2 — Quebrar em etapas menores

Nenhum problema complexo é resolvido de uma única vez. Cada etapa menor é um problema mais simples. Isso tem um nome técnico: **separação de responsabilidades** — cada parte do sistema cuida de uma coisa só.

### Passo 3 — Criar o fluxo lógico

Escreva ou desenhe (com diagramas) as decisões antes de abrir o editor. Em que ordem as coisas vão acontecer? Quais são as decisões? O que muda dependendo de cada resposta?

### Passo 4 — Transformar em instruções executáveis

Só agora você abre o editor. Com o fluxo mapeado, o código não é uma criação — é uma **tradução**. Cada linha corresponde a uma decisão que você já tomou.

---

## Aplicando os Quatro Passos: Caixa Eletrônico

### Passo 1 — Entender o problema

**Caminho feliz:**
1. Usuário insere o cartão
2. Digita a senha
3. Escolhe o valor a sacar
4. O dinheiro sai
5. Operação finalizada

**O que pode dar errado:**
- Senha incorreta
- Saldo insuficiente
- Caixa sem dinheiro disponível
- Cartão bloqueado

**Como o sistema reage:**
- Senha errada → permite tentar novamente (até 3x)
- Saldo insuficiente → mostra saldo disponível e pergunta se quer outro valor
- Cartão bloqueado → avisa e encerra a sessão

---

### Passo 2 — Quebrar em etapas menores

| Etapa | Responsabilidade |
|---|---|
| Autenticação | Verificar se cartão e senha são válidos |
| Verificação de saldo | Checar se há saldo suficiente para o pedido |
| Validação do saque | Checar limite diário e valor disponível no caixa |
| Execução do saque | Debitar da conta e liberar o dinheiro físico |
| Encerramento | Devolver cartão, imprimir comprovante, encerrar sessão |

A autenticação não precisa saber nada sobre o saldo. A validação do saque não precisa saber nada sobre a autenticação.

---

### Passo 3 — Criar o fluxo lógico (autenticação)

```
1. Usuário insere o cartão
2. Sistema verifica se o cartão existe na base de dados
   - NÃO existe → devolve o cartão, exibe "cartão não reconhecido", encerra
   - Existe → continua
3. Sistema pede a senha
4. Usuário digita a senha
5. Sistema verifica se a senha está correta
   - INCORRETA → incrementa contador de tentativas
     - tentativas >= 3 → bloqueia o cartão, encerra
     - tentativas < 3  → volta ao passo 3
   - CORRETA → autenticação concluída, segue para verificação de saldo
```

> **Estado:** o contador de tentativas é um exemplo de estado — o que o sistema precisa lembrar para tomar decisões. O sistema não bloqueia na primeira senha errada; ele decide baseado em quantas vezes o usuário já errou.

---

### Passo 4 — Transformar em código (Python)

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
            return True  # autenticação concluída

        tentativas += 1

    bloquear_cartao(cartao)
    exibir_mensagem("Cartão bloqueado após 3 tentativas.")
    return False
```

Cada linha corresponde a uma decisão mapeada no fluxo:
- O primeiro `if` → "o cartão existe?"
- O `while tentativas < MAX_TENTATIVAS` → permite até 3 tentativas
- O `bloquear_cartao` → o cenário de erro mapeado no passo 1

> O mesmo raciocínio e fluxo poderiam ser escritos em Java, JavaScript ou qualquer outra linguagem. O que muda é a sintaxe. A lógica permanece a mesma.

---

## Recapitulando

| Passo | O que fazer |
|---|---|
| 1. Entender o problema | Não só o caminho feliz — mapeie tudo que pode dar errado |
| 2. Quebrar em partes menores | Resolva a autenticação, depois o saldo, depois o saque |
| 3. Criar o fluxo de decisão | Escreva ou desenhe antes de abrir o editor |
| 4. Escrever o código | Traduza as decisões em instruções executáveis |

---

## Próximo tema

**Estruturas de dados:** como organizar as informações que o fluxo precisa. Onde fica o contador de tentativas? Como o sistema sabe o saldo do usuário? Essas decisões têm nome, têm trade-off e definem se o sistema vai ser lento ou rápido com escala.
