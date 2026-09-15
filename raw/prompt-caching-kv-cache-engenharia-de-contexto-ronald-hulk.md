# Prompt Caching e KV Cache: Como Fazer Prompting Como um Profissional

**Autor:** Ronald Hulk
**Formato:** transcrição de vídeo (YouTube)
**Tema:** engenharia de prompt / cache de inferência de LLM

---

Ok, você deve estar vendo esse print aí e deve estar se perguntando: "Nossa, a solução dele é muito mais eficiente que a minha?" Se você tá pensando isso, provavelmente você está correto — mas isso não precisa ser assim para sempre, e neste vídeo eu vou te mostrar como fazer prompting como um profissional. Para você que não me conhece, meu nome é Ronald Hulk e eu ajudo indivíduos e empresas a colocarem soluções de IA em produção e lucrarem com isso. Vamos pro vídeo.

Esse vídeo vai ser bem direto, então recomendo você ir com papel e caneta na mão anotando as coisas para depois poder aplicar de fato. Então: você entende, analisa e aplica. Você tá na camada do entendimento agora.

Antes de eu te explicar exatamente como fazer, eu preciso explicar o que é, senão não faz nenhum sentido, correto? Você já ouviu falar essa palavra "cache" em algum momento. Você pode pensar na mesma lógica de cache — por exemplo, quando você tem alguma aplicação que faz um cache de alguma informação e você recupera. Só que aqui a gente tem uma camada chamada **KV Cache**, que é: quando você tá fazendo inferência, quando você chama uma API e tem um computador lá trabalhando, processando esse token para te dar a resposta, ele guarda essa informação que você enviou em algum lugar para ficar mais fácil de recuperar.

Então o que a gente vai fazer é usar essa "janelinha" e manipular ela para usar mais vezes de maneira mais eficiente. Por que a gente vai fazer isso dessa maneira? A gente evita gastar mais computação — computação tem custo, correto? Tem eletricidade, tem um monte de coisa por trás. E a gente vai fazer com que não exista reprocessamento de várias coisas que a gente não precisa reprocessar. Então, ao invés de pagar pela mesma coisa, você vai deixar de pagar pela mesma coisa — você vai pagar um valor bem descontado. E quais as vantagens disso? Sua solução vai ser mais rápida e vai ser mais barata para você. Então todo mundo gosta disso, e é isso que a gente quer.

## Como funciona

Você faz a primeira chamada lá, passando suas ferramentas, é o prompt, né, o system prompt, e uns documentos, por exemplo fixos, que você tem lá. Ele vai lá no seu provedor de IA que você usa — tanto faz qual é — e ele vai escrever no cache. Escreveu, beleza, show de bola.

Na segunda chamada, ele vai usar o mesmo prefixo, porque as ferramentas são as mesmas, correto, o prompt é o mesmo, e de repente o documento que você tá usando de base é o mesmo. Então ele não vai reprocessar essa parte — ele vai reprocessar só a pergunta nova. Você vai economizar um tanto de token aí, e obviamente vai ser mais rápido, porque tudo já está processado, ele só vai ver o cache e vai seguir em frente.

E é exatamente o contrário que vai acontecer nas soluções que não usam o cache: elas vão fazer com que o contexto seja repetido, então o input vai ser reprocessado, e o que acontece é que você vai pagar a conta inteira de novo de algo que já foi trabalhado. Então você tá literalmente desperdiçando o recurso. Se você é engenheiro de IA, você se ocupa de otimizar recursos — isso é engenharia. É isso que você faz muito bem.

Usando o KV Caching você faz isso de maneira eficiente, porque reaproveita o recurso que já foi computado, correto. No fundo você tá economizando, tá salvando a natureza, tá fazendo tudo bem. Então não tem porque não fazer isso.

E o importante para a sua solução é que o **time to first token** (TTFT — tempo para o primeiro token) é menor. Esse é um conceito que você encontra em ferramentas como a Rock Pro, com boas fontes sobre engenharia de IA em alto nível.

## Regras variam por modelo e provedor

Aqui a gente começa a entrar num ponto importante: para cada modelo existem diferenças de regra para alcançar o KV Cache. Existe uma regra universal — a gente organiza o prompt de uma certa maneira — mas cada provedor pode fazer o caching de forma diferente.

- **Anthropic** é um caso especial: até bem pouco tempo você tinha que forçar muito mais para o cache ocorrer, e o tamanho mínimo do prefixo era muito grande.
- **Os modelos da OpenAI** já são mais fáceis de usar, relativamente há pouco tempo.
- **Os modelos via OpenRouter** — que agrega muitos modelos — funcionam na combinação modelo + provedor, então você tem que analisar caso a caso.

