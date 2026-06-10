---
type: source
title: "Formação IA para Devs — Aula 06: Q&A"
aliases: ["IA para Devs Aula 6", "Q&A Formação IA"]
date_created: 2026-06-02
date_updated: 2026-06-02
source_count: 0
tags: [ia-para-devs, qa, arquitetura, codigo-legado, revisao-de-codigo, junior, seguranca]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/Aula 06 - Q&A.md"
source_url: ""
author: "Rodrigo Branas, Pedro Nauke"
date_published: "2026"
date_ingested: 2026-06-02
---

# Formação IA para Devs — Aula 06: Q&A

## TL;DR

Sessão de perguntas abertas cobrindo: revisão de código com IA (ainda fazemos, mas de forma diferente), por que boas práticas de arquitetura continuam relevantes (e talvez sejam mais importantes), como lidar com sistemas legados grandes, o futuro dos desenvolvedores juniores, e como a linguagem Go se sai bem no contexto de IA por ter escopo fechado e baixa ambiguidade.

## Key Claims

- **Revisão de código não desaparece — muda de nível**: Pedro revisa PRs, mas não olha linha a linha; confia no pipeline (testes, E2E, rules, skills). Em projetos críticos (checkout), lê tudo. Em projetos com baixo risco, não lê. Evidência: Pedro descreve seu workflow real com o Compose.
- **Boas práticas de arquitetura são MAIS importantes com IA, não menos**: arquivos pequenos e coesos, DDD, inversão de dependência, single responsibility — tudo isso facilita o trabalho do LLM. Evidência: argumento de Pedro + Branas sobre arquivos grandes vs muitos arquivos pequenos.
- **"Mais token" ≠ "clean architecture é ruim"**: ter muitos arquivos não é problema. O problema é arquivos grandes. O modelo não carrega o projeto inteiro — carrega os arquivos relevantes. Evidência: Branas rebate o mito de que clean architecture desperdiça tokens.
- **Segurança vai crescer em importância**: agentes estão recebendo mais permissões do que nunca. OWASP de agentes é emergente. Evidência: Branas relata crescimento de palestras sobre segurança em eventos de IA.
- **Spec-driven documentation é por tarefa, não uma "living doc" permanente**: a documentação não precisa ser viva/atualizada para sempre. É produzida para guiar uma execução e pode ser descartada depois. Evidência: resposta de Branas ao questionamento de Wanderlei.
- **Sistemas legados: abordagem de referência é melhor que reconstrução do zero**: o LLM trabalha bem com referências existentes (código, regras de negócio). Migração com spec-driven + técnicas corretas deu muito certo na experiência de Pedro. Evidência: Pedro relata migração bem-sucedida de sistema legado "horroroso".
- **Go é a linguagem mais AI-friendly** citada: escopo fechado, erros explícitos, baixa ambiguidade. "O que era ruim para o humano é bom para o LLM." Evidência: Nauke explica mecanismo (menos ambiguidade = menos tokens para interpretar intenção).
- **Tipagem estática reduz custo de inferência**: modelo não precisa rastrear chamadores para saber o tipo do parâmetro. JavaScript puro força o modelo a "ler quem está chamando o método". Evidência: argumento técnico de Branas.
- **Juniors não vão desaparecer, mas a régua subiu**: a fábrica de carro mudou de "100 pessoas martelando" para "1 engenheiro por linha", mas a indústria não desapareceu. O júnior vai ter que se especializar mais rápido. Evidência: analogia de Pedro + observação de vagas no Vale do Silício.
- **Pessoas neurodivergentes podem ter vantagem natural em paralelismo de tarefas** — observação de Branas. Evidência: observação empírica, não claim científico.
- **Maior problema na adoção de IA**: não é o modelo ou o harness — é a falta de contexto, rules, skills e técnica adequada. Sonnet 4.6 + processo correto > GPT-5.5 sem processo. Evidência: Branas responde ao relato de alucinação do Reinaldo.

## Q&A Highlights

| Pergunta | Resposta-chave |
|---|---|
| "Como vocês revisam código sem olhar?" | Revisão no nível de PR, não linha a linha; pipeline automatizado captura o resto |
| "DDD ainda faz sentido com IA gerando código?" | Sim — arquivos coesos são mais fáceis para o LLM ler e reusar |
| "Como fazer para sistema de 6 milhões de pessoas em Natural/ADABAS?" | Quebrar em tarefas pequenas como qualquer sistema grande; spec-driven ajuda na decomposição |
| "O que esperar de juniores no futuro?" | A régua subiu, mas existem vagas; juniores ágeis com IA superam sêniores engessados |
| "Guardar rules/skills localmente sem versionar?" | Não faz sentido — são padrões da equipe, devem estar no repositório |

## Entities

- [[wiki/entities/rodrigo-branas]]
- [[wiki/entities/pedro-nauke]]
- [[wiki/entities/compose-tool]]

## Concepts

- [[wiki/concepts/spec-driven-development]]
- [[wiki/concepts/harness]]
- [[wiki/concepts/novo-perfil-dev-ia]]
- [[wiki/concepts/codigo-legado-ia]]
- [[wiki/concepts/worktree-paralelismo]]
- [[wiki/concepts/niveis-adocao-ia-l0-l4]]
- [[wiki/concepts/prompt-engineering]]

## Open Questions

- Como o spec-driven se comporta em sistemas com dependências externas fortes (ex: integração com DETRAN/Denatran)?
- Existe algum benchmark formal de "LLM-friendliness" de linguagens de programação?

## Raw Quotes

> "Ainda assim, eu acho que boas práticas de design arquitetura seguem sendo absolutamente relevantes, porque a gente ainda usa linguagens." — Pedro Nauke

> "Para LLM o Go fez muito, muito sentido. O que era ruim para o ser humano é bom para o LLM." — Pedro Nauke

> "Código que a gente nem colocou nem playwright, nem figma, nem mais coisas que vão dar condições da LLM validar se o que foi feito está de acordo." — Rodrigo Branas

> "O ser implícito traz muitos resultados ruins. Ela não é porque está dentro do teu código que ela tem ideia do que você está falando." — Pedro Nauke
