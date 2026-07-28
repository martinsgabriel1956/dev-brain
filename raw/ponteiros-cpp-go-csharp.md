# Ponteiros em C++, Go e C# — Stack, Heap e Smart Pointers

Fala pessoal, hoje a gente vai entender um pouco mais sobre ponteiros. A gente vai ver exemplos em três linguagens: C++, Go e C#. A ideia é ver como cada linguagem trabalha com ponteiros e ir descendo o nível aos poucos para ver como são ponteiros de verdade lá embaixo, na memória.

Se você já trabalha com Go, você já deve ter uma noção de como ponteiros funcionam. Você pega o endereço de uma variável, desreferencia o ponteiro — isso já faz parte da sua rotina. Mas em Go o Garbage Collector tá sempre ali te protegendo. Você não precisa se preocupar com quem libera memória, ou quando libera, ou mesmo se alguém ainda tá usando aquele endereço que já não é mais válido. Então a gente usa ponteiros, mas nunca precisa ficar pensando "será que eu dei free nisso" ou mesmo "será que alguém ainda tá usando essa memória" — isso simplesmente não existe pra gente.

E se você trabalha com C#, a ideia é a mesma. O C# até deixa usar ponteiro com `unsafe`, mas no dia a dia quase ninguém faz isso. A gente trabalha com referências gerenciadas, e o garbage collector cuida de tudo pra gente. Então quando você cria um objeto e passa ele para um método, aquele método tá mexendo no mesmo objeto, não é uma cópia. Se ele muda uma propriedade ali dentro, quando a execução volta o objeto já tá diferente, e você nunca precisou pensar em endereço de memória para nada disso.

E é por isso que nesse vídeo a gente vai usar C++ para explicar, porque em C++ não tem garbage collector rodando por baixo, não tem referência gerenciada. Ele te dá um endereço, te deixa mexer na memória direto, e se você fizer alguma coisa errada o programa simplesmente quebra. Claro, existem ferramentas que facilitam a vida e a gente vai até falar delas mais pra frente, mas o C++ permite chegar na memória sem nenhuma camada ali no meio. Por isso ele é perfeito para entender como ponteiros funcionam de verdade. Então bora lá.

## O que é um ponteiro

Uma variável comum armazena um dado — um número, um texto, por exemplo. Um ponteiro também é uma variável, só que o dado que ele armazena é o endereço de uma outra variável. Ele aponta para onde o valor tá na memória.

### C++

```cpp
int idade = 25;
int *ptr = &idade;

std::cout << idade << std::endl; // 25
std::cout << ptr << std::endl;   // endereço de memória (decimal)
std::cout << *ptr << std::endl;  // 25 (dereferência)

*ptr = 30;
std::cout << idade << std::endl; // 30
```

A gente começa criando uma variável chamada `idade` com valor 25. Na linha de baixo a gente cria um ponteiro chamado `ptr` e armazena nele o endereço da variável `idade`. Agora a gente tem duas formas de chegar no mesmo dado: pela variável `idade` diretamente, ou pelo ponteiro `ptr`, que sabe onde `idade` tá na memória.

Quando a gente imprime `idade`, aparece 25. Quando a gente imprime `ptr`, aparece o endereço de memória, aquele número decimal. E quando a gente dereferencia o ponteiro — ou seja, pede para ele ir até aquele endereço e trazer o que tá lá — a gente recebe 25 de novo.

Agora olha o que acontece: a gente usa o ponteiro para mudar o valor naquele endereço para 30. E quando a gente imprime a `idade` de novo, 30. A gente não tocou na variável diretamente, a gente foi pelo ponteiro, alterou o conteúdo daquele endereço, e a variável refletiu a mudança, porque no fundo é o mesmo lugar na memória.

### Go

```go
idade := 25
ptr := &idade

fmt.Println(idade) // 25
fmt.Println(ptr)    // endereço
fmt.Println(*ptr)   // 25

*ptr = 30
fmt.Println(idade) // 30
```

Em Go, ponteiros existem e os operadores são os mesmos. Olha como é parecido: a gente cria a variável `idade` com valor 25, pega o endereço dela e armazena em `ptr`. Mesma coisa que a gente fez em C++. Imprime o valor, imprime o endereço, dereferencia o ponteiro para acessar o valor, tudo igual. E aqui também a gente muda o valor pelo ponteiro para 30, e a variável `idade` reflete a mudança — mesmo comportamento.

A diferença entre Go e C++ não tá na sintaxe, tá no que acontece por trás.

### C#

Em C# a gente não trabalha com ponteiros diretamente, a gente trabalha com referências. Por baixo o conceito é parecido — as duas coisas te levam até um objeto — mas a referência é uma abstração. Você não vê endereço, não faz aritmética de ponteiro, não manipula nada. O runtime e o garbage collector cuidam disso. Você só usa o objeto.

```csharp
class Pessoa
{
    public int Idade;
}

void Modificar(Pessoa p)
{
    p.Idade = 30;
}

var pessoa = new Pessoa { Idade = 25 };
Modificar(pessoa);
Console.WriteLine(pessoa.Idade); // 30
```

