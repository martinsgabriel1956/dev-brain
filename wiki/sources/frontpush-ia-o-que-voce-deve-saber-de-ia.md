---
type: source
title: "FrontPUSH, módulo de IA: o que você deve saber de IA? (parte 1)"
aliases: ["o que você deve saber de IA", "o que é a IA FrontPUSH", "hierarquia da IA do Násser", "módulo de IA FrontPUSH aula teórica 1"]
date_created: 2026-11-24
date_updated: 2026-11-24
source_count: 0
tags: [inteligencia-artificial, sistema-especialista, machine-learning, redes-neurais, deep-learning, llm, probabilidade, engenharia-de-features, spam, fundamentos, ia]
skill: tech-mentor-ai
status: draft
source_file: "/home/nemomartins/Documentos/new/dev-study/raw/frontpush-ia-o-que-voce-deve-saber-de-ia.md"
source_url: ""
author: "Násser"
date_published: ""
date_ingested: 2026-11-24
---

# FrontPUSH, módulo de IA: o que você deve saber de IA? (parte 1)

## TL;DR

Aula teórica do módulo de IA do [[wiki/entities/frontpush|FrontPUSH]], com cerca de 16 min e três slides ("O que é a IA?", pt. 1 a 3). [[wiki/entities/nasser|Násser]] a chama de "segunda aula do módulo", mas o arquivo vem numerado 01. A primeira é provavelmente [[wiki/sources/frontpush-ia-como-eu-crio-imagens-e-videos-com-ia]] (inferência). A tese é que **"a IA é probabilidade"**: ela não pensa nem entende, e só parece inteligente porque junta muito poder computacional, muitos dados e um bom modelo de probabilidade da próxima palavra. A aula monta a [[wiki/concepts/inteligencia-artificial|hierarquia]] IA ⊃ [[wiki/concepts/machine-learning|ML]] ⊃ [[wiki/concepts/rede-neural-artificial|redes neurais]] ⊃ [[wiki/concepts/deep-learning|deep learning]] ⊃ [[wiki/concepts/llm-large-language-model|LLMs]]. Depois percorre a evolução como uma cadeia de barreiras. Regras escritas à mão ([[wiki/concepts/sistema-especialista]]) exigem "milhões de regras". O ML aprende padrões dos dados, mas o humano escolhe as features ([[wiki/concepts/engenharia-de-features]]). As redes neurais ajustam os pesos sozinhas, mas pedem muitos parâmetros. O deep learning empilha camadas e esbarra em recurso: GPUs, Big Data e arquiteturas. Transformers, LLMs, [[wiki/concepts/harness]] e [[wiki/concepts/agente-ia|agentes]] ficam para a próxima aula. A sequência didática está certa na hierarquia. Algumas explicações de mecanismo não estão: a curva de Gauss no filtro de spam, o humano que "dá os pesos" no ML e as regras chamadas de "probabilidades" (ver Contradições).

## Key Claims

### O que é IA, e por que "parece inteligente"

- **Definição (slide):** "É qualquer sistema que executa tarefas que normalmente exigiriam inteligência humana." Exemplos: reconhecer voz, jogar xadrez, dirigir carro, traduzir texto, detectar fraude, conversar.
- **"IA é simplesmente probabilística" (slide):** "não pensa, nem sente", "não é 'inteligente'" e "não entende como um ser humano". Ela "só é inteligente porque ela tem uma alta capacidade computacional", muitos dados da internet e um modelo que calcula "a probabilidade da próxima palavra" a cada iteração ([[wiki/concepts/llm-large-language-model]], [[wiki/concepts/determinismo-vs-probabilismo-em-ia]]).
- **Argumento retórico:** com o poder de "ler várias coisas em milésimos de segundo" e com a internet, "você erraria muitas coisas?". O hardware, "está tudo na faixa dos gigahertz".
- **"Mas IA NÃO significa necessariamente aprendizado" (slide, em destaque).** Sistemas de regras também contam como IA.
- **Tipos (slide):** IA tradicional, Machine Learning, Deep Learning, IA Generativa, LLMs. **Evolução (slide):** 1. sistemas baseados em regras, 2. ML, 3. redes neurais, 4. deep learning, 5. Transformers, 6. LLMs, 7. Harness, 8. Agentes/autonomia. O último item é "o ponto que a gente está", "a grande virada de chave" no mercado, fruto do "acumulado de todos esses conceitos".

### A hierarquia correta

