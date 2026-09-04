> Transcrição de vídeo fornecida pelo usuário em fala corrida, sem pontuação, em português (pt-BR — sem necessidade de tradução). Formatada e pontuada abaixo, com pequenas correções de reconhecimento de fala marcadas entre colchetes onde o termo técnico ficou ambíguo na transcrição original. Autoria não identificada por nome na fala (fala em primeira pessoa, menciona ter um curso próprio de estruturas de dados e algoritmos com aulas dadas pelo próprio autor — não confirmado quem é).

# Recursão vs. Iteração: Call Stack, Church-Turing e Tail Call Optimization

Steve Jobs tem uma palestra muito famosa em que ele fala sobre "connecting the dots" — conectar os pontos. Nessa palestra ele fala sobre como adquiriu conhecimento durante a vida inteira dele: ele não sabia como esse conhecimento faria sentido, e em algum momento ele conseguiu conectar esses pontos, olhando pro passado dele, e tudo aquilo que ele tinha aprendido começou a fazer algum sentido.

Por que eu tô te falando isso? Porque esse vídeo aqui vai ser mais ou menos acadêmico e não vai ter uma aplicabilidade hoje em dia no seu trabalho — possivelmente isso aqui não tem relevância nenhuma para você hoje no seu mercado de trabalho, mas mesmo assim eu acho que seria interessante você aprender. Então hoje a gente vai falar de recursão e iteração.

## A crença popular: iteração é mais eficiente

Talvez vocês tenham ouvido falar de alguém — até bem-intencionado, possivelmente uma pessoa muito inteligente — que já te falou que iteração é a maneira mais rápida, e que recursão não é recomendado, que recursão vai ser menos eficiente. Muita gente também vai acabar achando que recursão é mais complexa. Hoje em dia a gente pode falar, de forma bastante branda, que o approach iterativo é mais favorecido na maioria dos contextos, na maioria das linguagens. As pessoas vão te dizer que algoritmos de maneira iterativa são mais eficientes e menos complexos.

Isso, de forma rasa, numa recomendação branda para as linguagens mais utilizadas — como por exemplo Python — não seria de todo errado: você fazer um algoritmo recursivo em Python sem nenhum tipo de otimização provavelmente vai ser terrivelmente ineficiente, e iteração vai ser melhor.

Agora, o que tá acontecendo aqui de verdade? Porque a maneira com que as pessoas lidam com esse assunto de recursão versus iteração — e a maneira com que eu lidei com isso durante muito tempo — me diz que tanto eu quanto essas pessoas, de repente, nunca pararam para realmente pensar no que tá acontecendo. Então vamos explicar um pouco o que tá acontecendo aqui, para depois a gente desconstruir essa explicação.

## Fatorial: iterativo vs. recursivo

Iteração talvez seja algo autoexplicativo — a função fatorial de maneira iterativa é um pouco explícita no que tá acontecendo. Usando `range`: o range inicializa um array de x tamanho — vamos imaginar um array de tamanho 3, `[1, 2, 3]` — e a gente percorre esse array com um for loop. Os valores vão sendo acumulados num resultado.

A mesma função dá pra fazer de maneira recursiva, e o código fica até um pouco mais simples:

```python
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)
```

Recebendo um 3, por exemplo: 3 é multiplicado pelo resultado de `factorial_recursive(2)`, que é 2 vezes `factorial_recursive(1)`, que finalmente cai no caso base (`n <= 1`) e retorna 1. Aí a função "sobe" de novo, efetivamente realizando as mesmas operações que a versão iterativa fez — só que, na maneira tradicional como isso roda em Python, de forma um pouco menos eficiente.

Na iteração, a gente alocou um array. Na recursão, a gente fez chamada de função, passando parâmetro, chamada de função, passando parâmetro, chamada de função, passando parâmetro — caiu no caso base, voltou, voltou, voltou.

## Por que a recursão "espera": a call stack

O momento em que eu pego o 3 e multiplico pelo resultado do fatorial de 2, meu programa não pode simplesmente continuar dessa linha — ele não pode perder o valor de `n = 3`, porque o resultado da expressão depende do retorno de `factorial_recursive(2)`. Então ele começa a empilhar valores numa **call stack**.

Durante o runtime de um programa, ele tem o que a gente chama de **stack** e **heap** — conceitos importantes. A stack é uma **estrutura de dados**: você pode alocar uma stack se quiser, não tem nada de proibido nisso. E na call stack vão sendo empilhados os métodos — como é uma pilha, ela segue o princípio **LIFO** (last in, first out): o último que chegou é o primeiro a ser resolvido.

Na primeira chamada, a call stack tem `factorial_recursive(3)`. Depois `factorial_recursive(2)`. Depois `factorial_recursive(1)`, que finalmente resolve e retorna 1. Esse 1 é multiplicado pelo 2 (segunda chamada, de baixo para cima), dando 2; esse 2 é multiplicado pelo 3, dando 6. O método encerra retornando 6 e desalocando a call stack que foi alocada.

