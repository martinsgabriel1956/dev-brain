# Avaliação de Skills com o Skill Creator: Otimização de Description e Benchmark com/sem Skill

Transcrição de vídeo/aula em PT-BR em que o apresentador explica a estrutura de uma skill (pasta `skills/` dentro de `.claude/` ou `.agents/`, um `SKILL.md` com front matter `name` + `description` e corpo de instruções, mais `references/` e `scripts/`) e demonstra, com resultados já rodados, como usar a skill **skill-creator** (da Anthropic) para **avaliar** skills: (1) otimização automática da `description` por loop de queries "should trigger / should not trigger" e (2) benchmark qualitativo **com skill vs. sem skill** em modelos diferentes (Haiku vs. Opus), com relatório de grades por asserção. Autor e canal não informados. Já em português — sem tradução. Título derivado do conteúdo. A transcrição termina no meio da frase final ("…minimamente parecida para todos os as pessoas do meu Sim") — **truncada**.

> **Nota de limpeza:** a transcrição automática corrompeu vários termos, corrigidos por contexto: "ponto cloud" / "cloud code" → `.claude` / Claude Code; "skill.m" → `SKILL.md`; "front" → front matter (frontmatter); "Antropic" → Anthropic; "Skill Creator" / "SK Creator" / "Screill Creator" → skill-creator; "room runlup.p pai" → provavelmente `run_loop.py` (script do skill-creator); "quer optim optimizer" → nome da skill do autor (provavelmente um "query optimizer" de SQL; **incerto**); "Haiko" / "Raico" → Haiku; "OPOS" / "Opus" → Opus; "assado crítico" → provavelmente "resultado crítico"/"insight"; "benchm" → benchmark; "Ricardo / Johnny / Wesley" → nomes de colegas hipotéticos usados como exemplo (Claude Code / Codex / OpenCode); "queries opa uma query" → queries; "grades" mantido (nome do artefato do eval). Vícios de fala (é, ã, né, tá, "galera", "pessoal") removidos e pontuação reorganizada; o conteúdo não foi alterado.

## Estrutura de uma skill

Geralmente há um diretório `.claude` no projeto e, dentro dele, uma pasta `skills` (se não estiver usando Claude Code, a pasta se chama `agents`). Dentro de `skills/` há uma pasta com o nome de cada skill e, nela, um arquivo único obrigatório: o `SKILL.md`.

O `SKILL.md` tem o **front matter** — com `name` e `description` — e o **body** (corpo), que é a instrução de fato: o que se quer que a IA execute para entregar o resultado. O corpo do exemplo está em português.

Uma skill não tem só o `SKILL.md`: pode ter **referências**. O apresentador mostra uma skill sua de banco de dados com um catálogo de **antipadrões de performance em SQL** (itens a que se deve ou não prestar atenção), e uma segunda skill, também de banco de dados, para **migração de um banco para outro**.

## A skill skill-creator (da Anthropic)

Uma terceira skill mostrada não foi criada pelo autor: é a **skill-creator, da Anthropic**, responsável por **testar as skills**. Tem mais pastas que as skills simples, mas a ideia é a mesma:

- `SKILL.md` como base central, com front matter;
- **scripts determinísticos** que ajudam a obter o resultado proposto;
- **referências** com contexto adicional;
- arquivos extras que garantem o uso da funcionalidade.

Ela é usada para executar o processo de **evaluation**.

## Parte 1 — Otimização da description (loop de queries)

O processo de evaluation é lento no dia a dia, então o apresentador já deixou o histórico rodado. O que ele fez:

1. Pegou uma skill sua (o "query optimizer") e **capou metade da description** de propósito.
2. Pediu: "skill-creator, roda para mim o processo de evaluation com foco na minha description".
3. Através da skill-creator, o Claude Code passou a rodar o arquivo `run_loop.py` (do skill-creator, da Anthropic) e a **iterar** com ele.
4. Havia a description original (a capada). Nesse **loop contínuo**, o modelo foi entendendo a ideia da skill e gerando, em **iterações distintas, descrições distintas**, avaliando o resultado de cada uma.
5. Ao final entregou um "resultado crítico": a **melhor description** encontrada com base em tudo que foi aplicado.

Resultado: a skill que antes tinha a description capada e **não funcionava bem** passou a ser acionada corretamente — o Claude Code entendeu a demanda e **se autocorrigiu** até atingir o resultado esperado.

Todo o processo é guardado numa pasta chamada **workspace**. Lá há uma pasta `description-optimization` com os **dados usados**: uma lista de **queries com o parâmetro `should trigger`** (devo chamar a skill ou não), baseada no loop visto rodando. O **log** do loop também fica lá, e é ele que permite entender e validar a melhor description.

## Parte 2 — Avaliação qualitativa do resultado (com skill vs. sem skill)

Além de melhorar a skill, é possível avaliar o **resultado** dela. Essa avaliação pode ser baseada em N parâmetros: **client** usado, **modelo**, **provedor**, **dataset** — várias formas para garantir que o resultado chegue o mais próximo possível do esperado.

Na prática, o apresentador rodou a skill de **migração de banco de dados** de duas formas, **em paralelo**:

- com o modelo **Haiku**;
- com o modelo **Opus**.

Resultados relatados:

- Houve um **delta de 40 pontos** — a diferença do resultado qualitativo. Com Haiku a skill "falhou muitas vezes" a nível qualitativo (resultado final); com Opus o resultado foi diferente.
- Com **Opus**, bateu **100 de 100** **com ou sem skill**: o modelo resolve sozinho, então **não há por que ter a skill** ao usar Opus. O processo de evaluation ajuda a identificar **se uma skill faz sentido ou não** de existir no projeto, porque os modelos hoje estão muito avançados.
- Com o modelo menor (Haiku), a skill se justifica: **com skill ≈ 90% de assertividade; sem skill ≈ 50%**.

O processo **encadeia vários subagentes** que testam, testam e consolidam o resultado. Há pastas de **iterações** (uma para o Haiku, uma para o Opus), e em cada uma há a pasta **com skill** e **sem skill**; no final há o **benchmark**, que consolida a lista de prompts e resultados esperados: o que funcionou e o que não funcionou. Sem a skill (Haiku) houve falhas em vários itens (3, 3, 4 e 2 itens nos casos listados), somando os ~40 pontos de falha; com Opus tudo funcionou muito bem. O sumário também traz "o que aprendemos" — se a skill vale mais no modelo menor ou não.

### Relatório e sumário executivo no browser

Além do resumo no chat, há um **relatório** e um **sumário executivo** abertos no navegador (mostrado para o processo de migração). Para cada caso aparece a **resposta dada ao prompt** e os **grades** (o set list / dados de asserções): dá para ir **item a item** entendendo o que falhou e **por que falhou**. Exemplo: o primeiro caso passou 5 de 5; outro passou apenas 2 e falhou 3. Entender o porquê da falha permite **voltar à skill e melhorá-la progressivamente todos os dias**.

## Conclusão do apresentador

A skill, apesar de estar "fora do hype", é **muito utilizada e super importante**: sem ela, **processos de workflow mais estruturados se tornam impossíveis** hoje. É preciso entender **como estruturar, por que estruturar e como funciona** — inclusive a nível de comportamento em **N modelos**. A razão: a ideia de ter um workflow é garantir que ele funcione **em N locais**, porque os membros do time têm preferências pessoais — o Ricardo gosta de usar o Claude Code, o Johnny o Codex, o Wesley o OpenCode — e a experiência deve ser **minimamente parecida para todas as pessoas do time**. *(Transcrição truncada nesse ponto.)*
