# Como Evoluir Software Sem Pagar o Preço de Microsserviços

> Transcrição de vídeo (português) sobre o caminho entre monolito e microsserviços — monolito modular, service de domínio e composição de módulos (module composition) como alternativas para escalar arquitetura sem pagar o custo operacional de microsserviços.

---

## Introdução

Existe um longo caminho na evolução da arquitetura que vai de monolito até microsserviços, mas entre esses dois extremos há muita coisa que acontece — e essas etapas intermediárias são fundamentais para uma arquitetura que evolui de forma sustentável.

Microsserviços mostraram algo importante para a arquitetura de software, sem necessariamente ter essa intenção. Muita gente acha que microsserviços foram a grande solução para escalar software. De certa forma eles ajudaram bastante quando surgiram, especialmente em grandes empresas com múltiplos times e domínios independentes. Mas, ao mesmo tempo, acabaram virando o padrão *default* para resolver qualquer tipo de complexidade de código — inclusive monolitos mal estruturados, algo que nem padrões de arquitetura em camadas como Hexagonal ou Clean Architecture conseguem resolver sozinhos, porque a organização de código monolítica tem um limite, não importa o padrão de arquitetura usado.

O livro *Arquitetura de Software: As Partes Difíceis* aponta que uma das maiores razões para as pessoas migrarem para microsserviços é organizar código. E é exatamente aí que está o problema.

## O problema: complexidade local vs. complexidade global

Microsserviços resolvem a **complexidade local**: o código de cada serviço fica pequeno, isolado, simples de mudar. A carga cognitiva necessária para mexer no código é baixa, porque tudo está junto — um arquivo do lado do outro, fazendo sentido.

Mas eles criam outro tipo de complexidade: a **complexidade global** — comunicação entre serviços, deploy orquestrado, garantia de consistência, monitoramento distribuído, debug com múltiplos logs. Essa conta chegou nos últimos anos, principalmente depois da crise: o custo de microsserviços ficou bem claro, e hoje várias empresas têm medo de adotar por causa dos efeitos colaterais.

## O aprendizado: modularização, não microsserviços

O que realmente melhora escalabilidade e manutenção de código não são os microsserviços em si, mas a **modularização**. Modularizar bem o código dentro de um monolito pode ser a chave para reduzir carga cognitiva, ter ciclos de desenvolvimento mais rápidos e manter a simplicidade operacional.

Quando isso é feito direito, você cria limites claros, responsabilidades separadas e dependências explícitas entre módulos. O monolito passa a se comportar como um sistema modular, pronto para escalar de forma individual ou conjunta, conforme a necessidade — dando muito mais flexibilidade.

## Três caminhos para escalar (além do monolito tradicional)

### 1. Serviços de domínio

Monolitos agrupados por domínio: em vez de um grande monolito, ele é quebrado em vários monolitos menores, cada um representando uma parte específica do domínio. Não é tão granular quanto microsserviço, o que traz um ótimo equilíbrio entre granularização e custo.

- É possível escalar partes maiores do domínio e dar a um time a propriedade de uma parte específica.
- Custo médio, escala média: ainda não dá para escalar coisas muito específicas — é preciso escalar o serviço inteiro, que pode ser grande.
- Microsserviços dão mais flexibilidade de escolher o que escalar, mas trazem custo maior: manutenção, ferramental, e a necessidade de mudar várias coisas a cada alteração. Isso gera custo alto tanto financeiro quanto de carga cognitiva.

### 2. Monolito modular clássico

Separação por módulos de domínio: módulos maiores, cada um referente a uma parte do domínio, com sua própria conexão de banco, suas próprias entidades, acessando apenas suas próprias tabelas — como se fossem serviços individuais, mas dentro do mesmo monolito.

Isso dá um design que já nasce pronto para ser quebrado, mas que ainda é um monolito. A visão central aqui: **monolito é uma escolha de deploy**, não necessariamente uma escolha de codebase.

