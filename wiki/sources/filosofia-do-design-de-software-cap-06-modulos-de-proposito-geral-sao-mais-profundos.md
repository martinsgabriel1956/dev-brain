---
type: source
title: "A Filosofia do Design de Software — Cap. 6: Módulos de Propósito Geral são Mais Profundos"
aliases: ["philosophy of software design cap 6", "ousterhout capítulo 6", "general-purpose modules are deeper", "módulos de propósito geral são mais profundos"]
date_created: 2026-11-26
date_updated: 2026-11-26
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-06-modulos-de-proposito-geral-sao-mais-profundos.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-26
source_count: 0
tags: [design, ousterhout, traducao, general-purpose, especializacao, casos-especiais, api-design, undo-redo, information-hiding]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 6 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 6.1 a 6.9. A tese: a especialização desnecessária "talvez seja a maior causa isolada de complexidade em software", e código de propósito mais geral é mais simples. O ponto ideal é o módulo **um tanto de uso geral** ([[wiki/concepts/modulo-de-proposito-geral]]): a funcionalidade atende às necessidades de hoje e a interface não fica presa a elas. O exemplo central é a classe de texto de um editor feito por alunos. A versão especializada tinha `backspace`, `delete` e `deleteSelection`; a geral tem `insert(position, newText)` e `delete(start, end)`, com menos código e melhor [[wiki/concepts/ocultamento-de-informacao|ocultamento]]. O capítulo dá três perguntas para achar o equilíbrio e manda empurrar a especialização para cima (para a UI) ou para baixo (para os drivers de dispositivo). O segundo exemplo é o desfazer/refazer, separado numa classe `History` genérica com ações específicas, parente do [[wiki/concepts/command-pattern]]. A última técnica é [[wiki/concepts/eliminar-casos-especiais]]: a seleção vazia em vez de "nenhuma seleção". Continua o cap. 5 ([[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]). A wiki já conhecia o capítulo pelo [[wiki/sources/filosofia-do-design-de-software-livro-completo]]. A leitura de primeira mão corrige uma frase da wiki.

## Key Claims

### Introdução

**Claim:** Lecionar o curso mudou a visão do autor sobre generalidade versus especialização. "A especialização leva à complexidade"; a superespecialização "talvez seja a maior causa isolada de complexidade em software". O princípio vale em vários níveis: no design de classes e métodos (API de uso geral é mais profunda e esconde mais) e no corpo dos métodos (eliminar casos especiais, o que também pode deixar o código mais eficiente, tema do cap. 20).
**Evidence:** Introdução do capítulo. É opinião de experiência em sala de aula, sem medição, como o resto do livro ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).
**Confidence:** alta quanto ao que o livro diz; a afirmação "maior causa isolada" é marcada pelo próprio autor com "talvez".

### 6.1 Um tanto de uso geral

**Claim:** O capítulo expõe os dois lados. Uso geral parece a mentalidade de investimento do cap. 3 ([[wiki/concepts/programacao-tatica-vs-estrategica]]): gastar um pouco agora para economizar depois. Uso específico parece o desenvolvimento incremental: construir só o que se sabe que precisa e refatorar quando surgir outro uso, já que o futuro é difícil de prever e o genérico demais pode não resolver bem o problema de hoje.
**Evidence:** 6.1, primeiro e segundo parágrafos. O segundo argumento é o de [[wiki/concepts/yagni]], sem o nome.
**Confidence:** alta.

**Claim:** O autor começou do lado do uso específico e mudou de ideia revisando projetos de alunos. As classes de uso geral "eram quase sempre melhores": interfaces mais simples e profundas, menos código na implementação. Dá menos trabalho construir a versão geral mesmo com um uso só, e ela continua melhor "mesmo que você não reutilize a classe".
**Evidence:** 6.1, terceiro parágrafo. A vantagem não depende de reuso, o que separa o argumento do "faça genérico porque um dia vai servir".
**Confidence:** alta quanto ao relato; a base é a observação do autor.

**Claim:** "Um tanto de uso geral" quer dizer que a **funcionalidade** reflete as necessidades atuais e a **interface** não. A interface deve ser fácil de usar hoje sem estar atrelada a hoje. "Um tanto" é o limite: genérico demais fica difícil de usar para o caso atual.
**Evidence:** 6.1, quarto parágrafo. Ver [[wiki/concepts/modulo-de-proposito-geral]].
**Confidence:** alta.

### 6.2 a 6.4 A classe de texto do editor

