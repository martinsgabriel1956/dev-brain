---
type: source
title: "Instalação do Sass: Live Sass Compiler no VS Code e Scout-App (FrontPUSH)"
aliases: ["Instalação SASS", "FrontPUSH instalação Sass", "módulo de CSS Sass, aula 02", "Live Sass Compiler FrontPUSH"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [css, sass, scss, live-sass-compiler, scout-app, prepros, vs-code, live-server, minificacao, source-map, frontend, curso]
skill: tech-mentor-frontend
status: draft
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/frontpush-instalacao-sass-live-sass-compiler-scout-app.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-16
---

# Instalação do Sass (FrontPUSH)

## TL;DR

Aula 02 do módulo de CSS Sass do [[wiki/entities/frontpush|FrontPUSH]], com [[wiki/entities/nasser|Násser]] ("Ah, Násser, por que você vai utilizar no próprio VS Code?"). Duas formas de compilar o [[wiki/concepts/pre-processador-css|Sass]]:

- **No [[wiki/entities/vs-code]]**, com a extensão [[wiki/entities/live-sass-compiler]]: o caminho que ele usa no curso, porque fica "tudo no próprio Visual Studio", sem aplicativo externo. Botão "Watch Sass"; gera o `.css`, um `.map` e já acrescenta `-webkit-` e `-ms-`.
- **Com o [[wiki/entities/scout-app]]**, aplicativo gráfico "free e open source" para Windows, Linux e Mac, para os alunos em que a extensão não rodou. Pastas de entrada e saída, modo expandido ou `compressed`.
- **Por que não a linha de comando:** exige "um conhecimento prévio maior" de terminal e muda conforme o sistema, mas "não é nenhum bicho de sete cabeças" ([[wiki/concepts/shell-terminal]]).
- **Outros aplicativos** da página de instalação do Sass: CodeKit (pago, Mac), Ghostlab (pago, Mac e Windows), Hammer, LiveReload e Prepros (trial ilimitado com pop-up pedindo pagamento).
- **Regra repetida:** o navegador não lê Sass; o HTML linka o `.css` gerado.

## Key Claims

### Por que o VS Code

- "Ele me traz a comodidade de já ter um plugin pronto que compile o Sass, e eu tenho tudo no próprio Visual Studio, então eu faço toda a gerência sem utilizar aplicativos externos."
- "Teve alguns alunos que tiveram problemas com o plugin [...] não estavam conseguindo rodar nas suas respectivas máquinas, e eu não sei exatamente o porquê." Por isso o Scout-App: "ele é free e é multiplataforma".

### Linha de comando × aplicativos

- O site do Sass ("CSS with superpowers") tem, em *install*, as opções de linha de comando e de aplicativos.
- "Linha de comando talvez exija de vocês um conhecimento prévio maior [...] e depende se [...] você está utilizando o Windows, ou o próprio Linux, ou o próprio Mac."
- Lista: "o CodeKit, ele é pago para Mac, tem o Ghostlab, ele também é pago para Mac e Windows, o Hammer, o LiveReload". Prepros: dá para usar "sem precisar pagar, mas ele sempre vai ter um pop-up falando assim, 'pague'"; suporta Sass, Less e outros pré-processadores, e "algumas funções de JavaScript".

### Live Sass Compiler

- Procurar "Live Sass Compiler" nas extensões, instalar e habilitar. "É uma das minhas [...] extensões do VS Code que eu não consigo viver sem, porque ele traz dois recursos."
- Recurso 1, a "live": "automaticamente ele cria um servidorzinho em localhost, e aí, quando você salva, ele automaticamente modifica e atualiza o seu browser". "Open with Live Server", porta 5500 ([[wiki/concepts/setup-live-reload-debug-testes]], [[wiki/concepts/porta-de-rede]]).
- Recurso 2, o compilador: "um botãozinho com esse olhinho [...] em Watch Sass".
- Projeto: pasta `SassAula`, `index.html` (HTML5), `css/style.scss`. Reset de `padding`, `margin` e `box-sizing: border-box` ([[wiki/concepts/estilos-padrao-do-navegador-e-reset]]); `body` com fundo `#0c0c0c` e `display: flex` + `justify-content: center` + `align-items: center` para centralizar ([[wiki/concepts/flexbox]]); `h1` branco.
- Salvar sem compilar: "não aconteceu absolutamente nada. Por quê? Primeiro, eu não linquei e não gerei o arquivo CSS."
- Com Watch Sass: "ele gerou dois arquivos: é um map, onde tem as configurações [...] vou falar dele posteriormente", e um CSS "já otimizado com os traços webkit, com o traço ms, para poder melhorar a compatibilidade com browsers antigos" ([[wiki/concepts/prefixo-de-fornecedor]]).
- "Você percebe que é CSS, não é Sass, que a gente linka." O compilador também avisa "quando tiver algum erro".

### Scout-App

- Baixar, extrair (ele usa `C:` no Windows) e abrir. Antes, parar o Watch Sass e apagar os arquivos gerados, "para poder [...] não ter conflito".
- Input folder e output folder "pode ser a mesma pasta", ou uma pasta `scss` e outra `css`: "também é uma forma de você estar se organizando".
- Modos: desenvolvimento (expandido) ou produção (`compressed`): "ele já tira os enters, as quebras de linha, os espaços, fazendo com que o seu CSS já seja cuspido de maneira otimizada com relação ao tamanho". Play para começar, pause para trocar o modo.
- "Isso aqui faz com que o arquivo fique bem menor, melhorando o tempo de requisição." Ver [[wiki/concepts/pipeline-de-assets]].

## Entities

- [[wiki/entities/nasser]]: instrutor (diz o nome).
- [[wiki/entities/frontpush]]: curso; aula 02 do módulo de CSS Sass.
- [[wiki/entities/vs-code]]: editor; onde roda o Live Sass Compiler.
- [[wiki/entities/live-sass-compiler]]: extensão usada no curso.
- [[wiki/entities/scout-app]]: aplicativo alternativo.

## Concepts

- [[wiki/concepts/pre-processador-css]]
- [[wiki/concepts/prefixo-de-fornecedor]]
- [[wiki/concepts/compatibilidade-entre-navegadores]]
- [[wiki/concepts/pipeline-de-assets]]
- [[wiki/concepts/setup-live-reload-debug-testes]]
- [[wiki/concepts/porta-de-rede]]
- [[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]
- [[wiki/concepts/estilos-padrao-do-navegador-e-reset]]
- [[wiki/concepts/flexbox]]
- [[wiki/concepts/shell-terminal]]
- [[wiki/concepts/compilador]]

## Precisões e tensões com a wiki

- **Os "dois recursos" são duas extensões.** `[external]` "Open with Live Server" vem da extensão Live Server. O Live Sass Compiler original (Ritwick Dey) tinha o Live Server como dependência "for live browser reload", por isso os dois apareciam juntos (https://github.com/ritwickdey/vscode-live-sass-compiler). O compilador em si só tem o "Watch Sass".
- **A extensão da aula foi descontinuada.** `[external]` O repositório de Ritwick Dey foi arquivado em 10/03/2022, e o README manda instalar o fork de Glenn Marks (`glenn2223.live-sass`), que mantém o botão "Watch Sass" / "Stop Watching Sass" (https://github.com/glenn2223/vscode-live-sass-compiler). A extensão original compilava com o LibSass (via sass.js), que não entende o `@use` e o `sass:math` do Sass moderno; o fork usa o Dart Sass (inferência a partir dos READMEs; confiança média).
- **Os prefixos vêm do Autoprefixer da extensão**, e não do Sass. Confirma o que a [[wiki/sources/frontpush-introducao-sass-pre-processador-sass-vs-scss|aula 01]] mostrou. `[external]` A extensão original tinha `liveSassCompile.settings.autoprefix` ligado por padrão (alvo `> 1%, last 2 versions`), o que explica o `-webkit-` e o `-ms-` sem configuração nenhuma. O padrão foi lembrado, não relido; o README não foi buscado nesta ingestão (confiança média).
- **Scout-App parado.** `[external]` O último commit é de 21/06/2021, e o app usa `node-sass` 4.x, ou seja, LibSass, descontinuado em 2020 (https://github.com/scout-app/scout-app, https://sass-lang.com/blog/libsass-is-deprecated/). Hoje a página de instalação do Sass lista só o CodeKit (pago, Mac) e o Prepros (pago, Mac, Windows e Linux) como aplicativos (https://sass-lang.com/install/). Para projeto novo, `npm install -D sass` e `sass --watch scss:css` funcionam igual em Windows, Linux e Mac.
- **"O Sass não é compilado"** é lapso: ele é compilado; o que não acontece é o navegador lê-lo. Ele mesmo diz isso no resto da frase.
- **`.map` é source map.** `[external]` Mapeia o CSS gerado de volta para as linhas do `.scss`; o DevTools usa isso para mostrar o arquivo-fonte. São "configurações" só no sentido de metadados. Não vai para produção, ou vai só se o time quiser depurar em produção.
- **`compressed` × produção hoje.** `[skill: tech-mentor-frontend]` O `--style=compressed` do Sass faz a parte de tirar espaços da [[wiki/concepts/pipeline-de-assets|minificação]]. Em produção, o servidor ainda aplica gzip/brotli, e o ganho de tempo vem dos dois somados. Em projetos com bundler (Vite etc.), o Sass entra como etapa do build, e o minificador é Lightning CSS ou esbuild.
- **Live Server é servidor estático.** Serve arquivos e recarrega; não roda aplicação ([[wiki/concepts/servidor-web-vs-servidor-de-aplicacao]]).
- **`height` de 100px** no Scout-App, depois de dizer no VS Code que o body teria "o tamanho da tela cheia". Para isso seria `100vh` ([[wiki/concepts/unidades-de-medida-css]]).
- **Responde a uma pergunta da wiki.** "A gente starta o SAS", da [[wiki/sources/frontpush-mentoria-pratica-com-css-grid|mentoria de CSS Grid]], é o "Watch Sass" do Live Sass Compiler (inferência: é o fluxo do curso).

## Open Questions

- "Procure lá nas aulas introdutórias do próprio Script F": nome de módulo ou erro da legenda? A aula de configuração do VS Code é [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]].
- "Se ela perceber que o CSS que está sendo cuspido": provavelmente "se você perceber"; mantido.
- A aula sobre o `.map` ("vou falar dele posteriormente") ainda não chegou à wiki.

## Raw quotes

- "não é nenhum bicho de sete cabeças"
- "é CSS, não é Sass, que a gente linka"
- "uma das minhas [...] extensões do VS Code que eu não consigo viver sem"
