---
type: concept
title: "Local-First"
aliases: ["local first", "client como fonte de verdade", "carrinho sem storage"]
date_created: 2026-07-10
date_updated: 2026-07-10
source_count: 1
tags: [local-first, system-design, hmac, arquitetura, escalabilidade]
skill: tech-mentor-system-design
status: draft
---

# Local-First

**Padrão arquitetural em que o dado calculado no servidor é enviado ao cliente e tratado como fidedigno localmente, sem ser persistido no servidor.** O servidor confia que o dado que o cliente devolve depois é o mesmo que ele originalmente gerou — validado por um mecanismo de integridade (tipicamente [[wiki/concepts/hmac]]) em vez de uma consulta a um registro salvo.

## O problema que resolve

Exemplo canônico: um `cart service` computa o valor final de um carrinho (descontos, preço unitário, total) e gera um payload para o cliente. Persistir esse carrinho calculado no servidor tem custo real em alto volume:

- **Banco relacional**: precisa de índice em memória sobre milhões de registros para lookup rápido.
- **Banco não-relacional** (ex.: DynamoDB): também paga custo de leitura/escrita por lookup.
- **Descarte**: carrinhos abandonados precisam ser expirados/limpos — outro custo operacional.

Se o estado vive só no cliente, o servidor nunca paga esse custo de storage nem de descarte.

## Como garantir integridade sem armazenar

O desafio central: como o servidor garante, quando o cliente devolve o dado (ex.: no fechamento do carrinho), que é exatamente o que foi originalmente calculado — sem ter uma cópia salva para comparar?

Abordagens e por que a maioria falha:

| Abordagem | Resultado |
|---|---|
| Criptografar o payload inteiro | Garante integridade, mas o cliente não consegue exibir o dado em claro (ex.: mostrar o preço ao usuário) |
| Assinatura assimétrica (RSA) | Resolve, mas computacionalmente cara demais em alto volume |
| `Hash(secret + payload)` simples | Vulnerável a ataque de extensão de mensagem |
| **HMAC** | Resolve: integridade garantida, payload continua legível, custo computacional baixo |

O fluxo: servidor gera payload + HMAC (assinatura simétrica derivada de um segredo só seu), manda os dois para o cliente sem salvar nada. Cliente exibe o payload normalmente. Ao devolver, servidor recalcula o HMAC sobre o payload recebido e compara com o header — se baterem, o dado não foi alterado. Ver [[wiki/concepts/hmac]] para a mecânica completa do algoritmo.

## Limitação em aberto: expiração e replay

O esquema básico não tem timestamp nem nonce — um payload antigo (ex.: carrinho calculado antes de uma mudança de preço) continuaria validando como íntegro mesmo defasado. Isso é diferente do padrão já estabelecido para [[wiki/concepts/webhook-signature-validation]], que inclui checagem de idade da requisição (`x-timestamp`) contra replay. Um esquema local-first em produção provavelmente precisaria da mesma camada adicional.

## Relação com outros conceitos

- [[wiki/concepts/hmac]] — mecanismo de integridade que viabiliza o padrão local-first sem custo de assinatura assimétrica
- [[wiki/concepts/webhook-signature-validation]] — mesmo mecanismo (HMAC em header), aplicado a um cenário diferente (validar payload de terceiros, não payload próprio devolvido pelo cliente)
- [[wiki/concepts/idempotencia]] — tema adjacente de tratar dado vindo do cliente com desconfiança controlada, mas focado em evitar duplicação de efeito, não em integridade do conteúdo

## Key sources

- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]
