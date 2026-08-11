# Como Extrair um Código Melhor dos Agentes de IA: Planejamento, Plan Mode e Skills

> Transcrição de vídeo (português, sem tradução necessária). O autor demonstra, usando a IDE com IA integrada **Verdent AI**, três mudanças pequenas na forma de usar agentes que elevam muito a qualidade do código gerado: (1) prompts específicos em vez de genéricos, (2) o **modo plan** (planejar antes de codar) e (3) **skills** para eliminar alucinação de pacotes e forçar padrões internos. O exemplo prático é refatorar múltiplos gateways de pagamento (Stripe e Abacate Pay) com o **Strategy Pattern**. Trechos finais de divulgação/patrocínio da ferramenta foram condensados.

---

## O cenário do erro comum

Imagine que você está mexendo num código legado e pensa: "vou pedir para a IA refatorar". Você abre o chat, copia e cola o código, ela te cospe umas 200 linhas que *aparentemente* estão certas. Você cola, roda, e metade dos testes unitários quebra — porque ela não entendeu as dependências. Aí você começa a discutir com ela como se estivesse falando com um humano ("xinga até a bisavó do ChatGPT"), diz que está errado mas **não passa um plano** para ela seguir. Resultado: o código fica ruim, e depois de uma hora nesse processo você desiste pensando "essas IAs não conseguem fazer nada mesmo".

**Esse é o erro número um entre os devs usando IA hoje: deixar que ela escreva o código sem planejar primeiro.**

O vídeo mostra pequenas mudanças no prompt e na estratégia de uso dos agentes que ajudam a extrair um resultado melhor.

---

## A ferramenta: Verdent AI

O autor testa a **Verdent AI**, uma ferramenta de desenvolvimento com IA nativa — basicamente uma IDE com IA integrada. Ela permite rodar múltiplos agentes em paralelo, configurar skills etc. (tudo aquilo que já é comum nesse tipo de ferramenta).

O projeto de exemplo: uma aplicação **Next.js** onde todo o back end está na parte de API. O código está em arquivos separados, mas sem organização clara, sem estrutura específica e sem nenhum design pattern — "meio que uma bagunça". O objetivo: suportar **múltiplos gateways de pagamento** (Stripe e Abacate Pay), tanto para oferecer mais opções ao cliente quanto para ter tolerância a falhas (se um provedor cair, troca para o outro).

---

## Parte 1 — O jeito errado: prompt genérico

A forma menos eficiente de pedir seria abrir o chat e mandar:

> Refactor the payment providers architecture to be more organized

Depois de rodar, a IA fez coisas até legais: analisou o projeto, pegou contexto e aplicou alterações. O que ela entregou:

- Excluiu os arquivos que estavam em `src/lib/` e criou uma nova pasta `payment/`, movendo os arquivos para lá.
- Refatorou as rotas: extraiu métodos que estavam declarados dentro das rotas e jogou para os arquivos específicos de cada provider.
- Ajustou os imports.

**O problema:** "organizar código é subjetivo". O prompt foi amplo e genérico demais — quando eu digo "payment providers", quero dizer a integração no front end ou só o back end? Só os arquivos que chamam Stripe/Abacate diretamente, ou as rotas também? Quando o prompt fica amplo, a decisão fica aberta para a IA, e é a IA que acaba decidindo — abrindo espaço para ela errar ou fazer diferente do que você queria.

O resultado não ficou *errado*, mas ficou raso: ela só moveu arquivos de uma pasta para outra e tirou algumas funções da rota. Um dev mais experiente olha aquilo e pensa "isso não é refatorar, isso não está organizado". Mas o problema **não está na IA — está na forma como ela foi usada.**

---

## Parte 2 — O jeito certo: prompt específico + contexto

O autor descarta as alterações e inicia um **chat do zero** (contexto zerado). Reaproveitar o mesmo chat faria a IA usar as conversas anteriores como contexto e poluiria a nova tarefa.

A primeira mudança é **especificar** o que quer. Ele já sabe (usando conhecimento próprio, sem delegar a decisão à IA) que quer usar o **Strategy Pattern**: quando há múltiplos providers de algo, uma Strategy decide qual serviço usar por baixo dos panos. Ele mostra o padrão na documentação do **Refactoring Guru / Design Guru** (exemplo clássico do algoritmo de navegação/rota) e usa o link como referência.

O novo prompt (essência):

> Refactor the payment provider functions to use strategy pattern for different providers (Stripe and Abacate Pay for now). Ensure it follows our existing error handler and logger. Ensure it keeps working with the current front end interface. Use the documentation as a guide to implement the pattern.

