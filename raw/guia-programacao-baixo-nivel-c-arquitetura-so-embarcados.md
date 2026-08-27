# Guia para começar em programação de baixo nível (C, arquitetura, SO, embarcados)

> Transcrição de vídeo, fornecida pelo usuário em português como texto bruto de fala, limpa e organizada em Markdown (pontuação, remoção de vícios de fala, divisão em seções). Conteúdo original preservado. Autoria do canal não identificada com certeza — o autor se apresenta como algo como "Way", produtor de conteúdo sobre programação de baixo nível e desempenho, possível erro de transcrição automática do nome/apelido real.

## Introdução

Vídeo dirigido a quem está cansado de React/JavaScript/Python e quer se aventurar em baixo nível: aprender C, gerenciamento de memória, lidar com memory leak, double free e os bugs típicos de quem começa a gerenciar memória manualmente. O autor propõe um guia de estudo: o que considera fundamental, quais matérias são interessantes, e como se aprofundar com projetos para portfólio em aplicações de baixo nível.

O autor se descreve como produtor de conteúdo sobre programação de baixo nível e performance, com presença em redes sociais e um canal de Discord para dúvidas.

## O que é "baixo nível"

Definição não acadêmica: proximidade da máquina — estar perto das operações que a CPU, a memória e o disco realmente fazem, em contraste com linguagens como Python e JavaScript, que têm várias camadas de abstração.

Linguagens consideradas baixo nível para os fins do vídeo: **C**, **C++**, **Rust**, **Zig**. O autor reconhece que há debate sobre se C++ "é" baixo nível, mas descarta essa discussão como ultrapassada.

## Fundamentos: a base que ninguém escapa

Antes de qualquer especialização em baixo nível, o autor defende que é indispensável ter uma base sólida em **fundamentos de programação** — sem isso, a dificuldade em baixo nível é ainda maior, porque a abstração disponível para resolver problemas é baixa. Exemplo dado: em JavaScript existe `.sort()` pronto; em C é preciso implementar a própria ordenação.

Duas áreas apontadas como fundamentais (tipicamente vistas em graduação):

1. **Estruturas de dados** — listas, filas, árvore binária, árvore B, implementação e utilidade de cada uma.
2. **Algoritmos** — ex.: detectar ciclo em grafo exige saber o que é grafo cíclico/acíclico.

Quem pula essa base terá dificuldade tanto em baixo nível quanto em web, segundo o autor.

### Fontes recomendadas para fundamentos

- **Cormen** ("Introduction to Algorithms") — chamado de "a Bíblia" da área; teórico e denso, referência completa mas de leitura difícil.
- **"Entendendo Algoritmos"** — livro citado como bem avaliado por outras pessoas, embora o autor diga ter aprendido mais por aula do que por esse livro especificamente.
- **Univesp** (universidade pública de SP, com aulas online gratuitas) — recomendada para praticamente todos os temas do vídeo, incluindo a playlist de estrutura de dados.

## Por que começar com C

Recomendação explícita: usar **C** como linguagem-base de estudo, por ser a linguagem mais próxima da máquina antes do assembly, e por ser a base da maioria dos cursos e materiais de baixo nível. Segundo o autor, não é opcional escolher só Rust ou só Zig — conhecer C (ponteiros, ponteiros de função, arrays, alocação de memória) é considerado obrigatório para quem quer trabalhar em projetos de baixo nível, mesmo que outras linguagens também sejam usadas.

## Arquitetura e organização de computadores

Segunda área apontada como essencial, mais específica de baixo nível: como o computador funciona em nível teórico — não montagem física de hardware, mas o funcionamento conceitual dos componentes.

Tópicos citados:

- **Arquitetura de Von Neumann** — modelo de comunicação entre memória de dados, memória de código e CPU.
- **Pipeline de execução** e **caches**.
- **Registradores** — o que são e como funcionam.

### Por que isso importa

Segundo o autor, ninguém programa em baixo nível "só porque quer" — normalmente há um motivo concreto (sistemas paralelos, computação de alto desempenho, sistemas embarcados, sistemas críticos), e cada motivo exige entender arquitetura para de fato ter controle de baixo nível. Exemplos de conhecimento necessário:

- Localidade de memória (temporal e espacial).
- Pipeline de execução e **branch prediction**.
- Em sistemas embarcados/críticos: interrupções, clocks de interrupção, tabela de interrupções do processador (ex.: NVIC do ARM).

