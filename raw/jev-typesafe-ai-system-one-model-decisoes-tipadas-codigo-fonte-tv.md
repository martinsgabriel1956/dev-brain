# Jev (TypeSafe AI): o modelo "System One" que decide em vez de escrever texto (transcrição)

> Transcrição de vídeo (PT-BR), limpa de erros de ASR; sem tradução (já em português). Autoria inferida pela fala "aqui no Código Fonte" (canal Código Fonte TV). O ASR grafava o nome do modelo como "JV/Jeev/Jeff/JEV"; normalizado para **Jev** (grafia confirmada em fontes externas) e "Typeesave AI" para **TypeSafe AI**. Trechos ambíguos marcados com `[?]`. Gravado em 23 de setembro (ano não dito).

Chamam esse modelo de "ChatGPT dos softwares", só que ele não conversa, não escreve texto e nem gera código, e talvez seja justamente isso que o torne interessante. A TypeSafe AI acha que estamos usando chatbots para resolver problemas que o software deveria resolver de outra forma. Vamos explicar isso e entender se o Jev é só hype ou algo que veio ajudar de verdade.

## O problema: LLM inteiro para um sim ou não

Imagine um agente que precisa decidir se chama uma ferramenta. Você manda o contexto para um LLM, espera ele raciocinar, gera um JSON, faz o parse, valida a resposta, e tudo isso para chegar muitas vezes a um sim ou a um não. Os engenheiros da TypeSafe AI acharam que estavam complicando demais uma decisão simples. Faz sentido chamar um LLM inteiro, gerar texto e depois transformar o que volta em dados? Eles decidiram simplificar, mas para isso foi preciso abrir mão da coisa que definiu esta geração de IA: a **geração de texto**.

## O lançamento

O Jev é novíssimo: lançado em 15 de setembro como o **primeiro "System One model"**. Usa **amostragem paralela** e um método de treinamento que a empresa chama de **Reinforcement Learning for Calibrated Decisions (RLCD)**. Em vez de strings abertas, o modelo recebe um **estado** mais **perguntas tipadas** e retorna **decisões probabilísticas**.

(Trecho patrocinado: Hostinger VPS, usada há mais de 10 anos pelo canal; custo previsível, qualquer tecnologia, bom custo-benefício quando os acessos crescem; aplicações instaladas em poucos cliques; usam Dokploy no VPS para levar o app do repositório do GitHub direto a um contêiner Docker, com vários deploys por dia; cupom "código fonte".)

## RLCD vs. RLHF

Nos LLMs tradicionais, uma técnica conhecida é o RLHF (reinforcement learning from human feedback): o treino ajuda o modelo a produzir respostas que humanos consideram boas, úteis e adequadas. O RLCD muda o objetivo: o modelo é treinado para **tomar uma decisão e expressar corretamente o nível de confiança** nela. Isso importa para software porque o código pode tomar decisões diferentes conforme a confiança do modelo. A TypeSafe AI alega que LLMs tradicionais, ao declarar a própria confiança, podem produzir valores inconsistentes ou excessivamente confiantes.

## Casos e repercussão

- **Vercel:** segundo uma reportagem, substituiu um modelo menor da OpenAI (ASR: "Luna 5.6, modelo mais barato oferecido pela OpenAI" `[?]`) para executar comandos de segurança pelo Jev e obteve resultados "até 18 vezes mais rápidos e mais precisos".
- **MotherDuck** (data warehouse): classificação de texto "50 vezes mais rápida com 1% do custo". A função SQL `prompt` alimentada pelo Jev classificou 100.000 linhas em 40 segundos por 50 centavos `[?]`, com a precisão de um LLM de ponta; o LLM levou 32 minutos e custou 37 `[?]` (unidades não ditas).
- O modelo estava em preview, abriu para todos e, dias depois, **fechou novas inscrições** por excesso de demanda (o apresentador tentou se cadastrar e não conseguiu).
- O criador, **Diogo Almeida**, trabalhou na OpenAI e foi um dos criadores da parte de reforço de treinamento do ChatGPT. Ficou dois anos na TypeSafe AI antes do lançamento. O apresentador diz que, pela apuração, ele é filipino (não brasileiro). A empresa captou **US$ 40 milhões** no Vale do Silício.
- A tese dele: nem tudo o que fazemos com IA generativa precisa de saída em texto. Hoje todos usam API com prompt e **não recebem o nível de confiança** da resposta; com a confiança, o código decide se continua ou não.
- Há movimento de integração em ferramentas de agentes (o OpenClaw, citado como "Open Cloud" `[?]`, aparece num tweet).

## Como funciona: System 2 (LLM) vs. System 1 (Jev)

**Fluxo tradicional (LLM):** o software envia um prompt; o modelo gera **token por token**; mesmo se você pede JSON, ele continua escrevendo texto. Depois o código faz o parse, valida a estrutura, converte tipos e trata erros; se o JSON vier quebrado, pode ser preciso nova chamada. Mais custo, latência e complexidade.

**Fluxo System One (Jev):** o software envia um **estado** e várias **perguntas tipadas**. O Jev processa as decisões diretamente, pode responder várias **em paralelo**, e a saída já chega no formato definido pelo programa, **acompanhada de probabilidades e grau de confiança**.

"Zero erro de esquema" **não** significa que o Jev nunca decide errado: significa que não deveria devolver valor incompatível com o tipo definido. Ele pode devolver uma resposta estruturalmente válida e semanticamente errada. Por isso, quando dizem que o Jev "não alucina", o ponto real é que ele **mostra o grau de confiança**.

## Anatomia de uma chamada: state, questions, answers

1. **State:** o contexto necessário. Exemplo: um chamado de suporte (assunto, mensagem do cliente, informações da conta, código de erro). Envie só o necessário para a decisão.
2. **Questions:** em vez de um prompt pedindo JSON, define-se o tipo exato de decisão, com três primitivas:
   - **choice:** lista fechada de opções (ex.: qual time deve atender o chamado); só pode escolher entre as enviadas.
   - **score:** avalia algo numa escala (ex.: nível de frustração do cliente).
   - **no** `[?]` (a pesquisa externa indica "noul", proposição verdadeiro/falso): decisão sim/não expressa como **probabilidade** (ex.: "esse chamado é urgente?").
   Todas podem ir na mesma chamada e são avaliadas em paralelo; o estado é recebido uma vez.
3. **Answers:** valores que o software usa diretamente, mais **probabilities** e **confidence**. Não basta saber que escolheu "technical": é preciso saber quão confiante está. O conceito: **estado entra, decisões tipadas saem**.

## Quando usar

O Jev **não substitui** um LLM: não gera texto. Lida com **tarefas de classificação** em que hoje se usa LLM, sem a mesma latência e custo. É um complemento: o LLM para raciocínio aberto e geração de dados; o Jev para decisões rápidas e estruturadas ao longo do processo. A regra do apresentador: **se a saída da etapa é um valor que o código usa para ramificar, considere o Jev; se é texto que uma pessoa vai ler, use um LLM.** É rápido porque decide de forma paralela e simultânea, não token por token.

## Conclusão

Promissor, mas "ainda é um bebezinho". O apresentador acha que não é só hype, que outras empresas vão imitar e pergunta se veremos concorrentes em breve. Ressalva: o Jev **não é um wrapper** de outro modelo; é um **foundation model** treinado para isso.
