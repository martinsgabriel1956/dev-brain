---
title: "Por que C é considerado alto nível? (alto vs. baixo nível, ISA, portabilidade)"
source_type: transcrição de vídeo (PT-BR, legenda automática)
author: "não identificado (apresentador de canal que cita 'membros' e o Zig; ver nota)"
date_ingested: 2026-10-14
---

# Por que C é considerado alto nível?

> Transcrição limpa (pontuação, parágrafos e termos corrigidos; muletas de fala "né", "tá", "eh" reduzidas). Já em português; sem tradução. Correções de ASR (legenda automática): "assemble/assembleia/acendo" → assembly; "ser/C" (som de "C") → C; "a B / AB" → ABI; "BI é program interface" → ABI = *Application Binary Interface*; "isa" → ISA (*Instruction Set Architecture*); "X32/T32/Art 32/X64" → x86 (32 bits)/ARM 32/x64 (inferido); "risque/Risk 5" → RISC / RISC-V; "unde defined behavior" → *undefined behavior*; "PLM" → PL/M (inferido); "bcpl" → BCPL; "Wersc/Workers/R" → outro participante da discussão, nome incerto; "grand recursive / recursive" → usuário do Discord apelidado "Recursive"; "anônimo/grande anônimo" → outro usuário do Discord. "Anô depende do compilador" → "[Anônimo:] depende do compilador" (inferido). O nome do apresentador não aparece na transcrição.

## Abertura: alto e baixo nível significam coisas diferentes para pessoas diferentes

Em programação estamos acostumados a ouvir "baixo nível" e "alto nível", mas os termos significam coisas distintas para pessoas distintas. Não depende necessariamente de quando a pessoa começou a programar (anos 90, etc.), e sim **do que ela programa e faz**. É comum ouvir que C é uma linguagem de baixo nível; para quem trabalha perto do hardware, C é **alto nível**, e isso não está errado. A questão é o que significa cada nível. A discussão veio de uma conversa no Discord, e o apresentador quer mostrar os argumentos de por que C é alto nível.

## A discussão no Discord

Um usuário anônimo falava de desenvolvimento de linguagem ou de algo para otimizar instruções, e o usuário "Recursive" entrou na conversa. Pergunta inicial: existe documentação de como construir qualquer coisa minimamente funcional em assembly sem precisar caçar as instruções da CPU? Assembly seria *low level*?

### A pergunta sobre ABI e velocidade

O anônimo comenta que a ideia de usar assembly é caçar instruções da CPU, mas nada impede de seguir uma **ABI** como a de C para fazer as coisas. ABI = *Application Binary Interface*, a interface binária; a interface binária "universal" é a de C, ninguém usa outra. A ideia é sempre ter o máximo de velocidade possível da CPU com o menor consumo de memória. Isso se faz com instruções específicas que o compilador não consegue gerar de forma consistente: se você quer máximo de velocidade e menos memória, não quer um compilador, quer assembly. Então o "minimamente acima de funcional" seria o assembly.

### Resposta do Recursive: o modelo do assembly é outro

O anônimo diz que "depende do compilador": é extremamente difícil fazer um compilador gerar instruções otimizadas para tudo, e, dependendo da linguagem em cima, pode ser **impossível** gerar algumas delas. O apresentador destaca que isso é muito importante, porque o **modelo em que o assembly funciona e o modelo em que uma linguagem funciona são bem diferentes**.

No assembly, na máquina, você tem **registradores**, **memória** e **instruções**. Não existe função, não existe variável, não existe loop; esses conceitos podem até ser *criados* em assembly, mas a máquina em si é registrador, *program counter* e espaço de memória. Pode haver classes diferentes de registradores (por exemplo, vetoriais), diferentes modos de endereçamento de memória e extensões (um coprocessador de ponto flutuante, por exemplo; estamos acostumados com ponto flutuante porque todos os computadores têm, mas nem todas as CPUs têm). O assembly é a **interface com a máquina**. A linguagem de programação tem outro propósito: ser a **interface com o programador**. Ao pensar em linguagem pensamos na máquina também, mas o principal é a nossa relação com a linguagem.

### Otimização: difícil, não impossível?

