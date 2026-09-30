# O Dev na Era da IA: Tempo Ganho, Qualidade, Esteira e Novas Preocupações

Transcrição de vídeo em PT-BR (continuação de um vídeo anterior sobre como o mercado está recebendo a IA). Autor e título originais desconhecidos; o autor diz trabalhar com consultoria para empresas grandes. Já em português — sem tradução. Título descritivo derivado do conteúdo.

> **Nota de limpeza:** a transcrição automática corrompeu alguns termos, corrigidos por contexto: "to calling" → tool calling; "LRAP" → provavelmente RAG (dito junto de "como funciona uma LLM"); "Fredery Books" → Fred Brooks (a fala não cita qual frase/obra); "Harnes / harness engineer" → harness engineering; "Claudê" → Claude (Code); "CSD" → CI/CD; "lter" → linter; "guspindo" → cuspindo; "go horse" mantido (gíria brasileira para desenvolvimento apressado e sem processo); "então nota só falando de cicd… isso só o ponto doberg" → trecho ininteligível, mantido de forma aproximada ("só nesse ponto"). Pontuação e pausas de fala foram reorganizadas em parágrafos; o conteúdo não foi alterado.

## Abertura: a visão para o dev

No último vídeo o autor falou de como o mercado está recebendo cada vez mais a IA — e de que a IA não trouxe só vantagens, trouxe "probleminhas", como qualquer outra ferramenta ao longo da história. Cita Fred Brooks ("o saudoso") como alguém que responde muita coisa que a gente está vivendo agora. Existe uma visão de mercado e vários problemas a resolver; hoje ele quer trazer a visão para o dev.

Todo mundo pergunta "o que devo estudar, o que não devo estudar". Algumas respostas são rápidas: com certeza você deveria entender minimamente de **tool calling**, **MCPs**, **bancos vetoriais**, e basicamente como funciona uma **LLM** e um **RAG** — são coisas necessárias agora. Mas o foco do vídeo é entender os **desafios** que dá para resolver, no dia a dia, com essas ferramentas ou com outras.

## O código é gerado pela LLM — e o valor do código?

Hoje a esmagadora maioria do código é gerada por LLM; o desenvolvedor praticamente não coda mais. Mesmo assim, o autor não acha que a relevância de saber codar bem e debugar caiu — pelo contrário: **quanto mais conhecimento você tem, mais valor isso agora ganha**.

Antes, o espaço do código gerado ocupava um tamanho enorme dentro de uma sprint: a sprint inteira era baseada no tempo necessário para gerar um pedaço significativo de código. Esse tempo caiu muito, e aí todo mundo diz que o valor do código caiu. O autor não negligencia isso, mas propõe outra leitura: "mais código em menos tempo, então o código vale menos" — há cenários em que sim, mas o que está sendo **achatado é o tempo de geração**; ele não sabe se o **valor** do código se perdeu tanto assim.

## O que o tempo ganho pode comprar: qualidade

Trabalhando em consultoria para muitas empresas gigantes, ele vê que o *go horse* e o **time to market** aceleram muito as entregas, e ao longo da história deixaram-se de lado coisas importantes: **cobertura de testes, quality gate, melhorias no CI/CD**. Refatorar, revisar código que precisa de refatoração — tudo isso era empurrado "muito pra frente, muito pra frente", porque o **produto vinha em primeiro lugar**. Ele não diz que isso é errado: o produto paga a conta, fecha o cliente. Só que essas necessidades técnicas muitas vezes cresciam até ficarem tão "berrantes" que viravam **crise**. Criar CI/CD, casos de teste, automação, até a base para teste (massa de testes) — tudo dependia de tempo.

Agora que se ganhou muito tempo com a IA, a pergunta é: o que fazer com ele? Onde o autor investe muito é **qualidade**: como fazer todo o código que ele escreve sair com boa cobertura de testes. Isso é diferente de "vai lá, IA, gera os casos de teste": pode-se ter o *draft* com a IA, começar por ela, mas **bons casos de teste** dependem de uma questão técnica **e do negócio** — tem que ser uma **construção conjunta**, não só delegar. "Você pode delegar muita coisa para a IA, mas tem que ter uma pitada de conhecimento que é sua."

## IA na esteira (CI/CD): determinístico vs. não determinístico

Muita gente coloca IA na esteira, e ele também — mas não do jeito que muitos imaginam. Ele usa a IA para **gerar muita coisa que fortalece a esteira**, mas não para, por exemplo, plugar um agente que toda vez que a esteira rodar leia o log do que foi feito e aponte o erro para o dev. Isso ele ainda não acha legal.

