---
type: concept
title: "Padrões de Interface (UI Patterns)"
aliases: ["ui patterns", "padrões de ui", "design patterns de interface", "interaction patterns", "padrões de interação"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 8
tags: [ui, ux, design, padroes-de-interface, usabilidade]
skill: ux-ui-mentor
status: draft
---

# Padrões de Interface (UI Patterns)

Soluções recorrentes para problemas comuns de design de interface, como busca no topo, breadcrumbs, wizard ou carrinho de compras ([[wiki/sources/ui-patterns-com-biblioteca-de-padroes]]). Funcionam porque "o cérebro humano trabalha com padrões" e o usuário chega com expectativas formadas em outras interfaces ([[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]]).

## Jogar a favor do padrão

A aula dá três exemplos:

- **Busca no topo.** Sem achar o produto nos destaques, o usuário procura a busca no menu, e o menu fica na parte superior.
- **Três tracinhos.** Um ícone com três linhas é lido como menu hambúrguer.
- **Lupinha sozinha.** Em e-commerce lotado de informação, um ícone de lupa no canto passa despercebido; uma barra de busca grande respeita o padrão e antecipa o erro do usuário leigo.

Conclusão: "não é tão interessante você fugir desses padrões". É a [[wiki/concepts/lei-de-jakob]]. A aula ressalva que o padrão se confirma com pesquisa: teste de usabilidade e heatmap.

`[skill: ux-ui-mentor]` Ordem de escolha de padrão: (1) o nativo da plataforma; (2) o mais comum no domínio; (3) o mais acessível; (4) solução customizada só se os três falharem. Todo padrão carrega expectativas, e quebrá-las sem motivo gera fricção.

## Linguagem comum

O [[wiki/entities/ui-patterns-com]] destaca outro papel: nomear um padrão dá uma linguagem comum entre designers e permite debater alternativas. É a mesma origem de [[wiki/concepts/design-patterns]] em software, ambos herdeiros da *A Pattern Language* de [[wiki/entities/christopher-alexander]]. O catálogo separa padrões de UI (entrada de dados, onboarding, navegação, dados, social) dos [[wiki/concepts/design-persuasivo|padrões persuasivos]].

## Padrão não é regra

[[wiki/concepts/pattern-recognition]] distingue *pattern* (repetição observada) de *standard* (regra). Um padrão de UI pode ficar obsoleto ou ser mal reconhecido. `[external]` A NN/g mostra que o ícone de hambúrguer não é reconhecido por todos e que navegação escondida é menos usada que a visível ([NN/g, 2016](https://www.nngroup.com/articles/find-navigation-mobile-even-hamburger/)). Por isso a aula pede validação.

## Relação com outros conceitos

- [[wiki/concepts/affordance]] — muitos padrões são affordances aprendidas por convenção.
- [[wiki/concepts/usuarios-como-agentes-do-caos]] — seguir o padrão reduz o espaço para erro.
- [[wiki/concepts/ui-design]] — padrões são uma das três frentes de uma boa UI, ao lado de apresentar bem a informação e as cores.

## Padrões nos princípios do design

Os slides de [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] põem "uso de patterns" sob acessibilidade ("o design não é pra você designer, é para o usuário"), ao lado de feedback. A mesma aula trata os usos do [[wiki/concepts/eixo-visual|eixo]] como padrões: card cortado para indicar mais conteúdo, eixo deslocado para indicar resposta, grid assimétrico para feed infinito.

## Patterns como melhor prática

[[wiki/sources/elementos-da-interface-introducao-ui-design]] põe patterns entre as seis melhores práticas de UI e dá um exemplo de quebra: num website, menu na parte de baixo "fere um pattern", porque o usuário aprendeu que o menu fica à esquerda ou no topo. A aula fala de website; em mobile a tab bar inferior é o padrão nativo, e a regra acima (nativo da plataforma primeiro) prevalece. Ver [[wiki/concepts/contexto-do-usuario]].

## Ícones como patterns

Engrenagem = configurar, sininho = notificações, "+" = adicionar, três tracinhos = menu, três pontinhos = mais opções, nove pontinhos = apps do Google: o significado vem do uso diário ("o ser humano é movido por padrões"). Ícones menos difundidos falham: a avó de Násser não reconhecia o "compartilhar" de três bolinhas ([[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]]). `[external]` A NN/g diz que ícones universais são raros e pede rótulo de texto (https://www.nngroup.com/articles/icon-usability/). Ver [[wiki/concepts/icones-em-interfaces]].

## Ícones que sobrevivem à troca de idioma

Prova prática do pattern: com o Facebook em japonês, os ícones continuam guiando, porque o sentido foi aprendido pelo uso, não pela leitura ([[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]]).

## Senso comum de ícones

Na edição "W7" da aula de ícones ([[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]]): "entender o senso comum de ícones e não mudar drasticamente", para atingir mais usuários, "justamente por ter criado um padrão na cabeça do ser humano". Engrenagem bate chave de boca para configuração; carta, balão, escudo, carrinho e sacola são universais; o smartphone, "não sei se é tão universal assim". Em Viena, sem opção de inglês, o autor se guiou pelos ícones.

## Patterns, UI Kits e guidelines como acessibilidade

Em [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]]: "use e abuse de patterns UI e patterns UX que já estejam bem estabelecidos no mercado". São "soluções experimentadas e testadas" que reduzem a [[wiki/concepts/carga-cognitiva]]. Para UI, há "bibliotecas de componentes que fornecem soluções comprovadas, ou seja, UI Kits e Guidelines", como as de [[wiki/entities/google]], [[wiki/entities/microsoft]] e [[wiki/entities/apple]], feitas por times de UX e UI que já testaram tudo. "Não estou dizendo que é uma regra, mas é uma boa recomendação"; "não estou freando a sua criatividade". Ver [[wiki/concepts/acessibilidade]].

## Biblioteca de wireframes na cabeça

Em [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]], o sketchbook do curso serve para "desenvolver [...] uma biblioteca de wireframes, de seções na sua cabeça", que melhora com o treino. É um repertório de padrões de seção, no mesmo espírito dos patterns.

## Patterns por tipo de página

Em [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]]: "acredite, tem padrões, existem padrões" para cada tipo de página. Página de cadastro pede nome e e-mail; página de venda repete o CTA "em várias partes da página" (o [[wiki/entities/frontpush]] mostra "quero me inscrever" três vezes); pricing tem planos em escada (standard ou prata, depois gold). Os patterns se acham por "observação e pesquisa" em sites como o [[wiki/entities/ui-movement]] e viram o [[wiki/concepts/page-map]].

## Seções como padrões

A [[wiki/concepts/biblioteca-de-wireframes]] é um repertório de "padrões de serviço de produto": hero, depoimentos, cadastro. A página se monta juntando-os, e "não existe esse negócio de bloqueio criativo" ([[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]]).

## Sites do mesmo tipo, mesmo esqueleto

Em [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]], os portfólios de [[wiki/entities/jonas-miller]] e [[wiki/entities/fabio-freire]] "estão na mesma linha, têm mais ou menos o mesmo page map". Násser parte desse esqueleto comum e só acrescenta o que o caso dele pede. Ver [[wiki/concepts/page-map]].

