---
type: concept
title: "Robustez de Sistemas"
aliases: ["sistemas robustos", "robustez", "software robusto"]
date_created: 2026-05-31
date_updated: 2026-08-03
source_count: 6
tags: [robustez, arquitetura, qualidade, escalabilidade, testes, segurança, era-agentica]
skill: tech-mentor-backend
status: stable
---

# Robustez de Sistemas

## TL;DR

Conjunto de propriedades que fazem um sistema continuar funcionando corretamente sob carga, mudança, falha e ataque. Na era da IA, tornou-se a **palavra do ano** para devs: a IA acelera a geração de código, mas também acelera a geração de problemas — e manter sistemas robustos exige profissionais experientes que a IA não substitui.

## Por que Agora

> *"Eu tô vendo muito bug, muito problema de quebrar produção, muito sistema caindo que não deveria cair. Muita falha de segurança."*

A [[era-agentica]] criou um paradoxo: nunca foi tão fácil gerar código, e nunca foi tão fácil gerar sistemas frágeis em alta velocidade. [[crud-resolvido|CRUD simples está resolvido]] — o que ficou difícil e valioso é garantir robustez.

## Atributos de um Sistema Robusto

| Atributo | O que significa |
|----------|----------------|
| **Escalabilidade** | Funciona sob carga crescente sem degradação |
| **Boas abstrações** | Interfaces claras que escondem complexidade |
| **Boas boundaries** | Fronteiras bem definidas entre sistemas e módulos |
| **Modularidade** | Componentes independentes e substituíveis |
| **Testabilidade** | Cobertura real, não superficial; [[teste-de-mutacao]] valida os testes |
| **Segurança** | Validada por ferramentas de análise estática, não apenas por intenção |
| **Observabilidade** | Você sabe o que está acontecendo em produção |

## Como Construir com IA

A IA não garante robustez por padrão — ela entrega o que você pediu. Robustez vem do [[harness-de-qualidade]] que você constrói ao redor da IA:

- **TDD**: [[tdd]] via IA gera código que passa em testes antes de ser aceito
- **Linters com boas regras**: a IA segue regras impostas por ferramenta, não só por prompt
- **Análise de complexidade ciclomática**: feedback objetivo sobre manutenibilidade
- **Análise estática de segurança**: não confiar no julgamento da IA sobre segurança
- **Coverage elevado + [[teste-de-mutacao]]**: garantir que os testes realmente testam
- **[[pipeline-de-qualidade]]**: pipeline determinística — passa ou não passa

## Os Erros Estruturais Típicos da IA

- **[[n-plus-one]]**: IA foca na feature, não no padrão de acesso ao banco
- **Deadlocks e concorrência**: entrega a tela pedida sem raciocinar sobre estados concorrentes
- **Segurança omitida**: "você não me pediu para ser seguro"

## O Dev como Orquestrador de Qualidade

O papel muda de *escrever código* para *garantir que o código gerado é robusto*:

```
Aprende o que é código bom
    ↓
Documenta e codifica em ferramentas (harness, pipeline)
    ↓
IA gera código dentro desses padrões
    ↓
Pipeline determina: passa / não passa (determinístico)
    ↓
Dev revisa o que a ferramenta não pega
    ↓
Refina os padrões continuamente
```

## Let it Crash como estratégia de robustez

Uma das estratégias concretas para construir sistemas robustos é o [[let-it-crash]]: em vez de tentar se recuperar de [[excecao-vs-erro|exceções]] imprevisíveis (banco de dados fora, memória esgotada), o sistema executa um [[graceful-shutdown]] controlado e deixa o orquestrador recriar instâncias limpas.

Isso complementa o [[harness-de-qualidade]]: o harness previne que código ruim entre, Let it Crash garante que quando o ambiente falhar, o sistema se comporta de forma previsível.

## Vibe Coding e a Ilusão de Robustez

[[wiki/concepts/vibe-coding|Vibe coding]] entrega bem MVPs e protótipos, mas não robustez por padrão: sustentabilidade a longo prazo, escala e segurança sem brechas exigem julgamento humano sobre arquitetura, integrações e contexto de negócio que um prompt não cobre sozinho. Ver [[wiki/sources/vibe-coding-limites-maturidade-profissional]].

## Sistemas Determinísticos (Juros, Impostos, Folha) Não Toleram "Quase Certo"

[[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] descreve o caso limite da robustez: sistemas corporativos que calculam juros, impostos ou salário precisam gerar o mesmo output para o mesmo input hoje, amanhã e daqui a 5 anos — sem espaço para interpretação. Um teste real do autor (validador de tarefas de COBOL via LLM) mostrou que modelos de IA aprovavam e reprovavam o mesmo tipo de erro de forma inconsistente entre execuções, porque tokenizam e respondem por probabilidade em vez de ler o conteúdo linha a linha. Ver [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] para a distinção central que essa fonte introduz na wiki.

## Confiabilidade como Guarda-Chuva (Visão de SRE)

Framing didático de SRE para "confiabilidade": consistência de dados + durabilidade (dado persistido não se perde) + [[wiki/concepts/tolerancia-a-falha|tolerância a falhas]] + previsibilidade + disponibilidade de recursos (CPU/memória suficientes, não só uptime). Esse guarda-chuva é essencialmente a mesma lista de atributos de robustez desta página vista pela lente de um SRE em vez de pela lente de arquitetura/dev — reforça que "robustez" e "confiabilidade" são o mesmo alvo descrito por papéis diferentes. Ver [[wiki/concepts/sre]] e [[wiki/concepts/planejamento-de-capacidade]].

## Key Sources

- [[wiki/sources/conteudo-tecnico-ia-robustez-sistemas]]
- [[wiki/sources/sre-capacidade-observabilidade-confiabilidade-custo]] — confiabilidade como guarda-chuva (consistência, durabilidade, tolerância a falhas, previsibilidade, disponibilidade de recursos)
- [[wiki/sources/ia-nao-substitui-sistemas-corporativos-deterministicos]] — sistemas determinísticos como o limite estrutural da robustez via IA; caso real de validador LLM inconsistente
- [[wiki/sources/conteudo-tecnico-ia-hype-sistemas-robustos]]
- [[wiki/sources/let-it-crash-nodejs-asynclocalstorage]] — Let it Crash como estratégia de robustez; graceful shutdown em Node.js
- [[wiki/sources/tdd-sdd-bdd-era-ia]] — TDD/SDD impostos via harness aumentam a chance da IA acertar a intenção
- [[wiki/sources/vibe-coding-limites-maturidade-profissional]] — robustez exige julgamento humano sobre arquitetura e contexto de negócio que vibe coding não supre
