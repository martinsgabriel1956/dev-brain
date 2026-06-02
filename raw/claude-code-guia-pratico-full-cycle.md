# Claude Code — Guia Prático: Instalação, MCP, Hooks e Produtividade

> Transcrição e comentários do vídeo do canal Full Cycle
> Tema: Claude Code (CLI da Anthropic) — como instalar, configurar e trabalhar no dia a dia

---

## O que é o Claude Code

Claude Code é um **agente de desenvolvimento de software criado pela Anthropic** que funciona como CLI (Command Line Interface). Diferente de IDEs como Cursor ou Windsurf, ele roda no terminal — mas existe integração que o conecta a qualquer IDE baseada em VS Code.

O autor usa Claude Code em conjunto com Cursor, Windsurf, VS Code e GitHub Copilot. A chave é usar **a ferramenta certa no momento certo**.

---

## Planos e Preços — Armadilha dos $500

> Atenção: esse é o ponto onde mais pessoas cometem erros caros.

Na hora de fazer login, o Claude Code oferece duas opções:

1. **API Key da Anthropic** — cobra por token, pode sair muito caro (o autor conheceu alguém que gastou $500 sem perceber)
2. **Claude Account with Subscription** — plano fixo mensal, muito mais econômico para uso intenso

### Planos disponíveis (referência da gravação)

| Plano | Preço/mês | Limites |
|-------|-----------|---------|
| Free | $0 | Muito limitado |
| Pro | ~$20 | Rate limiting relativamente rápido |
| Max | $100 | 5x mais uso que o Pro; acesso ao Opus |
| Max | $200 | 20x mais uso que o Pro |

**Recomendação:** se for usar com frequência, assine o plano Max ($100). O plano Pro serve para uso ocasional. Nunca use API Key diretamente sem entender o custo por token.

---

## Instalação

```bash
npm install -g @anthropic-ai/claude-code
claude                  # abre dentro do diretório do projeto
```

No primeiro uso, será solicitado login — escolha **"Claude account with subscription"**.

---

## Integração com IDE (VS Code / Cursor)

Apesar de ser CLI, o Claude Code integra com qualquer IDE baseada em VS Code:

1. Abra a aba de extensões e busque por **"Claude Code"**
2. Instale a extensão
3. Um botão **"Run Claude Code"** aparecerá na interface
4. Clique para abrir o painel ao lado do editor (funciona como o painel do Cursor/Copilot)

### Conectar à IDE pelo terminal

```
/ide
```

Isso detecta as IDEs abertas e conecta o Claude Code ao projeto atual. Após a conexão aparece: `IDE connected`.

---

## CLAUDE.md — Memória e Regras do Projeto

O Claude Code usa um arquivo `CLAUDE.md` na raiz do projeto para armazenar regras, contexto e instruções que ele deve sempre seguir — equivalente ao `cursor rules`.

### Gerar automaticamente com /init

```
/init
```

O Claude analisa todo o codebase (README, estrutura, código) e gera um `CLAUDE.md` automaticamente com:
- Comandos para rodar o projeto
- Arquitetura geral
- Estrutura de diretórios
- Notas de desenvolvimento

Você pode customizar o `/init` passando instruções adicionais:

```
/init — inicialize lendo todo o projeto, mas ignore a pasta mcp-sdk-repo
```

---

## Sistema de Memória

O Claude Code tem dois níveis de memória:

| Tipo | Escopo | Arquivo |
|------|--------|---------|
| Project Memory | Só para este projeto | `CLAUDE.md` na raiz |
| User Memory | Global (todos os projetos) | `CLAUDE.md` na pasta do usuário |

### Editar memória

```
/memory
```

Isso abre o arquivo de memória relevante. Para adicionar uma regra, use `#` na frente:

```
# nunca use emojis no projeto, nem em logs ou outputs
```

O Claude confirma e salva. A regra entra no `CLAUDE.md` e vale para todas as sessões futuras.

---

## Servidores MCP

