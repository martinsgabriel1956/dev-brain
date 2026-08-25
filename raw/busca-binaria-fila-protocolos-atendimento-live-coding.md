# Busca Binária: Encontrando a Posição de um Protocolo numa Fila Ordenada (Live Coding)

Transcrição de um corte de live coding (canal de cortes, material extraído do canal principal "Fernanda Kiperdev"), com leitura ao vivo de trechos do livro *Entendendo Algoritmos*.

## O problema

O desafio aqui é a gente conseguir encontrar a resposta correta em um array de números. Digamos que a gente tem um array com dados e esses dados estão ordenados — ordenados quer dizer que eles estão em ordem. Se for um array numérico, eles vão estar ordenados em ordem crescente ou decrescente; também se for um array de strings, eles vão estar ordenados em ordem alfabética. Então esses dados estão ordenados nesse array, e aí o nosso objetivo é descobrir em qual posição essa resposta que a gente tá procurando está nesse array.

Eu tenho um array com vários números ordenados em ordem crescente. Eu quero encontrar onde tá o número 1250. Só que são números aleatórios — não é 1, 2, 3, 4, 5, 6. Eu posso ter 1, 4, 7, 12, 27, 52, 67, vários números aleatórios, mas ordenados em ordem crescente. Eu quero descobrir em qual posição desse array o número 1253 está. Para eu descobrir a posição desse número nesse array ordenado, eu posso escrever alguns tipos de algoritmos — a gente vai estudar na live de hoje qual é o algoritmo mais eficiente para eu fazer essa descoberta da posição da resposta correta em um array ordenado.

## Exemplo prático: fila de protocolos de atendimento

Vamos pegar um exemplo do mundo real agora. Digamos que a gente trabalha num sistema de atendimento que controla os protocolos através de filas, e esses protocolos ficam armazenados em ordem crescente. Então eu tenho ali o protocolo número 1001, número 1008, número 1012, 1019, 1024, 1030, vários protocolos. Dado o número de um protocolo — digamos que eu preciso encontrar o protocolo número 1024 — o nosso desafio é encontrar a posição desse protocolo nessa fila, que é uma lista de dados, uma lista de números.

Algumas observações sobre esse desafio, para que a gente consiga introduzir esse algoritmo:

- Essa lista vai estar **sempre ordenada**, como mencionado.
- A posição desse número na lista é considerada a partir do **índice da lista**: uma lista sempre começa no índice zero, não no índice um, e vai crescendo (0, 1, 2, 3, 4, 5, 6...). Se uma lista tem 100 números, os índices vão de 0 a 99.

O desafio não é apenas encontrar aquele valor, mas também pensar em como fazer isso de maneira inteligente — de maneira eficiente — à medida que a lista aumenta.

## Pergunta ao chat: "o que vocês fariam?"

Antes de partir para a leitura do livro *Entendendo Algoritmos*, foi pedido para o pessoal do chat mandar o que eles fariam — um exercício em conjunto para desenferrujar a lógica, sem depender de IA para gerar a resposta. A pergunta: vocês têm uma lista ordenada e precisam encontrar um protocolo específico dentro dela, sabendo que essa lista pode ter **1 milhão de protocolos** — qual é a posição de um protocolo específico?

Respostas do chat:

- **Teles:** "Rapaz, eu não faço a mínima ideia."
- **Rick:** "Talvez uma busca binária."
- **Fel:** "Só sei binary search."
- **Bianca:** "Eu arriscaria resolver com busca binária."
- **Albert Conceição:** "Eu lembrei do dividir e conquistar (divide and conquer), mas não sei se seria o melhor."
- **Fábio:** "Eu compararia o elemento com cada um; se desse match, eu guardava o índice."
- **Jomo:** também iria de busca binária.
- **Victor:** "Busca binária?"
- **Daniel:** "Binary search — eu tava treinando isso, tá fresquinho na minha mente."
- **Felipe Brandão:** "Dividindo a lista ao meio e vendo se está maior, menor ou igual, até chegar no valor."
- **Rodrigo Rosa:** "Algoritmo de quick search."
- **Bruno:** "Busca binária."
- **Vida Program:** "Busca binária."

O algoritmo que o Felipe descreveu no chat — dividir a lista ao meio e olhar se o valor do meio é maior, menor ou igual — é exatamente a **busca binária**.

## Como a busca binária funciona, passo a passo

Eu pego a lista, divido ela ao meio. Digamos que eu tenho os elementos do 1001 ao 1038. Se eu dividisse ela ao meio, a metade dessa lista seria o número 1019. Aí eu olho: o número 1019 é maior ou igual ao número que eu tô buscando? Digamos que o número que eu tô buscando é 1024. Então 1019 é menor. Se ele é menor, o que isso significa? Significa que tudo que vem antes de 1019 eu vou jogar fora, porque eu já sei que são todos números menores do que eu tô buscando.

Por que eu sei disso? **Porque a lista está ordenada.** Se ela não estivesse ordenada, toda essa lógica cairia por terra — nesse caso eu teria outro problema, e poderia primeiro ordenar a lista e depois buscar, ou usar outro algoritmo de busca.