- "Tem todo um iceberg por dentro." Slide: "LLM é um tipo de Deep Learning; Deep Learning usa Redes Neurais; Redes Neurais faz parte de Machine Learning; Machine Learning é uma área da IA" ([[wiki/concepts/inteligencia-artificial]]).

### 1ª geração: sistemas baseados em regras

- "É o que a gente faz em if else." Exemplo do slide: "SE temperatura > 30 ENTÃO ligar ventilador" ([[wiki/concepts/sistema-especialista]]).
- Dá para fazer algo que "parece inteligente" com um "if else dentro de if else gigantesco", mas "você teria que programar milhões de regras" (slide, em vermelho). O limite vem da "quantidade de parâmetros", do "erro humano" e da "quantidade de conhecimento".
- Ele descreve o if/else como "traçando possibilidades, lembre-se, probabilidades de uma determinada ação". Ver Contradições.

### 2ª: Machine Learning

- "Em vez de programar regras... o sistema aprende padrões sozinho através de dados" (slide) ([[wiki/concepts/machine-learning]]).
- **Exemplo do spam.** Método antigo: "programar palavras proibidas manualmente" num if/else que precisa ser atualizado a cada golpe novo. Com ML, "mostrar milhões de emails", e o modelo percebe "certas palavras", "certas estruturas" e "certos comportamentos" (slide). Isso vai para o [[wiki/entities/google|Google]], e o [[wiki/entities/gmail|Gmail]] avisa: "muito provavelmente isso aqui é um spam".
- Mecanismo descrito: "uma distribuição [...] como se fosse uma curva de Gauss, depois pesquisem aí", em que uma área da curva concentra as palavras típicas de spam. Ver Contradições.
- Mesmo padrão nos avisos de fake news "nas eleições passadas" ("verifique as fontes confiáveis, pode ter conteúdo de inteligência artificial").
- **Modelos (slide, em verde):** regressão linear, árvores de decisão, random forest, SVM, clustering ([[wiki/concepts/modelo-de-machine-learning]]).
- **Limitação (slide pt. 3):** "Humanos precisavam dizer quais características importar." Para reconhecer rosto: distância entre os olhos, formato do nariz, contorno facial; "o humano escolhia as features" ([[wiki/concepts/engenharia-de-features]]). Na fala, o humano também "tem que colocar qual é o parâmetro que pesa mais, o que pesa menos". Ver Contradições.

### 3ª: Redes neurais

- "Tentam imitar parcialmente o cérebro humano. Não biologicamente... mas matematicamente" (slide). "Cada conexão possui um peso matemático; durante o treinamento os pesos são ajustados e a rede aprende relações" ([[wiki/concepts/rede-neural-artificial]]).
- Vêm "para tentar ultrapassar essa barreira": "automatizar, melhorar, otimizar essa parte do peso matemático". Padrões de peso alto concatenados dão "uma chance maior".
- **Barreira:** "Pra ser bom, precisa de muitos parâmetros. Para ter muitos parâmetros precisa de muito recurso" (slide). O exemplo é o golpe por e-mail, que "todo dia" inova, "principalmente no Brasil".

### 4ª: Deep Learning

- "'Deep' = múltiplas camadas neurais" (slide): "eu continuo aplicando a rede neural [...] só que agora eu aplico diversas camadas" ([[wiki/concepts/deep-learning]]).
- **"A principal barreira do Deep Learning é recurso":** Big Data ("uma quantidade enorme de dados"), arquiteturas e modelos, e [[wiki/concepts/gpu|GPUs]] ("poder computacional, de fato"). Slide: "Deep Learning consome recurso, agora o hardware consegue fornecer esse recurso".
- É por isso que "a inteligência artificial deu o boom". A aula termina aqui e a continuação (Transformers em diante) fica "para a próxima aula".

## Contradições e precisões

