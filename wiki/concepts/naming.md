---
type: concept
title: "Naming"
aliases: ["nomeação", "naming things", "nomear variáveis", "nomes ruins"]
date_created: 2026-04-26
date_updated: 2026-11-25
source_count: 11
tags: [naming, clean-code, craftsmanship, legibilidade, carreira]
skill: tech-mentor-leadership
status: draft
---

# Naming

Nomear bem é uma das habilidades mais subestimadas em desenvolvimento. Nomes ruins compõem **dívida cognitiva permanente** — cada leitura futura do código custa mais do que custaria ter passado 5 minutos pensando no nome certo.

## Por que é difícil

[[wiki/entities/phil-karlton|Phil Karlton]]: *"There are only two hard things in Computer Science: cache invalidation and naming things."* — citação sem fonte primária confirmada; ver o histórico da própria frase e suas variações em [[wiki/concepts/two-hard-things]] (fonte: [[wiki/sources/two-hard-things-martin-fowler]]).

Nomear bem exige entender completamente o que o código faz. Se você não consegue nomear claramente, é sinal de que não entende o suficiente ainda.

## Anti-padrões comuns

| Nome ruim | Problema | Alternativa |
|---|---|---|
| `doStuff()` | Nenhuma informação sobre o que faz | `processPaymentWebhook()` |
| `data`, `data2` | Genérico — qualquer coisa é dado | `validatedUserInput`, `rawApiResponse` |
| `manager` | Faz tudo, não diz nada | `SessionStore`, `PermissionChecker` |
| `handler` | Qual evento? Qual entidade? | `handleUserCreatedEvent` |
| `info` | De quem? Sobre o quê? | `userProfileMetadata` |

## Regra prática

> Gaste 5 minutos no nome → economize 5 horas depois.

Se 6 meses atrás você não entende o que `data2` significa, nomeie agora. Se você não consegue nomear algo de forma clara, é um sinal de que você deve refatorar antes de nomear.

## O bug de 6 meses causado por um nome ambíguo (Ousterhout)

[[wiki/sources/filosofia-do-design-de-software-livro-completo]] (Cap. 14) conta o bug mais difícil que [[wiki/entities/john-ousterhout]] já corrigiu: no sistema operacional distribuído Sprite, a variável `block` era usada tanto para bloco físico em disco quanto para bloco lógico dentro de um arquivo. Em um ponto do código os dois sentidos se confundiram e um bloco de disco não relacionado foi zerado silenciosamente. Vários desenvolvedores leram o código com o bug sem notar o problema — o nome ambíguo fazia todo mundo assumir, por reflexo, que `block` significava o que "fazia sentido" ali. Levou 6 meses para encontrar. Nomes como `fileBlock` e `diskBlock` (ou tipos distintos para os dois) teriam tornado o erro impossível de compilar.

**Duas propriedades de bom nome, segundo o livro:** precisão (evitar genéricos como `count`, `result`, `status` sem contexto) e consistência (mesmo nome, mesmo propósito, sempre — nunca reaproveitar um nome comum para algo com comportamento diferente).

**Discordância explícita com o guia de estilo do Go:** Andrew Gerrand (Go) defende nomes curtos, às vezes de uma letra, argumentando que "nomes longos obscurecem o que o código faz". Ousterhout rebate citando um exemplo do próprio Go (`i`, `n` vs. `index`, `count`) e argumenta que legibilidade deve ser julgada por quem lê, não por quem escreve — e que a cultura Go de reaproveitar nomes curtos ambíguos (`ch` para "character" ou "channel", `d` para "data", "difference" ou "distance") é o mesmo tipo de risco que causou o bug do `block`. Concorda, porém, com uma regra do próprio Gerrand: "quanto maior a distância entre a declaração de um nome e seus usos, mais longo o nome deveria ser" — o que explica por que `i`/`j` são aceitáveis em loops curtos, mas não em variáveis de escopo amplo.

## Números Mágicos: Naming Aplicado a Constantes

