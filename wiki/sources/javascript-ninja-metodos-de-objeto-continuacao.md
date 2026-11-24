---
type: source
title: "Métodos de objeto, continuação, e desafio da semana 3 (JavaScript Ninja, semana 3, vídeo 03)"
aliases: ["JavaScript Ninja métodos de objeto continuação", "JS Ninja desafio 3", "03 - Métodos de objeto (continuação)"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, objetos, metodos, git, github, fork, upstream, pull-request, branch, desafio]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-metodos-de-objeto-continuacao.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Métodos de objeto, continuação, e desafio da semana 3 (JavaScript Ninja, semana 3, vídeo 03)

## TL;DR

Terceiro e último vídeo da "terceira aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 14 min), depois de [[wiki/sources/javascript-ninja-metodos-de-objeto|métodos de objeto]]. Dois minutos de revisão e o resto sobre o desafio da semana 3 e o fluxo de git para entregá-lo. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]] com confiança alta: "meu nome é Fernando da Silva" na legenda, a conta `fdaciuk` e o repositório da organização `da2k`.

- **Propriedade × método:** variável dentro do objeto "chama propriedade"; função dentro do objeto "não se chama função, ele se chama método". `pessoa.nome` dá o valor; `pessoa.andar` é função e precisa ser invocado ([[wiki/concepts/objetos-javascript]]).
- **Desafio 3** no repositório do curso: criar objetos, propriedades e métodos. Nomes "todo em maiúsculo [...] entre colchetes", como em "Olá, meu nome é [NOME] [SOBRENOME]!", marcam onde concatenar o valor ([[wiki/concepts/template-literals]]).
- **Fluxo de fork:** `origin` é o fork na conta do aluno (`fdaciuk/curso-javascript-ninja`); `upstream`, o do curso (`da2k/curso-javascript-ninja`). Recomenda a linha de comando, porque o software do GitHub "não suporta mais de um remote" ([[wiki/concepts/fork-e-upstream]], [[wiki/concepts/git]]).
- **Passos:** voltar para a master, `fetch` do upstream, merge na master (aparece a pasta do challenge 3, em branco), `checkout -b challenge-03`, editar, `git add`, `git commit -m`, `git push origin challenge-03`, pull request; depois `git push origin master`.
- **Uma branch por desafio**, e a master "sempre atualizada com o repositório principal", com os desafios em branco.
- **Dúvidas:** responder o email do curso ou, melhor, abrir uma issue no GitHub; mandar o pull request "pela metade mesmo" e perguntar nele. "O ninja de verdade" pergunta.
- Fim da aula 3; próxima semana.

Continua em [[wiki/sources/javascript-ninja-truthy-e-falsy]] (semana 4, vídeo 01: truthy e falsy).

## Key Claims

### Revisão: propriedade × método

- Métodos "são funções que você usa como o valor da propriedade do objeto": "quando eu tenho uma propriedade que recebe uma function, [...] essa propriedade se torna método".
- `pessoa.nome` "vai me retornar o nome. Isso é uma propriedade". `pessoa.andar` "é uma função. Eu vou precisar invocar ela para ver o resultado dela."
- Analogia: fora do objeto, `var` cria variável e `function` cria função; "dentro de um objeto, [...] ao invés de variável, você tem uma propriedade [...] e você tem um método quando você cria uma função". "Meu objeto ponto propriedade, ele é basicamente como se fosse a minha variável [...] dentro do objeto."

### Desafio da semana 3

- "Você podem ver que o desafio 3 já está aqui, está no repositório." O tema: "criação de métodos, de criação de objetos e criação de propriedades no objeto".
- Exemplo do enunciado: "Crie um método chamado o nome completo, que retorna a frase: Olá, meu nome é", nome e sobrenome, "um ponto de exclamação".
- "Sempre que tiver um nome assim, todo em maiúsculo, [...] entre colchetes [...] significa que [...] você [vai] utilizar uma variável [...] para você concatenar essa string." No caso, a propriedade do objeto que o aluno vai criar.

### Remotes

- Para quem está "batendo um pouco [a] cabeça" com a atualização do repositório: o fork já foi feito nos vídeos anteriores.
- "Recomendo que você utilize a linha de comando [...] Até onde eu vi, o software do [GitHub] [...] não suporta mais de um remote."
- "A origem [...] vai ser [...] o meu repositório na minha conta": `fdaciuk/curso-javascript-ninja`. "E o upstream vai ser um repositório do curso mesmo": `da2k/curso-javascript-ninja`. "Na aula 2 eu mostrei" como adicionar.

### Atualizar e entregar

- Na master local havia challenge 1 e 2, "faltando três". Ele volta para a master e dá o comando que "vai baixar [...] do repositório principal [...] todas as branches"; depois um merge, e a master passa a ter os três desafios "em branco".
- "Você não vai editar direto na master": `checkout -b challenge-03` "vai criar uma branch [...] baseado na master". Nela, edita o arquivo do desafio (`var objeto = {}`, "você que vai fazer isso sozinho").
- O status mostra o arquivo modificado; `add`; "alterações [...] para serem commitadas"; `git commit` com a mensagem "challenge 03"; `push origin challenge-03`, para o próprio repositório, "não é o repositório do curso". Depois, o pull request, como nas outras semanas.
- Volta para a master e `git push origin master`, para o fork também ter a master atualizada.

### Uma branch por desafio