**Claim:** Os alunos fizeram um editor de texto com GUI: várias janelas do mesmo arquivo e desfazer/refazer em vários níveis. Muitas equipes moldaram a API da classe de texto pelos recursos da UI: `backspace(Cursor)`, `delete(Cursor)` e `deleteSelection(Selection)`. O resultado foi uma classe com muitos métodos rasos, cada um servindo a uma operação da UI, vários chamados num único lugar. Quem trabalhava na UI tinha de aprender todos eles.
**Evidence:** 6.2. É [[wiki/concepts/carga-cognitiva]] dos dois lados e [[wiki/concepts/modulo-profundo|módulos rasos]] em série.
**Confidence:** alta.

**Claim:** A especialização vazou informação entre UI e classe de texto: seleção e tecla backspace apareceram dentro da classe de texto. Cada operação nova da UI exigia um método novo na classe de texto, então quem mexia numa mexia na outra. As duas classes não podiam mais ser desenvolvidas de forma independente.
**Evidence:** 6.2, último parágrafo. É vazamento no sentido do cap. 5 ([[wiki/concepts/ocultamento-de-informacao]]) e [[wiki/concepts/acoplamento]] entre camadas.
**Confidence:** alta.

**Claim:** A API geral precisa de dois métodos para modificar texto: `insert(Position, String)` e `delete(Position start, Position end)` (apaga de `start` inclusive até `end` exclusive). Usa `Position` em vez de `Cursor`, que é um conceito da UI. Para navegar, `changePosition(position, numChars)`, que anda para frente ou para trás e atravessa linhas. Delete vira `text.delete(cursor, text.changePosition(cursor, 1))`; backspace vira `text.delete(text.changePosition(cursor, -1), cursor)`.
**Evidence:** 6.3, com os quatro trechos de Java.
**Confidence:** alta.

**Claim:** O código da UI fica um pouco mais longo, mas mais óbvio: quem lê vê quais caracteres o backspace apaga sem abrir a classe de texto. E o total de código cai, porque muitos métodos específicos viram poucos gerais.
**Evidence:** 6.3, quarto parágrafo. Mais linhas no chamador e menos complexidade é o mesmo argumento do cap. 2 sobre LOC ([[wiki/concepts/modulo-profundo]], seção "Mais linhas pode ser mais simples").
**Confidence:** alta.

**Claim:** A classe geral serve a outros usos. Numa aplicação que troca todas as ocorrências de uma string, `backspace` e `delete` não valem nada; a classe geral já tem quase tudo. **Falta** um método `findNext(Position start, String string)`, que um editor com busca e substituição provavelmente já teria.
**Evidence:** 6.3, quinto e sexto parágrafos. O livro não diz que a classe serve "sem alteração" (ver Contradições).
**Confidence:** alta.

**Claim:** O `backspace` da versão especializada era uma **falsa abstração**. Fingia esconder quais caracteres apaga, mas a UI precisa saber disso, e quem trabalha na UI vai ler o código do método para confirmar. "Um dos elementos mais importantes do design de software é determinar quem precisa saber o quê, e quando." Quando o detalhe importa, ele deve ficar explícito; escondê-lo atrás de uma interface "apenas cria obscuridade".
**Evidence:** 6.4, segundo parágrafo. O termo vem do cap. 4 ([[wiki/concepts/abstracao]], seção "Falsa abstração") e a obscuridade é uma das causas do cap. 2 ([[wiki/concepts/causas-de-complexidade-ousterhout]]). Contrapeso ao cap. 5: esconder só o que não é necessário fora.
**Confidence:** alta.

### 6.5 Perguntas para se fazer

**Claim:** Três perguntas para achar o equilíbrio. (1) Qual é a interface mais simples que cobre todas as necessidades atuais? Menos métodos sem perder capacidade indica métodos mais gerais: três métodos de deletar viraram um. Mas só enquanto cada método continua simples; se for preciso adicionar muitos argumentos, não simplificou. (2) Em quantas situações o método será usado? Método feito para um uso só, como `backspace`, é sinal de alerta. (3) A API é fácil de usar para as necessidades atuais? Se o chamador precisa de muito código extra, a interface não dá a funcionalidade certa.
**Evidence:** 6.5. A segunda pergunta chama o uso único de "sinal de alerta", mas o capítulo não tem quadro de *red flag* ([[wiki/concepts/red-flags-de-design]]).
**Confidence:** alta.

