---
type: entity
title: "Uncle Bob (Robert C. Martin)"
aliases: ["uncle bob", "robert c. martin", "robert cecil martin"]
date_created: 2026-07-03
date_updated: 2026-08-11
source_count: 10
tags: [clean-code, clean-architecture, solid, autor, quality-gate]
skill: tech-mentor-backend
status: stub
---

# Uncle Bob (Robert C. Martin)

Autor e figura conhecida da indústria de software, associado aos princípios de Clean Code, Clean Architecture e SOLID. Citado numa thread do Twitter reagindo a uma afirmação de que SQL nunca deveria ter sido incorporado a programas de computador — SQL teria sido pensado originalmente como linguagem de console para relatórios, não para uso embutido em aplicações.

## Contexto da Menção

Numa thread analisada em [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]], Uncle Bob reage a uma afirmação (atribuída a outro "Bob" na thread) de que incorporar SQL em programas foi "um dos erros mais graves da nossa indústria". A discussão gerou confusão generalizada no Twitter, com muitos comentaristas comparando SQL a NoSQL — um eixo de discussão diferente do que estava sendo levantado (SQL embutido no código vs. abstraído por camadas como ORM/DSL).

**Nota de verificação**: a transcrição de origem não cita URL nem data da thread, e o autor da transcrição não confirma se o post referenciado ("Bob Tables: SQL is Demon Spawn...") é de fato de Robert C. Martin. Tratar a atribuição com cautela.

## Boy Scout Rule

Segunda menção, em [[wiki/sources/5-principios-que-mudaram-como-programador]]: Uncle Bob é creditado como quem popularizou a [[wiki/concepts/boy-scout-rule]] na comunidade de programação — a prática de deixar o código um pouco mais limpo a cada mudança feita numa base de código existente.

## Análise Estática no Pull Request como Não Negociável

Terceira menção, em [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]]: citado via Twitter argumentando que programadores são lentos para escrever código, mas isso não é motivo para abrir mão de qualidade — a recomendação concreta atribuída a ele é colocar análise estática e análise de qualidade de código diretamente no fluxo de pull request. O autor da fonte credita essa citação como o gatilho direto que o levou a montar seu próprio [[wiki/concepts/quality-gate|quality gate]] com padrão [[wiki/concepts/ratchet-baseline|ratchet]].

## Objetos vs. Estruturas de Dados (Post de Blog)

Quarta menção, em [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]]: um post do blog de Uncle Bob, escrito em formato de diálogo, define **objeto** e **estrutura de dados** como conceitos literalmente opostos — objeto é um conjunto de funções que operam sobre dados implícitos/encapsulados; estrutura de dados é um conjunto de dados operados por funções implícitas/externas. A partir dessa definição, Uncle Bob argumenta que não existe mapeamento direto entre objetos e relações de banco de dados (só transferência de dados), e sugere que "Object-Relational Mapper" é um nome equivocado. Essa distinção é a base teórica de [[wiki/concepts/objeto-vs-estrutura-de-dados]], que por sua vez fundamenta como [[wiki/concepts/clean-architecture]] alterna entre objetos (Entities, Use Cases, Presenter) e estruturas de dados (Input/Output Data, ViewModel) no fluxo de uma aplicação web — diagrama descrito no livro *Clean Architecture* do próprio Uncle Bob.

**Nota de verificação**: assim como na menção sobre SQL, a transcrição de origem não cita o título exato nem a URL do post do blog — vale confirmar contra `blog.cleancoder.com` se a atribuição precisar ser usada como fonte primária.

## Livro *Arquitetura Limpa na Prática* (Otávio Lemos)

Quinta menção, em [[wiki/sources/arquitetura-limpa-na-pratica]]: o livro inteiro de Otávio Lemos é um tutorial prático em torno da Clean Architecture de Robert Martin, com um estudo de caso completo em TypeScript. Traz uma anedota pessoal do autor: um bate-papo com Robert Martin no canal do YouTube do próprio Otávio, no qual Martin defende que validação sintática de dados (formato de email, por exemplo) pode ficar em camadas mais externas — posição da qual Otávio conscientemente se desvia no livro, preferindo validar já na camada de Entidades para tornar o modelo mais autocontido.

## Post no Twitter/X: "Não Leio Mais Nenhuma Linha de Código dos Meus Agentes"

Sexta menção, em [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]]: post recente (segundo a fonte, "semana passada") em que Uncle Bob afirma não ler mais nenhuma linha de código escrita pelos seus agentes de IA — aparente contradição com o argumento central de *Clean Code* de que se lê muito mais código do que se escreve, logo ele deve ser extremamente legível. O vídeo resolve a aparente contradição argumentando que o leitor mudou (é o próprio agente que lê cada linha, toda vez), mas as mesmas regras de legibilidade seguem se aplicando a esse novo leitor.

A parte central do post, segundo o autor da fonte, não é a frase de abertura e sim a segunda metade — a lista do que Uncle Bob faz **no lugar** de ler código: teste unitário, teste Gherkin, procedimento de QA, métrica de qualidade e mutation test ("vários outros"). Cada item citado pega um tipo de erro que os demais deixam passar — ver [[wiki/concepts/teste-de-mutacao]] e [[wiki/concepts/bdd]]. A fonte também traz uma nota de contexto pessoal citada pelo próprio Uncle Bob no Twitch: ele programa desde os anos 60, o que segundo o autor do vídeo explica a velocidade com que consegue confiar no próprio harness — resumida na frase "o direito de não ler código é conquistado, não copiado."

