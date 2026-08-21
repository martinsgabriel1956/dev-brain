---
type: concept
title: "Context Engineering (nível Harness)"
aliases: ["context engineering harness", "engenharia de contexto", "project knowledge ia"]
date_created: 2026-06-02
date_updated: 2026-08-20
source_count: 9
tags: [context-engineering, harness, rules, skills, project-knowledge]
skill: tech-mentor-ai
status: draft
---

# Context Engineering (nível Harness)

Prática de estruturar e disponibilizar o **conhecimento do projeto** para o agente de forma que ele precise fazer menos exploração e produza resultados mais alinhados. É a evolução do prompt engineering: em vez de instruções por prompt, o contexto relevante é persistente via rules, skills, CLAUDE.md e referências de arquivos.

## A Metáfora da Bússola

A LLM não conhece seu projeto. Sem context engineering, ela é um explorador no mato sem bússola: vai lendo arquivo por arquivo até encontrar o que precisa (7 tool calls para corrigir 1 bug). Com context engineering, ela tem um mapa: "tudo relacionado a desconto está em `src/domain/coupon.ts`; regras de negócio ficam no service; persistência no repository".

## Evolução

```
Prompt Engineering
       ↓
Context Engineering  ← você está aqui
       ↓
Harness Engineering
```

- **Prompt Engineering**: como estruturar um prompt individual
- **Context Engineering**: como gerenciar o que entra no contexto ao longo do tempo e das sessões
- **Harness Engineering**: como montar o ecossistema completo (tools, MCPs, subagents, CI/CD) ao redor do modelo

## Ferramentas de Context Engineering

### Rules (CLAUDE.md / .cursorrules)
Regras de projeto lidas em toda sessão. Ex: "componentes React devem ter no máximo 100 linhas", "regras de negócio ficam no domain model".

### Skills
Conjuntos de instruções para tarefas recorrentes. Ex: skill "criar slide" com todos os modelos de slide possíveis — cada novo slide inicia com contexto limpo mas carrega a skill. Evita repetir instruções em todo prompt.

### MCPs (Model Context Protocol)
Servidores que expõem tools/resources ao agente via protocolo padronizado. Ex: MCP do Figma para acessar designs; MCP do banco de dados para queries; 50+ tools da Adobe (liberadas em 2026).

### Progressive Disclosure
Ver [[wiki/concepts/progressive-disclosure-ia]] — arquivos de contexto por diretório.

### Memória de Longo Prazo
Ver [[wiki/concepts/memoria-de-longo-prazo-ia]] — salvar outputs de research como .md para reusar entre sessões.

## O Fator Decisivo de Qualidade

> "No fim das contas, o resultado vem de modelo, de harness, de técnica, e principalmente da formalização de conhecimento." — Rodrigo Branas

Usar Opus 4.7 ou GPT-5.5 sem context engineering produz resultados mediocres. Usar Kimi K2.6 com bom context engineering pode superar modelos mais caros. **A técnica e o contexto importam mais que o modelo.**

## Sensores vs Guias

O user harness divide-se em duas categorias (Branas, Aula 01 Parte 2):

- **Guias** — antecipam comportamento: rules, skills, MCPs, CLAUDE.md. Ver [[wiki/concepts/sensores-vs-guias]].
- **Sensores** — fornecem feedback: testes, linter, compilador, browser, banco, LLM de revisão.

> "Qualidade dos seus sensores faz a diferença no resultado." — Rodrigo Branas

### Exemplo Didático de Guia Faltando: o Login Sem Redirect

