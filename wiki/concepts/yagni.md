---
type: concept
title: "YAGNI — You Ain't Gonna Need It"
aliases: ["yagni", "you ain't gonna need it", "não vou precisar disso"]
date_created: 2026-04-23
date_updated: 2026-08-18
source_count: 9
tags: [arquitetura, principios, pragmatismo, over-engineering, xp]
skill: tech-mentor-backend
status: stable
---

# YAGNI — You Ain't Gonna Need It

Princípio do Extreme Programming (Kent Beck, 1999): não implemente algo até que você *precise* — não até que você *acha* que vai precisar.

## O Princípio

> "Tu não precisa de algo até precisar. E quando precisar, refatora — porque código simples é mais fácil de refatorar do que a abstração que tu tentou adivinhar ao futuro."

A maioria dos "e se um dia mudar X" nunca acontece. E quando acontece, a realidade é tão diferente do que foi imaginado que a abstração preventiva atrapalha em vez de ajudar.

## Por Que Fica Pior com IA

A IA escalou o problema do YAGNI. Antes, criar abstração preventiva levava dias de trabalho. Hoje: dois prompts e está lá. O custo de geração caiu. O custo de manutenção permanece igual — ou subiu, porque agora o codebase tem mais arquivos para agentes navegarem.

Ver [[concepts/abstraction-bloat]] — o agente gera 1000 linhas onde 100 bastariam por viés de treinamento.
Ver [[concepts/abstraction-illusion]] — a IA torna padrões acessíveis sem torná-los apropriados.

## Quando Aplicar

A abstração é justificada quando a dor é real:
- Você trocou essa dependência nos últimos 2 anos? Se não → não abstrai
- Tem um segundo caso de uso real agora? Se sim → extrai (após o segundo caso, nunca antes)
- O contrato de um serviço externo vai poluir seu domínio? → Anticorruption Layer

## Benefícios

- **Foco no que realmente importa** — o tempo economizado em features especulativas vai para o que é essencial à entrega atual.
- **Entregas mais rápidas** — menos código para escrever, revisar e testar antes de considerar a feature pronta.
- **Menos complexidade** — a base de código tem funcionalidades específicas para o que se propõe a resolver; quem lê o código consegue identificar exatamente o que existe implementado, sem precisar distinguir "o que é usado" de "o que foi implementado por precaução".

## Nota de atribuição bibliográfica

[[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] atribui o livro que apresenta o YAGNI a "Ronald Jeffries" — provável imprecisão. O livro fundador é *Extreme Programming Explained* (1999), de [[wiki/entities/kent-beck]]. Ron Jeffries é cocriador da Extreme Programming junto com Beck no [[wiki/entities/c3-project|projeto C3]] e autor de obras próprias sobre XP, mas não do livro citado nessa fonte.

## Relação com Outros Princípios

YAGNI não contradiz DDD ou Clean Architecture — ele questiona a *implementação ritualística*. Os princípios estratégicos (bounded context, separação de domínio e infra) continuam válidos. O que YAGNI questiona é: interface para cada repositório com uma única implementação, use case para cada operação CRUD, mappers em todas as direções.

Ver também [[wiki/concepts/fazer-a-coisa-mais-simples-que-poderia-funcionar]] — mesmo espírito de XP/Kent Beck aplicado a um eixo diferente: YAGNI questiona *o que construir agora*, o outro questiona *quão complexa deve ser a solução do problema atual*.

## Ignorar YAGNI como sinal de over-engineering, na prática

[[wiki/sources/underengineering-overengineering-mario-souto]] lista "ignorar YAGNI" entre os sinais de [[wiki/concepts/over-engineering]] discutidos a partir de um card/tweet, ao lado de microsserviços prematuros e otimização prematura — reforçando o vínculo já registrado nesta página entre violar YAGNI e over-engineering. A mesma fonte dá um exemplo do lado oposto do mesmo princípio: construir a própria lib de formulário do zero em vez de usar React Hook Form ou Formik não é exatamente "abstração especulativa" no sentido clássico de YAGNI, mas é a mesma disciplina aplicada a infraestrutura — "você não vai precisar construir isso, alguém já construiu e mantém."

## Ordem de Prioridade entre YAGNI, SOLID e DRY

[[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] (Chris Kiehl) propõe uma hierarquia explícita entre os três princípios — **YAGNI, SOLID, DRY, nessa ordem** — que nenhuma fonte anterior na wiki havia formulado: primeiro decidir *se* algo deve existir (YAGNI), depois *como* estruturá-lo bem caso exista (SOLID), e só então eliminar repetição (DRY). A ordem reforça o que já está documentado acima — YAGNI questiona o que construir antes de qualquer princípio de qualidade de código entrar em jogo.

## YAGNI Aplicado à Construção de Contrato de Serviço

[[wiki/sources/microsservicos-martin-fowler-james-lewis]] descreve um exemplo concreto de YAGNI aplicado a arquitetura de microsserviços: um time na Austrália orienta a construção de novos serviços por [[wiki/concepts/contract-testing|contratos orientados pelo consumidor]] definidos *antes* do código — o serviço é então construído apenas até o ponto em que satisfaz o contrato, "uma abordagem elegante para evitar o dilema do YAGNI ao construir novo software". É o mesmo princípio de "não implemente até precisar" aplicado no nível de fronteira de serviço, não só no nível de classe/função.

## Microsserviços Prematuros como Violação Direta de YAGNI

[[wiki/sources/microsservicos-monolito-first-renato-augusto]] nomeia explicitamente YAGNI como o princípio por trás da recomendação de não começar um projeto com [[wiki/concepts/microsservicos]]: no início, a prioridade deveria ser validar a ideia via MVP com velocidade máxima, e toda a infraestrutura extra de um projeto que nasce distribuído (mensageria, CI/CD por serviço, observabilidade distribuída, domínio obrigatório de CQRS/Event-Driven/Event Storming) é tempo tirado da construção das funcionalidades essenciais do domínio — antes mesmo de se saber se o produto tem valor para o usuário final. É a primeira fonte na wiki a nomear o princípio explicitamente nesse contexto, reforçando (sem contradizer) o que [[wiki/sources/underengineering-overengineering-mario-souto]] já registrava sobre microsserviços prematuros como sinal de over-engineering.

## Key Sources

- [[wiki/sources/microsservicos-monolito-first-renato-augusto]] — microsserviços prematuros nomeados explicitamente como violação de YAGNI; tempo de infraestrutura distribuída como custo de oportunidade contra validação de MVP
- [[sources/clean-architecture-ia-custo-real]]
- [[sources/super-productivity-ai-architecture-guide]]
- [[sources/addy-osmani-80-problem-agentic-coding]]
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/kiss-yagni-entrega-rapida-qualidade]] — exemplo de repositório com métodos CRUD implementados por precaução; benefícios de foco, velocidade e menor complexidade
- [[wiki/sources/underengineering-overengineering-mario-souto]] — "ignorar YAGNI" listado como sinal de over-engineering; exemplo de usar React Hook Form/Formik em vez de construir gerenciamento de formulário do zero
- [[wiki/sources/topicos-desenvolvimento-software-mudei-de-ideia-6-anos]] — ordem de prioridade explícita YAGNI → SOLID → DRY; escalar sem necessidade real como sinal de mau engenheiro
