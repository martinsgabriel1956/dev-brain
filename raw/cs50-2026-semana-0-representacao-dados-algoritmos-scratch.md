# CS50 2026 — Semana 0: IA, Representação de Dados, Algoritmos e Scratch

> Transcrição traduzida (inglês → português) da aula de abertura do CS50 (Harvard University — "Introduction to the Intellectual Enterprises of Computer Science and the Art of Programming"), ministrada por David Malan. Fonte: gravação em vídeo/áudio da aula, transcrita automaticamente e traduzida para este arquivo.

## Abertura: o elefante na sala é a IA

Este é o CS50, o curso introdutório de Harvard sobre os empreendimentos intelectuais da ciência da computação e a arte da programação. Antes de qualquer outra coisa, vale endereçar o "elefante na sala": a inteligência artificial, que parece estar em todo lugar nos últimos anos e que, de fato, está mudando a programação — e vai continuar mudando cada vez mais.

Isso é, na visão do professor, uma coisa boa. Usar IA em qualquer uma de suas formas permite pedir ao computador ajuda para resolver um problema, encontrar um bug ou erro no código e, cada vez mais, pedir para a IA implementar novas funcionalidades. Isso é enorme porque, há décadas, humanos programando sozinhos sempre foram o gargalo: há um número finito de horas no dia, um número finito de pessoas em um time ou empresa, e sempre existem mais bugs para resolver e mais funcionalidades para implementar do que tempo disponível.

Ainda assim, é preciso entender os fundamentos. Um curso como o CS50 nunca foi, no fundo, sobre "ensinar a programar" — isso é só um efeito colateral. O objetivo real é ensinar a **pensar**: como pegar uma entrada (input) e produzir a saída (output) correta, e como dominar essas e outras ferramentas. Ao final do semestre, além de conhecer linguagens como Scratch, C, Python, SQL, HTML, CSS e JavaScript, o aluno será capaz de se ensinar coisas novas e, cada vez mais, dizer ao computador o que quer que ele faça — mas continuando no banco do motorista, como piloto, como maestro.

É como as calculadoras: mesmo depois delas existirem, continua valendo a pena saber somar e subtrair na mão. O professor lembra de suas próprias aulas de cálculo na faculdade, aprendendo dezenas de técnicas diferentes para derivadas e integrais — depois da sexta técnica, a sensação era "já entendi a ideia, preciso mesmo saber *todas* essas formas?". O mesmo vale para IA e código: dá para dominar as ideias fundamentais e, depois, apoiar-se em um copiloto/assistente para resolver os mesmos problemas.

## Demo: construindo um chatbot próprio em ~10 linhas de Python

Para dar um gostinho do que será possível fazer ao longo do curso, o professor abre o **Visual Studio Code (VS Code)** — um editor de texto popular, open source, usado por profissionais na indústria (comparável a um Notepad/TextEdit, mas sem formatação de texto como negrito). É a versão do CS50 desse ambiente (mais detalhes na semana seguinte).

Na parte de baixo da tela existe um **terminal**, onde é possível digitar comandos que dizem ao computador o que fazer. O objetivo é escrever o próprio chatbot — não o ChatGPT, Gemini ou Claude prontos, mas um programa próprio construído em cima da API (Application Programming Interface) de uma empresa terceira, a OpenAI.

Código digitado ao vivo, em Python, em um arquivo chamado `chat.py`:

```python
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    input="Em uma frase, o que é o CS50?",
    model="gpt-5",
)

print(response.output_text)
```

Executando `python chat.py` no terminal, a resposta impressa é algo como: *"CS50 é o curso introdutório de ciência da computação de Harvard University, os empreendimentos intelectuais da ciência da computação e a arte da programação, cobrindo resolução de problemas, algoritmos, estruturas de dados e mais, usando linguagens como C, Python e SQL."*

### Tornando o programa dinâmico: input do usuário

O programa acima está "hard-coded" — responde sempre à mesma pergunta. Para tornar dinâmico, adiciona-se uma linha pedindo o prompt ao usuário:

```python
prompt = input("Prompt: ")

response = client.responses.create(
    input=prompt,
    model="gpt-5",
)
```