E ele **menciona arquivos específicos** no contexto: o arquivo do Abacate Pay, o do Stripe, a rota onde são usados, a parte do checkout — tudo que valha a pena estar no contexto melhora o resultado.

### Trocar para o modo Plan

Em vez de enviar direto, ele troca para o **modo plan**. O que o modo plan faz:

1. A IA mapeia todas as dependências e o contexto da aplicação onde vai mexer.
2. Analisa o contexto que foi passado.
3. Monta um **plano de implementação** — uma espécie de especificação técnica: onde vai mexer, como pretende implementar, quais os benefícios.
4. Gera esse plano **antes de programar**, para que o usuário revise, comente e peça alterações.

Outro ganho do modo plan: se algo ficar **ambíguo** (o código permite duas formas de fazer, o pedido tem interpretações diferentes — botão em cima ou embaixo, aceitar CPF ou CNPJ), a IA **pergunta antes** de decidir. No modo "piloto automático" anterior, ela simplesmente assumia a resposta mais provável e tomava a decisão sozinha.

### Revisando o plano

O plano gerado foi detalhado: objetivo (aplicar Strategy para construir a payment provider logic), os dois flows em comum (webhook handling e checkout creation), garantia de que as rotas do front end mantêm as mesmas URLs e formatos de request/response. Ele veio inclusive com um **diagrama em Mermaid.js** mostrando a interface `PaymentStrategy` (métodos `verifyWebhook`, `processWebhookEvents`, `createCheckout`) e as duas implementações (Stripe e Abacate). O plano listava os arquivos novos (`types.ts`, a interface, cada strategy, o payment context) e quais arquivos seriam tocados.

> É muito importante ler o plano e ver o que ela pretende fazer — isso previne que ela faça besteira.

O autor então **comenta em cima do plano** para ajustá-lo. Ele tinha dito antes para não mudar o formato de request/response, mas resolve liberar isso:

> You can change the request and response formats if it fits better in the new class organization, because the old ones were too coupled into the Stripe and Abacate SDKs.

A IA reanalisa o comentário e **atualiza o plano** (e o diagrama): cria tipos compartilhados como `CheckoutParams`, `CheckoutResult` e `NormalizedPaymentEvent`, com todos os providers usando **tipos agnósticos** (sem importação direta de Stripe/Abacate), deixando o código mais desacoplado. Só olhando o plano já dá para ver que o nível da refatoração será muito superior ao anterior.

### Executar (build)

Depois de revisar e comentar, ele clica em **build** — só então a IA começa a escrever o código. Dá para acompanhar as tarefas (os "todos") sendo riscadas conforme completadas (ex.: 8 tarefas no total). O resultado final:

- Arquivos de tipos criados.
- `StripePaymentStrategy` implementando a interface `IPaymentStrategy` (o que já se fazia nas funções soltas, porém muito mais organizado).
- Rotas muito mais limpas: cada rota carrega o **payment context** com a strategy correspondente e chama métodos comuns (`createCheckout` etc.).

Antes, cada router estava 100% acoplado ao seu provider; agora os dois usam o mesmo payment context — basta carregar a strategy do provider certo, e ambos respeitam os mesmos tipos. **A qualidade do código ficou infinitamente superior**, com poucas mudanças no modo de pedir.

---

## Parte 3 — Skills: contra alucinação e repetição

Outro erro comum, especialmente em projetos grandes de empresas:

- **Alucinação de pacotes:** a IA importa módulos que não existem (não estão declarados em lugar nenhum, nenhum artifactory), ou importa métodos/tipos que não existem no pacote real.
- **Não reutiliza o sistema de componentes da empresa:** usa Tailwind num arquivo, Chakra em outro, ou alucina um componente inexistente.
- **Repetição:** você precisa ficar repetindo "usa essa lib aqui", "usa o design system da empresa", "segue essa arquitetura de classes" a cada prompt.

### Por que isso acontece

As LLMs foram treinadas com **dados públicos** (Stack Overflow, GitHub, repositórios públicos), onde a galera usa frameworks/bibliotecas populares e open source. Quando a IA mexe num código **corporativo** que usa um framework interno da empresa ou um padrão próprio (declaração de classes, injeção de dependências adaptada), ela se perde — não tem contexto sobre aquilo. No fim, a LLM é uma máquina probabilística: ela tenta adivinhar a geração de código mais provável para o que você pediu e o contexto que tem.

### A solução: skills

