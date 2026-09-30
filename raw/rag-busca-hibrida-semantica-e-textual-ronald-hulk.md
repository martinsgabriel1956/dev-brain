# Sua RAG é Ruim? Busca Híbrida (Semântica + Palavra-chave) na Prática

**Autor:** Ronald Hulk
**Formato:** transcrição de vídeo (YouTube), já em português (sem tradução)
**Tema:** RAG, busca semântica, busca textual/palavra-chave, busca híbrida, fusion, top-K
**Título:** derivado do conteúdo (a transcrição abre com "Sua RAG é ruim?").

> **Nota de limpeza:** transcrição automática limpa e estruturada em parágrafos; o conteúdo não foi resumido. Termos corrompidos corrigidos por contexto:
> "reg"/"regia"/"ha" → RAG / IA · "bed"/"beding"/"imbédi"/"B jeans" → embedding(s) · "topic"/"top K" → top-K · "Rock Pro" → nome da harness online do autor (grafia mantida da fonte anterior do mesmo autor) · "quadjuvantes" → coadjuvantes · "Antrópic" → Anthropic · "cloud" (no trecho da memória) → Claude · "Fusion" → etapa de fusão de rankings.
> Trechos ambíguos: "120 150 200 milhões de tokens" (provavelmente **mil** tokens; o autor diz que o desempenho cai a partir daí); a palavra buscada na demo ("B jeans") é provavelmente "embeddings"; "a bad sozinho funciona" (frase da memória semântica) foi interpretado como "a busca por palavra-chave sozinha funciona" — incerto.

---

## Abertura

Sua RAG é ruim? Então bem-vindo ao clube. Tive essa epifania há uns dois anos, quando construía minhas primeiras soluções de RAG e os modelos eram bem diferentes. Saí em uma jornada para descobrir como fazer uma RAG que de fato funciona, e a única verdade de lá para cá é que **busca semântica não é suficiente**. Neste vídeo mostro como uma RAG de **busca híbrida** funciona e por que funciona — não em teoria, não em regra hipotética, mas com uma harness online, um sistema em funcionamento.

Meu nome é Ronald Hulk e eu ajudo indivíduos e empresas a colocarem soluções de IA em produção e lucrarem com isso.

## RAG é, acima de tudo, um problema de busca

RAG é um dos assuntos mais importantes relacionados à IA, porque há muitas aplicações. No início das LLMs elas não chamavam ferramentas como hoje, e fazíamos RAG de um jeito. A partir do momento em que as LLMs passaram a chamar ferramentas de maneira consistente, o que fazemos é dar uma **ferramenta de busca** ao agente. Essa ferramenta de busca é, na verdade, uma RAG: ela busca no banco de dados (ou onde você quiser), devolve o resultado para a LLM, e a LLM dá a resposta. É basicamente isso. Então RAG, acima de tudo, é um **problema de busca**.

Aí entra a **busca semântica**, um dos atores principais do vídeo: ela se preocupa com **significado**. E por que não é suficiente? Porque, se você ainda não tem uma solução de IA em produção, vai ver que o usuário muitas vezes não facilita para que a informação que ele quer seja achada. Você precisa de técnicas complementares à busca semântica — é isso que exploramos hoje.

O roteiro: ver como as duas buscas funcionam, como combiná-las e, finalmente, como o contexto é entregue ao agente para que ele responda.

## Chunking e embeddings (base de tudo)

Antes de entrar na busca híbrida existe um fator muito importante: o **chunking** (tenho vídeos no canal sobre isso e não vou explorar aqui). Você tem um documento — um PDF de 1000 páginas — e, ao colocá-lo num lugar para ser pesquisado, **não coloca o documento inteiro**; isso não seria eficiente. Para ter mais precisão e melhor aproveitamento da LLM, lembrando que a **janela de contexto é limitada** e não infinita: mesmo com 1 milhão de tokens de contexto, existem pesquisas em todos os modelos mostrando que, a partir de um certo volume (o autor cita "120, 150, 200 milhões" — provavelmente mil — de tokens), o desempenho do modelo começa a cair. Por isso é preciso ser cuidadoso com os chunks.

Quebramos o documento inicial em pequenos pedaços; cada pedaço vira contexto, evidência, exemplo. Esse pedaço textual é transformado em **embedding**: uma representação vetorial — um conjunto (grande) de números. Quem não fez álgebra linear na faculdade pode ter alguma dificuldade com o próximo conceito; o autor diz ter feito álgebra linear duas vezes ("gostei tanto que repeti a primeira") e que não é matéria simples, mas é importante para entender o comportamento dessas coisas.

Feita a indexação (documento → embeddings), na hora em que o cliente faz uma pergunta, **a pergunta que será buscada no banco não é o texto corrido**: o agente captura a pergunta e a transforma também em embedding. O que a busca faz é **comparar o embedding da pergunta com os embeddings dos chunks**.

## Busca semântica: similaridade, não igualdade

Pense em Q como a *question*. Você nunca deve esperar o melhor caso — deve esperar sempre o pior. Para construir uma boa solução, a pergunta dificilmente será exatamente igual ao chunk criado; **nunca haverá match exato**. Não se busca igualdade (senão usaríamos um "igual"), busca-se **similaridade**. A conta, no geral, é a **similaridade de cosseno**: compara-se a distância entre o vetor da pergunta e os vetores (chunks) da base.