O problema de linguagens como Python é que essa alocação de coisas na call stack, por causa de como a linguagem foi desenhada e roda, acaba sendo quase sempre mais lenta do que alocar o array na mão e percorrê-lo com um for loop. Numa linha de raciocínio até um pouco rasa, então, a gente conclui que iteração é mais eficiente e menos complexa que recursão.

## A virada: stack é só estrutura de dados, e nada te impede de alocar a sua

Só que a stack é uma estrutura de dados — é só código. Tudo ali é linha de código, alocação de memória. Você sabe alocar memória. Nada impede você de alocar a sua própria stack, de alocar seus próprios recursos na memória.

Isso leva a dois nomes grandes na computação: **Alonso Church** e **Alan Turing**. Church e Turing deram as bases computacionais de basicamente tudo que a gente usa hoje. Juntando os dois nomes, tem-se a **Church-Turing thesis** (tese de Church-Turing) — daria outro vídeo inteiro pra falar sobre o *lambda calculus* de Church e a *Turing machine* de Turing.

Você provavelmente já ouviu falar de Alan Turing e de Turing machines, e provavelmente sabe o que significa uma linguagem ser **Turing complete**: significa que essa linguagem, dado tempo suficiente, pode computar tudo aquilo que pode ser computado. A tese de Church-Turing estabelece uma certa equivalência aqui: lambda calculus e Turing machines — ambos podem computar tudo o que pode ser computado.

O ponto a que eu quero chegar: todas as linguagens de programação que você usa no seu trabalho são Turing complete. Não existe, no seu dia a dia, nenhuma linguagem de uso geral que não seja Turing complete (HTML puro, CSS puro à parte). Uma decorrência natural disso é que **toda recursão pode ser convertida em iteração, e vice-versa** — todo algoritmo recursivo pode ser convertido num algoritmo iterativo que não utiliza recursão.

Intuitivamente a gente já sabe disso: os processadores, as CPUs, foram feitos para executar instruções sequenciais. Se você der as instruções corretas, na sequência correta, ela executa sem problema. É só uma questão de organizar em forma iterativa as instruções que seriam dadas de maneira recursiva.

## Convertendo fatorial recursivo em iterativo (com stack manual) em Python

O que significa que, quando eu tenho um algoritmo recursivo em mãos, eu posso identificar o que está sendo empilhado na call stack e alocar a minha própria stack. Em Python:

```python
def factorial(n):
    if n <= 1:
        return 1

    stack = []
    for num in range(n, 1, -1):
        stack.append(num)

    result = 1
    while stack:
        result = result * stack.pop()

    return result

print(factorial(4))  # 24
```

A stack é preenchida com `[3, 2, 1]` (para `n=4`, os valores de `n` até `2`, decrescendo — mais o próprio `n`). Depois, dando `pop` (LIFO: de cima pra baixo), a gente vai multiplicando: primeiro o valor do topo (o último empilhado) pelo resultado acumulado, e assim por diante, até o resultado final de 24.

Convertemos, de fato, um algoritmo recursivo num algoritmo iterativo, na mesma linguagem. Isso deve ser mais rápido, mais eficiente, alocar menos memória — porque Python não faz otimizações decentes em algoritmos recursivos. Mas isso não significa que otimizar recursão seja impossível de ser feito de forma alguma — só que não em Python.

## Olhando o assembly: call vs. jump

Trazendo a função fatorial recursiva em C para um compiler explorer, sem nenhuma otimização do compilador: dá pra ver um `cmp` (compare) correspondente ao `if`, e um jump para o fim da função (o `return`) quando a condição de parada é satisfeita. A parte que faz a recursão de fato tem um método `call` no final da função — se ela não fez o jump pra fora (não caiu no caso base), ela chama a si mesma via `call`.

Substituindo pelo fatorial iterativo (for loop acumulando o resultado): tem uma comparação que dá jump pra fora quando o loop termina, e, caso a condição não seja satisfeita, ele executa a linha do acumulador e dá um jump **de volta** pro início do loop.

Em essência, `call` e `jump` são ambos controle de fluxo — são "gotos". A diferença é que o `call` também administra a stack. **Recursão é basicamente jumps, é basicamente gotos — uma iteração cuja stack é administrada pelo compilador**, não por você. Na maioria dos casos você não quer lidar com a sua própria estrutura de dados, com a sua própria stack — você torce pro compilador lidar com isso.

## Tail Call Optimization (TCO)

Existe um caso em várias linguagens chamado **tail call optimization (TCO)** — que, salvo engano, não é possível em Python. TCO permite que alguns tipos de função recursiva **não acumulem** na call stack, evitando a alocação de memória correspondente.

