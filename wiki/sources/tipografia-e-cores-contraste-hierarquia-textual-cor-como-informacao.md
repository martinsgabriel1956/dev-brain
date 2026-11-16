---
type: source
title: "Tipografia e cores: contraste, hierarquia textual e cor como informação"
aliases: ["tipografia e cores", "aula 06 tipografia FrontPUSH", "cores em tipografia", "como aumentar o contraste", "cores de suporte"]
date_created: 2026-11-15
date_updated: 2026-11-15
source_count: 0
tags: [ui, ui-design, tipografia, cor, contraste, acessibilidade, wcag, hierarquia-visual, cor-semantica, botoes, style-guide]
skill: ux-ui-mentor
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/tipografia-e-cores-contraste-hierarquia-textual-cor-como-informacao.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-15
---

# Tipografia e cores: contraste, hierarquia textual e cor como informação

## TL;DR

Aula 06 do módulo de [[wiki/concepts/tipografia]] do [[wiki/entities/frontpush]] (cerca de 16 min), de [[wiki/entities/nasser|Násser]]. Retoma o módulo de cores aplicado a texto em três pontos: **[[wiki/concepts/contraste]]** (tipografia existe para ser lida, então acessibilidade vem primeiro), **hierarquia textual** (escala, peso, caixa alta e escala de cinza; o título dos cards do FrontPUSH e os títulos azuis do [[wiki/entities/google]]) e **cor como informação** (azul informa, vermelho é erro, amarelo é alerta, verde é sucesso; [[wiki/entities/twitter-bootstrap|Bootstrap]] como referência). Quando a paleta não dá contraste, a escada é: observar a [[wiki/concepts/luminosidade-das-cores|luminosidade]] (amarelo, ciano e verde são claros), aumentar peso, aumentar escala, inverter as cores neutras e, em imagem, escurecer o fundo. Na prática, o verde do FrontPUSH dá 1.65 contra o branco e reprova num checker de [[wiki/concepts/razao-de-contraste]]; no [[wiki/entities/who-can-use]], o laranja também falha com branco e passa em tudo com preto. Por isso os botões verde e laranja do style guide levam texto preto, "apesar de eu achar que ele era mais bonito" com branco.

## Slide da aula

O slide (enviado pelo usuário na hora do ingest, não salvo em `raw/`) tem quatro blocos sob o título "Tipografia":

- **Tipografia e cores → Acessibilidade:** Contraste → "Garantir uma boa leitura, acessibilidade"; Hierarquia textual → "Facilidade, localização, importância"; Informação → "Cor verde? Cor vermelha? Cor amarela?"
- **Cores de suporte, boas práticas:** escala de cinza para criar hierarquia em corpos de texto; cores auxiliares para informação; seguir a paleta de cores e a regra 60, 30, 10.
- **Como aumentar o contraste?** Observar a luminosidade da paleta; aumentar o peso tipográfico; aumentar a escala; inverter as cores neutras; em imagens, escurecer o fundo.
- **Conceitos muito utilizados em style guides.**

O logo no topo é o "W7" das aulas da edição "W7", embora a transcrição esteja na pasta FrontPush (ver Open Questions).

## Key Claims

### Contraste: o objetivo da tipografia

- **Acessibilidade primeiro:** a tipografia "precisa ter como objetivo acessibilidade, em outras palavras tem que ter contraste"; "não faz muito sentido a gente escrever algo onde a pessoa tenha dificuldade para ler". Ver [[wiki/concepts/contraste]].
- **Para qualquer usuário:** "com problema de visão ou sem problema de visão, com deficiência física ou não". Promete um site que testa o contraste contra "uma boa área de problemas visuais" (o [[wiki/entities/who-can-use]]).
- **Exceção consciente:** a palavra "criatividade" escondida de propósito num slide anterior, "para poder causar essa experiência"; fora disso, "sempre garanta um bom contraste".

### Hierarquia textual

