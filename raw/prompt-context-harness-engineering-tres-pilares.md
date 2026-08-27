---
date: 2026-08-27
tags: [prompt-engineering, context-engineering, harness, transcricao]
type: transcript
---

# Prompt Engineering, Context Engineering e Harness Engineering — Os Três Pilares

> Transcrição de trecho de vídeo/aula. Áudio com ruído de reconhecimento de fala em alguns trechos (marcados abaixo); mantido conforme captado, sem correção de conteúdo.

Então vamos para três assuntos que são pilares fundamentais para que nós possamos usar a IA muito bem: **prompt engineering**, **context engineering** e **harness engineering**. Todo mundo já ouviu falar. Esse diagrama aqui mostra muito bem a dinâmica dessas três palavras.

## Prompt Engineering

Primeiro temos o prompt engineering, que é a engenharia do prompt. Prompt é isso que você está trocando de mensagens ali com a IA — anexando outras coisas também junto, né. Lá em 2022, quando começou a ter o ChatGPT, essas coisas assim, sabia que a janela de contexto era de apenas 4.000 tokens? Sabia disso? 4.000 tokens. Hoje é de 1 milhão. É uma diferença enorme, né.

Então, nessa época, como não tínhamos essa janela de contexto — o que a IA consegue suportar de conteúdo dentro dela para poder fazer o processamento — se falava muito que "você tem que saber pedir". Não é só você interagir com ela; a forma como você pede, a forma como você estrutura o seu prompt, é essencial. Então é exatamente isso: durante muito tempo isso se figurou como uma importância muito grande, e ainda continua sendo importante hoje, porque se você pedir as coisas de N formas diferentes, você vai ter N respostas diferentes — muitas vezes respostas mais assertivas.

Mas acontece que hoje a gente está tendo modelos cada vez melhores. Então, às vezes, você coloca um prompt mais ou menos e ele já te dá uma boa resposta. Provavelmente você já deve ter sentido isso, de uns anos para cá: você pede ali uma coisa mais ou menos e ele consegue fazer para você. Mas o primeiro ponto é que se figurava isso como fundamento: nós precisamos estruturar muito bem o que eu peço para ela.

## Context Engineering

Depois, quando a janela de contexto foi aumentando um pouquinho mais, permitindo mais possibilidades mas mesmo assim limitada, surgiu o termo **context engineering** — engenharia do contexto. O que é que a minha IA pode ver? Porque eu tenho uma janela de contexto limitada, e se eu tenho uma codebase, tenho várias instruções, ela não vai poder ler tudo de uma vez. Então eu preciso selecionar muito bem o que eu mando para ela. Esse "selecionar muito bem" é o segredo. Por isso que nós fazemos a engenharia: eu tenho um mundo de coisas, esse mundo não cabe, então eu preciso encaixar muito bem.

## Harness Engineering

E aí vem o **harness**. O harness é um conceito que surgiu em 2026 — já vinha sendo conversado no final de 2025, mas veio a toda em 2026.

Imagina que essa aqui é a sua LLM — pode ser o GPT, o Opus, ou qualquer outro. A LLM por si só é como se fosse um cérebro que não faz nada. Tem muita inteligência, eu consigo pensar um monte de coisas, mas eu não entrego nenhum valor. Então o segredo de utilizar bem a IA é o que está em volta dela — e é isso que nós chamamos de harness.

Tem até um mantra que é assim: **"se você não é o modelo, você é o harness"**. Essa palavra é um pouco estranha para traduzir, não tem uma tradução literal para o português, mas o que ela mais se aproxima, ainda mais no contexto da IA, seria **infraestrutura**. A ideia é justamente que, para poder operar muito bem a IA, eu preciso cercar ela com uma série de políticas, ferramentas, metodologias e recursos, para aí sim ela poder trabalhar de forma correta.

Então, quando estamos falando de harness — sabe quem é harness? Claude Code é harness. [ASR incerto: "Itubilot CLI"] é harness. [ASR incerto: "diminers"]. O Cursor também é harness. O AntiGravity também é harness. Todo mundo está ao redor do modelo.

Pense: cada uma dessas ferramentas vai fornecer recursos para poder compactar o contexto, ferramentas de planejamento, organização. Eu vou poder visualizar também a janela de contexto — consigo fazer ali uma barra de "context", quantos tokens eu tenho. Enfim, pense no número de recursos que você tem em volta. Se você tira essa ferramenta e sobra só o modelo, ele não consegue fazer nada.

### Duas Camadas de Harness

Então tem esse harness embutido, que você adquire através da ferramenta que você tem. E aí tem o harness que você vai criar, para que você controle. Imagina que esse vermelho aqui são todas essas ferramentas — mas agora nós vamos criar o nosso harness. Esse harness nosso vai ficar em volta.

Vamos lá configurar aqueles arquivos de memória, como CLAUDE.md, configurar regras do projeto, configurar skills — que é um recurso que a gente vai falar daqui a pouco —, configurar MCP, criar um workflow em que eu consiga planejar uma feature, sendo que essa feature esteja planejada de acordo com as necessidades do projeto. Quando eu for implementar, vou rodar os testes — na verdade, vou ensinar para a IA como ela roda os testes de forma correta, quais testes ela tem que rodar, quais testes ela tem que criar. Se caso der qualquer problema na hora que implementei, como ela vai recuperar dos erros. Tudo isso aqui é o que a gente cria para que ela consiga seguir o caminho desejado.

A mistura desses dois harness (o embutido na ferramenta + o que você constrói) é o que vai fazer com que a gente tenha um bom workflow para poder desenvolver.

### Complexidade Crescente e Arquitetura

Lembre-se que um software, por definição, independente de antes ou agora com a IA, a complexidade desse software vai crescendo ao longo do tempo. Inclusive gosto de citar o Robert Martin, lá do Clean Architecture, que tem aquele gráfico de complexidade versus tempo: vai adicionando código, várias pessoas vão passando pelo projeto, e a complexidade vai crescendo, crescendo, crescendo. Como que eu consigo manter esse projeto nas rédeas? É tendo uma boa arquitetura, fazendo uma boa engenharia nesse projeto. Eu consigo isso através do meu harness — configurando as regras, as guidelines, como que as coisas têm que ser feitas, e como eu consigo verificar que aquelas coisas feitas estão corretas.

### Voltando ao Contexto: o Ponto Ótimo

E aí volta a questão da engenharia do contexto — engenharia do que é passado para a IA. Se eu passo pouco contexto para a IA, ela faz besteira. Se eu passo contexto demais para a IA, ela também faz besteira. Então o ponto ótimo é o meio-termo: você passar o contexto certo no momento certo. E você só vai conseguir passar (delimitar) esse contexto se você tiver um bom harness — se você tiver uma boa ferramenta que vai te ajudar a desenvolver, mais a montagem do seu harness.

Saiba que você tem que começar a usar a IA de um modo diferente.
