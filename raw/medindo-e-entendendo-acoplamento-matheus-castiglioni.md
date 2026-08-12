# Medindo e Entendendo Acoplamento

**Autor:** Matheus Castiglioni — Software Engineer
**Fonte:** https://blog.matheuscastiglioni.com.br/medindo-e-entendendo-acoplamento/
**Tempo de leitura:** 3 min (634 palavras)

---

Algo muito falado quando estamos construindo um sistema é o tal de **acoplamento**, mas afinal, o que isso significa e como podemos medi-lo? Acoplamento é a medida do nível de interdependência entre os módulos, ou seja, são as dependências entre os códigos.

## Tipos de Acoplamento

Existem alguns tipos de acoplamento:

- **Acoplamento de informação (_Data Coupling_)**: As partes são independentes umas as outras e se comunicam através de informações.
- **Acoplamento de carimbo (_Stamp Coupling_)**: Estruturas de informações são passadas de uma parte à outra.
- **Acoplamento de controle (_Control Coupling_)**: As partes que se comunicam passam informações de controles, ou seja, parâmetros que indicam comportamentos completamente diferentes.
- **Acoplamento externo (_External Coupling_)**: Quando partes dependem de outras partes.
- **Acoplamento comum (_Common Coupling_)**: Quando partes dependem de informações ou estruturas globais.
- **Acoplamento de conteúdo (_Content Coupling_)**: Uma parte pode modificar a informação de outra parte ou o fluxo de controle é passado entre partes.

Todos esses tipos de acoplamentos possuem seus _trade-off_, ou seja, às vezes vamos ter mais de um tipo e menos de outro (dependendo da situação e contexto).

## Categorias de Acoplamento

Além dos tipos de acoplamento também existem duas categorias de acoplamento:

- **Acoplamento apropriado (_Appropriate Coupling_)**: Você sabe que existe, está tudo bem existir e/ou deveria existir.
- **Acoplamento não apropriado (_Unappropriate Coupling_)**: Você não sabe que existe ou se sabe não deveria existir.

## Medindo Acoplamento

Uma das formas de medir o acoplamento é através do Acoplamento Aferente (_Afferent Coupling_) e Acoplamento Eferente (_Efferent Coupling_) ou _Incoming Coupling_ ou _Outgoing Coupling_.

- **Acoplamento Aferente**: Mede o número de conexões de entrada aos códigos, exemplo: Componentes, Classes, Funções, etc…
- **Acoplamento Eferente**: Mede o número de conexões que sai dos códigos.

### Medindo Abstrações

Abstrações é a proporção de artefatos abstratos para artefatos concretos, ela representa uma medida entre abstrações e implementações.

A equação que define tal métrica pode ser representada da seguinte forma:

**A = ma / (ma + mc)**

Nessa equação `ma` representa elementos abstratos (_interfaces_ ou classes abstratas) com o módulo e `mc` representa elementos concretos (classes não abstratas).

Exemplo: Imagine uma aplicação com 5.000 linhas de código, todas em uma única função `main`, o numerador de abstração é `1` enquanto o denominador é `5000`.

### Medindo Instabilidade

Instabilidade é uma métrica derivada, definida como a proporção de acoplamento eferente à soma de ambos (aferente e eferente). Ela determina a volatilidade da base de código, uma base de código que possui um alto nível de instabilidade quebra mais facilmente quando mudada por causa do alto acoplamento.

A equação que define tal métrica pode ser representada da seguinte forma:

**I = Ce / (Ca + Ce)**

Na equação `Ce` representa acoplamento (_coupling_) eferente (_efferent_) (ou que sai (_outgoing_)) e `Ca` representa acoplamento (_coupling_) aferente (_afferent_) (ou que entra (_incoming_)).

### Distância da Sequência Principal

A métrica de distância imagina um relacionamento ideal entre abstrações e instabilidades.

A equação que define tal métrica pode ser representada da seguinte forma:

**D = |A + I - 1|**

Nessa equação `A` representa o resultado da equação de abstrações e `I` representa o resultado da equação de instabilidade.

Ambos abstrações e instabilidade são frações do qual o resultado irá sempre ficar entre 0 e 1. Então quando formamos um gráfico podemos ver a linha da sequência principal.

Ao aplicar tais métricas para uma classe particular, isso nos permite calcular a distância da classe da sequência principal.

Olhando para a linha, conseguimos extrair mais informações, por exemplo:

- Classes mais próximas da linha são melhor equilibradas.
- Classes que sobem muito entram na zona de inutilidade (_zone of uselessness_).
- Classes que caem muito entram na zona de dor (_zone of pain_).

Onde:

- **Zona de inutilidade**: Código que é muito abstrato se torna difícil de usar.
- **Zona de dor**: Código com muita implementação e não tem abstrações o suficiente se torna frágil e difícil de manter.

## Conclusão

Nesse _post_ vimos e entendemos um pouco sobre acoplamentos (tipos e categorias) e sobre algumas métricas que podemos tirar referente a tal aspecto de arquitetura dos nossos sistemas.

Abraços, até a próxima.