`=` aqui significa "armazenar essa resposta em uma variável chamada `prompt`" — exatamente como X, Y ou Z na matemática. Agora, ao rodar o programa, ele pergunta o que o usuário quer saber, e a resposta muda conforme a pergunta digitada ("em uma frase, o que é o CS50?", "em uma palavra, o que é o CS50?", "em uma palavra, o que é melhor, Harvard ou Stanford?" — a esta última a IA responde algo como "depende", sem se comprometer).

### System prompt vs. user prompt

Em vez de repetir manualmente "em uma frase" ou "em uma palavra" a cada pergunta, é possível instruir o modelo a *sempre* se comportar de determinado jeito — introduzindo o conceito de **system prompt**, em contraste com o **user prompt** (o que o usuário digitou):

```python
user_prompt = input("Prompt: ")
system_prompt = "Limite sua resposta a uma frase."

response = client.responses.create(
    input=user_prompt,
    instructions=system_prompt,
    model="gpt-5",
)
```

Agora o humano não precisa mais lembrar de pedir "em uma frase" toda vez — isso está fixado nas instruções do sistema. E, por brincadeira, o `system_prompt` pode virar "Finja que você é um gato" — e a resposta a "o que é CS50?" vem com um "miau" no final, prova de que o comportamento pode ser coagido via essas ~10 linhas de código (nem todas usadas, já que algumas ficam em branco).

### O pato de borracha do CS50

Em programação, existe a prática de manter um pato de borracha (ou qualquer objeto inanimado fofo) na mesa: quando travado em um bug e sem ninguém mais experiente por perto, verbalizar o problema para o pato — só o processo de organizar os pensamentos para "explicar" a outra entidade frequentemente faz a lâmpada acender e revela o erro de lógica.

O CS50, inspirado nisso, oferece um pato de borracha **virtual**: **CS50.ai** (também embutido em **CS50.dev**), a IA do curso, disponível para os alunos usarem ao longo do semestre. Pelo regulamento do curso, **não** é permitido usar outras ferramentas de IA (Claude, Gemini, ChatGPT, etc.) fora do próprio CS50.ai — mas é reasonable e muito incentivado recorrer tanto a humanos (professor, monitores, colegas) quanto à IA própria do curso. O pato virtual foi desenhado para se comportar como um bom tutor humano: conhece CS, sabe conduzir o aluno até a solução, idealmente sem simplesmente entregá-la.

## O que é ciência da computação

Ciência da computação é o estudo da **informação**: como representá-la, como processá-la. O termo relacionado é **pensamento computacional** — a aplicação de ideias da ciência da computação a problemas do mundo real em geral. No fundo, ciência da computação é sobre **resolução de problemas**; computadores e programação são só ferramentas e metodologias para isso.

Um problema pode ser reduzido a: uma **entrada** (input, o problema a resolver), uma **saída** (output, a meta/solução) e, no meio, uma **caixa-preta** — o "molho secreto" que leva de um ao outro.

## Representação de informação: do unário ao binário

Para computadores (Macs, PCs, celulares) processarem qualquer coisa, é preciso um sistema padronizado de representação. No fim das contas, todo computador usa apenas **zeros e uns** — esse é o alfabeto inteiro.

- **Unário (base 1):** contar usando dígitos únicos, como dedos de uma mão. Uma mão humana conta até 5 (ou até 10 com as duas mãos), depois precisa "de mais hardware" (outra mão, os dedos dos pés).
- **Binário (base 2):** em vez de contar quantos dedos estão levantados, importa o **padrão** — quais dedos, e o peso (valor) atribuído a cada posição. Com convenção adequada (dedo 1 = valor 1, dedo 2 = valor 2, dedo 3 = valor 4, dedo 4 = valor 8, dedo 5 = valor 16), uma única mão consegue contar até **31** (32 combinações possíveis, incluindo o zero).

**Bit** (binary digit) é o termo para um único dígito binário: 0 ou 1. É comumente representado como uma lâmpada apagada (0) ou acesa (1) — ou, em um computador de verdade, como um **transistor** que retém (1) ou dissipa (0) um pouco de eletricidade. A vantagem do binário é que eletricidade é simplesmente "fluindo" ou "não fluindo" — não é preciso distinguir múltiplos níveis de voltagem, só presença/ausência.

