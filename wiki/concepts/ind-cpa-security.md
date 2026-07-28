---
type: concept
title: "IND-CPA (Indistinguibilidade sob Ataque de Texto Escolhido)"
aliases: ["ind-cpa", "indistinguishability under chosen plaintext attack", "chosen plaintext attack"]
date_created: 2026-07-28
date_updated: 2026-07-28
source_count: 1
tags: [criptografia, seguranca-formal, ind-cpa, criptoanalise]
skill: tech-mentor-security
status: stub
---

## Definição

Modelo formal para medir se um esquema de criptografia é seguro. O atacante pode escolher e submeter quantas mensagens quiser para serem criptografadas (**chosen plaintext attack**) e observar as cifras resultantes. O esquema é **IND-CPA seguro** se, ao receber a cifra de uma de duas mensagens candidatas de mesmo tamanho escolhidas pelo próprio atacante, ele não consegue identificar qual das duas gerou aquela cifra com probabilidade melhor que a de um chute aleatório.

## Por Que a Cifra de César Falha

A [[wiki/concepts/caesar-cipher]] **não é IND-CPA segura**: como cada letra é sempre substituída pela mesma letra, o padrão de repetição de caracteres da mensagem original é preservado na cifra. Se em uma mensagem candidata a letra "E" se repete nas mesmas posições em que uma letra se repete na cifra recebida, o atacante identifica qual mensagem originou aquela cifra — a correspondência posicional de repetição entrega a resposta, sem precisar quebrar a chave.

## Por Que Importa

IND-CPA é o padrão mínimo esperado de qualquer cifra moderna (AES-GCM, RSA-OAEP) — um esquema que vaza até um bit de informação sobre qual mensagem foi cifrada, além do comprimento, é considerado inseguro por esse critério, independentemente de "parecer" complexo.

## Relação com outros conceitos

- [[wiki/concepts/caesar-cipher]] — exemplo concreto de esquema que falha no teste
- [[wiki/concepts/aes]] — esquemas modernos são projetados para passar em IND-CPA (e modelos mais fortes, como IND-CCA)
- [[wiki/concepts/criptografia]] — contexto geral

## Key Sources

- [[wiki/sources/criptografia-cesar-vigenere-rsa-aes-hashing-quantica]]
