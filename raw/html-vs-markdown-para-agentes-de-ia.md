# HTML vs. Markdown para Agentes de IA

> Transcrição de vídeo (áudio em português). Limpeza de disfluências e vícios de fala, sem alteração de conteúdo ou opinião do autor.

## Introdução — o gancho

Tu ainda usa Markdown quando tá usando teu agente? Cara, isso é coisa de noob. Agora tudo mudou, vamos aprender do zero! Não, brincadeira. Falando sério: hoje eu quero mostrar como eu tô usando HTML para melhorar a investigação de problemas no Persua, e até como eu tô criando *quality gates* em todo o meu sistema.

Isso aqui é algo que eu já postei para vocês: eu estava usando HTML para analisar o quanto o Persua tava errando na hora de transcrever o que a pessoa fala numa reunião, usando modelos locais. E aí a Anthropic também divulgou algo parecido sobre como é efetivo usar HTML em vez de Markdown quando se está usando agentes de IA.

Vamos ler o artigo do Tarik e depois eu mostro como estou fazendo isso no Persua — inclusive como deixei o GPT-5.5 Extra High rodando até gastar todos os meus créditos do Codex.

## O que o artigo do Tarik diz

Markdown se tornou o formato de arquivo dominante usado por agentes para se comunicar conosco. É simples, portátil e tem alguma capacidade de texto rico, além de ser fácil de editar — o Claude, inclusive, ficou surpreendentemente bom em usar ASCII para fazer diagramas dentro de arquivos Markdown.

Mas, à medida que os agentes se tornaram cada vez mais poderosos, o Markdown passou a parecer um formato limitante: é difícil ler um arquivo Markdown com mais de 100 linhas.

É verdade, tenho que confessar: muitas vezes quando pergunto algo para o meu agente, ele me responde com um Markdown gigante, e eu não consigo conectar os pontos porque tem informação demais ali. De fato, o que eu tenho começado a fazer é usar HTML para isso — e acho que é isso que o Tarik está sugerindo. Tem prós e contras, que já vou comentar, mas devo confessar que os melhores modelos estão criando coisas boas nesse formato.

## Caso de uso 1 — qualidade de transcrição no Persua

Dentro do Persua a gente faz transcrição usando modelos locais. São seis modelos: Whisper Tiny, Base, Small, Medium, e o Large V3 (quantizado e não quantizado, além do Turbo).

Eu queria saber o quanto esses modelos estavam "traduzindo" corretamente — qual era a *accuracy* deles, qual a certeza de que estavam transcrevendo exatamente o que estava no áudio. Pedi para o modelo rodar todos os testes de qualidade que eu tenho, e ele gerou um Markdown enorme, cheio de texto. Aí eu pedi para ele converter aquilo em HTML, para eu poder visualizar — e ficou muito melhor de visualizar.

## Caso de uso 2 — entender as implementações de transcrição em tempo real

Dentro do Persua existem várias formas de usar os modelos: dá para conectar modelos locais para fazer a transcrição, usar o Apple Speech, ou usar por API a OpenAI e o Gemini. Cada uma dessas soluções tem uma maneira diferente de implementar a transcrição em tempo real.

Por exemplo: usando Apple Speech, não preciso fazer o *enforcement* de um prompt — não preciso instruir o Apple Speech a transcrever a voz em texto de uma forma específica. Mas usando o Gemini, preciso, porque o Gemini não tem uma API real-time tipo Whisper para transcrição. Para o Gemini eu preciso usar um prompt que o transforma num tradutor/transcritor.

Um exemplo de prompt que uso: instrução para o modelo transcrever o áudio de forma acurada, avisando que o conteúdo é sobre tópicos de *software development*, negócios e tecnologia, e pedindo para manter termos como *API*, *endpoint*, *deployment*, *repository* em inglês. Isso é muito importante passar para os modelos.

O problema é que, dentro do projeto, é difícil visualizar isso. Se eu pedir para o modelo me dizer qual é a forma atual de implementação para cada provedor, é complicado — por exemplo, para OpenAI eu tenho dois tipos de implementação por causa de *fallbacks*: um caminho via WebSocket e, se o WebSocket falhar, um REST com *chunks* de áudio. Tem muitas implementações.

Pedi para ele criar um HTML estático explicando como, no meu projeto, cada forma está sendo utilizada. Foi muito útil.

*(Nota lateral do autor: o Persua estava aberto nesse momento porque ele estava sendo usado para traduzir texto em tempo real via um assistente de leitura de artigos — seleciona um texto na tela e o Persua identifica a seleção e roda a tradução.)*

