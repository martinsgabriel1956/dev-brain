---
type: source
title: "NLW #1 com Diego Fernandes, dia 1: Ecoleta, API REST, TypeScript, Node, React e React Native"
aliases: ["NLW 1 Diego dia 1", "Next Level Week 1 Diego Fernandes dia 1", "Ecoleta TypeScript", "Ecoleta API REST", "NLW 1 trilha Node React React Native"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 0
tags: [nodejs, typescript, express, ts-node, npm, npx, api-rest, json, mvc, react, spa, create-react-app, componentizacao, react-native, expo, mobile, homebrew, chocolatey, vs-code, frontend, backend, rocketseat, ecoleta, iniciante]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/nlw-1-diego-fernandes-dia-1-ecoleta-api-rest-typescript-react-native.md"
source_url: ""
author: "Diego Fernandes"
date_published: ""
date_ingested: 2026-11-16
---

# NLW #1 com Diego Fernandes, dia 1: Ecoleta, API REST, TypeScript, Node, React e React Native

## TL;DR

Primeira aula prática (cerca de 1h10) da trilha da [[wiki/entities/next-level-week|Next Level Week #1]] conduzida por [[wiki/entities/diego-fernandes]], da [[wiki/entities/rocketseat]]. É o mesmo projeto, o Ecoleta, que a wiki já tem na versão de [[wiki/entities/mayk-brito]] ([[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta|dias 1–5]]). Aqui a pilha é outra: API em Node com TypeScript, web em React e app em React Native. A aula tem sete partes:

1. **O layout do Ecoleta.** Na web, a entidade cadastra o ponto de coleta: imagem, contato, endereço marcado no mapa e itens coletados. No celular, a pessoa escolhe UF e cidade, vê os pontos no mapa, filtra por item e abre o detalhe, com WhatsApp (deep linking) e e-mail (Mail Compose).
2. **O ambiente.** [[wiki/entities/nodejs|Node.js]] LTS (12, em 2020) instalado por [[wiki/concepts/gerenciador-de-pacotes|gerenciador de pacotes]]: Homebrew no macOS, Chocolatey no Windows (com PowerShell como administrador) e repositório da distribuição no Linux. Depois, o npm e o [[wiki/entities/vs-code]] com o tema Omni (derivado do Dracula) e o Material Icon Theme.
3. **Por que uma API RESTful.** O back-end cuida de regras de negócio, banco, e-mail, serviços externos, [[wiki/concepts/autenticacao-e-autorizacao|autenticação e autorização]] e criptografia. No "MVC" com [[wiki/concepts/template-engine|template engine]], a rota `/users` devolvia o HTML pronto. Numa [[wiki/concepts/api-rest|API REST]], ela devolve só os dados em [[wiki/concepts/json|JSON]], e qualquer cliente (React na web, React Native no celular) monta a tela.
4. **Por que TypeScript.** A função `displayUserInformation(user)`, esquecida há três meses, não diz se o campo é `user.city` ou `user.address.city`. Com tipos, o IntelliSense mostra. Depois vêm cinco mitos: produtividade, "vira Java", mercado, substituição do JavaScript e iniciantes. Ver [[wiki/entities/typescript]].
5. **O projeto Node.** `mkdir server`, `npm init -y` e o [[wiki/concepts/package-json|package.json]]. Depois, [[wiki/entities/express]], `node_modules` e `package-lock.json`, e o `src/server.ts`. O erro "could not find a declaration file" leva ao `@types/express` como dependência de desenvolvimento ([[wiki/concepts/arquivo-de-declaracao-de-tipos]]). Por fim, `app.get("/users")`, `app.listen(3333)`, `ts-node`, `typescript`, `tsc --init`, `response.send` → `response.json`, `ts-node-dev` e o script `npm run dev`.
6. **React e SPA.** React é uma "biblioteca para construção de interfaces" usada para [[wiki/concepts/single-page-application|single page applications]], com o pacote `react` compartilhado entre web e mobile, [[wiki/concepts/componentizacao|componentização]] e [[wiki/concepts/separacao-de-responsabilidades|divisão de responsabilidades]]. O projeto web sai de `npx create-react-app web --template typescript`, e o Hello World é um `<h1>` em `src/App.tsx` com cor `#7159c1`.
7. **React Native e Expo.** No modelo tradicional, há dois apps: iOS (Objective-C/Swift, IPA) e Android (Java/Kotlin, APK). O [[wiki/entities/react-native]] usa uma base só, com o JavaScript rodando no aparelho ("JavaScript Core") e interface nativa. O [[wiki/entities/expo]] poupa o Android Studio e o Xcode, porque o app Expo no celular já traz as APIs nativas.

Fecha com "talk is cheap, show me the code", de [[wiki/entities/linus-torvalds]], e anuncia o back-end para o dia seguinte.

## Key Claims

### O projeto: Ecoleta

- **Contexto:** "essa semana, desde a segunda-feira [...] começa a Semana Internacional do Meio Ambiente". O Ecoleta é "um mapa, um marketplace, uma conexão" entre entidades que coletam resíduos e pessoas que precisam descartá-los.
- **Exemplos de resíduos:** lâmpadas, pilhas e baterias (supermercados, "porque eles vendem e eles são obrigados a coletar"), óleo de cozinha, resíduos eletrônicos e orgânicos.
- **Layout "totalmente desenvolvido do zero"** pelo designer Thiago (o mesmo da versão do Mayk).
- **Web (React):** uma landing page, a página "cadastrar um ponto de coleta" (imagem, nome, e-mail, WhatsApp, endereço com "um ponto no mapa", itens coletados) e uma mensagem de sucesso.
- **Mobile (React Native):**
  - Splash screen, landing page com estado e cidade ("o estado aqui até deveria estar antes, porque ele é mais importante"), mapa com os pontos e filtro por item.
  - O detalhe do ponto traz imagem, nome, resíduos e endereço.
  - Para o WhatsApp, "um recurso chamado Deep Linking" abre o app instalado ([[wiki/concepts/mobile-deep-links]]). Para o e-mail, "Mail Compose" cria a mensagem "sem sair" do app.

### Ambiente: Node e gerenciadores de pacotes

- **LTS:** "Eu sempre recomendo você utilizar a versão LTS, Long Term Support". A versão mais atual "pode ter alguma falha e pode não se comportar muito bem" com React, React Native e Expo. A faixa pedida vai de 11 a "no máximo [...] 12.alguma coisa". Ver as tensões.
- **Evitar o instalador "next, next, next":** ele "deixa resquícios na nossa máquina", e depois "é muito difícil a gente remover ou alterar a sua versão". Por isso, gerenciador de pacotes. Ver [[wiki/concepts/gerenciador-de-pacotes]].
- **macOS:** o Homebrew sai de um comando em Ruby, que "já vem instalado em todo Mac por padrão". Depois, `brew install node@12`; só a versão principal, "ele já vai pegar a última".
- **Windows:**
  - Chocolatey pelo PowerShell como administrador. O PowerShell é "muito mais performático" que o CMD e roda comandos "que antes estavam disponíveis só no Linux".
  - `Get-ExecutionPolicy`: se der Restricted, um comando muda a política; se der Bypass, "pode continuar".
  - O teste é `choco`; se der "comando não encontrado", reinicie: "a gente resolve muito problema reiniciando a máquina".
  - A instalação é `cinst nodejs-lts`; `cinst` "é a mesma coisa que Choco Install".
- **Linux:** "o mais fácil de todos". Ele vai em "Node.js Binary Distributions" para Debian/Ubuntu e roda os comandos da versão 12 como root.
- **Conferência:** `node -v` (12.13 na máquina dele) e `npm -v`. O npm "vem junto com o Node" e equivale ao Composer do PHP, ao pip do Python e às gems do Ruby: serve para "instalar pacotes de terceiros".

### Visual Studio Code

- **"Totalmente opcional":** "quer usar Sublime, Atom, [...] PhpStorm, use o que você gostar".
- **Tema Omni:** "um tema que a gente desenvolveu aqui dentro da própria Rocket", "totalmente baseado no Drácula", mais escuro e "mais pro roxo da Rocketseat". Para quem prefere mais claro, o próprio Dracula.
- **Material Icon Theme:** ícones por tipo de arquivo, "só perfumaria". Diego promete ensinar o resto do setup no fim da semana. Ver [[wiki/entities/vs-code]].

### Por que uma API RESTful

- **REST como padronização:** a API "vai seguir algumas regras, ela vai seguir uma padronização [...] Se a nossa API segue os padrões REST, a nossa API é RESTful". Ver [[wiki/concepts/api-rest]].
- **O que o back-end faz:**
  - "Regras de negócio" e "o core da nossa aplicação"; "o front-end [...] não define como que a nossa aplicação se comporta".
  - Conexão com o banco, envio de e-mails e "serviços externos" (cálculo de frete).
  - Autenticação ("logar e deslogar") e autorização ("o que o usuário [...] tem permissão para fazer"). Ver [[wiki/concepts/autenticacao-e-autorizacao]].
  - Criptografia e "a parte de segurança".
- **O jeito antigo:** MVC é "Model, View e Controller", e a View era um template engine no back-end: Blade no Laravel, Handlebars, EJS e [[wiki/entities/nunjucks]] no Node. "Barra users [...] devolvia não só os dados do usuário, como todo HTML da página." Ver [[wiki/concepts/template-engine]].
- **O jeito REST:** "eu vou retornar apenas os dados dos usuários e não todo o HTML", em JSON, "uma estrutura muito parecida com a de um objeto dentro do JavaScript". O exemplo é um array de objetos com nome e e-mail (Diego Fernandes). Ver [[wiki/concepts/json]].
- **Por que isso importa: vários clientes.** "O React Native ele não lê HTML". Sem uma API, seria preciso "criar uma estrutura totalmente separada" para o app. Com ela, há "uma forma única de retornar dados das entidades". Ver [[wiki/concepts/arquitetura-cliente-servidor]] e [[wiki/concepts/renderizacao-ssr-vs-csr]].
- **Prática antes da teoria:** "entender na prática é muito melhor do que entender na teoria".

### Por que TypeScript

- **Definição:** "um superset, tem gente que chama de linguagem", "o JavaScript com superpoderes", "com a possibilidade de nós adicionarmos tipagens". Ver [[wiki/entities/typescript]] e [[wiki/concepts/sistema-de-tipos]].
- **O problema da função esquecida:** a tarefa é incluir cidade e UF no retorno de `displayUserInformation`, e as dúvidas se acumulam:
  - "Qual o formato do objeto de usuário?"
  - `user.city` ou `user.address.city`?
  - Um `console.log` resolve se a função "pode ser chamada em tantos lugares diferentes"?
  - Os campos são obrigatórios, ou precisam de um valor padrão?
- **IntelliSense:** "Sabe quando a gente digita um pouquinho do nome da variável e dá um CTRL espaço [...] e às vezes não mostra nada?" Com o tipo declarado, o editor sabe que `user` tem `name`, `email` e `address.city`/`uf`. "Essa é a essência do TypeScript. Facilitar a vida para o desenvolvedor."
- **Mitos e verdades:**
  - *Diminui a produtividade?* "Sim e não." No começo, para quem vem de tipagem dinâmica (PHP, JS); quem vem de Java ou C# "vai se sentir em casa". A produtividade faz "um J": "começa lento e daqui a pouco explode".
  - *Vira Java ou C#?* Não: "a gente continua utilizando o JavaScript da maneira que a gente já conhece". Pela inferência de tipos, só "10%, 15% dos casos" pedem anotação.
  - *O mercado não usa?* "Um mito dos maiores", e por isso o tema entrou na NLW, "pelo bem da sua carreira".
  - *Substitui o JavaScript?* Não. O TypeScript é "totalmente baseado no JavaScript", as mudanças do JS "vão ser refletidas no TypeScript de forma automática", e o código "é convertido para JavaScript, principalmente quando ele for executar no browser".
  - *Atrapalha o iniciante?* "Depende muito." Atrapalha "um pouquinho bem no início".

### Projeto Node com TypeScript e Express

- **Estrutura:** `mkdir server` e `npm init -y`, com o `-y` "para o npm não fazer as questões". O comando `code .` abre o VS Code (no Mac e no Linux, via "Install Code Command in Path").
- **[[wiki/concepts/package-json|package.json]]:** nome, versão, descrição, arquivo principal, scripts, autor, licença e, "muito interessante", as dependências com versão.
- **[[wiki/entities/express]]:** "um micro framework para lidar com rotas". `npm install express` cria `dependencies`, `node_modules` e `package-lock.json`. Diego chama o lock de "arquivo de cache" e diz que "a gente nunca vai precisar mexer aqui dentro"; ver as tensões. O `node_modules` tem muitas pastas porque o Express "também tem as suas próprias dependências" (accepts, array-flatten, body-parser).
- **`src/server.ts`:** "eu utilizo sempre o ts ao invés do js. Mas o código é exatamente o mesmo."
- **Definição de tipos:**
  - O import do Express mostra "could not find a declaration file for module express".
  - Algumas bibliotecas trazem os tipos junto; outras os separam, e aí entra `npm install @types/express -D`. O `@types` é "o repositório que mantém a grande maioria das definições de tipos".
  - `-D` é dependência de desenvolvimento, porque em produção o código "já vai ter [sido] convertido" para JavaScript.
  - Ctrl+clique em `express` leva ao pacote de tipos: "Não existe código funcional aqui dentro". Ver [[wiki/concepts/arquivo-de-declaracao-de-tipos]].
- **Primeira rota:** `const app = express()` e `app.get("/users", (request, response) => ...)`. O primeiro argumento é "qual que é o recurso que eu tô querendo acessar", e o segundo, a função executada quando a rota é chamada. Depois vem `app.listen(3333)` ("eu particularmente sempre uso essa porta"). Ver [[wiki/concepts/recurso-rest]].
- **Rodar TypeScript:**
  - `node src/server.ts` "não vai funcionar", porque "o node ele só entende JavaScript".
  - Ele instala o `ts-node` como dependência de desenvolvimento e o executa com `npx`, que "serve para a gente executar um pacote que a gente instalou" (os binários de `node_modules/.bin`).
  - Faltava o pacote `typescript`, e depois o `tsconfig.json`, criado com `npx tsc --init`: "eu não preciso mexer em nada praticamente dele".
- **request e response:**
  - O `request` serve para "obter dados da requisição", como o corpo de uma rota de criação; o `response`, para devolver a resposta. Sem resposta, o navegador "vai ficar aqui executando para sempre".
  - `response.send("hello world")` vem primeiro. Depois, `response.json([...])` com um array de nomes (Diego, Clayton, Robson, Daniel): "eu retorno ou um objeto ou um array". O ponto e vírgula "é totalmente facultativo".
  - A extensão JSON Viewer formata o JSON no navegador.
- **Reload automático:** `ts-node-dev` "vai ficar observando o nosso código". Depois ele cria o script `"dev": "ts-node-dev src/server.ts"`, rodado com `npm run dev`; o nome é livre ("se você botar aqui batata [...] vai funcionar").

### React e Single Page Applications

- **O que é:** "uma biblioteca para construção de interfaces", para "tudo aquilo que o usuário interage". Ver [[wiki/entities/react]].
- **[[wiki/concepts/single-page-application|SPA]]:** ao trocar da listagem para a edição, "eu não preciso ter um recarregamento completo da tela". Cabeçalho, menu e rodapé ficam, e só o conteúdo muda, "para o usuário ter uma performance melhor".
- **Biblioteca ou framework?** "Para mim tanto faz". Diego considera framework "principalmente por todo o ecossistema".
- **Tudo no JavaScript:** CSS, imagens e HTML são importados ou escritos dentro do JS. O exemplo é um botão que "é uma função que retorna o HTML". Ver [[wiki/concepts/jsx]].
- **Pacotes:** o `react` é "compartilhado tanto em aplicações web [...] e aplicações mobile". Cada ambiente tem "mais um pacote que integra o React com a forma de construção de interfaces": HTML na web, elementos nativos no mobile.
- **Vantagens:**
  1. *Organização por [[wiki/concepts/componentizacao|componentização]]:* um botão repetido vira componente, e "se eu precisar alterar ele, eu altero apenas em um lugar". O diagrama mostra App, lista de comentários, comentário e formulário.
  2. *Divisão de responsabilidades:* o back-end fica com regras e banco, o front-end com interface, CSS e interação. Ver [[wiki/concepts/separacao-de-responsabilidades]].
  3. *Uma API para vários clientes:* React, React Native, Angular, Vue e "uma API pública".

### Projeto React

- **`npx create-react-app web --template typescript`**: o npx baixa o pacote se ele não estiver na máquina e o executa. A estrutura vem "praticamente pronta"; "uns 2, 3 minutos, vai pegar um café".
- **O que vem:**
  - `public/` com um HTML que tem só uma `div` com id `root`, mais arquivos de PWA.
  - `src/` com o código, `node_modules`, `package.json` e a configuração do TypeScript.
- **`npm start`** abre o navegador. Ele troca o `p` e o `a` de `src/App.tsx` por um `h1` "hello world", e o live reload atualiza "num piscar de olhos". O CSS também funciona: `h1 { color: #7159c1 }`, o roxo.
- Componente, estado e propriedades ficam para quarta-feira.

### React Native e Expo

- **Modelo tradicional:** "nós precisamos criar um aplicativo para iOS e um aplicativo para Android", com o trabalho "repetitivo, tanto para a criação quanto para alterações". Ver [[wiki/concepts/mobile-cross-platform-decision]].
- **React Native:**
  - "Uma única base de código que no final ela funciona tanto para iOS quanto para Android."
  - O código não é convertido para Objective-C, Swift, Java ou Kotlin. Uma dependência, o "JavaScript Core", "adiciona uma thread de processamento de código JavaScript dentro do seu dispositivo". "Ele não é transpilado."
  - "A interface [...] é totalmente nativa", "não é uma interface web", ao contrário de Ionic e PhoneGap. Ver [[wiki/entities/react-native]].
- **Por que o Expo:**
  - Sem ele, é preciso instalar "a SDK do Android, que [...] vem junto com o Android Studio" e o Xcode, os dois "extremamente pesados".
  - Cada recurso nativo (câmera, geolocalização, mapa, sensores) exige procurar "uma biblioteca na internet, de terceiros".
  - Sem Mac, "você não consegue testar no iOS"; "e no Expo a gente já consegue".
  - O app Expo, instalado da App Store ou da Google Play, "já tem a parte do Android e a parte do iOS" e as APIs de "mapa, geolocalização, câmera, sensores, calendário". "Assim a gente pode colocar apenas JavaScript."
  - Limitações e casos de uso ficam para depois. Ver [[wiki/entities/expo]].

### Encerramento

- O "primeiro pilar" é "foco e prática". A citação é de [[wiki/entities/linus-torvalds]], "o criador do Linux e do Git": "talk is cheap, show me the code [...] falar é fácil, mostre-me o código".
- Amanhã, o back-end da API; depois, React, React Native e "recursos avançados".

## Tensões e precisões

- **Duas trilhas, duas arquiteturas.** No [[wiki/sources/nlw-1-dia-4-back-end-node-express-nunjucks-ecoleta|dia 4 de Mayk]], o Ecoleta é renderizado no servidor com Nunjucks, e Mayk chama isso de "full MVC". Aqui Diego usa o mesmo termo ("um sistema full MVC, como eu chamo") para o que *não* vai fazer. O mesmo produto aparece nos dois modelos de [[wiki/concepts/renderizacao-ssr-vs-csr]], o que dá uma boa comparação.
- **REST não é o oposto de MVC.** REST é um estilo de arquitetura (Fielding, 2000), com recursos, interface uniforme e ausência de estado entre requisições `[external]` (https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). Uma API pode continuar organizada em models e controllers; a "view" passa a ser o JSON. E JSON não é exigência do REST, só o formato mais comum. Ver [[wiki/concepts/api-rest]].
- **A faixa "11 a 12" mistura LTS com Current.** As versões ímpares do Node nunca viram LTS, então o 11 não era uma escolha LTS. LTS também não é "à prova de falhas": é a linha que recebe correções de segurança por mais tempo. `[skill: lang-dynamic]` Hoje (novembro de 2026), o Node 26 é Active LTS desde 28/10/2026, o 24 está em Maintenance e o 22 sai de suporte em 30/04/2027.
- **Troca de versão é trabalho de um gerenciador de versões.** Homebrew e Chocolatey instalam uma versão. Para alternar entre projetos, o caminho é nvm, fnm, Volta ou mise, com `.nvmrc` ou `engines` no `package.json`. `[skill: lang-dynamic]` O "resquício" do instalador oficial é exagero; o problema real é a troca de versão.
- **No Linux, não foi snap.** "Node.js Binary Distributions" é o repositório apt da NodeSource, não um pacote snap.
- **`cinst` não existe mais.** O Chocolatey 2.0 removeu os atalhos `cinst`, `cup` e `cuninst`; o comando é `choco install` `[external]` (https://docs.chocolatey.org/en-us/guides/upgrading-to-chocolatey-v2-v6/).
- **O `package-lock.json` não é cache.** É o lockfile: fixa as versões exatas da árvore de dependências e deve ir para o repositório. A wiki já corrigiu o mesmo ponto na versão de Mayk. Ver [[wiki/concepts/package-json]].
- **O TypeScript não acompanha o JavaScript "de forma automática".** O time do TypeScript implementa as propostas do TC39 quando chegam ao estágio 3, e há um intervalo entre uma coisa e outra. "Convertido [...] principalmente quando ele for executar no browser" também não vale para o servidor: desde o Node 22.18 e de forma estável no 24.12, o Node roda `.ts` apagando os tipos (type stripping), sem conversão prévia, desde que o código evite `enum`, decorators e outras sintaxes que geram JavaScript. `[skill: lang-dynamic]` Ver [[wiki/concepts/transpilador]].
- **"10%, 15% dos casos"** é uma estimativa de Diego, sem fonte.
- **`ts-node` e `ts-node-dev` envelheceram.** `[skill: lang-dynamic]` O ts-node está parado na 10.9.2. Para projeto novo, a skill recomenda `tsx watch src/server.ts` (com esbuild, partida de cerca de 100 ms contra 1–3 s), ou o próprio `node --watch src/server.ts` com type stripping, mantendo `tsc --noEmit` no CI para checar os tipos.
- **`localhost 3000 users`.** O servidor ouve na 3333, mas a transcrição diz 3000 ao abrir o navegador. Pode ser deslize de fala ou erro de legenda; foi mantido literal.
- **O Create React App foi descontinuado.** O time do React o encerrou em fevereiro de 2025 e recomenda um framework (Next.js, React Router) ou um build tool como o Vite `[external]` (https://react.dev/blog/2025/02/14/sunsetting-create-react-app).
- **"Tudo dentro do JavaScript" é obra do bundler.** Importar CSS e imagens num arquivo JS não é recurso do React: é o webpack que o CRA configurava (hoje, Vite). O "HTML" que a função retorna é [[wiki/concepts/jsx]], que vira chamadas de função.
- **Os motores do React Native.** O JavaScriptCore era o motor em 2020. Desde o React Native 0.70 o padrão é o Hermes, e a Nova Arquitetura (JSI, sem a bridge assíncrona) é padrão desde a 0.76 `[external]` (https://reactnative.dev/docs/hermes). "Não é transpilado" vale para a linguagem nativa: o JavaScript ainda passa pelo Babel e pelo Metro, e o Hermes compila para bytecode.
- **Expo hoje.** A documentação do React Native recomenda começar por um framework, e o Expo é o indicado `[external]` (https://reactnative.dev/docs/environment-setup). O app Expo Go serve para experimentar; projetos reais usam *development builds*. Testar no iPhone sem Mac funciona, mas gerar e publicar o app de iOS ainda exige macOS ou o build na nuvem (EAS Build).
- **AJAX é anterior ao jQuery.** O termo é de 2005, sobre o `XMLHttpRequest`. O jQuery (2006) só simplificou o uso. Ver [[wiki/concepts/fetch-api]].

## Entidades

- [[wiki/entities/diego-fernandes]]: instrutor
- [[wiki/entities/rocketseat]] e [[wiki/entities/next-level-week]]: o evento e o Ecoleta
- [[wiki/entities/nodejs]]: runtime, LTS, npm e npx
- [[wiki/entities/express]]: micro framework de rotas
- [[wiki/entities/typescript]]: superset tipado
- [[wiki/entities/react]]: interfaces web, SPA e create-react-app
- [[wiki/entities/react-native]]: app mobile nativo com JavaScript
- [[wiki/entities/expo]]: ferramenta e app que encapsulam as SDKs nativas
- [[wiki/entities/vs-code]]: tema Omni, Material Icon Theme, `code .`
- [[wiki/entities/nunjucks]]: citado como template engine do Node
- [[wiki/entities/linus-torvalds]]: "talk is cheap, show me the code"

Citados sem página: Homebrew, Chocolatey, PowerShell, Composer, pip, RubyGems, Laravel/Blade, Handlebars, EJS, jQuery, Whimsical, Dracula, JSON Viewer, Microsoft Edge, Ionic, PhoneGap, Android Studio, Xcode, Angular, Vue, Thiago (designer).

## Conceitos

[[wiki/concepts/api-rest]] · [[wiki/concepts/recurso-rest]] · [[wiki/concepts/json]] · [[wiki/concepts/template-engine]] · [[wiki/concepts/renderizacao-ssr-vs-csr]] · [[wiki/concepts/arquitetura-cliente-servidor]] · [[wiki/concepts/autenticacao-e-autorizacao]] · [[wiki/concepts/sistema-de-tipos]] · [[wiki/concepts/arquivo-de-declaracao-de-tipos]] · [[wiki/concepts/transpilador]] · [[wiki/concepts/package-json]] · [[wiki/concepts/gerenciador-de-pacotes]] · [[wiki/concepts/single-page-application]] · [[wiki/concepts/componentizacao]] · [[wiki/concepts/separacao-de-responsabilidades]] · [[wiki/concepts/jsx]] · [[wiki/concepts/mobile-cross-platform-decision]] · [[wiki/concepts/mobile-deep-links]]

## Open Questions

- Os dias 2 a 5 desta trilha (API completa, React, React Native, recursos avançados) ainda não estão na wiki. O dia 2 (API com Knex e SQLite) está em [[wiki/sources/nlw-1-diego-fernandes-dia-2-back-end-express-knex-sqlite-ecoleta]].
- O nome oficial das trilhas da NLW #1 (a de Mayk e a de Diego) não aparece nas transcrições `[external, não verificado]`.
- Data provável: 1º de junho de 2020, segunda-feira da semana do meio ambiente `[external, não verificado]`.
- A transcrição tem repetições por sobreposição da legenda ("Agora que a gente já entendeu os princip Bora lá!", "se ele não retornar Restricted..."), mantidas como estão.
