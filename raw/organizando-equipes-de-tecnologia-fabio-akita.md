# Como Organizar Equipes de Tecnologia — Fábio Akita

> Nota de transcrição: transcrição via reconhecimento automático de fala (ASR), com trechos confusos, repetições e nomes possivelmente mal reconhecidos. Reorganizada e pontuada para leitura, mas o conteúdo é o mesmo do áudio original — nenhuma afirmação nova foi adicionada. Participantes: o entrevistado é identificado como Fábio Akita (detalhe que confirma a identidade: relato de ter sido consultor em projetos de unificação de sistemas da Vivo/Claro/Petrobras); há pelo menos um interlocutor não identificado com clareza (citado por "Guilherme" em um trecho), possivelmente apresentador ou produtor do canal onde a conversa foi gravada. Trechos de identificação incerta são marcados com `[transcrição incerta]`.

## Abertura

Hoje vamos fazer um bate-papo (no áudio soa como "bike shared") sobre equipes de tecnologia. Isso complementa um vídeo anterior do canal, e a ideia aqui é continuar essa discussão: uma equipe só de sêniors não funcionaria bem para a maioria absoluta dos casos.

Isso aparece o tempo todo em conversas com empresas: "estou precisando de mais sênior", "quero contratar só sênior", "quero que minha equipe inteira tenha X anos de experiência com a tecnologia".

`[transcrição incerta]` Antes de entrar no assunto, uma nota de apresentação pessoal: quem fala aqui não é o "outro" Fábio Akita conhecido como empreendedor — é o programador, fundador de uma empresa de desenvolvimento de software que avalia e contrata para projetos constantemente há cerca de 10 anos. Antes disso, a carreira foi como consultor, passando por empresas como Vivo, Claro e Petrobras, sempre no modelo de consultoria/Body Shop — contratação agressiva e um tanto absurda: em um dos casos, o RH de uma consultoria ligou avisando que "ia contratar" antes mesmo de haver confirmação de que a pessoa toparia — e ele já estava alocado no cliente sem nem saber. Isso ainda acontece hoje.

O ponto de tudo isso: o que se fala sobre mercado nesses vídeos não é teoria — é prática observada ao longo de 25 anos, desde agência de publicidade, consultoria, até hoje no mundo de startups. E existem padrões que se repetem o tempo todo. "Quem não conhece a história está fadado a repeti-la."

## Por que um time só de sêniors não funciona: a metáfora do pedreiro e do mestre de obras

Um pedido recorrente de cliente novo: "quero um time, me vê aí uns 5 sêniors para viagem." A resposta de sempre é: "me explica o seu projeto." Na prática, o cliente não precisa de 5 sêniors — precisa de 1 sênior, 1 pleno e 3 júniors.

A metáfora: é como alguém que quer construir a própria casa e diz "não vou contratar nenhum pedreiro, vou contratar só mestre de obras, porque o mestre de obras é mais experiente." Só que se você colocar um mestre de obras com 10 anos de experiência para ficar erguendo parede de tijolo o dia inteiro, ele vai reclamar — e com razão. Não é que o trabalho do pedreiro seja ruim; ao contrário, o pedreiro sabe erguer parede, só não sabe *mais* que isso (não tem a visão do mestre de obras). Um sênior de software forçado a fazer uma tela simples, responsiva, com CSS bonito, seria improdutivo nessa tarefa — um júnior faz isso mais rápido, porque é o trabalho do dia a dia dele.

Por outro lado, se você perguntar a um júnior "qual dessas arquiteturas escala melhor, qual vai ter menor custo", ele pode até ter um bom palpite, mas não tem a experiência de já ter passado por várias dessas decisões — o sênior já testou 20 opções ao longo da carreira e sabe que só 2 valem a pena; o júnior teria que testar as 20 para chegar à mesma conclusão, levando um tempo desproporcional.

**Conclusão prática:** o time ideal é sempre misto. O júnior precisa da experiência prática para aprender — para descobrir se a teoria que estudou realmente funciona. O sênior precisa da oportunidade de orientar o júnior para as decisões corretas — essa orientação é o que comprova se ele é sênior de verdade.

## Escalabilidade vertical vs. escalabilidade horizontal (aplicada a pessoas)

Um sênior que só estuda, estuda, estuda, sozinho, é como escalabilidade vertical: melhora o próprio "hardware" até um teto — "só tem 10 dedos", chega num ponto que não dá pra crescer muito mais sozinho. Escalabilidade horizontal é colocar vários "computadores" em paralelo: um sênior no centro (o "cérebro"), orientando dois ou três júniors ao lado. Isso multiplica a capacidade da equipe.

