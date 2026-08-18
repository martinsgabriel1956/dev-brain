---
type: concept
title: "Redução de Incerteza Antes de Estimar"
aliases: ["reduzir incerteza antes de estimar", "testar presunções antes de estimar", "não dá para estimar o desconhecido"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_count: 1
tags: [estimativa, carreira, planejamento, prova-de-conceito, engineering-management]
skill: tech-mentor-leadership
status: draft
---

# Redução de Incerteza Antes de Estimar

Não é possível estimar com qualquer grau de precisão algo que nunca foi feito, cuja viabilidade ainda não foi confirmada. Antes de tentar dar um número, é preciso primeiro reduzir a incerteza sobre **o que** será feito e confirmar que **é possível** fazê-lo — só então o processo de estimar (desenhar o sistema, quebrar em tarefas, atribuir números) tem qualquer chance de produzir um resultado útil.

## O Método, em Sequência

```
1. Identificar as partes do sistema que já são conhecidas
   (padrões já resolvidos pela equipe — endpoints, storage, etc.)
   → não geram incerteza relevante, não precisam de validação

2. Identificar as presunções desconhecidas / partes menos conhecidas
   → priorizar estas para redução de incerteza primeiro

3. Testar essas presunções — via prova de conceito real
   ou via pesquisa de terceiros que já resolveram problema parecido
   ([[wiki/concepts/prova-de-conceito|PoC]] não precisa ser sempre código;
   ler relatos de quem já resolveu pode dar ~95% de confiança)

4. Só depois de confirmado que A, B e C (as partes incertas) são
   viáveis, desenhar o sistema (diagrama ou texto)

5. Quebrar o desenho em tarefas pequenas e bem definidas
   e só então estimar cada uma
```

Pular a etapa 1–3 e ir direto para estimar o desenho ideal é o erro mais comum: a estimativa resultante não reflete o problema real, porque o problema real só se revela ao testar as partes desconhecidas.

## Por Que Isso Muda o Resultado

Testar uma presunção tecnológica pode revelar dois mundos radicalmente diferentes — e sem testar, não há como saber em qual desses mundos o time está:

- **Mundo A:** a lib/framework padrão já resolve exatamente o problema → questão de um dia.
- **Mundo B:** ninguém nunca resolveu o problema daquele jeito específico → questão de semanas ou meses, construindo do zero.

Sem esse teste, qualquer número dado é um chute disfarçado de estimativa — o próprio ato de "bater o martelo" numa estimativa sem ter confirmado a viabilidade é o que torna a estimativa inútil, mesmo que o processo pareça rigoroso (Fibonacci, planning poker, três estimadores).

## Priorizar o Menos Conhecido Primeiro

Não é viável (nem necessário) testar todas as presunções de um sistema antes de estimar — o retorno é maior ao testar primeiro as partes com maior chance de dar errado ou cujos limites são desconhecidos. Duas vantagens de testar cedo o que é menos conhecido:

- Pode poupar trabalho inteiro — o time desiste da abordagem ou da tarefa ao descobrir cedo que não é viável como imaginado.
- Pode corrigir a estimativa antes de comprometer um prazo com stakeholders, em vez de descobrir a inviabilidade no meio da execução.

## Relação com Outros Conceitos

- [[wiki/concepts/prova-de-conceito]] — é a ferramenta prática usada para reduzir incerteza; esta página generaliza o *quando* e o *porquê* usar PoC especificamente no contexto de preparar uma estimativa, não só de validar tecnologia nova antes de produção
- [[wiki/concepts/estimativas-de-software]] — esta página é o método prescritivo que resolve a lacuna que aquela página deixa em aberto (que fatores causam subestimação); aqui está o "como reduzir" na prática, passo a passo
- [[wiki/concepts/divisao-de-tarefas-em-partes-menores]] — a quebra em tarefas pequenas (passo 5 do método) só faz sentido *depois* da redução de incerteza; tentar dividir um problema ainda desconhecido em subtarefas "seguras e com prazo" (os dois testes daquela técnica) tipicamente falha porque a incerteza de fundo ainda não foi resolvida
- [[wiki/concepts/planning-fallacy]] — reduzir incerteza é uma contramedida estrutural ao viés, equivalente em espírito ao *reference class forecasting* já registrado naquela página (ambos buscam informação externa/empírica em vez de confiar só na intuição)

## Key Sources

- [[wiki/sources/por-que-estimativas-de-software-falham-como-melhorar]] — exemplo central: feature de geração de PDF para 1 milhão de clientes, com as presunções concretas testadas (capacidade do banco, viabilidade da lib de PDF) antes de desenhar o sistema e quebrar em tarefas