O anônimo diz que otimizar é difícil, não impossível; "se fosse fácil, qualquer um faria". O Recursive responde que em C, por exemplo, é **impossível** ter acesso a registradores periféricos que não são mapeados em memória: você precisa escrever assembly para acessá-los, porque a linguagem simplesmente não foi projetada com isso em mente. O mesmo vale para as demais linguagens de alto nível. Já para as de "low level" seria uma tarefa difícil, mas não impossível, porque seriam apenas um nível acima do assembly. E sim, **C é alto nível**.

O apresentador explica: C não é pensada na arquitetura; ela não foca na arquitetura. Seja x86, ARM, RISC, uma arquitetura dos anos 80/90 (antigamente havia muito mais diversidade de arquiteturas no mainstream; hoje há menos, mas em embarcados ainda existe), C **abstrai tudo isso** e não se preocupa com o que está na máquina, porque é de alto nível.

### Exemplo clássico: troca de contexto

Um exemplo clássico em que é preciso escrever assembly para tocar registradores: a **troca de contexto** em um sistema operacional (o programa para de rodar e outro começa). É preciso salvar todo o estado do processador, incluindo os registradores, em algum lugar, e depois carregá-lo de volta. Todo sistema operacional precisa implementar isso, e **não dá para fazer em C, só em assembly**. As linguagens de "low level" seriam as que se preocupam e colocam a abstração no nível do assembly, do hardware.

### O mais importante: interoperabilidade

O apresentador diz que esqueceu de comentar o ponto mais importante do alto nível: a **interoperabilidade**. É pegar o mesmo programa e compilá-lo em máquinas diferentes, marcas X, Y e Z, arquiteturas X, Y e Z, versões diferentes. Isso foi **revolucionário**: não precisar escrever um programa diferente para cada máquina. Um dos motivos de C ser tão adotado é que existiam compiladores de C para diversas arquiteturas; até hoje é a linguagem mais universal, a que compila para a maior gama de arquiteturas da história. Escreve-se um programa e ele compila para diversas arquiteturas, diversas ISAs.

## C é "mid level"?

O anônimo concorda que C é *high level* comparado ao assembly, mas o colocaria em "mid level". O apresentador diz que não vai entrar no mérito, mas que é daí que vem o debate. O anônimo sugere que o problema seria C ser "portável demais"; o apresentador corrige: ser portável é **por design**, essas linguagens são pensadas para serem portáveis; o problema não é ser portável demais, é simplesmente ser portável.

### Definição do Recursive

> "Assembly é a representação mais baixa possível da ISA." ISA = *Instruction Set Architecture*, o conjunto de instruções e como o hardware funciona (ou, no mínimo, o modelo que se precisa ter em mente para escrever código para ele: conjunto de instruções, modelo de endereçamento, extensões; é a especificação da CPU).

Assembly é sempre a representação mais baixa possível da ISA; **não contém nem pode conter conceitos abstratos**; precisa ser o mais possível um-para-um com o hardware, porque esse é o objetivo. Um assembly só é portável se a arquitetura também for: x86 de 32 bits roda em x64 porque o x64 é feito em cima do x86, mas não roda em ARM de 32 bits, nem em RISC-V, etc. Para ter algo portável, **obrigatoriamente** é preciso se afastar do hardware e introduzir conceitos abstratos, como funções, ponteiros, *unions* etc.

O apresentador acha que aqui o Recursive pega o núcleo do que, para muita gente de baixo nível, é a diferença entre baixo e alto nível: no **baixo nível** você fala do hardware, específico daquele hardware, no assembly; no **alto nível** há uma **abstração em cima do hardware**. Se quiser diferenciar também *acima* disso (C versus Python, C versus Java, C++), faz sentido e ele concorda, mas para quem é de baixo nível a regra é: **tenho abstração em cima do hardware → alto nível; não tenho → baixo nível**. Não é bom ou ruim; cada um serve a seu propósito. O FFmpeg tem partes em assembly; sistemas operacionais têm partes em assembly por requisitos funcionais. Não há certo ou errado, e geralmente, quando se chega nesse nível, **mistura-se os dois**: o que é portável em linguagem, o que não é portável em assembly. Ou, se quiser, tudo em assembly; ninguém proíbe.

## Otimização, retrocompatibilidade e a história

