---
type: source
title: "Acessibilidade (FrontPUSH, interfaces web): WCAG, contraste A/AA/AAA, textos invisíveis, KISS e patterns"
aliases: ["aula de acessibilidade", "acessibilidade FrontPUSH", "03 - Acessibilidade", "textos invisíveis", "WCAG na aula de Násser"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ux, ui, ui-design, acessibilidade, a11y, wcag, contraste, alt-text, text-to-speech, kiss, padroes-de-interface, carga-cognitiva, guidelines]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/acessibilidade-wcag-contraste-textos-invisiveis-kiss-patterns.md"
source_url: ""
author: "Násser (inferido)"
date_published: ""
date_ingested: 2026-11-15
---

# Acessibilidade (FrontPUSH, interfaces web): WCAG, contraste A/AA/AAA, textos invisíveis, KISS e patterns

## TL;DR

Terceira aula (cerca de 9 min) do módulo de interfaces web do [[wiki/entities/frontpush]], na parte de pesquisa e prototipagem inicial, com o logo "W7" no slide. A tese é que **nós não somos o usuário**: em algum momento alguém com "imparidade" auditiva, motora ou cognitiva vai usar a interface, então ela tem que ser [[wiki/concepts/acessibilidade|acessível]]. O [[wiki/concepts/wcag]] tem regras demais para um site cumprir todas, e a aula fica com as principais. São quatro. **Contraste de cor** distingue elementos, guia a jornada e tem três notas (A mínima, AA média, AAA alta): mire no mínimo em AA e reserve AAA para interfaces de governo, como a do auxílio emergencial. Ferramentas: Contrast Ratio e [[wiki/entities/who-can-use]]. **Textos invisíveis**, descrições em imagens, alimentam o text-to-speech ([[wiki/concepts/texto-alternativo]]). **[[wiki/concepts/kiss]]**: simples, passo a passo, com [[wiki/concepts/feedback-do-sistema|feedback]], ícones e cor bem usada. **UX/UI patterns** consagrados reduzem a [[wiki/concepts/carga-cognitiva]] ([[wiki/concepts/padroes-de-interface]]), e para UI valem os UI Kits e as guidelines de [[wiki/entities/google]], [[wiki/entities/microsoft]] e [[wiki/entities/apple]]. "Não é uma regra, mas é uma boa recomendação."

## Key Claims

### O que é e para quem

- **Continuação da aula de usabilidade:** o conceito "se agrega e muito com o quesito usabilidade". A aula 02 (Usabilidade) ainda não foi ingerida.
- **Nós não somos o usuário:** "A gente tem que sempre pensar que nós não somos quem vai utilizar aquele produto." Ver [[wiki/concepts/acessibilidade]].
- **Para quem:** pessoa "com algum tipo de imparidade, com algum tipo de deficiência, seja ela auditiva, motora ou cognitiva". O slide repete: "Imparidade auditiva, motoras, cognitivas...". "Imparidade" parece decalque do inglês *impairment*; mantido como dito.

### WCAG

- **Slide:** "WCAG: Diretrizes de acessibilidade ao conteúdo da web". Ver [[wiki/concepts/wcag]].
- **Recursos:** um site no "Master File" do curso, com links, plugins e "inúmeras guidelines que eu vou deixar em anexo".
- **Impossível cumprir tudo:** "por ser muito texto e muitas leis, é difícil um website compreender a totalidade de regras", e a aula fica com "as principais recomendações". `[external]` As WCAG são recomendações do [[wiki/entities/w3c]], não leis. Viram obrigação legal quando uma lei as adota, como a LBI no Brasil (Lei 13.146/2015, art. 63), que obriga sites de empresas e do governo a serem acessíveis (https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2015/lei/l13146.htm).

### Contraste de cor

- **Função:** "é saber distinguir elementos dos outros, garantir melhor visibilidade e legibilidade". Interfaces que talvez sejam "90% [...] tipografia, [...] informação" dependem disso. Ver [[wiki/concepts/contraste]] e [[wiki/concepts/tipografia]].
- **Guia a jornada:** "o contraste de cor bem aplicado, ele até guia, ele facilita o usuário pela sua jornada".
- **Hierarquia de texto na própria interface:** um texto branco, outro em escala de cinza; ele não faz "uma palette de cor pobre". Ver [[wiki/concepts/hierarquia-visual]].
- **Ferramentas:** "Contrast Ratio" e "esse Who Can Use", já citados na seção de tipografia. A ideia é ter "uma lista de doenças, talvez visuais", para saber se a interface atende "todo e qualquer pessoa". Ver [[wiki/entities/who-can-use]].
- **Três notas:** "uma letra A, acessibilidade mínima; duas letras A, acessibilidade média; três letras A, acessibilidade alta".
- **AAA nem sempre:** "não necessariamente eu preciso sempre projetar uma interface para ser AAA". Interfaces de governo, como a do auxílio emergencial, devem buscar AAA porque atendem "um volume de pessoas muito grande". "Eu sempre miro nesses dois aqui no mínimo", isto é, AA.

### Texto: os "textos invisíveis"