**Exemplo prático (NestJS):**

- Um `main.ts` inicializa a aplicação inteira como monolito, carregando todos os módulos de domínio (ex.: content, identity, billing).
- Um segundo entrypoint, `video-processor-worker-main`, inicializa **apenas** o módulo de processamento de vídeo (`content-processor-module`), rodando como um processo separado — sem carregar o restante do monolito.
- No Docker/Docker Compose, são feitos dois builds separados: um para o monolito completo, outro para o worker. Ambos vêm da mesma aplicação/codebase, mas rodam como processos independentes.
- Não foi necessário criar um microsserviço isolado (repositório próprio, pipeline próprio) só para o worker — é tudo parte do mesmo codebase, modularizado de forma que um módulo consegue rodar totalmente separado sem precisar importar o outro.

**Limite dessa abordagem:** como os módulos fazem parte do mesmo codebase, uma mudança em um módulo (ex.: `identity`) pode forçar redeploy do worker também, mesmo que o worker não dependa diretamente dele. Isso não é problema por um bom tempo, mas quando a aplicação cresce muito, vira um gargalo — e é aí que entra o próximo nível: arquitetura modular com module composition.

### 3. Arquitetura modular com module composition (monorepo)

Estrutura muda para uma separação entre `apps/` e `packages/` (ou pacotes de domínio). Os pacotes de domínio (billing, content, identity, shared/infra) ficam isolados; `apps/` contém as formas de inicializar (bootstrap) a aplicação.

Usando um monorepo (o autor usa **NX**), é possível compor módulos de domínio de infinitas maneiras:

- Um app `billing-api` só carrega o `billing-api-module`, que por sua vez carrega o módulo de domínio `billing` (que não sabe nada sobre HTTP — só contém a lógica de domínio) e expõe uma API para ele.
- Outro app, o "monolito", carrega um `monolith-module` que agrega múltiplos módulos de domínio (ex.: `content` + `identity`).
- Um módulo de domínio não sabe como vai rodar — pode rodar junto com outros ou separado, dependendo apenas de qual "app"/bootstrap o carrega.

**Module composition** = poder compor módulos de domínio em infinitas combinações. A partir de um único codebase (monorepo), é possível ter, na prática, "infinitos microsserviços" sem pagar o preço de múltiplos repositórios, múltiplos pipelines e infraestrutura duplicada. O desenvolvimento acontece de forma unificada (bom para a capacidade cognitiva do time), e a necessidade de escala é tratada separadamente: quando um módulo precisa escalar individualmente, ele é colocado para rodar em um processo/app separado.

Isso descreve uma evolução: código monolítico tradicional → módulos → composição de módulos → escala individual por módulo quando necessário.

## Quando microsserviços de fato passam a fazer sentido

Quando a empresa cresce muito — múltiplos times em fusos horários diferentes, ou quando o monorepo fica lento demais para operar. Na prática, ferramental atual (ex.: NX) já resolve boa parte disso: é possível rodar pipelines apenas para o que foi alterado (ex.: mudança só no módulo de billing roda o pipeline só para ele, sem afetar o resto). Grandes empresas (Meta, Uber) também vêm seguindo essa linha de repositórios grandes e bem ferramentados. A escolha de onde o código "mora" importa menos do que a estruturação do código em si.

## Fechamento

A ideia central: ter menos tradeoffs para conseguir os mesmos benefícios de arquiteturas como microsserviços, adiando o máximo possível o momento de precisar pagar o preço de manter repositórios separados, infraestrutura separada, bibliotecas compartilhadas em repositórios à parte — custos de infraestrutura que não são custos de negócio.

O autor menciona ter um curso ("Construindo Aplicações Enterprise") cobrindo modularização, monolito modular, arquitetura modular e critérios para migrar para microsserviços, além de um livro gratuito futuro sobre "os 10 municípios da arquitetura modular" (nota: trecho de áudio impreciso, possivelmente "os 10 mandamentos da arquitetura modular").
