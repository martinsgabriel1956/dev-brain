# RAG — Introdução e Pipeline Completo

> Transcrição de aula/vídeo (estilo Full Cycle) sobre os fundamentos de RAG. Formatada em Markdown a partir de transcrição bruta em áudio-para-texto; conteúdo técnico preservado sem edição, apenas pontuação, parágrafos e correções de erros óbvios de transcrição de fala (ex.: "Full Psycho" → "Full Cycle").

## O que significa RAG

RAG significa Retrieval-Augmented Generation. O que isso significa na prática:

- **Retrieval** — busca e recupera informação.
- **Augmented** — pega, de todas as informações buscadas, algo contextualizado que faça sentido para o contexto daquele momento.
- **Generation** — pega esse contexto, manda para um modelo e recebe uma resposta.

Basicamente, quando eu preciso fazer uma pergunta pro meu modelo sobre algo em que ele não foi treinado — o GPT não sabe das coisas da sua empresa, por exemplo — eu preciso dar essa informação para ele. Existem várias formas de fazer isso. Uma delas é pegar informação de banco de dados e embutir isso no prompt.

## O pipeline, na prática

É basicamente um pipeline: chega uma solicitação, é buscada a informação, existe um prompt do modelo, a gente passa o contexto recuperado e coloca embaixo a pergunta do usuário.

Se você perceber, é uma coisa meio ridícula, meio gambiarra: eu pergunto pro agente "quanto custa uma Ferrari, assim assim assado" e o modelo não tem essa precisão, ele não sabe isso. O que ele faz? Vai buscar no banco de dados, e no contexto aparece algo como "uma Ferrari custa $10.000" (exemplo ilustrativo). Aí a pergunta é "quanto custa uma Ferrari?" — adivinha o que ele vai responder: $10.000. Porque eu passei o conteúdo antes. É como se eu tivesse com uma prova e um gabarito junto: a resposta já está no meio da pergunta do usuário.

A gente consegue fazer isso evitando ter que treinar modelos muito específicos, o que entraria num mundo muito caro. Então o RAG combina a busca da informação com um contexto relevante, gerando as respostas pro usuário.

Exemplo: "Qual o prazo para o reembolso para um plano Enterprise?" Eu tenho um assistente, tipo um chatbot. O RAG vai consultar uma base externa, o modelo vai pegar essas informações da base externa e mandar pro modelo. É basicamente isso que acontece.

## RAG é arquitetura, não tecnologia

Quando você fala em RAG, entenda que a gente está falando de pipelines. É por isso que o RAG entra muito na parte arquitetural: ele não é necessariamente uma tecnologia, e sim formatos de pipeline que fazem com que você consiga trazer contextos para responder — ou para que um agente de IA, por exemplo, utilize.

**Ponto importante: RAG não é um agente de IA.** Um agente de IA pode usar, ou fazer parte de, um processo de RAG — mas não necessariamente porque eu tenho um RAG eu tenho um agente de IA. Chamar um modelo não faz, necessariamente, você ter um agente de IA — faz com que você faça uma consulta de API, é isso que acontece na real. Tirem isso da cabeça: qualquer coisa que chama um modelo não é um agente. Eu posso criar um "Hello World" chamando um modelo e não ter um agente — o que eu tenho é uma chamada de API. Isso é importante que fique claro.

## Os dois pipelines: ingestão e consulta

No pipeline do RAG a gente tem dois pipelines principais:

1. **Pipeline de ingestão** — inserir dados num banco de dados para que sejam consumidos.
2. **Pipeline de consulta** — buscar esses dados na hora de responder.

### Ingestão

Eu posso ter diversas fontes de dados: markdown, PDFs, Google Drive, bancos de dados, planilhas, arquivos de texto, balancetes — qualquer coisa que faça sentido a empresa ter e que a gente tenha acesso. A gente extrai metadados, pega esses documentos inteiros e quebra em pedaços menores (não dá pra colocar um documento inteiro numa consulta — imagina ter que colocar o resultado de um livro inteiro pra responder uma pergunta, ou colocar a Bíblia inteira pra tirar dúvida de um versículo).

Para isso, os dados precisam ser buscáveis de forma inteligente no banco de dados. Então eu converto essas informações num formato vetorial — **embeddings** — que é um tipo de modelo que pega um texto e transforma em um vetor. Esses vetores são salvos, por exemplo, no Postgres (usando a extensão **PG Vector**). Existem vários bancos de dados que trabalham no formato vetorial, ou seja, conseguem fazer buscas de proximidade com diversos algoritmos para ver qual consulta chega mais próxima daquele vetor. O Postgres, com a extensão PG Vector, aguenta bastante carga, melhorou muito em relação ao que era antigamente, e dá para rodar em produção tranquilamente — mesmo existindo bancos feitos especificamente pra isso.

### Consulta

A gente pergunta, transforma essa pergunta em um vetor, faz uma busca por proximidade no banco de dados, trazendo os pedacinhos (chunks) mais próximos daquela pergunta. Depois, pega esses pedaços, coloca dentro do prompt, chama o modelo e devolve a resposta.

## Chunking

No meio da ingestão existe um processamento: dividir o documento em pedaços menores sem perder o contexto e o significado — isso é o **chunking**.