O júnior nesse modelo cresce rápido — não é "passar a mão na cabeça", é orientação prática. Com esse tipo de estrutura (sênior orientando com essa mentalidade), o crescimento que levaria 10-12 anos sozinho pode acontecer bem mais rápido, com o júnior chegando a um nível de trabalhar sozinho, quase sem precisar de orientação constante.

Isso porque cerca de 80% do trabalho do dia a dia é mundano/mecânico/repetitivo — decidir arquitetura ou escolher tecnologia é raro (episódico, talvez uma vez a cada 6 meses); no dia a dia é corrigir bug, atender ticket, responder cliente reclamando. São tarefas mundanas que todo sênior já passou e sabe resolver, mas não quer (nem deveria) fazer o dia inteiro — e são exatamente as tarefas que o júnior ainda precisa aprender na prática (ex.: aprender que um bug gerado por ele foi para produção e um cliente ligou reclamando é uma lição que só se aprende vivendo).

## O ciclo de feedback diário

Feedback não é "você está indo bem" — isso não é feedback, é elogio vazio. Feedback de verdade acontece no dia a dia: revisão de código que trava, comentário de "isso aqui vai dar problema em produção, corrige essa linha", teste que está quebrando. A orientação tem que travar o erro *antes* de ele ir para produção, não depois.

Sinal de que está indo bem: seu código para de ser barrado / voltar em revisão. Sinal de que precisa estudar mais: seu código volta toda vez. A pergunta certa nesse caso é "o que eu devo estudar para não cometer esses mesmos erros de novo?" — esse é o ciclo saudável de feedback contínuo, diário, não apenas em avaliações formais e espaçadas.

## Por que um time só de júniors também não funciona

Dois cenários opostos e igualmente comuns:

- **Startup que acabou de captar investimento** e quer impressionar investidores contratando só sênior no mercado.
- **Startup que ainda não captou**, gastando dinheiro do próprio bolso do fundador, tentando esticar o caixa ao máximo — com a ideia de que "júnior tem potencial, cresce rápido, vou montar um time só de júnior."

O segundo cenário costuma dar errado: mesmo o júnior mais bem-intencionado e capaz, sem orientação, vai cometer erros — não porque é ruim, mas porque é da natureza de qualquer pessoa cometer erros numa área que ainda não domina. A mesma lógica da metáfora do pedreiro se aplica de novo: colocar alguém sem prática numa tarefa nova, o resultado sai "torto", mesmo que a pessoa saiba a teoria.

Não é falsa humildade dizer isso — é reconhecer que velocidade e qualidade vêm de repetição/experiência, não só de teoria. Nenhuma equipe só de sênior, nenhuma equipe só de júnior — funciona sempre em mix.

## Formação e capacitação interna de equipe

Empresas mais maduras (o exemplo citado é a própria empresa do entrevistado, e casos como a Zup, mencionados pelo interlocutor) estão levando a capacitação interna a sério: mentoria, treinamento, espaço e tempo dedicados à evolução das pessoas, contratando pensando na necessidade da empresa daqui a alguns anos, não só na vaga aberta agora.

Quem terceiriza esse investimento e só contrata "quando precisa", nos momentos de mercado aquecido (todo mundo com liquidez sobrando contratando a rodo), acaba sem conseguir fechar a conta — todo mundo quer o "jeitinho" de resolver só na hora, e quando chega a hora, "não sobra ninguém".

## Body Shops vs. empresas de desenvolvimento

No mundo de terceirização de desenvolvimento de software existem, em linhas gerais, dois tipos de empresa:

**Body Shops** — o nome já diz: "lojas de corpos". O funcionamento típico: ligar o dia inteiro rastreando LinkedIn, disparando e-mails automatizados de proposta ("adorei seu perfil, tenho uma oportunidade" — mensagem de robô, sem ninguém de fato tendo lido o perfil). Quando fecha um projeto que precisa de 10 pessoas, começam a contratar até "bater a meta" de corpos — sem coesão, sem comunicação, sem cultura de equipe.

**Empresas de desenvolvimento "de verdade"** — cuidam de coesão de equipe, comunicação, cultura.

Existe mercado para os dois tipos, inclusive porque muita gente contratante não entende o que é desenvolvimento de software e só precisa "gastar orçamento". Isso é comum em multinacionais: se um departamento não gasta o orçamento anual, a lógica corporativa é "não precisava desse dinheiro" — e o orçamento do ano seguinte é reduzido. Resultado: departamentos gastam dinheiro em projetos sem necessidade real só para não perder orçamento no ano seguinte, especialmente perto do fim do ano fiscal, quando há revisão orçamentária.

## Mercado aquecido, salários inflados e promessas vazias

No momento de mercado com muita liquidez (dinheiro sobrando, todo canal de recrutamento saturado), aparecem sintomas específicos:

- Empresas oferecendo salário de sênior para júnior.
- Propagandas de curso prometendo salários de R$ 50.000 e a virada de "júnior para sênior em 6 meses" — promessa que não se sustenta.
- Empresas estrangeiras que descobriram que "brasileiro sabe programar" oferecendo contratação com promessa de relocação (ex.: para o Canadá) "assim que a pandemia acabar" — promessa que tende a não se concretizar; imigração tem uma série de exigências legais que a empresa não controla sozinha, e o interesse real dela costuma ser só contratar barato por um ano para resolver uma meta pontual.

Nesse cenário, os Body Shops (que já estão saturados de vagas e sem gente disponível) passam a vender júnior com currículo "florido" a preço de sênior — a empresa contratante, com dinheiro sobrando, faz vista grossa. Resultado: o júnior não tem quem o oriente (ninguém vai mentorar alguém contratado como "sênior" instantâneo), não cresce de verdade, entrega abaixo do esperado, e a reputação de todo o mercado piora.

Esse padrão não é sustentável a longo prazo. Vender sonho é especialmente perigoso quando envolve educação: não é só dinheiro, é o tempo de estudo que a pessoa está investindo — prometer uma direção maluca para alguém despreparado é grave.

## Por que a palavra "cultura" virou desgastada

"Cultura", assim como muitas palavras usadas em excesso (o exemplo citado é o "diário" da moda), foi tão mal empregada que praticamente virou palavra ruim. Quando alguém puxa esse assunto de forma performática, normalmente é sinal de discurso vazio — o "cara que nunca trabalhou, vem de sonho a preço de banana".

A prática comum: toda empresa nova escreve um "manifesto de cultura" (às vezes copiado — "cultura da Netflix", "cultura do Facebook"). Mas cultura não é um manifesto escrito em pedra — ela evolui com o tempo, do mesmo jeito que a cultura de uma cidade muda entre décadas. Empresas são como micro-cidades: as pessoas mudam, evoluem, aprendem que erraram e corrigem o rumo. Cultura escrita e estática, sem espaço para reconhecer erro e mudar, tende a manter o erro e estagnar a empresa.

Cultura de verdade não é uma lista de 50 protocolos — são poucos valores básicos (ser honesto, não prejudicar as pessoas, não fazer nada ilegal ou antiético). Quando esses valores básicos são violados, a solução não é "consertar" a pessoa — é desligá-la. Só que muitas empresas, na prática, seguram artificialmente pessoas incompatíveis com a cultura (por medo de perder "corpo" ou por apego), o que é uma perda de tempo dupla: da empresa e da pessoa, que talvez performasse melhor em outro lugar.

**Exemplo de mudança real de cultura via liderança:** a citação é a Microsoft, comparando a era anterior a Satya Nadella com a era pós-Nadella — as palavras oficiais da cultura corporativa continuaram praticamente as mesmas, mas o comportamento observável mudou completamente (ex.: postura em relação a produtos concorrentes/plataformas abertas) a partir da mudança de liderança, não da mudança do texto escrito na parede.

A frase de efeito "cultura, a gente é gente, a gente valoriza as pessoas" hoje funciona majoritariamente como marketing de atração de talento, num mercado onde bom programador é recurso raro e toda empresa está competindo por atenção.

## Paralelo com a bolha da internet (final dos anos 90 até 2001)

As características do momento de mercado aquecido atual (`[transcrição incerta sobre o ano exato de referência da fala]`, o áudio sugere ~2021) se repetem historicamente: no fim dos anos 90 até 2001, um monte de programadores — nem todos excepcionais — ganhava salários astronômicos, disputados a tapa por empresas recebendo investimento "como se não houvesse amanhã", até alguém questionar o valor real disso na bolsa de valores. Quando o dinheiro sumiu, ficou claro quem de fato gerava valor e quem só estava numa posição inflada pelo momento.

Quando a crise chegou (2001), as empresas foram obrigadas a repensar eficiência — e resolveram terceirizando parte da produção para a Índia, que tinha (e tem) grande volume de mão de obra a um décimo do custo. Posições que existiam só "para o investidor ver volume" desapareceram, porque ninguém mais estava interessado nessa métrica de vaidade quando o dinheiro acabou.

**Quem sobrevive a qualquer crise** é quem construiu a mentalidade de ser o melhor *profissional*, não só o melhor programador — são coisas diferentes. Um programador tecnicamente excepcional, mas que não consegue trabalhar em equipe, não gera o mesmo valor para a empresa/cliente que alguém capaz de tomar decisões, orientar um time e fazer um produto sair do papel sem se perder em reuniões improdutivas. Boas crises fazem esse tipo de profissional crescer, porque de repente há um espaço vazio (90% do mercado não sabe tomar decisão e gerar resultado de verdade) para ser preenchido.