Skills podem ser vistas como **prompts salvos e reutilizáveis**, mas tecnicamente são mais profundas: uma **camada extra de injeção de contexto/instruções** na pipeline do modelo. O diferencial: você **não precisa dizer explicitamente** para a IA usar a skill. Pelo formato como a skill é criada, ela tem uma **descrição** de quando deve ser usada; quando o momento chega, a IA **aciona a skill automaticamente**, injetando aquele contexto. Isso **sobrescreve o comportamento genérico** da LLM (o que ela aprendeu com códigos públicos).

É ótimo colocar em skills:
- Especificações de bibliotecas internas/proprietárias da empresa.
- Heurísticas de design (UX/UI) que precisam ser seguidas à risca.
- Padrões de código/design do repositório.
- Definições de esquema de JSON de APIs internas/terceiras sem documentação pública (só com exemplos a IA já consegue adivinhar o resto).

### Criando uma skill (com a skill Skill Creator)

Na Verdent, o autor usa uma skill que já vem na ferramenta e **ajuda a criar skills** (o "Homem-Aranha apontando pro Homem-Aranha" — uma skill que cria skills). O prompt:

> Help me create a skill that is called always when I ask the agent to refactor something. Then the agent should look into the Refactoring Guru design patterns to see if any design pattern matches the current need or resolves the current problem, and then refactor following the design pattern structure.

O que aconteceu:
- A primeira coisa que a IA fez foi **ler o Skill Creator**, que nada mais é do que um arquivo `SKILL.md`. **Toda skill é um arquivo markdown** que dá contexto para uma tarefa, evitando repetição.
- O `SKILL.md` do Skill Creator diz o que são skills, o que aquela skill entrega, e — crucial — tem um **título e uma descrição** que a IA usa para decidir **quando acionar** a skill. Quando acionada, todo o contexto dela é injetado; quando não é útil, não é injetado (economia de janela de contexto).
- O Skill Creator inclui até comandos/scripts que a IA deve rodar para criar a skill e o que não incluir.
- A IA rodou os comandos e criou uma nova skill: **Refactoring with Design Patterns**. No fim, a skill vira um arquivo `.skill` (que contém o `SKILL.md` + uma pasta `references/`, tudo zipado para salvar na IDE).

Depois de instalar (`install skill`), a skill aparece nas configurações com a descrição:

> This skill should be used whenever the user asks to refactor, restructure, reorganize, redesign, or improve the code quality

…mais **trigger keywords**. Toda vez que um prompt chega, a IA analisa todas as skills instaladas, busca por essas palavras-chave e pelo match com a tarefa; se alguma skill atende, injeta o contexto — senão, não injeta.

Dentro da skill criada há uma referência `references/design-patterns.md` — um arquivo markdown com vários design patterns e **quando usar cada um** (creational, structural, behavioral patterns), extraído do Refactoring Guru.

> Só essa pequena coisa já vai elevar muito o nível das minhas refatorações.

### Reutilizar skills da comunidade

Não é preciso criar skills manualmente sempre. O valor de criar é adaptá-las ao cenário da sua empresa (biblioteca de componentes, API específica, design system próprio). Mas dá para **importar skills da comunidade** open source (nas settings → skills → add skill). O autor importa uma skill de **front-end refactoring** que "o Léo" criou baseado num livro sobre Tailwind.

---

## Sobre economia de contexto

> Não é só porque você passou mais informação que a IA vai trazer um resultado melhor.

O contexto também precisa ser **otimizado** para a tarefa: contexto demais (ou irrelevante) pode confundir o modelo. Por isso o lazy loading das skills (só a descrição no system prompt; o corpo carregado sob demanda) é valioso — economiza janela de contexto e aumenta a eficiência.

---

## Resumo da ópera

Para ter produtividade real com agentes de IA:

1. **Não jogue prompts aleatórios** nem pegue a primeira coisa que a IA gera.
2. **Seja específico** e traga o contexto certo (arquivos, referências, o design pattern que você já sabe que quer).
3. **Planeje antes de codar** (modo plan): leia, revise e comente o plano antes de autorizar a execução.
4. **Use skills** para injetar padrões internos e eliminar alucinação e repetição.

Assim a IA escreve o código correto de primeira e evita retrabalho.

---

## Notas de divulgação (condensadas)

O autor apresenta a **Verdent AI** como a IDE usada ao longo do vídeo (em beta de lançamento), com opção de conta gratuita para testes. Blocos de call-to-action (link na descrição, like/inscrição) omitidos por não serem conteúdo técnico.
