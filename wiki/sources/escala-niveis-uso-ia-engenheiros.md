---
type: source
title: "Os 7 Níveis de Como Engenheiros Usam IA — Por Que os Estudos de Produtividade Medem o Nível Errado"
aliases: []
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 0
tags: [escala-maturidade-ia, niveis-ia, carreira, modelo-mental, era-agentica, delegacao, orquestracao, multiagente]
skill: tech-mentor-leadership
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/escala-niveis-uso-ia-engenheiros.md
source_url: ""
author: "Valdemar Neto"
date_published: ""
date_ingested: 2026-06-01
---

# Os 7 Níveis de Como Engenheiros Usam IA

## TL;DR

Framework de 7 níveis (0–7) criado por "Steve" (ex-Google, ex-Amazon) que descreve como engenheiros evoluem no uso de IA. O que muda entre níveis não é a ferramenta — é o **modelo mental**. A maioria dos devs trava na transição do nível 2 para o nível 4. Os estudos que medem 20–30% de ganho de produtividade estão medindo os níveis 1–2 — onde a IA não mudou fundamentalmente a forma de trabalhar. A diferença entre nível 2 e nível 4 com a mesma ferramenta é de ~5x.

---

## Argumento Central

### Por que os estudos de produtividade estão errados

Estudos que medem ganhos de 20–30% avaliaram devs nos níveis 1–2 de uma escala de 7. O que eles não mediram: a diferença entre um dev nível 2 e um dev nível 4 com a mesma ferramenta não é 20% — é **~5x**. Não porque o nível 4 digita mais rápido, mas porque ele faz um trabalho fundamentalmente diferente.

### O paradoxo central

> Quanto mais alto o nível, **mais skill é necessária** — não menos.

- Nível 5: entender sistemas
- Nível 6: saber gerenciar times
- Nível 7: visão arquitetural de Staff+

Dev ruim com IA → faz coisas ruins mais rápido. Dev bom com IA → faz coisas muito melhores muito mais rápido. A IA amplifica o skill existente.

---

## Os 7 Níveis

| Nível | Nome | O que faz | Modelo mental |
|---|---|---|---|
| 0 | Negacionista | Não usa IA | "É hype, vou escrever na mão" |
| 1 | Cauteloso | Autocomplete, aceita/rejeita sugestão | Ferramenta de digitação |
| 2 | Perguntador | Chat para tirar dúvidas, substitui Stack Overflow | Oráculo de consulta |
| 3 | Delegador Básico | Pede funções uma por vez, copia, adapta | Assistente de código |
| 4 | Diretor | Escreve spec/testes, delega implementação, vai para a próxima tarefa | Especificador de comportamento |
| 5 | Orquestrador | Agente navega projeto, roda testes, corrige erros | Tech lead dando direção |
| 6 | Multi-Agentes | Múltiplos agentes em paralelo, cada um numa tarefa | Engineering manager |
| 7 | Arquiteto | Define arquitetura, contratos, specs; agentes constroem tudo | Arquiteto de sistemas |

---

## Claims Principais

### Claim 1 — Não dá para pular níveis

**Evidência:** Cada nível exige o modelo mental do anterior. Tentar ir do nível 2 direto ao nível 5 falha não por causa da ferramenta, mas porque a confiança e o contexto necessários não estão construídos.

**Confiança:** Alta — argumento lógico e consistente com padrões de aprendizado progressivo.

### Claim 2 — O gargalo crítico: transição nível 2 → nível 4

**Evidência:** A maioria dos devs trava aqui. O nível 4 exige:
1. **Confiança** — para deixar a IA trabalhar sem microgerenciar
2. **Contexto do sistema** — para escrever uma spec que faça sentido

Paradoxo: o nível 4 exige **mais** conhecimento de domínio do que o nível 3, mesmo delegando mais tarefas.

**Exemplo concreto:**
- Nível 3: "Escreve uma função que valida CPF."
- Nível 4: escreve arquivo de testes com todos os casos (CPF válido, inválido, com/sem máscara, casos de exceção, CPF internacional) e pede para implementar.

**Confiança:** Alta — demonstrado com exemplo concreto no vídeo.

### Claim 3 — Níveis 5–7 mudam a relação com o código

**Evidência:**
- Nível 5 (Orquestrador): agente navega, lê arquivos, roda testes, corrige — você define tarefa de alto nível
- Nível 6 (Multi-agentes): múltiplos agentes em paralelo; referência: Boris Cherny (criador do Claude Code) com 5 terminais abertos
- Nível 7 (Arquiteto): raramente toca em código; define arquitetura, contratos de API, critérios de qualidade

**Confiança:** Alta para 5–6, média para 7 (ainda emergente na prática).

---

## Entidades

- [[wiki/entities/valdemar-neto]] — autor do vídeo; relata estar no nível 6
- [[wiki/entities/steve-ex-google-amazon]] — criador original do framework (nome completo não mencionado)
- [[wiki/entities/boris-cherny]] — criador do Claude Code; citado como referência de workflow nível 6

---

## Conceitos Tocados

- [[wiki/concepts/escala-maturidade-ia-dev]] — conceito central criado neste ingest
- [[wiki/concepts/era-agentica]] — níveis 5–7 são a materialização individual da era agêntica
- [[wiki/concepts/learning-gap-organizacional]] — estudos de 20–30% mediram os níveis errados; explica parte do gap
- [[wiki/concepts/autonomia-tecnica]] — paradoxo: mais delegação exige mais autonomia/conhecimento, não menos
- [[wiki/concepts/dependencia-ia]] — níveis 0–2 como zona de estagnação; nível 3 como primeiro passo real de delegação

---

## Questões em Aberto

1. Quem exatamente é "Steve" (ex-Google, ex-Amazon) que criou o framework? O vídeo não menciona o sobrenome.
2. Os níveis 6 e 7 exigem infraestrutura organizacional (aprovação de multi-agentes, orçamento de tokens) além de skill individual — como isso interage com o [[learning-gap-organizacional]]?
3. Existe framework equivalente para times inteiros (não apenas devs individuais)?
