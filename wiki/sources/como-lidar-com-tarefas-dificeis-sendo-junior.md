---
type: source
title: "Como Lidar com Tarefas Difíceis Sendo Júnior"
aliases: ["tarefas difíceis dev júnior", "próximo nível tarefas difíceis", "descubra os pontos de alteração"]
date_created: 2026-07-23
date_updated: 2026-07-23
source_count: 0
tags: [carreira, junior, sindrome-do-impostor, decomposicao-de-tarefas, organizacao-pessoal, mentoria]
skill: tech-mentor-leadership
status: stable
source_file: "/home/gabriel-martins/Documentos/dev-brain/raw/como-lidar-com-tarefas-dificeis-sendo-junior.md"
source_url: ""
author: "André Casciotti (canal Próximo Nível)"
date_published: ""
date_ingested: "2026-07-23"
---

## TL;DR

André Casciotti (mesmo autor de [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]]) argumenta que tarefas difíceis parecem mais difíceis do que realmente são para quem é júnior/pleno, porque (a) tarefas realmente complexas naturalmente vão para os seniores, e (b) o estado de "não ter habilidade ainda" é provisório, não permanente — a síndrome do impostor ataca em todos os níveis de carreira, só que com sintomas diferentes. Três técnicas práticas: (1) descobrir pontos de alteração seguindo o fluxo do código desde a ação do usuário, nunca partindo direto do ponto óbvio; (2) dividir tarefas em partes menores até conseguir responder "tenho segurança para fazer isso?" e "consigo dar um prazo?", com o limite de divisão sendo "ainda dá para dividir entre duas pessoas diferentes?"; (3) organizar o trabalho — anotar tudo (preferencialmente em papel), manter lista de subtarefas priorizada, riscar o que foi concluído para ver progresso, e treinar a habilidade de estimar prazos mesmo sem pressão.

---

## Reivindicações Principais

**Claim:** A síndrome do impostor não é exclusiva de quem é júnior — sêniores também a sentem, só que como medo de estar "desatualizado" ou de que o conhecimento acumulado não seja mais suficiente.
**Evidência:** Observação do autor sobre o ritmo de evolução da área de tecnologia gerar, em qualquer nível, a sensação de estar "ficando para trás"; nenhum estudo citado.
**Confiança:** Média-alta — coerente com [[wiki/concepts/sindrome-do-impostor]], que já documenta a variante júnior a partir de outra fonte; aqui o autor generaliza a manifestação também para sêniores, algo não coberto antes na wiki.

**Claim:** Tarefas complexas são atribuídas a seniores por múltiplos motivos que não têm relação com o júnior ser incapaz: são mais interessantes/desafiadoras para quem já domina o básico, o sênior carrega mais responsabilidade formal (e ganha mais por isso), e às vezes o sênior prefere executar ele mesmo a delegar e corrigir depois.
**Evidência:** Raciocínio observacional do autor sobre dinâmica de equipe, sem dado ou estudo — reconhece explicitamente que "depende de empresa para empresa" e que existe sênior que se esconde na própria zona de conforto.
**Confiança:** Média — plausível e alinhado ao raciocínio de [[wiki/concepts/voluntariar-para-desconhecido]] (tarefas desconhecidas/desafiadoras têm valor de carreira), mas é opinião de conteúdo de carreira, não estudo verificável.

**Claim:** Habilidade é adquirida e aprimorável — não é talento nato — mesmo reconhecendo que existem pessoas com aptidão inicial mais alta para programação.
**Evidência:** Analogia com outras profissões (medicina, docência, mecânica) que também têm pessoas com aptidão aparente; nenhum dado, argumento por analogia.
**Confiança:** Alta — reforça diretamente [[wiki/concepts/disciplina-vs-talento]], que já documenta a mesma conclusão a partir de outra fonte independente.

**Claim:** Para descobrir os pontos de alteração de uma tarefa, é preciso começar do começo (a ação do usuário) e seguir o fluxo completo do código até o ponto de alteração — nunca ir direto ao ponto aparentemente óbvio (ex.: buscar direto o texto de uma mensagem de erro).
**Evidência:** Exemplo descritivo: dev busca o texto de uma mensagem com "Ctrl+Shift+F", altera, mas o problema real estava numa regra de negócio anterior à mensagem — que só seria encontrada seguindo o fluxo desde o clique do usuário.
**Confiança:** Alta — mecanismo idêntico ao já documentado em [[wiki/concepts/exploracao-com-intencao]] a partir do Excalidraw, aqui aplicado ao contexto de manutenção/correção (não onboarding), com ênfase adicional em anotar cada trecho entendido do fluxo.

**Claim:** Uma tarefa está dividida no nível certo quando (a) você tem segurança para executá-la como está descrita e (b) você consegue dar um prazo para ela; se não consegue responder as duas, divida em duas partes e repita.
**Evidência:** Analogia entre estimar o tempo de construir uma casa do zero (impossível sem conhecimento) vs. estimar o tempo de pintar uma parede já pronta (possível mesmo sem ser pintor profissional).
**Confiança:** Alta — mecanismo específico e testável, sem contradição com nada já registrado na wiki; complementa [[wiki/concepts/arvore-de-decomposicao]] (decomposição de problemas vagos) com um critério de parada operacional que aquele conceito não define explicitamente.

**Claim:** O limite inferior da divisão de tarefas é "ainda dá para dividir entre duas pessoas diferentes sem gerar conflito de merge" — se não dá, a tarefa já está simples o suficiente e não deve ser mais subdividida.
**Evidência:** Exemplo: duas regras de negócio dentro do mesmo método não podem ser divididas entre duas pessoas sem risco de conflito de merge.
**Confiança:** Média-alta — heurística específica e coerente com a prática de desenvolvimento colaborativo, mas apresentada como regra pessoal do autor, não como prática validada externamente.

