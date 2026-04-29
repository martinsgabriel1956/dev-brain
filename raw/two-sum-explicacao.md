# Two Sum — Explicação Completa

## O Problema

Dado um array `nums` e um `target`, retornar os **índices** de dois números que somam ao target.

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # porque nums[0] + nums[1] = 2 + 7 = 9
```

---

## A Ideia Central: Complemento

Para cada número `i` no array, a pergunta é:
> "Já vi o **complemento** de `i` (ou seja, `target - i`) antes?"

Se sim → encontramos o par. Se não → guardo `i` no mapa para consulta futura.

---

## Solução em Python — Linha a Linha

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasher = {}
        # Dicionário que vai mapear: valor → índice
        # Ex: { 7: 0 } significa "vi o número 7 no índice 0"

        for idx, i in enumerate(nums):
            # enumerate dá o índice (idx) e o valor (i) juntos

            if hasher.get(i) is not None:
                # Pergunta: o valor atual (i) já foi registrado como complemento de alguém?
                # Se sim, hasher[i] tem o índice do número que precisava de mim
                return [hasher.get(i), idx]
                # Retorna: [índice do número que "precisava" do atual, índice do atual]

            hasher[target - i] = idx
            # Registra: "o complemento de i (target - i) precisa do índice idx"
            # Ou seja: "se alguém valer (target - i) no futuro, o parceiro dele está aqui"
```

---

## Simulação Visual

`nums = [2, 7, 11, 15]`, `target = 9`

| Iteração | idx | i | hasher antes | i está no hasher? | hasher depois |
|---|---|---|---|---|---|
| 1 | 0 | 2 | `{}` | ❌ | `{7: 0}` |
| 2 | 1 | 7 | `{7: 0}` | ✅ → retorna `[0, 1]` | — |

**Iteração 1:** vemos o número `2`. O complemento é `9 - 2 = 7`. Gravamos `hasher[7] = 0`.

**Iteração 2:** vemos o número `7`. Checamos se `7` está no hasher → **está!** O índice guardado é `0`. Retornamos `[0, 1]`.

---

## O Truque Elegante

A chave da solução é o que fica no `hasher`:

- **A chave** é o **complemento** (`target - i`) — o valor que estamos *esperando encontrar*
- **O valor** é o **índice** de quem fez esse "pedido"

Então quando um número novo chega, basta verificar se *ele mesmo* é o complemento esperado por alguém.

---

## A Lógica Produtor/Consumidor

O elemento atual não sabe quem é seu par — ele só sabe o que está **faltando**. Então ele deixa registrado no hash map: *"preciso de X"*. Quando X aparecer nas próximas iterações, X olha pro hash map, se vê lá, e diz: *"sou eu que você estava esperando"*.

```
Iteração passada  →  produz um "pedido" no hash map  (hasher[target - i] = idx)
Iteração futura   →  consulta se ela mesma é pedida   (hasher.get(i))
```

O encontro sempre acontece no **segundo elemento do par** — é ele que olha para trás, encontra o recado, e encerra o algoritmo.

---

## Exemplo com um caso que demora mais

`nums = [3, 5, 1, 8]`, `target = 9`

| Iteração | i | Está no hasher? | Armazena |
|---|---|---|---|
| 1 | 3 | ❌ | `hasher[6] = 0` ("preciso de um 6") |
| 2 | 5 | ❌ | `hasher[4] = 1` ("preciso de um 4") |
| 3 | 1 | ❌ | `hasher[8] = 2` ("preciso de um 8") |
| 4 | 8 | ✅ `hasher[8] = 2` | retorna `[2, 3]` |

O `8` da iteração 4 chegou e encontrou o "recado" que o `1` deixou na iteração 3 — mesmo sendo duas iterações completamente diferentes.

---

## Um Detalhe Importante

O check `is not None` (em vez de simplesmente `if hasher.get(i)`) é necessário porque o índice `0` é falsy em Python. Se o complemento estiver no índice `0` e você checar com `if hasher.get(i):`, vai ignorar esse caso. Usar `is not None` é a forma correta.

---

## Complexidade

| | Complexidade |
|---|---|
| **Tempo** | O(n) — uma passagem no array |
| **Espaço** | O(n) — pior caso, guarda n-1 entradas no hash map |

A abordagem ingênua seria dois `for` aninhados → O(n²). Essa solução troca espaço por tempo, o que é quase sempre o trade-off certo aqui.

---

## Solução Correta em TypeScript

```typescript
function twoSum(nums: number[], target: number): number[] {
    const map = new Map<number, number>(); // valor → índice

    for (let idx = 0; idx < nums.length; idx++) {
        const current = nums[idx];           // valor atual
        const complement = target - current; // o que estamos procurando

        if (map.has(complement)) {
            return [map.get(complement)!, idx]; // par encontrado
        }

        map.set(current, idx); // guarda: "vi esse valor nesse índice"
    }

    return []; // nenhum par encontrado
}
```

### Diferença entre Python e TypeScript

Repara que a lógica de armazenamento é ligeiramente diferente — mas o conceito é idêntico:

| | Python | TypeScript |
|---|---|---|
| Chave no map | `target - i` (complemento) | `i` (valor atual) |
| Consulta | `hasher.get(i)` | `map.has(target - current)` |
| Efeito | mesmo resultado | mesmo resultado |

As duas abordagens funcionam — só invertem *quando* a subtração acontece. O que importa é que o map sempre consegue responder: *"já vi o complemento antes?"*