- **Quatro alavancas:** escala ("aquilo que é maior você enxerga primeiro"), peso (bold tem hierarquia maior que o fino), caixa alta e cor, em especial a **escala de cinza**. Ver [[wiki/concepts/hierarquia-visual]].
- **O que a hierarquia faz:** "facilitam, nos localizam [...] e declaram importância" (o slide: "Facilidade, localização, importância"). A cor é "super complementar"; "não deixe de utilizar a cor também como hierarquia textual".
- **Exemplo FrontPUSH:** o título "o que compõe o FrontPUSH" é maior, mais pesado e de contraste maior; o usuário lê o título e decide se lê o resto ("eu consigo passar e literalmente só enxergar o que eu quero ver"). Ver [[wiki/entities/frontpush]].
- **Exemplo Google:** os títulos dos resultados "estão sempre em azul", com contraste e tamanho maiores; o usuário lê primeiro o título e só depois clica ou lê a descrição. Ver [[wiki/entities/google]].
- **Style guide adiante:** a escala de cinza para hierarquia em texto volta na parte de style guide.

### Cor como informação

- **Mesmo raciocínio do módulo de cores**, com o [[wiki/entities/twitter-bootstrap|Bootstrap]] aberto: azul é "simplesmente informativo, então é algum link"; vermelho, "um erro"; amarelo, alerta; verde, "sucesso, deu certo, cadastrado, entregue". Ver [[wiki/concepts/cor-semantica]].
- **Definir cores auxiliares** na interface "para poder ajudar nessa passagem de informação".

### Cores de suporte: boas práticas

- Escala de cinza para hierarquia; cores auxiliares para informação; seguir a paleta e a [[wiki/concepts/regra-60-30-10]], "que a gente também viu no módulo de cores".

### Como aumentar o contraste sem trocar a paleta

- **A pergunta do aluno:** "E Násser, beleza [...] eu quero aumentar o máximo possível, mas sem mudar as cores, o que eu posso fazer?" Vale para "um botão, [...] um texto, [...] um título".
- **1. Observar a luminosidade:** o amarelo é "a mais clara do espectro visível", o azul "o mais escuro"; ciano muito claro, "em terceiro vem o verde". Com esses, contraste com branco "é um pouco mais complicado". Daí "muitas interfaces puxadas para o azul". Ver [[wiki/concepts/luminosidade-das-cores]].
- **2–5. Peso, escala, inversão, fundo:** "aumenta o peso tipográfico se for necessário, aumenta a escala, inverte as cores se não tiver jeito"; "em imagens sempre escureça o fundo para garantir o contraste". Ver [[wiki/concepts/texto-sobre-imagem]].
- **Último recurso:** mudar a saturação ou o brilho; "você tem que sacrificar a sua paleta de cores nesse sentido para poder garantir a acessibilidade, principalmente nos botões, que são os call to actions".

### Na prática: os botões do FrontPUSH

- **Botão secundário:** branco sobre fundo preto. No hover azul, manteve o texto branco porque o azul ainda contrasta; admite que deveria ficar preto "para poder ficar consistente, isso aqui é até um erro". Ver [[wiki/concepts/botoes-em-interfaces]].
- **Botão verde invertido:** o verde é mais claro, "com o branco já não teria um contraste legal, então eu tive que inverter".
- **Checker de contraste:** branco + "5F36A" dá **1.65**, nota vermelha. Três notas: vermelha (reprovado), laranja (dá com peso e tamanho maiores: "em botões você pode utilizar, só que em corpo de texto é um pouco mais complicado") e, implícita, a de aprovação. Preto é "o contraste máximo". A WCAG "elaborou uma nota de 0 a 21". Ver [[wiki/concepts/razao-de-contraste]].
- **Who Can Use:** o verde "deu feio, está falho"; lista Trichromatic ("quase foi satisfeito, 68%"), dificuldade com vermelhos (1.3, falha), Red blind, dificuldade com verdes. O laranja do FrontPUSH também falha com branco; com preto "passou em todas". Mostra simulações de glaucoma e catarata. Ver [[wiki/entities/who-can-use]].
- **Brilho:** reduzir o brilho da cor "vai aumentar o contrast ratio".
- **Style guide:** arquivos para download com os padrões do curso; os botões laranja ficaram com texto preto por causa desse teste.

## Entities