O Claude Code suporta **servidores MCP (Model Context Protocol)** — ferramentas externas que expandem as capacidades do agente (ex: acesso ao Docker, bancos de dados, APIs).

### Gerenciar MCPs pelo CLI

```bash
claude mcp --help          # ajuda
claude mcp list            # listar servidores configurados
claude mcp remove <nome>   # remover servidor
claude mcp add <nome> <comando>   # adicionar servidor
```

**Exemplo — adicionar MCP do Docker:**
```bash
claude mcp add mcp-docker docker mcp gateway run
```

### Verificar MCPs dentro do Claude Code

```
/mcp
```

Lista os servidores conectados e status.

### Configuração Global vs Local

A configuração de MCPs fica nos arquivos de settings (ver seção abaixo).

---

## Arquivos de Configuração — settings.json

O Claude Code cria uma pasta `.claude/` com arquivos de configuração:

| Arquivo | Escopo | Commitar? |
|---------|--------|-----------|
| `settings.json` | Projeto (compartilhado com o time) | ✅ Sim |
| `settings.local.json` | Projeto (só para você) | ❌ Não |
| `~/.claude/settings.json` | Global (todos os projetos) | — |

**Regra:** tudo que é pessoal (permissões, MCPs locais) vai no `settings.local.json`. O que deve ser compartilhado com o time vai no `settings.json`.

### Exemplo de settings.local.json

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run build:*)",
      "Bash(npm run *)",
      "mcp__mcp-docker__*"
    ]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [{ "type": "command", "command": "echo hello world" }]
      }
    ]
  }
}
```

---

## Sistema de Permissões

Por padrão, o Claude Code pede confirmação para cada ação (editar arquivos, rodar comandos). Você pode conceder permissões permanentes:

- **Só dessa vez** — aprova uma execução única
- **Sim, e não pergunte nessa sessão** — aprova para a sessão atual
- **Sempre permitir** — salva no `settings.local.json`

### Ver e gerenciar permissões

```
/permissions
```

Exemplo de permissões comuns no settings:
```json
"allow": [
  "Bash(npm run build)",
  "Bash(npm run *)",
  "Bash(pkill *)"
]
```

---

## Modos de Operação — Auto-accept vs Plan Mode

Ao pressionar **Shift+Tab**, você alterna entre:

| Modo | Comportamento |
|------|---------------|
| Auto-accept edits | Aplica mudanças automaticamente sem pedir confirmação |
| Plan Mode | Gera apenas um plano de ação para você revisar antes de executar |

**Recomendação de workflow:**

1. Ative o **Plan Mode**
2. Descreva a tarefa (mesmo com prompt ruim)
3. Discuta e refine o plano com o Claude
4. Quando o plano estiver bom, aceite para execução

Isso evita que ele saia fazendo alterações prematuras antes de você alinhar a direção.

---

## Commands — Scripts em Markdown

Um dos recursos mais poderosos: criar **comandos customizados** em arquivos `.md` dentro de `.claude/commands/`.

### Como criar

1. Crie a pasta `.claude/commands/`
2. Crie um arquivo `.md` (ex: `exec-prompt.md`)
3. A primeira linha do arquivo vira a descrição do comando

### Exemplo: exec-prompt.md

```markdown
# Execução de tarefa

Siga as instruções do prompt passado entre as tags <instruções> para executar as tarefas informadas como $ARGUMENTS.

<instruções>
## Estratégia de execução

1. Alto nível: compreender o problema
2. Investigar o codebase existente
3. Desenvolver um plano detalhado
4. Implementar
5. Testar

