# Pilares do Desenvolvimento com IA: Harness, Contrato de Revisão e Waves

Transcrição de vídeo/aula em PT-BR de um instrutor que enumera os "pilares" para desenvolver com IA com mais clareza, mostra ao vivo um workflow básico (spec → IA implementa → revisão) num app Kanban feito "no go horse" com Claude Code, explica por que ele é improdutivo e apresenta a alternativa que o autor defende: **contrato de revisão auditável**, **gates de qualidade** e **waves** de desenvolvimento em paralelo. Autor e canal não informados (o nome "Wesley" aparece na fala, provavelmente como o nome do próprio apresentador dirigido pelo agente; possível vínculo com o MBA da Full Cycle, citado como "o MBA" — **não confirmado**). Já em português — sem tradução. Título derivado do conteúdo.

> **Transcrição truncada:** o texto colado termina no meio da frase ("…foi implementada da forma que eu gostaria h"). O fecho da aula não está disponível.
>
> **Nota de limpeza:** a transcrição automática corrompeu vários termos, corrigidos por contexto: "CAMBAN" → Kanban; "trelo" → Trello; "Stail Wind" → Tailwind; "Secolite" → SQLite; "Note" (na lista de stack) → provavelmente Node; "Sonet" → Sonnet; "cloud code" / "cloud.md" → Claude Code / CLAUDE.md; "agents.m MD" → AGENTS.md; "NIP" → provavelmente Knip (detector de código morto); "Typecript" → TypeScript; "postgre" → PostgreSQL; "ifes" → ifs; "autificável" → auditável (provável); "Ia"/"I" → IA; "mimar" → "para mim"; "implementuate" → comando/skill de implementação de feature (nome exato incerto). Vícios de fala (é, ã, né, tá, "cara", "galera") foram removidos e a pontuação reorganizada em parágrafos; o conteúdo não foi alterado.

## Os pilares: o que dominar para minimizar problemas com IA

É preciso entender quais pilares ajudam a desenvolver com mais clareza ao trabalhar com IA e quais elementos, se dominados, aumentam a chance de minimizar os problemas recorrentes.

- **Ferramentas (IDEs e CLIs).** São elas que conversam com os agentes — ou seja, passam a ser o nosso **harness**. Essas ferramentas têm agentes, e os agentes podem ser **especializados**: dá para definir e criar os próprios, o que torna o desenvolvimento mais intencional quanto ao tipo e ao domínio do problema.
- **Modelos.** Quando se domina e se entende melhor os modelos, usa-se o modelo certo no momento certo, com a velocidade correta, gastando menos.
- **Documentação e artefatos** que suportem o processo de desenvolvimento — para o próprio desenvolvedor entender o que o projeto fez, para o chefe entender ou para um funcionário novo entender como o sistema funciona.
- **Memória.** Uma das coisas mais importantes, porque impede o agente de cometer o mesmo erro repetidamente. Lidar com memória é complexo: existe o **memory rot** — a memória fica velha e deixa de refletir o estado do software.
- **Onde o sistema roda:** local, remoto, numa pipeline de CD no GitHub, ou usando o recurso de *remote control* para programar pelo celular.
- **Skills.** Uma das coisas mais importantes hoje no desenvolvimento; a diferença entre uma boa skill e uma "bem sem vergonha" é enorme, e há uma **falsa sensação** de saber criar uma skill decente — daí a frustração quando o resultado não vem.
- **Servidores MCP** adequados **na quantidade adequada**, porque inicializar muitos servidores MCP ocupa muito da janela de contexto.

Ao entender cada item com mais profundidade, o desenvolvedor passa a ser mais intencional em pontos que fazem diferença.

## O workflow básico e o problema dele

O workflow básico mostrado: **planejar/criar uma especificação → a IA desenvolve → revisar → pedir para simplificar** ("tirar aquele monte de ifs redundantes"). Ele funciona e é como muita gente já desenvolve hoje. O pedido é simples, então em tese o modelo acerta de primeira — mas provavelmente haverá problemas de qualidade de código, de segurança e de outros aspectos, que precisarão ser resolvidos ao longo do tempo.

### Demonstração ao vivo

O projeto: um **sistema de gerenciamento de tarefas Kanban** ("um Trello extremamente simplificado"): criar conta, entrar, sair, criar/editar/excluir tarefas, visualizá-las num quadro Kanban, mover entre status e reordenar dentro da mesma coluna. Colunas: a fazer, em andamento, concluído; a tarefa tem título, descrição e status. Stack: Next.js, Tailwind, SQLite e Prisma, com Node.

O autor **não fez nada** antes: apenas pediu ao Claude Code para instalar o Next.js e deu um `/clear`. Roda com **Sonnet**, esforço (*effort*) **high**, e pede simplesmente "implemente o projeto de acordo com o @spec" — sem planejamento, sem CLAUDE.md, sem AGENTS.md próprio. O único "harness" é o próprio Claude Code e o `AGENTS.md` gerado pelo Next.js, que manda o agente ler a documentação embutida (porque "esse não é o Next.js que você conhece") para não gerar código nas versões antigas do framework. Ele chama isso de "go horse".

### Os problemas observados

