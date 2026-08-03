# Git Worktree para Paralelismo com Agentes de IA (Codex, Claude Code, Abacus.AI)

Transcrição de vídeo/short em português, transcrito automaticamente por voz-para-texto. O texto abaixo foi reorganizado em seções e teve a pontuação corrigida para legibilidade, **sem adicionar conteúdo que não estivesse implícito na fala** — trechos que permaneceram ambíguos mesmo após reconstrução estão marcados como `[transcrição incerta]`. Não foi necessária tradução: a fonte já está em português.

## Introdução: o que é uma worktree

O autor introduz o tema dizendo nunca ter usado `git worktree` até recentemente, quando a feature passou a ser muito relevante para o trabalho com IA. Ele promete explicar o que é uma worktree no Git (corrigindo-se: não é uma feature do GitHub, é do Git), por que considera importante conhecê-la e usá-la ao programar com IA, e como usá-la no Codex e no Claude Code.

## Bloco patrocinado: Abacus.AI e o recurso "Multi-Engine Agent Farm"

O vídeo é patrocinado pela Abacus.AI. O autor apresenta uma feature nova chamada **multiengine agent farm** (ou "agent farm"): ao pedir, dentro do Abacus, a criação de uma feature — principalmente usando o "ZP Agent" da Abacus — essa feature cria algo complexo, entregando o workflow de um "agent farm": vários agentes trabalhando em conjunto para subir um projeto do zero. Segundo o autor, isso funciona muito bem para montar projetos complexos rapidamente. O exemplo mostrado na tela é um SaaS de RH (HR).

A Abacus.AI é descrita como um ferramental que permite usar diversos modelos de IA num único chat: o autor cita o Nano Banana 2, o "ChatGPT 5.4" `[transcrição incerta sobre o número exato da versão]` e o Claude Opus 4.7. Além do chat com múltiplos modelos e do Agent Farm, a Abacus também oferece uma CLI própria, comparável ao Codex ou ao Claude Code (ver seção de demonstração abaixo). O autor menciona um link de desconto na descrição do vídeo original e o preço de assinatura mensal (valor exato não recuperável da transcrição).

## Por que ninguém usava worktree antes

O autor contextualiza dizendo, de forma irônica, que está falando dos "primórdios da computação" (2024/2025) — quando ele nunca tinha usado worktree porque seu modelo de trabalho era sequencial: uma branch por vez, terminar, comitar, subir pro remoto, trocar de branch. Nesse modelo, branches comuns já resolvem bem o problema, porque o desenvolvedor nunca está escrevendo código em duas branches ao mesmo tempo.

O problema de trocar de branch no Git tradicional: se há arquivos alterados e não commitados, é preciso ou dar `stash` neles, ou comitar, ou descartar as mudanças antes de trocar de branch — o que é incômodo quando se quer alternar rapidamente entre duas linhas de trabalho.

## O que uma worktree realmente faz

Na prática, uma worktree mantém um único repositório com um único histórico, mas separa o trabalho em múltiplas pastas, de modo que o trabalho numa branch não afeta o trabalho na outra. É como ter, na prática (embora tecnicamente não seja isso), dois clones do mesmo repositório — permitindo trabalhar em paralelo.

## Por que isso importa na era da IA

O autor argumenta que, cada vez mais, o trabalho do desenvolvedor é manter contexto na cabeça, manter documentação concisa do que precisa ser feito, e usar bem o tempo para fazer coisas em paralelo — porque, se não for possível paralelizar, perde-se parte do ganho de produtividade que a IA promete. Usando worktrees, uma instância do harness de IA (Codex, Claude Code, Abacus) pode trabalhar numa branch enquanto outra instância trabalha em outra branch, sem confundir sessões ou contexto.

## Demonstração prática: criando worktrees no terminal

