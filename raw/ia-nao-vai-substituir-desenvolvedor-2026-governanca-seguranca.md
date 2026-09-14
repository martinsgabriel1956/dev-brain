# IA em 2026: Por Que Ela Não Vai Substituir o Desenvolvedor — Processos, Governança e Segurança

> Transcrição de vídeo sem roteiro sobre o momento atual da inteligência artificial no dia a dia das empresas — não sobre lançamentos de modelos (ex.: Kimi 3) ou notícias de bigtechs, mas sobre problemas reais discutidos com líderes de grandes empresas brasileiras (bancos, e-commerces, companhias faturando R$5-10B+) em consultorias.

---

## IA não vai substituir o desenvolvedor

Visão do autor: não é uma questão de os modelos ficarem melhores — os modelos atuais já geram código excelente na maioria das situações, resolvendo problemas reais do dia a dia. O ponto é outro: o código gerado continua **incompleto**, e não por falta de conhecimento técnico (framework, compilador, network, arquitetura — a IA já domina bem esses tópicos).

O problema real é que **orquestrar informação para obter um bom software continua sendo trabalho humano**: tomada de decisão, revisão, controle sobre o que a IA deve gerar. O contexto técnico já está bem coberto pela IA, mas o contexto específico de cada empresa — suas particularidades de negócio — ainda está muito longe disso. Falta ferramental para isso, e muitas vezes falta também **mudar os processos** das empresas para incorporar isso de verdade.

## Repensando processos: sprints e tamanho de tarefas

Exemplo de provocação que o autor tem feito em algumas empresas: será que ainda faz sentido ter sprints de duas semanas? Ao invés de continuar quebrando tarefas em pedaços cada vez menores (como se fazia com estimativa em Fibonacci — "se for maior que 21, quebra"), talvez faça sentido ter **tarefas cada vez maiores**, com sprints menores (uma semana, três dias).

Raciocínio: um desenvolvedor backend não é totalmente leigo em frontend (e vice-versa) — normalmente tem uma noção das outras camadas. A IA consegue preencher bem esse gap de conhecimento. Se o problema não está na complexidade da especificação ou da regra de negócio ser difícil de entender, é melhor o dev pegar tarefas maiores e entregar mais rápido. Se a entrega não tiver qualidade, refaz — porque **o custo e o tempo de gerar um novo código hoje é extremamente baixo**.

O que passa a importar mais é: **traduzir bem a regra de negócio para código eficiente**.

## Conhecimento técnico + conhecimento de negócio = ouro

Discorda da tese de que agora "quem manda" é o profissional de negócio/de visão analógica, e que o desenvolvedor perderia importância. O raciocínio contrário: o desenvolvedor consegue adquirir conhecimento de negócio rápido, partindo de uma base técnica que ele já tem — e esse conhecimento técnico **não foi descartado**, continua muito relevante. A questão é *como* ele é usado.

Quando conhecimento técnico se combina com conhecimento de negócio, isso "vira ouro". Antes da IA, era comum ter desenvolvedores muito técnicos mas pouco interessados em regra de negócio (o autor se inclui nesse perfil). Agora, cada vez mais é preciso ter profissionais tecnicamente bons que também façam esse esforço de entender a regra de negócio — isso encorpa as entregas, não só em quantidade/produto, mas em **qualidade**.

Antes, havia "go horse" (acelerar sem cuidado) mesmo com conhecimento técnico disponível. Hoje, como o código é gerado muito mais rápido, os ciclos encurtam — e isso significa **falhar mais rápido também**, com custo de falha menor. Falhar não é mais tão problemático.

## Ciclos menores liberam tempo para qualidade

Com sprints menores e mais automação (esteiras, harness engineering para melhorar contexto/agentes), sobra tempo para focar no que antes ficava sempre de lado por falta de tempo/incentivo: bons casos de teste, quality gates fortes, foco real em qualidade. Isso é algo que os times já queriam fazer, mas nunca era priorizado quando "tudo era prioridade".

Essa mudança não é uniforme — a maioria dos lugares ainda não mudou como pensa sprints e testes.

### Contraponto: isso não vai sobrecarregar os devs?

Pode ser uma questão cultural da empresa, mas também pode ser um respiro: se uma sprint que levaria um mês passa a ser entregue em uma semana, por que não dar uma folga ao time, ou uma sprint mais leve focada em débito técnico, ou premiar quem entrega assim? Esses questionamentos já estão acontecendo dentro das empresas — não é consenso, e não vai ser realidade em todo lugar (e onde for, vai levar tempo), mas a pergunta já está em pé.

## Governança: um assunto pouco falado no mainstream

Em times técnicos de grandes bancos, e-commerces e outras empresas de grande porte no Brasil, governança de IA é tema central — mas quase não aparece nos principais canais/vídeos, talvez por não gerar tanto hype ou engajamento. Temas citados: como governar, gerenciar, visualizar e controlar gastos de IA na prática.

## Segurança: para além de "o que a IA pode responder"

A preocupação não é mais só "o que a IA pode/deve responder" e ter visibilidade sobre isso — é também **como controlar o que ela não deveria responder** e como não sofrer ataques de **anomalia**.

### Caso emblemático: ataque à Alibaba/OpenAI

Caso citado como mais conhecido: um ataque de destilação contra a OpenAI atribuído à Alibaba, usando ~25.000 contas falsas e um número muito alto de interações (valor exato não lembrado) para tentar destilar o modelo (extrair como ele responde/funciona/foi treinado).

### O risco real é outro: extração de dados com poucas interações

Percepção equivocada comum: acham que, por o ataque de destilação exigir milhões de interações/contas falsas, esse tipo de risco é distante da realidade das empresas comuns. Mas se o objetivo do atacante não é destilar o comportamento do modelo, e sim **extrair dados expostos ao agente** (o conhecimento proprietário da empresa embutido no contexto), bastam **5-6 interações bem feitas** para fazer uma engenharia reversa e extrair informações que o modelo nunca deveria revelar.

Esse tipo de ataque é chamado de **ataque/verificação de anomalia**: como detectar comportamento anômalo para saber que uma LLM exposta via agente está sob ataque — hoje ainda é difícil até perceber que o ataque está acontecendo.

## Conclusão

Esses temas (repensar processos ágeis, governança, segurança contra ataques de anomalia/extração de dados) não substituem o "feijão com arroz" do desenvolvimento — a IA gerando ~100% do código continua relevante — mas são as **novas temáticas de 2026** que separam quem está se preparando de quem não está. O autor recebe consultorias frequentes sobre esses assuntos e reforça que é um mercado aquecido, pouco coberto no mainstream, mas muito discutido dentro das empresas grandes.
