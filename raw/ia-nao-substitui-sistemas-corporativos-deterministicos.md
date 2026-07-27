# IA não substitui sistemas corporativos determinísticos

Você deve ter visto essa notícia nos últimos dias: um monte de empresas grandes, as maiores do mundo, estão reduzindo ou cancelando projetos de inteligência artificial. E isso é estranho, né? Porque ao mesmo tempo a mesma imprensa fala em revolução da IA, superinteligência, agentes inteligentes, substituição de emprego. Então como que essas duas coisas se encaixam? Como que uma tecnologia que parece ser tão impressionante tá decepcionando algumas empresas?

A resposta para isso, eu acho, pode tá acontecendo por uma confusão: em alguns desses projetos a gente tá tentando usar a IA para fazer o trabalho que era de software tradicional.

## Um caso real

Eu vou começar com um caso real. Outro dia eu acordei com uma ideia que eu achei sensacional: eu ia substituir os scripts de validação de tarefa do curso por validadores inteligentes. Eu só tinha que juntar a especificação da tarefa, o programa que o aluno construiu ou alterou, juntava isso com as evidências de teste, fazia um prompt para amarrar tudo isso e chamava a API da IA, e ela me dava um feedback.

Esse feedback ia ser melhor do que os scripts que eu tinha, porque além de verificar se as tarefas foram cumpridas, se os pré-requisitos foram cumpridos, a IA ia poder também sugerir melhoria de código, sugerir padronização, padrão de nomenclatura. Poderia dar uma resposta muito mais completa e melhorar muito a experiência do aluno. Ou seja, a ideia parecia perfeita.

E funcionou — até que começou a parar de funcionar. Depois de três semanas batendo cabeça com ChatGPT, Claude e Gemini, eu fui percebendo que alguns programas que estavam certos, a IA reclamava de alguma coisa; programas que estavam incompletos, claramente incompletos, a IA dava como aceitável. Por exemplo, tinha caso em que a variável nem tinha sido definida no working storage, mas a IA considerava que tava tudo certo.

## Por que isso acontecia

Depois de muita dificuldade — alguns casos funcionavam, outros não — eu comecei a conversar com a própria IA para tentar entender por que ela não conseguia fazer uma coisa que parecia ser a área de especialidade dela: analisar contexto, analisar conteúdo, analisar código, e me dar um feedback.

A resposta eu achei interessantíssima, e foi a mesma nas três IAs que eu tava usando: "Você tá tentando usar uma ferramenta de análise semântica para fazer análise determinística." A IA é boa para analisar contexto e fazer resumo, mas ela é péssima para reproduzir resultados sempre da mesma maneira.

Para você ter uma ideia, os agentes não conseguiam identificar nem se o programa tinha sido codificado em free format ou fixed format. Porque quando ele pega um programa fonte, ele não lê o programa linha a linha como a gente faz — ele transforma aquilo tudo em tokens, vai criando contextos para aquilo, e gera a resposta a partir de probabilidade que ele conhece. E nem sempre essa resposta vai estar 100% certa.

O problema não era falta de conhecimento de COBOL — COBOL, os três agentes conhecem como ninguém. O problema era outro: eu tava tentando usar uma ferramenta probabilística para executar uma tarefa que precisava de um resultado determinístico.

## Determinismo importa

Agora pense em um banco, pensa num sistema que calcula juros, calcula imposto, calcula salário. Quando esse sistema recebe um input, ele precisa gerar um output completamente previsível, 100% previsível. Isso tem que acontecer hoje, amanhã, daqui a 5 anos. Para determinadas atividades não tem espaço para criatividade — acho que esse é o ponto. Não existe espaço para interpretação, não existe espaço pro "quase certo". E é exatamente por isso que sistemas corporativos são construídos com regras rígidas e comportamento previsível.

E aqui que tá o ponto que eu acho que muitas empresas descobriram, ou tão descobrindo, quando investem pesado em IA: modelos de IA são excelentes para interpretar, reconhecer contexto, são excelentes para resumir documento. Você pode resumir, gerar uma ata de reunião a partir da transcrição do que foi falado, de 10 maneiras diferentes se você pedir 10 vezes — e isso é aceitável nesse tipo de tarefa. Mas interpretar não é a mesma coisa que executar um processo de negócio.

Se uma empresa tenta substituir um sistema inteiro por IA achando que ele vai conseguir repetir aquilo com muito mais facilidade, ele vai conseguir ser criativo, ser interpretativo, mas ele não vai resolver os problemas que o software tradicional resolve. A empresa descobre que tá usando a IA para uma tarefa que ela não foi projetada para executar — como usar um carro de corrida para arar um campo, usar uma chave de fenda para pregar um prego na parede. O problema não é a chave de fenda, o problema é a tarefa que você tá esperando executar com ela.

## Para onde o modelo caminha

Depois dessa experiência eu fiquei com a impressão de que o modelo vai caminhar para uma outra direção: a IA vai interpretar coisas, mas quem vai tomar decisões é o software, é o sistema do jeito que a gente conhece. A IA entende o que o cliente quer, o software é que vai gerar a transação. A IA resume um contrato, mas quem registra o processo é o sistema tradicional.

Quando a gente lê na imprensa sobre os projetos que estão avançando, que estão sendo mais bem-sucedidos, pode reparar que todos eles têm essa característica: a IA vai até um determinado ponto, e depois disso o resultado é entregue pro sistema que faz o processamento lógico que a gente conhece.

## O que isso significa para quem trabalha com mainframe e COBOL

Isso tem uma consequência interessante para quem trabalha com mainframe, com COBOL e com sistemas corporativos. Muita gente — a gente ouviu falar muito disso esse ano — acredita que a IA vai substituir o próprio desenvolvedor, vai substituir o próprio processo de construção desses sistemas. E eu acho exatamente o contrário: a existência da IA tá tornando mais evidente a importância dos sistemas previsíveis.

Quando bilhões de reais estão em jogo, a característica mais importante do sistema que vai tratar aquilo não é a inteligência dele, é a previsibilidade, é a sua confiabilidade, é a sua consistência, é a sua capacidade de reproduzir o mesmo resultado milhões de vezes sempre da mesma maneira. E é exatamente isso que os sistemas corporativos fazem há décadas.

Então quando você lê uma notícia dizendo que um grande projeto de IA fracassou, não culpe a tecnologia. Não é a tecnologia de IA que tá fracassando, não é porque ela é uma bolha, não é só uma modinha — pelo contrário, ela é realmente revolucionária. A pergunta certa é: a IA tava sendo usada nesse projeto para interpretar informações, ou ela tava pretendendo substituir o software tradicional?

## Pergunta para reflexão

Você acha que a IA realmente vai substituir os sistemas tradicionais, ou vai surgir um modelo onde as duas coisas vão cooperar?