## Voltando ao artigo — edição de arquivos e preferência por HTML

O Tarik conta que também tem deixado cada vez mais de editar arquivos diretamente, usando-os como especificações, arquivos de referência e resultado de brainstorm — coisa que o autor do vídeo também faz, inclusive com os arquivos `.md` de projeto (tipo os que a gente cria para descrever projetos), hoje escritos com ajuda de modelo.

O Tarik diz que, quando faz edições, geralmente pede isso ao Claude — e afirma que tem passado a preferir HTML como formato de saída em vez de Markdown.

Aqui o autor do vídeo discorda um pouco: acredita que não é uma boa prática generalizada. E cita que, se não se engana, a própria OpenAI também não recomenda esse *approach* — no *Prompt Guidance* da OpenAI, a recomendação é começar com um `role` (personalidade, objetivo etc.) e usar Markdown na estrutura do prompt. Isso muda de modelo para modelo — não à toa a própria OpenAI criou uma ferramenta para otimizar prompts de acordo com o modelo escolhido. Modelos mais antigos de *chain of thought* performavam melhor com tags (não necessariamente HTML — eram tags XML-like).

O autor ainda hoje usa tags dentro do Persua para dividir, por exemplo, instruções de formato de output, e dentro dessas tags ainda usa Markdown — não HTML como o Tarik sugere.

### O teste do prompt otimizado

O autor decide testar: pega um prompt do seu assistente de leitura de artigos, que usa tags, e pede para o GPT-5.4 avaliar se está otimizado e sugerir melhorias. Depois de uns 5 minutos rodando, o modelo fez 55 modificações — e removeu todas as tags do prompt original. Conclusão do autor: ainda não dá para saber com certeza qual abordagem é "certa".

## Por que HTML, segundo o Tarik — densidade de informação

Segundo o Tarik, HTML permite criar tabelas, ter um design melhor, ilustrações, demonstração de código, interações (*sliders*, *toggles* etc.). De fato, como mostrado no exemplo do Persua, fica muito mais fácil para um humano visualizar como o sistema está funcionando.

O autor esclarece que, até agora, não usou esse HTML como *input* para alimentar o modelo de volta (ou seja, não realimentou o agente com o HTML gerado) — mas acredita que seria um passo natural, porque se o HTML é usado para melhor visualizar o que está sendo criado, ao sair do modo plano ele acabaria alimentando o modelo com esse HTML.

### O contra, na visão do autor

Gerar HTML consome muito mais tokens — estimativa do autor: pelo menos umas 20 vezes mais tokens que Markdown equivalente. Mas, se acertar de primeira, talvez até compense (economize idas e vindas).

O Tarik argumenta que quase não há conjunto de informação que o Claude possa ler que não possa ser representado de forma razoavelmente eficiente em HTML — o que torna esse formato altamente eficiente tanto para o modelo comunicar informação e profundidade, quanto para o humano revisá-la. Na ausência disso, segundo ele, o modelo tende a fazer coisas mais "improvisadas" e ineficientes, como diagramas em Markdown/ASCII, ou (o exemplo favorito do Tarik) estimar cores usando caracteres Unicode — como em uma captura de tela do Claude Code, que ele cita como sintoma de ineficiência de ferramenta.

O Tarik diz que vai considerar substituir o renderizador de Markdown que usa no Claude Code por um renderizador de HTML.

### Outros argumentos do artigo, com a opinião do autor do vídeo

- **Clareza na visualização** — concordância total: fica mais fácil de ler.
- **Especificações/planos ficam muito grandes** — à medida que o Claude executa tarefas mais complexas, o *spec*/planejamento cresce bastante em tamanho.
- **"É mais fácil de compartilhar"** — o autor discorda parcialmente aqui: um arquivo Markdown grande também não é fácil de compartilhar (não cabe direito num *clipboard*), então esse argumento não convence tanto.
- **Interações** — HTML permite criar *sliders* e outros componentes interativos para ajustar parâmetros dentro de um plano (o autor cita, como exemplo geral desse tipo de componente, os "chips" usados em Android, mas aplicado aqui a interações dentro de planos gerados).
- **Por que não usar o Claude Cosmos/Claude Design (produto da Anthropic) para isso?** O Tarik responde que um dos maiores motivos é todo o contexto que o Claude Code consegue ingerir. Por exemplo: ao escrever um artigo técnico, ele pediu ao Claude Code para ler a pasta de código e encontrar todos os arquivos HTML relevantes. O autor do vídeo comenta que também tem escrito posts técnicos sobre o que está fazendo no Persua, usando os mesmos agentes locais que usa para programar.

