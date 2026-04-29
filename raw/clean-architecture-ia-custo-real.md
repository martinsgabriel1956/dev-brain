---
date: 2026-04-23
tags: [arquitetura, clean-architecture, ia, agentes, yagni, ddd, contexto, tokens, custo]
skill: tech-mentor-backend
level: sênior
tipo: transcrição-video
---

# Clean Architecture na Era da IA — O Custo Real das Abstrações

## O Caso Real

Um time de 10 devs, SaaS B2B com clientes pagantes e domínio complexo: billing, contratos, relatórios fiscais. Seguiram Clean Architecture à risca — várias camadas, interfaces para cada repositório, use case para cada operação, ports, adapters, DTOs, mappers. Tudo o que Uncle Bob mandou.

Seis meses depois, adotaram IA com Claude Code no fluxo. A produtividade deveria ter dobrado. Não dobrou. Em alguns módulos, caiu.

**Uma feature simples como adicionar um novo campo tocava 18 arquivos.** A IA:
- Consumia contexto demais
- Às vezes inventava relações que não existiam
- Às vezes sugeria design patterns ainda mais complexos ("se já usa Clean Architecture, vai usar Decorator também")
- Repetia lógica em dois lugares porque não achou a primeira ocorrência

O custo por feature ficou alto: alto em tokens, alto em revisão, e bugs chegaram em produção.

---

## A Pergunta Central

> Quanto da arquitetura que a gente defendeu por décadas era sobre código — e quanto era sobre os nossos próprios limites cognitivos?

---

## A Indústria Já Vinha Simplificando

Muito antes da IA existir, as linguagens modernas apontavam outra direção.

**Go** não tem:
- Classes
- Herança
- Anotações

Tem: struct, interface implícita, função.

Todo o ecossistema sério em Go (Kubernetes, Docker, a infraestrutura do Cloudflare) implementa os princípios fundamentais de Clean Architecture:
- Lógica de negócio isolada
- Injeção de dependência
- Testabilidade

...sem cerimônia. Direto ao ponto.

**Conclusão:** o princípio sempre foi separável da prática ritualística.

---

## Por Que Mais Arquivos = Mais Custo com IA

Cada arquivo a mais é token a mais no contexto do agente. Você paga pela sua decisão arquitetural.

Cada indireção a mais é um pulo a mais para o agente entender o fluxo. Cada abstração sem propósito real é ruído competindo com a lógica que importa.

**Isso não é opinião. É mensurável.** Roda o mesmo prompt em dois projetos — um com arquitetura ritualística, outro com arquitetura enxuta e design bom — e vê o custo por feature mudar.

---

## O Navigation Paradox (paper 2026)

Um paper de fevereiro de 2026 mediu exatamente o custo das abstrações para agentes.

**Resultado principal:** Dependency Injection e Inversion criam conexões entre arquivos que não existem no código-fonte — existem no container runtime. O agente lê o código, não acha a ligação, e simplesmente não descobre que um arquivo é relevante.

**Dados:**
- Em tarefas com dependências escondidas (G3), o Claude Code acerta apenas **76.2% dos arquivos necessários** sem auxílio
- Mesmo com uma ferramenta de navegação de grafos disponível, o agente a **ignora 58% das vezes**
- Múltiplas pastas no estilo `domain/application/infrastructure/presentation` fazem o agente abrir 7–13 arquivos para uma feature que em Vertical Slice seria um único arquivo

→ Links: `navigation-paradox-2026.md` (arxiv.org/html/2602.20048v1)

---

## Por Que a IA Sugere Arquitetura Complexa

Se custa tanto e não é bom para IA — por que a própria IA continua sugerindo arquitetura complexa?

**Addy Osmani (Google)** documentou o fenômeno: **abstraction bloat**.

O agente sem supervisão escreve 1000 linhas onde 100 bastariam. Cria hierarquias de classes onde uma função resolveria. O motivo não é bug — é treinamento.

Os LLMs são treinados com todo o conhecimento da internet, e os dados de treinamento são superrepresentados por blogs sobre padrões complexos. Ninguém escreve um artigo dizendo "fiz um CRUD com três arquivos e está funcionando há 5 anos". As pessoas escrevem sobre Event Sourcing hexagonal com Saga pattern num to-do list.

Quando você pergunta "como estruturar esse serviço?", a IA responde com a média ponderada da internet de tech — e essa média é enviesada para o complexo.

→ Link: `addy-osmani-80-problem-agentic-coding.md`

---

## A Abstraction Illusion (Super Productivity)

> "A IA torna padrões sofisticados acessíveis sem torná-los apropriados."