**Nota de verificação**: assim como nas menções anteriores, a fonte não cita URL nem data exata do post — tratar a atribuição e a citação textual com a mesma cautela já registrada acima.

## Segundo Post/Vídeo Sobre o Mesmo Tema: Quatro Técnicas de Gate de CI

Sétima menção, em [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]]: um vídeo de reação diferente, mas ao mesmo tipo de post de Uncle Bob sobre não revisar código de agentes e confiar em métricas (cobertura, dependency structure, complexidade ciclomática, tamanho de módulo, mutation tests) — não fica claro se é o mesmo tweet da sexta menção ou um post distinto na mesma janela de tempo. Essa fonte foca menos no debate teórico (função pequena vs. módulo profundo) e mais em detalhar quatro gates de CI concretos e bloqueáveis a partir da mesma lista: [[wiki/concepts/complexidade-ciclomatica|complexidade ciclomática]] com limite (CCN 1–20), cobertura + [[wiki/concepts/teste-de-mutacao|mutation testing]] com `mutmut`, limite de tamanho de arquivo (300 linhas), e análise de [[wiki/concepts/acoplamento|estrutura de dependências]] (import circular, camadas invertidas, módulo de API vs. implementação). O autor fecha admitindo que sua concordância com Uncle Bob é motivada por uma limitação prática: gera ~10.000 linhas de código por dia e não consegue revisar esse volume manualmente.

**Nota de verificação**: mesma cautela de atribuição das menções anteriores — sem URL nem data exata do post na fonte.

## Generalização de OCP + LSP em Dependency Inversion (1996)

Oitava menção, em [[wiki/sources/principios-solid-ilustrados]]: segundo a fonte, Robert C. Martin descreveu em 1996 que o uso rigoroso conjunto do [[wiki/concepts/open-closed-principle|Open/Closed]] e do [[wiki/concepts/liskov-substitution-principle|Liskov Substitution]] pode ser generalizado num princípio à parte, o [[wiki/concepts/dependency-inversion-principle|Dependency Inversion Principle]].

**Nota de verificação**: atribuição não cross-checada contra a fonte primária (o paper original "The Dependency Inversion Principle", C++ Report, 1996) — tratar como não confirmado até verificação.

## Terceiro Vídeo de Reação (Lucas Montano): Treta com "Fernando" e a Origem nos Anos 60

Nona menção, em [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]]: [[wiki/entities/lucas-montano]] reage a mais um post de Uncle Bob sobre não ler código de agentes — desta vez com o elemento novo de uma treta pública no X com um "Fernando" que o cutucou ("tu sabe o que é estar *on call* ou só sabe escrever livros?"). Uncle Bob respondeu que foi líder técnico e passou muitos anos de plantão, e reforçou que começou a programar no final dos anos 60 — dado que Montano usa para reforçar a mesma tese de [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] ("o direito de não ler código é conquistado"). Novos elementos desta fonte: (1) a citação *"Code quality still matters. It matters a lot. I verify it by using tools that measure."*; (2) a observação de que os projetos no GitHub de Uncle Bob parecem *play projects* (ex.: "Missile Command dual platform"), o que reduz o risco de não ler código porque nada crítico vai pra produção; (3) o argumento "ele nunca falou sobre código, falou sobre **regras** mensuráveis". Não fica claro se é o mesmo post das menções anteriores ou um distinto na mesma janela — provavelmente posterior.

**Nota de verificação**: mesma cautela de sempre — a fonte não cita URL nem data, e as citações textuais são reportadas de segunda mão.

## Key Sources

- [[wiki/sources/sql-nao-e-banco-de-dados-uncle-bob]]
- [[wiki/sources/principios-solid-ilustrados]] — atribuição da generalização de OCP+LSP em Dependency Inversion (1996), não confirmada contra fonte primária
- [[wiki/sources/5-principios-que-mudaram-como-programador]]
- [[wiki/sources/quality-gate-ratchet-multiplos-agentes-ia]] — citação sobre análise estática em PR como gatilho para o setup de quality gate do autor
- [[wiki/sources/objetos-vs-estruturas-de-dados-clean-architecture]] — post de blog sobre objeto vs. estrutura de dados, e diagrama de cenário web do livro *Clean Architecture*
- [[wiki/sources/arquitetura-limpa-na-pratica]] — livro-tutorial inteiro construído em torno da Clean Architecture de Martin, incluindo anedota de bate-papo pessoal sobre onde validar dados de entrada
- [[wiki/sources/uncle-bob-direito-de-nao-ler-codigo-agentes-ia]] — post recente sobre não ler mais código de agentes, e o harness (testes, Gherkin, QA, métricas, mutation testing) que sustenta essa afirmação
- [[wiki/sources/quatro-tecnicas-ci-cd-gate-qualidade-codigo-ia-uncle-bob]] — segundo vídeo sobre o mesmo tema, detalhando quatro gates de CI concretos (CCN, cobertura+mutation, tamanho de módulo, dependency structure)
- [[wiki/sources/ninguem-mais-revisa-codigo-ia-migracao-review-galego]] — terceiro vídeo de reação (Galego): concorda que as métricas são objetivas mas insuficientes, e propõe a matriz risco × dificuldade para migrar de "reviso tudo" para "não reviso"
- [[wiki/sources/code-review-morreu-uncle-bob-push-force-prod-lucas-montano]] — vídeo de Lucas Montano: treta com "Fernando" sobre estar on call, origem nos anos 60, citação "code quality still matters... tools that measure", projetos GitHub como play projects
