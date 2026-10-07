# Erros que devs brasileiros cometem ao aplicar para vagas na gringa (Augusto Galego)

> **Fonte:** transcrição de vídeo (autor se refere a si como "Galego"; canal de Leetcode/System Design), colada pelo usuário em 2026-10-07. Já em português; sem tradução.
> **Limpeza:** pontuação e parágrafos adicionados; erros de ASR corrigidos ("déveis" → devs; "Cloud Code" → Claude Code; "Elite Code"/"Lit Code" → LeetCode; "Postgress" → Postgres; "semicolum" mantido como dito; "vi 'galego'/'galego solutions'" mantido como exemplo). Trechos omitidos: patrocínio da "UVP" (escola de investimentos, cartão black, sala VIP) e divulgação final do curso "Roadmap pro seu próximo emprego" e do bônus de internacionalização.

---

## Abertura

Lista, em formato de conversa pouco estruturada, de erros que o autor vê devs brasileiros cometendo ao aplicar para empresas estrangeiras. Todo mundo pede ajuda com isso; o autor já fez entrevistas na gringa, já trabalhou para empresas de fora e já contratou brasileiros para trabalhar na gringa.

## Erro 1 — Inglês (um erro duplo)

Algumas pessoas acham, erroneamente, que precisam de um inglês perfeito, e isso as faz procrastinar e não aplicar. É um erro gigantesco: ao trabalhar numa empresa gringa, vê-se que muitas pessoas não têm inglês excelente, têm um inglês bom, que dá para conversar, com dificuldade em alguns termos técnicos. Exemplo: pergunte a um italiano, francês ou espanhol como se chamam em inglês os símbolos do teclado; muitos não sabem. O autor mesmo hesita (ponto e vírgula = *semicolon*; dois pontos = *colon*, que ouviu espanhóis chamarem de "two dots"; `|` = *pipe*; `\` = *backslash*; `/` = *forward slash*). Se você não sabe nada disso, não tem problema; a maioria também não sabe.

A outra metade do erro: não dá para passar numa entrevista só "na cara de pau"; o inglês tem que ser OK. Costuma-se dizer que o inglês para trabalhar fica entre B1 e B2, mas o autor não gosta de cravar essa regra: ter inglês para *viver* em inglês é diferente de ter inglês para *conversar sobre software* em inglês. É preciso dominar o linguajar (*clients, software, back pressure, queues, lists, service, modules, databases*) mais do que tempos verbais elaborados ("eu teria feito tal coisa caso outra coisa não tivesse...").

## Erro 2 — Storytelling

Numa entrevista a pessoa quer saber três coisas: (1) se você é técnico e resolve problemas; (2) sua capacidade de comunicação (trabalho em empresa é trabalho em equipe); (3) sua capacidade de liderar (mesmo sem liderar pessoas hoje, você pode liderar um projeto ou ser a cabeça por trás de uma feature).

Dificilmente você convence alguém se não consegue contar uma historinha. Não é para mentir ou inventar: as pessoas são muito ríspidas e diretas nas respostas e não percebem como quem pergunta está visualizando aquilo.

Exemplo ruim: "Como foi seu trabalho na última empresa?" → "Foi bom, trabalhei com Java e Postgres, fui elogiado." Resposta "um lixo". Outro: "Um projeto difícil de que você se orgulha, e por quê?" → "Migração do Java 8 pro Java 9, foi difícil, fiz horas extras, entregamos no prazo e fiquei feliz." Responde à pergunta, mas não mostra capacidade técnica, nenhum desafio técnico, boa comunicação, nem o *porquê* específico do orgulho.

Melhor: contar uma história que envolva desafios técnicos resolvidos, impacto no cliente, como foi mensurado e por que foi importante para a empresa. Muita gente peca nisso, provavelmente por nervosismo: trava e tenta responder o mais rápido possível para se livrar da pergunta.

**Sugestão:** pegue essas histórias e ensaie (não decore palavra por palavra). Todo mundo diz que soft skill e networking são importantes; então sente e treine storytelling. Pegue um projeto muito desafiador e explique para alguém (espelho, bichinho de pelúcia, sua mãe), ressaltando os pontos que demonstram dificuldades, impacto no cliente, por que foi valioso para a empresa, como contornaram desafios. Vão perguntar dessa história.

## Erro 3 — Não investir (fora de entrevista)

*(Trecho patrocinado, omitido: escola de investimentos. Ideia geral: o dev dedica a carreira inteira a ganhar dinheiro e vale dedicar algumas semanas a aprender a cuidar bem dele.)*

## Erro 4 — Não treinar LeetCode e System Design

O autor admite "puxar a sardinha": criou o canal baseado em LeetCode e System Design porque viu que ninguém no Brasil prestava atenção nisso. Entrevistas na gringa muito comumente cobram LeetCode e System Design, porque as empresas ainda não adaptaram o processo de contratação e não estão usando IA muito bem para contratar. As Big Techs, em resposta, trouxeram LeetCode e System Design para o formato **presencial**, para impedir "colar" com IA em entrevista remota. Não tem muito o que dizer: você tem que se preparar.

**Como começar LeetCode:** abra o LeetCode e comece por *array*; faça exercícios de *two pointer* e *sliding window* (os mais simples); depois procure outros padrões. Faça uns 10 exercícios de two pointer até entender o padrão. Se quebrar a cabeça e não conseguir resolver, olhe a resolução, decore, escreva-a e vá para o próximo: é uma maneira bem mais efetiva de aprender do que derivar do zero.

**Como começar System Design:** aqui recomenda estudo *antes* da prática. Estude os building blocks primeiro: banco de dados, load balancer, API gateway, lambda/serverless, um pouco de networking, a relação client-server, microsserviços, monolitos. Não tem como fugir. É o mínimo do mínimo: com isso você talvez não passe, mas sem isso você roda numa entrevista que cobre LeetCode ou System Design.

## Erro 5 — Não explicar o porquê das coisas

Exemplo: na empresa do autor, no passado, migraram um grande monólito para microsserviços. *Por que* (e não só escalar o servidor, ou trocar de linguagem)? *Como* foi tomada a decisão, quem decidiu, como foi feito? É muito fácil só explicar "caiu no meu colo uma task de implementar login com Google". Mas: por que estamos fazendo isso? Quais desafios (já existe um login; o usuário já tem um e-mail e pode entrar com o mesmo e-mail via Google)? Como resolveram os problemas decorrentes? Isso falta e volta ao storytelling.

## Erro 6 — Silêncio/passividade na parte técnica

Vale para LeetCode, System Design e qualquer desafio técnico. O entrevistador passa um desafio ("escreva Fibonacci") e o candidato fica em silêncio pensando, ou balbucia código sem explicar ("x = n... não, um while... count igual a n... não, vamos colocar um response..."). O entrevistador vê alguém que parece falar sozinho sem lógica compreensível e que entrega uma solução sem ter feito nenhum questionamento.

Melhor: começar perguntando ("Fibonacci dá para resolver de forma recursiva ou iterativa? Iterativa costuma ser mais rápida, principalmente em Python; vamos de iterativa. Que parâmetros posso receber? Preciso checar se o número é negativo?"). O entrevistador é uma parte **colaborativa** do processo; cada um tem seu estilo, mas ele está ali para você conversar e mostrar que seu raciocínio é bom. Se você não mostra o raciocínio, ele não consegue medi-lo, nem te contratar. Não tenha passividade em nenhum tipo de entrevista técnica.

## Erro 7 — Chegar despreparado na empresa

A pessoa mal sabe o nome da empresa, o que faz, quantos funcionários tem, em que etapa está, se é lucrativa, que software desenvolve. Pergunta da entrevistadora: "O que te chamou atenção na Galego Solutions LTDA?" Resposta ruim: "O vale-alimentação; vi que é uma empresa inovadora que faz softwares inovadores." Não cola.

Pesquise a empresa e vá preparado para *aquela* entrevista. Não precisa de horas: **15 minutos** (no auge da preguiça) já servem. Dica operacional: jogue o link da empresa no Claude Code ou no GPT, peça um resumo do que a empresa faz e diga "sou software engineer aplicando para tal vaga; que perguntas legais posso fazer à pessoa do RH sobre a empresa que demonstrem interesse?". Depois leia você mesmo, estude um pouquinho e, nos pontos que chamarem sua atenção, faça perguntas pertinentes. Se já trabalhou no nicho da empresa, pergunte como resolveram um problema que você conhece (ex.: gateway de pagamentos: "quando trabalhei com isso tive muito problema de cartão de crédito recusado; vocês têm equipe dedicada? algum algoritmo de machine learning?"). Isso demonstra interesse.

## Fechamento

O autor reconhece que nada disso difere de se preparar para uma entrevista no Brasil, e é verdade. Depois de ~6 anos no Brasil e ~5 para empresas de fora, na sua visão pessoal (de uma só pessoa), não existe mágica que separe uma empresa brasileira de uma americana além de uma faturar em dólar e a outra em real: se não fosse pelo idioma, talvez não notasse diferença em muitos casos. Você não precisa ter medo de aplicar para a gringa; não há nada de especial numa empresa gringa que você talvez já não saiba.

*(Divulgação final do curso "Roadmap pro seu próximo emprego" omitida.)*
