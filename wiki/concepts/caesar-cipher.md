---
type: concept
title: "Caesar Cipher (Cifra de César)"
aliases: ["caesar cipher", "cifra de cesar", "shift cipher", "cifra de deslocamento"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
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

## Relação com outros conceitos

- [[concepts/encryption]] — Caesar Cipher é o exemplo histórico mais simples do conceito.

## Key Sources

- [[sources/encoding-hashing-encryption]]
