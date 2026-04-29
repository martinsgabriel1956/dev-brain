---
type: concept
title: "Encoding"
aliases: ["encoding", "codificação", "url encoding", "base64", "hex encoding"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [encoding, base64, url-encoding, representacao-de-dados, fundamentos]
skill: tech-mentor-security
status: stable
---

## Definição

Encoding é a transformação de dados de uma forma para outra com o propósito de armazenamento ou transmissão. Não envolve segredo — qualquer pessoa com conhecimento do esquema de encoding pode reverter a transformação.

**Encoding não é segurança. É representação.**

## Por que existe

Diferentes sistemas aceitam diferentes conjuntos de caracteres. URLs, por exemplo, só aceitam um subconjunto limitado de caracteres ASCII. Espaços não são válidos — então são convertidos para `%20` (URL encoding / percent-encoding). A informação precisa chegar; o encoding garante que ela seja transportável.

## Formas comuns

| Encoding | Uso típico |
|---|---|
| **URL encoding (percent-encoding)** | Queries em URLs (`%20` = espaço, `%3F` = `?`) |
| **Base64** | Imagens inline em HTML/CSS, tokens JWT, dados binários em JSON |
| **Hexadecimal** | Cores CSS (`#FF5733`), representação de bytes, hashes |
| **Binário** | Comunicação de baixo nível, protocolos de rede |
| **UTF-8** | Texto universal — cobre todos os caracteres Unicode |

## Propriedades

- **Reversível** por qualquer pessoa que conheça o esquema.
- **Sem chave** — não há segredo envolvido.
- **Determinístico** — mesma entrada, mesma saída.
- **Sem perda** — encoding preserva todos os dados originais.

## Antipadrão comum

Base64 não é criptografia. É apenas uma forma de representar dados binários como texto ASCII. Qualquer pessoa pode decodificar base64 sem nenhuma chave. Usar base64 para "esconder" dados sensíveis é um erro de segurança.

## Relação com outros conceitos

- [[concepts/hashing]] — irreversível, sem chave. Encoding é reversível e sem chave.
- [[concepts/encryption]] — reversível, mas requer chave. Encoding é reversível sem chave.

## Key Sources

- [[sources/encoding-hashing-encryption]]
