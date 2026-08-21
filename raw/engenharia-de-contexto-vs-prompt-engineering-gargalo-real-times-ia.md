# Engenharia de Contexto vs. Prompt Engineering — o Gargalo Real dos Times com IA

> Transcrição limpa e organizada em seções. Idioma original: português (Brasil) — sem necessidade de tradução. Autor/canal não identificado com segurança na transcrição (o locutor se dirige ao público como "meus queridos" e menciona algo como "Joel" logo na abertura, possivelmente um apelido ou nome de canal mal transcrito pelo reconhecimento de voz — não usado como base para atribuição de entidade).

## Abertura — o padrão observado

Revisando projetos com IA em empresas de tamanhos bem diferentes — startup, banco, indústria — o locutor identifica um padrão recorrente: times escrevem prompts caprichados e mesmo assim o resultado é medíocre. O time fica frustrado achando que o problema é "não saber pedir direito". Na visão do locutor, o problema geralmente não está só na pergunta — são duas coisas, e a segunda custa mais caro que a primeira.

## O boom do "Prompt Engineer" e suas duas promessas

Nos últimos dois anos, Prompt Engineering virou uma pequena indústria: cursos, e-books, templates, carrosséis de LinkedIn com "os 10 prompts que vão mudar sua vida". Duas promessas sustentam esse mercado:

1. **A fórmula da pergunta** — aprenda a técnica certa e a IA entrega o que você quiser.
2. **A aceleração** — a IA escreve um serviço em minutos, então o time entrega mais rápido (essa segunda promessa é retomada e questionada mais adiante).

Citando Frederick Brooks: não existe bala de prata — nenhuma técnica isolada resolve a complexidade essencial do trabalho de engenharia de software. O "prompt mágico" é, na visão do locutor, apenas o novo nome da bala de prata de sempre. Caímos nessa promessa porque é mais confortável comprar uma fórmula do que fazer engenharia.

## O que realmente se quer de uma IA de projeto

O que se busca não é uma IA que responda bem a uma pergunta isolada — qualquer modelo faz isso. O que se busca é uma IA que se comporte como **um membro sênior do time**: alguém que conhece o histórico do projeto, sabe por que uma gambiarra existe, sabe qual padrão o time segue e qual foi abandonado.

Analogia: o melhor sênior com quem você já trabalhou não precisava de três parágrafos de instrução — bastava meia frase, porque essa pessoa carregava anos de contexto do projeto na cabeça. A pergunta era pequena porque o repertório era gigante.

## A janela de contexto como limite físico

Todo modelo de linguagem trabalha com uma janela de contexto — sua memória de trabalho. O que está dentro da janela, o modelo enxerga; o que está fora, para ele **literalmente não existe** — não é que foi esquecido, é que nunca esteve lá.

Um projeto acumula anos de regras de negócio, decisões de arquitetura que vivem na cabeça de três pessoas, convenções não documentadas. Quando o prompt é enviado, na maioria dos casos quase nada disso está na janela. Na prática, isso equivale a dar instruções detalhadíssimas para uma pessoa vendada dentro de uma sala que ela nunca viu — e depois reclamar que ela esbarrou no móvel.

## Caso concreto: o serviço de cobrança recorrente

Em um dos projetos acompanhados, um dev pediu à IA para criar um serviço de cobrança recorrente. O prompt especificava idempotência, formato de resposta, tratamento de erro. A IA entregou um serviço limpo, testável, bonito de ver.

O problema: o projeto tinha uma regra central — nesse cliente, toda cobrança passa obrigatoriamente por uma fila de auditoria antes de ser efetivada. Essa regra estava documentada, mas em um arquivo que a IA nunca viu. Resultado: código bonito e inútil. Refazer custou mais caro do que escrever do zero, porque primeiro alguém precisou descobrir que estava errado.

O diagnóstico padrão nesses casos costuma ser "seu prompt estava ruim, faça outro curso, aprenda a técnica nova" — um diagnóstico que, segundo o locutor, erra o alvo: a energia do time estava toda no lugar errado, otimizando detalhe (o prompt) em cima de uma fundação que não existia (o contexto do projeto).

## Engenharia de Contexto: os três movimentos aplicados

Em um dos projetos, o time parou de mexer no prompt e redirecionou toda a energia para a pergunta "o que esse modelo precisa enxergar para decidir bem?". Três movimentos:

1. **Transformar conhecimento implícito em artefato.** Regras de negócio, decisões de arquitetura e seus porquês, convenções do time — tudo escrito curto e direto em arquivos que vivem junto do código e são versionados com ele.
2. **Dosagem — divulgação progressiva.** Mais contexto não é melhor contexto: despejar tudo na janela afoga o essencial no acessório. A organização foi em camadas: uma visão geral sempre presente, e detalhes que só entram quando a tarefa pede. O modelo recebe primeiro o mapa, só depois a rua específica onde vai trabalhar.
3. **Exemplos reais do próprio projeto.** Em vez de descrever uma convenção em abstrato, mostrar dois trechos reais de código que seguem o padrão — o modelo aprende muito melhor por exemplo do que por descrição.

Resultado relatado: o mesmo modelo, com prompts medianos, passou a entregar código que respeitava a fila de auditoria, seguia a convenção de nomenclatura e usava o módulo certo. Nada mudou no modelo — mudou o que ele enxergava.

## Velocidade de geração de código ≠ velocidade de entrega

Isso resolve só metade do problema. A IA gera código rápido — mas ler "geração rápida de código" como "entrega rápida" é, na visão do locutor, uma leitura perigosa.

