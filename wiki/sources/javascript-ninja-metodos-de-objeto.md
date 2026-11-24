---
type: source
title: "Métodos de objeto (JavaScript Ninja, semana 3, vídeo 02)"
aliases: ["JavaScript Ninja métodos de objeto", "JS Ninja métodos", "02 - Métodos de objeto"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [javascript, objetos, metodos, notacao-de-ponto, reatribuicao, incremento, funcoes]
skill: lang-dynamic
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/javascript-ninja-metodos-de-objeto.md"
source_url: ""
author: "Fernando Daciuk"
date_published: ""
date_ingested: 2026-11-24
---

# Métodos de objeto (JavaScript Ninja, semana 3, vídeo 02)

## TL;DR

Segundo vídeo da "terceira aula" do [[wiki/entities/javascript-ninja|JavaScript Ninja]] (cerca de 10 min), continuação de [[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos|tipos de dados e objetos]]. Fecha o elo entre "atribuir função a uma variável" e objeto. Autoria de [[wiki/entities/fernando-daciuk|Fernando Daciuk]], confirmada pelo próprio exemplo: `pessoa.nomeCompleto()` devolve "Fernando Daciuk" ("Fernando da Silva" na legenda).

- **Método:** "quando nós atribuímos a uma propriedade de um objeto uma função, nós chamamos essa propriedade de método" ([[wiki/concepts/objetos-javascript]], [[wiki/concepts/funcoes-de-primeira-classe]]).
- **Reatribuir a variável apaga tudo:** `pessoa = { sexo: 'masculino' }` deixa só `sexo`; "você vai perder tudo o que você tinha" ([[wiki/concepts/efeito-colateral]]).
- **Acrescentar com ponto:** `pessoa.cor = 'caucasiano'` cria a propriedade e mantém as outras. "Novas atribuições, sempre [...] o nome do objeto, ponto, o nome da propriedade, é igual, o valor" ([[wiki/concepts/notacao-de-ponto-e-colchetes]]).
- **Três métodos:** `andar` retorna "estou andando"; `aniversario` faz `pessoa.idade++` e "não vai retornar nada"; `nomeCompleto` retorna `pessoa.nome + ' ' + pessoa.sobrenome` e "não vai modificar nada".
- **Invocar** é `pessoa.andar()`: sem os parênteses, só se vê a função ([[wiki/concepts/funcoes-javascript]]).
- Próximo vídeo: "mais algumas coisas legais [...] com objetos" (na pasta, "Métodos de objeto (continuação)").

Continua em [[wiki/sources/javascript-ninja-metodos-de-objeto-continuacao]] (semana 3, vídeo 03: continuação e desafio da semana 3).

## Key Claims

### Do valor ao método

- O objeto tem propriedades com "o nome [e] um valor", e o valor "pode ser um valor primitivo [...] ou [...] um outro objeto". Função é objeto ([[wiki/sources/javascript-ninja-tipos-de-dados-e-objetos|vídeo anterior]]), então pode ser valor de propriedade.
- "Quando nós atribuímos a uma propriedade de um objeto uma função, nós chamamos essa propriedade de método."
- Os métodos "podem ser, basicamente, ações que eu vou atribuir a essa pessoa".

### Reatribuir × acrescentar

- Ponto de partida: `var pessoa = { nome: 'Fernando', idade: 30, altura: 1.85, peso: 85 }`.
- "Se eu [...] atribuir novamente um valor aqui, por exemplo, sexo masculino [...] quando eu acessar a variável pessoa, eu perdi todas as minhas outras propriedades, porque eu atribui novamente um outro objeto."
- "Se eu quiser [...] que um objeto já criado [...] tem outras propriedades, eu preciso usar a notação do ponto": `pessoa.cor = 'caucasiano'`, e "eu tenho todas as minhas propriedades que eu tinha criado, inclusive a cor".
- Resumo da aula: na criação, chaves, "dois pontos" e "separando as propriedades por vírgula"; depois, `objeto.propriedade = valor`.

### `andar`

- `pessoa.andar = function () { return 'estou andando' }`. "Aqui eu tenho todas as minhas propriedades, e tenho mais [...] o meu método andar."
- Para executar, "a notação de abre e fecha parênteses": `pessoa.andar()`.

### `aniversario`

- "Ele não vai retornar nada, na verdade, mas ele vai fazer com que a idade dessa pessoa aumente um ano": `pessoa.aniversario = function () { pessoa.idade++ }`.
- Invocado, "não retorno nada, certo? Porque a minha função não retorna nada" (o REPL mostra `undefined`). Depois, `pessoa.idade` é 31.
- "O operador [...] mais mais, ele vai incrementar o valor e vai automaticamente atribuir aquele valor. É exatamente o que acontece com o nosso objeto" ([[wiki/concepts/incremento-e-decremento]]).

### `nomeCompleto`

- `pessoa.sobrenome = 'Daciuk'` e `pessoa.nomeCompleto = function () { return pessoa.nome + ' ' + pessoa.sobrenome }`: "eu não vou modificar nada. Simplesmente vou retornar".
- `pessoa.nomeCompleto()` "me retornou Fernando Daciuk".

## Precisões e tensões com a wiki

`⚠️` A skill lang-dynamic não tem arquivo de referência para objetos e métodos do JavaScript básico; as precisões vêm da MDN e da especificação, marcadas `[external]` (sem fetch, conhecimento base; confiança alta salvo indicação).

1. **A definição de método está certa.** `[external]` Método é a propriedade cujo valor é função (https://developer.mozilla.org/en-US/docs/Glossary/Method). Não há tipo "método" separado: `typeof pessoa.andar` é `"function"`.
2. **Os métodos usam `pessoa`, não `this`.** `[external]` Funciona aqui, mas amarra o método à variável global: se `pessoa` for reatribuída ou o método copiado para outro objeto, ele lê o objeto errado. A forma usual é `this.idade++` e `this.nome + ' ' + this.sobrenome`, com `this` igual ao objeto antes do ponto na chamada ([[wiki/concepts/objetos-javascript]], seção *this*). `this` não aparece na aula.
3. **Reatribuir troca a referência, não apaga o objeto.** `[external]` `pessoa = { sexo: 'masculino' }` faz a variável apontar para um objeto novo; o antigo continua intacto para quem ainda o referencia, e só some quando o coletor de lixo o recolhe. "Perder tudo" vale para quem só tinha a variável.
4. **Ponto cria ou sobrescreve.** `[external]` `pessoa.cor = ...` cria a propriedade se ela não existe e troca o valor se existe; é mutação do mesmo objeto, visível por todas as referências a ele ([[wiki/concepts/efeito-colateral]], [[wiki/concepts/imutabilidade]]).
5. **`aniversario` × `nomeCompleto` é a distinção comando × consulta.** O primeiro muda estado e devolve `undefined`; o segundo devolve valor sem mudar nada. A aula diz as duas coisas com todas as letras ("não vai retornar nada", "não vou modificar nada").
6. **"Operador binário mais mais".** `++` é unário; a mesma troca apareceu três vezes no [[wiki/sources/javascript-ninja-operadores-unarios|vídeo de unários]] e ficou literal ([[wiki/concepts/operadores-unarios-javascript]]).
7. **Nomes de método com espaço não existem.** A fala diz "nome completo"; o código usa `nomeCompleto` (inferência pelo identificador; o nome exato não se lê na legenda). Com espaço, só por colchetes e aspas ([[wiki/concepts/identificadores-javascript]]).
8. **Legenda.** Trocas principais: "na índia"→Ninja (alta), "parentes"→parênteses, "aponta"/"aponte" (4×)→ponto (média-alta), "o pai de"→eu perdi (média), "no homem"→nome (média-alta), "corte"/"Acordo"/"corpo"→cor (média), "mutação"→notação (média), "por exemplo"→por vírgula (média), "oportunidade"→ponto idade (média-alta), "amizade"→idade, "fundação"→função (alta), "meu mentor"→me retornou (média), "Silva"→Daciuk (média-alta, ver Open Questions), "da Silva"→Daciuk (alta). Lista completa no [[wiki/log]].

## Entities

- [[wiki/entities/fernando-daciuk]]: instrutor; o próprio nome é o dado do exemplo.
- [[wiki/entities/javascript-ninja]]: o curso.
- [[wiki/entities/javascript]]: assunto.

## Concepts

- [[wiki/concepts/objetos-javascript]]
- [[wiki/concepts/notacao-de-ponto-e-colchetes]]
- [[wiki/concepts/funcoes-javascript]]
- [[wiki/concepts/funcoes-de-primeira-classe]]
- [[wiki/concepts/incremento-e-decremento]]
- [[wiki/concepts/efeito-colateral]]
- [[wiki/concepts/imutabilidade]]

## Open Questions

- **Sobrenome:** a legenda diz "sobrenome igual Silva" e o resultado "Fernando da Silva". `nome + ' ' + sobrenome` com 'Silva' daria "Fernando Silva"; com 'Daciuk', "Fernando Daciuk", que a legenda sempre escreve "Fernando da Silva". Por isso os dois viraram Daciuk (média-alta).
- O texto do `andar` é "estou andando", mas a fala depois diz "isso vai dizer que a pessoa está andando": pode ser só paráfrase.
- "Uma fantochada", ao criar `aniversario`: provavelmente "uma function"; ficou literal.
- A legenda perde o peso e o `sexo` no segundo objeto ("Isso porque eu nem sei o que o sexo masculino está"); pelo contexto, o objeto recriado tem `sexo: 'masculino'`.

## Raw quotes

- "Quando nós atribuímos a uma propriedade de um objeto uma função, nós chamamos essa propriedade de método."
- "se você atribui novamente um outro objeto pra uma pessoa, você vai perder tudo"
- "eu não vou modificar nada. Simplesmente vou retornar"
