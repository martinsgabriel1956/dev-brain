# The S.O.L.I.D Principles in Pictures

> Tradução/adaptação do artigo original em inglês "The S.O.L.I.D Principles in Pictures", de Ugonna Thelma, publicado em 18 de maio de 2020 na publicação Backticks & Tildes (Medium). Fonte: https://medium.com/backticks-tildes/the-s-o-l-i-d-principles-in-pictures-b34ce2f1e898

---

## Visão Geral

O artigo é um guia visual que explica cinco princípios de desenvolvimento de software desenhados para melhorar a manutenibilidade e a escalabilidade do código. A autora enfatiza que, embora esses princípios possam parecer semelhantes entre si, cada um mira um objetivo diferente.

---

## S — Single Responsibility (Responsabilidade Única)

**Definição:** "Uma classe deve ter uma única responsabilidade."

**Explicação:** Quando uma classe lida com múltiplas responsabilidades, o risco de bugs aumenta significativamente. Modificações em uma responsabilidade podem afetar as outras sem querer.

**Objetivo:** O princípio separa comportamentos para que bugs resultantes de uma mudança não se espalhem para funcionalidades não relacionadas.

**Nota sobre a ilustração:** A imagem mostra um personagem com um propósito único e focado, em contraste com outro tentando fazer múltiplas tarefas conflitantes ao mesmo tempo.

---

## O — Open-Closed (Aberto-Fechado)

**Definição:** "Classes devem estar abertas para extensão, mas fechadas para modificação."

**Explicação:** Modificar o comportamento existente de uma classe impacta todos os sistemas que dependem dela. Em vez disso, estenda a funcionalidade adicionando novos métodos, em vez de alterar os que já existem.

**Objetivo:** Isso estende as capacidades da classe sem modificar o comportamento atual, evitando bugs em sistemas que já utilizam essa classe.

**Nota sobre a ilustração:** A imagem contrasta estender comportamento (adicionar novas capacidades) com modificar a funcionalidade existente.

---

## L — Liskov Substitution (Substituição de Liskov)

**Definição:** "Se S é um subtipo de T, então objetos do tipo T em um programa podem ser substituídos por objetos do tipo S."

**Explicação:** Classes filhas precisam executar todas as ações da classe pai e retornar tipos de resultado compatíveis. Por exemplo, se uma classe pai retorna `Coffee`, as classes filhas podem retornar tipos específicos de café, como `Cappuccino`, mas não itens não relacionados, como `Water`.

**Objetivo:** O princípio garante consistência, permitindo que classes pai e filha sejam usadas de forma intercambiável sem gerar erros.

**Nota sobre a ilustração:** A imagem retrata relações entre classe pai e classe filha, e quais tipos de retorno são aceitáveis ou não numa substituição.

---

## I — Interface Segregation (Segregação de Interface)

**Definição:** "Clientes não deveriam ser forçados a depender de métodos que não usam."

**Explicação:** Classes devem implementar apenas as ações que de fato precisam. Métodos desnecessários geram desperdício e potenciais bugs, caso a classe não consiga executá-los corretamente.

**Objetivo:** O princípio divide conjuntos de ações em subconjuntos menores, garantindo que cada classe execute apenas os métodos necessários.

---

## D — Dependency Inversion (Inversão de Dependência)

**Definição:** "Módulos de alto nível não deveriam depender de módulos de baixo nível. Ambos deveriam depender da abstração."

**Termos-chave definidos:**
- **Módulo de alto nível:** uma classe que executa uma ação usando uma ferramenta.
- **Módulo de baixo nível:** a própria ferramenta.
- **Abstração:** uma interface que conecta as duas classes.
- **Detalhes:** como a ferramenta funciona internamente.

**Explicação:** Classes não deveriam depender diretamente de ferramentas específicas. Em vez disso, deveriam depender de interfaces que essas ferramentas implementam. Tanto a classe quanto a interface permanecem independentes dos detalhes de implementação da ferramenta.

**Objetivo:** Isso reduz a dependência da classe de alto nível em relação às classes de baixo nível, através da introdução de uma interface.

**Nota sobre a ilustração:** O diagrama mostra relações desacopladas por meio de camadas de abstração.

---

## Conclusão

Esses princípios, em conjunto, facilitam o ajuste, a extensibilidade e a testabilidade do código com o mínimo de complicação. A autora enfatiza a importância de entender o objetivo único de cada princípio, em vez de tratá-los como intercambiáveis.