...demais instruções do seu prompt padrão...
</instruções>
```

### Como usar

```
/exec-prompt remover usuários do servidor MCP passando uma lista de e-mails
```

O Claude executa o arquivo `.md` como se fosse um script — substituindo `$ARGUMENTS` pelo texto que você passou.

**Casos de uso:**
- `/exec-prompt <tarefa>` — executa com seu workflow padrão de desenvolvimento
- `/security-check` — roda auditoria de segurança com suas regras
- `/create-commit` — gera commits no padrão que você quer
- `/review-pr` — faz code review seguindo suas diretrizes

---

## Hooks — Automação Garantida

Diferente do `CLAUDE.md` (que é uma *guideline* que o modelo pode ignorar), os **hooks executam comandos reais** em eventos específicos.

### Eventos disponíveis

| Evento | Quando dispara |
|--------|----------------|
| `PreToolUse` | Antes de executar qualquer ferramenta |
| `PostToolUse` | Após executar qualquer ferramenta |
| `UserPromptSubmit` | Quando você envia uma mensagem |
| `Stop` | Quando o agente termina a tarefa |
| `SubagentStop` | Quando um subagente termina |

### Matchers

Dentro de cada evento, você define um **matcher** para filtrar quando o hook dispara:

- `Write` — quando escreve um arquivo
- `Edit` — quando edita um arquivo
- `Bash` — quando executa um comando shell
- `Task` — quando uma tarefa (subagente) é finalizada
- `WebFetch` — quando acessa a web

### Criar um hook

```
/hooks
```

O assistente pergunta:
1. Qual evento?
2. Qual matcher?
3. Qual comando executar?
4. Salvar em local, project ou user settings?

### Exemplo prático

Hook que roda os testes sempre que o Claude termina uma tarefa:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Task",
        "hooks": [
          {
            "type": "command",
            "command": "npm test -- --watchAll=false"
          }
        ]
      }
    ]
  }
}
```

Se os testes falharem (exit code != 0), o Claude lê o output e continua trabalhando para corrigir o erro.

### Códigos de retorno

| Exit code | Significado |
|-----------|-------------|
| `0` | Sucesso |
| `2` | Erro — o Claude lê o output e tenta corrigir |

---

## Janela de Contexto e Compactação

O Claude Code tem uma janela de contexto de ~200.000 tokens. Conforme a sessão avança:

1. O indicador mostra a % da janela utilizada
2. Quando fica cheia, o Claude faz **compactação automática**: resume o histórico e limpa o contexto
3. Após compactação, o contexto não é idêntico ao original — podem ocorrer perdas sutis

### Compactação manual

```
/compact
```

Gera um resumo do histórico e limpa o contexto atual.

### Boas práticas

- **Termine a sessão ao terminar uma tarefa** — abra uma nova sessão para a próxima tarefa
- **Mantenha `CLAUDE.md` atualizado** — é o contexto que persiste entre sessões
- **Use design docs e planos de ação em arquivos** — não dependa do histórico da conversa
- Pense como se cada sessão fosse um novo Claude sem memória — tudo relevante deve estar nos arquivos

---

## Problema Comum: npm start Travando o Terminal

Quando o Claude executa `npm start` ou qualquer processo que não termina, o terminal trava e ele para de funcionar.

**Solução:** diga para ele rodar em background:

```
"quando rodar npm start, use & no final para não travar o terminal"
```

Ou adicione no `CLAUDE.md`:

```markdown
## Comandos de servidor
Sempre use `&` ao iniciar servidores para não bloquear o terminal.
```

---

## Resumo dos Comandos Principais

| Comando | O que faz |
|---------|-----------|
| `/init` | Gera CLAUDE.md analisando o codebase |
| `/memory` | Edita a memória (CLAUDE.md) do projeto ou usuário |
| `/ide` | Conecta ao IDE aberta (VS Code, Cursor, etc) |
| `/mcp` | Lista servidores MCP conectados |
| `/hooks` | Gerencia hooks de eventos |
| `/permissions` | Visualiza permissões configuradas |
| `/compact` | Compacta o histórico para liberar contexto |
| `Shift+Tab` | Alterna entre Auto-accept e Plan Mode |
| `/<nome>` | Executa um comando customizado de `.claude/commands/` |
| `Esc` | Para a execução atual |

---

## Tags

`claude-code` `anthropic` `cli` `agente-ia` `mcp` `hooks` `prompt-engineering` `ide-integration` `produtividade-dev` `configuracao` `context-window` `plan-mode`
