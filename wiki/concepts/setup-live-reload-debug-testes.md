---
type: concept
title: "Setup de Live Reload, Debug e Testes Integrados"
aliases: ["live reload node", "node --watch --inspect", "launch.json debug testes", "ambiente de desenvolvimento produtivo"]
date_created: 2026-07-21
date_updated: 2026-11-17
source_count: 11
tags: [testes, debugging, node-js, produtividade, vscode, ferramental]
skill: tech-mentor-testing
status: draft
---

# Setup de Live Reload, Debug e Testes Integrados

Prática de investir as primeiras horas de um projeto (novo ou legado) configurando três camadas de ferramental que, juntas, eliminam o ciclo lento e manual de validação: alterar código → reiniciar servidor manualmente → `console.log` → verificar em ferramenta externa → repetir.

## As três camadas

### 1. Live reload
Reinicia o processo automaticamente a cada alteração salva, sem intervenção manual no terminal.
- Node.js: flag `--watch` (`node --watch service.js`)
- Web/navegador: Browser Sync

### 2. Modo de depuração
Abre uma porta de debug que o editor pode conectar, permitindo breakpoints direto no código sem sair do ambiente de desenvolvimento.
- Node.js: flag `--inspect`

### 3. Testes automatizados integrados ao ciclo de save
Combina as duas camadas anteriores com o test runner: a cada `Ctrl+S`, os testes rodam automaticamente, o debugger já está conectado, e é possível colocar um breakpoint dentro do teste ou do código de produção.
```json
"test:debug": "node --inspect --watch --test test/"
```

## `launch.json` como cola entre editor e `package.json`

A peça final é apontar o debugger do editor (ex.: VS Code) para o **script do `package.json`**, não direto para o binário do Node.js — isso garante que qualquer pessoa do time rode exatamente o mesmo comando subjacente, independente de qual editor usa:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "launch",
      "name": "Run test debugger",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["run", "test:debug"],
      "skipFiles": ["<node_internals>/**"],
      "console": "integratedTerminal"
    }
  ]
}
```

- `skipFiles` esconde código interno do Node.js ao inspecionar/steppar.
- `console: "integratedTerminal"` mantém a saída dentro do próprio editor, em vez de abrir terminais novos a cada execução.

## Coverage e debug não combinam bem (observação prática)

Ao combinar `--experimental-test-coverage` com `--inspect` no mesmo script, o coverage simplesmente não aparecia — comportamento observado ao vivo, não documentado oficialmente. Solução prática: manter coverage só no script de teste "normal" (sem debug) e usar o script de debug apenas para testes + breakpoints.

## Debug Console como REPL contra o estado real

Com o debugger conectado, o "Debug Console" do editor permite executar expressões arbitrárias contra as variáveis reais em memória (ex.: `user.email.replace(/\W/g, '-')`) sem alterar o valor original, ou atribuir um novo valor a uma variável para simular um cenário diferente e continuar a execução a partir dali — sem precisar reiniciar o processo nem sair do editor.

## Por que isso é um pilar, não um detalhe

O ganho não é conveniência marginal — é eliminar a necessidade de sair do ambiente de desenvolvimento para validar qualquer hipótese. Ver [[wiki/concepts/debugging]] para o processo de investigação em si, e [[wiki/concepts/tdd]] para o ciclo RED-GREEN-REFACTOR que esse setup viabiliza em velocidade de `Ctrl+S`.

## Modo watch como terceiro estágio de maturidade (Jest)

[[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] descreve o mesmo padrão com Jest em vez de `node --test`: tela dividida entre teste e runner em modo watch, onde qualquer alteração salva reroda o teste automaticamente. A fonte enquadra esse setup como o terceiro (e mais maduro) estágio de uma progressão pessoal — antes dele vêm testar clicando manualmente na interface, e depois testar via cliente HTTP dedicado (Postman). Ver [[wiki/concepts/tres-estagios-maturidade-testes]] para a progressão completa. O ganho demonstrado ali vai além do feedback rápido: o mesmo teste que expõe um bug de autorização (rota retornando `200` em vez de `403` para usuário anônimo) continua rodando em modo watch meses depois, pegando uma regressão futura completamente não relacionada assim que ela é introduzida.

## Live Server no front-end estático

Em [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]], a extensão Live Server do [[wiki/entities/vs-code]] faz o papel do live reload para HTML e CSS: "inicializei um servidor" e cada Ctrl+S aparece no navegador. Equivale ao Browser Sync citado acima.

## Na NLW #1 (Mayk Brito)

Em [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]], [[wiki/entities/mayk-brito|Mayk Brito]] usa a extensão Live Server do VS Code: botão direito em `index.html` → Open with Live Server, e "sempre que eu salvar, o Live Server vai atualizar a página". Avisa que a bolinha na aba é arquivo não salvo, "um dos motivos da gente às vezes não conseguir acompanhar a aula".

## Live Server na aula de ambiente do FrontPUSH

Em [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]], [[wiki/entities/nasser|Násser]] pede "por favor, instale" o Live Server por dois motivos: sobe um "servidorzinho", porque "tem alguns recursos que só funcionam quando são rodados em servidor" (diferente de abrir o HTML com dois cliques), e faz *auto reloading* a cada Ctrl+S. `[external]` Exemplos do que falha em `file://`: módulos ES e `fetch` de arquivos locais (https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy#file_origins).

