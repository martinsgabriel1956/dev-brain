# Como Entregar Seus Projetos Mais Rápido e Com Mais Qualidade — KISS e YAGNI

**Autor:** Everton Oliveira — engenheiro de software sênior
**Tema:** Dois princípios fundamentais para entregas rápidas e com qualidade (KISS e YAGNI)
**Formato:** Transcrição de vídeo (português, limpa e pontuada — sem tradução necessária)

---

## Introdução

Um desafio muito grande na carreira de programador é conseguir realizar entregas rápidas e com qualidade. Ao mesmo tempo que o time de produto e o time de negócio esperam um projeto entregue no prazo, existe a expectativa de que esse projeto seja entregue com qualidade e atenda as necessidades do usuário.

Dois princípios atacam diretamente esses dois desafios do dia a dia de um programador: **KISS** e **YAGNI**.

---

## Princípio 1 — KISS (Keep It Simple, Stupid)

KISS foi criado pela Marinha dos Estados Unidos e utilizado pela primeira vez nesse contexto militar. O objetivo é manter as coisas o mais simples possível.

Se você está implementando um método ou uma classe, precisa deixar essa classe, esse método, o mais simples possível — para que outras pessoas consigam dar manutenção e para que o código não se torne complexo, caro e difícil de manter a longo prazo.

Esse princípio se aplica em diversas áreas: organização de projetos, arquitetura e design de software, e também em testes. Por exemplo: às vezes existem muitos testes unitários que não geram valor, que não agregam tanto — nesses casos, dá para remover esses testes e ter testes mais focados no coração do problema, naquilo que realmente precisa ser testado e garantido.

### Exemplo de refatoração com KISS

Lógica de validação que verifica se uma transferência, dado seu status atual, pode ser reprocessada (política de idempotência de reprocessamento).

**Antes** — vários `if`s encadeados, cada um comparando o status contra uma lista de valores, até por fim retornar `false`.

**Depois** — usando KISS:
1. Validação inicial com retorno antecipado.
2. Os status que habilitam reprocessamento são colocados dentro de uma lista.
3. Verifica-se se o status atual da transferência está contido nessa lista.
4. Por fim, retorna `false`.

O resultado tem menos linhas encadeadas e qualquer profissional que ler esse código depois vai ter muito mais facilidade de entender o que o código se propõe a resolver.

### Benefícios do KISS

- **Redução do número de bugs** — quanto mais simples o código, mais fácil de manter, entender e evoluir, e consequentemente menos bugs.
- **Menor custo de manutenção.**
- **Entregas mais rápidas** — código simples evolui com mais facilidade.
- **Mais qualidade** — código simples de entender é mais simples de testar e de garantir que funciona.
- **Maior retenção de usuário** (no aspecto de front-end/interfaces) — uma interface mais simples, que o usuário entende logo de cara, tem maior propensão a manter esse usuário utilizando o sistema.

---

## Princípio 2 — YAGNI (You Aren't Gonna Need It)

YAGNI significa "você não precisará disso". Foi apresentado no livro *Extreme Programming* de Ronald Jeffries. O objetivo é que você só adicione uma feature ao seu software se ela for realmente necessária naquele momento.

Exemplo comum: ao criar um repositório, o programador já pensa em criar um método para `get`, um para `update`, um de `delete`, porque "tem certeza que vai usar" — o costume de tentar prever o futuro e já fazer implementações antecipadas. Isso vai aumentando o código com coisas que não são necessárias para aquele momento, para aquela entrega.

Esse princípio também se aplica em várias áreas: organização de projetos, arquitetura e design de software, entre outras.

No exemplo do repositório: imagine vários métodos possíveis (get, insert, delete, update...), mas a feature em questão só precisava de três deles. Implementar os outros métodos que não eram necessários naquele momento aumenta o tempo de entrega e entrega algo que não vai gerar valor naquele momento — pode nunca ser utilizado, vira "lixo" dentro do projeto que depois vai ter que ser removido.

### Benefícios do YAGNI

- **Foco no que realmente importa** — mais tempo investido naquilo que é essencial para a entrega.
- **Entregas mais rápidas** — reduz o tempo gasto com implementações desnecessárias.
- **Redução da complexidade do software** — o software passa a ter funcionalidades bem específicas para o que se propõe a resolver, e quem lê o código consegue entender exatamente o que existe de feature implementada.

---

## Conclusão

Esses dois princípios são simples, mas se aplicados no dia a dia trazem um valor enorme — tanto para a empresa quanto para a carreira do programador. Mais foco no que realmente importa, cuidado em fazer implementações simples e fáceis de entender, efeito positivo tanto na entrega quanto na manutenção do software, e redução de custos para a empresa (software mais barato de manter, que demora menos para gerar valor ao usuário).

Na experiência do autor como engenheiro de software, muitos profissionais ignoram esses princípios e investem tempo em funcionalidades que muitas vezes nunca são usadas — desperdício de tempo e de recursos da empresa que poderiam estar sendo aplicados em outra coisa. YAGNI, em particular, ajuda a manter o código mais enxuto e mais fácil de manter, e permite dar mais atenção (inclusive de cobertura de teste) para o que é essencial e realmente gera valor para a empresa e para o usuário final.

O autor aplica esses dois princípios diariamente na rotina de trabalho como programador.
