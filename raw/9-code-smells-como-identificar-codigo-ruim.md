# 9 Code Smells — Como Identificar que seu Código Pode Estar Piorando

> Transcrição de vídeo colada pelo usuário no chat (ASR bruto, sem pontuação, já em pt-BR — sem necessidade de tradução). Limpa e organizada em seções abaixo. Inclui um bloco de patrocínio (AUVP) que não é conteúdo técnico — mantido por fidelidade à transcrição, mas irrelevante para ingestão.

## O que é um code smell

Code smell é algo que pode indicar que o código talvez esteja deteriorando em qualidade. É importante notar a palavra "talvez": um código que apresenta uma dessas características não está garantidamente ruim a ponto de precisar de refatoração — não é um negócio determinístico. São sinais que não podem ser ignorados, e o vídeo ensina quais são esses sinais.

## O que é um bom código (opinião do autor)

Antes de definir sinais de deterioração, é preciso definir o que é um código bom. Existe a máxima de que "código bom é código que está rodando e seu cliente está pagando e dá dinheiro" — mas isso é considerado mentira pelo autor: todo desenvolvedor odeia trabalhar com código macarrônico e reclama dele todo dia, então código bom não é código que dá dinheiro.

Na opinião do autor, código bom é:

- **Compreensível** — dá para ler sem xingar o código.
- **Testável.**
- **Baixo acoplamento.**
- **Alta coesão.**
- **Modular.**
- **De fácil manutenção.**

Essas guidelines (opinião pessoal do autor) são a régua usada para julgar cada um dos nove smells a seguir.

## [Bloco de patrocínio — AUVP, não técnico]

Trecho publicitário sobre a AUVP ("maior e melhor escola de investimentos do Brasil"), usando por analogia os mesmos critérios de "boa carteira de investimentos" (diversificação global, adequação ao perfil de risco, foco em ativos de valor) espelhando os critérios de bom código do vídeo. Contém oferta comercial (análise de perfil, cartão black, garantia de reembolso). Não relevante para a wiki técnica.

## Os 9 Code Smells

### 1. Funções muito longas

Uma função muito longa pode estar funcionando e "entregando valor" sem causar problema aparente — mas existe uma tendência (não uma regra determinística) de funções muito longas serem difíceis de compreender. É difícil para um ser humano manter o contexto inteiro de uma função longa na cabeça: ela tende a não ser concisa, e um título que descrevesse tudo o que ela faz teria que ser um título enorme.

É raro que uma função muito longa seja compreensível e raro que seja testável — quem já tentou escrever teste para uma função muito longa sabe que é chato. A função também tende a ter "autoacoplamento": é uma parte só, inteiramente acoplada nela mesma, e provavelmente de manutenção difícil, como consequência de ser difícil de compreender e de testar.

**Recomendação:** não refatorar automaticamente só porque uma função está longa. Perguntar: ela é compreensível? É testável? É de fácil manutenção? Se sim às três, não há problema. Se não, é sinal de que pode valer a pena melhorar.

### 2. God Objects (classe Deus)

Classe que faz tudo — no exemplo dado, uma classe `SystemManagement`/`handleUser` que lida com autenticação, faz update no banco de dados e envia notificações, tudo junto.

Esse tipo de classe ainda costuma ser compreensível e "mais ou menos" testável — seria mais fácil testar as partes separadamente, mas isoladamente isso não é o problema mais grave. O problema real está em **acoplamento** e **coesão**: tudo está altamente acoplado, e coesão significa deixar coisas que devem estar juntas juntas e coisas que devem estar separadas separadas — autenticação junto de banco de dados junto de notificação não é coeso, não é modular, e não é fácil de manter. Uma mudança referente a banco de dados, ou a autenticação, ou a qualquer uma das partes, acaba afetando a classe inteira.

**Recomendação:** modularizar — não importa se em classes diferentes, funções diferentes ou módulos diferentes, o mecanismo específico é secundário. A técnica sugerida é **composição**: compor o objeto a partir de serviços menores (ex.: um serviço de autenticação, um serviço de banco de dados, um serviço de notificação) injetados na classe maior (ex.: `UserManagement`), de forma que cada serviço possa ser substituído sem afetar os outros.

### 3. DRY (Don't Repeat Yourself) — visão controversa do autor

O autor declara não ser "o maior fã do mundo" de DRY: repetição às vezes é aceitável, e às vezes é melhor repetir do que fazer uma abstração prematura. A avaliação depende do que exatamente está sendo repetido.

Exemplo dado como problemático: uma aplicação inteira "inundada" de chamadas a uma API espalhadas em vários lugares do código, cada uma validando manualmente se o status é 200, extraindo `response.json()`, tratando erro — um código quase duplicado em, por exemplo, 20 lugares diferentes.

