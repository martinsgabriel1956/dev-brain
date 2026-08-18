# Recursão em JavaScript: Fatorial e Fibonacci

Na programação, a recursão pode ser definida como uma função que chama ela mesma. É como se você tivesse um sonho dentro de um sonho, ou como uma boneca russa, onde você precisa abrir todas as bonecas uma dentro da outra até chegar na menor de todas — e depois faz a mesma coisa de trás para frente para voltar elas ao formato original.

## Função iterativa vs. função recursiva

Para entender a função recursiva, primeiro a gente precisa entender a diferença entre a função iterativa e a função recursiva.

A função iterativa é uma função que usa o loop, como o `for` ou `while`, para repetir uma série de instruções até que uma certa condição seja atendida.

Por outro lado, a função recursiva é uma função que chama ela mesma até uma condição ser atendida. Ou seja, ela divide o problema principal em problemas menores, e no final é como se ela juntasse todos os resultados dos problemas menores para retornar o resultado do problema principal.

Só falando assim fica difícil de entender, então vamos a um exemplo prático.

## Exemplo: fatorial

Vamos supor que a gente precisa criar uma função em JavaScript que calcula o fatorial de um número.

Na matemática, o fatorial é representado por um número positivo seguido por um ponto de exclamação, e o resultado do fatorial é a multiplicação de todos os números positivos de 1 até n. Ou seja:

- O fatorial de 5 (`5!`) seria `5 × 4 × 3 × 2 × 1`, que dá 120.
- O fatorial de 3 (`3!`) seria `3 × 2 × 1`, que dá 6.

Vamos criar essa função das duas formas — iterativa e recursiva — assim fica mais fácil entender a diferença entre elas.

### Forma iterativa

Na forma iterativa, criamos a função `fatorial` que pega `n` como argumento. Dentro dela, criamos uma variável `resultado` com valor 1, porque esse é o valor mínimo que o fatorial pode ter. Depois criamos o loop `for` da função: enquanto o contador `i` for menor ou igual ao número que a gente quer calcular o fatorial, o loop continua, e dentro dele multiplicamos o valor do `resultado` pelo próximo número da contagem.

Ou seja, se pedirmos para a função calcular o fatorial de 3, esse loop vai fazer a multiplicação `1 × 2 × 3`, que retorna o resultado 6.

```javascript
function fatorial(n) {
  let resultado = 1;
  for (let i = 1; i <= n; i++) {
    resultado *= i;
  }
  return resultado;
}
```

Essa é a função iterativa, que você provavelmente já usou diversas vezes.

### Forma recursiva

Agora, para criar a função recursiva, começamos de novo criando a função `fatorial` que pega `n` como argumento. Só que agora começamos criando uma condição: se `n` for igual a 1 ou igual a 0, a função retorna 1. Mas se `n` for maior que 1, a função retorna `n` multiplicado pela própria função, só que dessa vez levando `n - 1` como argumento.

```javascript
function fatorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }
  return n * fatorial(n - 1);
}
```

Ou seja, se a gente quiser calcular o fatorial de 5, a função vai verificar: "5 é igual a 1? Não." Então ela retorna `5 × fatorial(4)`. Isso chama a função de novo, mas dessa vez com `fatorial(4)`, que retorna `4 × fatorial(3)`. O `fatorial(3)` retorna `3 × fatorial(2)`. O `fatorial(2)` retorna `2 × fatorial(1)`. E por fim o `fatorial(1)` retorna 1.

O fatorial de 1 é o que a gente chama de **caso base**, porque é ele que coloca um fim no loop da função. Sem o caso base, a função recursiva entraria em um loop infinito, e isso não seria muito bom para o seu computador.

Então, quando a função recursiva chega no `fatorial(1)` e retorna 1, esse resultado é usado para completar o `fatorial(2)`, que tinha ficado pendente na memória do computador. Agora o `fatorial(2)` consegue a resposta, que vai ser `2 × 1 = 2`. Com isso, o `fatorial(3)` também consegue se completar, resultando em `3 × 2 = 6`. Com o resultado do `fatorial(3)`, é possível completar o `fatorial(4)`, que era `4 × fatorial(3)`, ou seja, `4 × 6 = 24`. E por fim, com o resultado do `fatorial(4)`, o `fatorial(5)` — que foi o problema que a gente queria resolver desde o começo — resulta em `5 × fatorial(4)`, ou seja, `5 × 24 = 120`.

E é assim que a função recursiva funciona: ela basicamente divide o problema em diversas partes e depois junta tudo para retornar a resposta do problema inicial.

## A analogia do poço

É como se você quisesse pegar água de um poço. Você começa com um balde na superfície e tem que baixar ele até o fundo do poço, passando por todo o percurso. Lá no fundo você pega a água — que nesse caso seria o caso base da função recursiva — e então você traz o balde para cima de novo, fazendo todo o caminho de volta, até que o balde retorna cheio de água, ou seja, com o resultado esperado.

