---
type: entity
title: "Who Can Use"
aliases: ["whocanuse", "whocanuse.com", "WhoCanUse"]
date_created: 2026-11-13
date_updated: 2026-11-15
source_count: 2
tags: [ferramenta, acessibilidade, contraste, wcag, cor, tipografia]
skill: ux-ui-mentor
status: stub
---

# Who Can Use

Ferramenta web de [[wiki/concepts/contraste]]: recebe a cor do texto e a cor do fundo, calcula a razão de contraste e mostra a nota WCAG para cada tipo de visão simulada. [[wiki/entities/nasser|Násser]] a indica no Notion do curso, seção de tipografia, e a usa para conferir o card do blog com gradiente: "deu uma nota 3A" ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]).

`[external]` Feita por Corey Ginnivan, com código aberto (https://github.com/coreyginnivan/whocanuse/). Simula visão tricromática, oito tipos de daltonismo (protanomalia a acromatopsia), catarata, glaucoma, baixa visão e duas situações: luz solar direta e modo noturno. A nota combina contraste, tamanho e peso do texto, ao contrário do que diz a aula ("ele só avalia a cor") (https://www.whocanuse.com/).

## Limite

Compara duas cores sólidas. Sobre foto, o fundo varia ponto a ponto; meça no pior ponto atrás do texto. Ver [[wiki/concepts/texto-sobre-imagem]].

## Na aula de variação de cores

Volta como a ferramenta de contraste que ele cita "bastante em tipografia" (identificação inferida pela descrição): o verde claro da marca dele com texto branco dá fail; com preto, AAA e 10.50:1 ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]). Ele descreve "regular vision" como quem "não consegue distinguir as três cores primárias"; na ferramenta, Regular Vision (Trichromatic) é a visão típica.

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — complemento à seção de contraste; notas "A, 2A, 3A"
- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — verde claro + branco reprova, preto AAA; "regular vision" mal descrita