- Se só existem 2 lugares fazendo esse tipo de requisição, não é considerado um problema.
- Se existem 3, 4, 5, 6 ou mais lugares, passa a ser considerado problemático.

O problema principal aqui não é compreensão nem testabilidade (ambas ainda ok) — é **manutenção**: se o endpoint muda, ou se o código de resposta esperado muda (de 200 para 201/202, por exemplo), é preciso mudar em todos os lugares duplicados em vez de corrigir em um único lugar, arriscando quebrar todos os pontos ao mesmo tempo.

**Recomendação:** abstrair o que é de fato muito repetido (ex.: uma "helper function" central para fazer o request e checar a resposta), não abstrair tudo preventivamente. Mesmo depois de abstrair, evitar detalhes "hard-coded" como a URL da API direto no código — preferir variável de ambiente (ex.: `.env`) ou, no mínimo, uma constante nomeada.

### 4. Condicional gigante

Exemplo: um método que calcula o preço de entrega com uma cadeia extensa de `if`/`elif` combinando método de entrega, país (Estados Unidos, Canadá, outros) e faixas de peso, cada combinação retornando um valor diferente (ex.: EUA + peso < 1 → custo 5; peso > 5 → custo 10; senão custo 20; repetido para Canadá e para o caso padrão).

Avaliação: "mais ou menos" compreensível, e a testabilidade é vista como o que pode efetivamente salvar esse tipo de código — testes cobrindo 100% dos casos e branches garantem que uma refatoração futura não quebre o comportamento. O problema principal apontado é compreensão e manutenção: uma indentação errada (o exemplo é em Python) pode quebrar tudo de forma sutil.

**Recomendação:** transformar a estrutura numa forma mais compreensível — de novo, o mecanismo é secundário (pode virar uma classe com polimorfismo, uma data class, tipagem forte, etc.). Uma solução simples ilustrada no vídeo é um dicionário/Hashmap de "base rates" por país (EUA, Canadá, default) com as faixas de preço — mais legível e explícito que a cadeia de `if`, embora ainda não perfeito (a ligação entre faixa de peso e valor ainda não fica totalmente explícita na estrutura). Um passo além seria uma estrutura que incorporasse as faixas de peso diretamente (ex.: uma classe ou combinação de mapa e classe).

### 5. Números mágicos (e "coisas mágicas" em geral, incluindo chaves de API)

Exemplo: `if user.age >= 16: grant_access()`, sem nenhuma explicação do porquê de 16. É comum ver isso "salvo" por um comentário em cima (ex.: "idade para tomar cerveja"), mas isso ainside é revelador do problema: o número cru não é autoexplicativo.

Dois problemas centrais:

- **Compreensão** — difícil saber o que aquele número representa sem contexto adicional (comentário ou não).
- **Manutenção** — com uma variável nomeada, dá para buscar no código inteiro onde aquele nome aparece; com um número mágico, a busca (`Ctrl+F` pelo número) é ambígua, porque o mesmo número pode aparecer em outros contextos sem relação nenhuma (ex.: buscar por `16` também acharia `1600`).

Exemplo de correção: transformar o `16` numa constante nomeada, como `LEGAL_BEER_BUYING_AGE_GERMANY = 16` (cenário hipotético: um site que vende cerveja na Alemanha, onde a idade mínima é 16). Se a lei mudar para 14, basta buscar por `LEGAL_BEER_BUYING_AGE_GERMANY` no código inteiro e alterar em um único lugar, sem risco de confundir com outros números iguais espalhados pelo código. A mesma lógica de "coisa mágica" vale para uma URL de API ou chave de API hard-coded, mencionadas no smell de DRY.

### 6. Feature Envy

Ocorre quando uma parte do código faz o trabalho de outra parte do código — acessando dados internos de outro objeto para fazer um cálculo que deveria ser responsabilidade desse outro objeto.

Exemplo dado (domínio de e-commerce: produtos e pedidos): uma classe `Order` (pedido) tem uma lista de itens (produtos); uma classe separada `OrderPrinter`, com um método `print_total`, itera sobre `order.items`, acessando o preço e o desconto de cada produto diretamente para calcular o total e imprimi-lo.

Isso é descrito como um problema grave porque a classe `Order` não expôs uma API própria para esse cálculo — quem deveria saber o total de um pedido é a própria classe `Order`, não a classe `OrderPrinter`. O código está acessando um atributo interno da classe `Order`, que por sua vez acessa um atributo interno da classe `Product` — acoplamento descrito como "altíssimo", "um nó", mais acoplado que espaguete.