Aí entra o **top-K**: você nunca retorna um resultado só. Testa, avalia e descobre qual o melhor K para o seu caso; na prática retorna 3, 4, 5, 10 chunks, entrega ao agente, que sintetiza e dá a resposta.

## Demonstração na harness (Rock Pro)

O autor mostra a Rock Pro, uma harness online que é literalmente uma RAG. Faz uma pergunta longa e contextual ("eu tenho uma RAG, isso, aquilo, blá blá"): a pergunta é carregada de sentido, o agente interpreta a entrada, manda ao banco, o banco acha os chunks relevantes e o sistema (com uma etapa generativa — tópico de outro vídeo) devolve a resposta. A busca do sistema é híbrida, mas para uma pergunta cheia de contexto como essa, **uma solução só com busca semântica também funcionaria**.

## O caso que derruba muitas RAGs: a palavra-chave

Existe outro caso, que derruba muitas RAGs: o usuário precisa buscar por uma **palavra-chave**, ou só sabe uma palavra-chave. Nesses casos a palavra-chave fica sempre **muito distante dos chunks**, porque o chunk é criado a partir de uma fatia do documento. Se o usuário pesquisa com uma ou duas palavras, dificilmente o embedding ficará próximo do contexto, e a busca semântica dirá "não achei nada significativo".

Quem controla a **significância** do que é trazido é você: poderia aumentar o "círculo" do top-K para abranger tudo, mas aí traria muitos documentos irrelevantes, poluiria o contexto e diminuiria a eficácia da resposta do agente — resposta pior, mais tokens gastos, mais lentidão. Você precisa achar o círculo do top-K de maneira **ótima**, o que é um trabalho de investigação: implementa, testa, coleta números, vê o que funcionou, itera. É o ciclo do bom engenheiro: aprende, aplica, coloca em produção, coleta feedback, volta. E é por isso que a maioria das RAGs que se vê na internet funciona na demo ("RAG fácil") e **não funciona no mundo real**.

## Como resolver: busca textual (palavra-chave)

Se a busca semântica resolve o significado, a **palavra-chave** resolve a busca textual — e isso é muito simples. Demonstração: o autor digita uma única palavra ("embeddings", provavelmente) e a harness acha mesmo assim. Alguém poderia dizer "sua RAG está ruim, trouxe conteúdo que não tem a ver com RAG (falando de embedding)" — engano, porque a decisão dele ali foi baseada **apenas na palavra-chave**. Pensando que todo o material é um documento com vários chunks, seria impossível a busca ter eficiência só com semântica; ela diria "não tem nada parecido, retorno zero".

O resultado aponta para a "aula 11 — implemente memória semântica". O autor explica o que é: quando você usa o Claude e nota que ele responde algo de sessões anteriores (você abriu uma nova conversa, mas ele sabe que você gosta de futebol), isso é **memória semântica**; para memórias semânticas é preciso entender significado. A palavra-chave sozinha funcionou aqui porque a aula trata de embedding; a harness entregou as lições e a coleção inteira no front end.

Recado à audiência: quem quer ser profissional e ganhar dinheiro com IA ainda confunde *harness engineering* com "usar Claude Code" e *loop engineering* com "fazer o agente perguntar e ter resposta". Esse universo é muito maior; nós criamos essas máquinas, não precisamos ser só usuários — somos protagonistas, não coadjuvantes de uma ferramenta esperando que alguém adicione uma feature.

## Combinando as duas buscas: fusion

Na prática, a busca acontece **em paralelo**: semântica e por palavra-chave. A busca semântica diz "o chunk correto é o chunk C"; a busca textual também diz que é o C, mas dá prioridade ao chunk A (exemplo dos gráficos). Depois vem uma etapa chamada **fusion**, responsável por **desempatar**: há duas opiniões diferentes, o fusion consolida o que recebe de entrada e **rankeia** o resultado. É simples.

E como se faz o fusion — é tecnologia alienígena? Depende da OpenAI? Não: **é um critério que você define**. Dependendo da natureza do dado você pode dar **mais peso às palavras-chave**; dependendo do dado, mais peso à busca semântica. Isso influencia o resultado da RAG quando o agente for responder.

## Como descobrir os pesos: teste e medição

"Roland, como eu descubro isso?" — **com teste**. Meça cada passo, principalmente o **retrieval** (o R da RAG): dei mais preferência à busca textual; agora à semântica; o resultado melhorou? Melhorou / não melhorou; se não melhorou, não fica com ele. É um "jogo da verdade": não existe enganação quando se faz teste. **IA não é adivinhação, IA é trabalho.** No fim você tem uma boa RAG não porque acha que ela é boa, mas porque tem testes, controle de todos os processos e buscas complementares — porque dados vêm em formas e naturezas diferentes e as pessoas usando sistemas reais se comportam de maneiras muito engraçadas (o autor diz estar de olho nos logs para ver como a audiência usa a harness, que ainda vai evoluir — "começamos timidamente como um Cursor, na primeira versão").

## Fechamento: retrieval é uma etapa; agente pode refazer a busca

A busca é **uma etapa** da RAG: R (recuperar), o agente recebe, e o agente gera. Num agente que faz RAG, se ele não encontrar o dado desejado, pode **refazer a pergunta**, voltar à busca e repetir quantas vezes você determinar. Boa prática: **não deixar o agente solto demais** chamando a ferramenta muitas vezes, porque pode entrar em loop e se perder. "Não confie no modelo, confie na sua habilidade." Abraço e até a próxima.
