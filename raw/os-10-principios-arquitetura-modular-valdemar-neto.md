# Os 10 Princípios da Arquitetura Modular — Valdemar Neto

Não é novidade que microsserviços estão em queda e que monolitos modulares estão extremamente em alta. Mas tem uma coisa curiosa que eu sempre vejo: sempre que alguém fala de monolito modular, aparece aquela mesma imagem de um monte de blocos conectados ao banco de dados dentro de um único código. Só que isso não é verdade. A verdade é que monolitos modulares podem escalar tanto quanto microsserviços se forem bem estruturados, e nesse vídeo vou te mostrar os 10 princípios para escalar arquiteturas modulares e como estruturar um monolito modular que escala praticamente de forma infinita.

Eu sou Valdemar Neto, cofundador da Tech Leads Club, já trabalhei em empresas como Atlassian e Totvs, e há mais de 6 anos venho pesquisando e aplicando arquiteturas modulares e sistemas de grande porte. Muito desse conteúdo faz parte do livro que eu venho trabalhando, que é "Os 10 Princípios da Arquitetura Modular".

## O que é um módulo e o que é um monolito

Para começar, a gente tem que entender o que é um módulo. Pensem no módulo como uma forma de agrupar e escolher o que você quer expor. Pode ser uma classe, um namespace, algo que agrupe outras classes, ou uma forma lógica de agrupamento onde você escolhe o que vai ser exposto para fora. Outra forma de pensar: uma parte do sistema que pode ser feita deploy ou compilada sozinha.

E o que é o monolito? De forma bem simples: faz deploy junto, roda no mesmo processo. Código é desenvolvido, faz deploy, roda junto no mesmo processo — vamos tratar isso como monolito aqui.

## Por que monolitos modulares voltaram com força

Se isso não é novidade — temos monolitos desde sempre — por que monolitos modulares voltaram com tanta força agora? Dois motivos principais:

1. **Virtualização.** Hoje conseguimos rodar qualquer parte do código isolada em contêineres.
2. **Aprendizado com microsserviços nas últimas décadas.** Aprendemos que separar o código traz benefícios — design e coesão melhores, código mais modular, mais fácil de manter — mas a separação física tem custos altíssimos: operação mais cara, carga cognitiva maior, gestão muito mais complexa.

Ou seja, a modularização sempre foi boa. O que mudou é que agora conseguimos colher os benefícios sem o custo dos microsserviços. Isso não é novidade — empresas grandes como Shopify, GitHub, Basecamp (DHH, criador do Ruby on Rails) são famosas por rodar em monolitos. Só que antes isso ficava restrito a empresas maiores porque não tinha tanto ferramental; hoje em dia qualquer um pode construir uma arquitetura modular que escala bastante.

## Exemplo prático: sistema de streaming

Para exemplificar, uso uma aplicação minha desenvolvida para meu curso na Tech Leads Club: um sistema de streaming similar à Netflix. O monolito modular tem contextos delimitados — billing, streaming, identity e infraestrutura compartilhada — que são partes separadas do domínio, cada uma um módulo dentro do monolito modular.

No código (uma aplicação NestJS/Node.js, mas o padrão é similar em qualquer linguagem — Java com Modulith, por exemplo), os módulos ficam separados: billing, identity, content etc. No arquivo `main.ts` são carregados todos os módulos — isso é o que torna a aplicação monolítica: não dá para escalar uma parte de forma independente.

Só que existe um `video-processor-worker` main separado, outro arquivo de bootstrap que carrega só o `content-processor-module` — um submódulo de `content` que trata apenas do processamento de vídeo. É possível fazer build de uma imagem Docker só para ele, rodando de forma independente. Ou seja, o monolito modular puramente dessa forma já escala, mas tem um limite: como colocar 100, 200 pessoas trabalhando nesse codebase sem que um impacte o outro? Como fazer só o billing escalar?

## A diferença entre monolito modular e arquitetura modular

Aqui entram os limites do monolito modular — e por que ninguém fala sobre a arquitetura modular, que é onde realmente está a grande escala. A grande diferença: numa arquitetura modular você pode ter vários monolitos, várias maneiras de agrupar módulos. Antes, o monolito tinha todos os módulos dentro; agora há infinitos números de possibilidades de combinação de apps — coisa que não é possível fazer com microsserviços, porque eles estão em codebases diferentes.

Imagine que a "app" é uma maneira de agrupar módulos: uma app usa `identity` + `streaming` + `shared infra` (logging); outra app usa `billing` separadamente. Na prática (exemplo com NX): agora existem `apps/` e `packages/`. Apps são somente a maneira de agrupar módulos. Uma app "monolito" carrega só `content` + `identity`. Se dois times trabalham nisso — um mantém o monolito, outro mantém a parte de billing — cada um trabalha de forma independente, mas os módulos ficam isolados em `packages/` e podem ser compostos em infinitos tipos de app: se você quiser rodar `content` junto com `billing`, é só importar `content` dentro do módulo de `billing`.

## Os 10 princípios

