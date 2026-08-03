---
type: source
title: "As 5 Escolas de Como Programar com IA"
aliases: ["5 escolas de ia", "autonomy slider karpathy", "automatic programming vs vibe coding antirez", "escolas de programação com ia"]
date_created: 2026-08-03
date_updated: 2026-08-03
source_count: 0
tags: [vibe-coding, spec-driven-development, agentes-ia, harness, loop-engineering, karpathy, dhh, antirez, peter-naur, comprehension-debt, carreira]
skill: tech-mentor-ai
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/cinco-escolas-programacao-com-ia.md"
source_url: ""
author: "Mano Deivin (canal de YouTube)"
date_published: ""
date_ingested: "2026-08-03"
---

## TL;DR

Vídeo em português (transcrição automática, sem necessidade de tradução) do canal Mano Deivin mapeando **cinco "escolas" de pensamento** sobre como programar com IA em 2026, organizadas ao longo do **"autonomy slider"** de [[wiki/entities/andrej-karpathy]] (quanto de autonomia/rédea se dá à IA): (1) IA como copiloto — humano dirige, IA sugere (Cursor/GitHub Copilot); (2) delegação total a agentes — dev vira "gerente"/"babá de agente" (Claude Code, AMP, spec-driven development); (3) "na unha" — sem IA, fundamentada na tese de 1985 de [[wiki/entities/peter-naur]] de que um programa é uma teoria mental, não código; (4) o loop — agente rodando sozinho, sem supervisão, até passar nos testes (Ralph Loop / "Half Wigun" de [[wiki/entities/geoffrey-huntley]]). O argumento central do vídeo é que **duas referências que defendiam publicamente "fazer tudo na unha" — [[wiki/entities/dhh]] e [[wiki/entities/antirez]] — trocaram de lado publicamente em menos de 12 meses**, o que o autor usa para argumentar que não existe consenso na indústria e que ninguém deveria se sentir "burro" por estar confuso. Antirez, ao trocar de lado, preserva uma distinção entre **"automatic programming"** (usar agente com direção e critério — o código continua sendo seu) e **vibe coding** (aceitar sem entender — "despachante de código"). Fecha com a crítica de que usar IA como muleta (sem entendimento crítico) é o erro real, não a ferramenta em si.

---

## Claims Principais

### 1. O "autonomy slider" de Karpathy organiza as cinco escolas num único eixo
**Evidência:** Karpathy descreve um controle deslizante contínuo (como volume de rádio) que regula o quanto de autonomia se delega à IA — do mínimo (só sugestão) ao máximo ("faz o que você quiser"). O autor do vídeo posiciona cada uma das cinco escolas como um ponto diferente nesse slider, argumentando que nenhuma delas é "a certa" isoladamente.
**Confidence:** Média-alta — framing citado de segunda mão (o autor não cita a fonte primária exata de Karpathy), mas coerente com a tese já documentada de Karpathy em [[wiki/concepts/paradigmas-interface-llm]] sobre autonomia crescente de LLMs.

### 2. Escola 1 (copiloto) ainda tem defensores ativos, apesar de "parecer" datada
**Evidência:** Ferramentas como Cursor e GitHub Copilot mantêm o modelo humano-no-controle, revisão sugestão-a-sugestão. O autor observa que, apesar de essa escola parecer "coisa de 2023", segue tendo adesão ativa em 2026 — citando um comentário atribuído a [[wiki/entities/fabio-akita]] de que essa abordagem já estaria "datada".
**Confidence:** Média — a observação de que a escola persiste é do próprio autor; a citação a Akita é de segunda mão e sem contexto completo, marcada como `[transcrição incerta]` no `raw/`.

### 3. Escola 2 (delegação total) tem defensores citando 70-80% do código gerado por agente
**Evidência:** Citação atribuída a Thorsten Ball (criador do agente AMP): "o agente escreve uns 70-80% do código, eu só faço commit." Citação atribuída a Steve Yegge sobre o dev virar majoritariamente "babá de agente".
**Confidence:** Média — citações de terceiros repassadas pelo autor do vídeo, sem link para a fonte primária; nomes próprios com grafia incerta na transcrição automática.

### 4. Sean Grove (OpenAI): a especificação é o artefato valioso, o código é uma projeção dela
**Evidência:** Citação atribuída a Sean Grove como justificativa para a variante spec-driven da Escola 2 — o documento de especificação importa mais que o código gerado a partir dele.
**Confidence:** Média — citação de segunda mão, sem fonte primária linkada; conceitualmente consistente com a tese já documentada de [[wiki/entities/pedro-nauke]] em [[wiki/concepts/spec-driven-development]] ("PRD não é um documento feito para a empresa, é um documento feito para a IA").

