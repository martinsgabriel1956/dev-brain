---
type: source
title: "Comandos Básicos de Linux que Todo Dev Precisa Conhecer (Augusto Galego)"
aliases: ["comandos básicos de linux galego", "comandos linux todo dev", "linux basics galego"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_count: 0
tags: [tech-mentor-infra, linux, shell, terminal, comandos-linux, permissoes-unix, variaveis-de-ambiente, pipe-operator, grep, sed, harness, ssh, augusto-galego]
skill: tech-mentor-infra
status: stable
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/comandos-basicos-linux-todo-dev-precisa-conhecer-galego.md
source_url:
author: Augusto Galego
date_published:
date_ingested: 2026-08-11
---

# Comandos Básicos de Linux que Todo Dev Precisa Conhecer (Augusto Galego)

## TL;DR

Vídeo introdutório de [[wiki/entities/augusto-galego]] cobrindo os comandos de shell que todo dev precisa reconhecer (não decorar). A tese pedagógica central e diferenciada: **você precisa conhecer esses comandos porque é assim que as IAs manipulam o seu computador** — quando um [[wiki/entities/claude-code|Claude Code]] roda dentro do seu [[wiki/concepts/linux]]/macOS, a [[wiki/concepts/harness|harness]] executa `cd`, `mkdir`, `cat`, `grep`, `sed` nativos, lê o output e o envia como parte do prompt ao servidor da [[wiki/entities/anthropic|Anthropic]]. Segundo motivo: ~90% dos servidores rodam Linux/Unix, e para operá-los (via [[wiki/concepts/ssh|SSH]] ou em pipelines de [[wiki/concepts/ci-cd|CI/CD]]) você usa esses comandos. Cobre: [[wiki/concepts/shell-terminal|terminal]], navegação (`pwd`/`ls`/`cd`/`mkdir -p`), leitura/escrita sem editor (`touch`/`echo >`/`echo >>`/`cat`), cópia/movimentação (`cp`/`mv`), remoção (`rm -rf` com aviso), [[wiki/concepts/variaveis-de-ambiente|variáveis de ambiente]] (`.env`/`export`/`.zshrc`), [[wiki/concepts/permissoes-unix|permissões]] (`chmod +x`/`sudo`), busca ([[wiki/concepts/codigo-grepavel|grep]] `-i`/`-n`/`-r`), [[wiki/concepts/pipe-operator|pipe operator]] (`|`) e substituição de texto (`sed`). Patrocínio da [[wiki/entities/abacus-ai|Abacus]].

## Key Claims

1. **As IAs manipulam o computador via comandos nativos** — o Claude Code não abre um editor gráfico; ele lê/escreve/busca arquivos rodando `cat`, `echo`, `grep`, `sed` etc. na máquina do usuário. "Isso é o puro suco da harness e do tool calling das LLMs." Ver [[wiki/concepts/harness]] e [[wiki/concepts/tool-call]].
2. **Fluxo do `cat` como leitura de arquivo pela LLM** — a harness dá `cat arquivo.md`, pega o output e faz uma requisição ao servidor da [[wiki/entities/anthropic|Anthropic]] com aquele conteúdo como parte do prompt. Reforça o modelo já documentado: **a LLM orquestra, a harness executa** na máquina real do usuário.
3. **~90% dos servidores do mundo rodam Linux/Unix** — por isso conhecer os comandos importa para SSH e pipelines de CI/CD. `[external, número aproximado citado pelo autor]`
4. **Não é preciso decorar** — o próprio autor não decora; revisou/testou antes e improvisou parte. A meta é *reconhecer* um `grep`/`sed`/`echo` numa pipeline e saber o que está acontecendo.
5. **`pwd`** imprime o working directory; **`ls`** lista; **`ls -l`** detalha (tipo `d`/`-`, permissões `rwx`, dono).
6. **Arquivos com ponto inicial são ocultos** — `.DS_Store` (Mac), `.env`, `.git`. Não aparecem no explorador por padrão.
7. **`mkdir -p a/b/c`** cria diretórios-pai e aninhados de uma vez; sem `-p`, falha se a pasta-pai não existe.
8. **`echo texto > arquivo` sobrescreve; `echo texto >> arquivo` faz append** — a distinção entre um `>` e dois `>>`.
9. **`cp` copia, `mv` move** — depois de `mv`, o arquivo some da origem.
10. **`rm` não remove diretório; `rm -rf` sim** — recursivo + force, **sem pedir confirmação**. Aviso explícito: rodar em pasta core do sistema quebra tudo rápido.
11. **`git init` cria a pasta oculta `.git`** — onde o Git guarda branch atual, arquivos staged etc. Deletar `.git` obriga a reconfigurar o repositório. Ver [[wiki/concepts/git]].
12. **`export VAR=valor`** define variável de ambiente na instância do terminal; configurações persistentes ficam em `.zshrc`/`.bashrc`; `echo $VAR` imprime o valor. Ver [[wiki/concepts/variaveis-de-ambiente]].
13. **`chmod +x` resolve "permissão negada" ao executar script** — arquivo pode ter `r`/`w` mas faltar `x`. É a origem daquele "dá um chmod que resolve" da IA/Stack Overflow. Ver [[wiki/concepts/permissoes-unix]].
14. **`sudo` roda como super user/admin** — permite forçar operações sem permissão; pede senha; usar com cuidado.
15. **`grep` para achar código** — `grep -i` (case insensitive), `grep -n` (número da linha), `grep -r` (recursivo por pastas). É assim que a LLM acha utilizações de função num arquivo grande. Ver [[wiki/concepts/codigo-grepavel]].
16. **Pipe operator `|`** encadeia comandos: output de um vira input do próximo (`cat arquivo | grep termo`). Ver [[wiki/concepts/pipe-operator]].
17. **`sed 's/A/B/'`** substitui texto — reconhecidamente rebuscado (escapar caracteres), o autor sempre pesquisa a sintaxe.
18. **Via SSH em produção você opera por comandos** — interface gráfica geralmente inexiste ou é travada; devs experientes preferem o terminal. Ver [[wiki/concepts/ssh]].

## Entidades Mencionadas

- [[wiki/entities/augusto-galego]] — autor; PWD do vídeo identifica o user "Augusto Galego"; ambiente demonstrado em macOS (usa `.DS_Store`, Finder).
- [[wiki/entities/anthropic]] — servidor para onde a harness do Claude Code envia o conteúdo lido via `cat`.
- [[wiki/entities/claude-code]] — exemplo canônico de harness que manipula arquivos por comandos nativos.
- [[wiki/entities/abacus-ai]] — patrocinador; agregador de múltiplas IAs (GPT 5.5, Claude Opus 4.8, Fable 5) numa subscription única.

## Conceitos Tocados

- [[wiki/concepts/comandos-basicos-linux]] (novo)
- [[wiki/concepts/shell-terminal]] (novo)
- [[wiki/concepts/permissoes-unix]] (novo)
- [[wiki/concepts/variaveis-de-ambiente]] (novo)
- [[wiki/concepts/pipe-operator]] (novo)
- [[wiki/concepts/linux]] · [[wiki/concepts/unix]]
- [[wiki/concepts/harness]] · [[wiki/concepts/tool-call]]
- [[wiki/concepts/codigo-grepavel]] · [[wiki/concepts/ssh]]

## Open Questions

- **Número dos ~90% de servidores Linux** — citado de improviso pelo autor, sem fonte; ordem de grandeza plausível mas não verificada aqui. `[external]`
- **Precisão dos nomes de modelo do bloco de patrocínio** (GPT 5.5, Claude Opus 4.8, Fable 5, $10/mês) — vindos de material publicitário, tratados como demonstração comercial, não como benchmark.

## Raw Quotes

- "É assim que as IAs estão manipulando o seu computador."
- "O Cloud Code manipula o arquivo via comandos."
- "Isso aqui é o puro suco da harness. A harness está fazendo isso o tempo todo."
- "Você não precisa decorar tudo isso... o importante é: quando eu leio numa pipeline um `sed`, um `grep`, um `echo`, eu sei o que está acontecendo."
- "Cuidado com `rm -rf` — ele deleta recursivamente e não vai pedir permissão nenhuma."