### 1. Limites bem definidos
Cada módulo deve ter um limite claro: isolar o que pertence a ele e não expor coisas internas. No NestJS, um módulo importa outros módulos, tem providers usados internamente, e não expõe nada além do necessário — encapsula tudo que pertence a ele. Ele pertence a um domínio (Domain-Driven Design, design estratégico) — módulos de domínio, não módulos de feature. No início do sistema modular, na dúvida, façam módulos bem grandes; deixem aparecer os agrupamentos e a coesão internamente antes de quebrar em módulos menores.

### 2. Componibilidade
Habilidade de módulos poderem ser compostos em apps (ex.: billing, identity, streaming compostos numa app). Para um módulo poder ser composto, ele não pode depender diretamente de outros módulos — deve ser isolado e facilmente composto com outros. No monolito modular do exemplo, os módulos são compostos, mas não têm dependência direta entre si — o que os torna fáceis de compor.

### 3. Independência
Módulos devem ser totalmente independentes em infraestrutura, testes, tudo que precisarem — devem rodar completamente isolados. Se você quiser mover o módulo para outro repositório, deve ser só pegar e mover. Isso exige um design que contenha tudo: testes end-to-end na raiz do módulo, testes de unidade dentro do service, migrations e conexão com banco dentro da camada de persistência do próprio módulo.

### 4. Isolamento de estado
Cada módulo tem sua própria conexão com o banco, roda suas próprias migrations, só vê as próprias tabelas — idealmente, em sistemas maiores, o próprio banco de dados. Se houver conexão com Redis ou filas, tudo é gerenciado de forma isolada a nível de módulo.

### 5. Comunicação explícita
Um módulo não deve chamar diretamente o service de outro módulo. Deve chamar através de uma API (ex.: REST para localhost) ou expor uma façade que o outro módulo chama através de uma interface. No exemplo: antes do login, `identity` precisa checar se o usuário tem uma subscription ativa em `billing`. Em vez de chamada direta, existe uma interface onde se injeta o que se quer usar — no caso, um HTTP client (chamada HTTP para o outro módulo), ou alternativamente uma classe façade injetada (um método que chama internamente um serviço do módulo de billing). São as duas formas mais comuns de manter baixo acoplamento entre módulos.

### 6. Substituibilidade
Um módulo pode ser substituído (ou removido) dentro de uma app sem afetar o resto da app, bastando uma mudança de configuração — o módulo precisa ser configurado para isso.

### 7. Deploy independente
O módulo em si não faz deploy — ele pertence a uma app, e é a app que pode ser feita deploy de forma independente. Os módulos dentro dela são configurados para deploy independente: não sabem do ambiente nem da app, só têm a própria configuração pronta para rodar isoladamente.

### 8. Escala independente
Um módulo deve escalar totalmente independente — não depender de outros módulos nem do ambiente em que está. Isso inclui o banco de dados e os serviços dos quais depende: toda a configuração fica nele, nada fica externo.

### 9. Monitoramento e observabilidade
Cada módulo deve ter seu próprio setup de monitoramento e observabilidade. Importante porque, quando há vários módulos numa mesma app com times diferentes donos de cada um, é essencial que os times certos recebam os alertas certos e vejam as métricas dos próprios módulos durante um incidente.

### 10. Falhas isoladas
Cada módulo deve isolar suas falhas: circuit breakers, boas práticas de shutdown, para não impactar outros módulos dentro da mesma app.

## Limites de cada abordagem

**Microsserviços:** não compõem — não dá para colocar vários microsserviços dentro de uma mesma app, porque estão em codebases diferentes. Essa é uma limitação central de microsserviços frente à componibilidade de arquiteturas modulares.

**Monolitos modulares (aplicando os 10 princípios num único monolito):** deploy independente é difícil (exige ferramental próprio construído na mão); escala independente também é difícil (tudo no mesmo codebase/processo — mesmo separando algo, exige muito script customizado); falhas isoladas são difíceis porque tudo roda no mesmo processo.

## A solução: monorepo com arquitetura modular

A solução para essas limitações é o monorepo com arquiteturas modulares — no exemplo, NX (mas dá para usar Bazel, muito usado com Java, ou Maven, que o pessoal Java usa bastante). Com monorepo + apps/packages, é possível fazer a combinação infinita de apps que se quiser: basta colocar um módulo para rodar sozinho (como o exemplo do video-processor) quando ele precisar escalar, ou deixá-lo rodando junto com outros módulos, economizando recursos. Ferramentas como o NX permitem rodar somente o que mudou — se só o módulo de billing mudou, só rodam os testes, o deploy e o pipeline dele. Assim se obtém deploy independente, escala independente e todas as outras vantagens que uma ferramenta de monorepo oferece.

Hoje temos boas ferramentas de monorepo e boas ferramentas de virtualização para rodar tudo isso em produção — é isso que torna possível ir muito além do monolito tradicional e escalar de forma simples, usando qualquer linguagem (o exemplo usa NestJS, mas todas as linguagens têm formas similares de fazer o mesmo).

---

*Nota de transcrição: o autor menciona um curso "Aplicações Enterprise" na Tech Leads Club e um livro em produção, "Os 10 Princípios da Arquitetura Modular". Nomes de empresas mencionados no áudio original de forma foneticamente distorcida ("Atlácia", "Totorks") foram normalizados para "Atlassian" e "Totvs" por contexto (nomes de empresas de tecnologia real e plausíveis foneticamente).*
