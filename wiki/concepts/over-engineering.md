---
type: concept
title: "Over-Engineering"
aliases: ["over-engineering", "overengineering", "complexidade desnecessária", "engenharia excessiva"]
date_created: 2026-04-29
date_updated: 2026-04-29
source_count: 1
tags: [over-engineering, accidental-complexity, kiss, design-patterns, carreira, qualidade]
skill: tech-mentor-backend
status: stable
---

## Definição

Over-engineering é a introdução de complexidade técnica além do necessário para resolver o problema atual. Acontece quando decisões de engenharia são guiadas por padrões, abstrações ou arquiteturas que não têm justificativa nos requisitos reais do projeto.

É tão prejudicial quanto a gambiarra — mas mais difícil de detectar porque parece correto, bonito e defensável.

## Por que acontece

**Progressão inversa de expertise:** Iniciantes pensam simples por limitação de conhecimento. Seniores precisam ativamente suprimir o viés de complexidade acumulado. Pensar simples é fácil quando você sabe pouco; é difícil quando você sabe muito.

**Ego como vetor:** A abstração deixa de ser ferramenta e vira demonstração de conhecimento. O dev abstrai "para ficar bonito" ao invés de abstrair por requisito real.

**Síndrome do impostor invertida:** Dev júnior vê o código do sênior aprovado sem comentários e conclui que "simples não é suficiente". Começa a adicionar complexidade para parecer mais sênior.

**Pensamento hipotético sem ancoragem:** "E se esse código de caldo de cana um dia fosse usado para fritar pastel?" — antecipar requisitos fictícios em vez de requisitos reais.

## Consequências

- **Conhecimento restrito:** Só meia dúzia de pessoas entende a arquitetura. Os demais criam gambiarras para contornar o que não entendem.
- **Frankensteins:** Dois padrões arquiteturais no mesmo projeto com gambiarras conectando os dois.
- **Código duplicado:** Devs sem contexto reimplementam funcionalidade que já existe — simplesmente porque não conseguem navegar na arquitetura existente.
- **Performance degradada:** Camadas desnecessárias de abstração têm custo real (ver [[concepts/abstraction-bloat]]).
- **Onboarding lento:** Novos membros gastam tempo entendendo a arquitetura, não resolvendo problemas de negócio.

## Diagnóstico

> "Essa abstração resolve um problema real no contexto atual — ou estou antecipando um requisito fictício?"

Sinais de over-engineering:
- Mudar um comportamento exige alterar N arquivos em N camadas.
- A explicação da arquitetura leva mais tempo que a explicação do problema.
- Outros devs criam workarounds ao redor do código "bonito".
- A palavra "talvez um dia" aparece na justificativa de uma decisão.

## Relação com outros conceitos

- [[concepts/kiss]] — o princípio que over-engineering viola
- [[concepts/accidental-complexity]] — a complexidade resultante do over-engineering
- [[concepts/abstraction-bloat]] — forma específica com IA como vetor
- [[concepts/abstraction-illusion]] — padrão acessível ≠ padrão apropriado
- [[concepts/ego-driven-development]] — o mecanismo psicológico por trás

## Key Sources

- [[sources/overengineering-carol-ate-quinta]]
- [[sources/listen-notes-good-enough-engineering]]