- [[wiki/entities/nasser]]: autor (pasta FrontPush; "E Násser, beleza"; "a minha interface" e "o que compõe o FrontPUSH"; "eu tive que deixar preto").
- [[wiki/entities/frontpush]]: site usado como exemplo (títulos dos cards, botões secundário, verde e laranja) e style guide.
- [[wiki/entities/google]]: títulos azuis nos resultados como hierarquia por cor, tamanho e contraste.
- [[wiki/entities/twitter-bootstrap]]: referência de cores de alerta.
- [[wiki/entities/who-can-use]]: teste do verde e do laranja contra condições de visão.
- Sem página própria: o checker de contraste anterior ao Who Can Use (não nomeado), WCAG (tratada em [[wiki/concepts/razao-de-contraste]]).

## Concepts

- [[wiki/concepts/razao-de-contraste]] (novo)
- [[wiki/concepts/luminosidade-das-cores]] (novo)
- [[wiki/concepts/regra-60-30-10]] (novo)
- [[wiki/concepts/contraste]]
- [[wiki/concepts/tipografia]]
- [[wiki/concepts/hierarquia-visual]]
- [[wiki/concepts/cor-semantica]]
- [[wiki/concepts/botoes-em-interfaces]]
- [[wiki/concepts/texto-sobre-imagem]]

## Tensões com a wiki

- **"Nota de 0 a 21" está errado.** `[external]` A razão WCAG vai de 1:1 a 21:1; não existe 0 (https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html). Ver [[wiki/concepts/razao-de-contraste]].
- **A faixa laranja não cobre qualquer botão.** "Em botões você pode utilizar" só vale se o label for texto grande (18 pt, ou 14 pt em negrito) `[external]`; um label comum de 16 px regular precisa de 4.5:1. Leitura do agente.
- **"Nunca só a cor".** `[skill: ux-ui-mentor]` O checklist de cor pede feedback de estado com cor + ícone + texto. A aula apresenta a cor como portadora da informação; o próprio Who Can Use da aula mostra por que ela não basta sozinha (Red blind, dificuldade com verdes).
- **Hierarquia por cinza e contraste mínimo.** `[skill: ux-ui-mentor]` A skill lista "cor / opacidade" como hierarquia secundária; o cinza mais claro do corpo ainda precisa de 4.5:1. A aula não fala desse limite.
- **Hover azul com texto branco.** O autor chama de "erro" de consistência; com o verde e o laranja invertidos para preto, o par de estados do botão secundário fica com duas regras diferentes.
- **Skill drift.** `references/cor.md` da skill define texto grande como "18px+ ou 14px bold"; a WCAG usa pt (~24 px e ~18,7 px). Registrado em [[wiki/concepts/razao-de-contraste]]; skills são só leitura.

## Open Questions

- **Hex do verde:** "5F36A" tem cinco dígitos. `#5FE36A` dá 1,66:1 no branco e 12,68:1 no preto (cálculo do agente), o que bate com o 1.65 falado. Inferência, confiança média.
- **"68%" no Who Can Use:** provavelmente a fatia da população com aquela visão, não "quase satisfeito". Confiança baixa.
- **Checker não nomeado** antes do Who Can Use.
- **Edição:** a transcrição está na pasta FrontPush, mas o slide tem o logo "W7". Pode ser o mesmo material reaproveitado entre as edições.
- **Lacuna de fala** em 00:03:10–00:03:21: "elas têm maior hierarquia textual" aparece sem referente (provavelmente as cores de maior contraste da escala de cinza).
- **Hex do laranja** não é dito.
- **Módulo de cores** do curso (luminosidade, 60-30-10, cor como informação) é citado e não está na wiki.
- `date_published` vazio.

## Raw Quotes

> "Não faz muito sentido a gente escrever algo onde a pessoa tenha dificuldade para ler."

> "Você tem que sacrificar a sua paleta de cores nesse sentido para poder garantir a acessibilidade, principalmente nos botões."

> "Esse laranja não tem um bom contraste com o branco, apesar de eu achar que ele era mais bonito."

## Ver também

- [[wiki/sources/botoes-e-links-guiar-jornada-consistencia-anatomia-hover]] — anatomia do botão, primário preenchido e secundário vazio, hover
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — contraste de texto sobre imagem
- [[wiki/sources/elementos-da-interface-visao-geral-proposito-consistencia-simplicidade]] — cor e tipografia entre os elementos da interface
