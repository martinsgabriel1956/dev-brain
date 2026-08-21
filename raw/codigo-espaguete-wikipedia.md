# Código Espaguete (Spaghetti Code)

> Tradução para português do artigo da Wikipédia **"Spaghetti code"**, incluindo a seção **Big ball of mud**.
> Fonte: https://en.wikipedia.org/wiki/Spaghetti_code
> Licença original: CC BY-SA. Tradução feita para fins de estudo.

---

**Código espaguete** é código-fonte de computador que codifica um **fluxo de controle** convoluto e, portanto, difícil de entender. O código espaguete pode ser causado por vários fatores, como uso contínuo de modificações por parte de várias pessoas ao longo do tempo, com estilos de programação distintos e possivelmente conflitantes.

Código espaguete bem escrito, porém complexo, é às vezes chamado ironicamente de *ravioli code*, mas o termo também pode significar código cujo fluxo de estruturas se assemelha a macarrão, torcido e emaranhado. O código espaguete também pode descrever um anti-padrão em que código orientado a objetos é escrito de forma procedural, por exemplo criando classes cujos métodos são longos e emaranhados, misturando muitas responsabilidades. Embora comumente encontrado, o resultado reduz significativamente a compreensibilidade de um sistema.

---

## História

Não está claro quando a expressão *spaghetti code* foi cunhada. **Martin Hopkins** fez uma referência inicial a "spaghetti" nesse contexto em 1972, escrevendo que a "principal motivação por trás da eliminação da instrução `goto` é a esperança de que os programas resultantes não pareçam uma tigela de espaguete" (*a bowl of spaghetti*).

No livro de 1978 *A primer on disciplined programming using PL/I, PL/CS, and PL/CT*, **Richard Conway** descreveu programas que "têm a mesma estrutura lógica limpa de um prato de espaguete" (*the same clean logical structure as a plate of spaghetti*) — frase repetida no livro de 1979 *An Introduction to Programming*, que ele coescreveu com **David Gries**.

No artigo de 1988 *A spiral model of software development and enhancement*, o termo é usado para descrever a prática mais antiga do *code and fix model* ("modelo de codificar e corrigir"), que carecia de planejamento e acabou levando ao desenvolvimento do **modelo cascata** (*waterfall*).

No livro de 1979 *Structured programming for the COBOL programmer*, o autor **Paul Noll** usa as expressões *spaghetti code* e *rat's nest* ("ninho de rato") como sinônimos para descrever código-fonte mal estruturado.

Na conferência *Ada – Europe '93*, Ada foi descrita como forçando o programador a "produzir código compreensível, em vez de código espaguete", por causa de seu mecanismo restritivo de propagação de exceções.

Em uma publicação de 1980 do *United States National Bureau of Standards*, a expressão *spaghetti program* foi usada para descrever programas antigos que tinham "arquivos fragmentados e espalhados".

Em uma paródia de linguagens de programação de 1981 na revista *The Michigan Technic*, intitulada "BASICally speaking...FORTRAN bytes!!", o autor descreveu FORTRAN afirmando que "ele consiste inteiramente de código espaguete".

**Richard Hamming** descreveu em suas aulas a etimologia do termo no contexto da programação primitiva em códigos binários:

> Se, ao corrigir um erro, você quisesse inserir algumas instruções omitidas, então pegava a instrução imediatamente anterior e a substituía por uma transferência (*transfer*) para algum espaço vazio. Lá você colocava a instrução que acabara de sobrescrever, adicionava as instruções que queria inserir e, em seguida, uma transferência de volta ao programa principal. Assim, o programa logo se tornava uma sequência de saltos do controle para lugares estranhos. Quando, como quase sempre acontece, havia erros nas correções, você usava o mesmo truque de novo, com outro espaço disponível. Como resultado, **o caminho de controle do programa pela memória logo tomava a aparência de uma lata de espaguete.** Por que não simplesmente inserir as instruções na sequência corrente? Porque então você teria que percorrer o programa inteiro e alterar todos os endereços que se referissem a qualquer uma das instruções deslocadas! Qualquer coisa, menos isso!

---

## Expressões relacionadas

### Big ball of mud (Grande bola de lama)

Uma *big ball of mud* é um sistema de software que **carece de uma arquitetura perceptível**. Embora indesejáveis do ponto de vista da engenharia de software, tais sistemas são comuns na prática por causa de pressões de negócio, rotatividade de desenvolvedores (*turnover*) e **entropia de software**. O termo foi popularizado por **Brian Foote** e **Joseph Yoder**, embora eles creditem **Brian Marick** por tê-lo cunhado.

> Uma *Big Ball of Mud* é uma selva de código espaguete estruturada de forma desordenada, esparramada, desleixada, montada com fita adesiva e arame. Esses sistemas mostram sinais inconfundíveis de crescimento não regulado e de reparos repetidos e improvisados. A informação é compartilhada promiscuamente entre elementos distantes do sistema, muitas vezes ao ponto de quase toda informação importante se tornar global ou duplicada. A estrutura geral do sistema pode nunca ter sido bem definida. Se foi, pode ter se erodido além do reconhecimento. Programadores com um mínimo de sensibilidade arquitetural evitam esses atoleiros. Apenas aqueles que não se importam com arquitetura e que, talvez, estejam confortáveis com a inércia da tarefa cotidiana de tapar os buracos dessas barragens que rompem, se contentam em trabalhar em tais sistemas.
>
> — Brian Foote e Joseph Yoder, *Big Ball of Mud*. Fourth Conference on Patterns Languages of Programs (PLoP '97/EuroPLoP '97), Monticello, Illinois, setembro de 1997.

### Relacionadas a massas (pasta)

**Lasagna code (código lasanha):** código lasanha tem camadas tão entrelaçadas que fazer uma alteração em uma camada obriga a alterar também outras camadas.

**Ravioli code (código ravióli):** código ravióli é composto por classes bem estruturadas, fáceis de entender isoladamente, mas que em combinação resultam em um design de sistema pouco claro.

---

## Prevenção

Evitar código espaguete e garantir a criação de software de alta qualidade depende de **melhores ferramentas**, **treinamento de desenvolvedores** e **melhores processos de desenvolvimento de software**.

---

## Ver também

- Anti-pattern (anti-padrão)
- Cyclomatic complexity (complexidade ciclomática)
- Goto — "Go To Statement Considered Harmful" (Edsger Dijkstra, 1968)
- Structured programming (programação estruturada)
- Software entropy (entropia de software)
- Software rot (apodrecimento de software)
- Technical debt (dívida técnica)
