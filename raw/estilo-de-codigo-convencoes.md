# Convenções de Estilo de Código — O que Ninguém Conta

> Transcrição de vídeo sobre convenções de código baseadas no Linux Kernel Coding Style.

---

## Tabs São 8 Caracteres (Não 2, Não 4)

Você usa tab de 2 ou 4 caracteres? Se a resposta é sim para qualquer um dos dois: você está errado.

**Tabs e indentações são 8 caracteres.** Sempre foram.

### "Mas 8 caracteres empurra o código para a direita da tela"

Para. O problema não é a indentação de 8 caracteres. O problema é que o código está **aninhado até o infinito**.

A indentação de 8 caracteres está te **avisando** que o aninhamento chegou longe demais. Não é o mensageiro que está errado — é a mensagem.

Se o código está saindo da tela com indentação de 8, é porque tem muitos níveis de aninhamento. A solução é refatorar, não reduzir a indentação.

---

## Comprimento de Linha

Todo mundo tem opinião sobre o limite de caracteres por linha, mas um ponto é consenso: **código não deve sair da lateral da tela** se puder ser evitado.

### Regra crítica: nunca quebre strings visíveis ao usuário ou mensagens de log

Imagine uma mensagem de log que resulta em uma linha longa de código. A tentação natural é quebrar ao meio:

```c
// ERRADO
printk("Erro ao processar requisição do usuário "
       "com id %d\n", user_id);
```

Problema: se o programa está rodando e você quer fazer `grep` por essa mensagem de log específica, **não vai encontrar** — porque a string está dividida em duas linhas.

A alternativa correta em C e a maioria das linguagens é usar **concatenação** mantendo a string intacta:

```c
// CERTO — permite grep da mensagem completa
printk("Erro ao processar requisição do usuário com id %d\n",
       user_id);
```

Quebre a linha em outro ponto, nunca dentro da string.

---

## Tamanho Máximo de Função

> *"O tamanho máximo de uma função é inversamente proporcional à sua complexidade e nível de indentação."*

Traduzindo: quanto maior a complexidade e o aninhamento de uma função, menor ela deve ser.

Complexidade e aninhamento são agrupados porque geralmente andam juntos — mais níveis de indentação quase sempre significam mais complexidade, e vice-versa.

### Exceção válida

Uma função longa mas **simples** — como um `switch/case` extenso com casos diretos e sem lógica complexa — pode ter mais linhas. O critério não é o número de linhas em si, é a combinação de comprimento + complexidade + aninhamento.

```
Função simples e longa       → OK
Função complexa e aninhada   → deve ser CURTA
```

---

## Comentários: Explique o QUÊ, Não o COMO

**Nunca use comentários para explicar como o código funciona.**

Se você tem um trecho de código inteligente mas difícil de ler, e a tentação é adicionar comentários explicando o mecanismo em detalhes — pare. Você está desperdiçando tempo.

O que você deveria fazer é **refatorar o código** para que o funcionamento seja óbvio pela leitura.

```c
// RUIM — comentário explicando o "como"
// Aqui deslocamos os bits à direita para dividir por 2,
// depois aplicamos a máscara para pegar apenas os 8 bits inferiores,
// o resultado é o índice do elemento no array
result = (value >> 1) & 0xFF;

// BOM — refatorado para ser legível
int half_value = value / 2;
int lower_byte = half_value & 0xFF;
int element_index = lower_byte;
```

**Reserve os comentários para explicar o QUÊ o código faz** — o propósito, o contexto, o porquê de uma decisão não óbvia. Não como ele funciona internamente.

---

## Resumo das Regras

| Assunto | Regra |
|---|---|
| Indentação | 8 caracteres — se empurra pra direita, o problema é o aninhamento |
| Comprimento de linha | Não sair da tela; quebrar em pontos que não partam strings |
| Strings de log | Nunca quebrar no meio — impossibilita grep |
| Tamanho de função | Inversamente proporcional à complexidade e aninhamento |
| Comentários | Explicam o QUÊ, nunca o COMO — se precisar explicar o COMO, refatore |