### Contando com lâmpadas (0 a 7, três bits)

Com 3 lâmpadas, é possível contar de 0 (todas apagadas) a 7 (todas acesas), atribuindo pesos 4, 2 e 1 às três posições — exatamente o mesmo sistema usado com os dedos. É o mesmo raciocínio do sistema decimal (base 10): "123" é lido como 1×100 + 2×10 + 3×1 porque cada posição tem um peso (unidade, dezena, centena — potências de 10). No binário, os pesos são potências de 2 (1, 2, 4, 8, 16...) em vez de potências de 10.

Tabela de contagem em binário (3 bits): 000=0, 001=1, 010=2, 011=3, 100=4, 101=5, 110=6, 111=7. Para representar 8, é preciso um **quarto** dígito — se não houver memória/hardware suficiente para esse dígito extra, o computador pode "dar a volta" (overflow) e voltar a 0 silenciosamente, causando bugs.

### Byte

Como contar até 7 ou 15 não é muito útil na prática, é comum usar **8 bits por vez** — essa unidade é o **byte**. Um byte com todos os bits em 0 representa o número 0; com todos os bits em 1, representa **255** — ou seja, 256 valores possíveis (0 a 255) com 8 bits, porque 2⁸ = 256. É por isso que 256 aparece com frequência em computação (ex.: imagens antigas limitadas a 256 cores).

Sistemas modernos comumente usam **32 bits** de uma vez (2³² ≈ 4 bilhões de combinações, ou ~2 bilhões se metade do espaço for reservada para números negativos) ou, cada vez mais, **64 bits** (2⁶⁴, um número enorme). O aumento de memória e velocidade de hardware ao longo dos anos, somado à quantidade de dados disponíveis na internet, é parte do que tornou possível o momento atual de IA — hardware encontrando a matemática/estatística que viabiliza ferramentas como o chatbot construído no início da aula.

## ASCII: representando letras

Como representar a letra "A" usando só zeros e uns? A resposta: atribuindo a ela um identificador numérico (um inteiro) por convenção. O mesmo padrão de bits pode significar coisas diferentes dependendo do **contexto** — em um app de mensagens, é interpretado como texto; em uma calculadora, como número; em um editor de imagem, como cor. O programador (ou o software) decide como interpretar aquele padrão.

Há décadas, um grupo de pessoas (majoritariamente americanas, à época) padronizou o **ASCII** (American Standard Code for Information Interchange): a letra maiúscula **A = 65**, **B = 66**, **C = 67**, e assim por diante — inicialmente em 7 bits, depois padronizado em 8 bits (1 byte) por caractere.

### Exercício: decodificando 3 bytes

Um exemplo de 3 bytes cujos valores decimais são **72, 73, 33** — consultando a tabela ASCII: 72 = H, 73 = I, 33 = ! (ponto de exclamação). Ou seja, os bytes representam **"HI!"**. Enviar essa mensagem de texto é, no fundo, transmitir esses 3 bytes; o dispositivo do destinatário, também padronizado em ASCII, sabe exibir "HI!" e não três números, cores ou qualquer outra coisa.

### Maiúsculas e minúsculas: uma diferença de 32

Letras minúsculas ficam **32 posições depois** das maiúsculas correspondentes na tabela ASCII (ex.: 'a' = 97, 'A' = 65; 97 − 65 = 32; 'b' = 98, 'B' = 66; 98 − 66 = 32). Isso significa que transformar uma letra maiúscula em minúscula (ou vice-versa) é, em binário, apenas ligar/desligar **um único bit** — o bit correspondente à posição "32" no padrão binário do caractere.

### Demonstração ao vivo: soletrando com 8 voluntários

Oito voluntários se posicionam representando, da direita para a esquerda, as posições de valor 1, 2, 4, 8, 16, 32, 64 e 128 de um byte. Cada um segue um roteiro individual (0 = ficar parado; 1 = levantar a mão) sem saber o que a palavra completa soletra. A plateia, com uma tabela ASCII em mãos, decodifica cada rodada:

- Rodada 1: padrão vale **66** → letra **B**
- Rodada 2: padrão vale **79** → letra **O**
- Rodada 3: padrão vale **87** → letra **W**

Resultado: **"BOW"** — e os voluntários fazem uma reverência (bow, em inglês).

## Além do inglês: Unicode e emoji

ASCII com 7 ou 8 bits só comporta **256 caracteres possíveis** — suficiente para o inglês (maiúsculas, minúsculas, números, pontuação), mas insuficiente para caracteres acentuados, alfabetos não latinos (árabe, chinês, japonês, grego...) e para o volume de símbolos usados hoje em dia. A resposta moderna é o **Unicode**, um superconjunto do ASCII que usa muito mais bits — 16, 24 ou até 32 bits por caractere — abrindo espaço para muito mais símbolos, incluindo **emoji**.

Um emoji é, tecnicamente, apenas um **caractere** — não uma imagem — cujo padrão de bits foi padronizado globalmente pelo Unicode Consortium (ex.: um padrão específico de 32 bits, cujo valor decimal é ~4.036.991.106, corresponde ao emoji "rosto chorando de rir"). O teclado de emoji é, essencialmente, um teclado de fontes diferentes e mais coloridas/gráficas.

Como cada fabricante (Apple, Google, Microsoft, Telegram...) é livre para desenhar graficamente como aquele caractere padronizado aparece, o mesmo emoji ("rosto chorando de rir", por exemplo) pode ter aparência visual diferente — ou até ser animado — dependendo da plataforma, mesmo representando exatamente o mesmo padrão de bits por baixo.

## Cores: RGB

Como representar cores como vermelho, verde ou azul (e tudo entre elas) usando apenas zeros e uns? Novamente, com inteiros — atribuindo valores numéricos por convenção. Uma das técnicas mais comuns é misturar três cores — **vermelho, verde e azul (RGB)** — em proporções diferentes para obter praticamente qualquer cor do arco-íris (o mesmo princípio de projetores antigos com três lentes de cor).

Exemplo: RGB = (72, 23, 33) resulta em um tom escuro de amarelo. Cada componente (R, G, B) tipicamente usa **1 byte** (8 bits), ou seja, varia de 0 a 255 — RGB (0,0,0) é preto (ausência total das três cores), RGB (255,255,255) é branco (máximo das três). Notação hexadecimal como `#00` ou `#FF`, comum em CSS/Photoshop, é apenas outra forma de representar os mesmos valores de 0 a 255.

Uma imagem digital é composta de **pixels** — pontos individuais, cada um com sua própria cor codificada em RGB. Usando 8+8+8 = 24 bits (3 bytes) por pixel, uma imagem com milhares de pixels rapidamente chega a megabytes de tamanho.

## Vídeo e som

Um **vídeo** é, essencialmente, uma sequência de ~30 imagens por segundo passando rápido o suficiente para o cérebro interpretar como movimento — o mesmo princípio de um flipbook (livrinho de folhas que, folheadas rapidamente, simulam animação). O termo "motion pictures" (o termo antigo para filme/cinema) descreve exatamente isso.

**Música/som** também pode ser representada com números: cada nota pode ser descrita por (pelo menos) três valores — **frequência/altura** (pitch), **duração** e **amplitude/volume**. Contanto que quem recebe o arquivo saiba interpretar esses números na mesma convenção, a música pode ser compartilhada e ouvida exatamente como pretendido.

## Algoritmos: da lista telefônica à busca binária

Se representação resolve o "input/output", falta o "meio" — a caixa-preta. Esse é o papel do **algoritmo**: instruções passo a passo para resolver um problema. Todo software é, no fundo, algoritmos implementados em código (C++, Java, Python, etc.).

### Exemplo: encontrar um contato

Um catálogo telefônico físico antigo (ou uma lista de contatos no celular) serve de analogia para busca. Suponha o objetivo de encontrar "John Harvard" em um catálogo de ~1000 páginas, ordenado alfabeticamente.

