# Substituir 6 milhões de linhas de COBOL: como o DMV da Califórnia usou IA para descobrir as regras de negócio

Fonte: transcrição de vídeo, colada pelo usuário em 2026-10-06. Já em português — sem tradução. Autor/canal não identificados na transcrição (o autor menciona ter um curso de programação COBOL, link "na descrição"). Adicionados apenas pontuação, parágrafos e títulos; erros de reconhecimento corrigidos por contexto.

Termos corrigidos (reconhecimento automático): "Cobal / Coboy / Coball / Incobol" → COBOL; "Assemble" → Assembly; "DMP" → DXP (Digital Experience Platform); "ARC / Ark / Ax" → ARC (Analysis and Renovation Catalyst, IBM); "Watson X / watsonex / Axonex / Oxonex" → watsonx; "Gol Live" → go-live; "piamou" → "faz o acompanhamento"; "Departamento de tecnologia da Califórnia" mantido como no áudio (provável California Department of Technology). **Truncamento:** o ano do go-live no áudio sai como "janeiro de 202" (provavelmente 2027; não confirmado).

---

## O problema: antes de traduzir, descobrir o que o sistema faz

Imagine receber a missão de substituir um sistema de 6 milhões de linhas de código escrito em COBOL e Assembly, que começou a ser construído no final dos anos 70, tem cerca de 2.500 programas e atende mais de 33 milhões de motoristas. Por onde começar? A resposta óbvia: montar uma equipe, escolher uma tecnologia, ler os programas e converter o código. Mas o Departamento de Veículos da Califórnia (DMV) tinha um problema anterior: antes de substituir os sistemas, precisavam descobrir **o que o sistema faz**. Foi aí que entrou a inteligência artificial.

## O projeto DXP

O DMV da Califórnia conduz o projeto **Digital Experience Platform (DXP)**. O objetivo declarado é substituir gradativamente os sistemas que rodam no mainframe por uma plataforma distribuída. Não são sistemas departamentais: são os sistemas que garantem o core do DMV. O programa é plurianual e executado em etapas — algumas funções já foram transferidas para a plataforma nova, outras ainda rodam no mainframe.

Uma das maiores dificuldades (ainda hoje) é descobrir as regras de negócio que se consolidaram no sistema do mainframe nos últimos 50 anos. O problema não era ter 6 milhões de linhas de código; era saber **por que cada uma daquelas linhas estava ali**.

A IBM participou da fase de discovery e fez um levantamento inicial: se a análise das regras de negócio fosse feita manualmente, levaria cerca de **5 anos** — só para extrair as regras.

## Por que o risco é alto

O DMV atende mais de 33 milhões de motoristas e portadores de identidade do estado, administra mais de 35 milhões de veículos e arrecada mais de 14 bilhões de dólares por ano. É como o Detran do estado da Califórnia: aplica políticas públicas e a legislação sobre veículos, identidade e habilitação, controla esses registros e se integra com outros órgãos públicos. Interpretar incorretamente uma regra afeta não só o DMV, mas os órgãos com quem ele conversa, a população e a forma como a legislação é aplicada — pode provocar caos no serviço público.

Por isso o projeto não pode começar pedindo a uma IA: "pega essas linhas de COBOL e traduz para Java". Antes de traduzir ou reescrever, é preciso entender por que aquilo está ali — recuperar o conhecimento que está no código.

## O conhecimento já se perdeu em parte

Os programas rodam no dia a dia, mas parte do conhecimento sobre eles já se perdeu. É um problema mundial da plataforma mainframe: desligamento, aposentadoria, afastamento, transição de carreira — o conhecimento vai embora com o especialista. O sistema processa milhões de transações por dia, mas poucas pessoas dominam o que partes dele fazem, e há partes que ninguém conhece mais. A única documentação possível — a única verdade — está no código-fonte.

## O que a IA fez de verdade

A contribuição da IA foi importante, mas diferente do que muita gente imagina (Claude Code, ChatGPT, Codex). Não se entregou 6 milhões de linhas ao LLM perguntando "me explica o que esse sistema faz". O processo foi:

1. O código-fonte COBOL/Assembly dos 2.500 programas foi passado por uma ferramenta da IBM chamada **ARC (Analysis and Renovation Catalyst)**. Ela entende a linguagem e gera **análise estática, determinística**: a estrutura de cada programa, quem chama quem, quais campos e arquivos cada programa usa, dependências, o que precisa rodar antes de quê.
2. Essa informação estática alimentava o **watsonx**, um modelo LLM, que criava as **regras de negócio em linguagem humana**.
3. O resultado ARC + watsonx ia para **revisores técnicos** (especialistas em COBOL e mainframe), que analisam sintaxe e lógica, comparam o que o ARC gerou com o que o watsonx escreveu e verificam se tecnicamente faz sentido.
4. Os mesmos outputs iam para **revisores de negócio** (área de usuário), que verificam se a regra tem a ver com a legislação e com os processos internos.
5. A revisão humana **realimenta o processo** e melhora o ciclo seguinte. O ciclo continua, pois o projeto está em andamento.

## Por que duas ferramentas

O LLM trabalha com probabilidades: pode dar uma resposta perfeitamente coerente com uma conclusão errada, porque interpretou errado. A análise estática do ARC deu ao watsonx um conjunto de informações muito mais concentrado e restrito, o que **eliminou boa parte dos casos de alucinação** — ainda havia problemas, por isso o ciclo de realimentação. Já o modelo generativo permitiu produzir uma explicação em linguagem humana compreensível tanto pelo especialista técnico quanto pelo de negócio.

## Resultado

Nos primeiros 12 meses fizeram a varredura de regras de negócio em 5 milhões de linhas de código; a fase completa de discovery terminou em **15 meses**, contra os 60 meses estimados para a análise manual.

## Crítica do autor ao exagero

A IA **não reescreveu** automaticamente os sistemas do DMV. Criou uma base organizada de regras de negócio e de informações sobre o sistema, que facilitou as fases seguintes e acelerou a leitura do código. Quem "bateu o martelo" (isso está certo, ajusta isso, acerta esse harness) foram os especialistas — técnicos (COBOL, mainframe, IA) e de negócio. A IA localiza e organiza com uma velocidade que nenhuma equipe humana alcançaria, mas depende de pessoas fazendo a pergunta certa do jeito certo e com capacidade de verificar se a resposta faz sentido.

## Estado do projeto

O DXP começou formalmente em 2021 e segue em andamento; algumas funcionalidades já rodam na plataforma nova. Em 2026 estava previsto entregar o sistema mais importante, o de **registro de veículos**, mas houve problemas: no final do ano passado o DMV **cancelou o contrato com a empresa integradora** do projeto, e a entrega atrasou várias vezes. A data prevista para o go-live agora é "janeiro de 202[?]" (truncado no áudio). Depois vem uma fase de estabilização do sistema de controle de veículos e o planejamento/execução das **ondas de migração** dos sistemas seguintes. Previsão de término: **2029**, custo estimado de **US$ 767 milhões**.

Como projeto público, é acompanhado por outro órgão (o departamento de tecnologia da Califórnia), que deu **nota vermelha em julho** no quesito **qualidade do software** — possivelmente efeito do problema com a integradora (hipótese do autor).

## Conclusões do autor

- Modernizar um sistema corporativo não é rápido, não é barato e não depende de escolher a ferramenta da semana.
- O mais difícil é descobrir décadas de regras de negócio que só existem no código-fonte, resolver dependências e identificar o que é mais arriscado, para montar o cronograma das ondas ("esse sistema vai na frente desse porque aquele é arriscado demais, é melhor esperar").
- Por isso esses projetos duram anos e muitas vezes não chegam ao fim; gastam centenas de milhões na expectativa de um retorno que o patrocinador muitas vezes nem estará lá para ver.
- Acompanhar o que dá certo e errado nesses projetos ensina mais do que tutorial de IA.
- Esses projetos vão continuar acontecendo, e durante muitos anos o profissional que conhece mainframe e COBOL será essencial para levá-los até o fim.
- O autor anuncia um curso de programação COBOL na prática (link na descrição) e que falará mais de projetos de modernização de mainframe ao longo do mês; pede sugestões de casos nos comentários.