## Na NLW #2, dia 1 (Mayk Brito)

Em [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]], o Live Server "criou um servidor pra gente" em `127.0.0.1:5500` e atualiza a página ao salvar. A regra de [[wiki/entities/mayk-brito|Mayk]]: "Nunca mais eu vou dar dois cliques nesse arquivo para abrir ele". Antes disso, ele ensina o hard reload (Ctrl+Shift+R) para fugir do cache.

## Live Server no módulo de Sass (FrontPUSH)

Em [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]], [[wiki/entities/nasser|Násser]] mostra o "Open with Live Server" na porta 5500 como recurso do [[wiki/entities/live-sass-compiler]]: "quando você salva, ele automaticamente modifica e atualiza o seu browser". Na versão original da extensão, o Live Server era dependência; são duas extensões. O Watch Sass completa o ciclo: salvar o `.scss` compila, e o recarregamento mostra o resultado.

## Node sem reload (JStack, aula 04)

Em [[wiki/sources/jstack-criando-o-servidor-http]], alterar o código com o servidor rodando não muda nada até Ctrl+C e rodar de novo; o nodemon automatiza isso, mas fica de fora para mostrar "o node raiz". O `node --watch` (estável desde Node 22.0/20.13) faz o mesmo sem pacote `[skill: lang-dynamic]`.

## Key Sources

- [[wiki/sources/3-pilares-testes-automatizados-produtividade]]
- [[wiki/sources/os-3-estagios-de-maturidade-para-testar-codigo]] — modo watch com Jest como terceiro estágio de maturidade; teste como rede de segurança contra regressão
- [[wiki/sources/basico-css-o-que-e-sintaxe-inline-incorporado-externo]] — Live Server como live reload de HTML/CSS
- [[wiki/sources/nlw-1-dia-1-programacao-web-html-css-ecoleta]]: Live Server e arquivo não salvo
- [[wiki/sources/frontpush-configurando-o-ambiente-git-node-yarn-vs-code-extensoes]]: Live Server: servidor local e auto reloading
- [[wiki/sources/frontpush-o-que-e-html-linguagem-de-marcacao-tags-semantica]]: Open With Live Server cria "um servidorzinho com essa página"
- [[wiki/sources/nlw-2-dia-1-programacao-web-html-css-proffy]]: NLW #2, dia 1: Live Server e hard reload
- [[wiki/sources/frontpush-instalacao-sass-live-sass-compiler-scout-app]]: Live Server + Watch Sass
- [[wiki/sources/jstack-criando-o-servidor-http]]: reinício manual, nodemon e node --watch
- [[wiki/sources/frontpush-conceitos-gerais-react-interface-dinamica-spa-virtual-dom-jsx]]: FrontPUSH, React aula 03: a página "carregue automaticamente quando percebe [...] mudança", atribuído a Babel e Webpack
- [[wiki/sources/frontpush-jsx-webpack-babel-react-createelement-create-react-app]]: FrontPUSH, React aula 06: Live Reload como função do Webpack (dev server); Fast Refresh no CRA 4+
