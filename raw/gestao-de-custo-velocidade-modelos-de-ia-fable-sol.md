---
title: "Fable, Sol e a Gestão de Custo e Velocidade na Escolha de Modelos de IA"
source_url: https://www.youtube.com/watch?v=...
author: desconhecido
date_published: 2026-07-31
date_ingested: 2026-07-31
type: transcript
language: pt-BR
tags: [llm, model-routing, custo, velocidade, anthropic, openai, abacus, artificial-analysis]
---

# Fable, Sol e a Gestão de Custo e Velocidade na Escolha de Modelos de IA

## Transcrição Traduzida

Os modelos da Anthropic e da OpenAI — Fable e Sol, respectivamente — fazem com que a gente tenha que mudar o paradigma, mudar a forma com que a gente utiliza IAs para desenvolver software. Atualmente são os dois melhores modelos do planeta Terra, e eles são os melhores não apenas em termos de capacidade e inteligência: são os maiores em termos de custo também.

Com esses modelos muito melhores que os anteriores, duas coisas passam a ser verdade. Primeiro, eles são capazes de fazer coisas que os outros modelos não eram capazes de fazer. Antes a gente dizia que os modelos de IA conseguiam, sem muitos problemas, fazer tarefas de nível estagiário — bem simples. Agora a gente consegue afirmar que esses modelos têm capacidades que muitas vezes vão se assemelhar a um dev sênior, dependendo da tarefa, do contexto e da supervisão. Não é exagero dizer que esses dois modelos conseguem sim desenvolver tarefas muito complexas — acho que isso é verdade, ninguém vai discordar disso.

### O paradigma antigo: um modelo só, o tempo todo

Até agora, a forma com que eu via quase todo mundo utilizando IA era a seguinte: pessoas mais sênior, com mais dinheiro, com a empresa financiando, pegavam um plano de 200 dólares e perguntavam "qual é o melhor modelo que existe?". A resposta era sempre o modelo de ponta do momento (Opus, em suas várias versões) — e a estratégia virava usar só esse modelo, exclusivamente, o tempo todo. Se a conta estourasse, comprava-se outra conta de 200, gastando 400. Para muita gente isso fazia sentido.

Hoje em dia essa estratégia dificilmente vai funcionar. O Fable e o Sol são caros demais para isso, e além de caros, eles demoram um pouco — são mais lentos. Os modelos menores respondem de maneira mais rápida. Então é inteligente utilizar as coisas de maneira mais otimizada. O tema de hoje é justamente sobre gestão de custo e de velocidade.

### O que o Artificial Analysis mostra

Uma das melhores fontes que a gente tem para comparar modelos de forma independente é o Artificial Analysis, que faz benchmarks de IA de forma independente. Nele dá para ver claramente, como esperado, que os dois melhores modelos em termos de inteligência são o Fable 5 e o GPT 5.6 (Sol) — disparados na frente, com pontuação de 60 e 59 respectivamente, bem maiores que todos os outros.

Só que, olhando a velocidade, eles perdem bastante para outros modelos mais rápidos: o GLM é mais rápido, o Grok é mais rápido, o Gemini Flash é muito mais rápido. E o custo deles é absurdamente mais alto que o dos outros. Por exemplo, o DeepSeek V4 pontua 44 no índice (contra 59-60 do Fable/Sol) — ou seja, é menos inteligente, mas adequado para várias tarefas — e custa cerca de 4 centavos por tarefa, enquanto o custo do Fable por tarefa costuma ser cerca de 70 vezes mais caro.

É conta básica: se o plano é de 200 dólares e você roda o Fable o dia inteiro, 40 horas por semana, o plano estoura rápido.

### A direção do mercado: orquestração de modelos

Uma das direções que o mercado está tomando hoje — e algo que qualquer um pode fazer — é, se a gente caminhar para fazer todo o código com IA (e sejamos sinceros: quase todos os devs com quem eu converso não escrevem mais código, boa parte nem revisa mais código; é assim que o mundo está organizado atualmente), a coisa inteligente a fazer é ter um processo de tomada de decisão sobre o que utilizar em qual momento.

Esse processo de decisão pode ser manual ou pode ser feito também pela própria IA — de modo que, para uma determinada tarefa, se decide quem vai executá-la. Isso vira uma espécie de orquestração de agentes, ou orquestração de modelos, como você quiser chamar.

De início, eu recomendo tomar essa decisão manualmente, testando na prática. No Claude Code, por exemplo, dá para escolher o modelo antes de rodar uma tarefa: para uma tarefa muito difícil, testar o Fable e ver se é adequado; para uma tarefa difícil mas não tanto, tentar Opus, ou Sonnet, e ir vendo o que cada um produz.