- "A ideia é que [...] cada [branch] [...] fique com o seu desafio", e a master "fica sempre com os desafios em branco", "sempre atualizada com o repositório principal".
- Prova: na branch, a pasta do challenge 3 tem a alteração; "se olhar na master, essa alteração não existe".

### Encerramento

- "O objeto é uma das partes mais importantes do JavaScript", junto com as funções; "é assim que vai conseguir chegar no nível Ninja".
- Dúvidas pelo email semanal do curso, ou "uma issue no GitHub", "que pode ajudar outras pessoas". Exercício travado: mandar "pela metade mesmo" e perguntar no próprio pull request.
- "Ainda não chegamos [...] na hora da prova"; os desafios são "praticamente uma prova onde você vai treinar".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para objetos básicos de JavaScript nem para o fluxo de git; as precisões vêm da MDN e da documentação do Git e do GitHub, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **Propriedade não é variável.** A analogia ajuda, mas propriedade não tem escopo, não é declarada com `var` e só existe pelo objeto: `pessoa.nome`, nunca `nome` sozinho. E o método que lê `pessoa` em vez de `this` continua frágil ([[wiki/sources/javascript-ninja-metodos-de-objeto]], Precisões 2).
2. **`[NOME]` é convenção do enunciado, não sintaxe.** O aluno troca pela concatenação com `+`. `[external]` Desde o ES2015 há template literals: `` `Olá, meu nome é ${this.nome} ${this.sobrenome}!` `` ([[wiki/concepts/template-literals]]).
3. **`fetch` não cria branches locais.** `[external]` `git fetch upstream` baixa os commits e atualiza as *remote-tracking branches* (`upstream/master`); a master local só muda com o merge (`git merge upstream/master`). `git pull upstream master` faz os dois de uma vez (https://git-scm.com/docs/git-fetch).
4. **O fluxo é o "syncing a fork" do GitHub.** `[external]` Remote `upstream`, `fetch`, merge na branch padrão, branch por mudança e pull request para o repositório original (https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork). Hoje o GitHub tem o botão *Sync fork* e `gh repo sync`, e a branch padrão de repositórios novos é `main` desde 2020 ([[wiki/concepts/fork-e-upstream]]).
5. **"O software do GitHub não suporta mais de um remote".** `[external]` O próprio instrutor diz "até onde eu vi". Era o GitHub Desktop da época; a afirmação não foi verificada e pode estar desatualizada (confiança baixa).
6. **Branch por desafio é *feature branch*.** A master fica idêntica ao upstream e cada entrega vive na sua branch, o que mantém os pull requests independentes. Não é Git Flow, que tem `develop` e branches de release ([[wiki/concepts/git-flow]]).
7. **O desafio da semana 2 continua fora da wiki.** O vídeo trata o fluxo como já visto ("na aula 2 eu mostrei", "como mostrei no vídeo anterior"), mas esses vídeos não estão entre as transcrições.
8. **Legenda.** É a mais deformada da série até aqui, sobretudo na parte de git. Trocas principais: "na índia"→Ninja (alta), "Manuel"→Meu nome é (média-alta), "da Silva"→Daciuk (alta), "metro do"→método, "fonte" (2×)→function (média), "timing"→string (média-alta), "focado"→forkado, "Monte"→remote (média-alta), "F da Silva que"→fdaciuk, "da 2K"→da2k (alta), "obstrui"→upstream (alta), "massa"→master (cerca de 12×, média-alta), "além de"/"Tim além de"/"tio além de"/"TI além de"→challenge (cerca de 25×, média), "bobagens"→branches (média), "Shekau te"→checkout (média-alta), "excelente"→challenge (média), "banda"/"frente"/"brinde"→branch (média), "convite"/"comite"→commit, "combinadas"→commitadas, "patch origem diferente"→push origin challenge (média), "Apple Watch"→pull request (média-alta), "gde"→git, "bilhete(s)"→objeto(s), "ficha"→issue (média). Os comandos exatos (`fetch`, `merge upstream/master`) não se leem; vêm do contexto. Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor; conta `fdaciuk`.
- [[wiki/entities/javascript-ninja]]: o curso e o repositório `da2k/curso-javascript-ninja`.
- [[wiki/entities/github]]: onde ficam o repositório, as issues e os pull requests.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/template-literals]]
- [[wiki/concepts/fork-e-upstream]]
- [[wiki/concepts/git]]
- [[wiki/concepts/git-flow]]

## Open Questions

- **Os comandos de sincronização.** "Eu vou dar o comando efetivo. Então eu percebi [...]" é provavelmente `git fetch upstream`; "um merge Down Tim" e "um MBA master", `git merge upstream/master`. Ficaram literais.
- "O nome dele vai se chamar eu percebi": provavelmente "upstream"; ficou literal.
- O nome da branch: "checkout menos B challenge fácil 03" e depois "uma branch chamada de aprendizado 3". `challenge-03` é inferência pelo padrão das pastas.
- O GitHub, na legenda, sai como "Vietname" e "evitar"; o terceiro "como evitar" ficou literal.
- "Eu tinha 29" e "a tela de 2", na listagem das branches, não se recuperam.

## Raw quotes

- "quando eu tenho o meu método, ele não se chama função, ele se chama método"
- "Você não vai editar direto na master."
- "Pergunte sempre, que o ninja de verdade [...] pergunta"
