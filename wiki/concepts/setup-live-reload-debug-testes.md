---
type: concept
title: "Setup de Live Reload, Debug e Testes Integrados"
aliases: ["live reload node", "node --watch --inspect", "launch.json debug testes", "ambiente de desenvolvimento produtivo"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
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

## Key Sources

- [[wiki/sources/3-pilares-testes-automatizados-produtividade]]
