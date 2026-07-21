---
type: concept
title: "Loop de Confirmação de Entendimento"
aliases: ["repetir o entendimento", "explicar de volta a tarefa", "playback de requisito"]
date_created: 2026-07-21
date_updated: 2026-07-21
source_count: 1
tags: [comunicacao, tarefas, requisitos, retrabalho, maturidade]
skill: tech-mentor-testing
status: draft
---

# Loop de Confirmação de Entendimento

Técnica para garantir que uma tarefa foi entendida corretamente antes de implementar: em vez de interromper quem está explicando com perguntas pontuais, ouvir até o fim, depois **dizer de volta o que foi entendido** ("o que eu entendi foi X, a lógica é Y") e pedir para a pessoa aguardar essa explicação completa antes de corrigir ou complementar.

## Por que funciona melhor que interromper

Interromper no meio da explicação tende a gerar correções fragmentadas e uma sensação de "já vou entender depois". Explicar de volta o entendimento completo, de uma vez, expõe lacunas e mal-entendidos de forma muito mais visível para quem está ouvindo — inclusive fazendo essa pessoa repensar se a própria proposta faz sentido.

## O loop

```
Pergunta o que precisa ser feito → anota
         ↓
Escuta a explicação completa, sem interromper
         ↓
Diz de volta: "o que eu entendi foi..."
         ↓
Pessoa corrige/complementa
         ↓
Repete até certeza real de entendimento
```

## Efeito colateral: antecipar problemas

Com prática, o loop deixa de ser só confirmação passiva — passa a gerar perguntas que antecipam edge cases ainda durante a explicação da tarefa. Exemplo: ao ouvir "atualizar a data de acesso quando o usuário logar", antecipar "e se o cliente sair da página sem deslogar?" — o que frequentemente revela que a regra de negócio não estava tão clara quanto quem pediu imaginava.

## Relação com [[wiki/concepts/comunicacao-tecnica]]

Comunicação Técnica coloca a responsabilidade da tradução em quem **emite** a informação. O loop de confirmação de entendimento é a aplicação prática disso do lado de quem **recebe**: em vez de assumir passivamente que entendeu, você verifica ativamente, transferindo para si mesmo parte do trabalho de garantir que a comunicação realmente aconteceu.

## Relação com [[wiki/concepts/pensamento-estruturado]]

É uma instância concreta do primeiro passo do pensamento estruturado ("entender o problema com clareza") aplicado especificamente ao momento de receber uma tarefa de outra pessoa, antes de qualquer decomposição técnica — ver [[wiki/concepts/mapear-entrada-processamento-saida]] para o passo seguinte, já técnico.

## Benefício de carreira

Além de reduzir retrabalho, o hábito constrói respeito no time: quem usa o loop consistentemente ganha reputação de estimar tarefas com precisão, porque nada "aparece no meio do planejamento" depois que o escopo foi confirmado dessa forma.

## Key Sources

- [[wiki/sources/3-pilares-testes-automatizados-produtividade]]
