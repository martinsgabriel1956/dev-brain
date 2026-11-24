---
type: concept
title: "Cor semântica"
aliases: ["cores semânticas", "cor de feedback", "cor de estado", "semantic color", "status colors"]
date_created: 2026-11-13
date_updated: 2026-11-24
source_count: 11
tags: [ui, ui-design, cor, cor-semantica, feedback, acessibilidade, design-tokens]
skill: ux-ui-mentor
status: stub
---

# Cor semântica

Cor usada para dizer algo, não para enfeitar: o usuário lê o estado ou o tipo da informação pela cor antes de ler o texto. Na aula de Násser, "cores funcionam para poder dar informação" ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## As convenções da aula

| Cor | Leitura | Exemplo da aula |
|---|---|---|
| Azul | link, informação | link azul se reconhece "de cara" |
| Vermelho | alerta, erro | "alertas geralmente são colocados na cor vermelha" |
| Amarelo | warning | "para poder sinalizar alguma coisa para o usuário" |
| Cor de destaque / preenchimento | hierarquia maior | botão preenchido acima do não preenchido |

É um [[wiki/concepts/padroes-de-interface|pattern]]: funciona porque o usuário já aprendeu. Ver também [[wiki/concepts/hierarquia-visual]] e [[wiki/concepts/feedback-do-sistema]].

`[skill: ux-ui-mentor]` A skill dá o mapa completo de feedback: verde sucesso, vermelho erro, âmbar warning, azul info. No código, isso vira tokens semânticos (`--color-error`, `--color-warning`), não cores cruas. No dark mode, os tokens mudam de valor, não de nome.

## Nunca só a cor

`[skill: ux-ui-mentor]` Regra crítica: estado não se comunica só pela cor. Daltonismo afeta cerca de 8% dos homens; acompanhe com ícone, texto ou padrão.

`[external]` WCAG 2.2, critério 1.4.1 (Use of Color): https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html. Link diferenciado só pela cor precisa de contraste de 3:1 com o texto ao redor e de outro sinal no foco ou hover; o sublinhado resolve.

## Cor como código entre cursos

Em [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]]: nos ícones do site do autor, "tudo que é laranja está remetendo ao curso de UI Design", "uma seleção que o seu cérebro faz até pela cor". É convenção de marca, não de estado; vale a mesma regra de nunca depender só da cor.

## Nomes de cor no style guide

Os grupos de cor mostram nomes por papel e por valor: primary, secondary, brand color, auxiliary color; white, black, neutral e gray colors para hierarquia textual. `Primary / Orange-1` mistura os dois; `[skill: ux-ui-mentor]` separar primitivo (`orange-500`) de semântico (`brand-primary`) deixa trocar a cor sem renomear ([[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]]).

## Cor como boa prática de usabilidade

"Uso adequado das cores, que é toda a teoria das cores que a gente conversou lá" aparece na lista de boas práticas de [[wiki/concepts/usabilidade]], ao lado de ícones e confirmações ([[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]]).

## Cor como informação no mapa e no card

A abertura do módulo de cores amplia a tabela ([[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]]): via vermelha ou laranja no Google Maps ou no Waze = bloqueio ou engarrafamento; card verde = sucesso, concluído; vermelho = erro; amarelo = alerta ou lembrete. A cor também **categoriza**: na Globo, verde = esporte, laranja = entretenimento, vermelho = notícias, "meio que virou padrão" (`[external]` g1 vermelho, ge verde, gshow laranja no globo.com). As associações por idade e cultura ficam em [[wiki/concepts/psicologia-das-cores]].

## Semântica × harmonia

A aula de [[wiki/concepts/harmonia-de-cores]] escolhe cores pela posição no círculo; a cor semântica, pela convenção aprendida. Numa paleta complementar azul + laranja, o laranja de destaque fica perto do amarelo/âmbar de warning: o acento da marca pode ser lido como alerta (inferência, não dita na aula) ([[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]]).

## Cor de marca x cor de estado

A aula de paleta ([[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]]) trata a cor de base como branding (Facebook azul, WhatsApp verde) e a de enfoque como destaque (o verde da [[wiki/entities/rocketseat]]). Quando a cor de enfoque coincide com uma convenção semântica (verde = sucesso), as leituras se misturam; tokens separados (`--color-accent` x `--color-feedback-success`) evitam o conflito no código. Ver [[wiki/concepts/paleta-de-cores]].

## Amarelo como cor de marca

Em [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]], o amarelo é a cor de destaque da paleta, não warning. `[skill: ux-ui-mentor]` Se o produto também usa amarelo para warning, os dois viram tokens diferentes e o warning vem sempre com ícone e texto. Ver [[wiki/concepts/paleta-de-cores]].

## Do token ao hex

Em [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]]: a cor vira código em hexadecimal ou RGB, e o HSB fica para compor a paleta. A cor semântica é a camada de cima: `--color-error` aponta para um valor cru (`#…`) que pode mudar sem que o nome mude. Ver [[wiki/concepts/modelos-de-cor]].

## Em tipografia: cores auxiliares

Em [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]], Násser retoma as convenções com o [[wiki/entities/twitter-bootstrap|Bootstrap]] aberto e completa o mapa com o **verde**: "sucesso, deu certo, cadastrado, entregue". Azul é "simplesmente informativo, então é algum link"; vermelho, erro; amarelo, alerta. Recomenda definir "cores auxiliares" para a passagem de informação.

## Modais de dashboard

Na [[wiki/sources/frontpush-dashboards-grids-e-patterns|aula 03 do módulo de dashboards]], as cores dos modais do DashClass: sucesso verde, informação azul, aviso amarelo, erro vermelho, neutro branco. [[wiki/entities/nasser|Násser]] chama isso de "psicologia das cores", mas é cor semântica: convenção de estado. Os modais e os status da tabela de vendas juntam ícone, cor e texto, sem depender só da cor.

## Key Sources

- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — azul link, vermelho alerta, amarelo warning; botão preenchido como hierarquia
- [[wiki/sources/icones-pratica-figma-plugins-icones-proprios-cards-constraints]] — laranja = curso de UI Design nos ícones do site
- [[wiki/sources/style-guide-pratica-figma-estilos-de-cor-texto-e-efeito]] — grupos de cor por papel (primary, brand, neutral) e por valor (orange-1)
- [[wiki/sources/usabilidade-facilmente-tres-esferas-boas-praticas-auxilio-emergencial]] — cor adequada na lista de boas práticas de usabilidade
- [[wiki/sources/teoria-das-cores-introducao-natureza-objetivos-fenomeno-fisico]] — trânsito no mapa, card verde/vermelho/amarelo, categorias da Globo
- [[wiki/sources/harmonia-das-cores-monocromatica-complementar-analoga-triadica]] — harmonia de cores x convenção semântica
- [[wiki/sources/paleta-de-cores-base-enfoque-monocromatica-analoga-triadica]] — cor de base (marca) e de enfoque (destaque), distintas da cor de estado
- [[wiki/sources/aplicando-paleta-de-cores-base-destaque-hierarquia-gradiente-icones]] — amarelo como destaque de marca, não warning
- [[wiki/sources/representacao-da-cor-em-codigos-hsb-hexadecimal-rgb]] — de onde vêm os valores crus (HSB, hex, RGB) que os tokens semânticos nomeiam
- [[wiki/sources/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao]] — verde = sucesso; cores auxiliares; Bootstrap como referência
- [[wiki/sources/frontpush-dashboards-grids-e-patterns]]: FrontPUSH, dashboards aula 03: verde/azul/amarelo/vermelho/branco nos modais