Em vídeos anteriores do canal, já foi mostrado como criar uma skill e subagents no Claude Code — e dessa forma é possível fazer uma skill tomar a decisão de qual subagente (e portanto qual modelo) usar. Você pode ter um subagente por modelo, e a skill decide qual modelo é adequado para aquela tarefa, criando um workflow com um processo de decisão que aciona um subagente diferente a depender do nível de dificuldade da tarefa.

### As três variáveis: inteligência, velocidade e custo

O que a maioria das pessoas provavelmente vai acabar fazendo é pensar sempre em três variáveis: inteligência, velocidade e custo.

**Ponta (modelos de fronteira — Fable e Sol):** faz sentido delegar para eles tarefas de alta complexidade, incerteza e desconhecidos — decisões de arquitetura, quebrar uma feature muito complexa em várias tasks menores implementáveis no futuro, bugs que ninguém nunca conseguiu resolver, tarefas em que o objetivo é claro mas o caminho não é. Olhando o coding index do Artificial Analysis, os melhores são GPT 5.6 (Sol), depois Fable, e logo atrás vêm GPT 5.5 e Claude Opus 4.8 — ainda bons candidatos para tarefas de alta complexidade no geral.

**Velocidade (tarefas simples, mas urgentes):** para um bug fix simples que você quer testar rápido e já subir, o Gemini 3.5 Flash é uma boa opção — pontua 70 no coding index do Artificial Analysis, um número bem alto. O DeepSeek pontua 59 e também é bom, mas quem ganha em velocidade mesmo são modelos como o da Nvidia e o Gemini Flash (o GPT-OSS é o mais rápido de todos, mas mais fraco em capacidade).

**Fallback (tarefas simples, sem exigência de velocidade, trabalho em background):** o Sonnet é perfeitamente razoável. Se quiser algo mais barato, o Kimi é uma boa decisão — tem um custo-benefício muito bom — e o DeepSeek também serve para isso.

### Como automatizar essa escolha: roteador customizado na Abacus

Fazer essa escolha manualmente, trocando de harness o tempo todo, não escala bem. Existem formas de automatizar isso. Recomendo mesmo assim começar manual, testando modelo por modelo — pegar a mesma tarefa complexa, rodar no Fable e no Kimi, por exemplo, e comparar: olhar o código, o resultado, screenshots, testes, tempo de execução. O objetivo é você mesmo verificar, não depender só da opinião de quem fala no vídeo.

Depois disso, dá para automatizar. O Claude Code, por si, deixa você mais preso ao ecossistema Anthropic (Fable, Opus, Sonnet, Haiku), mas isso não é um problema tão grande. Também é possível usar uma ferramenta como o OpenRouter, ou algo parecido no Cursor.

Como exemplo prático, a Abacus (ferramenta patrocinadora do canal) permite criar um "custom router": dentro da assinatura mensal, existe a opção "Create Custom Router". Uma das formas é o "RouteLL", roteamento próprio da Abacus, em que a própria ferramenta decide qual modelo é mais adequado para cada tarefa. A outra forma é criar um router customizado: escolher um template (por exemplo, o template "Frontier"), dar um nome, definir um system prompt (pode ficar vazio), e configurar categorias com o modelo desejado para cada uma. No exemplo montado no vídeo:

- **Frontier / problem solving** → Fable, com descrição de "tarefas extremamente difíceis, não familiares, open-ended, etc."
- **Complexo** → Opus 4.8
- (adicionada uma categoria extra) → GPT 5.5
- **Velocidade** → Gemini Flash
- **Balanceado** (não precisa de velocidade) → Kimi
- **Fallback / outras coisas** → Sonnet 5

Esse mesmo tipo de configuração pode ser feito com outras ferramentas, via skill, ou até com um script próprio local — não há vendor lock-in nesse conceito. Depois de salvar o router, a Abacus fornece uma chave de API. Essa chave pode ser usada com ferramentas como o OpenCode (mostrado em vídeo anterior do canal), que funciona de forma parecida com o Claude Code, mas permite rotear os requests para onde você quiser: basta conectar um provider (na tela de conexão de provider) usando essa chave de API da Abacus, da mesma forma como já foi mostrado antes a conexão com Anthropic e com Kimi.

### Fechamento

O apresentador pede feedback nos comentários sobre se esse tipo de conteúdo (técnicas e otimizações de uso de IA no dia a dia, menos hype) é relevante para o público, mencionando que está em um período de determinar que tipo de conteúdo é mais valioso. Ele reconhece tentar evitar falar tanto de IA, mas nota que é um tema inevitável pois "está engolindo" a carreira de desenvolvedor. Alternativas sugeridas pelo próprio apresentador, caso o público prefira outros temas, incluem banco de dados e system design.