- **"Coloque textos e descrições em imagens: 'textos invisíveis'"** (slide). Isso "ajuda quem tem deficiência visual a utilizar os recursos text-to-speech", que celulares e smartphones já trazem. Ver [[wiki/concepts/texto-alternativo]].
- **KISS:** "projete a interface como se fosse de maneira simples e estúpida, mais fácil possível, bem passo a passo, dando feedback para o usuário, dando confirmação visual, utilizando ícones, fazendo uso adequado das cores". Diz que já falou disso "lá na outra aula". Ver [[wiki/concepts/kiss]] e [[wiki/concepts/feedback-do-sistema]].

### Use UX/UI patterns

- **Slide:** "Bom uso de heurísticas, patterns, padrões...".
- **UX:** "soluções experimentadas e testadas para resolução de problemas" por quem "já comprovou em uma alta gama de usuários". Não reinventar a roda "reduz a carga cognitiva do usuário": algo totalmente novo obriga o usuário a "gastar tempo para poder aprender". Ver [[wiki/concepts/padroes-de-interface]], [[wiki/concepts/carga-cognitiva]] e [[wiki/concepts/lei-de-jakob]].
- **UI:** "bibliotecas de componentes que fornecem soluções comprovadas, ou seja, UI Kits e Guidelines", com links no Notion. As guidelines de [[wiki/entities/google]], [[wiki/entities/microsoft]] e [[wiki/entities/apple]] vêm de "empresas bilionárias que tem um time de UX, que tem um time de UI" e que já testaram muito.
- **Com medida:** "não estou dizendo que é uma regra, mas é uma boa recomendação"; "não estou freando a sua criatividade". O cérebro "trabalha muito com padrões".

## Entities

- [[wiki/entities/nasser]] — instrutor (inferido)
- [[wiki/entities/frontpush]] — curso; módulo de interfaces web
- [[wiki/entities/who-can-use]] — checker de contraste indicado
- [[wiki/entities/w3c]] — `[external]` publica as WCAG
- [[wiki/entities/google]], [[wiki/entities/microsoft]], [[wiki/entities/apple]] — guidelines como referência de UI
- Contrast Ratio — checker indicado; sem página própria. `[external]` Provavelmente o contrast-ratio.com de Lea Verou (confiança média).

## Concepts

- [[wiki/concepts/acessibilidade]] (novo)
- [[wiki/concepts/wcag]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/texto-alternativo]]
- [[wiki/concepts/kiss]]
- [[wiki/concepts/padroes-de-interface]]
- [[wiki/concepts/carga-cognitiva]]
- [[wiki/concepts/lei-de-jakob]]
- [[wiki/concepts/feedback-do-sistema]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/tipografia]]

## Open Questions

- **Nota "A" em contraste não existe.** `[external]` No WCAG 2.x, A, AA e AAA são níveis de conformidade da norma inteira. Para contraste só há critérios AA (1.4.3: 4.5:1 em texto normal, 3:1 em texto grande) e AAA (1.4.6: 7:1 e 4.5:1). O nível A tem o 1.4.1, que proíbe usar só a cor para passar informação (https://www.w3.org/TR/WCAG22/#contrast-minimum, https://www.w3.org/TR/WCAG22/#contrast-enhanced). O "A" que o [[wiki/entities/who-can-use]] mostra é uma nota da ferramenta, não do critério.
- **"Textos invisíveis" é mais que alt text.** `[skill: ux-ui-mentor]` Imagem decorativa leva `alt=""`, e ícone funcional leva `aria-label`. `[external]` O leitor de tela (VoiceOver, TalkBack) lê o alt, o que vai além de um simples recurso de text-to-speech.
- **A aula só cobre a visão.** As quatro recomendações tratam de visão e cognição. Teclado, foco visível e legendas para quem tem deficiência auditiva ficaram de fora, embora a abertura cite as deficiências auditiva e motora.
- **Auxílio emergencial:** "o próprio exemplo que eu disse" vem de uma aula anterior, talvez a 02 (Usabilidade), ainda fora da wiki.
- **"Master File":** provavelmente o arquivo-mestre de links do curso (Notion); não confirmado.

## Raw quotes

- "A gente tem que sempre pensar que nós não somos quem vai utilizar aquele produto."
- "O contraste de cor bem aplicado, ele até guia, ele facilita o usuário pela sua jornada."
- "Não necessariamente você mira sempre na AAA, sempre varia, mas eu sempre miro nesses dois aqui no mínimo."
- "Se você projetar algo totalmente novo, o usuário vai ter que gastar tempo para poder aprender como é que utiliza a sua interface."
- "Não estou dizendo que é uma regra, mas é uma boa recomendação."

## Ver também

- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — Who Can Use na prática; notas "A, 2A, 3A"
- [[wiki/sources/imagens-e-ilustracoes-ilustracoes-mascotes-consistencia-svg]] — "sempre coloque um texto alternativo"
- [[wiki/sources/patterns-o-que-faz-uma-boa-ui-padroes]] — contraste para idosos; não fugir dos padrões
- [[wiki/sources/principios-do-design-eixo-simetria-consistencia-simplicidade]] — "uso de patterns" e feedback listados sob acessibilidade
