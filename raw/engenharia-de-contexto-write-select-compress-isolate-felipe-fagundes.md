# Engenharia de contexto na prática: Write, Select, Compress, Isolate (Felipe Fagundes)

> Transcrição de vídeo de YouTube de Felipe Fagundes, colada pelo usuário e limpa. Já estava em português; sem tradução.
> Limpeza: pontuação e parágrafos adicionados; hesitações e repetições de fala removidas; correções de ASR ("making inspector" = função inspetora do contexto, nome exato incerto; "Miders" = middlewares; "link chain" = LangChain; "lock de scratch de investigação" = log do "scratchpad" de investigação, incerto; "hag" = RAG; "cloud" = Claude; "somarização" = sumarização). Omitido: abertura/saudação, pedido de inscrição/like/comentário e despedida. Números são os mostrados pelo autor em uma demo com dados fictícios; nada é verificado.

## Tese e promessa

Nenhuma janela de contexto de milhões de tokens resolve o problema, porque o problema sempre foi **o que se coloca dentro da janela**, não o tamanho dela. O autor mostra um agente que construiu e que precisava de ~8.000 tokens para gerar uma única linha de resposta, com custo alto; mostra como reduziu o pico de tokens em **71%** e apresenta quatro técnicas que engenheiros de IA usam para controlar o contexto: **Write, Select, Compress, Isolate**.

## Passo zero: enxergar antes de melhorar

A engenharia de contexto **começa na análise, não na melhoria**. O autor cria uma função inspetora que, a cada chamada ao LLM, retorna: (1) quantas mensagens entraram, (2) uma estimativa aproximada de tokens e (3) a lista de ferramentas disponíveis naquele turno.

## O agente problemático (baseline)

- Um agente **SRE** que analisa três serviços fictícios.
- Ferramentas: buscar logs, listar serviços e outras sem sentido para o caso (ex.: "traduzir texto"), colocadas de propósito para **poluir o contexto**.
- A ferramenta de buscar logs devolve logs fictícios, com tokens estimados.
- Uma lista de perguntas simula os turnos de conversa do usuário (cada linha = uma mensagem).
- Resultado: em todo turno o contexto carrega ferramentas inúteis (ex.: "traduzir texto"), o que dá ao agente mais decisões a tomar e aumenta o que o autor chama de **superfície probabilística** (mais chance de erro). Os tokens crescem em saltos a cada turno; no último turno — pedido de resumo das análises dos três serviços — foi preciso carregar uma janela de **8.339 tokens**, por concatenar todas as mensagens e respostas anteriores mais a lista de ferramentas inúteis repassada a cada vez.

## 1. Write — escrever em memória o que importa

Em vez de apagar coisas do contexto sem como recuperá-las, **salva-se em memória** as informações relevantes ou textos grandes e recupera-se depois.

- Com LangChain: `store.put` com um **namespace** (como um nome de pasta, para organizar), um **identificador** (para recuperar) e o **conteúdo**.
- Dois tipos de memória aparecem nos logs:
  - **Semântica**: especificidades do usuário (time para o qual torce, formato de resposta preferido).
  - **Episódica**: um evento/ação que o LLM julgou importante para o contexto daquele agente.
  - Há uma terceira, **procedural**: regras de como alguma ação foi feita (não usada na demo).
- Ganho: a informação saiu do contexto **sem ser perdida**.

## 2. Select — recuperar com filtros (e filtrar ferramentas)

Objeção do autor a si mesmo: "se salvo em outro lugar e recupero tudo, dá na mesma?" Resposta: não, porque **na recuperação aplicam-se filtros**. O que ele usa (não necessariamente o padrão que todos devem seguir):

- **Janela de tempo**: parâmetro em horas; com `1`, só volta memória com menos de 1 hora.
- **Importância**: de 0 a 1, atribuída na hora de salvar (o LLM julga a importância); a recuperação filtra por esse parâmetro.
- **Degradação (meia-vida)**: parâmetro `meia_vida_horas`; com 72, a importância começa em 1, cai para 0,50 após 72 h, 0,25 após mais 72 h, e assim por diante.
- Alternativas: RAG ou busca por termos-chave (a função de tokenizar da demo faz busca por palavras-chave).
- Princípio: **a memória não é tratada como fonte completa da verdade**; sabe-se que as coisas estão salvas, mas sempre se aplica um filtro para trazer só o relevante.

**Select também vale para ferramentas.** Uma variável `domínios` mapeia palavras-chave da **última mensagem do usuário** para um conjunto de ferramentas relevantes; a ferramenta de traduzir some da lista porque não faz sentido para o agente SRE. O filtro é **dinâmico por turno**: dá ao agente só o que ele precisa e evita que fique "pensando" qual ferramenta usar. (Os domínios/palavras-chave da demo são fictícios.)

## 3. Compress — manter o sinal, descartar o resto

Duas camadas:

1. **Sumarização**: quando a conversa chega a **3.500 tokens**, faz-se uma sumarização; pode-se customizar com um system prompt específico definindo o que manter.
2. **Clipar e offload**: se o resultado de um turno/ferramenta passar de **1.200 tokens**, **nada é excluído**: o conteúdo completo é salvo em memória (a "memória intacta", recuperável com filtro), e no contexto permanece só o sinal — no caso, as **últimas linhas com `error` e `warn`** (por serem logs). O corte deve ser adaptado ao contexto de cada aplicação.

## 4. Isolate — subagentes

Usar **subagentes** isola o contexto principal: o subagente recebe uma tarefa extensa, gasta muitos tokens processando, e devolve só um **resumo curto** (algumas linhas, ~180–200 tokens) em vez de 2.000–3.000 tokens. O autor reconhece o **custo adicional**, mas o objetivo aqui é **preservar o contexto principal**. Menciona que Claude e Codex fazem isso ao disparar subagentes em pesquisas extensas. Na demo, um subagente processa os logs volumosos de cada serviço e devolve uma linha de diagnóstico.

## O agente reformulado (as quatro juntas)

Novo system prompt (um pouco maior, o que aumenta a primeira chamada), lista completa de ferramentas passada novamente mas **filtrada em runtime**, e **middlewares** para o select de memórias, a compactação e a seleção dinâmica de ferramentas.

Resultados mostrados:

- Última chamada (o resumo): de **~8.339 para 2.426 tokens** (o "71%" do título). Isso pode permitir **modelo menor** e, portanto, custo menor.
- A ferramenta "traduzir" não aparece mais no contexto (contexto "limpo").
- Subagentes: o subagente processou ~2.525 tokens, mas o contexto principal foi de **1.815 para 1.999** antes/depois — ou seja, o processamento pesado ficou fora, e só poucas linhas entraram.
- Um **scratchpad de investigação**: após cada análise de serviço, o diagnóstico foi salvo em memória; no pedido final de resumo, o agente **não releu os logs**, apenas recuperou essas poucas linhas da memória.

## Conclusão do autor

Tratar engenharia de contexto como **arquitetura e decisão de projeto**, não como algo "bonito de falar": **escrever** o que precisa sobreviver fora da janela, **selecionar** memórias quando necessário, **comprimir** informação pesada preservando só o sinal (sem descartar totalmente), **isolar** tarefas que não precisam estar no contexto principal. O resultado "não é apenas menos token": o agente recebe **menos ruído**, e menos ruído = menor **superfície probabilística** = respostas mais assertivas.