1. **Algoritmo 1 — busca linear página a página:** começar na página 1 e virar uma página de cada vez até achar o nome. Correto, porém **lento** — em pior caso, até 1000 páginas viradas.
2. **Algoritmo 2 — pular de 2 em 2 páginas:** o dobro da velocidade, mas **incorreto** por padrão — pode pular exatamente a página onde o nome está. É corrigível: se ultrapassar a seção e não achar, voltar uma página. Com esse ajuste, o algoritmo funciona e é ~2x mais rápido que o primeiro.
3. **Algoritmo 3 — busca binária (dividir para conquistar):** abrir o catálogo bem no meio; se o nome procurado vem antes daquele ponto, descartar a metade posterior (e vice-versa); repetir o processo na metade restante, sucessivamente, até restar uma única página.

O terceiro algoritmo é o que catálogos telefônicos físicos (e apps de contatos modernos) efetivamente usam — não literalmente "abrir no meio", mas o princípio de eliminar metade do espaço de busca a cada passo.

### As três curvas em um gráfico

Plotando "tamanho do problema" (eixo X) contra "tempo gasto" (eixo Y):

- **Algoritmo 1** (1 página por vez): reta com inclinação proporcional a **n** — dobrar o catálogo dobra exatamente o tempo.
- **Algoritmo 2** (2 páginas por vez): também uma reta, mas com metade da inclinação — ainda cresce linearmente com n, só que com uma constante melhor.
- **Algoritmo 3** (dividir ao meio): curva logarítmica, muito mais achatada — cresce **muito** devagar. Se dois catálogos de 1000 páginas se fundem em um de 2000 páginas, os algoritmos 1 e 2 dobram de tempo; o algoritmo 3 precisa de apenas **um passo a mais** de divisão.

Isso ilustra a diferença prática entre crescimento **linear** (O(n)) e **logarítmico** (O(log n)) — quanto maior o problema, maior a vantagem da busca binária.

## Pseudocódigo

**Pseudocódigo** não é um formalismo único — é uma forma de escrever passo a passo em linguagem próxima do inglês/português, sem sintaxe rígida de uma linguagem real. Traduzindo o algoritmo de busca binária no catálogo:

```
1. Pegue o catálogo telefônico
2. Abra na página do meio
3. Olhe a página
4. Se a pessoa procurada estiver na página, ligue para ela
   Senão se a pessoa vier antes na lista, abra na página do meio da metade esquerda; volte ao passo 3
   Senão se a pessoa vier depois na lista, abra na página do meio da metade direita; volte ao passo 3
   Senão, desista (a pessoa não está no catálogo)
```

O "senão, desista" é um **caso de borda (corner case)** frequentemente esquecido — se a pessoa não estiver no catálogo, sem esse passo o algoritmo entraria em loop infinito ou comportamento indefinido. Software real que "trava" ou reinicia sozinho, muitas vezes, é resultado de um desenvolvedor que esqueceu de tratar um caso de borda como este.

### Terminologia central

- **Funções** — verbos/ações que realizam uma pequena tarefa (ex.: "ligue para a pessoa", "abra na página X").
- **Condicionais** — bifurcações ("se... senão...").
- **Expressões booleanas** — perguntas com resposta binária (sim/não, verdadeiro/falso), em homenagem ao matemático George Boole.
- **Loops** — instruções de "volte para" que induzem repetição.

Esses quatro conceitos (funções, condicionais, booleanos, loops) sustentam praticamente todo código escrito no curso, seja em Scratch, C, Python ou qualquer outra linguagem.

## Da eletricidade ao código: compiladores e abstração

Assim como dados (números, letras, cores), **instruções** também são padronizadas em zeros e uns. Empresas como Intel, AMD e NVIDIA definem quais padrões de bits significam "somar dois números", "carregar dados da memória", "imprimir na tela", etc.

Escrever programas diretamente em zeros e uns (como nos primórdios da computação, com cartões perfurados) era extremamente tedioso. Por isso, alguém inventou o primeiro **compilador** — um programa que traduz uma linguagem mais amigável (ex.: C) para os zeros e uns que o hardware entende. Com o tempo, mesmo C ficou "tedioso" para certas tarefas, motivando linguagens ainda mais abstratas como **Python** (um `printf` cheio de chaves e ponto-e-vírgula em C vira um `print()` simples em Python).