**Claim:** A terceira pergunta pega o excesso de generalidade. Uma classe de texto com `insert` e `delete` de um caractere é simples e geral, mas obriga a UI a escrever laços para intervalos e fica ineficiente em operações grandes. Por isso a classe deve operar sobre intervalos de caracteres.
**Evidence:** 6.5, último parágrafo. O cap. 11 volta à mesma classe comparando interfaces por linha, por caractere e por intervalo ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).
**Confidence:** alta.

### 6.6 Empurre a especialização para cima (e para baixo)

**Claim:** A especialização não some; o código especializado deve ficar separado do geral, empurrado para cima ou para baixo na pilha. **Para cima:** as classes de topo de uma aplicação são especializadas nos recursos, mas isso não precisa descer para as classes que os implementam. A API de texto revisada deixou o comportamento do backspace no código da UI. **Para baixo:** o sistema operacional define uma interface geral para armazenamento secundário ("ler um bloco", "escrever um bloco") e cada driver implementa essa interface com os comandos do seu dispositivo. O núcleo do SO não conhece características de nenhum dispositivo, e um dispositivo novo entra sem mudar o núcleo.
**Evidence:** 6.6. O driver de dispositivo é inversão de dependência na forma clássica (leitura da wiki; o livro não usa o termo).
**Confidence:** alta.

### 6.7 O mecanismo de desfazer

**Claim:** O editor tinha de desfazer e refazer mudanças no texto, na seleção, no cursor de inserção e na visualização. Desfazer uma exclusão restaura o texto, seleciona de novo e rola até ele. Alguns alunos puseram tudo na classe de texto: a lista de desfazer, entradas de texto adicionadas automaticamente, métodos extras para a UI registrar seleção, cursor e visualização, e *callbacks* de volta para a UI desfazer esses itens. O resultado misturou o núcleo geral (gerenciar e percorrer uma lista de ações) com tratadores específicos sem relação com texto, vazou informação entre texto e UI e exigiria mudar a classe de texto para cada entidade nova.
**Evidence:** 6.7, primeiro a terceiro parágrafos.
**Confidence:** alta.

**Claim:** A correção extrai o núcleo para a classe `History`, com a interface `History.Action` (`undo()`, `redo()`) e os métodos `addAction`, `addFence`, `undo` e `redo`. `History` não sabe o que as ações guardam. As ações específicas ficam nos módulos que entendem o assunto: a classe de texto cria `UndoableInsert` e `UndoableDelete`, a UI cria `UndoableSelection` e `UndoableCursor`. *Fences* (barreiras) agrupam ações para que um pedido do usuário desfaça um grupo inteiro; quem decide onde pôr as barreiras é o código de alto nível da UI.
**Evidence:** 6.7, trecho de Java e quarto a sexto parágrafos. `History.Action` com `undo`/`redo` é o [[wiki/concepts/command-pattern]] aplicado a desfazer; o livro não nomeia o padrão (leitura da wiki).
**Confidence:** alta.

**Claim:** O desfazer fica em três partes independentes: o mecanismo geral (`History`), as especificidades de cada ação (várias classes, cada uma com poucos tipos) e a política de agrupamento (UI de alto nível). Nenhuma precisa conhecer as outras. A decisão fundamental foi separar a parte geral da específica; "o restante do design surgiu naturalmente".
**Evidence:** 6.7, sétimo a nono parágrafos.
**Confidence:** alta.

**Claim:** Separar geral de específico vale **dentro de um mecanismo**. Um módulo pode juntar o código geral de um mecanismo com o código específico de outro. A classe de texto é geral para texto e contém o desfazer específico de texto (`UndoableInsert`), que não deve ir para `History`, mas faz sentido ao lado das outras funções de texto.
**Evidence:** Nota da 6.7. Delimita a regra e evita a leitura "todo código específico sai da classe".
**Confidence:** alta.

### 6.8 Elimine casos especiais

**Claim:** Casos especiais são a especialização dentro do corpo dos métodos: muitos `if`, código difícil de entender e propenso a bugs. A melhor saída é desenhar o caso normal para que trate as condições de contorno sem código extra. Exemplo: a maioria dos alunos tinha uma variável de estado dizendo se havia seleção, e o código se encheu de verificações. Com a seleção sempre existente, e "nenhuma seleção" representada por seleção vazia (início igual ao fim), copiar insere 0 bytes e apagar junta o pedaço antes e o pedaço depois da seleção, o que regenera a linha original quando ela é vazia.
**Evidence:** 6.8. Ver [[wiki/concepts/eliminar-casos-especiais]]. O cap. 10 trata as exceções, que geram ainda mais casos especiais ([[wiki/concepts/definir-erros-para-fora-da-existencia]]).
**Confidence:** alta.