O anônimo pergunta se dá para exportar as otimizações, fazendo uma linguagem para assembly, e acha que dá para fazer um pouco melhor. Sobre "portável demais": x86 de 32 bits é portável de certa forma para x64, mas aí você depende da arquitetura. O x86 é historicamente **retrocompatível**, por motivos da Intel e de quem tem dinheiro ali: há programas dos anos 80 rodando dos quais não existe mais código-fonte, só o binário, e ninguém vai recompilar. Por isso muitas instruções remetem ao 8080 e a processadores da Intel dos anos 70/80. Retrocompatibilidade é extremamente importante na indústria, principalmente nas bem tradicionais, com dinheiro para financiar isso.

### Linguagens de baixo nível "portáveis" antigas

O Recursive responde sobre linguagens como BCPL e PL/M, que se baseavam nessa ideia de ser de "baixo nível" e portáveis. O problema: cada arquitetura é diferente, algumas completamente incompatíveis, o que forçava o fabricante a criar dialetos, extensões e *forks* dessas linguagens para funcionar de forma agradável em seu hardware. Para quem criava software, era horrível: decorava-se bem menos coisa que em assembly, mas era preciso lidar com comportamentos dependentes de máquina e de fabricante, que distribuía e mantinha várias versões de compiladores/interpretadores, numa época em que a internet basicamente não existia. Era um caos que foi evoluindo até chegar ao alto nível: BCPL foi para B, que seria a base de C, resolvendo os problemas **em parte** (C ainda tem *undefined behavior* justamente por isso), "até que exista uma arquitetura indiscutivelmente perfeita, o que provavelmente não vai acontecer neste milênio".

O apresentador comenta que hoje damos por garantido que nosso programa roda na máquina (navegador, x86 meio universal), mas nos anos 60, 70 e 80 havia uma diversidade enorme de arquiteturas: se seu programa rodava na arquitetura X e a empresa a quem você queria vender usava a Y, ou você reescrevia o programa ou precisava de uma ferramenta que o traduzisse, sem falar em bugs e manutenção. Com C como "dialeto universal", escreve-se o programa em C (com algumas exceções em assembly), cada arquitetura tem um compilador que gera um binário para aquela máquina, e idealmente o comportamento é o mesmo: **corrige-se uma vez, corrige-se para todos**. Isso coloca o peso no compilador, não no fabricante.

## Dependência de caminho e o futuro

É interessante ver a história por essa perspectiva, porque esquecemos a **dependência de caminho** (*path dependence*): nada surge do nada; o que usamos hoje vem de decisões dos anos 60 e 70. Vale a pena mudar? Como definir isso? Não sabe. Será que existirá uma arquitetura indiscutivelmente perfeita? Quanto estamos dispostos a investir em tempo, dinheiro e recurso? Exemplo hipotético: se nos anos 2000 decidíssemos unificar tudo, de repente surge a GPU e quebra muita coisa, ou outra tecnologia.

O apresentador elogia o Recursive ("uma aula de história"). Também quer deixar claro que **não é porque todo mundo usa C que ele é perfeito**: tem vários problemas (como o *undefined behavior*), mas tanta coisa depende de ele ser universal que superá-lo é difícil de imaginar. Isso aconteceu por questões históricas, não porque seja necessariamente certo ou errado: C "ganhou as batalhas das linguagens" no nível de abstração imediatamente acima do assembly com portabilidade universal. Mesmo assim, ele acha que **o ecossistema tem muito a melhorar**; gosta da abordagem de **Zig** (como quem acompanha o canal deve saber), mas não acha que melhorar seja fácil, rápido ou garantido, só que não se deve aceitar "está ruim, mas é assim". Como melhorar é onde ninguém concorda e surgem as brigas: ele gosta de alternativas de outras linguagens; há quem prefira construir ferramentas em cima de C ou linguagens que transpilem para C, e isso também é válido.

## Resumo final do apresentador

Por que dizem que C é alto nível? Para quem é do baixo nível, alto/baixo está associado à **abstração em relação ao hardware**: no nível do hardware, com controle fino de registradores e PC, em correspondência um-para-um, você está em baixo nível (assembly). Se você tem uma abstração sobre o hardware e **ganha portabilidade**, já está em alto nível (C): troca-se controle de hardware por portabilidade. Para a maior parte dos programas, tenta-se deixar o específico de hardware e otimizado em algumas porções e o resto geral. Desafio: tentar escrever um programinha do zero para RISC, ARM e x86 para entender o "trabalho hercúleo" que as pessoas tinham antes das linguagens de alto nível, ou, como outro participante falou, com extensões de linguagens de baixo nível.
