# Harness Explicado: Function Calling, HAG (RAG Interno) e Evals — Como Construir uma Harness do Zero

> Transcrição de vídeo em português, colada pelo usuário no chat e reorganizada em seções/parágrafos para leitura (removidas repetições e hesitações de fala; conteúdo não traduzido — já em português). O autor comenta que "o Té aqui" (Téo, referenciado como "tio") "venceu na corrida" para publicar conteúdo sobre harness primeiro — vídeo de comparação/resposta a esse conteúdo prévio, com foco em desmistificar o termo através de uma harness mínima construída ao vivo em Python com a API da OpenAI. Vídeo patrocinado pela Abacus (menção comercial no início, não relevante ao conteúdo técnico).

## Abertura: Por Que Falar de Harness

O autor situa harness como o próximo passo depois de entender "hardness" (sic — pronúncia/grafia usada ao longo do vídeo para "harness") para quem quer criar sistemas com IA. Entender como uma harness funciona por dentro ajuda a tomar melhores decisões de design ao construir sistemas próprios. Menciona que o termo tem sido muito usado ("hypado") recentemente, mas é vago — pesquisar no Google tende a devolver Claude Code, Codex ou ferramentas similares em vez de uma definição.

## Bloco Patrocinado (Abacus)

Abacus oferece uma CLI no estilo Claude Code por ~$10/mês, mais acesso a um chat com vários modelos (Nano Banana Pro/2 para imagem, Opus 4.7 para código, entre outros) e um "Agent" com uma feature chamada "agent swarm" que lança múltiplos agentes em paralelo para tarefas complexas — ganho de velocidade e qualidade em tarefas grandes. Combo de assinaturas por ~$20/mês total (citado como "menos de R$50/mês" na cotação da época). Bloco comercial, sem relação direta com o conteúdo técnico do restante do vídeo.

## Experiência Pessoal: Construindo um HAG (RAG) Antes do Termo "Harness" Existir

O autor conta que, numa empresa anterior, construiu o que hoje se chamaria de harness sem saber o termo — via avaliação sistemática de modelos usando um framework parecido com o Evals da OpenAI (framework para avaliar se modelos/sistemas fazem o que deveriam fazer).

O sistema em questão era um HAG (o autor pronuncia como "rag"/"hag" — no contexto, é um RAG: Retrieval-Augmented Generation) que:

1. Pegava uma série de documentos (ex.: 3 a 5 documentos) e fazia **chunking** — dividia em pedaços menores.
2. Armazenava os chunks numa **vector database**.
3. Buscava os chunks mais relevantes usando **KNN** ou **BM25** (dois estilos de busca por similaridade) para ranquear quais documentos mais se pareciam com a pergunta do usuário.
4. Selecionava os 3-4 documentos mais relevantes e injetava esse conteúdo no **prompt**, junto com um **system prompt forte** instruindo o modelo a responder **apenas** com base nos documentos fornecidos (não usar conhecimento próprio).
5. A resposta gerada era então avaliada por **outra IA**, usando um framework de avaliação (tipo Evals), para checar se a resposta foi fiel o suficiente aos documentos enviados.

Exemplo dado: se o usuário perguntasse algo como "jogar uma pedra pela janela é crime?", o sistema enriquecia o prompt (possivelmente via IA), rodava a busca por similaridade contra a base de documentos, e se algum texto relevante sobre o tema existisse na base, era injetado no contexto antes de gerar a resposta.

**Ponto central do autor**: tudo isso — prompts, funções de busca por similaridade, orquestração de idas e vindas entre código e modelo — é essencialmente o que uma harness faz. A construção desse HAG, feita antes do termo "harness" ficar popular, já era uma harness na prática.

## O Que É uma Harness (Definição de Trabalho)

Harness é um termo "guarda-chuva" (catch-all), impreciso, que hoje é usado principalmente para se referir a ferramentas como Claude Code, Codex e Cursor, e ao **tooling em volta da IA** de forma geral.

Separação conceitual central do vídeo:

- **Modelo**: roda no data center do provider (Anthropic, OpenAI etc.).
- **Harness**: roda na máquina do usuário (localmente).

Quando o usuário digita um prompt numa ferramenta como o Claude Code, o prompt **não** vai direto para o modelo via chamada de API pura. Antes de ser enviado, a harness:

1. Adiciona o **system prompt**.
2. Adiciona conteúdo de arquivos de configuração (ex.: `CLAUDE.md`), se existirem.
3. Envelopa tudo isso e envia ao modelo.

Dentro do system prompt, o modelo é informado de quais **tools** (ferramentas) tem disponíveis e como chamá-las — via **function call** / **tool call** (o autor nota que são conceitos ligeiramente diferentes, mas relacionados). Exemplo: uma tool `bash` que o modelo pode invocar pedindo, por exemplo, um `ls` para listar arquivos de um diretório.

### O Ciclo de Idas e Vindas

1. O modelo lê o prompt e decide que precisa listar arquivos — ele **não executa nada diretamente**; ele retorna uma resposta pedindo uma **tool call** (ex.: rodar `bash` com `ls`).
2. A harness, rodando localmente, **executa de fato** esse comando.
3. O output do comando é adicionado de volta à conversa e reenviado ao modelo.
4. O modelo processa esse novo contexto e decide o próximo passo — pode pedir outra tool call (ex.: um `cat` para ler arquivos) ou já responder ao usuário com uma mensagem final.
5. O ciclo se repete quantas vezes forem necessárias até o modelo devolver uma resposta de texto final ao usuário.

