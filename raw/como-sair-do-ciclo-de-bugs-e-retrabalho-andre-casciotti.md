---
title: "Como sair do ciclo de bugs e retrabalho (André Casciotti — Próximo Nível)"
source_type: transcrição de vídeo (PT-BR, legenda automática)
author: "André Casciotti"
date_ingested: 2026-10-14
---

# Como sair do ciclo de bugs e retrabalho

> Transcrição limpa (pontuação, parágrafos e termos corrigidos). Já em português; sem tradução. Correções de ASR: "André Casarc" → André Casciotti; "dev que resolve" mantido como nome do curso do autor; "Alício" (mundo de Alício) → provavelmente "Alice" (mundo de fantasia, inferido); "Mod de documento" provavelmente "modelo de documento" (inferido); "Visual Studio" mantido como no original; "desenvolve" → dev. Trechos ininteligíveis foram omitidos.

## Abertura

Lidar com bugs é sempre um problema, seja na sustentação do software ou na fase de testes de um projeto. Na correria você corrige uma coisa, quebra outra, tenta corrigir o que quebrou, quebra uma terceira — e quando percebe está "nadando em bugs". Este vídeo é para quem vive essa realidade. Faz parte do quadro "Próximo Nível", com dicas e estratégias de carreira para devs; o autor ajuda devs a "subir de nível com código que resolve e que não volta com bugs".

## O ciclo de bugs e retrabalho

O ciclo é uma das coisas que mais afeta o dia a dia e, ao mesmo tempo, um dos problemas mais invisíveis: virou **normalizado** ("é normal voltar bug", "é normal o usuário reclamar", "software em produção buga mesmo"). A carga de estresse e a carga mental de lidar com código ruim, gambiarra e bug atrás de bug entrou na rotina sem ninguém perceber — e passa de geração em geração, para quem chega.

Como o ciclo funciona:

1. **Pressão.** Projetos já começam atrasados (duas ou três semanas depois da data acordada); na sustentação há cobrança para resolver rápido o que afeta a operação. Quem está no projeto acha que o dia a dia da sustentação é tranquilo; quem está na sustentação inveja o projeto (coisa nova, sem código legado). A pressão existe nos dois, em doses diferentes ("homeopática" no dia a dia, "tudo de uma vez" no projeto).
2. **Pressa.** Sem tempo de pensar, o dev "se afoba" e tenta **sobreviver** em vez de manter o software e o código fáceis de manter. Chega o bug, quer despachar o mais rápido possível.
3. **Correção de qualquer jeito → teste de qualquer jeito.** O teste reflete a correção: meia-boca, ou nenhum — "apertar o botão, acho que passou". Sobe em produção "do jeito que dá", ou manda para o QA testar.
4. **O bug volta, ou nasce outro.** Corrige uma coisa e quebra outra. Às vezes sobe pensando "se não funcionar eu volto e corrijo".
5. **Mais pressão.** O acúmulo de bugs gera mais cobrança; o dev sente "estou fazendo de qualquer jeito porque você me aperta" (a culpa é de quem pressiona), mas não fala para proteger o emprego. O sentimento retroalimenta o ciclo e o dev fica preso num **loop infinito** de pressão, bug e retrabalho.

Observação: muitos devs associam retrabalho a reaproveitamento ruim ou a novas features feitas meia-boca, mas **a maior parte do retrabalho vem dos bugs**: faz-se uma coisa, depois se refaz, desfaz, faz de outro jeito, volta ao código e gera outra gambiarra.

## Como sair do ciclo

**Antes de tudo: pare e respire.** Na pressão, o primeiro reflexo é abrir o editor e sair fazendo. Antes de mexer, parar para pensar e "oxigenar o cérebro". Toda vez que se faz as coisas correndo, coloca-se um risco novo no código, e a longo prazo prejudica o código, o time e o próprio dev. Se não pensar direito, o loop continua e o dev continua achando que a culpa é dos outros.

O autor não nega que os outros têm culpa ("todo mundo tem uma parcela de culpa, inclusive você"), mas **não se controla o que os outros fazem**: por melhor que o dev seja, sozinho ele não muda isso — normalmente está "na base da cadeia alimentar", "um grão de arroz dentro da empresa". Então: **mudar o que se pode mudar**.

