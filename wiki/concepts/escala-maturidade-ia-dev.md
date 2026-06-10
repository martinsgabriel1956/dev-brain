---
type: concept
title: "Escala de Maturidade de IA para Devs"
aliases: ["7 níveis de uso de IA", "escala de Steve", "niveis ia engenheiro", "maturidade ia dev"]
date_created: 2026-06-01
date_updated: 2026-06-01
source_count: 1
tags: [carreira, ia-engineering, modelo-mental, maturidade, niveis, delegacao, orquestracao]
skill: tech-mentor-leadership
status: draft
---

# Escala de Maturidade de IA para Devs

Framework de 7 níveis (0–7) que descreve como engenheiros evoluem no uso de IA. **O que muda entre níveis não é a ferramenta — é o modelo mental**: como você pensa sobre o problema e como você usa as ferramentas.

## Os 7 Níveis

### Nível 0 — Negacionista
Não usa IA. Acredita que é hype passageiro ou que escrever código na mão é superior.

**Consequência prática:** os devs ao redor ficam mais produtivos; em comparação, você fica mais lento. Essa posição prejudica a carreira não porque a IA é mágica, mas pelo delta de produtividade relativa.

---

### Nível 1 — Cauteloso
Usa **autocomplete na IDE**. Aceita ou rejeita sugestão por sugestão.

**Uso das capacidades disponíveis:** ~5%.

---

### Nível 2 — Perguntador
Usa **chat de IA para tirar dúvidas**. Essencialmente substituiu o Stack Overflow — mais rápido e contextual.

**Limitação:** você ainda faz 100% do trabalho. A IA só responde perguntas.

---

### ⚠️ Gargalo crítico: transição do nível 2 para o nível 4

A maioria dos devs trava aqui. Nos níveis 0–2, a IA **não mudou fundamentalmente como você trabalha** — você ainda é o único que pensa, decide e implementa.

---

### Nível 3 — Delegador Básico
Pede para a IA **escrever código** — uma função por vez. Copia, cola, adapta manualmente.

É um salto real, mas o ciclo é lento: microgerenciamento de cada linha, validação manual de cada output.

---

### Nível 4 — Diretor *(o salto mais importante)*

O modelo mental muda completamente:

| | Nível 3 | Nível 4 |
|---|---|---|
| O que você pede | "Escreve uma função que valida CPF" | Escreve arquivo de testes com todos os casos e pede para implementar |
| Papel seu | Microgerenciador de código | Especificador de comportamento |
| Papel da IA | Assistente de linha | Implementadora de spec |
| O que você faz depois | Revisa e adapta | Vai para a próxima tarefa |

**Por que a maioria não chega aqui:**
1. **Confiança** para deixar a IA trabalhar sem microgerenciar
2. **Contexto do sistema** para escrever uma spec que faça sentido

**Paradoxo:** o nível 4 exige **mais** conhecimento de domínio do que o nível 3 — mesmo que você esteja delegando mais.

---

### Nível 5 — Orquestrador
Agentes como Claude Code (agent mode), Cursor agent mode.

A IA não só escreve código — **navega o projeto, lê arquivos, roda testes, corrige erros**. Você define a tarefa de alto nível e ela executa.

Modelo mental: **tech lead** dando direção para um júnior.

---

### Nível 6 — Multi-Agentes
**Múltiplos agentes em paralelo**, cada um em uma tarefa diferente.

Referência: Boris Cherny (criador do Claude Code) com 5 terminais abertos, cada agente trabalhando em paralelo.

Modelo mental: **engineering manager** — você gerencia, revisa, prioriza.

---

### Nível 7 — Arquiteto
Raramente toca em código. Define arquitetura, contratos de API, especificações, critérios de qualidade. Os agentes constroem tudo.

**Pré-requisito real:** dominar os seis níveis anteriores. Visão arquitetural de Staff+.

---

## O Paradoxo Central

> Quanto mais alto o nível, **mais skill você precisa** — não menos.

| Nível | Skill adicional necessária |
|---|---|
| 5 | Entender sistemas |
| 6 | Saber gerenciar times |
| 7 | Visão arquitetural de Staff+ |

**Implicação:** A IA amplifica o skill existente. Dev ruim com IA → faz coisas ruins mais rápido. Dev bom com IA → faz coisas muito melhores muito mais rápido.

## Por que Estudos de Produtividade Medem Errado

Estudos que concluem "IA aumenta produtividade em 20–30%" estão medindo os **níveis 1–2**. A diferença entre nível 2 e nível 4 com a mesma ferramenta é de **~5x** — não por velocidade de digitação, mas por diferença fundamental no tipo de trabalho.

Ver [[learning-gap-organizacional]] para a dimensão organizacional desse mesmo problema.

## Como Progredir

- **Preso no nível 2?** → Delegue uma tarefa inteira: escreva a spec e deixe a IA escrever os testes.
- **Preso no nível 3?** → Escreva uma spec completa para a próxima feature; defina os testes primeiro.
- **No nível 4?** → Use Claude Code por uma semana numa tarefa real; não microgerencie cada arquivo.

**Regra:** não pule níveis. Cada um exige o modelo mental do anterior.

## Relação com outros conceitos

- [[era-agentica]] — níveis 5–7 são a materialização individual da era agêntica
- [[learning-gap-organizacional]] — estudos de 20–30% mediram os níveis errados
- [[autonomia-tecnica]] — o paradoxo do nível 4: mais delegação exige mais autonomia e conhecimento
- [[dependencia-ia]] — níveis 0–2 são a zona onde a relação com IA permanece passiva
- [[rpi-workflow]] — o RPI é a implementação prática dos níveis 4–5

## Key sources

- [[wiki/sources/escala-niveis-uso-ia-engenheiros]] — framework completo dos 7 níveis; paradoxo de skill; gargalo nível 2→4