Outras tool calls comuns citadas: editar arquivos de texto em linhas específicas — sempre chamadas de função que um programador poderia escrever manualmente (o autor relata ter escrito esse tipo de function call na empresa onde trabalhou).

### Harness Simples é Possível, mas a Combinação com Modelos Bons é o Que Torna Isso Poderoso

É possível construir uma harness simples com relativamente pouco código. O que mudou nos últimos anos é que tanto a qualidade das harnesses (Claude Code, Cursor etc.) quanto a qualidade dos modelos cresceram muito — a combinação dos dois é o que tornou essas ferramentas tão fortes.

### Skills Não São "Superpoderes" Mágicos

Contra-argumento a uma objeção comum ("mas minhas skills dão superpoder ao modelo"): skills **não dão superpoder** de fato — elas apenas **adicionam mais texto ao prompt**. O ponto chave: existem coisas rodando localmente na máquina do usuário (código, que pode ser lido e compreendido, e replicado) e coisas rodando no data center do provider — e tudo que entra e sai do data center é **texto** (prompt). Não é mágica; é prompt engineering e engenharia de sistema em volta disso. Se algo aqui merece ser chamado de "mágico", é a qualidade dos modelos em si — não o mecanismo da harness.

## Function Calling (Referência Técnica)

O autor recomenda a leitura da documentação de **function calling da OpenAI** como material de referência — permite fornecer ao modelo as tools/funções disponíveis e construir um sistema agêntico. Relata que, na época em que trabalhou com isso (antes do function calling formal existir na Anthropic), a técnica usada era pedir ao modelo que respondesse usando **tags XML** para sinalizar chamadas de função — funcionava cerca de 99% das vezes; quando falhava, bastava fazer um **retry**.

## Demonstração Prática: Harness Mínima em Python com a API da OpenAI

O autor demonstra uma harness "ultra simplória" implementada num único arquivo Python (`harness.py`), com os seguintes elementos:

- Uma chave de API da OpenAI carregada de variável de ambiente.
- Um **system prompt**.
- Uma lista de **tools** disponíveis para o modelo — nesse exemplo, uma única tool chamada `run` (que executa comandos via `bash`).
- Definição do payload da chamada à API.
- Um **loop while true** ("wild through", conforme falado) que roda indefinidamente, alternando entre "vez do usuário" e "vez do modelo": enquanto houver **function calls** pendentes, a harness as executa, adiciona o resultado ao histórico de mensagens, reenvia para a API, e processa a resposta seguinte. Isso é o coração da harness.
- Um output estruturado que deixa claro quando a resposta da API é uma **function call** (`type: function_call`, com o `name` da função, ex. `run_bash`) versus uma resposta final de texto (`type: output_text`).

### Testes ao Vivo

1. **"Hi"** → resposta simples do modelo ("How can I help"), sem tool call — troca direta de texto.
2. **"What files are in this directory?"** → o modelo não tem nenhuma forma de saber em que diretório está a não ser executando uma tool call. Ele retorna uma function call pedindo `run bash` com `ls`. A harness executa localmente, lista arquivos como `.env`, `.cache`, `harness.py`, devolve o resultado ao modelo, que então responde ao usuário citando os arquivos encontrados (incluindo `harness.py`). O autor enfatiza: não haveria nenhuma outra forma do modelo saber disso — só porque o sistema local executou o comando e devolveu o resultado.
3. **"What is harness.py?"** (após reiniciar a sessão, então sem memória do teste anterior) → o modelo busca pelo arquivo, executa algo como `sed` para ler o conteúdo completo, envia o conteúdo lido de volta como parte do contexto para a API, e a API responde descrevendo o que o script faz (carrega chave da API, envia mensagens, define modelo, repete o loop) — uma auto-descrição correta do próprio harness.py, obtida por leitura real do arquivo via tool call, não por adivinhação.

Conclusão da demo: isso é, na prática, um **agent harness** que permite ao modelo da OpenAI inspecionar e interagir com o sistema local via shell/bash commands — nada de extraordinário tecnicamente, mas é exatamente o mecanismo por trás de ferramentas como Claude Code e Codex.

## As Três Camadas de um Sistema de IA Bem Construído

O autor fecha destacando três componentes que quem constrói sistemas de IA precisa ter em mente (não apenas dois):

1. **Código determinístico** — que toma ações com base no output da IA (executa comandos, chama APIs, edita arquivos).
2. **Prompts** — o texto que vai e volta entre o código e o modelo.
3. **Avaliação de qualidade** — medir se o sistema está de fato fazendo o que deveria.

Sobre o item 3, o autor detalha a prática usada na empresa onde trabalhou: pegar toda a interação (usuário + modelo + harness) e usar um **LLM como judge** (juiz) para pontuar a qualidade de cada resposta — por exemplo, quão fiel a resposta foi aos documentos fornecidos (no contexto do HAG/RAG descrito antes). Também mediam **custo em tokens** por interação, permitindo comparar diferentes modelos por adequação a diferentes tipos de tarefa (ex.: "esse modelo é melhor para X, esse outro é melhor para Y"). O autor descreve esse tipo de sistema de avaliação como parte central do seu trabalho em 2024–2025.

## Encerramento

Bloco final de divulgação de cursos do canal do autor (estruturas de dados e algoritmos/LeetCode, roadmap para entrevistas, e um curso de system design em pré-lançamento com lista de espera) — conteúdo promocional, não técnico.
