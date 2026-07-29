# Git Rebase na Prática

> Transcrição de vídeo em português sobre o comando `git rebase` — patrocinado pela Alura. Reestruturada em markdown com seções; conteúdo já em português, sem necessidade de tradução. Transcrição original bastante coloquial/informal, adaptada aqui para clareza mantendo o conteúdo técnico integral.

## Introdução — Por Que Aprender Git é Essencial

Se você perguntar para qualquer desenvolvedor de software se é necessário aprender a usar o Git, provavelmente 99,9% vai dizer que sim, que é essencial. Não importa qual tecnologia, framework ou linguagem você trabalha, se você está sozinho ou em um time com um projeto de software, usar o Git para versionamento é tão importante quanto para um cozinheiro saber acender um fogão.

Este vídeo mostra na prática o uso do `rebase`. É um comando super poderoso, mas também super perigoso — por isso é importante entender e usar de forma correta, porque se cair em mãos erradas pode literalmente estragar (ou, como diria a avó do autor, "esbodegar") o versionamento do projeto.

> Nota de patrocínio: o vídeo conta com apoio da Alura, plataforma de ensino de tecnologia no Brasil, com cursos do básico ao avançado incluindo um curso específico de Git e GitHub para quem gerencia projetos.

## Parte 1 — Conceito: Estrutura de Branches e Commits

Antes da prática, o autor desenha a estrutura de branches e commits para explicar como o `rebase` funciona (usando a extensão de desenho do VS Code).

Cenário de exemplo:

1. Existe uma branch principal, `main`. Um commit é feito nela (`commit 1`).
2. Uma nova alteração é feita, gerando o `commit 2`, ainda na `main`.
3. A partir do `commit 2` da `main`, cria-se uma nova branch, `feature`, para implementar uma nova funcionalidade.
4. Na branch `feature`, são feitas mudanças e um novo commit é criado (`commit` da feature). Depois, mais uma mudança gera outro commit (`feature 2`).
5. O desenvolvedor permanece nessa branch de feature, commitando, até conseguir uma versão final para o recurso que está sendo criado.

### O Problema

Enquanto isso, a `main` pode receber atualizações — outros commits — porque frequentemente há trabalho paralelo acontecendo (múltiplas branches de feature, muitas vezes nomeadas com algum código de referência).

Quando chega o momento de juntar tudo (finalizar o código de uma feature), é comum a `main` já não estar mais no mesmo commit em que a branch de feature foi criada — isso acontece com muita frequência, seja usando `main`/`master` como branch principal, seja usando uma estratégia como Git Flow com `develop`.

## Parte 2 — A Ideia do Rebase

Ao invés de tentar fazer um merge (que criaria um commit de merge que "não serve para nada"), a ideia do `rebase` é trazer toda a branch de feature para a ponta atual da `main` — ou seja, trocar a *base* da feature. Daí o nome **rebase**: reposicionar a origem (base) da branch a partir do commit mais recente da branch principal de onde ela foi criada.

Depois do rebase, a branch de feature já fica pronta para um merge (fast-forward) ou para outra estratégia, trazendo consigo todo o histórico de commits da `main` que ela não tinha antes. Depois disso, a branch de feature pode ser descartada.

**Importante:** essa estratégia é usada em repositórios **locais**. Não deve ser utilizada em repositórios **públicos/remotos** compartilhados, pois o `rebase` reescreve o histórico do Git. É fundamental usá-lo com muita parcimônia, mantendo as features sempre alinhadas com a branch principal (seja `main` ou `develop`).

## Parte 3 — Demonstração Prática

### Setup inicial

O autor cria um repositório de teste:

```bash
git init
git add .
git commit -m "commit 1"
```

Ele está na branch `master` (poderia renomear para `main`, que é a mais usada atualmente). Para visualizar o histórico de commits diretamente no VS Code, usa a extensão **Git History**.

Segue fazendo uma segunda alteração e commit:

```bash
git add .
git commit -m "commit 2"
```

### Criando a branch de feature

Com o histórico tendo dois commits na `main`, chega o momento de criar a feature. É adicionado um trecho de código (um `console.log` personalizado) — mas antes de commitar, o autor **cria uma nova branch**:

```bash
git checkout -b feature
```

Agora, ainda na branch `feature`, o código é adicionado e commitado:

```bash
git add .
git commit -m "feature: primeira alteração"
```

Ao olhar o histórico na branch `feature`, ele mostra os dois commits herdados da `main` mais o novo commit da feature — a partir do `commit 2` é que se abriu o espaço para a feature.

Simulando que a feature ainda não está pronta, é feita mais uma alteração (uma injeção de dependência de exemplo, chamada `feature 2`):

```bash
git add .
git commit -m "feature: segunda alteração"
```

Agora a branch `feature` tem dois commits próprios além dos herdados da `main`, exatamente como no diagrama desenhado no início.

### Simulando uma atualização paralela na main

Nesse meio-tempo, imagine que a `main` foi modificada por outra pessoa/trabalho paralelo. Para simular isso, o autor volta para a `main`:

```bash
git checkout main
```

Faz uma alteração no mesmo arquivo usado na feature (para gerar conflito propositalmente) e commita direto na `main` (o autor ressalta que commitar direto na `main` não é o ideal, é só para fins didáticos):

```bash
git add .
git commit -m "commit 3"
```

Agora a `main` tem um `commit 3` que a branch `feature` não conhece. Nessa situação, um `git merge` da feature para a main **não conseguiria** ser feito de forma limpa (fast-forward), pois as histórias divergiram e o mesmo arquivo foi alterado nos dois lados — vai gerar conflito.

### Resolvendo com rebase

Voltando para a branch `feature`:

```bash
git checkout feature
git rebase main
```

O `git rebase main` pega o início da feature (os commits que ela tem a mais) e reposiciona a partir do último commit da `main` (`commit 3`). Como o mesmo arquivo foi alterado nos dois lados, ocorre um **conflito**, que o Git sinaliza pedindo resolução manual.

O VS Code oferece um editor de merge/conflitos: de um lado mostra o que está na versão corrente (na `main`) e do outro o que está entrando (da `feature`), com um painel de resultado. O autor resolve o conflito optando por manter as duas mudanças (aceitando ambas as alterações concorrentes no arquivo).

Após resolver o conflito no editor:

```bash
git add .
git rebase --continue
```

Olhando o histórico da branch `feature` depois disso: ela não está mais baseada no `commit 2` — agora o `commit 3` (que veio da `main`) foi inserido na linha do tempo, e os commits da feature continuam na sequência, por cima dele. É por isso que o rebase é considerado perigoso: ele altera a estrutura do histórico do Git. Mas dessa forma, a feature fica preparada para ser recebida pela `main`, já que o último commit em comum bate.

### Finalizando: merge da feature na main

Voltando para a `main`:

```bash
git checkout main
git rebase feature
```

(O autor observa que, alternativamente, poderia ter feito só o primeiro rebase — feature baseada na main — e depois um `merge` normal da main para trazer a feature.)

Depois desse segundo rebase, o histórico da `main` mostra o `commit 3` que já existia, agora seguido pelos commits da feature — o código final combinado.

## Parte 4 — Regra de Ouro

Essa estratégia (rebase para realinhar branches) só deve ser adotada como boa prática em **repositórios locais**. Quando o trabalho envolve repositórios remotos compartilhados, a prática correta é usar **pull request** e fazer o **merge** como deve ser feito — não reescrever histórico compartilhado com rebase.

## Encerramento

O autor menciona que pode fazer um vídeo futuro sobre **squash**, outra técnica muito utilizada para deixar o histórico do Git mais limpo.