- **"IA é probabilidade" × a 1ª geração.** Sistemas de regras são **determinísticos**: mesma entrada, mesma saída. O if/else enumera *possibilidades*, não calcula *probabilidades*, e o próprio slide diz que IA não implica aprendizado. A tese vale para ML e LLMs, não para toda a IA. [[wiki/concepts/determinismo-vs-probabilismo-em-ia]] já registra o contraste. [skill: tech-mentor-ai] O guia "AI vs Rule-based" recomenda regras justamente quando a saída precisa ser "auditável e determinística". Confiança alta.
- **Spam e "curva de Gauss".** O filtro estatístico clássico de spam é o **Naive Bayes**. Ele calcula a probabilidade de spam por palavra e as combina; não procura uma área de uma normal. [external] Paul Graham, "A Plan for Spam" (2002), http://www.paulgraham.com/spam.html. O Gmail usa ML desde cedo e, em 2019, o Google anunciou bloquear mais 100 milhões de spams por dia com TensorFlow. [external] https://workspace.google.com/blog/product-announcements/ridding-gmail-of-100-million-more-spam-messages-with-tensorflow. Confiança alta no Naive Bayes e média-alta no número do Google (sem fetch).
- **Quem define os pesos no ML clássico.** O humano escolhe as **features**, mas os **pesos** são aprendidos no treino: é isso que "aprender com dados" significa, também na regressão linear do próprio slide ([[wiki/concepts/modelo-de-machine-learning]]). O que as redes profundas automatizaram foi a **extração de features** (*representation learning*), não o ajuste de pesos. [external] Bengio, Courville e Vincent, "Representation Learning: A Review and New Perspectives" (2013), https://arxiv.org/abs/1206.5538. Confiança alta. O slide ("o humano escolhia as features") está certo; a fala mistura features com pesos.
- **Ordem didática não é cronológica.** O Perceptron é de 1958 ([[wiki/concepts/rede-neural-artificial]]), anterior ao SVM (anos 90) e ao random forest (2001). Ou seja, "regras → ML → redes neurais" é uma escada conceitual, não histórica. Concorda com [[wiki/sources/10-conceitos-fundamentais-ia-moderna-bernardo-lobato]] na hierarquia.
- **"Tudo na faixa dos gigahertz."** O clock de GPU fica em torno de 1 a 2 GHz desde a década passada. O que explodiu foi o **paralelismo** (milhares de núcleos, FLOPs) e a largura de banda de memória ([[wiki/concepts/gpu]]). Confiança alta. Lapso retórico, não muda a tese.
- **"Não entende" × interpretabilidade.** [[wiki/concepts/llm-large-language-model]] já registra que a Anthropic encontrou planejamento interno antecipado. "Prevê a próxima palavra" descreve o laço de geração, não esgota o mecanismo.
- **Lapsos de fala mantidos no raw:** "Cai no else, então não está menor que 30" (o else de `> 30` é "não está maior"); "concorda com mim"; "para uns impossível".

## Entities

- [[wiki/entities/nasser]]: instrutor.
- [[wiki/entities/frontpush]]: curso, módulo de IA.
- [[wiki/entities/google]], [[wiki/entities/gmail]]: exemplo do filtro de spam.

## Concepts

- [[wiki/concepts/inteligencia-artificial]] (definição e hierarquia)
- [[wiki/concepts/sistema-especialista]] (1ª geração, if/else)
- [[wiki/concepts/machine-learning]], [[wiki/concepts/modelo-de-machine-learning]]
- [[wiki/concepts/engenharia-de-features]] (limitação do ML)
- [[wiki/concepts/rede-neural-artificial]], [[wiki/concepts/deep-learning]], [[wiki/concepts/gpu]]
- [[wiki/concepts/llm-large-language-model]], [[wiki/concepts/determinismo-vs-probabilismo-em-ia]], [[wiki/concepts/ia-generativa]]
- Só citados (próxima aula): [[wiki/concepts/transformer-architecture]], [[wiki/concepts/harness]], [[wiki/concepts/agente-ia]]

## Open Questions

- Continuação: [[wiki/sources/frontpush-ia-o-que-sao-as-llms]] (parte 2: Transformers e LLMs; "harness" redefinido como arquitetura do modelo). A parte 2 vai cobrir Transformers, LLMs, harness e agentes. Vai também corrigir a tese da "IA = probabilidade" para a IA de regras?
- Que critério separa "harness" de "agentes/autonomia" na escada dele? Na wiki, [[wiki/concepts/harness]] já inclui o laço do agente.
- A numeração do módulo: "segunda aula" na fala, arquivo 01.

## Raw Quotes

- "A IA é probabilidade e eu estou afirmando isso para vocês."
- "Se você tirar as bases da Inteligência Artificial, ela vira burra, ela não sabe mais o que ela faz."
- "Você teria que programar milhões de regras, você precisaria fazer um if else dentro de if else gigantesco."
- "O ser humano que escolhe as features, então não é uma inteligência artificial em si."
- "A principal barreira do Deep Learning é recurso."
