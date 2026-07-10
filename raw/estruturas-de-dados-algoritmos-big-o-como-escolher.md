# Estruturas de Dados, Algoritmos e Big O — Como Escolher

O mesmo código que parece instantâneo com 100 usuários pode travar quando chega a 1 milhão. É aí que entram estruturas de dados, algoritmos e Big O. Antes de escolher uma estrutura, você precisa enxergar qual operação cresce junto com os dados.

## O que você quer resolver

Antes de pensar em qual estrutura de dados usar, pense sobre o que você quer resolver. Às vezes você quer achar um usuário pelo e-mail, ou por exemplo quer pegar o próximo job que entrou numa fila. Cada caso pede uma resposta diferente. Para achar por e-mail, o ideal é ter um caminho direto. Para pegar o próximo job, a ordem de chegada importa.

Uma estrutura de dados organiza os valores de um jeito específico, e esse jeito prioriza algumas operações mas deixa outras mais caras. Por isso sempre se pergunte: o que precisa ser priorizado? Buscar, inserir, remover, percorrer, manter a ordem, consultar por chave.

## Estrutura de dados vs. algoritmo

A estrutura de dados é o jeito como os dados ficam guardados. O algoritmo é a sequência de passos que você executa em cima desses dados.

Exemplo: numa busca por e-mail, uma lista de contas. Cada conta tem nome, ID e e-mail.

- Se as contas estão numa lista, o algoritmo vai testar uma por uma até achar o e-mail certo.
- Se existe um índice por e-mail, o algoritmo consegue ir direto na chave que você pediu.

No código acontece a mesma coisa: às vezes você melhora a sequência de passos; em outros casos a grande melhoria vem de guardar os dados de outro jeito. Por isso estrutura de dados e algoritmo andam juntos — a melhor escolha de estrutura de dados transforma o algoritmo numa sequência bem mais direta e performática.

## Por que Big O

Para comparar essas escolhas, a gente precisa pensar sobre o que acontece quando a quantidade de dados cresce. Big O entra justamente aqui. Medir só em milissegundos pode enganar, porque o resultado muda com a máquina, a linguagem, o banco, o cache e um monte de detalhe do ambiente.

Por isso a pergunta tem que ser mais genérica: quando tem mais dados, o código precisa dar quantos passos a mais? Se a quantidade de dados dobra, ele faz quase o mesmo número de passos, faz o dobro, ou faz muito mais que o dobro?

- Quando o número de passos fica quase igual mesmo com mais dados, a gente chama isso de **O(1)**.
- Quando os passos aumentam na mesma proporção que os dados, a gente chama de **O(n)**.

O "n" é o tamanho da entrada. Pode ser número de usuários, produtos, linhas, nós de um grafo, ou qualquer quantidade que o problema esteja medindo. A letra pode representar coisas diferentes, mas a pergunta é sempre a mesma: o que acontece com o número de passos quando a quantidade de dados aumenta?

## As quatro curvas essenciais

Para começar, você não precisa saber tudo isso de cara. Na prática, saber essas quatro curvas já é o suficiente:

- **O(1)** — aumentar a quantidade de dados quase não muda a quantidade de passos.
- **O(n)** — o código precisa olhar item por item. Se dobrar a lista, dobra a quantidade de coisas para verificar.
- **O(log n)** — aparece quando cada passo corta uma parte grande do problema. É o caso de uma busca que sempre joga fora metade das opções.
- **O(n²)** — aparece quando cada item precisa ser comparado com vários outros. Aí uma lista duas vezes maior gera muito mais passos que só o dobro.

Um loop passando pelos itens costuma ter cara de O(n). Dois loops aninhados já é um O(n²). O segundo código cresce muito mais rápido quando a entrada aumenta. É por isso que uma solução aceitável e rápida com 1.000 itens pode ficar horrível com 100.000.

## Como escolher a estrutura certa

Na hora de escolher a melhor estrutura de dados pro seu caso, você precisa se perguntar: qual operação eu quero que seja otimizada?

- Uma estrutura pode ser ótima para buscar e muito ruim para inserir no meio.
- Outra pode facilitar inserções mas ser lenta quando você tenta acessar um item por posição.

Se o sistema busca o tempo todo, escolha pensando em busca. Se insere e remove o tempo todo, escolha pensando nisso. Se precisa manter a ordem, lembre que essa ordem sempre vai ter um custo. A melhor estrutura é a que favorece a operação que mais aparece no seu caso.

## Trade-off entre tempo e memória

Outra escolha comum é gastar mais memória para economizar passos.

- Se você só guarda a lista original, a busca pode precisar passar item por item.
- Se você mantém o índice por fora, ocupa mais espaço, mas consegue chegar no item bem mais rápido.

Esse é o raciocínio por trás de muita coisa que parece estranho no começo: você prepara uma estrutura antes para não pagar a busca inteira toda vez.

Na prática, a melhor escolha depende do limite do problema. Uma solução pode responder rápido mas ocupar espaço demais. Outra economiza espaço mas demora mais do que aceitável pro usuário. E quando o volume é pequeno, qualquer solução simples funciona. O Big O ajuda a enxergar os trade-offs, mas não significa que a menor notação é sempre a melhor opção.

## Melhor caso, pior caso e caso médio

Quando você fala da complexidade de uma busca, está falando do item do começo, do item no final, ou do que costuma acontecer na média?

Pensa numa busca simples numa lista:

- Se o item tá no começo, a resposta vem rápido (melhor caso).
- Se ele tá no final, o código tem que percorrer todos os elementos (pior caso).
- Se essa busca roda milhares de vezes por dia, o comportamento médio é o que importa (caso médio).

Numa entrevista, quando alguém pergunta a complexidade sem explicar mais nada, quase sempre tá falando sobre o pior caso. Mesmo assim, vale saber que a mesma busca pode ter o melhor caso, pior caso e o caso médio.

## Sinais numa entrevista técnica

Numa entrevista, quando te passam um problema, você precisa procurar os sinais do tipo de operação que mais importa:

- Se o enunciado fala em **dados duplicados**, vai ter uma forma melhor do que comparar todo mundo com todo mundo.
- Se fala em **busca por chave**, pense em uma estrutura que ache essa chave com O(1).
- Se fala em **próximo item, menor valor, caminho ou prefixo**, cada palavra dessas aponta para uma família de estruturas e algoritmos.

## Quatro perguntas antes de escrever a solução

Um jeito prático de pensar é fazer quatro perguntas antes de escrever a solução:

1. Qual é o N?
2. Qual a operação mais comum?
3. Qual estrutura de dados ajuda essa operação?
4. Como esse custo aumenta quando o N cresce?

Cada estrutura de dados vai entrar como resposta para um tipo de problema. A primeira estrutura a explorar são os arrays — os mais simples, e bons para sentir a diferença entre acesso direto, varredura e deslocamento.

O padrão vai ser sempre o mesmo: olhar como os dados ficam organizados, qual operação fica mais fácil, e qual o custo de cada uma.
