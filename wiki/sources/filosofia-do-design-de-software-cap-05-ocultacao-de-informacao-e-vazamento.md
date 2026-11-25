---
type: source
title: "A Filosofia do Design de Software — Cap. 5: Ocultação de Informação (e Vazamento)"
aliases: ["philosophy of software design cap 5", "ousterhout capítulo 5", "information hiding and leakage", "ocultação de informação e vazamento"]
date_created: 2026-11-25
date_updated: 2026-11-25
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/filosofia-do-design-de-software-cap-05-ocultacao-de-informacao-e-vazamento.md
source_url: ""
author: "John Ousterhout (tradução do usuário)"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-11-25
source_count: 0
tags: [design, ousterhout, traducao, information-hiding, vazamento-de-informacao, decomposicao-temporal, api-design, http, parnas]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Tradução do usuário do capítulo 5 de *A Philosophy of Software Design*, de [[wiki/entities/john-ousterhout]], com a introdução e as seções 5.1 a 5.10. O capítulo apresenta a primeira técnica para chegar a [[wiki/concepts/modulo-profundo|módulos profundos]]: o [[wiki/concepts/ocultamento-de-informacao|ocultamento de informação]], de [[wiki/entities/david-parnas]] (1972). Cada módulo esconde uma ou poucas decisões de design. O oposto é o **vazamento**: a mesma decisão refletida em vários módulos, pela interface ou "pela porta dos fundos". Uma causa comum de vazamento é a [[wiki/concepts/decomposicao-temporal|decomposição temporal]], que estrutura o código pela ordem de execução. Os exemplos vêm de projetos de alunos que implementaram um servidor HTTP: duas classes para ler e analisar a requisição, `getParams()` devolvendo o `Map` interno, e a versão HTTP exigida do chamador em vez de vir como valor padrão. O capítulo fecha com dois limites: ocultar também vale dentro de uma classe, e não se esconde o que é necessário fora do módulo. Continua direto o cap. 4 ([[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]]), que definiu interface e profundidade. A wiki já conhecia o capítulo pelo [[wiki/sources/filosofia-do-design-de-software-livro-completo]]. A leitura de primeira mão corrige duas frases da wiki.

## Key Claims

### Introdução e 5.1 Ocultação de informação

**Claim:** Cada módulo deve encapsular alguns conhecimentos que representam decisões de design. O conhecimento fica na implementação e não aparece na interface. Os exemplos do livro: como guardar dados numa árvore B, como achar o bloco físico de um bloco lógico, como implementar TCP, como agendar *threads* num processador *multi-core*, como fazer *parsing* de JSON. A informação escondida inclui estruturas de dados, algoritmos, detalhes de baixo nível (tamanho de página) e premissas de alto nível ("a maioria dos arquivos é pequena").
**Evidence:** 5.1, primeiro a terceiro parágrafos. A técnica é atribuída ao artigo de Parnas de 1972 (nota de rodapé na 5.10).
**Confidence:** alta.

**Claim:** O ocultamento reduz a complexidade de duas formas. Simplifica a interface, o que diminui a [[wiki/concepts/carga-cognitiva]] de quem usa o módulo (quem usa uma árvore B não pensa no *fanout*). E facilita a evolução: se não há dependência fora do módulo, uma mudança de design afeta só ele (uma mudança no controle de congestionamento do TCP não toca o código que envia e recebe dados).
**Evidence:** 5.1, quarto parágrafo. São os dois sintomas do cap. 2 vistos pelo lado da solução: carga cognitiva e amplificação de mudanças ([[wiki/concepts/sintomas-de-complexidade-ousterhout]]).
**Confidence:** alta.

**Claim:** Declarar atributos e métodos como `private` **não** é ocultar informação. `private` ajuda, porque impede o acesso direto, mas *getters* e *setters* públicos expõem a natureza e o uso da variável "tão expostos quanto se elas fossem públicas".
**Evidence:** Nota da 5.1. Entra em tensão com [[wiki/concepts/encapsulamento]], que tratava getters e setters como a forma de uma classe definir sua interface (ver Contradições).
**Confidence:** alta.

**Claim:** O melhor caso é a informação totalmente escondida, irrelevante e invisível para o usuário. A ocultação **parcial** também vale: um recurso que só alguns usuários precisam, acessado por métodos separados, quase não cria dependência nos casos comuns.
**Evidence:** 5.1, último parágrafo. A 5.7 usa os valores padrão como exemplo de ocultação parcial.
**Confidence:** alta.

### 5.2 Vazamento de informação

