# C pode ser uma das linguagens mais importantes do futuro? (quadro "Bora tomar café")

> **Origem:** transcrição de vídeo em português (YouTube) — corte do quadro *"Bora tomar café"*, que a apresentadora diz acontecer toda sexta-feira de manhã no canal principal de Fernanda Kipper (a transcrição grafa "Fernanda Keeper"; "8:27 da manhã" provavelmente é o horário "8h27"). Colada pelo usuário em 2026-10-02. Já estava em português (sem tradução). Texto limpo, pontuado e dividido em seções; o conteúdo foi preservado. Foram omitidos apenas o pedido de like/inscrição no canal de cortes e a despedida.
>
> **Formato:** o vídeo lê em voz alta um artigo/post do Twitter (autor **não identificado**) e comenta no meio. Aqui, o trecho em citação (`>`) é o artigo lido; o texto sem citação é o comentário da apresentadora (identidade não informada na transcrição).
>
> **Correções de reconhecimento de fala (por contexto):** "legislibilidade" → *legibilidade*; "atual do custo" → *arcar com o custo*; "Cláudio GPT Jemen" → *Claude, GPT, Gemini*; "Kilby" → *KB (kilobytes)*; "16 GB de RAM" (microcontroladores) → provavelmente *16 KB*, pois o contexto são microcontroladores; "gn" → *GCC (compilador)*; "supercutadores" → *supercomputadores*; "midware" → *middleware*; "streings e butidas" → *strings e [tipos] embutidos* (trecho incerto: "sem strings embutidas" no original do artigo); "structo/struct" mantido como *struct*; "Fazuellison" → nome de usuário de comentarista, grafia incerta; "Pedro" → outro comentarista. **Nota sobre a anedota da apresentadora:** ela fala em "integer = 8 bits e caractere = 4 bits" para exemplificar aritmética de ponteiros; os tamanhos citados não correspondem aos usuais em C (em geral `char` = 1 byte, `int` = 4 bytes) — preservado como dito, é ilustração oral.

## Abertura — a tese do artigo

> Uma das linguagens de programação mais importantes do futuro pode ser o **C**. Não o C++, não o Python, não o Rust. Na era do software gerado por IA, não precisamos mais arcar com o custo de tempo de execução de linguagens criadas para a legibilidade humana.

**Comentário:** isso é interessante, e é fato quanto ao tempo de execução. Comparando C com Python ou JavaScript: Python e JavaScript são muito mais simples para a gente escrever, aprender e ler — a sintaxe é bem mais amigável. Mas, se comparar tempo de execução, o C é muito melhor, muito mais eficiente.

> Quando a IA escreve o código, o C volta a ser o rei. Eis o porquê.
>
> Primeiro, entenda por que abandonamos o C. O C é rápido, é eficiente e oferece controle total sobre o hardware. Produz os binários menores e mais rápidos possíveis. **Mas o C é difícil para os humanos.**

## Digressão — a experiência da apresentadora com C na faculdade

Eu me lembro de quando fiz algoritmos e estruturas de dados na faculdade: a gente tinha que fazer os algoritmos em C. Na época havia o Stack Overflow e, às vezes, repositórios open source para se inspirar, mas a gente tinha que criar a `struct` para armazenar dados e ler esses dados com **manipulação de ponteiros**.

Exemplo: tenho uma `struct` em que salvei um caractere e um booleano. Aquilo, na verdade, era uma referência para um ponteiro num endereço de memória de tipo `void`. Se eu quisesse ler o booleano de dentro da `struct`, bastaria acessar a propriedade; mas, por não ter tipo, eu tinha que mover o ponteiro manualmente: se há um inteiro, um caractere e depois o booleano, e sei o tamanho de cada um, tenho que andar com o ponteiro (no exemplo falado, "12 bits") para o lado até chegar ao endereço de memória onde está o booleano.

No começo, meu Deus, a turma toda não entendia o que estava fazendo. Depois de algumas aulas a gente pegou o jeito e era C "na veia". Foram três matérias de algoritmos e estruturas de dados; na primeira teve essa dificuldade, depois a gente pegou e, nas seguintes, escrevia "umas coisas cabulosas" em C. Isso era legal da faculdade — é uma coisa que eu não teria feito se não tivesse cursado; no mercado de trabalho eu nunca teria feito. Me fez aprender muito sobre como uma linguagem de programação funciona.

Tive uma aula de **conceitos de linguagem de programação**, uma das melhores da ciência da computação, muito elucidativa. A gente entende como uma linguagem é escrita — escrevemos partes de uma linguagem de programação. Você fica "agora eu sei o que está acontecendo desde a placa-mãe até chegar na CPU, passar pelos barramentos, carregar o sistema operacional em memória, o sistema operacional puxar o meu código para rodar". Depois vêm **compiladores e interpretadores**, um nível um pouco mais alto: no JavaScript declaramos `const nomes = []` (ou, em Java, uma `List`) — como isso cria um array, como aloca espaço na memória, como, ao acessar a posição zero, ele me retorna aquilo. Tudo isso a gente entende. Foi uma das melhores matérias da universidade.