Consequências:
- **Testabilidade:** para testar `print_total` é preciso montar um pedido inteiro com produtos — teste acaba testando várias camadas empilhadas.
- **Manutenção:** péssima — renomear um campo como `price` dentro de `Product` quebra uma classe a duas camadas de distância (`OrderPrinter` → `Order` → `Product`), sem relação direta de dependência declarada.

**Recomendação (solução):** mover a responsabilidade do cálculo para dentro da própria classe `Order`, com um método `get_total()` que retorna o valor total do pedido. A responsabilidade de saber o total de um pedido passa a ser exclusivamente da classe `Order`; `OrderPrinter` (se existir) fica só com a responsabilidade de imprimir o valor já calculado, sem acessar variáveis internas de outra classe para fazer cálculos que não são da sua alçada.

### 7. Grupos de dados (data clumps)

Ocorre quando várias variáveis que deveriam estar juntas são passadas soltas, separadamente, em vários lugares do código — exemplo: `nome`, `email` e `idade` sendo passados como três argumentos separados repetidamente ao criar um usuário, em vez de um único parâmetro tipado.

Coesão, nesse contexto, significa juntar o que pertence junto: nome, e-mail e idade dizem respeito a um mesmo conceito ("usuário"), então deveriam ser agrupados numa estrutura nomeada — o vídeo usa uma data class como exemplo, mas reforça que a estrutura específica (classe, tupla nomeada, struct, etc.) não é o ponto central; o que importa é o conceito de agrupar dados relacionados.

Benefício prático citado: se o conceito de usuário evolui (ex.: substituir o campo `idade` por `data_de_nascimento`, calculando a idade dinamicamente), a mudança é localizada na definição do tipo `Usuario` — todos os lugares que acessam `user.age` já vão acusar erro automaticamente, ao invés de ser necessário caçar manualmente todos os lugares do código que recebiam `nome`, `email`, `idade` como parâmetros soltos.

### 8. Comentários inúteis

Referência a um vídeo anterior do canal dedicado inteiramente a comentários úteis vs. inúteis (não detalhado de novo aqui). Exemplo dado: `if age > 16:` com um comentário acima dizendo "idade para tomar cerveja" — o comentário existir é, em si, um sinal de que o código não está suficientemente claro. Alternativa: nomear a variável diretamente (ex.: `idade_para_tomar_cerveja_alemanha = 16`), eliminando a necessidade do comentário.

Reforça que comentário pode ser, ele mesmo, um code smell indicando falta de compreensibilidade — mas o vídeo reconhece que às vezes um comentário genuinamente é necessário, não sendo uma regra absoluta.

### 9. Uso exacerbado de tipos primitivos (primitive obsession)

Exemplo: um "endereço de e-mail" tratado como `string` pura ao longo de toda a aplicação. Como uma string não carrega informação sobre se já foi validada ou não, o código acaba validando o mesmo dado repetidamente em vários lugares (ex.: checando se há um "@" dentro da função de enviar e-mail), sem garantia de que outros pontos do sistema estejam fazendo essa validação de forma consistente — ou revalidando de forma duplicada, ou confiando (sem garantia) num único ponto de validação central.

Exemplo mais forte citado: dinheiro. Em vez de passar dinheiro como string ou inteiro cru por todo o sistema, cria-se um tipo próprio (classe/tipo dedicado) para dinheiro: o valor é convertido para esse tipo assim que entra no sistema (validação na entrada) e convertido de volta ao formato necessário (string, inteiro, etc.) quando sai do sistema (cast na saída). A mesma lógica se aplica a e-mail: uma classe `Email`, validada no método de inicialização (ex.: `__init__` checando a presença do "@"), pode circular pelo resto do código com a garantia de que já foi validada.

Vantagens: reduz necessidade de revalidação repetida (ex.: a função de enviar e-mail não precisa validar de novo, porque o tipo recebido já garante isso por construção), reduz risco de manutenção inconsistente e de duplicidade de lógica de validação espalhada pelo código.

## Fechamento — como usar esses smells na prática

Os nove smells listados não são bugs nem indicam necessariamente um problema real na code base. A recomendação explícita do autor é não sair varrendo a code base inteira procurando cada um desses padrões para refatorar sem antes considerar o objetivo real que se quer atingir. Às vezes o código apresenta um desses smells mas a melhoria seria complicada demais para valer a pena; às vezes as guidelines dadas simplesmente não se aplicam bem ao cenário específico. A recomendação final é usar pensamento crítico, entender os **conceitos por trás** de cada smell (e não seguir os exemplos específicos dados no vídeo como regras rígidas).
