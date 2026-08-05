# Binary Search em 5 Minutos

Binary search é um algoritmo de busca em um array ordenado. Como que esse algoritmo funciona? A performance dele é O(log n) — melhor do que O(n). A gente não precisa olhar todos os elementos de um array para identificar se um item está lá ou não, e a gente só consegue isso porque esse array sempre está ordenado. Se ele não estiver ordenado, o binary search não funciona.

## Busca linear vs. binary search

Se a gente quisesse fazer uma busca linear pelo item nove nesse array, a gente ia olhar: -1 não é, 0 não é, 3 não é, 5 não é, nove é o elemento. A gente efetivamente percorreu em O(n).

Como o binary search é um algoritmo mais eficiente — já que ele só funciona em arrays ordenados — a gente olha direto no meio. O meio desse array é o três. Como o nove é maior do que o três, a gente corta tudo que está à esquerda do três e olha no novo array no meio. O meio desse novo array é o nove. A gente efetivamente encontrou ele em dois passos, em O(log n), ao invés de O(n). Não precisou percorrer tudo.

## Por que two pointers em vez de recursão com recriação de array

Criar e recriar array recursivamente seria muito caro computacionalmente. Existe uma implementação com two pointers para fazer binary search em que, ao invés de ficar recriando array e chamando função recursivamente, a gente inicializa um ponteiro na esquerda e um ponteiro na direita — cada um desses ponteiros aponta para um índice.

O índice da esquerda é o zero, porque é o primeiro do array. O da direita é o cinco (o último índice). A metade seria 2.5, que arredondado vira dois. A gente olha o elemento nessa posição — o três — em busca do nosso target (nove). O três é menor do que o nove, então a gente move o ponteiro da esquerda para uma posição depois da metade: a nova metade agora é o índice quatro. O elemento nessa posição é o nove — encontramos.

## Implementação

Dois ponteiros, `left` e `right`. `left` inicializa em 0. `right` inicializa em `nums.length - 1` (o último elemento). Enquanto `left` for menor ou igual a `right` — quando eles cruzarem, o algoritmo acabou.

O meio é `(left + right) // 2` (divisão inteira — em Python isso já funciona; em outras linguagens é preciso tomar cuidado com overflow ao somar `left + right`).

- Se `nums[mid]` for maior do que o target, o `right` se move uma posição antes do meio (`right = mid - 1`) — porque eliminamos a parte à direita que não precisa mais ser olhada.
- Se `nums[mid]` for menor do que o target, o `left` se move uma posição depois do meio (`left = mid + 1`) — o target está mais pra frente.
- Se não for nem maior nem menor, por definição é igual — retorna `mid`.

Por padrão o LeetCode quer que se retorne `-1` quando o elemento não é encontrado.

```python
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid

    return -1
```

Essa é a implementação correta de binary search em Python. Resolvido no LeetCode em menos de cinco minutos.

## Nota final do autor sobre o curso

O autor menciona ter um curso de estruturas de dados e algoritmos, onde binary search também é ensinado (junto com outros tópicos), hospedado com link na descrição do vídeo original — incluindo a oferta de enviar o curso de graça por e-mail para quem não tem condições de pagar.
