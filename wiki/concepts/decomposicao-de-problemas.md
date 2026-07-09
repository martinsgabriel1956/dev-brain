---
type: concept
title: "Decomposição de Problemas"
aliases: ["problem decomposition", "quebrar em partes menores"]
date_created: 2026-05-13
date_updated: 2026-07-09
source_count: 3
tags: [decomposicao, fundamentos, cs-fundamentals]
skill: cs-fundamentals
status: draft
---

# Decomposição de Problemas

Técnica de resolver um problema complexo quebrando-o em subproblemas menores e mais simples, cada um resolvível de forma (quase) independente.

## Por que funciona

Nenhum problema complexo é resolvido de uma única vez. Ao decompor, cada parte menor pode ser pensada, testada e corrigida sem afetar as outras.

## Exemplo: caixa eletrônico

| Módulo | Responsabilidade |
|---|---|
| Autenticação | Verificar cartão e senha |
| Verificação de saldo | Checar saldo disponível |
| Validação do saque | Checar limite diário e dinheiro no caixa |
| Execução do saque | Debitar e liberar dinheiro físico |
| Encerramento | Devolver cartão, comprovante, encerrar sessão |

A autenticação não precisa saber nada sobre saldo. Isso é [[separacao-de-responsabilidades]] na prática.

## Relação com outros conceitos

- Viabiliza [[separacao-de-responsabilidades]]
- É o passo 2 do framework de [[logica-de-programacao]]
- Cada subproblema gera seu próprio [[fluxo-logico]]

## Exemplo: clone de Netflix

| Subproblema | Pergunta concreta |
|---|---|
| Autenticação | Cadastro, login, sessão |
| Galeria | Thumbnails, navegação |
| Página de vídeo | URL `/video/id=123`, player |
| Entrega do vídeo | **Onde está o arquivo? Como chega ao usuário?** |

A decomposição transforma "clone Netflix" — nebuloso demais para começar — em perguntas acionáveis que já apontam para soluções pesquisáveis.

## Relação com outros conceitos

- Viabiliza [[separacao-de-responsabilidades]]
- É o primeiro pilar do framework de [[logica-de-programacao]]
- Cada subproblema gera seu próprio [[fluxo-logico]]
- Com [[repertorio]] suficiente, a decomposição acelera por reconhecimento de padrões

## Aplicação em debugging: a árvore de decomposição

Fora do design de sistemas, a mesma técnica se aplica a diagnosticar um problema vago em produção ("o sistema tá lento"). Em vez de decompor em módulos, decompõe-se em perguntas cada vez mais específicas (onde, quando, para quem) até chegar numa causa isolável — ver [[arvore-de-decomposicao]] e [[pensamento-estruturado]].

## Key sources

- [[wiki/sources/logica-de-programacao-quatro-passos]] — framework de 4 passos; caixa eletrônico como exemplo
- [[wiki/sources/logica-de-programacao-o-que-e-de-verdade]] — primeiro pilar dos 5; exemplo com clone de Netflix e remoção de elemento de array
- [[wiki/sources/pensamento-estruturado-resolucao-de-problemas]] — aplicação da decomposição ao debugging de produção via árvore de perguntas (onde/quando/para quem)
