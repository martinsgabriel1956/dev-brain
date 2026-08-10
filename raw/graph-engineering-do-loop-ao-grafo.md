# Graph Engineering: Do Loop ao Grafo

> Transcrição bruta em bloco único, sem pontuação/seções — reestruturada em markdown (o que é um grafo, exemplos cotidianos de nós/arestas/pesos, grafos em redes sociais e em métricas de negócio, o tweet de Peter Steinberger que disparou o termo "graph engineering", o motivo de uma métrica isolada nunca ser suficiente, o exemplo de gestão de projeto com épicos/histórias/tarefas como grafo de dependências, e o fechamento sobre fundamentos como alavanca contra o FOMO tecnológico). Vídeo original em português, patrocinado pela Hotmart.

## Contexto: "Toda Semana Tem Que Aprender Algo Novo"

Toda semana surge algo novo para aprender: loop engineering, Hermes, um novo agente de IA, e agora grafos — "ainda tá fazendo loop? A onda agora é graph". A mudança começou com um tweet de **Peter** (citado como "criador do Open Claw"), que disse basicamente: "estamos todos ainda fazendo loops, ou já podemos mudar para graphs?" — "skill, harness, loopy, graph, this changes everything". Toda semana um novo termo vira post de LinkedIn ("long live graph engineering"). Se você usa ou constrói um agente, e se o seu produto depende de um agente funcionando em produção, este vídeo é sobre essa mudança de arquitetura — começando pelo que, de fato, é um grafo.

## O Que é um Grafo

Um grafo é uma estrutura de dados simples — a mais simples depois de uma lista. Tem apenas duas coisas:

- **Nodes** (nós) — representados por "N" no algoritmo.
- **Edges** (arestas) — a ligação entre nós, representada por "E".

## Exemplo Cotidiano: a Manhã Como Grafo

Uma manhã típica, modelada como grafo:

- Nó "dormindo" → nó "acordar", com uma aresta de **peso** (edge weight, `ew`) de 2 minutos até "levantar".
- Nó "levantar" → nó "escovar os dentes", aresta de 5 minutos.
- Nó "escovar os dentes" → nó "café na xícara", aresta de 3 minutos.

Pesos podem representar qualquer coisa — inclusive automação: "eu tenho alguém que me traz café na cama, grito pro meu robô antes de levantar, ele prepara o café enquanto eu ainda durmo, e recebo o café antes mesmo de levantar da cama". No momento em que esse grafo tem pesos nas arestas, dá para implementar buscas e otimizações sobre o processo — em vez de escrever vários arquivos `.md` soltos em pastas para um agente navegar, dá para desenhar um grafo de informação e desenhar a engenharia de como ligar/conectar/pesar esses nós.

Todo mundo que já resolveu problemas de LeetCode reconhece essa progressão: lista → lista encadeada → árvore → árvore binária → grafo.

## Grafos em Redes Sociais

Em uma rede social (do ponto de vista de quem a constrói, não de quem a usa), cada pessoa normalmente é um nó, e cada relação tem um peso — amizade, familiaridade, tópicos semelhantes, trabalho, outras redes onde essas pessoas se conectam. Isso cria o grafo social, e os algoritmos hoje navegam nesse grafo para decidir que tipo de conteúdo oferecer. Exemplo: quando o LinkedIn diz "vocês têm três conexões em comum, adicione esta pessoa" — essas "três conexões" são, literalmente, três arestas de distância no seu nó.

## Grafos em Métricas de Negócio

Numa startup: tráfego → gera signup → gera conta criada → gera ativação → pode gerar assinante premium → pode gerar churn → que define o LTV. Uma campanha de marketing tem um budget que gera tráfego, e essa mesma campanha pode gerar um percentual de churn diferente dependendo da qualidade do lead (lead não tão quente, ou fora do público-alvo do maior use case da aplicação). Dá para modelar até um negócio inteiro como grafo, e deixar um agente de IA tomar decisões ou dar insights de forma autônoma em cima dele.

## Exemplo de Produto Digital: o Afiliado Como Aresta

Para um criador de conteúdo (SaaS, curso, PDF, webinar, mentoria), o nó "produto" só vale alguma coisa se conectado ao nó "consumidor" — a pergunta central é como desenhar essa aresta. Colocar um produto no ar é uma coisa; fazer alguém chegar até ele é outra. Estratégias de conexão incluem tráfego pago, SEO/orgânico e afiliados — o afiliado é literalmente uma aresta: uma pessoa que conecta o produto a outras pessoas, tipicamente alguém com audiência mas sem o conhecimento para gerar o produto em si.