**Claim:** Anotar em papel (não só digitalmente) fixa melhor a informação na memória do que anotação puramente digital.
**Evidência:** Afirmação direta do autor, sem estudo citado — reconhece uso complementar de anotações digitais para consulta rápida (busca por texto).
**Confiança:** Baixa-média — **[external]** existe literatura de psicologia cognitiva (ex. Mueller & Oppenheimer, "The Pen Is Mightier Than the Keyboard", 2014) associando escrita manual a maior retenção, mas o vídeo não cita essa pesquisa; tratar como crença pessoal reforçada por evidência externa não verificada nesta fonte.

**Claim:** Uma lista de tarefas visível, com itens riscados conforme concluídos, reduz a ansiedade de "não vai dar tempo" porque fecha os "loops abertos" mentais que ficam martelando enquanto uma tarefa está em andamento.
**Evidência:** Observação pessoal do autor sobre lembrar de trabalho durante atividades não relacionadas (banho, caminhada) — descrita como efeito de "loop aberto".
**Confiança:** Média — **[external]** o mecanismo descrito é equivalente ao Efeito Zeigarnik (tarefas incompletas permanecem mais acessíveis na memória do que tarefas completas), estudado por Bluma Zeigarnik em 1927; o vídeo não usa esse termo nem cita a pesquisa.

**Claim:** Dar um prazo para tarefas mesmo sem pressão externa, e depois comparar com o tempo real gasto, é a forma de treinar a habilidade de estimativa antes de precisar fazê-lo sob pressão (quando o erro custa mais caro e não há tempo de calibrar).
**Evidência:** Contraste com o cenário comum: dev que nunca treinou orçamento é forçado a estimar sob pressão, erra, e não tem tempo de refinar a estimativa no meio da cobrança.
**Confiança:** Média-alta — coerente com a lógica geral de prática deliberada em ambiente de baixo risco, já documentada em [[wiki/concepts/pratica-deliberada]] a partir de outra fonte, aqui aplicada especificamente à habilidade de estimativa de prazo (diferente do escopo de [[wiki/concepts/estimativas-back-of-envelope]], que trata de capacidade/tráfego em system design, não de prazo de entrega de tarefas).

---

## Entidades

- Autor do vídeo, canal "Próximo Nível" → [[wiki/entities/andre-casciotti]]

## Conceitos

- [[wiki/concepts/sindrome-do-impostor]]
- [[wiki/concepts/voluntariar-para-desconhecido]]
- [[wiki/concepts/disciplina-vs-talento]]
- [[wiki/concepts/exploracao-com-intencao]]
- [[wiki/concepts/arvore-de-decomposicao]]
- [[wiki/concepts/estimativas-back-of-envelope]]
- [[wiki/concepts/divisao-de-tarefas-em-partes-menores]] (novo)
- [[wiki/concepts/organizacao-pessoal-do-trabalho]] (novo)
- [[wiki/concepts/estimativa-como-habilidade-treinavel]] (novo)

## Questões em Aberto

- O autor generaliza a distribuição de tarefas difíceis para seniores como padrão de mercado, mas reconhece variação entre empresas e a existência de seniores que evitam desafio por conta própria síndrome do impostor — não há dado que quantifique o quão comum é o padrão descrito.
- A afirmação sobre anotação em papel ser superior à digital é apresentada como fato, mas o vídeo não cita a pesquisa cognitiva que sustentaria essa afirmação — tratada aqui como reforço externo não verificado na própria fonte.
- A regra "divisível entre duas pessoas" como critério de parada da decomposição de tarefas não é comparada com nenhum framework de estimativa/planejamento formal (ex.: INVEST para user stories) — pode ser interessante cruzar com [[wiki/concepts/user-stories]] em ingestão futura.

## Contradições com a Wiki

Nenhuma contradição direta encontrada. Reforça, com nova nuance, [[wiki/concepts/sindrome-do-impostor]] (variante sênior, não documentada antes) e [[wiki/concepts/disciplina-vs-talento]] (segunda fonte independente chegando à mesma conclusão de que habilidade é adquirida, não nata — mesmo padrão de convergência já registrado entre [[wiki/sources/3-dicas-colocar-conhecimento-em-pratica]] e [[wiki/sources/pare-de-terceirizar-suas-decisoes]] sobre leitura não-linear de livros técnicos). O método de rastreamento de fluxo de código ("comece do começo, siga o fluxo, anote") é a mesma técnica central de [[wiki/concepts/exploracao-com-intencao]], mas aplicada a um cenário diferente: aquele conceito nasceu de um contexto de **onboarding** em codebase nova (Excalidraw); esta fonte aplica o mesmo mecanismo a **manutenção/correção de bug** numa codebase já conhecida pelo time — ampliando o escopo de aplicabilidade da técnica sem contradizê-la.

## Citações Preservadas

> "O estado onde você se encontra agora não é fixo, ele não é permanente — o estado onde você se encontra agora é provisório."

> "Você não tem habilidade ainda, você não tem experiência ainda — isso é muito importante de ter em mente."

> "O software não é uma ilha de código isolada onde as coisas funcionam ali e tudo vai dar certo se você alterar."

> "Quando você consegue dar um prazo para alguma coisa é porque você enxerga que aquilo é possível de ser feito."

> "Tira da cabeça e bota no papel, bota numa lista — você vai ver como o negócio flui melhor."

> "Calma, coragem, cara de pau — você vai precisar dos três, mesmo sendo júnior, mesmo sendo inexperiente."