[[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] ilustra concretamente o que acontece quando um guia (a spec, nesse caso) não cobre um comportamento: pedir "implemente um login" sem especificar o que acontece após o sucesso não dá ao agente informação suficiente para saber que deve redirecionar para o dashboard — ele decide "do jeito que achar que é bom". O framework de [[wiki/concepts/criterios-de-uma-boa-spec|7 critérios de qualidade de spec]] dessa fonte existe justamente para fechar esse tipo de lacuna antes da execução.

## Rules vs Skills

| | Rules | Skills |
|---|---|---|
| Carregamento | Sempre inteira no system prompt | Só front-matter; corpo sob demanda |
| Escopo | Global e obrigatório | Contextual e sob demanda |
| Tamanho ideal | < 300 linhas | Sem limite |

Ver [[wiki/concepts/rules-agente]] e [[wiki/concepts/skills-agente]] para detalhes.

## Prompt Caprichado, Resultado Medíocre: Sintoma de Contexto Faltando, Não de Prompt Ruim

[[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] descreve um padrão observado revisando projetos de IA em empresas de portes variados (startup, banco, indústria): times escrevem prompts caprichados e ainda assim recebem resultado medíocre, e o diagnóstico mais comum ("seu prompt está ruim, aprenda a técnica nova") erra o alvo. O caso ilustrativo: um prompt detalhado (idempotência, formato de resposta, tratamento de erro) gerou um serviço de cobrança recorrente limpo e testável — mas que ignorava uma regra de negócio central (cobrança passa obrigatoriamente por fila de auditoria) documentada em um arquivo que nunca entrou na janela do modelo. Refazer custou mais caro que escrever do zero.

Depois de identificar o padrão, o time da fonte parou de mexer no prompt e aplicou os mesmos três movimentos já descritos nesta página — conhecimento implícito virando artefato versionado, divulgação progressiva (mapa antes da rua) e exemplos reais do projeto em vez de descrição abstrata — e o **mesmo modelo, com prompts medianos**, passou a respeitar a regra de auditoria e as convenções do time. A conclusão da fonte reforça a tese central desta página: "nada mudou no modelo, mudou o que ele enxergava".

A fonte também nomeia o efeito colateral do diagnóstico errado: citando Frederick Brooks, chama o "prompt mágico" de reencarnação da busca por bala de prata — otimizar o detalhe (fraseado do prompt) sobre uma fundação que não existe (contexto do projeto).

## Contexto Como Ativo de Longo Prazo

Context engineering não é gerar documentação estática uma vez — é fazer a IA buscar, em tempo real, documentação viva de servidores e bancos de dados da empresa. Em aplicações de grande porte (diferente de uma prova de conceito), cada documento e decisão registrada ao longo do tempo vira um **ativo do projeto**, na mesma lógica de investimento de um teste automatizado: paga-se o custo uma vez, colhe-se o benefício pelo resto do projeto. Ver [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] e [[wiki/concepts/rag-arquitetura-avancada]] para o mecanismo concreto de busca em tempo real.

## Key Sources

- [[wiki/sources/formacao-ia-devs-aula-04-harness]]
- [[wiki/sources/formacao-ia-devs-aula-05-hands-on]]
- [[wiki/sources/context-engineering-codebases-grandes-rpi]]
- [[wiki/sources/formacao-ia-devs-aula-01-context-harness-engineering]]
- [[wiki/sources/formacao-ia-devs-aula-02-rules]]
- [[wiki/sources/formacao-ia-devs-aula-03-skills]]
- [[wiki/sources/8-pontos-arquitetura-de-software-na-era-da-ia]] — contexto (docs, design docs, playbooks) como ativo de longo prazo análogo a teste automatizado; busca de documentação em tempo real vs. estática
- [[wiki/sources/spec-writer-skill-criterios-de-boa-spec]] — exemplo didático de guia faltando (login sem redirect especificado) e framework de 7 critérios para fechar lacunas de contexto numa spec
- [[wiki/sources/engenharia-de-contexto-vs-prompt-engineering-gargalo-real-times-ia]] — caso do serviço de cobrança recorrente (regra de fila de auditoria fora da janela); prompt caprichado + resultado medíocre como sintoma de contexto ausente, não de técnica de prompt; crítica do "prompt mágico" como bala de prata