Aviso: o que vem a seguir não é difícil e provavelmente soará como "nada de novo". Mas o autor tem certeza de que **a maioria não faz** o que diz saber que é importante. Pede que o espectador anote, cole no monitor e **faça de verdade**: "saber que é importante é muito diferente de fazer". O loop existe porque se trabalha no **automático**, principalmente quem é experiente (iniciante ainda não tem esses vícios; experiente tem o hábito de dizer "eu já sei"). O que ajuda não é outro vídeo técnico com técnica nova, é **fazer o básico bem feito**.

São **três passos** para quando chega um bug.

### Passo 1 — Identifique a causa raiz do problema

Corrigir na origem resolve o problema de fato. Todo mundo diz que é importante, mas muitos não fazem, porque **sintomas são fáceis de corrigir**: a variável nula (object reference not set), o valor zerado (divisão por zero), o registro que não existe na base, a consulta que retorna `count` zero ou nulo. Corrigir **causas raízes** é bem mais complexo: o erro que aparece na ponta é o sintoma; o problema pode estar em outro lugar — o registro não existe porque, três etapas atrás, uma regra de negócio fez o fluxo não entrar no `if` e o registro nunca foi gravado; ou uma regra de negócio está no lugar errado e deixou o valor nulo/zerado.

A tendência é olhar sempre para o sintoma, o lugar onde estourou o erro, porque se vai pelo caminho mais rápido (e há a pressão). Em vez de seguir o fluxo, o dev vai ao ponto que deu erro e coloca um `if` ("se nulo não entra", "se zerado, põe 1", "se não existe, pula a etapa"). **Isso gera novos bugs**: funcionou para a situação do dev mas quebrou em outro lugar; ou parou de dar erro no meio do fluxo e passou a dar no fim. Pior: nem sempre o bug é técnico (exception) — às vezes a tela não exibe um registro, não mostra uma seção, bloqueia um botão que não deveria, não mostra uma mensagem. Muitos bugs são **de negócio**, e quem não tem conhecimento de negócio nem percebe que introduziu outro bug; ele chega ao QA e ao usuário.

Pior ainda: corrigir sintoma atrás de sintoma **empilha gambiarra** no código. Se o código em que se mexe hoje está "aquela desgraça", talvez seja porque um monte de devs passaram por ele corrigindo sintoma em vez de acertar um ponto lá atrás no fluxo que resolveria para todo mundo. Identificar a causa raiz é evitar esse empilhamento.

Como fazer — antes de mexer, pensar em três coisas:

1. **Faz sentido o estado em que o código chegou aqui?** Poderia ser nulo/vazio/zero/sem registro? Faltou um tratamento simples (um `if`), ou o valor **não deveria ter chegado** nesse ponto com esse estado? Exemplo: o valor chegou aqui como R$ 1.000, e o cálculo final que deveria dar 5.000 deu 5 milhões — será que nem este ponto deveria ser 1.000, será que errou uma vírgula em algum lugar?
2. **Como é o fluxo de negócio todo?** De forma macro: de onde se chega nessa informação, por onde se passa, quais as etapas, por que passa por aqui; em determinada situação passa e em outra não? Ter uma visão geral e o contexto do código que deu erro (ou do problema de tela).
3. **Por que o código está desse jeito?** Muitas vezes não foi você que o escreveu, e a pessoa pode ter tido uma motivação. "Se a tartaruga está em cima da árvore, deixa a tartaruga lá, porque deve ter algum motivo" — não é verdade 100% das vezes, depende de análise de contexto. Por isso a ordem: primeiro entender se aquela situação é válida, depois o fluxo, e só então pensar se o código está assim por algum motivo específico.

O grande objetivo é **parar de olhar para um ponto fixo e abrir a visão para o fluxo** — analisar o fluxo como um todo, não só o lugar onde se vê o erro ("era para habilitar o campo e não habilita; põe um `if` que habilita" — sem saber por que era para estar desabilitado).

### Passo 2 — Evidencie o problema

