---
type: source
title: "A Filosofia do Design de Software — Cap. 4: Módulos Devem Ser Profundos"
aliases: ["philosophy of software design cap 4", "ousterhout capítulo 4", "modules should be deep", "módulos devem ser profundos", "deep modules capítulo"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-25
source_count: 0
tags: [design, ousterhout, traducao, modulo-profundo, interface, abstracao, classite, unix, java, cs-fundamentals]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 4 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 4.1 a 4.8. O capítulo apresenta o design modular como a técnica de deixar o desenvolvedor lidar com só uma fração da complexidade de cada vez. Todo módulo tem **interface** (o que quem usa precisa saber) e **implementação** (o código que cumpre a interface). A interface tem parte **formal** (assinaturas) e parte **informal** (comportamento, restrições de ordem), e a informal costuma ser a maior ([[wiki/concepts/interface-formal-e-informal]]). Uma interface é uma [[wiki/concepts/abstracao]]; abstração que omite detalhe importante é **falsa abstração**. Os melhores módulos são **profundos**: muita funcionalidade atrás de uma interface simples, com interface como custo e funcionalidade como benefício ([[wiki/concepts/modulo-profundo]]). Exemplos profundos: as cinco chamadas de E/S do Unix e o coletor de lixo. Exemplos rasos: lista encadeada e um método de uma linha. O excesso de classes pequenas é a **classite** ([[wiki/concepts/classite]]), com o I/O do Java como caso típico. Daí sai a regra de tornar o caso comum simples. A wiki já conhecia o capítulo pelo [[wiki/sources/filosofia-do-design-de-software-livro-completo]] e pelo podcast; esta é a primeira leitura em primeira mão.

## Key Claims

### Introdução e 4.1 Design modular

**Claim:** Uma das técnicas mais importantes contra a complexidade é projetar o sistema para que o desenvolvedor precise lidar só com uma pequena fração da complexidade total a cada momento. Isso é design modular.
**Evidence:** Introdução do capítulo. É a segunda estratégia geral do cap. 1 (encapsular a complexidade), agora com nome.
**Confidence:** alta.

**Claim:** No mundo ideal, cada módulo seria totalmente independente e a complexidade do sistema seria a do seu pior módulo. Isso é inatingível: módulos chamam uns aos outros e precisam saber algo uns dos outros. O objetivo do design modular é **minimizar** as dependências, não eliminá-las.
**Evidence:** 4.1, primeiro e segundo parágrafos. Exemplos de dependência: os argumentos de um método (mudou a assinatura, mudam todas as chamadas) e uma dependência sutil de ordem ("um método pode não funcionar corretamente a menos que algum outro método tenha sido invocado primeiro"). Retoma as dependências do cap. 2 ([[wiki/concepts/causas-de-complexidade-ousterhout]]).
**Confidence:** alta.

**Claim:** Cada módulo tem duas partes. A **interface** é tudo o que um desenvolvedor de outro módulo precisa saber para usá-lo; descreve *o que* o módulo faz, não *como*. A **implementação** é o código que cumpre as promessas da interface. Quem trabalha num módulo precisa entender a interface e a implementação dele, mais as interfaces dos módulos que ele chama, mas não as implementações desses outros módulos.
**Evidence:** 4.1, terceiro parágrafo. Exemplo: uma árvore balanceada esconde o rebalanceamento; quem insere só passa chave e valor.
**Confidence:** alta.

**Claim:** Para o livro, **módulo é qualquer unidade de código com interface e implementação**: classe, método, função, subsistema ou serviço (com interfaces como chamadas de kernel ou requisições HTTP). O livro fala mais de classes, mas as técnicas valem para todos.
**Evidence:** 4.1, quarto parágrafo. A definição é mais larga que a de [[wiki/concepts/tipos-de-modulos]] ou de módulo de linguagem ([[wiki/concepts/modulos-nodejs]]): para Ousterhout um método também é módulo.
**Confidence:** alta.

**Claim:** Os melhores módulos têm interface muito mais simples que a implementação. Duas vantagens: (1) a interface simples reduz a complexidade que o módulo impõe ao resto do sistema; (2) toda mudança que não altera a interface não afeta nenhum outro módulo.
**Evidence:** 4.1, último parágrafo. A vantagem (2) é a mesma de [[wiki/concepts/ocultamento-de-informacao]] (cap. 5).
**Confidence:** alta.

### 4.2 O que há em uma interface?

**Claim:** A interface tem parte **formal** e parte **informal**. A formal está no código e a linguagem verifica parte dela: assinatura do método (nomes e tipos de parâmetros, tipo de retorno, exceções), e, para uma classe, as assinaturas dos métodos públicos e as variáveis públicas. A informal não é verificável pela linguagem: comportamento de alto nível (a função apaga o arquivo do argumento) e restrições de uso (um método deve ser chamado antes de outro).
**Evidence:** 4.2, primeiro e segundo parágrafos. Ver [[wiki/concepts/interface-formal-e-informal]].
**Confidence:** alta.

**Claim:** Regra geral: "se um desenvolvedor precisa saber de uma informação específica para conseguir usar um módulo, então essa informação faz parte da interface do módulo". A parte informal só se descreve em comentários, e para a maioria das interfaces ela é **maior e mais complexa** que a formal.
**Evidence:** 4.2, segundo parágrafo. É o fundamento do argumento dos caps. 12 a 15 de que comentário de interface faz parte do design ([[wiki/concepts/comentarios-como-ferramenta-de-design]]).
**Confidence:** alta quanto ao texto. "Maior e mais complexa" é avaliação do autor, sem medida.

**Claim:** Uma interface claramente especificada diz exatamente o que o desenvolvedor precisa saber, o que ajuda a eliminar as **incógnitas desconhecidas** da 2.2.
**Evidence:** 4.2, terceiro parágrafo. Ver [[wiki/concepts/sintomas-de-complexidade-ousterhout]].
**Confidence:** alta.

**Claim:** Linguagens de especificação formal, quase todas de pesquisa, permitem descrever e verificar automaticamente o comportamento de um método. O autor acha que uma interface descrita em linguagem natural continua mais intuitiva para desenvolvedores que uma escrita em linguagem de especificação.
**Evidence:** nota de rodapé 1 (no raw, ao fim da 4.8). A N.T. lembra que "inglês" ali quer dizer linguagem natural.
**Confidence:** baixa como fato; alta como registro da opinião ("minha opinião atual").

### 4.3 Abstrações

**Claim:** Abstração é uma visão simplificada de uma entidade que omite detalhes sem importância. Em programação modular, cada módulo fornece uma abstração na forma da sua interface.
**Evidence:** 4.3, primeiro e segundo parágrafos. Ver [[wiki/concepts/abstracao]].
**Confidence:** alta.

**Claim:** Uma abstração erra de dois jeitos. (1) Inclui detalhes que não importam e fica mais complicada que o necessário, o que aumenta a carga cognitiva. (2) Omite detalhes que importam e gera obscuridade: é uma **falsa abstração**, que parece simples mas não é. A chave do design é entender o que importa e buscar designs que minimizem a informação de fato essencial.
**Evidence:** 4.3, terceiro parágrafo. Os dois erros batem com os sintomas e causas do cap. 2: o primeiro gera carga cognitiva, o segundo é obscuridade ([[wiki/concepts/causas-de-complexidade-ousterhout]]).
**Confidence:** alta.

**Claim:** O sistema de arquivos é o exemplo dos dois lados. Esconde como os blocos são escolhidos no disco, que não importa ao usuário se o desempenho for adequado. Mas a regra de descarregamento (*flushing*) do cache para o disco **precisa** estar na interface, porque um banco de dados precisa saber quando os dados estão de fato gravados para sobreviver a falhas.
**Evidence:** 4.3, quarto parágrafo. É o mesmo problema de durabilidade que bancos resolvem com `fsync` e write-ahead log `[external, não verificado no livro]`.
**Confidence:** alta.

**Claim:** Usamos abstrações o tempo todo fora da programação: o micro-ondas expõe alguns botões de tempo e intensidade; o carro esconde motor, bateria, freio ABS e controle de cruzeiro.
**Evidence:** 4.3, quinto parágrafo.
**Confidence:** alta.

### 4.4 Módulos profundos

**Claim:** Módulo **profundo** é o que oferece funcionalidade poderosa com interface simples. Na Figura 4.1, cada módulo é um retângulo: a área é a funcionalidade e a borda superior é a interface, cujo comprimento mede a complexidade da interface. Profundo é estreito e alto; raso é largo e baixo.
**Evidence:** 4.4, primeiro parágrafo, e a Figura 4.1 (SVG no raw, com os rótulos traduzidos). Ver [[wiki/concepts/modulo-profundo]].
**Confidence:** alta.

**Claim:** Profundidade é uma relação **custo-benefício**. O benefício é a funcionalidade; o custo, em complexidade do sistema, é a interface. "Interfaces são boas, mas interfaces em maior quantidade ou mais extensas não são necessariamente melhores!"
**Evidence:** 4.4, segundo parágrafo.
**Confidence:** alta.

**Claim:** A E/S de arquivos do Unix (e do Linux) é uma interface profunda: cinco chamadas de sistema (`open`, `read`, `write`, `lseek`, `close`) com assinaturas simples, sobre uma implementação moderna de centenas de milhares de linhas. A implementação resolve representação em disco, diretórios e caminhos, permissões, interrupções, escalonamento, cache e vários dispositivos. Ela mudou radicalmente ao longo dos anos, mas as cinco chamadas não.
**Evidence:** 4.4, terceiro a sexto parágrafos, com o bloco de código C das assinaturas. Sequencial é o padrão; acesso aleatório fica no `lseek`. Ver [[wiki/concepts/unix]].
**Confidence:** alta quanto à interface. "Centenas de milhares de linhas" é estimativa do autor.

**Claim:** O coletor de lixo de Go ou Java é um módulo profundo **sem interface nenhuma**. Ele até reduz a interface do sistema, porque elimina a interface de liberação de objetos, e esconde uma implementação complexa.
**Evidence:** 4.4, sétimo parágrafo. É o caso-limite da definição: benefício alto com custo zero de interface.
**Confidence:** alta.

### 4.5 Módulos rasos

**Claim:** Módulo **raso** tem interface relativamente complexa para a funcionalidade que fornece. Uma classe de lista encadeada é rasa: inserir ou excluir leva poucas linhas, então a abstração esconde pouco e a interface é quase tão complexa quanto a implementação. Classes rasas às vezes são inevitáveis e úteis, mas não ajudam muito contra a complexidade.
**Evidence:** 4.5, primeiro parágrafo. Ver [[wiki/concepts/lista-encadeada]].
**Confidence:** alta.

**Claim:** Exemplo extremo de método raso, tirado de um projeto de aula: `addNullValueForAttribute(attribute)`, cujo corpo é `data.put(attribute, null)`. Ele piora a complexidade: não abstrai nada, quem chama ainda precisa saber da variável `data`, a documentação seria mais longa que o código e chamar o método custa mais teclas que mexer em `data` direto.
**Evidence:** 4.5, segundo e terceiro parágrafos, com o código Java. A wiki registrava o I/O do Java como exemplo de Shallow Module; o exemplo do próprio livro para o sinal de alerta é este método.
**Confidence:** alta.

**Claim:** Sinal de alerta **Módulo Raso**: interface complicada em relação à funcionalidade. O benefício (não precisar aprender como funciona por dentro) é anulado pelo custo de aprender e usar a interface. "Módulos pequenos tendem a ser rasos."
**Evidence:** quadro de sinal de alerta da 4.5. Ver [[wiki/concepts/red-flags-de-design]].
**Confidence:** alta.

### 4.6 Classite

**Claim:** O valor das classes profundas não é reconhecido. O senso comum ensina que classes devem ser pequenas e que métodos com mais de N linhas (N pode ser 10) devem ser divididos. Isso produz muitas classes e métodos rasos, que aumentam a complexidade do sistema.
**Evidence:** 4.6, primeiro parágrafo. O livro não cita nomes aqui; o debate com Uncle Bob está em [[wiki/concepts/comprimento-de-funcao]] e [[wiki/concepts/modulo-profundo]].
**Confidence:** alta quanto ao texto.

**Claim:** **Classite** é o extremo dessa visão: "classes são boas, então quanto mais classes, melhor". Cada classe nova recebe o mínimo de funcionalidade. Cada uma é simples, mas suas interfaces se somam numa complexidade enorme no nível do sistema, e o boilerplate de cada classe deixa o código prolixo.
**Evidence:** 4.6, segundo parágrafo. Ver [[wiki/concepts/classite]].
**Confidence:** alta.

### 4.7 Exemplos: I/O no Java e no Unix

**Claim:** A biblioteca do Java é o exemplo mais visível de classite. A linguagem não exige classes pequenas, mas a cultura da comunidade sim. Por muitos anos, ler objetos serializados de um arquivo exigiu três objetos: `FileInputStream` (I/O rudimentar), `BufferedInputStream` (buffer) e `ObjectInputStream` (serialização). Os dois primeiros nunca mais são usados depois da abertura.
**Evidence:** 4.7, primeiro e segundo parágrafos, com o código Java. Ver [[wiki/concepts/decorator-pattern]] para o ângulo do padrão.
**Confidence:** alta.

**Claim:** É irritante e propenso a erro que o buffer precise ser pedido explicitamente: quem esquece fica com I/O lento. Dar escolha é bom, mas **as interfaces devem tornar o caso comum o mais simples possível**. Quase todo mundo quer buffer, então ele deveria vir por padrão, com um jeito separado de desligá-lo (outro construtor ou um método) que a maioria nem precisa conhecer.
**Evidence:** 4.7, terceiro parágrafo. O texto remete a "a fórmula na página 6", que deve ser a $C = \sum_p c_p t_p$ do cap. 2 ([[wiki/sources/filosofia-do-design-de-software-cap-02-natureza-da-complexidade]]). Essa identificação é inferência da wiki.
**Confidence:** alta quanto ao texto.

**Claim:** As chamadas do Unix fazem o contrário: sequencial é o padrão e o acesso aleatório fica no `lseek`, que quem só lê em sequência nem precisa conhecer. Se a maioria dos desenvolvedores só precisa de alguns recursos de uma interface, a complexidade efetiva dela é só a dos recursos mais usados.
**Evidence:** 4.7, quarto parágrafo. A última frase é a aplicação da fórmula do cap. 2 à interface: recurso pouco usado pesa pouco.
**Confidence:** alta.

### 4.8 Conclusão

**Claim:** Separar interface de implementação esconde a complexidade da implementação do resto do sistema. A questão mais importante no projeto de classes e módulos é torná-los profundos, com interface simples para os casos de uso comuns e funcionalidade significativa. Isso maximiza a complexidade escondida.
**Evidence:** 4.8.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **O exemplo do sinal de alerta é o método, não o `java.io`.** [[wiki/concepts/red-flags-de-design]] apresentava o I/O do Java como o exemplo de Shallow Module, a partir do podcast. No livro, o quadro de Módulo Raso vem junto do `addNullValueForAttribute` (4.5), e o I/O do Java aparece na 4.7 como **classite** e como falha em tornar o caso comum simples. As duas leituras são compatíveis, porque a classite gera classes rasas, mas a página foi ajustada para dizer de onde vem cada exemplo.
- **"Pequenas funções" no Unix.** [[wiki/concepts/unix]] registra, por outra fonte, a filosofia Unix de "pequenas funções reutilizáveis e combináveis". Ousterhout usa a E/S do Unix como exemplo de módulo **profundo**. Não é contradição: o que é pequeno é a interface (cinco chamadas), não a funcionalidade. Mas "pequeno" quer dizer coisas opostas nas duas fontes, e a página agora registra isso.
- **Regra de N linhas.** [[wiki/concepts/comprimento-de-funcao]] diz que funções simples podem ser longas e complexas devem ser curtas. Ousterhout ataca direto a regra de N linhas (4.6). As duas posições recusam o limite fixo, mas a página usa aninhamento como critério e o livro usa profundidade.
- **Módulo é mais que classe.** A wiki tem várias páginas que tratam módulo como unidade de empacotamento ([[wiki/concepts/tipos-de-modulos]], [[wiki/concepts/modulos-nodejs]], [[wiki/concepts/monolito-modular]]). No livro, um método é um módulo. Ao aplicar "módulos devem ser profundos", vale a definição larga.
- **N.T. repetida.** A nota sobre "classite" aparece duas vezes, na 4.6 e na 4.7, com redações diferentes. Não muda o sentido.
- **Nota de rodapé fora do lugar.** A nota ¹ é chamada na 4.2, mas o texto dela está no arquivo da 4.8. O raw manteve essa ordem.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-03-codigo-funcional-nao-e-suficiente]]
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/classite]] (nova)
- [[wiki/concepts/interface-formal-e-informal]] (nova)
- [[wiki/concepts/abstracao]]
- [[wiki/concepts/ocultamento-de-informacao]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/causas-de-complexidade-ousterhout]]
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]]
- [[wiki/concepts/lista-encadeada]]
- [[wiki/concepts/unix]]
- [[wiki/concepts/decorator-pattern]]
- [[wiki/concepts/comprimento-de-funcao]]

## Open Questions

- A "fórmula na página 6" da 4.7 é mesmo a $C = \sum_p c_p t_p$ do cap. 2? Conferir a paginação do original.
- O livro não mede profundidade. Existe métrica que aproxime "funcionalidade / complexidade de interface", por exemplo linhas de implementação por método público? Qualquer métrica dessas mediria o tamanho da implementação, não a funcionalidade, que é o que o autor quer dizer.
- A falsa abstração (4.3) é o mesmo fenômeno que a wiki chama de [[wiki/concepts/abstraction-illusion]]? Pela definição desta, parece outra coisa (padrão acessível mas inadequado), então não foram ligadas como sinônimos.
- ~~O cap. 5 (ocultamento de informação) é o próximo da tradução.~~ Respondida: [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]. A 5.7 retoma o *buffer* do Java I/O desta 4.7 como exemplo negativo de valor padrão.

## Raw Quotes

> "Os melhores módulos são aqueles cujas interfaces são muito mais simples do que suas implementações."

> "Uma abstração que omite detalhes importantes é uma falsa abstração: ela pode parecer simples, mas na realidade não é."

> "Interfaces são boas, mas interfaces em maior quantidade ou mais extensas não são necessariamente melhores!"
