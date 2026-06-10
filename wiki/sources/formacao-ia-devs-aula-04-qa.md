---
type: source
title: "Formação IA para Devs — Aula 04: Q&A (Rules + Skills)"
aliases: ["aula 04 qa formacao", "qa rules skills formacao ia"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [qa, harness, rules, skills, legacy, spec-driven, modelos-open-source, custo]
skill: tech-mentor-ai
status: stable
source_file: /home/nemomartins/Documentos/new/dev-study/raw/Aula 04 - Q&A.md
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: 2026
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 04: Q&A (Rules + Skills)

## TL;DR

Sessão de perguntas práticas sobre harness, modelos e estratégias de uso. Insights principais: para scaffolding, dê o comando CLI ao invés de pedir à LLM que crie do zero; para refactoring legado, spec-driven por módulo é o caminho; caveman-style token reduction não resolve o problema real (são as iterações agênticas, não os tokens de linguagem natural); planos de $20 são inadequados para uso L3+; sistemas grandes precisam de skills por módulo como mapa de navegabilidade.

## Afirmações-chave

| Afirmação | Evidência | Confiança |
|---|---|---|
| Para scaffolding: referenciar o comando CLI oficial é melhor do que pedir LLM criar a estrutura | Rodrigo Branas, caso Flutter | Alta |
| Refactoring de sistema grande: spec-driven por módulo, não o sistema inteiro de uma vez | Pedro Nauke | Alta |
| Caveman/RDK token reduction tem impacto pequeno — o custo real está no loop agêntico | Pedro Nauke | Alta |
| Plano $20 Claude/Codex é inadequado para spec-driven — esgota rapidamente | Pedro Nauke, Rodrigo Branas | Alta |
| Sistemas com 2-3M linhas de código: skills com mapa por módulo + indicar arquivo no prompt | Pedro Nauke (mesma situação no seu projeto) | Alta |
| Claude Code reseta a cada 5h; Cursor e outros consomem crédito sem reset | Rodrigo Branas | Alta |
| Quando seu sistema vira harness (LLM embarcada), você é o responsável pelo system prompt | Rodrigo Branas | Alta |
| OpenCode é o melhor harness para quem quer usar modelos open source | Pedro Nauke | Alta |
| Modelos open source via ZEN plan ($20) são viáveis para tasks boas | Pedro Nauke | Alta |

## Questões e Respostas

### Boilerplate/Scaffolding — Flutter

**Problema:** Pedir à LLM "crie um projeto Flutter" faz ela gerar tudo na mão, queimando tokens e podendo ficar desatualizada.

**Solução:** Seja explícito: "crie o projeto do zero, mas siga rigorosamente o processo de instalação do CLI que gera o boilerplate automaticamente". LLM vai executar o comando correto em vez de reinventar a estrutura.

**Alternativa:** Achar um boilerplate no GitHub e pedir à LLM para instalar/adaptar.

### Refactoring de Sistema QT → Flutter

**Problema:** Sistema legado em QT, quero portar para Flutter. Código ou print de tela para a LLM?

**Resposta:** Os dois. Quanto mais informação, melhor. Processo ideal:
1. Pegar feature de autenticação
2. Criar spec de migração para essa feature (spec-driven)
3. Referenciar arquivos antigos de autenticação + screenshots daquela parte
4. Executar feature por feature, não o sistema inteiro

### Caveman/RDK para Economizar Token

**Problema:** Protocolo de linguagem simplificada para reduzir tokens.

**Resposta:** Impacto pequeno. O maior custo está nas iterações do loop agêntico (todo o contexto é reenviado a cada tool call). Linguagem natural simplificada não muda tool calls, resultados de execução, código gerado. Risco: remover informação importante do contexto.

> "Prefiro garantir. Gastar mais agora para não gastar mais depois."

### Planos e Custos

| Plano | Situação |
|---|---|
| $20 Claude | Reseta, mas esgota rápido com spec-driven; inadequado para L3+ |
| $20 Codex | Similar; ambos forçando usuários para $100 |
| $100 Claude | Reset a cada 5h; limite pouco transparente |
| $100 OpenAI | Melhor limite percebido; menos "sacana" que Anthropic |
| $20 Cursor | Crédito; quando acaba, acabou |
| Open source via ZEN | $20/mês; boa qualidade; Minimax 2.7 estava free |

Recomendação para quem não pode pagar $100: OpenCode + open source ($40).

### Sistemas Legados com Milhões de Linhas

**Estratégia:**
1. Skills com um arquivo de referência por módulo (mapa de navegabilidade)
2. No prompt: referenciar a skill + dizer qual módulo
3. Indicar o arquivo específico quando souber (Ctrl+F manual é válido)
4. Não existe cache permanente de código — a LLM sempre vai precisar fazer alguma leitura

> "Você vai ter menos tool calls, mas não zero."

### LLM Embarcada no Código (LangChain, etc.)

**Pergunta:** Como funciona o harness quando a LLM está dentro do meu sistema?

**Resposta:** Seu sistema **vira o harness**. Você é responsável por:
- System prompt do agente interno
- Registro de tools
- Loop de execução

> "Quando tu bota LLM dentro do sistema, tu tá criando o teu próprio harness."

### Transferência de Contexto entre Harnesses

**Problema:** Quero alternar Codex/Claude Code quando um esgota, mantendo continuidade.

**Resposta:** Com spec-driven funciona: a spec persiste no arquivo, qualquer harness pode retomar. Sem spec-driven: salvar resumo do contexto em MD é possível mas trabalhoso. Contextos de harnesses diferentes são incompatíveis diretamente.

## Conceitos Mencionados/Reforçados

- [[wiki/concepts/spec-driven-development]] — solução para refactoring, continuidade entre harnesses, transferência de contexto
- [[wiki/concepts/ciclo-agente]] — onde está o custo real (não na linguagem natural)
- [[wiki/concepts/codigo-legado-ia]] — skills por módulo como mapa de navegabilidade
- [[wiki/concepts/harness]] — quando seu sistema embarca LLM, você cria o harness
- [[wiki/concepts/skills-agente]] — mapa por módulo para sistemas grandes

## Entidades Mencionadas

- [[wiki/entities/rodrigo-branas]] — facilitou Q&A; caso pessoal com RP de 5 bilhões de reais
- [[wiki/entities/pedro-nauke]] — respondeu a maioria das perguntas técnicas; tem projeto com 2-3M linhas

## Open Questions

- Qual é o limite exato de tokens no plano $100 do Claude Code (reset a cada 5h)? Anthropic não documenta claramente.
- OpenCode ZEN plan $20 — lista completa de modelos disponíveis e qual está free a cada momento?
