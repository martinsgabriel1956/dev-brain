---
type: concept
title: "Exceção vs. Erro"
aliases: ["erro vs exceção", "exception vs error", "erro de domínio", "exceção de sistema"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [fundamentos, backend, resiliencia, dominio, excecao, nodejs]
skill: tech-mentor-backend
status: draft
---

# Exceção vs. Erro

Distinção fundamental para design de sistemas resilientes: nem toda falha é igual, e a estratégia de tratamento muda radicalmente dependendo da categoria.

## Definições

### Erro de domínio

**Previsível**. Faz parte do fluxo normal da aplicação. Pode acontecer a qualquer momento e a aplicação sabe como reagir.

Exemplos:
- Campo obrigatório não enviado
- Tipo de dado inválido (`"abc"` onde se espera número)
- Usuário não encontrado
- Produto fora de estoque
- Senha incorreta

**Como tratar:** retornar uma resposta de erro com status HTTP adequado (400, 404, 422, etc.). Não lançar exceção. A aplicação continua rodando normalmente.

### Exceção

**Imprevisível**. Fora do controle da aplicação. Indica que algo no ambiente ou em uma dependência externa falhou de forma inesperada.

Exemplos:
- Conexão com banco de dados falhou
- Sistema externo indisponível
- Falta de memória no servidor
- Sem conexão com a internet
- `JSON.parse` de dado corrompido vindo de fila

**Como tratar:** [[let-it-crash]] — responder o cliente afetado, executar [[graceful-shutdown]], deixar o orquestrador recriar a instância.

## Por que a distinção importa

Tratar exceções como erros de domínio (com `try/catch` e retorno de mensagem genérica) pode:

1. **Mascarar o problema**: a aplicação parece estar funcionando, mas está num estado corrompido
2. **Impedir o reinício**: sem o `process.exit`, o orquestrador nunca recria uma instância limpa
3. **Acumular estado ruim**: cada requisição sucessiva torna o estado mais corrompido

Tratar erros de domínio como exceções (derrubar a aplicação por senha incorreta) é destruir disponibilidade por motivos evitáveis.

## Tabela de decisão

| Situação | Categoria | Estratégia |
|---|---|---|
| Email inválido | Erro de domínio | Retorna 422 |
| Usuário não existe | Erro de domínio | Retorna 404 |
| Banco de dados fora do ar | Exceção | Let it Crash |
| Memória esgotada | Exceção | Let it Crash |
| JSON malformado (input do usuário) | Erro de domínio | Retorna 400 |
| JSON malformado (dado de fila interna) | Exceção | Let it Crash (dado inesperado) |

A última linha mostra que o mesmo tipo de evento pode ser erro ou exceção dependendo da **origem**: input do usuário é previsível, dado corrompido de uma fila interna não é.

## Relação com outros conceitos

- [[let-it-crash]] — estratégia para exceções
- [[graceful-shutdown]] — implementação do encerramento após exceção
- [[asynclocalstorage]] — permite responder o cliente correto quando exceção ocorre
- [[robustez-de-sistemas]] — sistemas robustos distinguem os dois e tratam cada um adequadamente

## Key sources

- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] — distinção central da estratégia; exemplos concretos de cada categoria