Para usar prompt caching existe um mínimo de tokens enviados. Na Anthropic, por exemplo, uns seis meses atrás (indústria anda muito rápido), se você mandasse um prompt muito pequenininho ele nunca batia o cache — nunca escrevia, nunca recuperava. Isso varia de modelo para modelo, e os modelos mais modernos estão aceitando prompts pequenos.

- **OpenAI:** hoje o caching é **implícito** — você não precisa fazer nada, só entrar dentro da condição mínima de tokens, e ele ativa sozinho. Antigamente não era assim.
- **Anthropic:** você tem um conceito chamado **Time to Live (TTL)** — quanto tempo você mantém esse cache — e você precisa controlar isso, o que dá mais trabalho.
- **OpenRouter:** depende do modelo que você tá usando. Por exemplo, o **DeepSeek** aceita cache com prompts bem pequenininhos, e é bem fácil de usar.

### Diferença de tamanho mínimo de prefixo entre modelos (Anthropic)

Modelos antigos da Anthropic (ex.: Sonnet 4.5, ~6 meses atrás no momento da gravação) exigiam **4096 tokens** de entrada mínima para o cache ser gravado — se você não mandasse esse tanto, o cache nunca era criado, e você sempre pagava o preço cheio. Já em modelos mais recentes, como o **Opus 5**, esse mínimo caiu para **512 tokens** — mostrando que a indústria está se preocupando cada vez mais com isso. Modelos intermediários citados: GPT 5.6 e Sonnet 4.6, cada um com seu próprio mínimo por modelo/provedor.

## Erros comuns (antipadrões)

Independente do modelo/provedor, existem técnicas básicas e padrões que valem seguir. Dois erros muito comuns vistos em consultoria ajudando empresas a colocarem soluções de IA em produção de forma eficiente:

1. **Colocar timestamp/data logo no início do prompt** (ex.: junto do system prompt "Você é um assistente tal..."). Se essa data muda a cada minuto/segundo, o prefixo do prompt está sempre mudando — e isso impede que o cache seja reaproveitado, porque a entrada nova nunca bate com o que já está no cache. Correção: **informação dinâmica (timestamp, dados vindos do cliente que são injetados a cada chamada) deve ir no final do prompt**, não no início.

2. **Estrutura ideal ("shape" de cache aproveitável):** system prompt → descrição das ferramentas → documentos fixos (se houver) → só depois os dados variáveis da chamada específica. Isso maximiza a porção do prompt que pode ser cacheada e reaproveitada entre chamadas.

Exemplo prático citado: numa ferramenta como a Rock Pro, ao fazer uma primeira pergunta (RAG por trás, busca e exibe a informação), esse primeiro turno vira prefixo fixo cacheável. Perguntas seguintes na mesma conversa reaproveitam esse cache e só pagam pelo processamento da pergunta nova.

## Cinco requisitos mínimos para alcançar cache hit

1. **Suporte** — verificar se o modelo/provedor suporta prompt caching (na OpenRouter, verificar modelo *e* provedor).
2. **Cuidado com o prefixo** — organizar o prompt na ordem certa (fixo primeiro, variável por último).
3. **Tamanho mínimo** — saber qual é o mínimo de tokens exigido para aquele modelo/provedor alcançar o cache.
4. **Continuidade/TTL** — saber por quanto tempo o cache persiste (ex.: se você voltar no dia seguinte, o cache ainda está lá?).
5. **Medição** — medir se o cache está de fato sendo usado. A métrica que a própria OpenAI/Anthropic reporta é um ponto de partida, mas idealmente você quer uma fonte de verificação independente delas — via ferramentas de telemetria para IA (ex.: LangSmith, LangFuse) — para confirmar se os números batem.

### Fluxo esperado

- Primeira pergunta, com um prefixo: escreve no cache (cache miss, grava).
- Segunda pergunta, mesmo prefixo: bate no cache (cache hit), processa só a parte nova.
- Se o prefixo muda (antipadrão) ou não atinge o mínimo exigido: sempre processa tudo de novo, nunca alcança o cache "bonito".

**Atenção ao log/payload:** a forma como cada provedor reporta informação de cache no payload de resposta é diferente. Você pode estar de fato batendo o cache mas olhando no lugar errado da resposta e achando que não está funcionando — então preste atenção em onde, especificamente, cada provedor (OpenAI, Anthropic etc.) expõe essa informação.

## Conclusão

A indústria de IA aplicada ainda está no início — os nomes e padrões de prompt caching ainda não estão totalmente consolidados nem documentados de forma unificada entre provedores. Esse tipo de conhecimento prático não está (ainda) nos livros — está "nas ruas", no mundo real, com quem está construindo. Existe um livro de engenharia de IA considerado bom, mas a prática de fato acontece ao vivo, com pessoas reais, não só na teoria.