## Padrão como apoio ao aprendizado e à memória

Em [[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]], padrões sustentam dois dos [[wiki/concepts/atributos-de-bom-design|atributos de um bom design]]: fácil aprendizado ("conversei isso com vocês sobre os patterns") e memorável ("já tem um padrão que você meio que entende"). O contraexemplo é o Photoshop, que mudou atalhos de teclado já aprendidos e obrigou o usuário a reaprender: o padrão também pode ser interno ao produto.

## Key Sources

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — o cérebro trabalha com padrões; busca, hambúrguer, lupinha
- [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] — catálogo, definição e linguagem comum
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — eixos como padrões; "uso de patterns" como parte da acessibilidade
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — menu embaixo fere o padrão em website; patterns como melhor prática
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — ícones como patterns aprendidos; o "compartilhar" que a avó não reconhece
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — Facebook em japonês como prova de pattern
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — senso comum de ícones; engrenagem mais forte que chave de boca; Viena
- [[wiki/sources/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns]] — patterns, UI Kits e guidelines das big techs como recomendação de acessibilidade
- [[wiki/sources/wireframes-parte-1-o-que-e-uso-foco-page-map-papel-e-caneta]] — biblioteca de wireframes e seções no sketchbook
- [[wiki/sources/wireframes-parte-2-briefing-objetivo-page-map-leitura-f-z]] — patterns por tipo de página (cadastro, venda, pricing) como base do page map
- [[wiki/sources/wireframes-pratica-1-hero-page-map-frankenstein-referencias]] — seções prontas (hero, depoimentos, cadastro) como padrões a combinar
- [[wiki/sources/wireframes-pratica-2-page-map-por-referencias-hero-processo-cta]] — portfólios de freelancer convergem no mesmo page map
- [[wiki/sources/o-que-e-um-bom-design-atributos-util-aprendizado-memoravel-eficaz-desejavel-prazeroso]] — patterns como base de fácil aprendizado e memorabilidade; atalhos do Photoshop