Quando se entende o erro, a solução fica clara — "pipoca na sua cara". Todo mundo diz que é óbvio, mas é onde os devs mais erram, e **pega mais o experiente que o inexperiente**: o experiente conhece o código todo, sabe onde passa o quê e tem tudo mapeado na cabeça, o que gera **certezas** ("tenho certeza que é aqui", "altero aqui que vai dar bom"). Nada de errado em ter experiência; o problema é o outro lado da moeda: assim como altera com muita confiança, **testa com muita confiança — ou nem testa**. Faz a correção "no olho", comita e sobe. Por isso o experiente comete bugs idiotas que o iniciante não comete (colocou o valor, não viu que mais abaixo podia estar nulo, dá erro de nulo dois minutos depois do deploy porque nem testou). Daí o retrabalho: baixar, corrigir, subir, testar de novo; já pegou outra atividade; vem a insegurança ("será que não é melhor testar direito?"); empilha gambiarra. Acontece com o autor também — "somos seres humanos, não robôs". Intuitivamente o dev sabe e às vezes acerta, mas às vezes não, e **é por isso que se estressa, cansa, tem retrabalho e atrasa as atividades**.

Como evidenciar: **simule o erro antes de alterar qualquer coisa** — faça dar o erro. E **não é só debugar**. O hábito de sair debugando é forte, e há situações (principalmente na sustentação) em que só debug não serve: não há acesso, não há tempo de montar o ambiente (nem todo mundo vive num "mundo de Alice" onde se baixa o código e tudo funciona). A evidência pode ser um **log**, uma **mensagem na tela** do usuário (um print), um comportamento visível. Entendida a evidência, olhe o sistema e tente **chegar no mesmo ponto**: o que o usuário fez, que tela preencheu, que código informou, que caso?

Conversar com as pessoas ajuda — e é uma oportunidade de desenvolver comunicação, não de ser "a pessoa mais social do planeta", mas de evitar a frieza do "me manda o link, o código, o número do produto, eu simulo":

- Com o **QA**: ele não só preenche a tela e reclama, ele **testa e explora** ("quando coloco o campo X dá erro, com outra opção não dá"; "acabou de subir uma correção desse campo, será?"). Isso é pista para o problema e uma ótima oportunidade de **aprender a testar** — o dev não aprende a explorar, o QA aprende.
- Com o **usuário** (se colaborativo): ele conta como entende o fluxo ("preenchi esse campo e ele não devia ter habilitado"), e o dev aprende mais **negócio**, desenvolvendo-se como dev por uma simples conversa por causa de um bug.

Depois, os **dados**: precisa de que campo/valor/consulta/cadastro de produto ou cliente para chegar na informação? Aqui o autor deixa claro: acesso direto ao banco facilita muito, mas, dependendo do ramo, **não se pode ter acesso ao banco de produção** por compliance e LGPD — e não adianta brigar com a empresa; é uma questão legal. Muitas vezes se tem acesso para ler mas não para gravar, e aí o debug de um processo que grava e consulta também não funciona. **Não trate falta de acesso como impeditivo total** (raramente é): há logs, mensagens, formas de chegar ao erro que dão mais munição que o banco de produção. Se sei que o problema ocorre ao preencher a informação X no campo, **posso simular em outro ambiente** sem dado de produção. Deixe a questão dos dados para o final e explore as situações; só quando de fato não há jeito, não há.

### Passo 3 — Prove que você corrigiu o problema

Parece o passo mais bobo, mas é o que o dev menos faz. De nove em dez vezes em que o autor pergunta "mas corrigiu, ou você acha que corrigiu?", a resposta é "acho que corrigi" — **sem prova**. Ter a prova traz **segurança real** (não falsa) ao dev e a transmite ao time e ao gestor; demonstra **senioridade**. Não garante 100% (às vezes dá problema), mas quanto mais se prova que corrigiu, menos isso acontece.

Hábito comum: testar com debug, F5, F10, F11, passou pelo código, não deu exception, "corrigido". Mas lembre: **debug não é evidência** — só mostra que passou pelo ponto que dava erro; o que importa é o que **aparece para o usuário**, o resultado final. É por isso que se corrige num ponto e quebra em outro: corrige ali, passa no debug, "beleza", e os campos aparecem bloqueados na tela sem o dev saber por quê. O autor insiste: as ferramentas de debug são ótimas e devem ser usadas, mas **debug é ótima ferramenta para diagnosticar, não para provar que corrigiu**.

