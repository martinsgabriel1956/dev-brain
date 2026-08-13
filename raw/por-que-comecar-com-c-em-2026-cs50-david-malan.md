# Por que começar com C em 2026 (CS50 — David Malan)

> Transcrição traduzida do inglês para o português. Conteúdo: David Malan (professor do CS50, Harvard) explica por que o curso ainda começa ensinando a linguagem C em 2026, e responde à crítica de que "você não precisa saber como o computador funciona por baixo dos panos".

## Por que começar com C em 2026

C é uma fundação maravilhosa sobre a qual construir o entendimento de como um computador funciona e como o software é feito. É quase o mais perto que dá para chegar do hardware antes que as coisas descambem — pelo menos esteticamente — para o código assembly, que é um código bem mais assustador de olhar, acho que para quase todo mundo. E além do assembly já são zeros e uns, o que não vai ser divertido para ninguém.

Então C acaba, pedagogicamente, encontrando um equilíbrio muito bom: tem uma sintaxe e abstrações parecidas com o inglês sobre primitivas de nível mais baixo, o que permite explorar programação procedural com construtos fundamentais que hoje são fundamentais para esse tipo de linguagem — loops, condicionais, funções, variáveis, valores de retorno e assim por diante. Tem tudo, mas ao mesmo tempo é uma linguagem bem pequena. A menos que você baixe bibliotecas de terceiros, a biblioteca padrão não é muito grande. Na prática, quase tudo o que você quiser você precisa construir por conta própria.

No CS50 a gente aproveita muito isso. Tanto que, na metade do semestre — na semana cinco do curso —, os alunos estão construindo suas próprias tabelas hash (hash tables). Estamos falando de como construir listas ligadas simples e duplamente encadeadas, hash tables e tries, árvores, tipos abstratos de dados como pilhas (stacks) e filas (queues), e muito mais.

O que acho especialmente significativo em C é que você não pode simplesmente instanciar uma dessas estruturas de dados quando quer uma — como você pode em Java e C++ com a STL e outras bibliotecas. Se você quer uma, vai ter que construí-la você mesmo. E só isso já é um bom exercício educacional. Não porque você vá precisar construir aquilo de novo, mas porque há valor em entender de baixo para cima o que está acontecendo dentro do dispositivo. Assim:

1. Você consegue tomar decisões mais informadas sobre como quer projetar e engenheirar suas próprias estruturas de dados.
2. Você consegue diagnosticar problemas raciocinando a partir de primeiros princípios — o que poderia dar errado —, porque você entende como os dados estão sendo armazenados e quais são os algoritmos que operam sobre esses dados.
3. É um andaime (scaffold) maravilhoso para linguagens de nível mais alto.

Uma das minhas coisas favoritas entre a semana cinco e a semana seis do CS50: os alunos saem de ter escrito, na semana cinco, a própria implementação de uma hash table — para adicionar dados, recuperar dados e por aí vai, que dá um tanto de linhas de código para determinado tamanho de fonte — e na semana seis isso é reduzido a uma única linha, na qual você apenas instancia um dicionário em Python.

Você consegue ser produtivo com um dicionário, e muitos cursos ensinam programação só por meio de Python. A gente também já fez isso para alguns públicos. Mas você nunca chega de fato a entender o que está acontecendo por baixo do capô. Um dos nossos objetivos no CS50 não é produzir programadores, mas engenheiros — e cidadãos instruídos, gente que realmente entende, a partir de primeiros princípios, como a tecnologia funciona. C, por exemplo, encontra exatamente esse equilíbrio certo.

Para os alunos que querem ir ainda mais fundo, numa disciplina de sistemas, eles podem ir aprender sobre assembly, compiladores e assim por diante. E os que querem seguir para programação web, ciência de dados ou coisas de IA hoje em dia podem simplesmente construir em cima das camadas de C e, na sequência, de Python que usamos no curso.

## "Não me diga que você não precisa saber como o computador funciona"

**Entrevistador:** Eu estava pesquisando e vi um vídeo no YouTube que dizia "faça o que fizer, não faça o CS50". Um clickbait. Aí eu assisti ao vídeo — e me pegou, me pegou. A perspectiva do autor do vídeo era que o CS50 ensina um monte de coisa que você não precisa saber se você for, tipo, um engenheiro full stack. Tipo, se eu fosse só entrar na indústria fazendo web apps, usando JavaScript ou o que seja, muita dessa coisa mais de base você talvez não precise — e então talvez não seja um bom uso do tempo. Estou curioso: o que você diria a alguém com essa mentalidade, de que você não precisa de fato saber como o computador funciona?

**David Malan:** Não quero começar uma briga inteira na internet aqui, mas acho que essa é absolutamente a mentalidade errada — certamente para um engenheiro full stack. Por definição de full stack, você deveria estar entendendo tudo o que acontece entre essas camadas.

Acho que a formulação melhor não é que você não precisa saber essas coisas, mas sim que você não vai precisar usar essas coisas — usar num sentido literal. Por exemplo, meu... C é uma linguagem muito popular. Segundo alguns rankings, ano após ano ela é a número um ou número dois em onipresença, ainda hoje, porque é altamente performática — ainda que mais difícil de escrever do que algumas linguagens. Eu só uso C por cinco semanas durante o próprio CS50. Mas isso não significa que ela não tenha me ajudado a entender linguagens de nível mais alto, o que está acontecendo dentro de um sistema, como você pode melhorar a performance ou o design de algum sistema entendendo, de novo, esses primeiros princípios.

Eu não uso Scratch, exceto por uma semana do ano. Eu uso Python com mais frequência, e uso JavaScript, um pouco de HTML e CSS. Mas acho que, se você vai se chamar de engenheiro, você deveria absolutamente ter domínio e conhecimento desses blocos de construção fundamentais — se o que você quer é não apenas cuspir algo que, francamente, uma IA hoje conseguiria cuspir, mas sim entender e conseguir criar a próxima coisa, ou a solução para algum outro problema que a gente ainda nem resolveu.

Acho que essa é a mentalidade melhor de se ter: sim, eu não vou precisar usar Scratch, ou C, ou talvez algumas das outras coisas que abordamos no CS50 — mas o conhecimento e os princípios que extraímos desses detalhes de implementação são incrivelmente valiosos se o que você quer é ser um engenheiro, e não apenas um "coder" (programador no sentido raso). É uma distinção que algumas pessoas talvez façam.