### 5. DHH trocou publicamente de "anti-agente raiz" para "agent first" em ~6 meses
**Evidência:** Citações atribuídas a DHH em 2025 ("sinto a competência escorregando para fora dos dedos", comparação com nunca aprender violão) vs. citações atribuídas a ele ~6 meses depois ("agente first" em toda tarefa, código na mão é "tedioso", usar agente é "vestir uma armadura").
**Confidence:** Média — citações de segunda mão repassadas pelo autor, sem link direto às fontes primárias (posts/vídeos originais de DHH); mas o padrão de virada de posição é coerente com o perfil já documentado de [[wiki/entities/37signals|37signals/DHH]] como adotante tardio, porém decidido, de mudanças de infraestrutura.

### 6. Antirez publicou "não use agente" no início de 2026, depois reverteu e cunhou "automatic programming"
**Evidência:** Post atribuído a Antirez (criador do Redis) argumentando que agentes deixam a base de código "frágil e inchada"; pouco depois, post revertendo a posição ("recusar usar agente não vai ajudar você nem sua carreira"), adoção do Claude Code, e o termo "automatic programming" para descrever uso de agente com direção/critério — distinto de vibe coding (aceitar sem entender).
**Confidence:** Média — mesma limitação das demais citações (segunda mão, sem link primário), mas é o claim mais central e mais detalhado do vídeo, com uma distinção conceitual (automatic programming vs. vibe coding) reaproveitável independentemente da precisão biográfica exata.

### 7. Peter Naur (1985): um programa não é o código, é uma teoria que vive na mente de quem o construiu
**Evidência:** Citação da tese de "Programming as Theory Building" como base filosófica da Escola 3 (na unha) — um agente de IA nunca constrói essa teoria, ela "vive" dentro da janela de contexto e se perde.
**Confidence:** Alta — corrobora, sem contradição, a tese já documentada de forma mais completa em [[wiki/concepts/teoria-do-programa-naur]] a partir de [[wiki/sources/cognitive-debt-margaret-storey]]; esta fonte chega à mesma tese de forma independente, aplicada especificamente ao debate de "escolas de IA" em vez de dívida cognitiva de time.

### 8. Addy Osmani (Google) chama esse mesmo fenômeno de "dívida de compreensão"
**Evidência:** Citação atribuída a Addy Osmani como o termo mais recente para a perda de teoria mental do programa quando o código é gerado por agente.
**Confidence:** Alta — corrobora diretamente [[wiki/concepts/comprehension-debt]], já documentado a partir de [[wiki/sources/addy-osmani-80-problem-agentic-coding]]; nota de precisão: a fonte já existente na wiki atribui a cunhagem do termo a Jeremy Twei, não a Osmani — Osmani é quem popularizou/escreveu sobre o conceito, não necessariamente quem o cunhou. Ver contradição registrada abaixo.

### 9. Peter Naur morreu em 2016; os fundadores vivos da Escola 3 migraram de lado
**Evidência:** Argumento do autor de que a Escola 3 ("na unha") está órfã: seu fundamento teórico mais citado (Naur) morreu antes do boom de LLMs agênticos, e os defensores contemporâneos mais visíveis (DHH, Antirez) migraram para escolas mais autônomas.
**Confidence:** Média-alta como observação estrutural (datas de morte e posições públicas são verificáveis), mas o enquadramento de "escola órfã" é interpretação do autor, não fato objetivo.

### 10. Escola 4 (loop sem supervisão) usa o método "Half Wigun" de Jeffrey/Geoffrey Huntley
**Evidência:** Descrição de um agente rodando em loop infinito a noite inteira até passar nos testes, com argumento comercial de custo por hora (US$ 10-42/hora, citado com incerteza) comparado a um salário de atendente de fast food.
**Confidence:** Baixa-média — nome próprio, valor em dólares e nome do método todos marcados como incertos na transcrição; mas o mecanismo descrito (loop sem intervenção humana até condição de parada) é consistente com [[wiki/concepts/ralph-loop]], já documentado nesta wiki e atribuído ao mesmo autor ([[wiki/entities/geoffrey-huntley]]).

### 11. Usar IA como "muleta" (sem visão crítica) é o erro real, não a ferramenta
**Evidência:** Resposta do autor a uma pergunta de audiência ("para que vou aprender a programar se o Claude Code sabe tudo?"): "se o Claude Code sabe tudo que você sabe, então ninguém precisa de você" — sem visão crítica para identificar alucinação da IA, o mercado "cospe" o profissional de volta.
**Confidence:** Alta como opinião consistente com múltiplas fontes já na wiki sobre o mesmo ponto (ex.: [[wiki/concepts/vibe-coding]], [[wiki/concepts/pensamento-critico]]); é uma tese de opinião, não um dado verificável.

---

## Entidades Mencionadas