## O contraste Google vs. Cadê (kd.com.br): eficiência nascida da escassez

O Google nasceu de fundadores estudantes que queriam resolver um problema real (indexação de páginas da internet), sem dinheiro sobrando — a restrição de recursos os forçou a criar o algoritmo PageRank e usar máquinas baratas reaproveitadas como servidores. Esse DNA de eficiência nasceu justamente da falta de dinheiro, num momento (fim dos anos 90) em que o resto do mercado de internet estava inundado de capital de investimento sem muita disciplina.

Em paralelo, no Brasil, o Cadê (kd.com.br) era um site de busca — mas, ao contrário do Google (que indexava automaticamente), funcionava como diretório manual, no modelo das páginas amarelas: dependia de centenas de pessoas cadastrando páginas manualmente. Isso só era viável enquanto havia dinheiro sobrando para pagar essas 500 pessoas. Quando o dinheiro secou, o modelo não se sustentou. O Google, por ter "chegado atrasado" à fase de dinheiro fácil, foi obrigado a resolver o problema via software (eficiência), e essa vantagem persistiu mesmo depois que o mercado normalizou.

## Contratação como métrica de vaidade e overhead de coordenação

O mesmo padrão se repete agora: empresas que recebem rodadas de investimento e não têm lucro/receita como métrica de sucesso acabam usando "número de contratações" e "número de usuários" como substitutos — métricas de crescimento, não de receita. Isso leva a contratar gente para fazer "quase nada", só para inflar a equipe.

Quantidade de pessoas é frequentemente o oposto de eficiência: mais pessoas exigem mais esforço de coordenação entre elas (2 pessoas = 1 canal de comunicação; 3 pessoas = 3 canais; a complexidade cresce rápido com o tamanho do time). Esse overhead de coordenação gera estruturas piramidais — líderes técnicos, coordenadores, gerentes — que não produzem diretamente, só coordenam quem produz. Em algum ponto, se a empresa quiser seriamente ganhar eficiência, a solução costuma ser cortar parte da equipe: isso elimina overhead de coordenação e muitas vezes a eficiência *não cai* — porque as pessoas restantes conseguem se coordenar diretamente, sem precisar de um "árbitro" no meio.

## Barreira de entrada varia com o ciclo de mercado

Processos seletivos rigorosos e longos (o exemplo citado: entrevistas de meses em empresas como o Google, incluindo os famosos testes teóricos que viraram meme — "quantos bolas de golfe cabem em um avião", puzzles de lógica) fazem sentido quando a empresa tem alto poder de escolha e está pedindo um compromisso alto do candidato (mudança de cidade, de país). Em mercado aquecido, com demanda alta e oferta escassa, a barreira de entrada cai — não porque o padrão "correto" mudou, mas porque o equilíbrio de oferta e demanda mudou temporariamente. Isso não é permanente: o padrão de seleção varia com o tempo, e quem entra achando que a barreira baixa atual é "o normal do mercado" tende a se surpreender quando o ciclo virar.

## Efeitos colaterais de crescer rápido demais

Contratar rápido e com pouco critério gera baixa confiança na equipe recém-formada — o que leva a mais burocracia, mais camadas de gestão, menos autonomia e mais processo (porque a empresa não confia que quem acabou de "roubar" de outro lugar tem lealdade para ficar). Isso também reduz o espaço de crescimento de carreira interno: crescer rápido contratando gente de fora para posições de liderança, em vez de promover de dentro, tende a gerar corporativismo, política interna e disputa por posição — o oposto do discurso de "cultura" que a mesma empresa costuma vender.

A alternativa mais sustentável, mas mais lenta: formar as pessoas desde estagiário, sabendo que estagiários viram júniors, júniors viram plenos, plenos viram sêniors — e que cada elo dessa cadeia precisa contribuir para o crescimento dos outros, porque ninguém cresce sozinho. Resultado rápido tende a custar caro e durar pouco; resultado duradouro exige tempo e paciência para construir uma fundação sólida.

## Encerramento: honestidade no feedback

Ninguém gosta de dar má notícia, mas deixar de dar feedback honesto (dizendo sempre "está indo bem, está indo bem") prejudica quem está recebendo — tira a chance de a pessoa corrigir o rumo antes de ser desligada ou de perder uma oportunidade melhor em outro lugar. Feedback honesto é diferente de ser gratuitamente ofensivo; quem não sabe fazer essa distinção (ataca as pessoas "porque é divertido") não deveria estar em posição de liderar. "Mau-caratismo" é tratado como algo que raramente muda: se a própria criação da pessoa não mudou isso em vinte anos, não é o RH ou um gestor que vai mudar em dois meses.