[[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] trata "número mágico" (e "coisas mágicas" em geral — URLs e chaves de API hard-coded) como um problema de naming, não um smell separado: `if user.age >= 16` sem contexto nenhum sofre do mesmo problema central desta página — falta de um nome que carregue significado. A diferença prática de uma constante nomeada (`LEGAL_BEER_BUYING_AGE_GERMANY = 16`) não é só legibilidade — é **manutenção mecânica**: buscar `16` no código inteiro retorna falsos positivos (`1600`, outros usos coincidentes do mesmo número), enquanto buscar o nome da constante é inequívoco. É o argumento de "precisão" já registrado acima (Ousterhout) aplicado especificamente a valores literais em vez de variáveis.

## Relacionado

[[wiki/sources/habitos-ruins-de-programador]] · [[wiki/concepts/testar-proprio-codigo]] · [[wiki/concepts/red-flags-de-design]] (Vague Name, Hard to Pick Name)

## Nomes de classe CSS (FrontPUSH)

Em [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]], [[wiki/entities/nasser|Násser]] chama de boa prática a "árvore de classes" (o filho leva o nome do pai: `nav` → `nav-item` → `nav-link`) e corrige a si mesmo por misturar português e inglês ("isso aqui não é legal"). `[external]` É a ideia do BEM (https://getbem.com/naming/).

## Identificadores em JavaScript (JavaScript Ninja)

Em [[wiki/sources/javascript-ninja-estrutura-lexica]], a regra mecânica antes do estilo: nomes começam com letra, `_` ou `$` e depois aceitam dígitos; `var π = 3.14` funciona, "mas você não deve utilizar", porque o próximo desenvolvedor pode não ter como "ditar" aquele código. Letras, dígitos, `_` e `$` deixam "o código mundialmente fácil [de] digitar" ([[wiki/concepts/identificadores-javascript]]).

## Nomes de função (JavaScript Ninja, semana 8)

Em [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]], o curso passa a exigir nome em toda função atribuída a variável, "de preferência o mesmo nome" da variável, "para ficar mais facilmente encontrada". O motivo é de ferramenta: o debugger mostra o nome da função, não o da variável. `[external]` O nome de uma *function expression* só existe dentro dela (serve para recursão); fora, vale a variável. Repetir o nome evita dois nomes para a mesma coisa.

## Nomes de função (JavaScript Ninja, semana 8, vídeo 03)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]], a função interna do `adder` é retornada anônima, dois vídeos depois de o curso adotar "sempre nomear". `[external]` A inferência do ES2015 não cobre o `return`: `add2.name` dá `''` (verificado). É exatamente o caso em que dar nome (`return function addY(y) {...}`) ajuda no stack trace.

## Nomes de função (JavaScript Ninja, semana 8, vídeo 04)

Em [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]], o callback passado direto pode ter nome "ou não, tanto faz", e a aula usa anônima "só para ficar menos coisa escrita". É a terceira exceção à regra de nomear em três vídeos. `[external]` O callback passado direto é o caso em que a falta de nome mais pesa no stack trace.

## Key Sources

- [[wiki/sources/two-hard-things-martin-fowler]] — origem (incerta) e curadoria da citação de Phil Karlton sobre naming como um dos dois problemas difíceis
- [[wiki/sources/5-principios-programador]]
- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — bug do `block` no Sprite; discordância com o guia de estilo de nomes do Go
- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] — números mágicos e valores hard-coded (URLs, chaves de API) como falta de naming; busca textual ambígua vs. busca por nome de constante
- [[wiki/sources/o-que-diferencia-pleno-de-junior-decisoes-legibilidade-modelagem]] — `double d` vs `valorDescontoPedido`: em método longo, a variável alterada várias vezes longe da declaração pesa na leitura
- [[wiki/sources/frontpush-flexbox-pratica-1-layout-youtube-estrutura-html]]: "árvore de classes" (prefixo do pai) e não misturar português com inglês
- [[wiki/sources/javascript-ninja-estrutura-lexica]]: JavaScript Ninja, semana 2, vídeo 03: regras de identificador e nomes só em ASCII
- [[wiki/sources/javascript-ninja-a-importancia-de-nomear-funcoes]]: JavaScript Ninja, semana 8, vídeo 01: nomear funções, de preferência com o nome da variável
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-2]]: JavaScript Ninja, semana 8, vídeo 03: função retornada sem nome, contra a regra de dois vídeos antes
- [[wiki/sources/javascript-ninja-programacao-funcional-parte-3]]: JavaScript Ninja, semana 8, vídeo 04: callback anônimo, "tanto faz" o nome