### Casos de uso listados no artigo

- **Spec / planejamento**
- **Exploração**
- **Code review**
- **Understanding** (entendimento de sistemas)
- **Design** — o autor comenta que, para design, já costuma usar Figma + MCP para implementar.
- **Relatório de pesquisa e aprendizado** — o autor acha que vale a pena principalmente para quem está entrando num projeto novo. Reforça um conselho que sempre dá para quem está começando a carreira: quem entra num projeto é "júnior" naquele projeto, independente do nível de senioridade geral — mesmo alguém com 1–2 anos de casa pode não entender tudo que se conecta ali, principalmente com múltiplos repositórios e múltiplos times. Nesse cenário, pedir para o agente investigar todos os repositórios acessíveis e desenhar como os serviços se comunicam, entregando isso em HTML, ajuda a absorver a informação muito mais rápido do que em Markdown.
- O artigo dá um exemplo de prompt nesse sentido: *"Não entendo como o nosso rate limiter realmente funciona. Leia o código relevante e produza uma única página explicativa em HTML: um diagrama do fluxo de token bucket, os três ou quatro trechos de código principais anotados, e uma seção de 'gotchas' no final."* — "gotchas" sendo armadilhas/detalhes que quebram tudo se ignorados (o autor comenta que é o "nome educado para coisas que a documentação esqueceu e que vão fazer alguém perder uma tarde").

## Conclusão sobre o dilema HTML vs. Markdown

O autor comenta o tom de "corrida" de muitos posts sobre o tema ("gastei tempo aprendendo a escrever Markdown, agora vou ter que aprender HTML") e brinca que isso mostra que o emprego de quem entende os fundamentos está seguro, porque a maior parte da concorrência está gastando energia discutindo formato em vez de fundamentos.

Resumo pessoal do autor: já tem feito algumas coisas em HTML sem nem saber que era isso que o Tarik estava sugerindo, e tem funcionado bastante — principalmente para entender partes complexas do próprio sistema. Ainda não usou HTML como *input* para o agente, mas acredita que, ao planejar uma funcionalidade inteira pedindo um HTML explicativo do plano, naturalmente esse HTML acabaria virando input para a execução.

## Dica final — baseline de qualidade e quality gates

O autor descreve um *quality gate* que criou no Persua para transcrição:

1. Gerou dois áudios a partir do mesmo texto-alvo (a "meta" do que deveria ser transcrito): um gravado pelo próprio autor (com voz humana, mais falha/natural) e outro gerado por uma IA (voz mais pausada, com menos erro de pronúncia).
2. Quando um Pull Request é aberto, o GitHub Actions transforma esses dois arquivos de áudio num *stream* de buffer, baixa os cinco modelos locais de Whisper usados no Persua, e alimenta esse áudio no código de transcrição do Persua.
3. O código gera a transcrição final. O autor compara o texto desejado (target) com o texto gerado e calcula uma nota de qualidade.
4. Essa nota precisa estar acima de um *threshold* (baseline de qualidade definida previamente). Se ficar abaixo, o teste falha, e o PR não pode ser *merged*.

O autor já tinha gravado um vídeo anterior sobre um outro *quality gate* que criou — que checa duplicação de código, roda linters, faz análise estática (como complexidade ciclomática), entre outras verificações.

Com esses dois *gates* combinados, o autor consegue delegar uma tarefa inteira para um agente executar e abrir um PR, com confiança de que — se todos os testes de qualidade passarem — o agente não está introduzindo dívida técnica nem piorando a qualidade dos modelos locais usados no projeto.

Exemplo concreto: no dia anterior ao vídeo, o autor conseguiu fazer melhorias nas transcrições do Persua com modelos locais deixando o modelo rodar por cerca de 3 horas seguidas, até atingir uma boa nota de qualidade — sem precisar de supervisão constante.

## Encerramento

O ponto central, segundo o autor: o que importa é ter esse tipo de processo (baseline de qualidade + quality gates), não a escolha entre HTML ou Markdown — isso é estilo pessoal. Engenharia de software não é sobre saber usar Markdown ou HTML. Copiar e colar respostas do ChatGPT não é fazer engenharia de software — é usar IA como um novo Google/Stack Overflow, o que não é necessariamente errado, mas não muda a forma como alguém *faz* engenharia de software com inteligência artificial.
