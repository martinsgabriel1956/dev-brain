# Story Points, Scrum Master e PO — Por Que Forçar 30-40 Pontos por Sprint Está Errado

**Autor/Canal:** Lucas Badico (Akita)
**Formato:** Transcrição de vídeo (YouTube), já em português — sem necessidade de tradução

## A Pergunta que Originou o Vídeo

Pergunta feita no grupo de mentorados do autor:

> "Pessoal que trabalha com Scrum e Story Points: quantos story points costumam fazer por sprint, e a sprint de vocês é de uma ou duas semanas? Pergunto porque o PO quer que sejam feitos 30 a 40 story points por sprint por pessoa."

O autor decidiu transformar as respostas do grupo em vídeo para discutir o papel do Scrum Master, do PO, e por que se usam pontos.

## Respostas dos Mentorados

**Bruno:** "É só jogar 20 pontos num CRUD que tu faz em três horas." — resposta não está errada: quando o PO pede um número X de pontos sem se importar com o valor real sendo entregue, ele está usando os pontos para se gabar ou atender demanda de quem está acima dele. Quando pontos são tratados assim, eles deixam de prestar para qualquer coisa.

**Thiago (segunda resposta):** "É igual apagar código, fazer commit, colar código, fazer commit — e deixar o GitHub verdinho." Uma métrica de exibição, uma métrica de ego, que não significa que o trabalho real está sendo feito.

**Italo (ex-colega do autor na Badil):**
- "Quando o PO quer forçar story points, é isso que acontece: os story points ficam inúteis."
- "Quando o time é novo, Story Points é só um chute. Tem que iterar algumas vezes para sentir a velocidade do time. Você chuta um valor, o time concorda, e esse valor passa a equivaler ao ritmo do time — independe da escala (pode ser bananas, maçãs, qualquer coisa)."
- Relato pessoal: no time em que entrou, quase todo mundo era novo (dev, technical manager, PM). Convencionaram que 1 story point = 1 dia (não é comum, mas fazia sentido porque não havia histórico algum, e por dia era mais fácil de estimar). Ficou ~10 pontos por dev por sprint. O technical manager acompanhou as métricas ao longo do tempo; hoje um ponto não equivale mais a um dia, e cada dev faz entre 12 e 16 pontos por sprint. O PM já prioriza com base nisso.
- Conclusão: o número arbitrário de pontos não significa nada por si só. Quando uma quantidade é forçada no time, a métrica perde todo o valor — não importa a escala, o que importa é se aquele número reflete a velocidade real do time.

**Thiago (autor original da pergunta):** "Story point aqui é baseado em complexidade... vejo [um colega] trabalhando 10 horas por dia e às vezes fim de semana para fazer os 40 pontos que ele se propôs."

## O Que São Story Points (Explicação para Quem Nunca Trabalhou com Agile)

Agile é um agrupamento de métodos e processos pensados primariamente para desenvolver software (hoje aplicado, nem sempre corretamente, a áreas fora de software).

Scrum é um desses processos/frameworks dentro do Agile. Tem várias cerimônias — seguir todas à risca pode consumir cerca de 1/3 do tempo da equipe só em cerimônias.

**Planning Poker:** cerimônia em que o time recebe os tickets/tarefas a serem feitas e "joga" um jogo de cartas — cada pessoa atribui um valor a uma tarefa numa escala qualquer (números primos, ímpares, Fibonacci etc.). O time precisa concordar em um valor comum:
- Se todos derem o mesmo valor de primeira, esse é o valor.
- Se houver divergência (ex.: 2, 5, 10), o time conversa até convergir.

O objetivo real do Planning Poker é fazer o time **conversar sobre a complexidade da tarefa**. Uma vez que o time está confortável com um número, esse número (ponto) é atribuído à tarefa. Os pontos de cada pessoa são somados ao final do sprint.

**Sprint:** é um **tempo fixo**, não uma entrega. Um erro comum é tratar sprint como sinônimo de deliverable ("sprint de entrega tal"). Se o trabalho planejado para aquele sprint não foi concluído, o sprint encerra do mesmo jeito e o que sobrou vai para o próximo — isso é o método padrão. Se sprints de duas semanas viram um mês ou 40 dias, o processo já não é Scrum de fato (mesmo que ainda seja tecnicamente "Agile").

**Sobre a escala dos pontos:** existem diversos padrões, cada time escolhe o seu, e o valor numérico em si pouco importa. O que importa é:
1. Constância — o time usa a mesma escala e o mesmo critério ao longo do tempo.
2. Tendência — o valor total de pontos entregues por sprint (velocity) deve se manter estável ou, idealmente, crescer.

Se um Scrum Master decide sozinho, na cabeça dele, que o time "precisa" fazer 30 ou 40 pontos por sprint — sem consultar o time para entender o impacto disso — ele já está errado. Uma equipe saudável consegue aumentar esses números organicamente ao longo do tempo, desde que a composição do time não mude constantemente.

## O Problema de Forçar um Número

- Forçar uma quantidade fixa de pontos por pessoa/por time faz a métrica perder qualquer valor, porque o número deixa de refletir a complexidade real do trabalho e passa a refletir apenas a pressão para "bater a meta".
- Reduz a colaboração: se o objetivo é "fechar meus pontos", o incentivo é não gastar tempo ajudando colegas durante o sprint.
- Pode levar a jornadas de trabalho excessivas para "bater a meta" (ex.: 10h/dia + fins de semana) sem remuneração extra correspondente — isso é sintoma de um erro de planejamento, não de falta de esforço do dev. Trabalho extra ocasional para lidar com uma situação pontual é aceitável; virar rotina não é.

## Crítica: "Agile Industrializado" (analogia com "o velho da caixa")

O autor compara Scrum Masters que cobram numerologia de pontos e cronometram cerimônias ("a daily tem que ter 15 minutos, se tiver 16 corta") a uma caricatura de microgerenciamento — o Scrum Master vira alguém que só confere se os cards foram movidos e se os pontos "batem", sem se interessar de fato pelo valor entregue, pelo conforto e pela continuidade saudável do time.

Ponto histórico: o Agile nasceu porque devs estavam exaustos de fazer crunch e entregar software ruim sob processos rígidos tipo Waterfall. A tese do Agile é que ele é **mais veloz** justamente porque valoriza o aprendizado contínuo e o bem-estar do time — não porque força mais output bruto.

Forçar a pessoa a escrever mais código ou fazer mais pontos não é a mesma coisa que ser mais veloz — pode parecer isso para quem não entende o processo por dentro. Usado dessa forma (números arbitrários forçados de cima para baixo, cerimônias cronometradas ao segundo), o Agile na prática não é diferente de um Waterfall: a única diferença é que garante alguém cobrando entrega semana a semana em vez de cobrar só no final do processo — o que é ruim do mesmo jeito, só que distribuído ao longo do tempo.

## Conclusão / Pergunta ao Público

O autor pergunta se quem está assistindo já viveu essa situação (PO/Scrum Master forçando uma meta arbitrária de story points), afirmando que qualquer dev com experiência suficiente provavelmente já passou por isso.
