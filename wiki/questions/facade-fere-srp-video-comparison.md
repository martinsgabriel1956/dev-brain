---
type: question
title: "O Facade fere o SRP? Duas fontes discordam"
aliases: ["facade quebra srp", "facade srp contradiction"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 2
tags: [design-patterns, facade, solid, srp, contradiction]
skill: tech-mentor-backend
status: draft
---

# O Facade fere o SRP? Duas fontes discordam

Duas fontes de vídeo em português, ambas construindo um `*Facade` de e-commerce/cliente do zero para ensinar o padrão [[wiki/concepts/facade-pattern]], chegam a conclusões opostas sobre se ele fere o Single Responsibility Principle.

## Posição A — Facade não fere SRP

[[wiki/sources/design-pattern-facade-renato-augusto]] (Renato Augusto): SRP é sobre ter **um único motivo para mudar**, não sobre "uma linha de código, uma ação". Uma Facade que orquestra pagamento, notificação e estoque continua respeitando SRP se o único motivo dela mudar for *o processo que ela representa* mudar — ela opera num nível de abstração diferente das classes de serviço que chama, cada uma delas com SRP estrito individualmente.

## Posição B — Facade fere SRP, "e quebra bonito"

[[wiki/sources/design-pattern-facade-codigo-fonte-tv]] (Código Fonte TV): o método `removeConta()` do `ClientFacade` "faz muito mais coisa do que deveria estar fazendo". O autor reconhece explicitamente a posição contrária ("tem gente que defende que não necessariamente isso quebra [SRP]... porque ele não sabe exatamente qual é a implementação de cada serviço"), mas discorda — na opinião dele, orquestrar múltiplas operações de subsistemas diferentes dentro de um único método é, sim, responsabilidade demais.

## Onde a discordância realmente está

Não é uma contradição factual (nenhuma fonte cita GoF ou Robert C. Martin como autoridade primária para sua posição — ambas são interpretações pessoais dos autores, registradas como tal nas respectivas fontes). É uma discordância sobre **o critério de aplicação do SRP**:

- Posição A trata "motivo de mudança" como a única métrica válida — e conclui que orquestração pura (sem lógica de negócio própria) não conta como responsabilidade adicional.
- Posição B trata a **quantidade de subsistemas coordenados num único método** como sinal suficiente de responsabilidade excessiva, independente de haver um único motivo de mudança.

Isso é consistente com o próprio texto de [[wiki/concepts/single-responsibility-principle]], que já registra a tensão "razão para mudar" vs. "faz só uma coisa" — mas antes desta ingestão a wiki só tinha a Posição A documentada com essa profundidade.

## Estado

Sem resolução — ambos são autores de conteúdo educacional sem citação de fonte primária do GoF para a questão específica de Facade vs. SRP. Tratar como debate legítimo e não resolvido dentro da comunidade de padrões de projeto, não como erro de uma das fontes.

## Key Sources

- [[wiki/sources/design-pattern-facade-renato-augusto]]
- [[wiki/sources/design-pattern-facade-codigo-fonte-tv]]
