---
type: concept
title: "Naming"
aliases: ["nomeação", "naming things", "nomear variáveis", "nomes ruins"]
date_created: 2026-04-26
date_updated: 2026-08-21
source_count: 6
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

[[sources/habitos-ruins-de-programador]] · [[concepts/testar-proprio-codigo]] · [[wiki/concepts/red-flags-de-design]] (Vague Name, Hard to Pick Name)

## Key Sources

- [[wiki/sources/two-hard-things-martin-fowler]] — origem (incerta) e curadoria da citação de Phil Karlton sobre naming como um dos dois problemas difíceis
- [[sources/5-principios-programador]]
- [[wiki/sources/5-principles-that-changed-me-as-a-programmer]]
- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — bug do `block` no Sprite; discordância com o guia de estilo de nomes do Go
- [[wiki/sources/9-code-smells-como-identificar-codigo-ruim]] — números mágicos e valores hard-coded (URLs, chaves de API) como falta de naming; busca textual ambígua vs. busca por nome de constante