O chunking não é uma unidade de busca 100% eficaz. Às vezes um pedacinho de algo fica descontextualizado. Exemplo: eu pergunto "qual é o preço disso?" — a palavra "preço" aparece em vários lugares do sistema, então eu posso acabar pegando preços de produtos errados.

O chunking, no fim das contas, tem estratégias para cortar esses pedaços sem perder o contexto de forma geral: pega uma ideia principal, corta em pedaços, e coloca numa unidade melhor pra buscar. Na hora da pergunta, trago só os pedaços que fazem sentido, baseado num score. Depois disso existem processos mais complexos: reescrita de query, reranking, reindexação. (Aula menciona que o MBA da Full Cycle tem aulas específicas sobre reranqueamento.)

## Como funciona a vetorização

Quando eu tenho a fonte de dados e os chunks (o conteúdo de cada pedaço), cada chunk tem:

- Um **ID**.
- **Metadados** — de onde ele vem, que ajudam nas buscas depois no banco de dados.
- Um **vetor gerado** a partir do conteúdo.

No banco de dados (ex.: Postgres), cada registro tem:

- O **embedding** (o vetor).
- O **texto** daquele vetor (o texto cru) — ou seja, há dado duplicado: o dado representado em vetor e o dado representado em texto.
- Os **metadados** — itens que ajudam a filtrar melhor a informação na hora da busca.

Exemplo prático: se o usuário quer saber algo sobre um produto específico e existem 2 milhões de registros de chunks no banco, não faz sentido buscar nos 2 milhões — busca-se "onde o produto é igual a tal". Esse filtro é um metadado.

## Metadados e filtros — segurança e precisão

O resumo de como isso funciona, por conta dos filtros e metadados:

> Usuário pergunta: "Como funciona o plano Enterprise?" → busca vetorial no banco de dados → vê quais chunks fazem sentido baseado na pergunta.

Nesse meio, existem filtros que podem ser usados: produto = suporte, status = documento publicado, visível ou não, se faz parte de um plano, qual o tipo de documento.

Essa parte de metadado é uma das coisas mais importantes na hora de estruturar um RAG. Por quê? Imagina que existe um RAG da empresa que todo mundo pode acessar — não faz sentido todo mundo poder saber o salário de alguém. Então, provavelmente, é preciso ter no banco de dados (ou na camada de aplicação) formas de filtrar informação, para não correr o risco de trazer dados que o usuário não deveria acessar naquela consulta.

Outros casos de filtro: documento que não está publicado (está como *draft*); documento desatualizado (por isso existe versionamento de documentos); *fingerprint* de documentos (útil depois para trabalhar com cache).

## Chunks elegíveis

Fazer uma busca vetorial e filtrar não traz necessariamente os chunks que você precisa — traz um **conjunto de chunks elegíveis**, ou seja, chunks elegíveis para estar montados no contexto.

Exemplo: recebo 10 pedaços de informação (10 chunks). Olho pra eles e digo: "para responder essa pergunta, preciso ter pelo menos 0,9 de certeza (de 0 a 1)". Dos 10, sobram só 3 chunks elegíveis — uso apenas esses três.

**E se eu achar que nenhum é elegível?** Posso simplesmente dizer que não vou responder. Num RAG, responder "eu não tenho essa informação" é tão importante quanto — ou mais importante do que — inventar a informação ou responder com algo descontextualizado.

Uma vez definida a elegibilidade, ainda dá pra rerranquear (reranking) os chunks elegíveis, dando mais ênfase a uns do que a outros no prompt — existem várias técnicas por trás disso que não são detalhadas aqui.

## O prompt final

O prompt fica montado assim, por exemplo:

- **Sistema**: "Você é um consultor de planos da empresa Full Cycle, entende sobre isso e aquilo, responde educadamente."
- **Contexto**: os chunks recuperados (ex.: informações sobre o plano Enterprise, suporte, etc.).
- **Pergunta do usuário**: "Como funciona o plano Enterprise?"

Esse prompt completo — incluindo os pedaços dos chunks — é enviado ao modelo, e a resposta vem de lá.

## RAG que funciona vs. RAG que não funciona

Fazer isso não é fácil. Fazer algo que responda perguntas baseado no contexto de uma busca vetorial é fácil — dá pra fazer até com um único arquivo. Mas fazer aquilo responder **certo** não é fácil. Existe uma diferença muito grande entre um RAG que funciona e um RAG que não funciona, porque a parte mais importante do RAG, no final das contas, é a **qualidade da resposta**.

Existem diversas técnicas para aumentar esse nível de qualidade. Tem gente que fala "já mexi e já trabalho com RAG", mas, se você for olhar as respostas, sai tudo errado — informação que não deveria, ou a busca faz uma varredura de 1 milhão de registros no banco pra pegar uma informação. A fonte de dados tem que estar muito apurada, e a forma de organizar os metadados tem que ser muito bem organizada — senão você tem um problema muito grave. Não é apenas fazer uma consulta vetorial: é ter uma arquitetura. É por isso que, no MBA da Full Cycle, RAG entra na área de arquitetura na era da IA — trabalhar com isso faz com que você tome decisões arquiteturais específicas para esse tipo de problema.

