---
type: concept
title: "Controller"
aliases: ["controlador", "controllers", "MVC controller", "fat controller", "thin controller"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [arquitetura, mvc, camadas, backend, api, separation-of-concerns, tech-mentor-backend]
skill: tech-mentor-backend
status: stub
---

# Controller

Camada que recebe a entrada (no backend, a requisição HTTP), chama a lógica da aplicação e devolve a saída (status, headers, corpo). Vem do MVC (Model–View–Controller); numa API, a "view" é a serialização em JSON ([[wiki/concepts/api-rest]]).

## O que fica no controller e o que não fica

| No controller | Fora dele (service/use case, domínio, repositório) |
|---|---|
| Ler `params`, `query`, `body`, headers | Regras: e-mail único, cálculo de preço, permissões de negócio |
| Validar formato da entrada | Acesso a banco e serviços externos |
| Chamar o use case certo | Orquestração de várias entidades e transações |
| Traduzir resultado e erros em status HTTP | Qualquer coisa que precise rodar sem HTTP (CLI, fila, teste) |

Na arquitetura hexagonal, o controller é um *primary adapter*: dispara o domínio, mas não contém o domínio `[skill: tech-mentor-backend]`. Ver [[wiki/concepts/camada-de-aplicacao-vs-modelo]], [[wiki/concepts/arquitetura-em-3-camadas]] e [[wiki/concepts/separation-of-concerns]].

**Fat controller:** a regra mora no controller, misturada com `request`/`response`. Funciona em app pequeno; o custo aparece quando a mesma regra precisa ser chamada de outro lugar ou testada sem servidor. **Thin controller** é o oposto: poucas linhas, só tradução HTTP ↔ aplicação.

## No JStack (aula 06)

Em [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]], [[wiki/entities/mateus-silva]] cria `src/controllers/UserController.js` (objeto com `listUsers(request, response)`) e o define como "o responsável por armazenar toda a regra de negócio da nossa aplicação", com as funções do [[wiki/concepts/crud]] de usuários. A separação tira a lógica do `index.js`, que é o objetivo; a definição, porém, descreve um fat controller. O exemplo citado (verificar se o e-mail já existe no banco) é de service.

## Key sources

- [[wiki/sources/jstack-controller-de-usuarios-e-sistema-de-rotas]]: UserController como objeto com listUsers; "toda a regra de negócio"
