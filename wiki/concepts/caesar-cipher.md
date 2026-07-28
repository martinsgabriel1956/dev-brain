---
type: concept
title: "Caesar Cipher (Cifra de César)"
aliases: ["caesar cipher", "cifra de cesar", "shift cipher", "cifra de deslocamento"]
date_created: 2026-04-29
date_updated: 2026-07-28
source_count: 2
tags: [criptografia, historia, cifra, caesar-cipher, encryption]
skill: tech-mentor-security
status: stub
---

## Definição

Técnica de substituição monoalfabética usada por Júlio César para proteger comunicações militares. Cada letra da mensagem é deslocada por um número fixo de posições no alfabeto. A chave é o número do deslocamento.

```
Deslocamento = 3
H E L L O  →  K H O O R
K H O O R  →  H E L L O  (revertendo)
```

## Limitações

- Apenas 25 chaves possíveis (26 letras - 1) — força bruta em segundos.
- Vulnerável a análise de frequência — letras mais comuns em inglês (E, T, A) aparecem com a mesma frequência no ciphertext.
- **Não usar em qualquer contexto real de segurança.**

## Relevância histórica / didática

Ilustra o princípio central de toda encryption: **a mensagem só é legível para quem possui a chave**. É o ponto de partida conceitual antes de avançar para AES, RSA e algoritmos modernos.

## Não é IND-CPA Segura

A cifra de César falha no modelo formal [[wiki/concepts/ind-cpa-security]]: como cada letra é sempre substituída pela mesma letra, o padrão de repetição de caracteres da mensagem original é preservado na cifra. Um atacante que recebe a cifra de uma de duas mensagens candidatas de mesmo tamanho consegue identificar qual foi cifrada apenas observando onde os caracteres se repetem — sem precisar quebrar a chave. Isso demonstra formalmente por que "parecer embaralhado" não é sinônimo de seguro.

## Contexto Histórico Mais Amplo

Não foi a primeira criptografia da história — a [[wiki/concepts/scytale]] espartana é anterior e usa transposição em vez de substituição. A limitação de "uma letra sempre vira a mesma letra" foi resolvida séculos depois pela [[wiki/concepts/vigenere-cipher]], que introduziu substituição polialfabética.

## Relação com outros conceitos

- [[concepts/encryption]] — Caesar Cipher é o exemplo histórico mais simples do conceito.
- [[wiki/concepts/scytale]] — outra cifra pré-moderna, por transposição em vez de substituição
- [[wiki/concepts/vigenere-cipher]] — evolução que resolve a fraqueza de substituição fixa do César
- [[wiki/concepts/ind-cpa-security]] — modelo formal que demonstra por que César é insegura

## Key Sources

- [[sources/encoding-hashing-encryption]]
- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