1. O autor está dentro de um repositório (`ls` mostra os arquivos, incluindo um Dockerfile). `git status` confirma a branch atual (`main`).
2. Cria duas worktrees para duas features diferentes: `git worktree add ../feature-a -b feature-a` (baseada na `main`) e o mesmo para `feature-2`. Nota-se o uso de `../` para criar as pastas um nível acima do repositório atual — recomendação simples para manter as worktrees fora do próprio repo (alternativa: uma pasta ignorada pelo Git dentro do próprio repositório, abordagem mais próxima do que o Claude Code faz nativamente).
3. As pastas novas não aparecem dentro do repositório original (`ls` não mostra), mas `cd ../feature-a` leva à nova pasta, que contém uma cópia completa dos arquivos do repositório.
4. `git worktree list` lista todas as worktrees ativas — no exemplo, três pastas: uma na `main`, uma na `feature-1`/`feature-a` `[transcrição incerta sobre o nome exato]`, uma na `feature-2`.

## Usando a CLI da Abacus.AI dentro de uma worktree

Dentro da pasta da worktree (`feature-a`), o autor roda o comando da CLI da Abacus (`abacus` / `abac`, nome exato incerto na transcrição) e já consegue programar normalmente ali. Para trabalhar em outra feature, basta abrir outra janela/instância de terminal, navegar até a pasta da outra worktree (`feature-2`) e trabalhar por lá.

## Codex: CLI vs. app nativo

Com a CLI do Codex, o fluxo é o mesmo: rodar `codex` dentro da pasta da worktree já é suficiente. Mas o **aplicativo** do Codex tem suporte nativo a worktrees: ao trabalhar localmente ("work locally"), há opções como "new worktree" ou, no painel do projeto, "create permanent worktree", que cria uma worktree permanente.

O autor testa isso ao vivo (usando o modelo "Spark" por ser rápido) pedindo uma alteração simples ao Codex. Rodando `git worktree list` depois, aparece uma entrada com "head detached". O Codex cria sua worktree dentro da pasta `.codex` do próprio repositório — diferente do exemplo manual anterior, que criava as pastas um nível acima.

## Claude Code: `claude --worktree`

O Claude Code também pode ser usado com worktrees criadas manualmente via `git worktree add`, sem problema algum. Mas ele oferece um facilitador mais nativo: o comando `claude --worktree <nome>`. No exemplo, o autor roda `claude --worktree feature-3`, e o Claude cria a worktree dentro do repositório, em `.claude/worktrees/feature-3`.

O autor autoriza as mudanças pedidas ("sim, eu permito") e, ao rodar `/quit` no Claude Code, a ferramenta pergunta se ele quer manter a worktree — ele escolhe manter, para poder mostrar a listagem depois.

## Comparando onde cada ferramenta guarda suas worktrees

Ao rodar `git worktree list` novamente, o autor mostra a pasta original do repositório, a worktree do Codex (fora da pasta, "escondida" em outro lugar do computador — não dentro da pasta `.codex` como o autor havia dito antes; ele se corrige ao vivo `[transcrição incerta sobre o local exato]`), a worktree do Claude Code (dentro de `.claude/worktrees/`), e as worktrees `feature-a`/`feature-2` criadas manualmente antes.

## Removendo worktrees

Fluxo típico: dentro de cada worktree, comitar o código na branch; quando não for mais necessário trabalhar nela, remover com `git worktree remove <caminho>`. O Git avisa se há mudanças não commitadas e pergunta (ou recusa) a remoção nesse caso — usar `git worktree remove -f <caminho>` força a remoção mesmo com mudanças pendentes. O autor demonstra removendo a worktree do Claude Code (`git worktree remove -f .claude/worktrees/feature-3`, corrigindo um erro de caminho ao vivo) e a do Codex, depois roda `git worktree list` de novo para confirmar que só restaram as worktrees remanescentes.

## Conclusão e aviso final

O autor encerra dizendo que essa é uma feature do Git com talvez uns 20 anos de existência, que ele nunca tinha usado porque nunca tinha sido relevante trabalhar em paralelo — e que agora usa porque consegue simultaneamente fazer três bug fixes simples em branches diferentes mais uma feature numa quarta branch. Ele conclui com um aviso: essa capacidade de gerar mais código em paralelo também é capacidade de gerar mais "gambiarra" mais rápido — por isso é importante prestar atenção no que está sendo entregue à IA (documentação boa, regras de negócio bem definidas), para que a IA realmente adira a essas regras. "Garbage in, garbage out."