Esse é o princípio da **abstração** em computação: cada geração se apoia no trabalho de quem resolveu os problemas de baixo nível antes — dos zeros e uns, a compiladores, a linguagens de alto nível, a bibliotecas e frameworks, e hoje a APIs de IA como a da OpenAI, que abstraem detalhes de implementação e permitem construir algo como o chatbot do início da aula em ~10 linhas.

## Scratch: programação visual em blocos

**Scratch**, criado há cerca de 20 anos pelo MIT Media Lab, é uma linguagem de programação **gráfica** (drag-and-drop) usada frequentemente em programas extracurriculares para ensinar programação de forma lúdica — jogos, gráficos, arte. Representa, com blocos de "quebra-cabeça", os mesmos conceitos fundamentais (funções, condicionais, loops) que serão vistos depois em C e Python.

A interface do Scratch (via navegador, em scratch.mit.edu) tem quatro partes principais:

- **Paleta de blocos** — os "blocos de construção" (funções, condicionais, loops etc.), organizados por categoria e cor.
- **Área de programação** — onde os blocos são arrastados e encaixados.
- **Sprites** — os personagens/objetos manipulados (por padrão, um gato; pode virar cachorro, pássaro, lixeira, etc.).
- **Palco** — o mundo 2D onde o sprite existe, com um plano cartesiano (X, Y) — (0,0) no centro, X positivo à direita, Y positivo para cima.

### Primeiro programa: "Hello, world"

Bloco de evento **"quando a bandeira verde for clicada"** conectado a um bloco **"fale [Hello, world]"** (categoria Aparência). Clicar na bandeira verde ("play") faz o gato exibir um balão de fala; clicar no sinal de parar ("stop") interrompe.

O bloco `fale` é uma **função**; o texto dentro do balão branco editável é um **argumento/parâmetro** (entrada da função); o balão de fala aparecendo na tela é um **efeito colateral** (side effect) — algo visível/audível que acontece como resultado de usar a função.

### Perguntando o nome do usuário

Bloco **"pergunte [Qual é o seu nome?] e espere"** (categoria Sensores) — diferente do bloco `fale`, este não tem efeito colateral imediato: ele **retorna um valor**, armazenado automaticamente na variável especial `resposta`. Um **valor de retorno** é algo que o código "vê" (mas o humano não vê diretamente), em contraste com um efeito colateral, que é visível ao humano.

Encadeando `pergunte` com `fale [resposta]`, surge um bug clássico de duas instruções que rodam sequencialmente rápido demais para o olho humano perceber (o "hello" desaparece antes do nome ser digitado). Soluções exploradas ao vivo:

1. Inserir um bloco `espere 1 segundo` entre as duas falas — funciona, mas fica visualmente "picotado" (fala "hello" depois fala o nome, separadamente).
2. Usar o bloco **`junte [hello] [resposta]`** (categoria Operadores) dentro de um único `fale`, compondo as duas strings em uma frase só — análogo a funções aninhadas, como em matemática (resolve-se o que está dentro dos parênteses antes).

Esse encadeamento ilustra composição de funções: o valor de retorno de `pergunte` (armazenado em `resposta`) vira o argumento de `junte`, cujo valor de retorno vira o argumento de `fale`.

### Extensão de texto para voz

Usando a extensão "Text to Speech" do Scratch, o bloco `fale` pode ser trocado por `fale em voz alta`, incluindo blocos de configuração como `defina voz para [tipo]` (ex.: "kitten", "giant") para variar o timbre da fala sintetizada.

### Repetição: da duplicação manual ao loop

Fazer o gato miar 3 vezes, inicialmente, foi feito **copiando e colando** três vezes o mesmo par de blocos (`toque som [Meow] até o fim` + `espere 1 segundo`). Funciona, mas é **mal projetado**: qualquer ajuste (ex.: mudar o tempo de espera) precisa ser repetido em cada cópia manualmente — um convite a erros e inconsistências à medida que o programa cresce.

Solução: bloco **`repita [3]`** (categoria Controle), envolvendo o par de blocos uma única vez — mesmo comportamento, design correto, mudanças centralizadas em um único lugar.

### Blocos customizados (funções definidas pelo usuário)