Provar dá trabalho (levantar informação, analisar, ler log, testar, rodar a aplicação, corrigir, avaliar) e gera **desculpinhas**: "não tenho acesso em produção", "não dá para testar local, tenho que testar no servidor", "é mais rápido subir e testar em produção". Quando resolve, parece que valeu a pena; quando dá problema, dá problema grande, **e a reputação do dev está em jogo**: o sistema para, apaga registros que não devia, passa a vender produto com valor errado (o autor cita como exemplo hipotético de promoção no Mercado Livre com produto de R$ 5.000 por R$ 1.000 que alguém subiu "rapidão" e quebrou sem ver) — gera transtorno gigante, cancelar vendas, avisar clientes.

Como provar — a dinâmica é simples, ainda que trabalhosa: **teste → corrija → teste de novo, exatamente o mesmo teste**.

1. Ache a causa raiz (senão não se sabe se corrigiu).
2. Evidencie o erro (senão não se sabe o que provar).
3. Com a evidência (log, mensagem, comportamento na tela), **rode o teste e veja o erro acontecer**; faça a correção; **rode o mesmo teste** de novo. Se dava erro e agora não dá, aí está a prova.

Depois de provar que corrigiu, analise os **impactos colaterais** (a ordem importa: primeiro corrija, senão o trabalho não anda; depois procure os impactos). Como já se analisou o fluxo todo, há visão macro:

- O trecho alterado é **reutilizado** em outros lugares? Procure as referências/consumidores do método (no Visual Studio, "find references"; busca em arquivos, Ctrl+Shift+F).
- Mudei a **entrada ou a saída** (o contrato)? Antes retornava sempre 1 e agora pode retornar 0; antes nunca nulo, agora pode ser — isso pode quebrar outro consumo. Se a mudança é só interna, o impacto é menor.
- Olhar o macro, e não só aquela linha, reduz muito a chance de corrigir num lugar e quebrar em outro.

Por fim, **faça teste unitário sempre que puder**: ele ajuda a **detectar mudança de entrada e saída** (mudou uma ou outra, o teste quebra) e a **procurar reutilizações** (se já existe teste, já há mapeamento dos consumos; se não há, crie testes para esses consumos). Não precisa de 300 testes em todo o código — só para a alteração. É mais um **ponto de prova**: o método entrava assim e mostrava esse valor, agora dava exception; criou o teste, rodou, deu exception; corrigiu, parou de dar. Pelo menos **atomicamente** é prova muito melhor que o debug, e é **empírica**: rodando 30 vezes dá o mesmo resultado. (Ainda é preciso olhar o fluxo todo.)

## Conclusão

Nada disso é óbvio: se fosse, todo mundo faria e não haveria tanto ciclo de bug e retrabalho nas empresas. "90% dos devs sabem que é para fazer, mas não fazem, porque dá trabalho" — o autor também tem preguiça; é tentador "só ir lá, corrigir e mandar para produção". Anote, cole no monitor, faça. Principalmente o dev experiente: pare de repetir que "é óbvio" e de cair na armadilha da segurança ("eu sei que se mudar aqui vai funcionar").

A **segurança real** de "eu corrigi de verdade, tenho as provas" cria **reforço positivo**: deu bom uma vez, o dev repete na próxima, o estresse cai e o hábito dos três passos se consolida: **causa raiz → evidenciar → provar**.

Tudo isso é, no fundo, **análise de requisitos**: entender o problema, ir atrás do porquê de as coisas terem que acontecer, analisar o fluxo de negócio inteiro, entender como validar o que o cliente pediu (validar = evidenciar o que é certo e provar que está certo — o mesmo trabalho, só que do ponto de vista "antes do bug", da construção). Também é **planejar o trabalho**: o autor tem um workflow ao receber um bug (identificar causa raiz → evidenciar o erro → provar que está certo → publicar); análise de requisitos ajuda a saber que passos seguir para um objetivo (nova feature ou correção de bug), inclusive bugs de produção. É o que ele ensina no curso **Dev que Resolve** (link na descrição): análise de requisitos (por onde começar, onde terminar, o que produzir — "será que tenho que fazer um modelo de documento?"), testes unitários, arquitetura de software para código mais fácil de manter e relacionado às necessidades do usuário, e refatoração (melhorar o código depois de feito e evitar efeitos colaterais como os discutidos).

Encerramento: curtir o vídeo, comentar outras formas de trabalhar, se inscrever no canal.