Então, sabendo que 1019 é menor, eu pego tudo que vem antes dele — toda a metade inicial — e jogo fora. Agora eu fico só com 1024, 1030 e 1038. O que eu faço? Divido ao meio de novo e faço a mesma comparação: 1030 é maior, igual ou menor que 1024? Maior. Então tudo que vem depois de 1030 eu jogo fora, e fico só com 1024. Pego o meio — só tem um número, o próprio 1024 — maior, igual ou menor? Igual. Aí eu descubro a posição do número 1024.

Eu faço isso guardando sempre a "cabeça" da lista, para saber em qual ponto eu estou, e assim eu consigo saber em qual índice eu tô.

### Caso onde o valor está numa posição diferente (1008)

Vamos aplicar para o 1008: corto a lista pela metade, 1019, comparo — 1019 é maior. Toda a metade de cima eu jogo fora. Fico com 1001, 1008, 1012. Corto pela metade — já vou cair no 1008. 1008 é menor, maior ou igual? Igual. Achei a posição dele.

### Caso onde o valor está numa posição diferente (1012)

Aplicando o mesmo para o 1012: 1019, corto pelo meio de novo, 1019 é menor, igual ou maior que 1012? Maior. Toda a metade de cima eu jogo fora. Sobra a lista de três: 1001, 1008, 1012. 1008 é maior, menor ou igual a 1012? Menor. Jogo tudo pra trás do 1008 fora. Sobra uma lista com um elemento: 1012. Maior, menor ou igual? Igual. Achei.

### Caso onde o valor não existe na lista (1013)

Buscando o 1013: corto pelo meio, 1019, maior ou igual ou menor? Maior. Jogo tudo do 1019 pra cima fora. Sobra a lista de três: 1001, 1008, 1012. 1008, maior, menor ou igual? Menor. Tudo abaixo de 1008 eu corto fora, porque eu sei que é menor do que o número que eu tô buscando (1013). Sobra uma lista com uma posição: 1012. Maior, menor ou igual? Menor. Jogo fora — e fico com uma lista com **zero elementos**. Aí eu sei que o 1013 não está nessa lista, e retorno **não encontrado** (nil/null).

Esse algoritmo só funciona se a lista estiver ordenada. Se a lista não estiver ordenada, com os números aleatórios, não dá para usar a busca binária diretamente — ou primeiro ordena a lista e depois busca, ou usa outro algoritmo de busca.

## Trecho lido do livro "Entendendo Algoritmos"

> Vamos supor que você está procurando o nome de uma pessoa numa lista telefônica. O nome começa com K. Você pode começar na primeira página da agenda e ir folhando até chegar ao K. Porém, você provavelmente vai começar pela metade, pois sabe que os K estarão mais perto dali.
>
> Ou suponha que você esteja procurando uma palavra que começa com O em um dicionário — novamente, você começa a busca pelo meio.
>
> Agora imagine que você entre no Facebook. Quando faz isso, o Facebook precisa verificar que você tem uma conta no site; logo, ele procura seu nome de usuário em um banco de dados. Digamos que o seu usuário seja `kalmcdaggon`. O Facebook poderia começar pelos As e procurar seu nome, mas faz mais sentido que ele comece a busca pelo M.
>
> Isso é um problema de busca, e todos esses casos usam um algoritmo para resolvê-lo: o algoritmo da **pesquisa binária**.
>
> A pesquisa binária é um algoritmo cuja entrada é uma lista ordenada de elementos. Se o elemento que você tá buscando está nessa lista, a pesquisa binária retorna a sua localização — ou seja, a posição/índice daquele elemento na lista. Caso contrário, a pesquisa binária retorna **nil** (não encontrou).
>
> Eis um exemplo de uma pesquisa binária e como ela funciona: eu estou pensando em um número entre 1 e 100. Você deve procurar adivinhar o meu número com o menor número de tentativas possível.

### Por que "menor número de tentativas" importa

Isso é bem importante. Eu até posso descobrir, por exemplo, o número em que você está pensando dizendo um por um: número um? não. Número dois? não. Número três? não. Número quatro? Número cinco? Número seis? — posso ir falando de forma consecutiva e sequencial todos os números até chegar no número certo. Só que isso não é eficiente, porque eu vou ter que testar várias tentativas até chegar lá.

Se você estiver pensando no número 2, beleza, vai ser rápido: "1? não. 2? sim." Agora se você estava pensando no número 99, eu vou ter que falar do 1 até o 99 para adivinhar — isso vai fazer com que eu gaste várias tentativas. Se o meu objetivo é usar o menor número de tentativas possível, é aí que eu vou olhar para um algoritmo que vai transformar essa busca numa busca mais eficiente.