TCO só é possível quando a **última coisa** executada numa função recursiva é a chamada de outra função (a própria, no caso da recursão). No `factorial_recursive` original, a última coisa executada não é a chamada recursiva — é a **multiplicação** de `n` pelo resultado da chamada de função. Por isso não dá pra fazer TCO nessa versão, mesmo pensando "a última coisa é a chamada de função".

Dá pra reescrever de forma que TCO seja possível, usando uma função helper com um acumulador:

```c
int factorial_helper(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_helper(n - 1, n * acc);
}

int factorial_recursive(int n) {
    return factorial_helper(n, 1);
}
```

Aqui, a última coisa que `factorial_recursive` faz é chamar `factorial_helper` — e a última coisa que `factorial_helper` faz é chamar a si mesma. Como toda a informação necessária para a próxima chamada já foi passada como parâmetro, não é preciso empilhar nada na call stack: essa chamada só precisa dar um jump, e nunca vai precisar "voltar" pro estado anterior, porque não há mais nenhum cálculo pendente depois dela.

Trocando a flag de otimização do compilador (nível 3), o assembly gerado fica irreconhecível para quem (como o autor) não entende profundamente de assembly — mas, em teoria, é possível que o compilador não empilhe nada na call stack nesse caso, e que esse código recursivo não seja nem menos eficiente, nem (dependendo do algoritmo) mais complexo. Nenhuma dessas duas coisas — "recursão é sempre menos eficiente" e "recursão é sempre mais complexa" — precisa necessariamente ser verdade, embora em muitos casos seja.

## Recursão e iteração são duas faces da mesma moeda

Recursão e iteração são duas faces da mesma moeda — isso é praticamente óbvio, não tem como ser diferente: em algum lugar, ou você está alocando as estruturas de dados, ou você está usando estruturas já pré-alocadas (a call stack, o heap do programa, ou o que quer que seja). Em máquinas de Turing, não existe outra forma.

Mesmo assim, existem algoritmos que se traduzem muito melhor de forma recursiva do que iterativa, e vice-versa — depende do contexto da linguagem que você tá usando, e qual escolha faz sentido.

## In-order traversal: recursivo elegante vs. iterativo com stack manual

Exemplo com uma árvore binária (`TreeNode`). Um in-order traversal em ordem, de forma recursiva:

```python
def in_order_traversal_recursive(root):
    if root:
        in_order_traversal_recursive(root.left)
        print(root.val)
        in_order_traversal_recursive(root.right)
```

In-order é um algoritmo que resolve primeiro o máximo possível à esquerda, depois sobe, depois olha se tem algo à direita — produzindo, no exemplo dado, a sequência 3, 2, 4, 1, 5. Essa forma recursiva é elegante: "procure sempre o máximo à esquerda; se não houver nada à esquerda, imprima o elemento; abra o nodo à direita".

A versão iterativa, com stack manual, é mais verbosa:

```python
def in_order_traversal_iterative(root):
    stack = []
    current = root
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val)
        current = current.right
```

O `current` desce sempre que possível pela esquerda, empilhando cada nó visitado; quando não há mais nada à esquerda, dá `pop` no topo da stack, imprime, e passa a considerar a subárvore à direita desse nó. Funciona, mas — nas palavras do autor — não é tão mais fácil nem tão mais legível quanto o algoritmo recursivo equivalente.

O ponto: existem algoritmos mais expressivos e mais fáceis de escrever de forma recursiva, assim como existem algoritmos mais bem expressados de forma iterativa.

## Fechamento: function call overhead, otimizações de compilador, stack overflow

Existe **function call overhead**: chamar uma função pode ter um certo custo, principalmente em linguagens sem TCO, ou em funções que não fazem uma tail call de fato (como o `in_order_traversal_recursive` acima, que ainda tem trabalho pendente — o `print` e a chamada à direita — depois da chamada recursiva à esquerda). Mas, na versão iterativa, você também precisa alocar uma estrutura de dados — então talvez compense um lado, talvez o outro.

Fica o questionamento: o que significa **stack overflow** (o nome do site, não o erro)? E fica o convite a considerar sempre as otimizações que o compilador pode ou não fazer por você.

Esse vídeo foi pra desmistificar um pouco a dicotomia recursão versus iteração — mostrando que é mais complicado, ou talvez mais simples, do que parece. Ele já foi tema de entrevista de emprego do autor: pediram para converter um algoritmo resolvido de forma recursiva em iterativo, e o autor não sabia, até aquele momento, que todo método recursivo pode ser convertido em iterativo — foi trabalhoso fazer a conversão sem saber exatamente o que esperar.

*(Trecho final do vídeo é material promocional de um curso de estruturas de dados e algoritmos do autor, incluindo depoimentos de alunos — omitido aqui por não ser conteúdo técnico relevante para a wiki.)*