**Claim:** Vazamento é quando uma decisão de design se reflete em mais de um módulo. Mudar a decisão exige mudar todos. Informação que aparece na interface já vazou, por definição; por isso interfaces mais simples tendem a esconder melhor. Mas a informação também vaza sem aparecer na interface: duas classes que conhecem o mesmo formato de arquivo (uma lê, outra escreve). Esse vazamento "pela porta dos fundos" é pior que o da interface porque não é óbvio.
**Evidence:** 5.2, primeiro parágrafo. O vazamento pela porta dos fundos é dependência somada a obscuridade, as duas causas do cap. 2 ([[wiki/concepts/causas-de-complexidade-ousterhout]]).
**Confidence:** alta.

**Claim:** O vazamento é um dos principais sinais de alerta ([[wiki/concepts/red-flags-de-design]]). Para corrigir, pergunte como reorganizar as classes para que o conhecimento afete uma só. Duas saídas: fundir as classes, se forem pequenas e ligadas à informação; ou extrair a informação para uma classe nova. A extração só vale se a nova classe tiver interface simples. Se ela expuser quase tudo, você trocou o vazamento pela porta dos fundos por um vazamento pela interface.
**Evidence:** 5.2, segundo parágrafo.
**Confidence:** alta.

### 5.3 Decomposição temporal

**Claim:** Decomposição temporal é estruturar o sistema pela ordem cronológica das operações. Exemplo: ler um arquivo, modificar, gravar de volta, cada etapa numa classe. Leitura e gravação conhecem o formato, e o formato vaza. A correção é juntar leitura e gravação numa classe só, usada nas duas fases. É fácil cair nisso porque a ordem das operações está na cabeça de quem programa.
**Evidence:** 5.3, primeiro parágrafo. O texto diz "uma causa **comum**", não "a mais comum" (ver Contradições). Ver [[wiki/concepts/decomposicao-temporal]].
**Confidence:** alta.

**Claim:** A ordem importa e vai aparecer em algum lugar do código, mas não deveria definir a estrutura dos módulos, a não ser que as etapas usem informações totalmente distintas. Ao projetar módulos, pense no conhecimento de cada tarefa, não na ordem das tarefas.
**Evidence:** 5.3. Na tradução, esse parágrafo está dentro da caixa "Sinal de Alerta: Vazamento de Informações". Pelo conteúdo, parece texto corrido da seção que foi parar na caixa na conversão do layout. Não verificado contra o original.
**Confidence:** alta quanto ao conteúdo; baixa quanto à posição no livro.

### 5.4 e 5.5 Servidor HTTP e classes demais

**Claim:** Os exemplos vêm de alunos de um curso de design de software que implementaram classes para servidores receberem requisições HTTP e enviarem respostas. A Figura 5.1 mostra a anatomia de uma requisição POST: linha inicial (método, URL, parâmetros, versão), cabeçalhos terminados por linha em branco e corpo opcional.
**Evidence:** 5.4 e Figura 5.1. Ver [[wiki/concepts/requisicao-http]].
**Confidence:** alta.

**Claim:** O erro mais comum dos alunos foi dividir o código em muitas classes rasas, a [[wiki/concepts/classite]] do cap. 4 num caso concreto. Uma equipe usou uma classe para ler a requisição da rede numa string e outra para analisar a string. É decomposição temporal ("primeiro lemos, depois analisamos"). Como o `Content-Length` diz o tamanho do corpo, não dá para ler a requisição sem analisar boa parte dela. As duas classes entendiam o formato HTTP e o código de análise ficou duplicado. Os chamadores ainda precisavam chamar dois métodos de classes diferentes numa ordem específica.
**Evidence:** 5.5, primeiro parágrafo. A ordem obrigatória de chamadas é o que a wiki chama de [[wiki/concepts/temporal-coupling]]: a decomposição temporal vazou para a interface.
**Confidence:** alta.

**Claim:** "Teria sido melhor" fundir as duas classes. Isso isola o formato numa classe e reduz a interface a um método. Tema geral: o ocultamento muitas vezes melhora quando a classe fica **um pouco maior**. Por dois motivos: juntar todo o código de uma capacidade, e subir o nível da interface (um método que faz o processamento inteiro em vez de um por etapa). Levar isso ao extremo (uma classe para a aplicação inteira) é ruim, e o cap. 9 discute quando separar.
**Evidence:** 5.5, segundo a quarto parágrafos. O livro recomenda a fusão; não diz que a equipe a fez (ver Contradições). Contraria a regra "classes pequenas" de *Clean Code* ([[wiki/entities/uncle-bob]]), desacordo que o livro explicita no cap. 9.
**Confidence:** alta.