1. **Ansiedade de ficar parado olhando a IA programar.** Parece perda de tempo; a ansiedade aumenta ao sair para o café, e surge a dúvida: "parece que estou entregando mais código, mas estou sendo produtivo de verdade?".
2. **Paralelizar com git não resolve sozinho.** Dá para trabalhar em várias branches/worktrees simultâneas sem afetar a que está sendo desenvolvida, mas ainda assim persiste a sensação de perder tempo. O maior problema, com cautela: o desenvolvimento termina numa aplicação com bugs, e é preciso ter como objetivo claro **levar a IA o mais longe possível** dentro do próprio fluxo.
3. **Ausência de revisão de verdade.** Se a IA revisa o próprio código, diz "terminei, revisei, maravilhoso, pronto para produção" (já aconteceu várias vezes). Revisão por IA funciona **desde que haja um processo completo e decente**: o agente que programou **não** deve ser o que revisa ("o cara que programou fica com o orgulho ferido e vai falar que o que fez foi bem"). A dificuldade é como fazer o revisor revisar o que o implementador fez — e, segundo o autor, **revisar algo que não está claro para ser revisado não é uma revisão completa**; ele testou múltiplos workflows e ferramentas e muitos trouxeram esse mesmo problema.
4. **Ciclo manual de correção.** Ao achar um bug no teste, é preciso escrever "encontrei esse bug, corrija", esperar, testar de novo, repetir. Aqui o agente até tenta um teste ponta a ponta com browser.

Conclusão do trecho: o que se faz ali **não está errado**, mas é um **processo improdutivo, sem consistência ao longo do tempo** — exige conversar o tempo todo com a IA ("faz isso, melhora aquilo"). A IA faz as coisas tão rápido que o multitarefa mental não acompanha: sempre se fez uma tarefa por vez, agora dá para fazer dez, então é preciso **organizar um fluxo em que as dez tarefas andem sem conversar o tempo todo com a IA**.

## A alternativa: contrato, gates e waves

### O contrato de revisão

O autor defende (sem obrigar ninguém) **um contrato**: o implementador desenvolve garantindo cumprir o contrato; o revisor lê o contrato e garante que tudo o que está nele funciona — e o contrato deve conter **tudo o que o revisor precisa para revisar sem entender nada do contexto do projeto**. Sobre SDD (Spec Driven Development): as ferramentas existem aos montes, mas "você já viu o contrato de revisão que essas ferramentas têm umas com as outras?". O autor não usa spec kit ou ferramenta pronta: usa a versão que eles têm no MBA, com nuances que muitas delas não têm.

Características do contrato (exemplo mostrado):

- **Auditável/verificável:** qualquer agente pode receber a tarefa de rodar e revisar a partir dele.
- **Pré-requisitos de ambiente:** runtime (backend de tal forma, Next.js, PostgreSQL, diretório gravável), **browser real via Playwright CLI**.
- **Estado inicial necessário para o teste:** por exemplo, usuário Alice com e-mail X (admin, suspenso etc.), usuário em branco, usuário Bob para o teste de UI; e, no exemplo (uma plataforma de vídeo), um arquivo MP4 e um thumbnail com determinadas características, além das configurações do ambiente.
- **Gates de qualidade** — "aqui o harness entra forte": um script que valida, no fim, linter, dependências corretas, arquitetura e até a **camada da aplicação** (falha se alguém colocou regra de negócio no controller ou instanciou um repositório numa camada onde não deveria). Roda também **Knip** (código slop/morto), verificação de **dependência circular** e da organização de arquivos conforme a arquitetura definida — as **fitness functions**. Também TypeScript etc.
- **Rastreabilidade por critério de aceitação:** cada item do contrato deriva de um critério de aceitação do produto, e mostra-se que ele está **coberto** porque certos testes o exercitam.
- **Superfícies (*surfaces*):** superfície de API HTTP, de UI (verificação real de interface) e, em outros casos, outras superfícies baseadas em protocolos. Qualquer agente deve ser capaz de rodar e conferir **item por item** do contrato; quando isso acontece, sabe-se que a feature foi implementada como se queria.

### Waves

Separando a aplicação por features ou histórias — o critério é livre —, pode-se quebrar em **waves** ("ondas de desenvolvimento"). A partir do projeto gera-se a especificação de cada tarefa e identifica-se o que pode rodar **em paralelo**: por exemplo, gerar a spec das tarefas 4, 7 e 12, executá-las em paralelo, cada uma gerando seu **pull request**, e com **agentes que se autorrevisam**. Benefícios: (1) clareza do que se pode desenvolver em paralelo, (2) especificar de forma decente, (3) um **contrato claro** do que precisa acontecer.

Demonstração: com a Wave 3 já em andamento, dispara-se um comando de implementação para a **feature 04**; ele carrega a skill e implementa **baseado numa especificação/plano gerado com SDD** — com detalhes de como funcionam as tarefas, o banco de dados, as decisões técnicas e um **plano de ação separado em etapas** (não uma lista de tarefas: o autor sentia que reduzir a tarefas "estava acabando com" a clareza). O contrato é apontado como "o cara que muda o jogo".

## Resumo dos quatro problemas do workflow básico (segundo o autor)

1. Não há harness.
2. Tempo gasto parado olhando a IA programar.
3. Não há nenhum mecanismo de revisão.
4. Bugs encontrados no teste geram um ciclo manual de "corrija → teste de novo → corrija de novo".