Isso é muito importante ter em mente porque é justamente o cenário que a gente vai lidar quando estiver trabalhando, por exemplo, com um sistema de atendimento que coloca tudo numa fila e a gente precisa encontrar a posição daquele cara na lista ordenada — porque muito provavelmente eu vou ter milhões de dados dentro dessa lista, não cinco ou dez elementos. Isso aí é irrisório, não é um problema onde eu preciso tornar mais eficiente com o algoritmo. O problema mesmo vai ser quando eu tiver lidando com milhares, centenas ou milhões de dados, e aí eu vou querer fazer essa busca da maneira mais eficiente possível, porque eu preciso que isso seja rápido.

O problema de eu ficar tentando um por um — o **brute force**, ou "pesquisa estúpida"/"pesquisa simples" como o livro chama — é que eu vou testar várias vezes e isso vai levar tempo. Quando eu uso um algoritmo como a busca binária, eu consigo reduzir significativamente esse tempo e esse número de tentativas até descobrir o número certo.

### Continuação do trecho do livro

> A cada tentativa eu digo se você chutou muito para cima, muito para baixo, ou corretamente. Digamos que você começou tentando assim: 1, 2, 3, 4 — veja como ficaria: um, muito abaixo; dois, muito abaixo; sete, muito abaixo. Isso se chama pesquisa simples (ou brute force, "pesquisa estúpida"). A cada tentativa você está eliminando apenas um número. Se o meu número fosse o 99, você precisaria de 99 chances para acertar.
>
> Uma maneira melhor de buscar é usar a pesquisa binária. Aqui está a técnica melhor: você começa pelo número 50 — a gente começa pelo meio. Se eu digo que esse número 50 tá muito abaixo do número que eu tô pensando, eu já elimino metade dos números dessa lista. Agora se tu falar que tá muito alto, eu elimino a outra metade, a metade maior. E assim, a cada próximo chute, eu vou eliminando metade dos elementos restantes, porque eu sempre vou chutando o número do meio, comparando se é maior ou menor, e eliminando uma metade ou a outra da lista até eu chegar num único número restante. Isso é a pesquisa binária.
>
> Você acaba de aprender um algoritmo. Aqui está a quantidade de números que você precisa eliminar por tentativa: com 100 itens, a gente conseguiria adivinhar, por exemplo, o número 99, em sete etapas. Seja qual for o número em que eu estiver pensando, você pode adivinhá-lo em um máximo de sete tentativas, porque a pesquisa binária elimina muitas possibilidades.
>
> Agora suponha que você esteja buscando uma palavra em um dicionário. O dicionário tem 240.000 palavras. Na pior das hipóteses, de quantas etapas você acha que você precisaria?

Se eu procurasse usando a pesquisa simples (brute force) e a posição dessa palavra estivesse lá em 239.999, eu ia ter que testar 239.999 vezes até encontrar a palavra. Agora, se eu utilizar a pesquisa binária, a cada etapa eu vou eliminando a metade das palavras restantes, até que só reste uma palavra. Usando o algoritmo de pesquisa binária, isso leva a **18 etapas** — uma lista com 240.000 itens só precisa de no máximo 18 etapas para encontrar a posição da palavra.

### A fórmula geral: log₂(n)

De maneira geral, para uma lista de **n** números (n pode ser qualquer número — 200, 1 milhão, 1 bilhão), a pesquisa binária precisa de **log de 2 na n** para retornar o valor correto. O log aqui, logaritmos, é sempre de divisão — e é um logaritmo de base 2 porque a gente tá sempre dividindo ao meio a cada etapa: dividindo por 2, dividindo por 2, dividindo por 2. Enquanto a pesquisa simples precisaria de **n** etapas, sendo n o comprimento da lista.

> Você pode não se lembrar de logaritmos, mas provavelmente lembra-se de como calcular exponenciais. A expressão log de 100 basicamente diz: quantos 10 eu consigo multiplicar para chegar a 100? A resposta é 2. Então log₁₀(100) é 2. Os logaritmos são os opostos dos exponenciais.

### Pergunta do chat: "e se o número tiver na metade retirada?"

**Rafael Sena** perguntou: "Mas e se por acaso o número tiver na metade retirada?"

Resposta: não tem como o número estar na metade retirada. Esse algoritmo só se aplica quando a lista está ordenada. Digamos que eu tô procurando um número 100: se eu corto a lista pela metade, o primeiro número que eu vou observar é o 1019. Aí eu pergunto: 1019 é maior ou menor que 100? Maior — então toda a metade para cima de 1019 eu jogo fora, porque eu sei que o 100 tá na metade de baixo, **porque a lista está ordenada**.

## Resumo final

O algoritmo só funciona se a lista estiver ordenada. Se eu estiver lidando com uma lista que não está ordenada, com os números aleatórios, não dá para usar a busca binária diretamente — eu posso primeiro ordenar essa lista, colocá-la em ordem, e depois usar a busca binária, ou posso usar outros algoritmos de busca.

---

*Nota de origem: este quadro foi retirado de um live coding que acontece todo segundo e quarto domingo do mês no canal principal "Fernanda Kiperdev", com conteúdo sobre programação e tecnologia. Publicado como corte no canal secundário do mesmo criador.*