## As duas partes obrigatórias de toda função recursiva

Toda função recursiva tem duas partes obrigatórias:

1. **Caso base** — é onde a gente diz para a função quando ela deve parar. O caso base é muito importante porque é ele que vai impedir que a função fique rodando infinitamente.
2. **Chamada recursiva** — é a parte da função onde ela chama ela mesma. É isso que torna a função recursiva.

Na função `fatorial` recursiva: a condição que verifica se `n` é 0 ou 1 é o caso base; a parte que retorna `n * fatorial(n - 1)` é a chamada recursiva.

## Exemplo: sequência de Fibonacci

Agora que você já entendeu melhor como a função recursiva funciona, vamos para um exemplo mais famoso em que a recursividade também pode ser aplicada: a sequência de Fibonacci.

A sequência de Fibonacci é uma sequência de números onde cada número é a soma dos dois números anteriores. A sequência começa com 0 e 1 e segue assim: `0, 1, 1, 2, 3, 5, 8...` (0+1=1, 1+1=2, 1+2=3, e assim por diante).

A sequência de Fibonacci é interessante porque ela aparece em muitos lugares na natureza, como nas flores, nas ramificações das árvores, no formato das galáxias, e até na Monalisa. É um conceito matemático simples, mas que tem muitas aplicações práticas na programação.

Para criar uma função recursiva de Fibonacci, começamos incluindo `p` como argumento da função, onde `p` vai ser a posição de Fibonacci que a gente quer descobrir. Ou seja, se `p` for 5, a função tem que retornar o quinto número da sequência, que é 3.

Criamos uma condição que verifica se `p` é igual a 1 — se esse for o caso, a função retorna 0, porque o primeiro elemento da sequência é 0. Agora, se esse não for o caso e `p` for igual a 2, a função retorna 1, já que esse é o segundo elemento da sequência. Ou seja, essas duas condições são os casos base da função recursiva.

Agora falta criar a chamada recursiva, e é aqui que as coisas ficam mais complicadas: a função retorna `fibonacci(p - 1) + fibonacci(p - 2)`. O que isso quer dizer é que a função retorna a soma dos dois números anteriores da sequência — e é exatamente isso que a gente quer.

```javascript
function fibonacci(p) {
  if (p === 1) {
    return 0;
  }
  if (p === 2) {
    return 1;
  }
  return fibonacci(p - 1) + fibonacci(p - 2);
}
```

Se a posição da sequência que a gente quer descobrir for 3, por exemplo, a função pergunta: "3 é igual a 1? Não. 3 é igual a 2? Não." Então retorna `fibonacci(3 - 1) + fibonacci(3 - 2)`, ou seja, retorna o número na posição 2 mais o número na posição 1 da sequência de Fibonacci.

Isso chama a função de novo, só que dessa vez com `p` igual a 2 e 1. Em `fibonacci(2)`, a função pergunta: "2 é igual a 1? Não. 2 é igual a 2? Sim." Então a função retorna 1. Já no caso do `fibonacci(1)`, a função pergunta: "1 é igual a 1? Sim." Então retorna 0 — e essa é a mágica dos casos base.

Voltando para `fibonacci(3)`, onde a função tinha chamado `fibonacci(2)` e `fibonacci(1)`: `fibonacci(2)` retorna 1 e `fibonacci(1)` retorna 0. Agora é só somar `1 + 0`, que dá 1. Ou seja, o número da terceira posição na sequência de Fibonacci é 1.

Agora, se a gente quer saber `fibonacci(5)`, por exemplo, ela vai chamar as funções `fibonacci(4)` e `fibonacci(3)`. O `fibonacci(4)` chamaria `fibonacci(3)` e `fibonacci(2)`, e assim por diante, até chegar nos casos base, onde as funções `fibonacci(1)` ou `fibonacci(2)` são chamadas e retornam 0 e 1, respectivamente. E então as respostas das funções com o caso base completam todas as funções que estavam pendentes, de trás para frente, até voltar para a função `fibonacci(5)`, que retorna 3.

Ou seja, quando você usa uma função recursiva, ela chama ela mesma repetidamente até chegar nos casos base que você definiu — ela vai criando várias cópias dela mesma, e enquanto não chegar nos casos base, as funções que foram chamadas ficam pendentes na memória.

## Recursiva vs. iterativa: trade-offs

Basicamente, as diferenças entre a função iterativa e a recursiva são:

- Na grande maioria dos casos, a função recursiva tende a ser mais lenta, já que ela acaba criando várias cópias dela mesma. De certa forma isso acaba consumindo mais memória que a função iterativa, e consequentemente deixando o programa mais lento.
- A vantagem da função recursiva seria que, em alguns casos, ela pode simplificar e facilitar a compreensão de um problema.

Sendo assim, em geral, as funções iterativas são mais eficientes, porém mais complexas, e as funções recursivas em geral são mais lentas, porém mais simples de escrever.