É preciso separar preocupações que talvez não existissem até hoje: **código gera ações determinísticas; uma LLM gera valores não determinísticos** (indeterminados).

- Usar IA para **gerar** casos de teste, melhorar cobertura, montar um ótimo quality gate — sim. Também para configurar ferramentas que você não domina (GitHub etc.), inclusive **para aprender**: não deixar a IA fazer por você, mas fazer **junto** com ela, seguindo os passos, perguntando quando não entender uma palavrinha.
- Mas a **execução** desse CI/CD, depois de pronto, não deveria depender de LLM. Se o código que você gera é extremamente determinístico — testes, quality gate, linter, seja o que for — ele pode até ter sido gerado com IA, com seu acompanhamento e seu conhecimento de regra de negócio, mas **a execução não deve depender de uma LLM**, para não ter consumo de tokens alto nem uma esteira mais lenta.
- Quando o **produto** que você desenvolve tem conexão com uma LLM (um chatbot, uma integração, uma automação), a esteira ainda é determinística (só código). Ela pode fazer perguntas à LLM para verificar **comportamento, drift**, se está soltando informação que não deveria (parte de segurança). Mas isso **não precisa rodar a cada build**: deve rodar **de tempos em tempos**, talvez até desacoplado do disparo do CI/CD — não a cada commit, mas **a cada duas semanas**, para ver se a LLM ainda responde de acordo, **ou quando houver mudança de prompt** (o prompt que sobe com essa LLM mudou → aí sim dispara).

Só falando de CI/CD já daria para encerrar o vídeo.

## Olhar para o que é útil no dia a dia — e skills que atrapalham

Ele propõe olhar muito para o que está sendo útil: o que estou usando no meu dia a dia que me torna mais eficiente? E, depois de mais eficiente: **o que posso criar com LLM, o que posso acelerar para tornar meu time mais eficiente?** Ele tem várias *skills*, mas às vezes percebe que **tem skill que o atrapalha, que "deixa a LLM burra"**. Dentro do Claude (Code), por exemplo, ele vê que a ferramenta pega um conhecimento que ele pediu para ficar em determinado lugar e tenta trazê-lo de volta para outro ponto — ele não queria isso; sente que a IA fica repetitiva, toma decisões que não deveria. E ele sempre busca **conter esse tipo de comportamento**.

## Retrospectiva de erros: como dar feedback à IA?

Voltando ao CI/CD: quando acontecia uma quantidade alta de bugs, na review/retrospectiva da sprint o time olhava o que deu errado e registrava **lições aprendidas** para não cometer os mesmos erros. Agora, trabalhando com LLM, **como fazer isso com uma LLM?** Se acontece um determinado bug, como criar uma **cerimônia** para investigar: foi porque a IA não seguiu um padrão de código meu ou da empresa? Foi porque essa regra de negócio está desatualizada? E como dar, de maneira eficiente, **feedback para a IA que gera o código**, de modo que, toda vez que ela gerar algo novo, não caia no mesmo erro — para os erros não se repetirem?

Isso é um pouco do que se fala como **harness engineering**, "mas eu acho que isso vai muito mais além": o harness dá uma visão para isso, mas há muito mais preocupações.

## Fechamento: migração, não extinção

Nota-se a quantidade de **preocupações a mais**: estamos "cuspindo" código mais rápido, mas não se pode deixar de notar que temos mais preocupações em relação a isso. É uma **mudança da maneira de trabalhar**, não só gerar código mais rápido — estamos mudando os elementos que envolvem o trabalho. **Isso não é uma fase de extinção do desenvolvedor, é uma fase de migração**: uma mudança de paradigma muito grande.

Esse tipo de conhecimento, sente ele, ainda não aparece nos "cursinhos" que estão sendo lançados. Ele consegue ver algumas coisas, mas é muito intrínseco — por exemplo, conhecimento de empresas grandes que contratam muito no Brasil —, então vai demorar um pouco até chegar às camadas mais de base. Muitas pessoas fazem cursos sem esse olhar *enterprise*, mas para projetos autônomos ou pequenos negócios (pelo menos essa é a sensação dele).

Ele termina achando que o vídeo abordou bastante coisa, mas que poderia caber muito mais e acaba ficando "raso" — "é um começo". Pede nos comentários: como está o dia a dia de vocês, o que preocupa, o que estão vendo nas empresas, e, para quem está de fora sem conseguir o primeiro emprego, o que vê do seu lado. Agradece e encerra.
