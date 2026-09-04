---
type: concept
title: "Local-First"
aliases: ["local first", "client como fonte de verdade", "carrinho sem storage", "posse do dado"]
date_created: 2026-07-10
date_updated: 2026-09-04
source_count: 2
tags: [local-first, offline-first, system-design, hmac, crdt, lww, arquitetura, escalabilidade]
skill: tech-mentor-system-design
status: draft
---

# Local-First

> **Nota de terminologia:** este termo tem dois usos incompatíveis registrados na wiki. Este documento apresenta primeiro o uso **canônico** (Ink & Switch / Kleppmann), depois marca explicitamente o uso divergente. Ver [[wiki/questions/local-first-definicoes-conflitantes]] para a análise completa.

## Definição canônica: réplica primária, posse do usuário

**Padrão arquitetural em que o dispositivo local é uma réplica primária e autoritativa do dado — não um cache.** A pergunta que separa local-first de [[wiki/concepts/offline-first]] não é "funciona sem rede?" (as duas funcionam offline), e sim **qual cópia do dado é a autoridade**:

| | Offline-first | Local-first |
|---|---|---|
| Autoridade | Servidor | Cada réplica local |
| Papel do local | Cache subordinado ao servidor | Réplica primária |
| Papel do servidor | Fonte da verdade | Cópia secundária ("relay") — pode cair sem impedir convergência |
| Escrita é definitiva quando | Servidor aceita a requisição | Aplicada localmente |
| Se a empresa fecha o serviço | Você tinha um cache de algo que não existe mais | O arquivo era seu — continua funcionando |

Exemplo: notebook e celular logados no mesmo app, ambos como réplicas primárias, convergindo entre si por sincronização — o servidor (relay) é só um dos caminhos de convergência, não o dono do dado.

### Conflito de edição concorrente offline

Se dois dispositivos offline editam o mesmo dado simultaneamente e depois sincronizam, é preciso resolver o conflito:

- **[[wiki/concepts/last-write-wins]] (LWW)** — mais simples de implementar; principal tradeoff é perda silenciosa de dados (a escrita mais recente sobrescreve sem aviso alterações anteriores).
- **[[wiki/concepts/crdt]]** — converge deterministicamente sem servidor central, mais complexo de implementar.

### Quando local-first é a decisão errada

Domínios que dependem de uma autoridade central por natureza do próprio negócio: aplicação bancária, e-commerce, rede social, app de corrida — regras de negócio que exigem que o servidor tenha razão em caso de divergência. Nesses casos, o que se quer é resiliência (offline-first), não posse (local-first).

### A pergunta que decide entre as duas

Se as duas cópias divergirem, quem tem razão? Se a resposta precisa ser "o servidor", quer-se offline-first. Se a resposta é "as réplicas convergem entre si", quer-se local-first — e está se decidindo dar **posse** do dado ao usuário. Cache pode ser adicionado depois sem redesenho; posse é uma decisão de arquitetura mais robusta, que precisa ser planejada desde o início.

## Uso divergente registrado na wiki: dado efêmero validado por HMAC

Uma fonte anterior ([[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]]) usa "local-first" para um padrão diferente e não relacionado à definição acima: **o dado calculado no servidor é enviado ao cliente e tratado como fidedigno localmente, sem ser persistido no servidor.** Aqui o cliente não tem posse/autoridade — ele só guarda e devolve o dado, validado por integridade (tipicamente [[wiki/concepts/hmac]]) em vez de comparação com um registro salvo. Isso é o oposto conceitual da definição canônica: o servidor continua sendo a autoridade lógica, o cliente nunca pode alterar o valor sem invalidar a assinatura. Mantido aqui como registro histórico da wiki — ver [[wiki/questions/local-first-definicoes-conflitantes]] para por que essas duas coisas não deveriam ter o mesmo nome.

### O problema que resolve (uso divergente)

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

- [[wiki/concepts/offline-first]] — a arquitetura oposta: servidor como autoridade, local como cache subordinado
- [[wiki/concepts/last-write-wins]] — estratégia mais simples de resolução de conflito entre réplicas locais
- [[wiki/concepts/crdt]] — estratégia de resolução de conflito por convergência matemática, sem servidor central
- [[wiki/concepts/cap-theorem]] — paralelo estrutural: escolher quem tem razão sob divergência é análogo a escolher consistência (C) vs. disponibilidade (A) sob partição
- [[wiki/concepts/hmac]] — mecanismo de integridade usado no uso divergente registrado abaixo, sem relação com a definição canônica
- [[wiki/concepts/webhook-signature-validation]] — mesmo mecanismo (HMAC em header), aplicado a um cenário diferente (validar payload de terceiros, não payload próprio devolvido pelo cliente)
- [[wiki/concepts/idempotencia]] — tema adjacente de tratar dado vindo do cliente com desconfiança controlada, mas focado em evitar duplicação de efeito, não em integridade do conteúdo

## Key sources

- [[wiki/sources/local-first-vs-offline-first]] — definição canônica (réplica primária, posse, LWW/CRDT)
- [[wiki/sources/hmac-integridade-mensagem-local-first-entrevista]] — uso divergente (dado efêmero validado por HMAC)
