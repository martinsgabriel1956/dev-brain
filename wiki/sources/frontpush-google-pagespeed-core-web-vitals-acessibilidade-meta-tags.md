---
type: source
title: "Google PageSpeed: Core Web Vitals, acessibilidade, SEO e meta tags (FrontPUSH)"
aliases: ["FrontPUSH otimização aula 05", "Google Page Speed", "módulo de otimização, aula 05", "PageSpeed parte 1"]
date_created: 2026-11-19
date_updated: 2026-11-19
source_count: 0
tags: [performance, core-web-vitals, lcp, inp, cls, fid, pagespeed, lighthouse, acessibilidade, contraste, wcag, seo, html-semantico, meta-tags, open-graph, theme-color, curso, frontend]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-google-pagespeed-core-web-vitals-acessibilidade-meta-tags.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-19
---

# Google PageSpeed: Core Web Vitals, acessibilidade, SEO e meta tags (FrontPUSH)

## TL;DR

Aula 05 do módulo de otimização do [[wiki/entities/frontpush|FrontPUSH]], cerca de 18,5 min, primeira de duas sobre o PageSpeed Insights. [[wiki/entities/nasser|Násser]] (diz o nome nas perguntas retóricas) explica o relatório além do desempenho.

- **[[wiki/concepts/core-web-vitals|Core Web Vitals]] = experiência do usuário.** Três se destacam: "carregamento do primeiro elemento visível" (ele mostra o FCP; verde até 2,5 s; a página dá 1,3 s no desktop e 2,6 s, laranja, no celular), "tempo de interação" (resposta a clique em até 100 ms) e "mudança de layout" (anúncio que surge e empurra a página, chamado de "dark pattern").
- **Quatro notas:** desempenho (imagens são "60%, 70%"; depois, JavaScript não usado), acessibilidade, práticas recomendadas e SEO.
- **Acessibilidade:** "tipografia, carro-chefe" ([[wiki/concepts/escala-tipografica]]: mínimo 14 px, ele usa 16); [[wiki/concepts/contraste]] testado no [[wiki/entities/who-can-use|Who Can Use]] (#999 falha, #777 falha em parte, #666 passa AA mas falha no sol); `alt` nas imagens ([[wiki/concepts/texto-alternativo]]); tamanho mínimo de botão e input ([[wiki/concepts/area-clicavel]]).
- **SEO e práticas recomendadas:** o Google "baixa a internet todos os dias"; links dentro de `header`, `nav` e `menu` mostram os principais links ([[wiki/concepts/html-semantico]], [[wiki/concepts/seo]]).
- **Meta tags:** o modelo HTML5 traz só charset, viewport e title, "insuficiente". Ele acrescenta `lang` pt-br, `theme-color` (cor da barra do sistema no celular), `keywords` (geradas no ChatGPT), author, title, description e a imagem de pré-visualização, repetidas com `property` para Facebook e Twitter ([[wiki/concepts/open-graph]], [[wiki/concepts/head-html-metadados]]).

## Key Claims

- **O Google indexa pela experiência.** "O que que o Google leva em consideração para melhor indexar a sua página? [...] avaliação das Core Web Vitals [...] é experiência do usuário."
- **Três métricas principais.** "Carregamento do primeiro elemento visível, tempo de interação e mudança de layout." Evidência: tela do PageSpeed da página de energia solar.
- **Primeiro elemento: FCP, até 2,5 s.** "First Contentful Paint [...] o tempo que demora para poder aparecer o primeiro elemento visível"; "no máximo classificar ali como verdinho, 2.5 segundos". Medido: 1,3 s no computador, 2,6 s no celular ("laranjinha", "dá para melhorar").
- **Interação: até 100 ms.** "Tempo de interação tem que ser menor que 100 milissegundos. Ou seja, se eu cliquei em alguma coisa, ela tem que me devolver alguma resposta [...] em até 100 milissegundos." Exemplo: menu de colapsar.
- **Mudança de layout é dark pattern.** "Apareceu uma propaganda e modificou o layout que você estava navegando de forma abrupta, sem você pedir. Dark pattern." Também o "xzinho bem pequenininho", com "área de contato muito pequena", e o clique sem querer no anúncio.
- **Desempenho: imagem e JavaScript.** "Coisa de 60%, 70% da imagem"; "quando não é desempenho, é JavaScript. Muito script que não está sendo utilizado [...] só acumulando lixo de código."
- **Acessibilidade é tipografia.** "Tipografia, carro-chefe de acessibilidade"; fontes "no mínimo 14 pixels", "eu sempre coloco no mínimo de 16 pixels"; título mais contrastante que o corpo, "mas não o suficiente para poder não passar no teste do AAA". "Por favor, não utilize amarelo com branco."
- **Who Can Use simula condições.** #999 em fundo branco: "fail, fail, fail"; #777: "falhou em alguns"; #666: "passou, só que agora com nota AA", mas "falhou quando [...] tem a luz do sol" (brilho baixo, economia de bateria).
- **`alt` descreve a imagem** "como a pessoa não consegue enxergar a imagem". Mais "regras de tamanho mínimo de botão, tamanho mínimo de input, contraste".
- **O Google rastreia tudo.** "Ele baixa a internet todos os dias [...] quanto mais fácil você deixar para o Google indexar isso, melhor ele te ranqueia também."
- **HTML semântico mostra os principais links.** O Google "vai procurar a tag A [...] dentro de alguma tag de header, dentro de alguma tag de nav, dentro de alguma tag de menu" e conclui "que esses são os principais links do site"; também `section`/`article` para classificar o conteúdo.
- **O modelo HTML5 é insuficiente.** "Ele só vem com duas tag-metas, que é a tag-meta de viewport e a tag-meta da codificação UTF-8 [...] e um título. Isso aqui, pessoal, é insuficiente." E: "ele traz a language en, você tem que vir aqui e colocar pt-br."
- **`theme-color` pinta a barra do sistema.** "Você coloca o theme color como o content do hexadecimal do fundo da sua página", para a hero ficar "completinho sem essa barra de status [...] cortando". "Uma firulinha que é interessante."
- **`keywords` pelo ChatGPT.** "Quais são as principais palavras-chave que eu posso colocar na minha aplicação para melhor indexar ao Google, dado que o meu nicho é energia solar" ([[wiki/entities/openai|ChatGPT]]).
- **Título, descrição e imagem geram a pré-visualização** do link num chat, como no YouTube; a imagem é um PNG. "Eu repito essas mesmas informações com diferentes propriedades pra poder ele ser amplamente compartilhado pelo Facebook ou pelo Twitter", "só mudando essa propriedadezinha aqui, property".

## Entities

- [[wiki/entities/nasser]]: instrutor; diz o nome.
- [[wiki/entities/frontpush]]: curso; aula 05 do módulo de otimização; Notion com o Who Can Use em "cores".
- [[wiki/entities/google]]: PageSpeed Insights, Search, documentação de acessibilidade.
- [[wiki/entities/who-can-use]]: teste de contraste com simulações.
- [[wiki/entities/openai]]: o ChatGPT como gerador de palavras-chave.
- [[wiki/entities/meta]]: o Facebook, dono do Open Graph.

## Concepts

- [[wiki/concepts/core-web-vitals]]: LCP, INP, CLS (e o FCP e o FID da aula).
- [[wiki/concepts/seo]]: rastreamento, indexação, ranking.
- [[wiki/concepts/open-graph]]: `og:` e Twitter Cards para a pré-visualização.
- [[wiki/concepts/head-html-metadados]]: o `<head>` além do modelo do Emmet.
- [[wiki/concepts/html-semantico]]: `nav`, `header`, `section`, `article`.
- [[wiki/concepts/acessibilidade]], [[wiki/concepts/wcag]], [[wiki/concepts/contraste]], [[wiki/concepts/razao-de-contraste]]: o teste AA/AAA.
- [[wiki/concepts/escala-tipografica]], [[wiki/concepts/hierarquia-visual]]: fonte mínima e hierarquia.
- [[wiki/concepts/texto-alternativo]]: `alt`.
- [[wiki/concepts/area-clicavel]]: o "xzinho" pequeno.

## Precisões e tensões com a wiki

- **O "primeiro elemento visível" dos Core Web Vitals é o LCP, não o FCP.** O trio é LCP (Largest Contentful Paint, o *maior* elemento visível), INP e CLS. O limite de 2,5 s que ele cita é o do LCP; o do FCP é 1,8 s. O FCP é métrica de diagnóstico ([[wiki/concepts/core-web-vitals]]). `[external]` https://web.dev/articles/vitals. Confiança alta.
- **Os 100 ms são do FID, aposentado.** O "tempo de interação" com limite de 100 ms é o FID (First Input Delay), que media só o atraso da primeira interação. Desde 12/03/2024 o Core Web Vital é o INP (Interaction to Next Paint), que mede todas as interações até a próxima pintura, com "bom" até 200 ms. `[external]` https://web.dev/blog/inp-cwv-launch. Tensão interna: na [[wiki/sources/frontpush-introducao-otimizacao-web-minificacao-css-js|aula 01]] ele já cita o INP; aqui usa o limite do FID, provavelmente de um material anterior a 2024. Confiança alta.
- **Mudança de layout não é dark pattern.** CLS mede quanto o conteúdo pula sem o usuário pedir: anúncio sem espaço reservado, imagem sem `width`/`height`, fonte trocando. Dark pattern é design que engana de propósito (cancelamento escondido, opção pré-marcada). O anúncio que empurra o botão para você clicar nele pode ser as duas coisas, mas a métrica não julga intenção. O "xzinho" pequeno é [[wiki/concepts/area-clicavel|área clicável]], e o anúncio que cobre a tela sem mover nada não gera CLS; é o que o Google chama de intersticial intrusivo, outra regra. Confiança alta.
- **A nota não é o ranking.** As quatro notas são do Lighthouse, em laboratório. O ranking usa o dado de campo (CrUX) dos Core Web Vitals; acessibilidade e "práticas recomendadas" do Lighthouse não são fatores de ranking. Confiança alta.
- **"Práticas recomendadas" não é HTML semântico.** No Lighthouse, Best Practices verifica HTTPS, erros no console, APIs obsoletas, proporção de imagens, bibliotecas com vulnerabilidade conhecida. HTML semântico e meta tags caem em SEO e em acessibilidade. A aula junta as duas categorias. Confiança alta.
- **Acessibilidade no Lighthouse não é "basicamente tipografia".** A categoria roda o axe-core: contraste, `alt`, `label` em campos, nome acessível em botões e links, `lang` no `<html>`, ARIA válido, ordem de títulos, alvos de toque. Tamanho de fonte nem é auditoria de acessibilidade; era auditoria de SEO ("fontes legíveis") (sem fetch). Contraste e `alt` são os achados mais frequentes. Confiança alta.
- **AA é a meta, AAA é o extra.** O Lighthouse e a maioria das leis cobram WCAG nível AA: 4,5:1 para texto normal, 3:1 para texto grande. AAA (7:1) é recomendável, não exigido. Os números da demonstração batem: #999 em branco ≈ 2,8:1 (falha), #777 ≈ 4,5:1 (no limite, falha por pouco em texto normal), #666 ≈ 5,7:1 (passa AA, falha AAA) ([[wiki/concepts/razao-de-contraste]]). Confiança alta.
- **`alt` não é sempre descrição.** Imagem decorativa leva `alt=""`, para o leitor de tela pular; imagem informativa descreve a função, não a aparência ([[wiki/concepts/texto-alternativo]]). Confiança alta.
- **`lang` é atributo, não meta tag.** O `pt-br` vai em `<html lang="pt-BR">`; o Lighthouse checa isso em acessibilidade, porque o leitor de tela escolhe a voz pela língua. Confiança alta.
- **`meta keywords` não serve para o Google.** O Google ignora a tag desde 2009 (anúncio oficial do Google Webmaster Central, setembro de 2009; sem fetch nesta sessão). Pedir as palavras ao ChatGPT ajuda a pensar o *conteúdo* e o `<title>`, não a tag. Confiança alta.
- **`description` e `title` aparecem no buscador também.** O `<title>` é o título azul do resultado e a `meta description` costuma virar o trecho abaixo (o Google pode reescrever). Para a pré-visualização em chat, o que conta é o [[wiki/concepts/open-graph|Open Graph]] (`og:title`, `og:description`, `og:image`, com `property`) e o Twitter Card (`twitter:card`, que usa `name`, não `property`). `og:image` pede URL absoluta e cerca de 1200×630. Confiança alta.
- **"Baixa a internet todos os dias".** O Googlebot rastreia de forma contínua, mas com frequência por site: página nova ou pouco linkada pode levar dias ou semanas. Para dar o "panorama geral" das páginas, o caminho oficial é o `sitemap.xml` e o Search Console; links no `nav` ajudam a descoberta, mas o Google segue qualquer `<a href>`, semântico ou não. Confiança alta.
- **`theme-color` pinta a interface do navegador**, não o sistema: a barra de endereço do Chrome no Android e a barra do Safari. A barra de status do sistema só muda com a página instalada como PWA. Aceita `media="(prefers-color-scheme: dark)"` para tema escuro. Confiança média (o suporte do Safari mudou entre versões).
- **"Sessão" é seção.** A legenda escreve "sessão" (homófono); corrigido no raw.

## Open Questions

- Qual página é a da demonstração? Provavelmente a Solten, pelo nicho de energia solar citado no ChatGPT.
- A "parte 2" do PageSpeed vai mostrar os avisos de diagnóstico um a um: conferir se aparecem LCP, CLS e INP pelo nome. **Respondida** em [[wiki/sources/frontpush-relatorio-pagespeed-imagens-render-blocking-dom-regra-80-20]]: não aparecem; a aula 06 só lê os diagnósticos.
- De onde vêm os 100 ms? Material anterior a 2024 (FID) ou confusão com o limite de "resposta instantânea" de UX (100 ms, Nielsen)?

## Raw quotes

- "Tipografia, carro-chefe de acessibilidade."
- "Por favor, não utilize amarelo com branco."
- "ele baixa a internet todos os dias"
- "Isso aqui, pessoal, é insuficiente, tá?"
- "uma firulinha que é interessante"
- "Como é que você tem inspirações para palavra-chave? ChatGPT."