### 6.9 Conclusão

**Claim:** A especialização desnecessária, em classes e métodos específicos ou em casos especiais, contribui muito para a complexidade. Não dá para eliminá-la, mas dá para reduzi-la bastante e separá-la do código geral. O resultado: classes mais profundas, melhor ocultamento e código mais óbvio.
**Evidence:** 6.9. Fecha o par com o cap. 5: lá o meio de aprofundar era esconder, aqui é generalizar, e a 6.4 mostra que um leva ao outro.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **"Sem alteração", não.** [[wiki/sources/filosofia-do-design-de-software-livro-completo]] e [[wiki/concepts/modulo-profundo]] diziam que a classe geral "serviu, sem alteração" para busca e substituição. A 6.3 diz que falta `findNext`, que o editor provavelmente já teria. Corrigido em modulo-profundo; registrado como nuance no livro completo.
- **YAGNI.** [[wiki/concepts/yagni]] diz para abstrair só depois do segundo caso de uso real. Ousterhout descreve esse argumento na 6.1 e o rejeita para a **interface**: comece um tanto geral mesmo com um uso só. Ele concorda com o YAGNI na **funcionalidade** (só o que se precisa hoje). As duas posições convivem se "abstração" no YAGNI for funcionalidade especulativa, e se chocam se for o formato da interface. Registrado nas duas páginas.
- **ISP.** [[wiki/concepts/interface-segregation-principle]] quebra interfaces gordas em interfaces menores por cliente. O cap. 6 junta vários métodos específicos em poucos gerais. Não é o mesmo eixo: o ISP fala de clientes dependendo do que não usam, o cap. 6 fala de métodos amarrados a um uso. A classe de texto especializada viola os dois, porque a UI depende de muitos métodos rasos. Leitura da wiki, sem fonte que compare os dois.
- **Tradução: `redo` ou `undo` na 6.7.** O texto traduzido diz "Cada chamada para `History.redo` caminha para trás na lista de histórico, desfazendo ações". A N.T. diz que o original impresso traz `redo` e que pela lógica deveria ser `undo`; a tradução manteve o literal. Não verificado contra o epub. Na wiki, quem anda para trás desfazendo é `undo`.
- **Tradução: "sinal de alerta" sem quadro.** A 6.5 chama de "sinal de alerta" o método feito para um uso particular, mas o capítulo não tem quadro de *red flag*. A mistura de código geral e específico vira quadro só no cap. 9 (*Special-General Mixture*, na tabela de [[wiki/concepts/red-flags-de-design]]).
- **"De uso geral" e "de propósito geral".** A tradução alterna as duas formas (título "propósito geral", 6.1 "uso geral", 6.7 "propósito geral"). A wiki usa "propósito geral" no nome da página e "um tanto de uso geral" como alias.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento]]
- [[wiki/concepts/modulo-de-proposito-geral]] (nova)
- [[wiki/concepts/eliminar-casos-especiais]] (nova)
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/ocultamento-de-informacao]]
- [[wiki/concepts/abstracao]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/yagni]]
- [[wiki/concepts/interface-segregation-principle]]
- [[wiki/concepts/command-pattern]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/reducao-de-complexidade]]
- [[wiki/concepts/definir-erros-para-fora-da-existencia]]
- [[wiki/concepts/programacao-tatica-vs-estrategica]]
- [[wiki/concepts/causas-de-complexidade-ousterhout]]

## Open Questions

- O original diz `History.undo` ou `History.redo` no parágrafo das barreiras? Conferir no epub.
- O capítulo afirma que a versão geral tem menos código no total, mas o único dado é a contagem de métodos de deletar (três para um). Há caso em que a versão geral sai maior e continua melhor? O livro não discute.
- Em que ponto "um tanto geral" vira genérico demais além do exemplo de um caractere? A terceira pergunta da 6.5 é o único teste dado.

## Raw Quotes

> "agora acredito que a superespecialização talvez seja a maior causa isolada de complexidade em software."

> "Um dos elementos mais importantes do design de software é determinar quem precisa saber o quê, e quando."

> "Uma vez feito isso, o restante do design surgiu naturalmente."