- [[wiki/entities/andrej-karpathy]] — autor do framework "autonomy slider" citado como organizador das cinco escolas
- [[wiki/entities/peter-naur]] — base teórica da Escola 3 ("na unha"), "Programming as Theory Building" (1985)
- [[wiki/entities/geoffrey-huntley]] — método de loop sem supervisão da Escola 4 ("Half Wigun" / Ralph Loop)
- [[wiki/entities/fabio-akita]] — citado de passagem sobre a Escola 1 (copiloto) estar "datada"
- [[wiki/entities/dhh]] — virada de "anti-agente raiz" para "agent first" em ~6 meses
- [[wiki/entities/antirez]] — virada de "não use agente" para "automatic programming"; distinção automatic programming vs. vibe coding
- [[wiki/entities/thorsten-ball]] — criador do agente AMP, citado com "70-80% do código gerado por agente"
- [[wiki/entities/steve-yegge]] — citado sobre dev virar "babá de agente"
- [[wiki/entities/sean-grove]] — citado sobre especificação como artefato valioso, código como projeção
- [[wiki/entities/mano-deivin]] — autor/canal do vídeo

## Conceitos Tocados

- [[wiki/concepts/vibe-coding]] — distinção de Antirez entre automatic programming (direção/critério) e vibe coding (aceitar sem entender)
- [[wiki/concepts/spec-driven-development]] — variante madura da Escola 2, citação de Sean Grove como reforço
- [[wiki/concepts/teoria-do-programa-naur]] — base filosófica independente da Escola 3, mesma tese de Naur aplicada ao debate atual de "escolas de IA"
- [[wiki/concepts/comprehension-debt]] — citado sob o nome "dívida de compreensão", atribuído por esta fonte a Addy Osmani
- [[wiki/concepts/ralph-loop]] — mecanismo da Escola 4, mesmo autor (Geoffrey Huntley) já documentado
- [[wiki/concepts/niveis-adocao-ia-l0-l4]] — paralelo estrutural: ambos os frameworks tentam categorizar posições de adoção de IA num espectro, embora com eixos diferentes (níveis vs. slider de autonomia)
- [[wiki/concepts/pensamento-critico]] — crítica final sobre usar IA como muleta

## Armadilhas Documentadas

1. **Citações de segunda mão sem fonte primária** — praticamente todas as falas atribuídas (DHH, Antirez, Thorsten Ball, Steve Yegge, Sean Grove) são repassadas pelo autor do vídeo sem link para post/vídeo original; tratar teor como plausível, não como citação verbatim confirmada.
2. **Nomes próprios com grafia incerta na transcrição automática** — "Thor Torstenbau" (Thorsten Ball), "Steve Egg" (Steve Yegge), "Jeffrey Huntley" (provavelmente Geoffrey Huntley), "Ed osm money" (Addy Osmani), "One tires"/"Antires" (Antirez) — todos resolvidos por contexto, não por confirmação direta.
3. **Atribuição de cunhagem de termo pode estar imprecisa** — esta fonte atribui "dívida de compreensão" a Addy Osmani; a wiki já documenta, a partir da fonte primária de Osmani, que o termo foi cunhado por Jeremy Twei e popularizado/escrito por Osmani. Ver contradição abaixo.

## Quotes Valiosas

> "Você até consegue terceirizar o seu pensamento; agora, o seu entendimento, isso não dá para passar pra frente." — atribuída a Andrej Karpathy, parafraseada pelo autor.

> "Recusar usar agente não vai ajudar você nem a sua carreira." — atribuída a Antirez, na virada de posição.

> "Se o Claude Code sabe tudo que você sabe, então ninguém precisa de você." — o autor, em resposta a uma pergunta de audiência.

## Contradições / Questões Abertas

- **Atribuição de "dívida de compreensão"/comprehension debt**: esta fonte atribui o termo a Addy Osmani; [[wiki/sources/addy-osmani-80-problem-agentic-coding]] (já na wiki) atribui a cunhagem a Jeremy Twei, com Osmani como autor do artigo que popularizou o conceito. Não é necessariamente uma contradição factual (cunhar ≠ popularizar), mas fica registrado para não propagar a atribuição errada em fontes futuras.
- Nome exato do canal do autor ("Mano Davi" nesta fonte vs. "Mano Deivin"/"Find My SaaS" em fontes já ingeridas) — a wiki já tem duas páginas de entidade possivelmente duplicadas para o mesmo canal ([[wiki/entities/mano-deivin]] e [[wiki/entities/mano-davin]]); esta fonte foi anexada a `mano-deivin` por ser a mais próxima em conteúdo (carreira/opinião, não segurança), mas a duplicação em si não foi resolvida — sinalizar para lint futuro.
- Valor exato de custo por hora citado para a Escola 4 (US$ 10-42/hora) não confirmado com precisão pela transcrição.
- Nome exato do método da Escola 4 ("Half Wigun") não confirmado — provável trocadilho com "Ralph Wiggum", mas a grafia entregue pela transcrição automática não bate exatamente com esse nome.
