---
type: source
title: "A Philosophy of Software Design — Livro Completo"
aliases: ["philosophy of software design completo", "ousterhout livro completo", "a philosophy of software design full book"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_file: /home/nemomartins/Documentos/new/dev-study/raw/a-philosophy-of-software-design.md
source_url: ""
author: "John Ousterhout"
date_published: "2018 (1ª ed.), 2021 (2ª ed.)"
date_ingested: 2026-07-29
source_count: 0
tags: [complexidade, arquitetura, design, ousterhout, modularidade, information-hiding, tech-debt, comentarios, naming, red-flags, clean-code]
skill: tech-mentor-backend
status: stable
---

## TL;DR

Ingestão do livro inteiro (22 capítulos), lido diretamente do epub original (não mais só o capítulo 1, já coberto por [[wiki/sources/filosofia-do-design-de-software-introducao]]). A tese central se mantém do capítulo 1 até o fim: **complexidade** (dependências + obscuridade) é o único inimigo real do design de software, e o livro inteiro é uma coleção de heurísticas para reconhecê-la e combatê-la — módulos profundos, ocultamento de informação, generalidade moderada, eliminação de casos especiais, comentários como ferramenta de design, nomeação precisa, consistência, e a distinção entre programação tática e estratégica. O livro é deliberadamente uma peça de opinião ("this book is an opinion piece"), e o próprio autor marca discordâncias explícitas com *Clean Code* (Robert Martin) em três pontos: tamanho de métodos, motivo dos comentários, e getters/setters.

**Nota sobre direitos autorais:** por instrução do usuário, este ingest **não reproduz o texto do livro na íntegra** (a página de copyright do próprio epub diz "All rights reserved. No part of this book may be reproduced..."). Este documento é resumo e paráfrase com citações curtas pontuais, seguindo o mesmo padrão de [[wiki/sources/filosofia-do-design-de-software-introducao]].

## Key Claims

**Claim:** Programar taticamente (foco em "fazer funcionar" o mais rápido possível) parece racional no curto prazo mas é a causa raiz do acúmulo de complexidade; o antídoto é a programação estratégica — investir 10–20% do tempo total de desenvolvimento em design, o que se paga sozinho dentro de 6–18 meses.
**Evidence:** Cap. 3. Ousterhout introduz o "tactical tornado" — o programador que entrega rápido mas deixa rastro de destruição que outros precisam limpar — e usa Facebook ("Move fast and break things", depois trocado para "Move fast with solid infrastructure") como exemplo real de empresa que sofreu com cultura tática, contra Google e VMware como exemplos de cultura estratégica bem-sucedida. O termo "technical debt" é usado explicitamente aqui, com a ressalva de que, ao contrário de dívida financeira, dívida técnica raramente é paga por completo.
**Confidence:** alta — capítulo inteiro dedicado ao tema, com dados qualitativos (opinião do autor, não medição controlada, o que ele mesmo admite).

**Claim:** O ocultamento de informação (information hiding, de Parnas 1972) é a técnica central para produzir módulos profundos: cada módulo deve encapsular uma decisão de design que não aparece em sua interface; o oposto — vazamento de informação (information leakage) — ocorre quando a mesma decisão de design se reflete em múltiplos módulos, criando uma dependência entre eles mesmo que nenhum dos dois exponha a informação publicamente ("back-door leakage").
**Evidence:** Cap. 5. Exemplo do servidor HTTP de um curso de design: dividir "ler a requisição" e "parsear a requisição" em duas classes obriga as duas a entenderem o formato HTTP (o Content-Length precisa ser parseado para saber onde a requisição termina), duplicando conhecimento — a correção foi fundir as duas classes. Introduz também **decomposição temporal** como causa comum de vazamento: estruturar módulos pela ordem de execução ("primeiro lemos, depois parseamos") em vez de pelo conhecimento necessário.
**Confidence:** alta — capítulo fundacional, com múltiplos sub-exemplos (parâmetros HTTP, valores default em respostas HTTP).

**Claim:** Módulos de propósito ligeiramente geral ("somewhat general-purpose") são mais profundos que módulos especializados — mesmo quando o único uso real é especializado, a versão geral tende a ter interface mais simples, menos código de implementação, e melhor ocultamento de informação.
**Evidence:** Cap. 6. Exemplo do editor de texto: uma classe de texto com métodos `backspace(cursor)` e `deleteSelection(selection)` (especializados, espelhando a UI) resultou em vazamento de informação entre UI e classe de texto; a versão generalizada, com apenas `insert(position, text)` e `delete(start, end)`, eliminou o vazamento e ainda serviu, sem alteração, para um caso de uso totalmente diferente (find-and-replace em arquivo). Regra prática: empurrar especialização para cima (UI) ou para baixo (device drivers), nunca deixá-la contaminar o núcleo genérico.
**Confidence:** alta — o autor descreve explicitamente que mudou de opinião sobre esse ponto ao longo de várias edições do curso.

**Claim:** Camadas adjacentes com abstrações parecidas são um red flag — manifestam-se como métodos pass-through (que só repassam argumentos para outro método de assinatura quase idêntica), decorators superusados, ou variáveis pass-through (que atravessam vários métodos que não as usam, só para chegar a um método de baixo nível que precisa delas).
**Evidence:** Cap. 7. Exemplo de uma classe `TextDocument` com 13 de 15 métodos públicos sendo puro pass-through para `TextArea` — sinal de divisão de responsabilidade confusa entre as duas classes. Para variáveis pass-through (ex.: certificado de segurança atravessando `main → m1 → m2 → m3`), a solução preferida do autor é um **objeto de contexto** único por instância do sistema, guardado como campo de instância nos objetos principais — mesmo reconhecendo que contextos têm as desvantagens de variáveis globais (dependências não óbvias) se usados sem disciplina.
**Confidence:** alta.

**Claim:** Quando uma complexidade é inevitável, é melhor "puxá-la para baixo" (para dentro do módulo, sofrendo o desenvolvedor do módulo) do que empurrá-la para cima (para o usuário do módulo, via exceção ou parâmetro de configuração) — a maioria dos módulos tem mais usuários que desenvolvedores.
**Evidence:** Cap. 8. Parâmetros de configuração são tratados como sintoma do problema oposto: uma desculpa fácil para não resolver algo internamente. Exemplo: em vez de expor um parâmetro de "intervalo de retry" de protocolo de rede, o protocolo pode medir o tempo de resposta de requisições bem-sucedidas e computar um valor razoável sozinho.
**Confidence:** alta.

**Claim:** A decisão de juntar ou separar dois pedaços de código deve ser guiada por complexidade total do sistema, não por regras mecânicas de tamanho ("todo método > 20 linhas deve ser quebrado"); Ousterhout discorda explicitamente de Robert Martin (*Clean Code*) nesse ponto.
**Evidence:** Cap. 9. Critérios dados: juntar se há informação compartilhada, se simplifica a interface, ou se elimina duplicação; separar se as partes são conceitualmente distintas e usadas independentemente. Cita a regra de Martin ("funções devem ser pequenas... a segunda regra é que devem ser menores ainda") e responde: "depth is more important than length: first make functions deep, then try to make them short enough to be easily read. Don't sacrifice depth for length." Introduz o red flag **Conjoined Methods** (métodos que só podem ser entendidos em conjunto).
**Confidence:** alta — desacordo explícito e nomeado, não inferido.

**Claim:** "Definir erros para fora da existência" (define errors out of existence) — redesenhar a semântica de uma operação para que a condição de erro deixe de existir — é a técnica mais eficaz para reduzir a complexidade desproporcional causada por exceções.
**Evidence:** Cap. 10. Três exemplos concretos: (1) o comando `unset` do Tcl, que o próprio autor admite ter sido um erro de design ao lançar erro para variável inexistente, em vez de simplesmente garantir que a variável não existe mais; (2) deleção de arquivo aberto no Unix (adia a deleção até o último handle fechar) vs. Windows (recusa a deleção, obrigando o usuário a caçar e matar o processo); (3) `substring` do Java, que lança `IndexOutOfBoundsException` para índices fora do intervalo, em vez de simplesmente truncar como Python faz em list slices. Um estudo citado (Yuan et al., USENIX OSDI 2014) encontrou que mais de 90% das falhas catastróficas em sistemas distribuídos vieram de tratamento de erro incorreto — não do erro em si.
**Confidence:** alta — um dos capítulos mais citável do livro, com estudo empírico externo referenciado.

**Claim:** Além de definir erros para fora da existência, há três técnicas complementares para reduzir onde exceções precisam ser tratadas: **mascarar** (tratar no nível mais baixo possível, ex.: TCP reenviando pacotes perdidos sem expor isso ao chamador; NFS travando a aplicação em vez de propagar erro de servidor fora do ar), **agregar** (um único handler no topo captura várias exceções distintas, ex.: parâmetros ausentes de URL em um servidor HTTP; RAMCloud "promove" erros pequenos — objeto corrompido — para o mesmo mecanismo de recuperação de crash de servidor inteiro, reduzindo a quantidade de mecanismos de recuperação distintos), e **simplesmente travar a aplicação** quando não há nada sensato a fazer (memória esgotada, erro de I/O em disco).
**Evidence:** Cap. 10, seções 10.6–10.8, com exemplos de TCP, NFS, RAMCloud e `malloc`/`ckalloc` em C.
**Confidence:** alta.

**Claim:** "Projetar duas vezes" (design it twice) — considerar ao menos duas alternativas radicalmente diferentes antes de escolher uma interface ou implementação — produz designs melhores mesmo quando a primeira ideia parece obviamente correta, e o hábito de nunca considerar uma segunda alternativa é uma armadilha comum de pessoas muito inteligentes.
**Evidence:** Cap. 11. Exemplo recorrente do livro (classe de texto de editor): comparar interface line-oriented, character-oriented e range-oriented explicitamente lado a lado leva a identificar os defeitos de cada uma e chegar à terceira, superior. O autor estima que o exercício raramente custa mais que 1–2 horas para uma classe pequena.
**Confidence:** alta.

**Claim:** Comentários não são um "mal necessário" (discordância explícita de *Clean Code*) — são a única forma de capturar a parte informal de uma abstração (o que não pode ser expresso em código), e por isso são fundamentais, não um sintoma de fracasso de design.
**Evidence:** Cap. 12. Cita diretamente Robert Martin: "comments are, at best, a necessary evil... comments are always failures." Ousterhout responde que código não consegue expressar tudo (unidades, pré-condições, efeitos colaterais, motivo de uma decisão) e que a alternativa de Martin (extrair blocos em métodos com nomes longos tipo `isLeastRelevantMultipleOfNextLargerPrimeFactor`) produz nomes crípticos que fornecem menos informação que um comentário bem escrito, além de obrigar o leitor a "retipar" a documentação toda vez que o método é invocado.
**Confidence:** alta — segunda discordância nomeada e explícita com Robert Martin.

**Claim:** Comentários bons descrevem coisas que não são óbvias a partir do código — nem repetindo o código (mesmo nível de detalhe) nem ficando vagos; a interface de um método deve ser documentável de forma completa mas simples, e se isso for difícil, é sinal (red flag "Hard to Describe") de que o próprio design tem um problema.
**Evidence:** Cap. 13. Exemplo extenso da classe `IndexLookup` de um sistema de storage distribuído: a primeira versão do comentário de interface vazava detalhes de implementação (nomes de RPCs internos, parâmetros de configuração privados) — a versão corrigida foca só no que o usuário da classe precisa saber. Red flag nomeado: "Implementation Documentation Contaminates Interface".
**Confidence:** alta.

**Claim:** A prática de "escrever os comentários primeiro" (antes do corpo do método) não é só sobre qualidade da documentação — é uma ferramenta de design: forçar-se a escrever o comentário de interface antes da implementação expõe cedo se a abstração é boa (comentário curto e completo) ou ruim (comentário longo, ou que precisa descrever implementação para ficar completo).
**Evidence:** Cap. 15. O autor descreve seu próprio processo: interface da classe → assinaturas e comentários dos métodos públicos mais importantes (corpo vazio) → variáveis de instância → só então os corpos dos métodos. Argumenta que adiar comentários para o fim do projeto quase garante que eles nunca sejam escritos ou sejam de baixa qualidade, porque o contexto de design já foi esquecido.
**Confidence:** alta.

**Claim:** Nomes precisos e usados de forma consistente evitam bugs reais, não só melhoram legibilidade — Ousterhout discorda explicitamente do guia de estilo de nomenclatura do Go (que recomenda nomes curtos, até de uma letra).
**Evidence:** Cap. 14. Conta a história de um bug de 6 meses no sistema operacional distribuído Sprite: a variável `block` era usada tanto para bloco físico em disco quanto para bloco lógico dentro de um arquivo — os dois sentidos se confundiram em um ponto do código e um bloco de disco não relacionado foi zerado. O autor cita e rebate Andrew Gerrand (Go): "long names obscure what the code does" — para Ousterhout, legibilidade é julgada por quem lê, não por quem escreve, e nomes ambíguos (`ch`, `d`) tendem à confusão do mesmo tipo do bug do `block`.
**Confidence:** alta — terceira discordância explícita e nomeada (desta vez com a comunidade Go, não com Robert Martin).

**Claim:** Ao modificar código existente, "ficar estratégico" significa deixar o sistema com a estrutura que teria se tivesse sido projetado desde o início considerando aquela mudança — não fazer "a menor alteração possível que funcione".
**Evidence:** Cap. 16. Reforça a distinção tática/estratégica do Cap. 3 aplicada a manutenção contínua, e dá regras concretas para manter comentários atualizados: colocá-los perto do código que descrevem (não em arquivos de cabeçalho distantes), documentar no código, não na mensagem de commit, evitar duplicação (usar um arquivo central `designNotes` para decisões cross-module sem lugar óbvio, como o caso de "zombie servers" no RAMCloud), e revisar o diff antes de commitar para checar se a documentação ainda bate com o código.
**Confidence:** alta.

**Claim:** Consistência (mesmos nomes, mesmo estilo, mesmos padrões para situações similares) cria alavancagem cognitiva: uma vez aprendido um padrão, o leitor pode assumir com segurança que ele se repete em outro lugar — o oposto (inconsistência) faz suposições familiares se tornarem perigosas.
**Evidence:** Cap. 17. Regras práticas: documentar convenções em lugar visível, automatizar checagem (ex.: script pre-commit que rejeita commits com caractere de retorno de carro, resolvendo um problema real de terminadores de linha Unix/Windows em um projeto do autor), seguir "quando em Roma, faça como os romanos" ao entrar em código novo, e nunca mudar uma convenção estabelecida só porque "tenho uma ideia melhor" sem justificativa forte o bastante para atualizar todos os usos antigos.
**Confidence:** alta.

**Claim:** Herança de implementação (não herança de interface) é uma fonte relevante de complexidade porque cria dependências bidirecionais entre classe pai e subclasses (vazamento de informação via variáveis de instância compartilhadas); TDD é tática, não estratégica, porque foca em fazer o próximo teste passar, não em desenhar a abstração inteira de uma vez; design patterns e getters/setters são bons só quando usados com critério, não por hábito.
**Evidence:** Cap. 19 ("Software Trends"), que avalia OOP/herança, agile, unit tests, TDD, design patterns e getters/setters pela mesma régua de complexidade do resto do livro. Sobre TDD: "the units of development should be abstractions, not features... don't create the abstraction in pieces over time; design it all at once." Sobre getters/setters: são métodos rasos que expõem estado interno — a exposição em si é o problema de design, não a ausência do getter/setter.
**Confidence:** alta — capítulo de síntese que aplica os princípios anteriores a modismos de indústria.

**Claim:** Simplicidade e performance não são opostos — código mais simples costuma ser mais rápido (menos casos especiais, menos cruzamentos de camada), e quando performance realmente importa, a técnica é desenhar em torno do "caminho crítico" (a menor quantidade de código para o caso comum), isolando casos especiais fora dele.
**Evidence:** Cap. 20. Estudo de caso real: a classe `Buffer` do sistema RAMCloud foi redesenhada em torno do caminho crítico de alocação, reduzindo de 6 checagens de condição e 3 chamadas de método para 1 checagem (via a nova variável `availableAppendBytes`) e 1 método — resultado: 2x mais rápido (8.8ns → 4.75ns por operação) e 20% menos código (1886 → 1476 linhas). A régua geral: nunca otimizar por intuição, sempre medir antes e depois.
**Confidence:** alta — exemplo com números concretos de medição, não só argumento qualitativo.

**Claim:** Uma habilidade central de design é separar o que importa do que não importa e estruturar o sistema em torno do que importa — erros de design em ambas as direções (tratar coisas demais como importantes, ou não perceber que algo importante precisa ser exposto) causam problemas distintos.
**Evidence:** Cap. 21, capítulo de fechamento antes da conclusão. Reusa o exemplo da interface Java de I/O (Cap. 4): forçar todo desenvolvedor a saber sobre buffering (quase sempre desejado) é tratar algo sem importância como importante. Conecta explicitamente com escrita técnica e com "bom gosto" como capacidade central de um bom designer de software.
**Confidence:** alta.

## Entities & Concepts Touched

- [[wiki/entities/john-ousterhout]]
- [[wiki/concepts/modulo-profundo]]
- [[wiki/concepts/ocultamento-de-informacao]]
- [[wiki/concepts/tech-debt-como-ferramenta]]
- [[wiki/concepts/refatoracao]]
- [[wiki/concepts/naming]]
- [[wiki/concepts/red-flags-de-design]]
- [[wiki/concepts/definir-erros-para-fora-da-existencia]]
- [[wiki/concepts/projetar-duas-vezes]]
- [[wiki/concepts/comentarios-como-ferramenta-de-design]]
- [[wiki/concepts/decidir-o-que-importa]]
- [[wiki/concepts/arquitetura-de-software]]
- [[wiki/concepts/modelo-cascata-vs-desenvolvimento-incremental]]
- [[wiki/concepts/code-review]]
- [[wiki/concepts/complexidade-acidental]]

## Open Questions

- O capítulo introdutório já ingerido ([[wiki/sources/filosofia-do-design-de-software-introducao]]) marcava como lacuna em aberto o conceito de "define errors out of existence" e o restante do livro — ambos agora cobertos aqui; essa fonte substitui a lacuna daquela página (atualizada com backlink).
- O livro é explicitamente uma peça de opinião pessoal do autor ("this book is an opinion piece"), sem medição controlada para a maioria das afirmações centrais (ex.: os 10–20% de investimento em design, ou o prazo de 6–18 meses para o payback da programação estratégica) — vale marcar essas cifras como heurística de experiência pessoal, não resultado empírico, ao citá-las em outras páginas.
- O wiki tem hoje duas páginas de conceito paralelas e não fundidas para o mesmo conceito: [[wiki/concepts/complexidade-acidental]] (estável, 4 fontes) e uma página em inglês `accidental-complexity.md` (não tocada neste ingest) — possível achado de lint a resolver depois (fundir ou desambiguar).

## Raw Quotes

> "Complexity is caused by two things: dependencies and obscurity." (Cap. 2, retomado ao longo de todo o livro)

> "The most important thing is the long-term structure of the system... your primary goal must be to produce a great design, which also happens to work." (Cap. 3)

> "Comments are always failures. We must have them because we can't always figure out how to express ourselves without them, but their use is not a cause for celebration." — Robert Martin, citado no Cap. 12 e rebatido pelo autor.

> "Depth is more important than length: first make functions deep, then try to make them short enough to be easily read. Don't sacrifice depth for length." (Cap. 9, resposta direta a *Clean Code*)

> "Code that hasn't been executed doesn't work." (Cap. 10, sobre por que código de tratamento de exceção raramente funciona na primeira tentativa real)
