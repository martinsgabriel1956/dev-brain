---
type: source
title: "A Filosofia do Design de Software — Cap. 7: Camada Diferente, Abstração Diferente"
aliases: ["philosophy of software design cap 7", "ousterhout capítulo 7", "different layer, different abstraction", "camada diferente, abstração diferente"]
date_created: 2026-11-27
date_updated: 2026-11-27
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-07-camada-diferente-abstracao-diferente.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-27
source_count: 0
tags: [design, ousterhout, traducao, camadas, pass-through, decorator, context-object, estado-global, modulo-profundo]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 7 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 7.1 a 7.6. A regra: em um sistema bem projetado, cada camada fornece uma abstração **diferente** das camadas vizinhas ([[wiki/concepts/camada-diferente-abstracao-diferente]]). Camadas adjacentes com abstrações parecidas são sinal de alerta de decomposição ruim. O capítulo mostra três formas do problema: o [[wiki/concepts/metodo-de-repasse]] (`TextDocument`, com 13 de 15 métodos públicos só repassando para `TextArea`), o [[wiki/concepts/decorator-pattern|decorator]] usado em excesso e a variável de passagem (`cert` atravessando `main → m1 → m2 → m3`), cuja saída preferida do autor é o [[wiki/concepts/objeto-de-contexto]]. Também aplica a regra à relação entre interface e implementação: a classe de texto guarda linhas, mas a API deve ser por caracteres. Duplicar assinatura é aceitável quando cada método agrega função: *dispatcher* e várias implementações da mesma interface. Continua o cap. 6 ([[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]). A wiki já conhecia o capítulo por um parágrafo do [[wiki/sources/filosofia-do-design-de-software-livro-completo]]; a leitura de primeira mão não contradiz, só detalha.

## Key Claims

### Introdução

**Claim:** Sistemas são compostos por camadas, as de cima usando as de baixo. Em um sistema bem projetado, cada camada tem uma abstração diferente da de cima e da de baixo: seguindo uma operação pelas chamadas, a abstração muda a cada método. Exemplos: o sistema de arquivos (arquivo como array de bytes de tamanho variável → cache de blocos de tamanho fixo → drivers que movem blocos entre disco e memória) e o TCP (fluxo de bytes confiável sobre pacotes de tamanho limitado entregues por melhor esforço).
**Evidence:** Introdução do capítulo. Camadas adjacentes com abstrações semelhantes são chamadas de "sinal de alerta (red flag)" de problema na decomposição de classes, mas não há quadro com esse nome; o quadro do capítulo é o do método de repasse (ver Contradições).
**Confidence:** alta.

### 7.1 Métodos de repasse

**Claim:** Um método de repasse faz pouco além de invocar outro método de assinatura semelhante ou idêntica. Exemplo de um projeto de aluno (editor de texto com GUI): `TextDocument` tinha `getLastTypedCharacter`, `getCursorOffset` e `insertString` que só chamavam o mesmo método em `TextArea`, e `willInsertString`, que repassava para o `listener` depois de checar se ele não era nulo. 13 dos 15 métodos públicos eram de repasse.
**Evidence:** 7.1, trecho de Java e quadro "Sinal de Alerta: Método de Repasse". Ver [[wiki/concepts/metodo-de-repasse]] e [[wiki/concepts/red-flags-de-design]].
**Confidence:** alta.

**Claim:** Métodos de repasse tornam as classes mais rasas: aumentam a interface sem aumentar a funcionalidade total do sistema. Também criam dependência: se a assinatura de `insertString` mudar em `TextArea`, o método de `TextDocument` tem de mudar junto.
**Evidence:** 7.1, terceiro parágrafo. É [[wiki/concepts/modulo-profundo|módulo raso]] e [[wiki/concepts/acoplamento]] sem ganho.
**Confidence:** alta.

**Claim:** O repasse indica confusão na divisão de responsabilidades: `TextDocument` oferece `insertString`, mas quem implementa é `TextArea`. "A interface de uma funcionalidade deve estar na mesma classe que implementa a funcionalidade." A pergunta a fazer: por quais recursos e abstrações cada classe é responsável? Provavelmente haverá sobreposição.
**Evidence:** 7.1, quarto parágrafo.
**Confidence:** alta.

**Claim:** Três refatorações (Figura 7.1): (b) expor a classe de baixo nível direto aos chamadores, tirando da classe de cima a responsabilidade pelo recurso; (c) redistribuir a funcionalidade para evitar chamadas entre as classes; (d) se as classes não puderem ser desembaraçadas, juntá-las. O aluno juntou `TextDocument`, `TextArea` e `TextDocumentListener` em duas classes com responsabilidades mais claras.
**Evidence:** 7.1, dois últimos parágrafos, e legenda da Figura 7.1 (que na tradução está dentro da 7.2, em Mermaid).
**Confidence:** alta.

### 7.2 Quando a duplicação de interface é aceitável

**Claim:** Mesma assinatura não é problema por si: o que importa é cada método contribuir com funcionalidade significativa. O *dispatcher* recebe argumentos, escolhe um entre vários métodos e repassa a maioria ou todos os argumentos. Tem a mesma assinatura dos métodos que chama, mas faz algo útil: decide quem executa. Exemplo: o servidor Web que examina a URL e escolhe o tratador, às vezes guiado por um conjunto de regras.
**Evidence:** 7.2, primeiro a terceiro parágrafos e o exemplo do servidor Web.
**Confidence:** alta.

**Claim:** Várias implementações da mesma interface (drivers de disco de um SO) também são aceitáveis e até reduzem a [[wiki/concepts/carga-cognitiva]]: quem aprendeu uma aprende as outras. Esses métodos costumam estar na mesma camada e não chamam uns aos outros.
**Evidence:** 7.2, último parágrafo. O mesmo exemplo de drivers aparece no cap. 6 como "empurrar a especialização para baixo" ([[wiki/concepts/modulo-de-proposito-geral]]).
**Confidence:** alta.

### 7.3 Decorators

**Claim:** O decorator (ou *wrapper*) encoraja duplicar a API entre camadas: recebe um objeto, oferece API semelhante ou idêntica e chama os métodos do objeto de baixo. Exemplos: `BufferedInputStream` sobre `InputStream` (o `read` de um caractere lê um bloco maior e guarda o resto) e `ScrollableWindow` sobre `Window`. A motivação é separar extensões específicas de um núcleo genérico, mas as classes decorator tendem a ser rasas, cheias de repasse e *boilerplate* para pouca função nova. Usado em excesso, gera a explosão de classes rasas do I/O do Java.
**Evidence:** 7.3, primeiro e segundo parágrafos. Aqui o livro nomeia o padrão, o que o cap. 4 não fazia ([[wiki/concepts/decorator-pattern]], [[wiki/concepts/classite]]).
**Confidence:** alta.

**Claim:** Antes de criar um decorator, quatro alternativas: (1) pôr a função na própria classe, se for geral, ligada à classe ou usada pela maioria dos usuários (quase todo mundo que cria um `InputStream` cria um `BufferedInputStream`, então as duas classes "deveriam ter sido combinadas"); (2) juntar a função ao caso de uso, se for especializada; (3) juntar a um decorator existente, ficando com um só mais profundo; (4) implementar como classe independente, sem envolver a base (as barras de rolagem provavelmente não precisam embrulhar a janela inteira).
**Evidence:** 7.3, lista de alternativas.
**Confidence:** alta.

**Claim:** Wrapper faz sentido quando uma classe externa de interface imutável precisa obedecer a outra interface na aplicação: ele traduz entre as duas. O autor diz que isso é raro e que geralmente há alternativa melhor.
**Evidence:** 7.3, último parágrafo. Esse uso é o que a wiki chama de [[wiki/concepts/adapter-pattern]]; o livro não usa o nome (leitura da wiki).
**Confidence:** alta quanto ao texto; a raridade é opinião do autor.

### 7.4 Interface versus implementação

**Claim:** A regra vale dentro da classe: a interface deve ser diferente da implementação. Se as duas têm abstrações parecidas, a classe provavelmente é rasa. No editor do cap. 6, a maioria das equipes guardou o texto em linhas, e algumas fizeram a API em linhas também (`getLine`, `putLine`). Isso deixou a classe rasa e desajeitada: a UI insere no meio de linhas e apaga intervalos que atravessam linhas, então os chamadores tinham de dividir e juntar linhas, com código não trivial, duplicado e espalhado pela UI.
**Evidence:** 7.4, primeiro parágrafo.
**Confidence:** alta.

**Claim:** As classes ficaram mais fáceis de usar com interface orientada a caracteres: `insert` de uma string arbitrária (com quebras de linha) em posição arbitrária e `delete` entre duas posições arbitrárias. Por dentro, o texto continuava em linhas. A diferença entre a API e o armazenamento "representa uma funcionalidade valiosa fornecida pela classe".
**Evidence:** 7.4, segundo parágrafo. Ver [[wiki/concepts/abstracao]] e [[wiki/concepts/modulo-profundo]].
**Confidence:** alta.

### 7.5 Variáveis de passagem

**Claim:** Variável de passagem é a que desce por uma longa cadeia de métodos que não a usam. Exemplo (Figura 7.2a): um argumento de linha de comando com os certificados só é usado por `m3`, que abre um *socket*, mas `cert` aparece na assinatura de `m1` e `m2`. Todos os intermediários ficam cientes dela, e adicionar uma variável nova (suporte a certificados depois) pode exigir mudar muitas interfaces.
**Evidence:** 7.5, primeiro e segundo parágrafos.
**Confidence:** alta.

**Claim:** Três saídas, com custos. (b) Guardar num objeto já compartilhado por `main` e `m3`, mas esse objeto pode virar ele próprio variável de passagem. (c) Variável global, que impede duas instâncias independentes do sistema no mesmo processo; parece improvável em produção, mas é útil em testes. (d) **Objeto de contexto**, a solução que o autor mais usa: guarda todo o estado global da aplicação (configuração, subsistemas compartilhados, contadores de desempenho), um por instância do sistema.
**Evidence:** 7.5, terceiro a quinto parágrafos e Figura 7.2. Ver [[wiki/concepts/objeto-de-contexto]] e [[wiki/concepts/estado-global-em-servidor]].
**Confidence:** alta.

**Claim:** Para o contexto não virar variável de passagem, os objetos principais guardam uma referência a ele como variável de instância; quem cria um objeto novo pega a referência do próprio objeto e passa ao construtor. O contexto fica disponível em todo lugar, mas só aparece explícito nos construtores. Variável nova entra no contexto sem afetar código existente, exceto construtor e destrutor do contexto, e testes podem mudar a configuração global mexendo em campos do contexto.
**Evidence:** 7.5, sexto e sétimo parágrafos. Passar pelo construtor é injeção de dependência ([[wiki/concepts/dependency-injection]]); o livro não usa o termo (leitura da wiki).
**Confidence:** alta.

**Claim:** Contextos "estão longe de ser uma solução ideal": têm a maioria das desvantagens de globais (não fica óbvio por que uma variável está lá nem onde é usada), podem virar um "amontoado desorganizado de dados" com dependências não óbvias e criar problemas de *thread-safety*. A melhor defesa é variáveis imutáveis no contexto. "Infelizmente, não encontrei uma solução melhor do que contextos."
**Evidence:** 7.5, último parágrafo. A imutabilidade conversa com [[wiki/concepts/estado-global-inofensivo]].
**Confidence:** alta.

### 7.6 Conclusão

**Claim:** Todo elemento de design (interface, argumento, função, classe, definição) custa complexidade, porque é mais uma coisa a aprender. Só vale se eliminar mais complexidade do que adiciona. "Camada diferente, abstração diferente" é uma aplicação disso: camadas com a mesma abstração, como métodos e decorators de repasse, provavelmente não pagam a infraestrutura que acrescentam; argumentos de repasse obrigam vários métodos a conhecê-los sem acrescentar função.
**Evidence:** 7.6. É o mesmo custo-benefício da Figura 4.1 ([[wiki/concepts/modulo-profundo]]) aplicado a camadas.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **Nenhuma contradição com o livro completo.** O parágrafo do cap. 7 em [[wiki/sources/filosofia-do-design-de-software-livro-completo]] (13 de 15 métodos, `main → m1 → m2 → m3`, contexto como campo de instância, desvantagens de globais) confere com o texto. Faltavam: a 7.4 (interface vs. implementação), os casos aceitáveis da 7.2, as quatro alternativas ao decorator e a recomendação de imutabilidade.
- **Decorator nomeado.** [[wiki/concepts/decorator-pattern]] registrava que, no cap. 4, Ousterhout não fala em Decorator e trata o `java.io` como classite. No cap. 7 ele nomeia o padrão e diz que `InputStream` e `BufferedInputStream` "deveriam ter sido combinadas". A tensão com a skill fica registrada lá: a referência `design-patterns.md` apresenta o Decorator como "alternativa a herança", sem custo [skill: tech-mentor-backend].
- **Request context passa adiante; Ousterhout evita passar.** [[wiki/concepts/request-context]] descreve agrupar o contexto da requisição e "passá-lo adiante" como alternativa ao global. Ousterhout chega à mesma rejeição do global, mas trata a passagem por todos os métodos como o problema e guarda a referência nos objetos. Os dois não brigam: um agrupa por requisição, o outro por instância do sistema, e ambos juntam várias variáveis num objeto só. Leitura da wiki.
- **Sinkhole é o mesmo sintoma na escala da arquitetura.** [[wiki/concepts/architecture-sinkhole]] (camadas fechadas que só repassam) é o método de repasse em escala de camadas da aplicação. Ousterhout não cita o termo; a ligação é leitura da wiki.
- **"Orientada a caracteres" não é "um caractere por vez".** A 6.5 critica `insert`/`delete` de um caractere; a 7.4 elogia a interface "orientada a caracteres". Não há conflito: a da 7.4 insere strings arbitrárias e apaga intervalos, que é a interface por intervalos da 6.5.
- **Tradução: "sinal de alerta" na introdução.** A introdução chama camadas com abstrações semelhantes de *red flag*, mas o quadro do capítulo é só o do método de repasse, e o apêndice ([[wiki/concepts/red-flags-de-design]]) lista apenas *Pass-Through Method* para o cap. 7.
- **Tradução: três nomes para *pass-through*.** "Método de repasse" (7.1), "variável de passagem" (7.5) e "argumentos de repasse" (7.6, onde o original diz *pass-through arguments*). A wiki usa [[wiki/concepts/metodo-de-repasse]] e trata a variável dentro de [[wiki/concepts/objeto-de-contexto]].
- **Figura 7.1 fora do lugar.** A tradução cita a Figura 7.1 na 7.1, mas o diagrama (Mermaid) e a legenda estão no arquivo da 7.2. O raw manteve a ordem dos arquivos.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos]]
- [[wiki/concepts/camada-diferente-abstracao-diferente]] (nova)
- [[wiki/concepts/metodo-de-repasse]] (nova)
- [[wiki/concepts/objeto-de-contexto]] (nova)
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/decorator-pattern]]
- [[wiki/concepts/adapter-pattern]]
- [[wiki/concepts/classite]]
- [[wiki/concepts/abstracao]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/architecture-sinkhole]]
- [[wiki/concepts/request-context]]
- [[wiki/concepts/estado-global-em-servidor]]
- [[wiki/concepts/estado-global-inofensivo]]
- [[wiki/concepts/dependency-injection]]
- [[wiki/concepts/dependency-lookup]]
- [[wiki/concepts/modulo-de-proposito-geral]]

## Open Questions

- Onde fica a fronteira entre *dispatcher* e método de repasse? Um método que escolhe entre duas opções com um `if` já "agrega funcionalidade"? O livro só dá o caso do servidor Web.
- O contexto guardado em todo objeto principal é, na prática, um *service locator* passado pelo construtor. O livro não discute a diferença nem o risco de toda classe depender do contexto inteiro.
- Como Ousterhout lida com contexto por requisição (usuário, *trace id*) num servidor? O capítulo só trata estado global por instância do sistema.

## Raw Quotes

> "a interface de uma funcionalidade deve estar na mesma classe que implementa a funcionalidade."

> "Infelizmente, não encontrei uma solução melhor do que contextos."

> "a diferença representa uma funcionalidade valiosa fornecida pela classe."