Via **"Fazer um Bloco"**, é possível criar um bloco próprio chamado `mie` (com um argumento `n`, número de vezes), cuja definição interna encapsula o `repita [n] { toque som [Meow] até o fim; espere 1 segundo }`. Uma vez definido, o bloco `mie [3]` pode ser usado livremente em qualquer lugar do programa — os detalhes de implementação ficam "fora de vista, fora da mente" (abstração), exatamente como o `print()` do Python esconde código C por baixo, e como a API da OpenAI esconde a implementação do modelo de linguagem.

### Loops infinitos e condicionais: "acariciar o gato"

Bloco **`para sempre`** (Controle) envolvendo um **`se [tocando no ponteiro do mouse?] então [toque som Meow até o fim]`** (Sensores + Controle) implementa a sensação de "acariciar" o gato: sempre que o cursor toca o sprite, ele mia.

Um erro didático comum: remover o `para sempre` e deixar só o `se`, executado uma única vez no instante em que a bandeira verde é clicada — nesse instante, o cursor quase nunca está tocando o gato, então o programa nunca detecta o toque depois. O `para sempre` garante que a condição seja **reavaliada continuamente**.

## Projeto "Oscar Time" (exemplo de PSet 0 do CS50, ~20 anos atrás)

Um jogo simples criado pelo próprio professor como exemplo do primeiro problem set do curso: o objetivo é arrastar o lixo que cai do céu até a lata de lixo (Oscar) antes que a música acabe. Construído em etapas incrementais (Oscar 0 a Oscar 4):

- **Oscar 0:** só o cenário estático (lâmpada de rua) e o sprite trocado de gato para lata de lixo — nenhum código ainda.
- **Oscar 1:** Oscar reage ao mouse — quando o cursor toca a lata de lixo, sua **fantasia (costume)** muda para "tampa aberta"; quando não está tocando, volta para "tampa fechada". Um sprite pode ter múltiplas fantasias/imagens, permitindo animação simples por troca de imagem.
- **Oscar 2:** o lixo (novo sprite) aparece em posição X aleatória, Y = topo da tela, e cai (`muda Y por -1`, em loop `para sempre`) até tocar a borda inferior. Um segundo script paralelo faz o lixo "teletransportar" de volta ao topo sempre que toca Oscar, simulando entrar na lata.
- **Oscar 3:** refatoração — extraído um bloco customizado `vá para o topo` (posição X aleatória, Y = topo), eliminando a duplicação do mesmo código em dois scripts diferentes.
- **Oscar 4:** adição de uma **variável `score`**, incrementada em 1 cada vez que o lixo toca Oscar antes de teletransportar — o Scratch exibe automaticamente um placar na tela.

A versão final soma música sincronizada manualmente (waits calculados para casar cada peça de lixo com uma menção específica na trilha sonora) e múltiplos sprites de lixo caindo simultaneamente.

## "IB's Hardest Game" (projeto de um ex-aluno)

Um jogo mais avançado, escrito por um ex-aluno do CS50, demonstra sprites com IA simples:

- **Brasão de Harvard (jogável):** move-se com as setas do teclado (`se tecla seta-cima pressionada, muda Y por 1`, etc.), e "ricocheteia" ao tocar paredes (`se tocando parede esquerda, muda X por 1`; `se tocando parede direita, muda X por -1`).
- **Sprite "Yale" (inimigo autônomo, movimento oscilante):** em loop `para sempre`, se tocando qualquer parede, `gira 180 graus`; senão, `mova 1 passo`. Aumentar o valor de "passos por iteração" (de 1 para 10) torna o movimento visivelmente mais rápido/difícil.
- **Sprite "MIT" (inimigo perseguidor):** em loop `para sempre`, `aponte na direção do brasão de Harvard` e `mova N passos`. Com N muito alto (ex.: 10), o movimento fica "nervoso"/instável visualmente — o sprite ultrapassa o alvo, corrige, ultrapassa de novo — um bug visual que ilustra a importância de calibrar a magnitude do passo por iteração.

A combinação de todos os sprites e níveis compõe o jogo completo, jogado ao vivo por uma voluntária da plateia até a vitória — marcando o fim da primeira aula, tradicionalmente celebrado com bolo.
