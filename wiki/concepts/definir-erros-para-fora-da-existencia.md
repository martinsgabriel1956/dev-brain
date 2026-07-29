---
type: concept
title: "Definir Erros Para Fora da Existência"
aliases: ["define errors out of existence", "mascarar exceções", "exception masking", "agregação de exceções", "exception aggregation"]
date_created: 2026-07-29
date_updated: 2026-07-29
source_count: 1
tags: [complexidade, design, ousterhout, exceptions, error-handling]
skill: tech-mentor-backend
status: draft
---

# Definir Erros Para Fora da Existência

## TL;DR

Técnica de [[wiki/entities/john-ousterhout]] (*A Philosophy of Software Design*, Cap. 10): redesenhar a semântica de uma operação para que uma condição antes tratada como erro deixe de ser um erro — eliminando a necessidade de qualquer código de tratamento de exceção para aquele caso. É a mais eficaz de quatro técnicas do livro para reduzir a complexidade desproporcional causada por exceções (as outras três: mascarar, agregar, e simplesmente travar a aplicação quando não há nada sensato a fazer).

## Por que exceções custam mais que parecem

Exceções interrompem o fluxo normal do código, criam mais casos especiais (retomar operação vs. abortar com estado inconsistente), e são pouco testadas na prática — daí a citação do autor: *"code that hasn't been executed doesn't work"*. Um estudo citado no livro (Yuan et al., USENIX OSDI 2014) encontrou que **mais de 90% das falhas catastróficas em sistemas distribuídos de dados vieram de tratamento de erro incorreto**, não do erro em si.

## Três exemplos concretos do livro

1. **Tcl `unset`** — o próprio autor admite erro de design: fazia `unset` lançar erro ao tentar remover uma variável inexistente. Mudar a semântica de "remover a variável" para "garantir que a variável não existe" elimina o erro por completo — não existe mais nada de errado em pedir para apagar algo que já não está lá.
2. **Deleção de arquivo aberto: Unix vs. Windows** — Windows recusa deletar um arquivo aberto por outro processo, obrigando o usuário a caçar e matar o processo. Unix adia a deleção real até o último handle fechar, e a chamada de deleção sempre retorna sucesso imediatamente — dois tipos de erro definidos para fora da existência ao mesmo tempo (a deleção falhar, e os processos que já têm o arquivo aberto verem uma exceção).
3. **`substring` do Java** — lança `IndexOutOfBoundsException` para índices fora do intervalo da string. Python resolve o mesmo problema retornando uma fatia vazia/truncada em list slices fora do intervalo — nenhum erro para tratar.

## As outras três técnicas (quando o erro não pode ser eliminado)

- **Mascarar (exception masking):** tratar a condição no nível mais baixo possível, sem propagar para cima. Ex.: TCP reenviando pacotes perdidos sem que a aplicação saiba; NFS travando a aplicação (em vez de lançar erro) quando o servidor de arquivos está fora do ar, porque não há nada sensato que a aplicação faria com esse erro de qualquer forma.
- **Agregar (exception aggregation):** um único handler no topo da pilha captura várias exceções distintas de baixo nível. Ex.: um servidor HTTP com um único handler de erro para todos os parâmetros ausentes de todas as URLs; RAMCloud "promove" um erro pequeno (objeto individual corrompido) para o mesmo mecanismo de recuperação de crash de servidor inteiro — menos mecanismos de recuperação distintos para manter, ao custo de recuperação um pouco mais cara para o caso raro.
- **Travar a aplicação (just crash):** quando não há alternativa sensata (memória esgotada, erro de I/O em disco físico), a resposta mais simples é abortar com mensagem de diagnóstico. Exemplo: `ckalloc` em C, que encapsula `malloc` e já aborta a aplicação se a alocação falhar, para que nenhum chamador precise checar o retorno.

## Limite do princípio

Só faz sentido definir um erro para fora da existência (ou mascará-lo) se a informação daquele erro **não for necessária** fora do módulo. Contra-exemplo do livro: um módulo de rede que mascarava todo erro de rede — aplicações que o usavam ficaram sem nenhuma forma de saber se uma mensagem foi perdida ou um peer caiu, tornando impossível construir aplicações robustas sobre ele. Nesse caso a exceção precisa ser exposta, mesmo que isso aumente a complexidade da interface. Ver [[wiki/concepts/decidir-o-que-importa]].

## Relação com outros conceitos

- [[wiki/concepts/complexidade-acidental]] — exceções mal desenhadas são uma das fontes mais concretas e mensuráveis de complexidade acidental do livro.
- [[wiki/concepts/modulo-profundo]] — exceções fazem parte da interface de um módulo; menos exceções (via essa técnica) tende a produzir módulos mais profundos.
- [[wiki/concepts/decidir-o-que-importa]] — o limite do princípio é, no fim, uma aplicação de "só esconda o que realmente não importa para quem está de fora".

## Key Sources

- [[wiki/sources/filosofia-do-design-de-software-livro-completo]] — Cap. 10 completo (definir para fora da existência, mascarar, agregar, travar)