A gente cria uma classe chamada `Pessoa` com uma propriedade chamada `Idade`. Na `main`, a gente instancia essa classe, coloca `Idade` como 25 e passa esse objeto pro método `Modificar`. Lá dentro o método modifica a `Idade` para 30. E quando a gente imprime de volta na `main`: 30. O método modificou o objeto original.

Isso acontece porque classes em C# são *reference type*. Quando a gente passou o objeto pro método, a gente não passou uma cópia, a gente passou a referência pro mesmo objeto na memória. É a mesma ideia que a gente viu em C++ e em Go — a mesma variável `idade` com 25 virando 30. Só que aqui a gente não escreveu nenhum asterisco, nenhum "e comercial" (`&`). O C# fez tudo por baixo.

## Stack e Heap

Antes de continuar a gente precisa falar onde os dados ficam na memória. Toda variável precisa morar em algum lugar, e existem dois lugares: a **stack** e a **heap**. Isso não é exclusivo de C++ — Go e C# também separam memória entre stack e heap. O que muda é quem limpa a heap depois.

A stack guarda as variáveis locais. Criou uma variável dentro de uma função, ela vai pra stack. A função terminou, tudo que estava ali é destruído automaticamente. Ela é rápida, mas o espaço é limitado.

A heap é a memória dinâmica. Você pede espaço, o dado fica lá, e ele só sai quando alguém liberar. Tem muito mais espaço que a stack, mas o "alguém que limpa" muda de linguagem para linguagem. Em C++ a gente limpa. Em Go e C# o garbage collector limpa pra gente.

```cpp
void exemplo() {
    int local = 10;       // stack — some quando a função termina

    int *ptr = new int(20); // heap — sobrevive ao fim da função
    // ...
    delete ptr;             // libera a heap manualmente
}
```

A primeira variável, `local`, recebe 10 e tá na stack. Quando a função `exemplo` terminar, ela deixa de existir. A segunda variável a gente cria com `new`. O `new` aloca um inteiro com valor 20 na heap e devolve o endereço desse espaço. A gente guarda esse endereço no ponteiro `ptr`. Só que, ao contrário da local, esse dado não some com o fim da função — ele continua lá na heap. Para liberar, você usa o `delete`. Se você esquecer essa linha, aquela memória fica presa enquanto o programa estiver rodando — isso é um *memory leak*.

Em C# e Go a gente quase nunca pensa nisso. A linguagem decide onde alocar para você.

- **Go**: se uma variável precisa sobreviver além da função, o compilador coloca ela na heap automaticamente. Isso se chama **escape analysis**.
- **C#**: a regra é mais direta — variáveis locais de *value types* (como `int` e `struct`) vão pra stack; *reference types* (como classes e arrays) vão pra heap.

A stack se limpa sozinha quando a função termina, e o garbage collector cuida de liberar o que não tá sendo mais usado na heap.

## O bug clássico: retornar endereço de variável local

```cpp
int* criarValor() {
    int valor = 42; // stack, local à função
    return &valor;  // BUG: retorna endereço de algo que vai deixar de existir
}

int main() {
    int *ptr = criarValor();
    std::cout << *ptr << std::endl; // undefined behavior
}
```

A função `criarValor` cria uma variável local com o valor 42 e retorna o endereço dela. Na `main`, a gente chama essa função e guarda o endereço num ponteiro chamado `ptr`. O problema é que a variável local vivia na stack da função `criarValor`. Quando essa função terminou, aquele pedaço da stack foi liberado, mas o ponteiro ainda tá apontando pro mesmo endereço. Só que agora não tem mais nada válido ali. Se a gente tentar acessar, pode aparecer 42, pode aparecer lixo, pode dar segfault — não tem como saber.

Em C++ isso tem o nome **undefined behavior**. A linguagem não garante nada sobre o que vai acontecer. E o compilador até te dá um warning, mas compilar e rodar ele deixa.

Agora olha o mesmo padrão em Go:

```go
func criarValor() *int {
    valor := 42
    return &valor // funciona
}
```

Mesma coisa — variável local com valor 42 retornando o endereço. Em C++ isso deu um problema. Aqui funciona. O compilador do Go fez escape analysis: ele percebe que essa variável tá escapando da função e, ao invés de colocar ela na stack, coloca direto na heap. O endereço continua válido depois que a função termina.

E em C#, como os *reference types* já vivem na heap, o GC garante que nada é liberado enquanto tiver referência apontando. Esse tipo de bug simplesmente não existe no uso normal.

## Gerenciamento manual em C++: o problema de verdade

Na parte anterior a gente viu que retornar o endereço de uma variável local dá problema — o ponteiro fica apontando para um lugar que não existe mais. Então como a gente cria um dado que sobrevive além da função em C++? A gente já viu `new` e `delete` rapidamente na parte da stack e heap. Agora vamos olhar com mais cuidado, porque o problema de verdade do gerenciamento manual não é o caso simples. O problema aparece quando o código fica mais complexo.

