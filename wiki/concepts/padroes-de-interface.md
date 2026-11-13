---
type: concept
title: "Padrões de Interface (UI Patterns)"
aliases: ["ui patterns", "padrões de ui", "design patterns de interface", "interaction patterns", "padrões de interação"]
date_created: 2026-11-13
date_updated: 2026-11-13
source_count: 7
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

## Key Sources

- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — o cérebro trabalha com padrões; busca, hambúrguer, lupinha
- [[wiki/sources/ui-patterns-com-biblioteca-de-padroes]] — catálogo, definição e linguagem comum
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — eixos como padrões; "uso de patterns" como parte da acessibilidade
- [[wiki/sources/elementos-da-interface-introducao-ui-design]] — menu embaixo fere o padrão em website; patterns como melhor prática
- [[wiki/sources/icones-parte-1-conceito-comunicacao-identidade-visual-familias]] — ícones como patterns aprendidos; o "compartilhar" que a avó não reconhece
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — Facebook em japonês como prova de pattern
- [[wiki/sources/icones-comunicacao-senso-comum-dicas-consistencia]] — senso comum de ícones; engrenagem mais forte que chave de boca; Viena