**Comentário de seguidor (Fazuellison):** "Criar um compilador do zero na faculdade foi um marco para mim. Eu nunca teria passado por esse sofrimento estudando sozinho." Concordo: quem entra na área sem saber que isso existe nem sabe que tem que estudar. Como meu bacharelado foi em ciência da computação, aprendi como a computação foi concebida desde o zero: a base matemática (definições, lógica de predicados etc.) combinada com a evolução do hardware, cada semestre colocando mais um bloco de conhecimento, até a camada de abstração de hoje. Infelizmente não tive profundidade em inteligência artificial (que quero aprofundar no mestrado) — só uma pincelada, pois a ciência da computação foca na computação clássica. Mas você entende todas as camadinhas até chegar a como os sistemas modernos são construídos. Muito legal, mas **tem que gostar**.

## Por que o C é difícil para humanos (volta ao artigo)

> Gerenciamento manual de memória. Aritmética de ponteiros. Estouro de buffer. Falhas de segmentação. Sem strings [e tipos] embutidos, sem coleta de lixo, sem mecanismos de segurança.

**Comentário:** aritmética de ponteiros é o que eu estava descrevendo: mexer o ponteiro manualmente com base no tamanho dos dados, literalmente quantos bits/bytes andar para passar por um dado e chegar no outro.

## Linguagens de alto nível trocaram desempenho por produtividade

> Então inventamos linguagens de alto nível: Python, Java, JavaScript, Ruby, Go, Rust. Cada uma trocou desempenho por produtividade. Tornaram o código mais fácil de escrever, ler e manter para humanos. Essa troca fazia sentido quando eram os humanos que escreviam o código.

## E se a IA escreve o código?

> Agora faça uma pergunta diferente: e se os humanos não estiverem mais escrevendo a maior parte do código? A geração de código por IA em 2026 não é brincadeira. Claude, GPT, Gemini estão gerando código de nível de produção em milhões de projetos todos os dias. E a IA não tem as mesmas limitações que os programadores humanos:
>
> - A IA não se esquece de liberar memória (se você disser para ela não fazer isso).
> - A IA não perde o controle da aritmética de ponteiros.
> - A IA não se confunde com sintaxe de baixo nível.
> - A IA não se cansa, não se entedia nem se frustra com código repetitivo.
>
> O motivo pelo qual criamos abstrações sobre o C foi para proteger o cérebro humano da complexidade. A IA não precisa dessa proteção.

**Comentário (ressalva):** essa afirmação é forte demais. "Esquecer" é um conceito humano, mas aquilo pode ficar perdido na janela de contexto: dependendo do tamanho da janela e da quantidade de coisas que ela está fazendo, uma instrução pode se perder e a IA não fazer o que você pediu. Não está no nível de garantir 100%. (E sobre "o cara acabou com a gente também": a apresentadora brinca com o tom do texto.)

## A compensação que muda tudo

> Cada camada de abstração tem um custo. Cada linguagem de alto nível adiciona sobrecarga. Python é 10 a 100 vezes mais lento que o C para a maioria das tarefas. O JavaScript tem um mecanismo de execução que consome memória. O Java tem a JVM. O Go tem o coletor de lixo. Até mesmo o Rust, queridinho da programação, adiciona complexidade em tempo de compilação em troca de garantias de segurança.
>
> Essas compensações valiam a pena quando os humanos precisavam delas. Mas, quando a IA está gerando o código, você está pagando o preço do desempenho das abstrações amigáveis aos humanos sem ter um humano escrevendo código. **Você está pagando o aluguel por um prédio onde ninguém está trabalhando.**

**Comentário (contraponto):** eu acho que não é que não vá ter mais nenhuma validação. Quem sabe a gente possa criar **uma nova linguagem de programação pensada para a IA**, com validações pensadas para os erros que a IA comete. As linguagens que temos foram pensadas para os erros que *a gente* cometia — erros de tipo, de validação, de estouro de memória. Quem sabe os erros da IA sejam diferentes, e aí criamos uma linguagem com validações diferentes.

## O que o C oferece quando humanos não são o gargalo

> - **Sobrecarga de tempo de execução zero.** Sem coletor de lixo, sem interpretador, sem máquina virtual. Seu código é compilado diretamente para instruções de máquina; nada entre a sua lógica e o hardware.
> - **Tamanhos de binário mínimos.** Um programa em C compila para KB. Um equivalente em Python precisa de um runtime de 50 MB. Um aplicativo Java precisa de uma JVM. O servidor Node precisa do mecanismo V8 completo.

**Comentário (crítica à comparação):** que tipo de comparação é essa? Eu sei que JavaScript e Node são mais lentos que C, mas "o Node precisa do V8 completo" — para compilar C você também precisa do GCC instalado; não é que o código "sai compilado num piscar de olhos". Só achei engraçada a forma de falar; ele está usando muitas frases de efeito.

> - **Desempenho máximo.** O C roda na velocidade do hardware. Todo o resto roda na velocidade da camada de abstração.
> - **Controle total do hardware.** O C se comunica diretamente com endereços de memória, registradores e periféricos — sem wrapper, sem API, sem middleware.
> - **Portabilidade universal.** O C roda em tudo: microcontroladores com 16 KB de RAM, supercomputadores, robôs exploradores de Marte, satélites, dispositivos médicos… torradeiras, sanduicheiras, chaleiras, micro-ondas, televisões.

**Comentário:** ele tem um ponto — o C realmente é mais eficiente e tem melhor desempenho —, mas está meio emocionado. (Sobre uma linguagem para IA: "poderia ser um Lisp?" — a apresentadora diz não ter argumentos nem lembrar direito dos detalhes do Lisp.) O comentarista Pedro observa: "esses artigos do Twitter às vezes têm coisas úteis, às vezes é só *bait*" — a apresentadora concorda: tem coisas relevantes, mas nem tudo.
