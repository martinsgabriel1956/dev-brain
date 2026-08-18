# Tokens: o que são e por que custam tão caro

> Transcrição de vídeo (PT-BR, sem tradução necessária). Fonte original em áudio, formatada em Markdown para ingestão na wiki.

A palavra "token" virou uma super buzzword na nossa área, mas praticamente ninguém entende de fato o que são tokens. Todo mundo está meio obcecado em gastar o máximo de tokens possível e nem entende por que esses tokens custam caro quando o modelo está gerando um output pra gente. Neste vídeo, um detalhamento mais profundo do que de fato são tokens, por que as LLMs precisam transformar nosso texto em tokens, e por que o token de output custa tão caro e pesa tanto na fatura.

## O que são tokens

A resposta simples: um token é uma palavra ou um pedaço de uma palavra.

LLMs (Large Language Models) são, no final das contas, modelos estatísticos — matemática, cálculos para prever a próxima palavra. O que uma LLM faz é multiplicação de matrizes, e dentro dessas matrizes só existem números. A LLM não lida com palavras nem com letras — ela lida exclusivamente com números. Nós, humanos, nos comunicamos por linguagem. Então como fazer a LLM entender nossa comunicação? Daí surge a unidade do token: uma maneira eficiente de traduzir nossa linguagem para algo entendível pelas LLMs.

Por que "pedaço de linguagem"? Na frase "o Claude é demais!", nós humanos enxergamos a palavra "Claude", "é", "demais" — os espaços não fazem muita diferença pra gente, a exclamação é só entonação. Para a LLM é completamente diferente: tudo que compõe a frase faz efeito no momento do cálculo. Foi necessário encontrar uma forma de traduzir frases (linguagem humana) para números — dividir o input em pedaços de palavra e então codificar esse input para números.

### Por que não dividir letra por letra?

Isso tornaria as matrizes muito maiores e exigiria muito mais cálculo: para cada frase, milhões de tokens a processar. Toda vez que o modelo tentasse compreender a correlação entre as palavras, primeiro teria que entender o que está perto do quê para formar uma palavra. Exemplo: a palavra "cat" viraria C-A-T, e o primeiro cálculo seria entender que aquilo é uma única palavra, não três coisas diferentes — desperdício de raciocínio, muitas quebras desnecessárias.

### Por que não dividir palavra por palavra?

Aí o problema não é mais de cálculo, é de vocabulário: seria preciso mapear todas as palavras de todas as línguas do mundo para o modelo performar em qualquer idioma. Mais que isso: não só as palavras, mas todas as suas flexões. Ex.: "corre" pode virar "corria" (passado), "corríamos" (plural), "correndo" (gerúndio), etc. — cada flexão sendo uma palavra nova nesse esquema, o que explode o vocabulário necessário.

### A solução: quebrar em pedaços (subword tokens)

A forma mais inteligente é quebrar as palavras em pedaços comuns entre suas flexões. Ex.: para "corre", "corria", "corríamos" — o pedaço "corr" é comum a todas as flexões e pode virar um token; o sufixo ("e", "ia", "íamos") vira outro token. Isso é fruto de um estudo/treinamento sobre um grande vocabulário de palavras de diversas línguas: o modelo aprende a forma mais comum como letras aparecem juntas e formam palavras, e então constrói seu próprio vocabulário de tokens.

No final, o processo é: dividir o input em tokens (ainda entendível por nós) → codificar esses tokens para números (entendível pelas LLMs).

## O tokenizer e o tamanho do vocabulário

Cada LLM tem seu próprio vocabulário, formado pelo **tokenizer** (tokenizador) — uma pequena rede neural cuja única função é traduzir o input para tokens. É a primeira etapa de processamento em qualquer LLM (Claude, Gemini, GPT etc.) antes de gerar uma resposta.

Cada tokenizer tem um tamanho de vocabulário diferente (ex.: 200.000 tokens vs. 1.000 tokens). **Quanto maior o vocabulário, menor a quebra em tokens** — e vice-versa:

- Vocabulário de apenas 1.000 tokens: as palavras precisam ser quebradas em pedaços bem menores (quase do tamanho de uma letra) para representar todas as palavras existentes no mundo, porque só há espaço para 1.000 entradas nesse vocabulário.
- Vocabulário de 200.000 tokens: dá pra guardar junções mais completas — por exemplo, "entendimento" poderia virar só 2 tokens, enquanto num vocabulário menor "end" (comum a inglês e português) seria um token reaproveitado em ambos os idiomas.

### Experimento prático: GPT-4o vs. Claude Opus 5

Comparação de quebra em tokens usando a mesma frase ("a raposa marrom rápida pula sobre o cão preguiçoso" / "the quick brown fox jumps over the lazy dog") nos dois modelos:

- **Em português**, GPT-4o gastou **22 tokens**; Claude Opus 5 gastou **42 tokens** — quase o dobro.
- O tokenizer do GPT-4o é público (documentado); o da Anthropic é privado, não divulgado.
- A explicação mais provável: o vocabulário do tokenizer do GPT-4o é maior (200.000 tokens como base), permitindo representações menos granulares (menos pedaços por palavra). O vocabulário da Anthropic é menor, exigindo mais pedaços para representar a mesma palavra. (Suposição do autor — a Anthropic não divulga o tokenizer, então não há como confirmar com certeza.)
- **Em inglês**, a mesma frase caiu para **15 tokens** no GPT-4o e **35 tokens** no Claude Opus — ambos caíram bastante frente ao português.
- Motivo: o inglês é a língua predominante nos dados de treino desses tokenizers (mais textos, código etc. online em inglês). Quanto mais comum uma palavra ou junção de letras nos dados de treino, mais provável que aquilo vire uma unidade única (um token) no vocabulário. Isso não significa que o modelo "não entende" português — só que ele precisa de uma representação mais granular (mais tokens) para o mesmo conteúdo.

### Experimento: palavra inventada vs. palavra real

Testando a palavra inventada "Ubazu" (sem significado, 5 letras) contra "carro" (palavra real, também 5 letras):

- "Ubazu": 10 tokens no Claude Opus, 2 tokens no GPT-4o.
- "carro": caiu para 8 tokens no Claude Opus (do mesmo comprimento, mas junção de letras mais comum na língua).

Confirma o padrão: quanto mais comum a sequência de letras nos dados de treino, menos tokens ela consome — independentemente do número de caracteres.

## Por que os tokens são tão caros (e por que o output custa mais que o input)

Analogia: ao ouvir uma história longa e depois responder uma pergunta sobre um detalhe específico (ex.: a cor de uma camiseta mencionada no início), um humano não precisa reler a história inteira palavra por palavra — ele guarda informações relevantes na memória e raciocina em cima delas.

**LLMs não funcionam assim.** Elas usam uma técnica chamada **autorregressão** (geração autorregressiva): para cada novo token gerado, o modelo precisa **reprocessar todo o texto imputado anteriormente mais o novo token gerado**.

Exemplo passo a passo — completar "o gato":
1. Modelo gera "senta" → contexto agora é "o gato senta" (3 tokens efetivos).
2. Para gerar o próximo token, o modelo reprocessa "o gato senta" inteiro — não dá pra prever o que vem depois de "senta" isoladamente, sem o contexto anterior.
3. Gera "no" → contexto agora é "o gato senta no". Reprocessa tudo de novo para gerar o próximo.
4. Gera "tapete" → contexto "o gato senta no tapete". Reprocessa tudo de novo.
5. E assim por diante, a cada token gerado.

A cada rodada, a quantidade de tokens sendo reprocessados aumenta — e é isso que torna cada execução progressivamente mais custosa em termos de processamento. Quanto maior a resposta gerada pelo modelo, mais tokens são gastos reprocessando contexto, e mais caro fica.

### Cobrança por token: input vs. output

Providers de LLM cobram por token, com preços diferentes para input e output. Exemplos citados (por 1 milhão de tokens):

- **Claude Opus**: input ~$5, output ~$25 (a saída custa 5x mais que a entrada).
- **Claude Sonnet**: preço de output também maior que o de input (proporcionalmente menor que Opus em valor absoluto, mas segue o mesmo padrão).
- **Claude Haiku** (modelo mais barato da Anthropic): output também mais caro que input, mesmo padrão relativo.
- O mesmo padrão (output mais caro que input) se repete em todos os providers — OpenAI, modelos chineses, etc.

### Por que o output é sempre mais caro que o input

- **Processo de input**: mais simples e "preto no branco" — pega o input do usuário, divide (tokeniza) e codifica (encoding). Não é recursivo.
- **Processo de geração do output**: é recursivo por natureza — para cada nova palavra gerada, o modelo precisa recolocar tudo que já foi gerado no contexto, para poder prever a próxima palavra corretamente. Não dá pra prever cada palavra isoladamente sem o contexto acumulado.

Essa é a razão estrutural (não apenas comercial) pela qual o output custa mais: a própria forma como os modelos autorregressivos funcionam para prever a próxima palavra exige reprocessamento cumulativo de contexto a cada token gerado.

## Resumo do pipeline completo

1. Input em linguagem natural.
2. Tokenização (pelo tokenizer, um modelo específico só para essa tradução) → pedaços de palavra.
3. Encoding → pedaços de palavra viram números.
4. Números viram matrizes, multiplicadas pelo modelo (inferência/previsão).
5. Output do modelo também é número.
6. Decoding → números voltam a virar texto em linguagem natural.
7. Esse processamento acontece de forma recursiva/autorregressiva: cada novo token gerado é reimputado na rede junto com tudo que foi imputado anteriormente, para prever o próximo token — e é por isso que o custo de output é muito mais caro que o de input.