### 5.6 Parâmetros HTTP

**Claim:** A maioria dos alunos acertou duas coisas. Escondeu se o parâmetro veio da linha inicial ou do corpo, mesclando os dois. E escondeu o *URL encoding*: o servidor recebe "What a cute baby!", não "What+a+cute+baby%21".
**Evidence:** 5.6, primeiro e segundo parágrafos.
**Confidence:** alta.

**Claim:** A maioria errou a interface de leitura: `getParams()` devolvia a referência ao `Map<String, String>` interno. O método é raso e expõe a representação interna, então mudar a representação muda a interface e todos os chamadores. Também dá mais trabalho ao chamador (pegar o `Map`, depois o parâmetro) e cria uma armadilha: modificar o `Map` altera o estado interno do `HTTPRequest`. A interface melhor é `getParameter(name)` e `getIntParameter(name)`, que escondem a representação e a conversão de tipo, e lançam exceção se o parâmetro não existir ou não converter.
**Evidence:** 5.6, terceiro a quinto parágrafos, com os dois trechos de Java. É o caso concreto da nota da 5.1: o `getParams` é um getter que expõe a variável como se fosse pública.
**Confidence:** alta.

### 5.7 Valores padrão em respostas HTTP

**Claim:** O erro mais comum nas respostas foram valores padrão ruins. Uma equipe exigia que o chamador informasse a versão HTTP da resposta, mas ela tem de ser a da requisição, que já é passada ao enviar a resposta. A biblioteca deveria preencher a versão sozinha; se o chamador informar, a informação vaza entre biblioteca e chamador. O mesmo vale para o cabeçalho `Date`.
**Evidence:** 5.7, primeiro parágrafo.
**Confidence:** alta.

**Claim:** Valores padrão tornam o caso comum o mais simples possível e são ocultação parcial: o chamador normal nem sabe que o item existe; o raro que precisa trocar o valor chama um método específico. As classes devem "fazer a coisa certa" sem ser pedidas. O contraexemplo é o *buffer* do Java I/O (4.7, a "página 26" do texto): tão universal que ninguém deveria ter de pedir. "As melhores funcionalidades são aquelas que você obtém sem sequer saber que existem."
**Evidence:** 5.7, segundo e terceiro parágrafos, e a caixa **Superexposição**: a API de um recurso comum não deve obrigar o usuário a aprender recursos raros. A mesma ideia, no nível de plataforma, está em [[wiki/concepts/sensible-defaults-paved-road]].
**Confidence:** alta.

### 5.8 a 5.10 Dentro da classe, limites e conclusão

**Claim:** O ocultamento também vale dentro de uma classe. Cada método privado deve esconder alguma informação do resto da classe, e cada variável de instância deve ser usada no menor número possível de lugares. Menos lugares, menos dependências internas.
**Evidence:** 5.8.
**Confidence:** alta.

**Claim:** Só faz sentido esconder o que não é necessário fora do módulo. Se diferentes usos exigem ajustes diferentes de parâmetros de desempenho, eles precisam estar na interface. O objetivo é minimizar o que se precisa saber de fora; um módulo que se ajusta sozinho é melhor que um que expõe parâmetros. Mas o que é necessário fora tem de ser exposto.
**Evidence:** 5.9. Antecipa o cap. 8 (puxar a complexidade para baixo), que o livro completo resume como "parâmetros de configuração são sintoma" ([[wiki/sources/filosofia-do-design-de-software-livro-completo]]).
**Confidence:** alta.

**Claim:** Ocultamento e módulos profundos andam juntos: esconder muito aumenta a funcionalidade e reduz a interface. Um módulo que esconde pouco tem pouca funcionalidade ou interface complexa, e de qualquer jeito é raso. Ao decompor, não se guie pela ordem de execução; pense nos pedaços de conhecimento e dê a cada módulo um ou alguns deles.
**Evidence:** 5.10.
**Confidence:** alta.

## Contradições e nuances com a wiki