Ao desenhar o fluxo de ponta a ponta (refinamento → desenvolvimento → revisão → teste → homologação → aprovação → deploy), se o ciclo fecha em duas semanas e o tempo de *escrever* código cai pela metade, o ganho fica limitado ao peso que essa etapa representa no ciclo total — as outras etapas continuam do mesmo tamanho.

Esse recorte não é universal: para um empreendedor validando uma ideia sem orçamento para um sistema robusto, código gerado rápido é uma vantagem real — muda o jogo, tira do zero e coloca no ar. Já para um dev num projeto com integração com legado, compliance e muita gente dependendo daquilo, escrever código rápido raramente foi o gargalo.

## Evolução vs. Revolução

Distinção central do vídeo:

- **Evolução** — fazer o que já se faz hoje, só que melhor e mais rápido.
- **Revolução** — mudar o jeito de pensar, o processo, o papel, como as pessoas enxergam o próprio trabalho.

Tratar a IA como evolução significa plugar a ferramenta no processo existente e esperar o ganho aparecer — e ele aparece, só que pequeno, porque o processo foi desenhado em cima de restrições que a ferramenta acabou de mudar.

### Exemplo aplicado: o tamanho da sprint

A sprint de duas semanas é padrão de indústria. O locutor relata experimentar reduzir esse número em projetos menos complexos — uma semana no melhor caso, até três dias. Isso quebra o timebox tradicional, e o locutor está confortável com essa quebra: o timebox não é objetivo, é meio — foi desenhado para criar ritmo de feedback num mundo onde escrever código custava caro. Esse custo mudou de lugar. Produzindo e revisando mais rápido mas mantendo a janela de feedback em 14 dias, o time só acumula trabalho não validado. Manter a caixa do mesmo tamanho por respeito ao ritual é, na prática, tratar a IA como evolução, não revolução.

## Por que evitar a discussão de métricas de velocidade agora

Diante da pergunta "quanto subiu a velocidade / throughput / pontos por sprint", o locutor evita entrar nessa discussão — não por estar fugindo, mas por prioridade: o que se observa nos projetos é a aceleração da entrega de um **produto robusto**, não só do software. Antes, ir rápido e entregar algo que aguenta operação/integração/auditoria ficavam em lados opostos da mesa. Encurtando o ciclo com contexto bem feito por trás, as duas coisas passam para o mesmo lado — um resultado mais expressivo do que qualquer métrica de velocidade que se pudesse medir antes da IA.

Argumento complementar: velocidade, performance e throughput são conceitos definidos numa época em que o gargalo era a capacidade de uma pessoa (ou time) escrever código. Se o gargalo mudou de lugar, a régua de medição também precisa mudar — por isso o locutor prefere não amarrar a decisão de hoje a uma régua que está prestes a ser trocada. Isso não resolve o problema sozinho, mas gera movimento, e movimento gera as perguntas desconfortáveis que seriam necessárias para evoluir.

## Questionando o dogma da tarefa pequena

Um desses movimentos incômodos: por que a obsessão pela tarefa pequena? Um dos motivos históricos é reduzir risco para caber na cabeça de uma pessoa só — daí a separação tradicional entre tarefa de back-end e tarefa de front-end, cada dev forte numa ponta.

O custo escondido dessa separação aparece na hora de juntar as partes: retrabalho, falha de comunicação, integração que não aconteceu como esperado. Consertar exige as duas pessoas boas, ao mesmo tempo, disponíveis — ou melhor, *indisponíveis* para o resto do trabalho. O retrabalho não custa uma pessoa: custa duas, mais a coordenação entre elas.

### O arranjo alternativo proposto

Dentro de um escopo, uma pessoa forte em uma das pontas (não precisa ser excelente nas duas) mas com conhecimento excelente do negócio, apoiada por agentes que cobrem a compreensão técnica da ponta mais fraca — essa pessoa entrega a feature de ponta a ponta e responde por ela por inteiro.

Resumo: tarefa maior, menos costura, menos handoff — o dev volta a ser dono de um pedaço do **produto**, em vez de dono de um pedaço da **camada**.

## As duas engenharias (e por que dev experiente ganha, não perde)

O que a IA enxerga do projeto (engenharia de contexto) é uma frente. Onde ela trabalha — o ciclo, o tamanho da tarefa, quem responde pela entrega (redesenho de processo) — é outra. As duas são trabalho de engenharia: têm trade-off, estrutura, manutenção. É por isso que, na visão do locutor, o dev experiente tem vantagem nesse jogo, não desvantagem.

## A inversão da lógica ao longo do vídeo

1. No início, o prompt era protagonista e o contexto, detalhe.
2. Depois, o contexto virou o produto.
3. No fim, o processo — a parte que a maioria dos devs prefere não olhar — vira o limitador do quanto se consegue extrair da IA.

### Consequência de carreira

Enquanto muita gente disputa quem escreve o prompt mais bonito, duas habilidades mais raras estão sendo formadas em silêncio:

1. Estruturar conhecimento de projeto para a máquina (e para as pessoas) consumirem.
2. Redesenhar o jeito como o time trabalha em cima disso.

Quem domina as duas vira peça central do time — o locutor relata ter visto isso acontecer de perto.

## Perguntas deixadas para o público

1. O que o modelo enxerga do seu projeto quando você pede algo?
2. Se amanhã a IA escrevesse todo o código do seu time em uma hora, quanto tempo a entrega ainda levaria para chegar ao cliente?

Se a segunda pergunta assusta mais que a primeira, esse é o gargalo real do time.

## Encerramento

Convite para compartilhar com colegas que colecionam templates de prompt e para comentar o tamanho atual da sprint do time e o que aconteceria se ela virasse uma semana.