**Nota de patrocínio:** o vídeo é patrocinado pela Hotmart, citada como maior plataforma de produtos digitais do mundo (mais de 25 milhões de compradores, R$ 50 bilhões em vendas), com publicação gratuita (paga-se apenas sobre venda realizada).

## O Tweet de Peter Steinberger e "Uma Métrica Nunca é Suficiente"

Peter publicou nove palavras que receberam milhares de curtidas, dizendo que a previsão mais segura é que a arquitetura em loop se tornará ortodoxa da mesma forma que loops simples e tutoriais serão substituídos — **porque uma métrica nunca é suficiente**.

Exemplo prático: um agente de IA rodando em loop para otimizar uma campanha de marketing, buscando a melhor imagem/texto que gera mais tráfego com menor custo de aquisição (CPI, CAC). O agente em loop consegue, de fato, baixar esse custo — mas, se ele está olhando **apenas** para essa métrica, pode estar ignorando um aumento no churn. O CAC cai, mas o churn sobe, o LTV cai, e isso coloca o próprio CAC em risco (não compensa mais adquirir um cliente que sai rápido demais). Por isso "uma métrica nunca é suficiente": é preciso olhar para múltiplas métricas simultaneamente e entender como uma afeta a outra.

Quando se precisa rodar um ou múltiplos agentes em paralelo, dando não um objetivo com uma métrica, mas **múltiplas métricas e como elas se afetam entre si**, a estrutura de dados necessária para representar isso para a IA é o grafo.

## Passo a Passo Recomendado: de Loop a Grafo

1. **Criar um loop simples primeiro** — task curta, objetivo claro. Pode ser um objetivo de SaaS, ou algo mais sistemático como a criação de tarefas: um PM desenha como tickets se relacionam (épico → história → tarefas → subtarefas), com dependências entre eles — não é uma árvore, porque há dependências cruzadas.

   - Exemplo: dentro de um épico, no mínimo dois devs podem trabalhar em paralelo (um por história), porque as histórias não dependem uma da outra diretamente.
   - Uma tarefa pode ter subtarefas que não se bloqueiam entre si (ex.: interface com dados mocados, em paralelo a quem ainda está construindo a base de dados) — permitindo alocar mais um dev/agente sem esperar a dependência anterior terminar.
   - Em times grandes (exemplo citado: 50 programadores num mesmo projeto, múltiplos times e "TPOs" — technical product owners — na Disney), o board de tarefas fica cheio de tasks e subtasks, e boa parte do tempo é gasta alinhando, não programando.

2. **Criar grafos** — o segundo passo é resolver como escalar de "um agente em loop até concluir uma única tarefa" para "múltiplos agentes com contexto suficiente para trabalhar em múltiplas tarefas ao mesmo tempo", sem que informações fiquem desatualizadas ou tarefas conflitem entre si. Para todo grafo é preciso também um checklist de conclusão — o peso daquela aresta —, e esse checklist, em algum momento, envolve a aprovação de um ser humano.

## Origem Provável do Termo: Peter Queimando US$ 1 Milhão/Mês em Tokens

A necessidade de criar grafos veio, provavelmente, de Peter estar "queimando 1 milhão de dólares por mês em token" ao rodar múltiplos loops simultaneamente. Em algum momento, esses loops paralelos começaram a conflitar entre si, ou informações ficaram desatualizadas ao concluir tarefas feitas em paralelo. Em vez de pensar em prompts e tickets simples para a IA, torna-se necessário criar um grafo e passar isso para um orquestrador.

Quem já fala "agora o foco é graph engineering" já está num nível de uso de IA em que a IA não está apenas escrevendo código para a pessoa — está resolvendo vários tickets ao mesmo tempo.

## Fechamento: Fundamentos Como Alavanca Contra o FOMO

Ponto final do vídeo: o fato de já saber o que é uma estrutura de dados de grafo fez com que o autor assimilasse rapidamente o conceito de "graph engineering" ao ler o tweet — sem precisar parar tudo para estudar do zero, porque "semana que vem vai vir outra coisa". Em vez de se jogar de cabeça em cada novo termo sem saber o porquê nem para que serve, a recomendação é parar e pensar na própria "alavanca" (leverage): **a IA é uma alavanca de algo que a pessoa já faz e já sabe** — e essa alavanca aumenta com mais conhecimento prático e mais conhecimento de base. Quem tem esse conhecimento de base perde o FOMO: ao ver "graph engineering" num tweet, consegue pensar "isso deve ser sobre grafo" e decidir conscientemente não parar a vida para estudar aquilo imediatamente, em vez de reagir por ansiedade a cada novo termo.
