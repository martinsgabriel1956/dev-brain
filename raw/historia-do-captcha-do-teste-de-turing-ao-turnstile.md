# A História do CAPTCHA: do Teste de Turing ao Turnstile

Transcrição de vídeo em PT-BR (canal e autor desconhecidos) sobre a história e a morte gradual do CAPTCHA. Já em português — sem tradução. Título original desconhecido; título descritivo derivado do conteúdo.

> **Nota de limpeza:** a transcrição automática corrompeu vários termos, corrigidos por contexto: "capt/captcha/capture/captivas" → CAPTCHA; "Monyor" → Moni Naor; "completely automated publicing test to" → *Completely Automated Public Turing test to tell Computers and Humans Apart*; "GIMP" → Gimpy (provável); "recaption/recapion" → reCAPTCHA; "No Capture" → No CAPTCHA reCAPTCHA; "Yolo/iolo" → YOLO; "cookie de rastreamento" mantido; "um unicip" → um único IP; "63.000 1 cookies" → número corrompido, mantido como "63.000 (valor incerto)"; "Cloud Flir" → Cloudflare; "tanto style" → Turnstile; "NS" → nonce; "to capture" → 2Captcha (provável); "fun capture" → FunCaptcha (Arkose Labs); "Proof of Space" → PoSpace; "recaptura V3" → reCAPTCHA v3. Pontuação e pausas de fala foram reorganizadas em parágrafos; o conteúdo não foi alterado.

## Abertura: como garantir que há um humano do outro lado?

Como garantir que do outro lado da tela há um ser humano e não um robô? A resposta óbvia é o CAPTCHA — mas o conceito de CAPTCHA que temos **já não existe mais** e, pior, ele simplesmente não consegue diferenciar humano de máquina até hoje. Além disso, o CAPTCHA inicial era uma "máquina de trabalho humano de graça", e os criadores sabiam que ele tinha prazo de validade. O vídeo conta a história desde o começo.

## 1996: a proposta teórica (Moni Naor)

Em 1996, o pesquisador Moni Naor escreveu um manuscrito teórico propondo usar um **teste de Turing** para verificar se quem está do outro lado de uma consulta web é humano ou máquina.

Teste de Turing: você conversa às cegas com alguém ou algo sem ver quem está do outro lado; se, depois da conversa, não consegue dizer se falou com uma pessoa ou um programa, o programa passa no teste — um "jogo de imitação". A ideia do CAPTCHA é o contrário: em vez de avaliar se a máquina é boa o bastante, avaliar se quem está do outro lado é **humano o bastante**.

Naor definiu alguns tipos de problema: reconhecimento de gênero, expressão facial, encontrar parte do corpo humano e até decidir se uma imagem tem ou não nudez.

## 1997–2000: texto distorcido e o nome "CAPTCHA"

Um ano depois, duas equipes diferentes, sem saber uma da outra, tiveram praticamente a mesma ideia: gerar uma imagem de **texto distorcido** difícil para o OCR da época ler. OCR (reconhecimento óptico de caracteres) é o software que identifica texto a partir de uma imagem — e isso era bem difícil na época.

Nos anos 2000 o teste foi batizado oficialmente como *Completely Automated Public Turing test to tell Computers and Humans Apart* (CAPTCHA). Dois dos primeiros sites famosos a usar foram **PayPal e Yahoo** (com Gimpy). Até então não havia formalização: cada um implementava como achava melhor.

## 2003: a formalização

Em 2003, um dos papers mais famosos da computação — *CAPTCHA: Using Hard AI Problems for Security* — formalizou que um CAPTCHA precisa de duas partes:

1. um **gerador**, que cria o desafio;
2. um **testador**, que confere a resposta **sem precisar saber a solução**.

Para ser um bom CAPTCHA, três pré-requisitos:

1. gerador e testador são fáceis de rodar automaticamente;
2. um humano de verdade passa com probabilidade alta;
3. **nenhum programa conhecido passa com probabilidade alta, mesmo sabendo o algoritmo usado para gerar o CAPTCHA**.

Para o terceiro requisito ser verdadeiro, o problema por trás do CAPTCHA tem que ser **um problema de IA em aberto**. Logo: o CAPTCHA só é seguro enquanto há um problema de IA em aberto, e a pesquisa de IA não para — é questão de tempo até algum problema ser resolvido. **Todo CAPTCHA, pela própria definição, já nasce com prazo de validade.**

## 2007: reCAPTCHA — trabalho humano aproveitado

Na época, cerca de **200 milhões de CAPTCHAs eram resolvidos por dia**, cada um levando ~10 segundos: mais de **500.000 horas** de cérebro humano jogadas fora todos os dias. Ao mesmo tempo, o **New York Times** tentava digitalizar seu arquivo (mais de 13 milhões de artigos desde 1850) e o OCR não conseguia ler parte dele.

A ideia: em vez de gerar texto aleatório e descartar, usar as palavras que o OCR não conseguia ler. Em 2007 foi criado o **reCAPTCHA**. O sistema mostrava **duas palavras**: uma que ele já sabia a resposta (**palavra de controle**) e outra realmente desconhecida.

Como saber se você acertou a palavra desconhecida, se nem o sistema sabe a resposta? Não sabe: só confere a palavra de controle. Se você acertou, assume-se que também acertou a outra, e o que você digitou é salvo como um **voto**. Com mais pessoas resolvendo, as palavras desconhecidas acumulam votos até haver uma grande maioria concordando na palavra certa.

## 2009–2014: o Google compra e mata o CAPTCHA de texto