Antes, implementar Event Sourcing exigia ler um livro, estudar exemplos, construir incrementalmente. Esse processo filtrava naturalmente os times que não precisavam daquilo.

Hoje: dois prompts e está lá. Para um sistema que nunca vai precisar. Mas você vai seguir pagando pelo overhead.

→ Link: `super-productivity-ai-architecture-guide.md`

---

## Go is not Java

Go prova que você pode ter os princípios de Clean Architecture sem o ritual de camadas físicas. Interfaces implícitas, sem frameworks de DI, sem anotações — e ainda assim sistemas testáveis, modulares e fáceis de navegar.

→ Link: `go-is-not-java.md`

---

## O Que Continua Vivo: DDD Estratégico

Não o DDD tático — o estratégico.

**Bounded Context**, **linguagem ubíqua**, **separação por domínio de negócio**: ficou mais importante, não menos.

Por quê? Quando você aponta o agente para um contexto delimitado:
- O escopo de arquivos fica pequeno
- A linguagem fica consistente
- A IA gera código que respeita as regras daquele domínio
- Menos tokens consumidos
- Menos chance de inventar relações que não existem

**Contexto delimitado virou otimização de token — não só clareza de modelo.**

---

## Encapsulamento vs. Inversão de Dependência

Confusão comum que gera over-engineering:

**Encapsulamento:** esconder o detalhe. `userRepository.find()` — o chamador não sabe que o Prisma existe. Se trocar o ORM, só esse arquivo muda. Sem interface, sem cerimônia. Isso é o que importa.

**Inversão de Dependência (o D do SOLID):** alto nível não depende de baixo nível diretamente — os dois dependem de uma abstração (interface). Vantagem: camada de domínio não importa nada da infra. Custo: indireção, boilerplate, carga cognitiva.

A maioria dos projetos precisa de encapsulamento. Poucos precisam de inversão de dependência formal.

---

## A Regra Prática: Estratégico → Flat → Abstrai Por Dor

**Passo 1 — Monolítico com módulos de domínio:**
Separa por módulos grandes: `billing/`, `orders/`, `identity/`. Cada um tem seu próprio modelo. Nenhum importa diretamente do outro. Isso é DDD estratégico no nível mais barato possível — só uma pasta.

**Passo 2 — Dentro de cada módulo, começa flat:**
Três arquivos: entrada/saída, lógica de negócio, persistência. Sem interfaces, sem ports, sem adapters, sem mappers entre camadas.

**Passo 3 — Abstrai quando a dor justificar:**
- Você trocou essa dependência nos últimos 2 anos? Não → não abstrai
- Tem outro lugar que precisa da mesma coisa? Sim → extrai para shared, só depois do segundo caso
- Tem medo do contrato de um serviço externo poluir seu domínio? Sim → coloca atrás de uma interface (Anticorruption Layer)

---

## Onde Eu Posso Estar Errado

> "Se a IA gera código 10x mais rápido, a ausência de estrutura vira caos 10x mais rápido."

O argumento vale. A resposta não é Clean Architecture ritualística, mas limites explícitos vêm de lugares mais baratos:
- Contextos delimitados bem definidos (pastas por domínio)
- Tipos fortes nos contratos entre módulos
- Testes que exercitam comportamento, não implementação
- Regras de lint que impedem imports entre domínios

---

## A Pergunta Para o Seu Projeto

> Tu defende a arquitetura atual por fundamento ou por hábito? Tu consegue justificar cada camada com o problema real que ela resolve?

Não é sobre jogar Clean Architecture fora. É sobre questionar peça por peça e aplicar só o que é necessário.

**Yagni — You Ain't Gonna Need It.** Kent Beck, 1999. A gente sabia isso. A IA não criou esse problema — ela o escalou, porque agora você consegue gerar abstração preventiva em minutos, não em dias.

---

## Conceitos Relacionados

- [[navigation-paradox-2026]] — custo mensurável das abstrações para agentes
- [[addy-osmani-80-problem-agentic-coding]] — abstraction bloat e comprehension debt
- [[super-productivity-ai-architecture-guide]] — abstraction illusion
- [[go-is-not-java]] — princípios sem cerimônia
- [[concepts/monolito-modular]] — módulos com contratos explícitos
- [[concepts/feature-flags]] — desacopla deploy de release
- [[sources/clean-architecture]] — camadas, dependency rule, use cases
- [[sources/ddd-strategic]] — Bounded Context, linguagem ubíqua

---

*Fonte: transcrição de vídeo PT-BR · 2026-04-23*
