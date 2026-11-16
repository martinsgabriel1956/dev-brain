---
type: entity
title: "Unsplash"
aliases: ["unsplash.com", "Unsplash+"]
date_created: 2026-11-13
date_updated: 2026-11-16
source_count: 9
tags: [banco-de-imagens, fotografia, licenca, figma]
skill: ux-ui-mentor
status: stub
---

# Unsplash

[[wiki/concepts/banco-de-imagens|Banco de imagens]] com o slogan "The Internet's Source of Freely Usable Images". É o que [[wiki/entities/nasser|Násser]] mais usa, "de disparado": ao enviar fotos, os fotógrafos aceitam a licença de uso livre. As fotos vêm em alta resolução (exemplo da aula: 3285×4800) e há plugin no [[wiki/entities/figma]], que entrega uma versão um pouco reduzida. Todas as imagens do blog pessoal do autor vieram dele ([[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]).

`[external]` A licença permite uso comercial e não comercial sem atribuição obrigatória, mas proíbe vender a foto sem alteração e montar serviço concorrente (https://unsplash.com/license). O Unsplash+ (pago, desde 2022) mistura imagens com outra licença na mesma busca.

## Fotos de fundo preto para blend modes

Na parte 3, as fotos de fundo preto do Unsplash viram os wallpapers do [[wiki/entities/frontpush]]: modo lighten e temperatura mais fria ([[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]]). Ver [[wiki/concepts/blend-modes]].

## Medir variações naturais

Na aula de variação de cores, Násser abre fotos do Unsplash e mede com o ColorZilla os tons de uma mesma cor: os claros têm menos saturação e mais brilho ([[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]]). Ver [[wiki/concepts/variacao-de-cores]].

## Na NLW #1, dia 3 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] busca "recycle" no Unsplash e cola o endereço das imagens nos cards da página de resultados, como provisórias até virem do banco de dados.

## Na NLW #1, dia 5 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] copia o link de imagens de reciclagem do Unsplash para o campo `image` dos pontos cadastrados no SQLite.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]], a imagem fixa dos pontos de coleta vem do Unsplash, reduzida pela URL com `w=400&q=60`.

Em [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]], a foto de teste do upload também vem do Unsplash.

## Key Sources

- [[wiki/sources/imagens-e-ilustracoes-formatos-bancos-otimizacao]]
- [[wiki/sources/imagens-e-ilustracoes-bom-senso-contraste-padronizacao-blend-modes]] — fotos de fundo preto usadas com blend modes nos wallpapers do FrontPUSH
- [[wiki/sources/imagens-e-ilustracoes-introducao-svg-bancos-texto-branco-resolucoes-formatos]] — edição "W7": o mais usado "de disparado", 0800, uso pessoal e comercial; plugin no Figma
- [[wiki/sources/imagens-e-ilustracoes-pratica-figma-importar-editor-plugins-exportacao]] — exemplo de instalação de plugin pela Community
- [[wiki/sources/variacao-de-cores-tons-claros-escuros-hsb-padrao-de-luminosidade]] — fotos usadas para medir tons claros e escuros com o ColorZilla
- [[wiki/sources/nlw-1-dia-3-itens-de-coleta-modal-pagina-de-resultados-ecoleta]]: imagens provisórias dos cards do Ecoleta
- [[wiki/sources/nlw-1-dia-5-banco-de-dados-sqlite-cadastro-pesquisa-ecoleta]]: imagens dos pontos no banco
- [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]]: imagem provisória dos pontos, redimensionada pela URL
- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: imagem de teste do upload