Em 2009 o **Google comprou o reCAPTCHA**, ganhando mais fontes de imagens difíceis. Em 2014, o CAPTCHA de texto foi oficialmente morto — e quem matou foi o próprio Google. Internamente, eles tinham problema para ler texto em fotos do Google Maps; contrataram pessoas só para digitalizar e treinar uma IA com as respostas. Quando ficou boa o bastante, testaram-na contra um CAPTCHA de texto clássico por curiosidade: ela resolvia quase tudo — **99% de acerto**, até na variante mais difícil.

## 2014: No CAPTCHA reCAPTCHA ("Não sou um robô")

Na mesma época anunciaram o substituto: o checkbox "não sou um robô". Antes, todo CAPTCHA pedia para resolver algo; esse **só observa o comportamento**, e se você não parece humano, aí sim recebe um desafio de imagem.

O que observam nunca foi revelado oficialmente, mas pesquisadores fizeram engenharia reversa e confirmaram o uso da **idade do cookie de rastreamento** e do **fingerprint do navegador**. Muita gente acreditava (e ainda acredita) que analisavam o **movimento do mouse** — mas os pesquisadores testaram e **não viram diferença nenhuma no resultado**.

Claro que também foi quebrado: em 2016 descobriram que **um único IP conseguia gerar até ~63.000 (valor incerto) cookies novos por dia**, e que um cookie maduro (**mais de 9 dias de idade**) garantia passar no CAPTCHA. Mesmo quando aparecia o desafio de imagem, um grupo de pesquisadores usou **YOLO** (rede neural de detecção de objetos) e teve praticamente 100% de acerto.

## 2018: reCAPTCHA v3

O v3 é só um selinho no canto da página; roda em segundo plano o tempo todo e o usuário não faz nada — só precisa parecer humano. No final calcula um **score de 0 a 1** de confiança de que você é humano, e **o programador decide o que fazer** com o número. Exemplo do vídeo: score < 0,2 bloqueia o formulário; < 0,5 pede confirmação por e-mail; acima disso aceita. O fluxo do usuário nunca é interrompido. Até hoje esse CAPTCHA é o mais usado.

**Crítica:** tecnicamente o reCAPTCHA v3 **não é um CAPTCHA de verdade**. O requisito de 2003 era que nenhum programa passasse *mesmo conhecendo o algoritmo*; o v3 faz o oposto — sua segurança está baseada em **obscuridade**: ninguém fora do Google sabe o algoritmo. "Isso nem devia se chamar CAPTCHA": a sigla significa teste de Turing público e automatizado, mas não há mais teste, é só um score de risco.

## Atualidade: a base teórica acabou

Nenhum sistema atual pede que você resolva um problema de IA em aberto (todos já foram resolvidos). A definição formal de 2003 não se aplica a quase nenhum CAPTCHA hoje — "alguém tem que atualizar isso".

### Cloudflare Turnstile (2022)

Roda pequenos desafios JS **não interativos**. Os dois principais:

**Proof of Work.** O servidor manda um desafio (um texto aleatório) e o navegador tem que achar um número (o **nonce**) que, colado ao texto e passado por uma função hash, produz um resultado que **começa com muitos zeros**. Não há atalho matemático: só força bruta — talvez 50.000 a 2 milhões de tentativas, conforme a dificuldade pedida. É o mesmo princípio da mineração de Bitcoin, em escala muito menor. Para o usuário é imperceptível; para um bot fazendo uma ação 100.000 vezes ao mesmo tempo, cada tentativa paga o mesmo custo — o PC não aguentaria.

**Proof of Space.** Foca em **memória**, não processamento. O servidor pede ao navegador que construa uma **tabela gigante** de valores calculados numa sequência específica e a guarde na memória; depois pede o valor de uma **posição aleatória**. Quem guardou a tabela responde na hora; quem tentou economizar memória e recalcular na hora demora muito mais, e o sistema detecta. Importa porque **GPUs são baratas para paralelizar cálculo** (podendo quebrar o proof of work), mas **memória RAM não escala barato** da mesma forma.

Isso realmente prova que sou humano? Não. O teste garante outra coisa: que existe **um navegador de verdade rodando JS**, e não um simples script HTTP fingindo ser usuário.

### FunCaptcha (Roblox / Arkose Labs)

O CAPTCHA "mais insuportável e estranho de todos": renderiza um **modelo 3D** (animal, objeto) de cabeça para baixo e pede que o usuário use setinhas até deixá-lo na posição certa, ou mostra uma grade de dados e pede para selecionar algo. São **mais de 1.200 variações** (modelo, fundo, regra) para dificultar treinar um classificador genérico. A verificação também é mais complexa: junto com a resposta do puzzle, a página carrega um **script ofuscado** que calcula um parâmetro de resposta, e junto com a **telemetria** o servidor cruza tudo — mesmo acertando o puzzle, ainda verifica se o ambiente bate com um navegador real. De novo, muita **segurança por obscuridade**.

## Corrida de gato e rato

Desde os anos 2000: de um lado, pessoas treinando IA para passar por humano; do outro, pessoas treinando IA para pegar quem finge ser humano. Mas as pessoas perceberam que não vale a pena brigar com uma IA de detecção se dá para **comprar o humano em que ela já confia**. Desde ~2007 já existia um mercado inteiro pagando gente para resolver CAPTCHA industrialmente; hoje é a mesma lógica via **API** (ex.: 2Captcha): o script manda o desafio, do outro lado uma rede de centenas de pessoas resolve na mão e devolve o **token de resposta**.

Conclusão: cada geração é a mesma coisa — alguém cria um teste, alguém o resolve e o deixa obsoleto, e o ciclo continua "até não dar mais".