O autor também aponta que boa parte dos ataques do tipo **side-channel** decorre de decisões de arquitetura nesse nível.

### Fontes recomendadas para arquitetura

Dois livros de **John Hennessy e David Patterson** (vencedores do Prêmio Turing em 2017):

- *Computer Architecture: A Quantitative Approach* — mais aprofundado, comumente usado em nível de mestrado, mas acessível a quem quiser se aprofundar.
- *Computer Organization and Design: The Hardware/Software Interface* — nível de graduação.

Sugestão de projeto: usar **VHDL** ou **Verilog** (linguagens de descrição de hardware) para construir uma CPU do zero.

## Depois da teoria: aplicar via projetos

Regra do autor: sem construir um projeto, o aprendizado não se consolida — "você pode ler 100 livros, se não fizer um programa não aprendeu nada". A partir da base de fundamentos + arquitetura, o caminho é aplicar em áreas que são, por definição, baixo nível e não permitem fugir de C/C++/Rust/etc.

### Sistemas operacionais

Apontado como uma das duas áreas centrais recomendadas. Um SO é a interface entre hardware e aplicações: troca de tarefas, execução concorrente aparente de múltiplos programas, sistema de arquivos, gerenciamento de memória (incluindo `malloc` e proteção de memória) e gerenciamento de processos. Fazer um sistema operacional do zero é apontado como uma das melhores formas de aprender baixo nível na prática — não precisa ser um Unix ou Windows completo, mas algo funcional o suficiente para rodar em um embarcado (Arduino, ESP).

O autor menciona a intenção de conduzir, como projeto para membros do canal, a construção de um sistema operacional em **Zig** para Arduino/ESP.

Fonte recomendada em português: **Carlos Maziero** (professor da UFPR), autor de um livro de sistemas operacionais usado pelo autor na graduação, com um projeto acompanhante de SO do zero baseado em POSIX/Unix — citado como o PingOS. O material do professor também referencia outros livros clássicos (ex.: um sobre Unix avançado) e sites como o OSDev Wiki.

### Sistemas embarcados

Segunda área central recomendada. Envolve trabalhar bastante a nível de protocolo e eletrônica: muito I/O, atuadores, interrupções customizadas baseadas em leitura de sensores, e a necessidade de escrever drivers (ler/escrever em sensores). Diferença apontada frente a SO: em SO muitas vezes dá para abstrair a arquitetura específica (x86, ARM); em embarcados isso não é possível — é preciso conhecer a arquitetura em detalhe.

Projetos sugeridos: pegar um Arduino ou ESP e fazer projetos pequenos; o projeto de SO mencionado acima combina as duas áreas (SO + embarcado).

### Outras áreas citadas (mencionadas, não aprofundadas)

- **Computação de alto desempenho (HPC)** — GPU, multicore, múltiplos nós, comunicação via MPI/OpenMPI; área de atuação do próprio autor. Exige algoritmos paralelos, padrões de programação em GPU e frameworks específicos.
- **Segurança ofensiva/defensiva** — o autor declara não ter tanto domínio pessoal, mas reconhece forte sobreposição com baixo nível.
- **Engenharia reversa** — envolve pegar assembly e reconstruir a lógica em C, exigindo domínio de baixo nível.

O autor justifica focar em SO e embarcados no vídeo por serem áreas mais universais, amplamente cobertas em graduação, e que englobam bastante conhecimento transferível.

## Mercado de trabalho

O autor reconhece que vagas de baixo nível no Brasil não são "as mil maravilhas" e que já fez um vídeo específico sobre isso. Mesmo assim, considera possível conseguir uma vaga com portfólio consistente, contribuição em open source e visibilidade. Cita como exemplo alguém que publicou um paper/servidor LBM (?) tipo "server fish" em 2013 e foi contratado pela Google no ano seguinte (posteriormente abandonou o projeto).

## Encerramento

O autor reconhece que a área "dá dor de cabeça" e que o retorno financeiro pode ser menor do que em web/frontend/backend, mas é uma área pela qual tem interesse genuíno. Convida a audiência a comentar se trabalha com isso, se o guia ajudou, e quais tópicos (SO, embarcados, tabelas de interrupção etc.) merecem conteúdo mais aprofundado.
