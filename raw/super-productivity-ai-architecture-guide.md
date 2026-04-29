---
date: 2026-04-23
tags: [ia, arquitetura, abstraction-illusion, constraints, decisao, yagni, reversibilidade]
skill: tech-mentor-backend
level: sênior
source_url: https://super-productivity.com/blog/ai-software-architecture-guide/
author: Super Productivity Blog
date_published: 2026
---

# AI and Software Architecture: A Dangerous Convenience

## TL;DR

A IA torna padrões sofisticados *acessíveis* sem torná-los *apropriados*. A barreira mudou de "você consegue construir?" para "você deveria construir?" — e a IA não ajuda com a segunda pergunta.

## A Abstraction Illusion

> Você perguntou ao seu assistente de IA como estruturar um novo serviço. Ele sugeriu event sourcing com CQRS, arquitetura hexagonal com ports e adapters, e um saga pattern para transações distribuídas. A explicação foi clara, os exemplos de código eram limpos, os diagramas faziam sentido.
>
> Seis meses depois, seu time de três pessoas está mantendo uma infraestrutura de event sourcing para uma aplicação que recebe 200 requests por dia. Cada feature leva três vezes mais tempo por causa do overhead de abstração. A arquitetura é tecnicamente excelente e praticamente ruinosa.

**Este é o abstraction illusion:** antes da IA, implementar event sourcing exigia ler livros, estudar exemplos, construir incrementalmente. Esse processo filtrava naturalmente os times que não precisavam daquilo. Hoje, qualquer dev gera uma implementação CQRS completa em uma tarde.

## Arquitetura é Escolha de Constraints, Não de Padrões

Cada decisão arquitetural troca um conjunto de capacidades por outro:

- **Microsserviços** trocam independência de deploy por complexidade operacional
- **Event Sourcing** troca simplicidade de query por completude de auditoria
- **Monolito** troca flexibilidade de escala por velocidade de desenvolvimento

Boas decisões arquiteturais vêm de entender suas *constraints específicas*: tamanho do time, padrões de tráfego, requisitos de consistência, capacidade operacional, timeline.

**A IA conhece os padrões — mas não conhece suas constraints.** Quando você pergunta "como devo arquitetar isso?", a IA responde a pergunta que *pode* responder (quais padrões existem) em vez da pergunta que você *precisa* (quais constraints devem guiar sua escolha).

## Onde a IA Ajuda

### O Que Funciona Bem

- **Exploração de padrões:** "Quais são as formas comuns de lidar com X?" — excelente ponto de partida, não a decisão final
- **Exemplos de implementação:** uma vez que você decidiu a abordagem, a IA gera exemplos excelentes
- **Articulação de tradeoffs:** a IA articula claramente os tradeoffs textuais de diferentes abordagens

### O Que Não Funciona

- **Decisões de restrição:** a IA não sabe se você tem 3 ou 300 devs, se o sistema precisa de 99.99% SLA, se você tem equipe de operações
- **Julgamento de adequação:** "deveria usar isso?" é uma pergunta que a IA não consegue responder sem o seu contexto

## O Workflow Prático

1. **Colete constraints primeiro.** Escreva: tamanho do time, expectativas de tráfego, requisitos de consistência, capacidade operacional, timeline. Faça isso *antes* de perguntar qualquer coisa para a IA.
2. **Explore opções com a IA.** Peça um survey de abordagens com tradeoffs. Trate como pesquisa, não como recomendação.
3. **Proponha sua abordagem.** Baseado em constraints + opções, forme sua própria opinião.
4. **Teste com a IA no papel de devil's advocate.** "Quais são os problemas com essa abordagem dado que somos um time de 4?"
5. **Escolha a opção mais reversível quando empatado.** Reserve decisões irreversíveis para quando você tem alta confiança.
6. **Documente a decisão.** Registre as constraints, opções consideradas e rationale. Isso é a documentação que a IA *não consegue gerar* — porque requer seu contexto específico.

## As 10 Perguntas de Adequação

Antes de adotar qualquer padrão arquitetural sugerido pela IA:

1. Qual problema específico esse padrão resolve no meu contexto?
2. Quais são as alternativas mais simples?
3. Meu time tem experiência para manter isso?
4. Qual é o custo operacional adicional?
5. Como isso afeta o tempo de onboarding de novos membros?
6. É reversível se as assumptions estiverem erradas?
7. Qual evidência tenho de que vou precisar dessa escala?
8. Quais são os failure modes específicos?
9. Como isso interage com sistemas existentes?
10. Qual é o plano de escape se não funcionar?

Se você não consegue responder a maioria, simplifique.

## Reversibilidade Como Critério

> "Prefira decisões reversíveis. Reserve decisões irreversíveis para situações onde você tem alta confiança."

Código simples é mais fácil de refatorar do que uma abstração que tentou adivinhar o futuro. Com IA, refatorar código simples é muito rápido. A abstração preventiva tem custo agora e cria rigidez — e o "e se um dia mudar" geralmente nunca acontece da forma imaginada.

## Conceitos Relacionados

- [[sources/addy-osmani-80-problem-agentic-coding]] — abstraction bloat, mesmo diagnóstico
- [[sources/clean-architecture-ia-custo-real]] — caso real com time SaaS B2B
- [[sources/navigation-paradox-2026]] — custo quantificado de abstrações para agentes
- [[concepts/yagni]] — You Ain't Gonna Need It, o princípio que fundamenta tudo isso

---

*Fonte: super-productivity.com/blog/ai-software-architecture-guide · 2026*