```cpp
int* criarValor() {
    int *ptr = new int(25); // heap
    return ptr;
}

int main() {
    int *ptr = criarValor();
    std::cout << *ptr << std::endl; // 25
    delete ptr;
    ptr = nullptr;
}
```

Mesma ideia de antes: uma função que cria um valor e retorna um ponteiro. Só que agora, ao invés de criar uma variável local na stack, a gente usa `new` para alocar um inteiro com valor 25 na heap. O `new` devolve o endereço e a gente retorna ele. Como tá na heap, o dado não morre com a função. Na `main`, dereferencia e imprime 25.

Toda vez que você usa `new`, precisa usar `delete`. Se esquecer, aquele espaço fica ocupado enquanto o programa rodar. E depois do `delete`, a gente seta o ponteiro para `nullptr`. Por quê? Porque depois do `delete` o endereço ainda tá lá no ponteiro, mas a memória já foi liberada. Se alguém tentar usar esse ponteiro, vai acessar uma memória que não é mais válida. Setar para `nullptr` deixa explícito que ele não aponta mais para nada.

```cpp
void processar() {
    int *dados = new int[1000]; // heap

    // ... processamento que pode lançar exceção antes do delete

    delete[] dados;
}
```

Agora olha o problema de gerenciar memória na mão. A gente aloca um array de 1000 inteiros na heap com `new`. No final da função a gente libera com `delete`. Até aqui tudo certo. Mas se no meio do processamento acontece um erro e a função retorna antes de chegar no `delete`, aquela memória nunca vai ser liberada. É um *memory leak*. Uma exceção no meio do caminho — mesma coisa. Qualquer caminho que saia da função antes do `delete` é um leak.

Em C# você também usa `new` para criar objetos, mas não existe `delete` — o garbage collector libera a memória quando o objeto já não é mais referenciado. Em Go você cria slice com `make` e pronto, o garbage collector cuida do resto. É por isso que as pessoas dizem que C++ é difícil, mas o C++ moderno tem ferramentas para evitar a maioria desses problemas.

## Smart pointers: `unique_ptr` e `std::move`

Em C++ moderno você quase nunca usa `new` e `delete` diretamente. Você usa smart pointers, e o principal deles é o `unique_ptr`.

```cpp
std::unique_ptr<int> criarValor() {
    return std::make_unique<int>(42);
}

int main() {
    auto ptr = criarValor();
    std::cout << *ptr << std::endl; // 42
    // sem delete — destruído automaticamente ao sair de escopo

    auto ptr2 = std::move(ptr); // transfere ownership
    // ptr agora é nullptr, ptr2 é o novo dono
}
```

Mesma ideia de antes: uma função que cria um valor na heap e retorna. Só que, ao invés de usar `new` direto, a gente usa `make_unique`, que cria um inteiro com valor 42 e coloca dentro de um `unique_ptr`. Esse `unique_ptr` é o dono daquele dado. Na `main`, a gente recebe esse ponteiro, dereferencia e imprime 42.

A diferença tá no que a gente **não** precisa fazer: não tem `delete`. Quando a variável `ptr` sai de escopo, o `unique_ptr` é destruído automaticamente e libera a memória junto — sem `delete`, sem risco de esquecer, sem memory leak.

Se você quer passar a posse para outro ponteiro, usa `std::move`. Isso transfere a ownership: `ptr2` vira o novo dono e `ptr` fica `nullptr`. A partir desse ponto, só `ptr2` é responsável por liberar aquela memória.

```cpp
struct Produto {
    std::string nome;
    double preco;

    Produto(std::string n, double p) : nome(n), preco(p) {
        std::cout << "Produto criado" << std::endl;
    }

    ~Produto() {
        std::cout << "Produto destruído" << std::endl;
    }
};

int main() {
    auto notebook = std::make_unique<Produto>("Notebook", 4500.0);
    std::cout << notebook->nome << " - " << notebook->preco << std::endl;
} // saída: Produto criado / Notebook - 4500 / Produto destruído
```

Um exemplo com uma struct: a gente tem um `Produto` com nome e preço. O construtor imprime quando o produto é criado. O destrutor imprime quando o produto é destruído. Na `main`, a gente cria um `unique_ptr` para um `Produto` chamado "Notebook" custando R$ 4.500. Imprime o nome e o preço, e a função termina.

A saída: "Produto criado", depois o nome e o preço, e por último "Produto destruído". A gente não chamou `delete` em nenhum lugar — o `unique_ptr` saiu de escopo e chamou o destrutor automaticamente.

## Conclusão

Go e C# resolvem pra gente o gerenciamento da memória com garbage collector. C++ não tem isso, mas para a maior parte do código que a gente escreve no dia a dia, o `unique_ptr` já cuida da liberação automaticamente. A regra é simples: deixe suas variáveis na stack sempre que possível, e quando realmente precisar de heap, use smart pointers. `new` e `delete` direto só em casos bem específicos.