- **"Uma causa comum", não "a causa mais comum".** [[wiki/concepts/ocultamento-de-informacao]] tinha a seção "Decomposição temporal — a causa mais comum de vazamento", e o index repetia isso. O texto diz "uma causa comum". Corrigido nas duas.
- **"Teria sido melhor" fundir.** A mesma página e o [[wiki/sources/filosofia-do-design-de-software-livro-completo]] diziam "a correção foi fundir as duas classes", como se a equipe tivesse feito. O livro só recomenda. Corrigido na página de conceito; no livro completo ficou registrado como nuance.
- **Getters e setters não são interface de encapsulamento.** [[wiki/concepts/encapsulamento]] abre com a analogia de [[wiki/sources/monolito-modular-transicao-mvp-empresa-madura]]: "uma classe expõe getters e setters definindo como o mundo externo interage com ela". Para Ousterhout, getters e setters deixam a variável tão exposta quanto se fosse pública. A mesma página já tinha a correção de [[wiki/sources/encapsulamento-proteger-estado-invalido]] ("um `setPrice` que só atribui não protege nada"), por outro motivo: lá o problema é a invariante, aqui é a dependência. As duas críticas convergem.
- **Encapsulamento e ocultamento não são sinônimos.** A N.T. da 5.2 diz que no Brasil "encapsulamento" também descreve o mesmo princípio, e [[wiki/concepts/encapsulamento]] tem "information hiding" como alias. A nota da 5.1 separa os dois: `private` (o mecanismo) não garante ocultamento (o objetivo). A wiki mantém duas páginas, com remissão entre elas.
- **Decomposição temporal ≠ temporal coupling.** Os nomes se parecem, mas são coisas diferentes. A decomposição temporal é um critério de modularização (estrutura segue o tempo). O [[wiki/concepts/temporal-coupling]] é uma ordem de chamada implícita. Na 5.5, a primeira causou a segunda: quem chamava tinha de chamar ler antes de analisar.
- **Classes maiores.** "O ocultamento muitas vezes pode ser melhorado tornando uma classe um pouco maior" contraria a regra de classes pequenas de *Clean Code* ([[wiki/entities/uncle-bob]]). O livro completo já registra o desacordo com Robert Martin no cap. 9; o cap. 5 é a primeira aparição dele.
- **Tradução: nomes das caixas.** As caixas das seções 5.3 e 5.4 dizem "Sinal de Alerta"; a da 5.7 diz "Bandeira Vermelha". O original usa *Red Flag* nas três. A N.T. da 5.3 explica a escolha por "Sinal de Alerta".
- **Tradução: posição das caixas.** A caixa de Vazamento está na 5.3 e a de Decomposição Temporal na 5.4, cada uma uma seção depois do tema. No livro as caixas flutuam no layout, o que explica o deslocamento. O parágrafo "A ordem geralmente importa…" está dentro da caixa de vazamento, mas parece texto corrido da 5.3. Não verificado contra o original.
- **"ocultamento" e "ocultação".** A tradução usa as duas formas (5.1 "ocultação", 5.5 "ocultamento"). A página de conceito da wiki usa "ocultamento" e ganhou "ocultação de informação" como alias.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/entities/david-parnas]] (nova)
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]]
- [[wiki/sources/filosofia-do-design-de-software-cap-04-modulos-devem-ser-profundos]]
- [[wiki/concepts/classite]]
- [[wiki/entities/uncle-bob]]
- [[wiki/concepts/ocultamento-de-informacao]]
- [[wiki/concepts/decomposicao-temporal]] (nova)
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/encapsulamento]]
- [[wiki/concepts/modelo-de-dominio-anemico]]
- [[wiki/concepts/temporal-coupling]]
- [[wiki/concepts/sensible-defaults-paved-road]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/causas-de-complexidade-ousterhout]]
- [[wiki/concepts/sintomas-de-complexidade-ousterhout]]
- [[wiki/concepts/acoplamento]]
- [[wiki/concepts/requisicao-http]]

## Open Questions

- O parágrafo "A ordem geralmente importa…" está mesmo dentro da caixa de *Red Flag* no original, ou é texto corrido da 5.3? Conferir no epub.
- A 5.9 diz para expor parâmetros que diferentes usos precisam ajustar. Como isso convive com o "parâmetros de configuração são sintoma" do cap. 8? A resposta provável é a da própria 5.9 (ajustar sozinho é melhor; expor só o que não dá para ajustar), mas fica para conferir quando o cap. 8 chegar.
- `getIntParameter` e companhia multiplicam métodos por tipo. Numa linguagem com genéricos, um `getParameter<T>` esconderia o mesmo com uma interface menor? O livro não discute.

## Raw Quotes

> "Um vazamento 'pela porta dos fundos' como esse é mais pernicioso do que o vazamento por meio de uma interface, porque não é óbvio."

> "Ao projetar módulos, concentre-se no conhecimento necessário para executar cada tarefa, e não na ordem em que as tarefas ocorrem."

> "As melhores funcionalidades são aquelas que você obtém sem sequer saber que existem."
