# Google está perdendo a corrida da IA? Memory Caching, Gemini 3.8 Live e o negócio por trás

> Transcrição de vídeo em PT-BR (autor/canal não identificado), colada pelo usuário em 2026-10-09. Já estava em português; sem tradução. Limpeza: pontuação, parágrafos e correção de erros de ASR (gemnight→Gemini, alfa alphabet→Alphabet, rns→RNNs, speeit to speit→speech-to-speech, high globe→Higlobe, Antigravity mantido). Termos incertos marcados com [?].

## Abertura: o Google vai perder a corrida?

Andam falando por aí, de boca em boca, que o Google não vai ganhar a corrida da inteligência artificial. Será que isso é justo? Será que a gente está sendo justo com o Google? Se você for ver as notícias e os artigos deles, no dia 15 eles lançaram o **Gemini 3.8 Live** enquanto todo mundo só falava do **Jev**. Sim, o Google tem um péssimo timing de divulgar novas coisas. Mas eles já tinham divulgado o **Gemini 3.8 Flash** [?: "cyber" no áudio] e, antes, o **3.7 Flash**, um dos modelos mais baratos que a gente vê no mercado. O 3.8 custa **US$ 0,75 por milhão de tokens** [valor dito como "0.75 centavos"; unidade ambígua].

Você pode dizer: "isso não me serve, eu nunca largaria meu Claude ou meu Codex por um Gemini". Só que o que você está esquecendo é que **o Google sabe fazer negócios**. Eles colocam no mercado coisas mais baratas, e se é mais barato para nós, imagine a eficiência para eles. Só que adicionam isso **dentro de produtos**. A gente fala muito de eficiência, mas para ter eficiência em IA é preciso ter resultado para o cliente/usuário final. Então o ponto do Google é outro: **fazer dinheiro e inovação**.

## Dinheiro: Alphabet e Google Cloud

No relatório de resultados do primeiro trimestre de 2026 da Alphabet, e no resumo sobre os produtos de cloud do Google no Q2 de 2026, aparecem números interessantes:

- Receita de **US$ 24,8 bilhões** na cloud, crescimento de **82% ano a ano**.
- **Backlog** subindo para cerca de **US$ 514 bilhões** [o autor diz "se eu não me engano"] em receita operacional na nuvem.
- O que puxa isso é o **GCP**: infraestrutura para IA e soluções com IA para grandes empresas, o núcleo dessas soluções.

Também se esquece que o Google tem suas próprias unidades de processamento, os **TPUs (Tensor Processing Units)**. É uma das poucas empresas que compete, ou melhor, **complementa**, a Nvidia: está na **cloud**, no **chip** e nas **soluções**. E não se enganem: onde a gente está hoje, o Sam Altman com o ChatGPT, é por causa de um paper que saiu de dentro do Google ("Attention Is All You Need"). E eles não param de inovar.

## Inovação: o paper de Memory Caching

Este ano o Google liberou um paper sobre **memória em RNNs**: como ter uma RNN com memória crescente para não ficar se perdendo.

- **RNN** = Recurrent Neural Network: processamento de informação em sequência, em que o contexto anterior importa para o próximo passo. Depois de bilhões de informações, ela começa a perder o início.
- Resumo pedido ao Gemini "como se eu tivesse 5 anos": a **RNN é como uma formiga** — lê a história palavra por palavra, devagar; quando chega ao fim, já esqueceu o começo. O **Transformer é como um super-homem** — olha a página inteira e lê todas as palavras ao mesmo tempo; liga início e fim num piscar de olhos. "Imagina o super poder da formiga se ela conseguisse lembrar do início da conversa."

(Dica do autor: se hidrate, "senão a tua RNN não funciona".)

> **[Publicidade removida do núcleo técnico]** Segmento patrocinado pela **Higlobe** (conta para receber em euro/dólar sem manutenção, transferência sem custo de empresa americana, compra de dólar com custo igual ao de saque local de 0,2% sem IOF, saques gratuitos por 3 meses, saldo rendendo 3% a.a., cartão Visa Signature sem custo nos EUA e 1% fora, cupom do apresentador). Preservado só como registro; sem valor técnico.

### Como o Memory Caching funciona

Em modelos recorrentes há um **espaço de memória fixo**, que vira o gargalo. A solução **não** é inventar outro "Attention Is All You Need": é basicamente **cachear checkpoints do estado da memória**. Num documento longo, a RNN teria um estado que sobrescreve lá no fim com um resumo; o Transformer guarda tudo, lembra de tudo, e é bem mais caro. O paper mostra como obter uma **RNN com memory caching**.

Resultados citados (experimento de **1,3 bilhão de parâmetros**, média em benchmarks de *language modeling* e *common sense reasoning*):

- Transformer: **53,19**
- Titans com [variante de Memory Caching, "GRM" no áudio]: **58,33**
- Até o "DLA" [?: provável variante tipo Gated DeltaNet/DLA] pontuou acima do Transformer.

Ressalva do autor: isso **não significa** que a RNN vai matar o Transformer. Todos os LLMs de hoje (ChatGPT, Claude, Gemini) têm Transformers por trás, que fazem a *atenção* a um contexto acontecer: pegar um documento inteiro e entender do que se trata, para prever o próximo token. A "formiga" com memory cache pode preencher o gap que a RNN não consegue e o Transformer consegue: o teste da **agulha no palheiro** (achar uma informação em qualquer posição de um documento gigante). Uma RNN com memória cacheada poderia melhorar isso e até superar o Transformer.

Ponto central: o Google **está muito atrás nos modelos que a gente usa**, mas parece estar **à frente nos estudos sobre eficiência** — junto com universidades americanas (Cornell, USC), dentro do **Google Research**.

## Modelos: Gemini 3.8 Live (speech-to-speech)

O Google lançou o **Gemini 3.8 Live** e o **3.8 Live Extended Thinking**, que permitem **speech-to-speech** (como ligar para o ChatGPT por voz; também via API), com experiência mais fluida.

- No **Speech-to-Speech Index**, o *Gemini 3.8 Live Extended Thinking High* superou o **GPT Live 1 [Astra?]** (novo modelo de voz da OpenAI) em *effort medium* e também o **Grok Voice**.
- Por que importa: atendimento por telefone com bot ainda tem **minutagem cara**. O Grok lançou isso dentro do Grok Bot (com Cursor/SpaceX), com plataforma de dev para criar API keys e adicionar números de telefone, mas "o preço é muito caro".
- Previsão: com a evolução, **no ano que vem** haverá muito mais IAs ligando para você; no Brasil, "vai ser um inferno" (telemarketing barato em escala, mais golpes), mas também espaço para inovar.
- **Custo comparado**: GPT Live 1 ≈ **US$ 0,05/min ≈ US$ 3/h**; Gemini 3.8 Live ≈ **US$ 0,84/h** → **mais de 3× mais barato**, com números melhores nos benchmarks.

## Conclusão

O Google está evoluindo, talvez não nas coisas que a gente quer. Para o autor, uma das principais causas de devs e da bolha do Twitter não enxergarem a evolução do Google (financeira no GCP; modelos de live speech-to-speech; pesquisa) é que o **Antigravity é "um lixo"**: produto de dev ruim, experiência horrível — feedback para quem trabalha nessas ferramentas no Google: investir mais nisso pode mudar a percepção. Como *shareholder/investidor*, o caminho de fazer dinheiro no corporativo (IA dentro das soluções e IA como infraestrutura na nuvem) segue ótimo. "Não esquece de se hidratar."
