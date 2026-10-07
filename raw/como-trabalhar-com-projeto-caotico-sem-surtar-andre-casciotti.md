# Como trabalhar com projeto caótico sem surtar (André Casciotti)

> **Fonte:** transcrição de vídeo do canal "Próximo Nível" / "Fala Dev" (André Casciotti), colada pelo usuário em 2026-10-07. Já em português; sem tradução.
> **Limpeza:** pontuação e parágrafos adicionados; erros de ASR corrigidos ("Vimex" → "Vira e mexe"; "Casac" → Casciotti; "Loable" → Lovable; "cloud code" → Claude Code; "Sonar Cube" → SonarQube; "Pemai" → PMI; "camban" → Kanban; "Screw Master" → Scrum Master; "techad" → tech lead; "Ajá" → Agile; "deslechada" → desleixada; "devá"/"deve" → dev). "Curva de rio" (provável "gargalo"/"funil") mantido como dito. Trechos omitidos: divulgação do Instagram da esposa-terapeuta (handle ininteligível no ASR), do curso "Dev que Resolve" e o pedido final de like/inscrição/comentário.

---

## Abertura

Trabalhar com programação é divertido, mas também é bem estressante. Vira e mexe a gente pega um projeto todo detonado, com prazo ridiculamente apertado: usuário que não sabe o que quer, gestor que não sabe cuidar da equipe, time que não sabe trabalhar junto, código muito ruim de alterar. A pergunta que fica: como trabalhar num ambiente desses sem surtar? Como manter a saúde mental sem querer jogar tudo pro alto e vender coco na praia?

O autor recebeu várias mensagens pedindo conteúdo sobre saúde mental. Poderia falar de hobbies ou de dicas genéricas, mas escolheu um conteúdo "com a cara do canal": voltado ao dia a dia de trabalho. Para lidar com emoções e pensamentos, diz, procure terapia (a esposa dele é terapeuta). Aqui o papo é mais profissional, baseado em mais de 20 anos de carreira e num projeto caótico que ele vive agora.

## Risco ocupacional

Para quem é iniciante isso desaponta: trabalhar com projeto caótico, sair do trabalho com a "cabeça inchada", é **risco ocupacional** do dev. Não é para ser constante, mas acontece. Várias profissões têm o mesmo problema, algumas mais (médicos, bombeiros, policiais: carga física, mental e emocional altíssima; o médico "sentadinho no consultório" já passou por UTI e emergência).

Por que o dev sofre: **ter software é poder**. Um bom parque de software acelera o crescimento, aumenta lucro ou reduz custo (menos pessoas, menor margem de erro numa operação grande). São softwares triviais do mundo corporativo: formulários eletrônicos, cadastros, fluxos, coisas que se resolvem com planilha. Quanto mais software, e mais rápido, melhor para a empresa.

Hoje todo mundo tem ideias e todo mundo pode criar software (Claude Code, Cursor, Lovable: algo que levava semanas sai em horas, mesmo para quem não é programador). **Mas criar software é fácil; mantê-lo em produção é outra coisa.** Grandes corporações não deixam software de faturamento milionário na mão de agentes automáticos; sempre há um dev por trás (não sabe se isso mudará, mas não é tão comum quanto se imagina). Mesmo quando o dev não produz o código, ele confere e revisa. Resultado: **tudo esbarra nos devs** ("a gente virou uma curva de rio"). Antes já era assim; agora o volume aumentou. Atrasos, custo das entregas, bugs, reclamações de usuários: tudo vem pra conta do dev. Somado ao esforço mental da profissão intelectual, é muita carga de estresse.

Logo, a vontade de "vender coco na praia" é risco ocupacional: ou você aprende a lidar com isso, ou é melhor fazer outra coisa. Isso **não** significa sacrificar a sanidade mental. Entender que faz parte do trabalho (é para isso que devs existem: dar vazão e resolver esses problemas) muda o olhar. As "diquinhas genéricas" funcionam; o problema é que muitas vezes a pessoa não entende de fato que aquilo é um problema, ou o trata como passageiro ("é assim mesmo"). Assim como é inevitável bater o carro em algum momento se você dirige, nem tudo está sob seu controle na profissão.

O autor traz três "mantras" que repete para si mesmo (não é regra nem guia de sanidade mental; é experiência pessoal para testar e voltar a comentar).

## Mantra 1 — Foque no que está ao seu alcance

Todo projeto tem problema: atraso, gestão ruim, processo ruim, usuário ruim, requisito ruim. É em todo lugar; é mais raro achar um lugar sem esses problemas do que com. Acontece que devs estudam muito, leem, fazem curso, são "resolvedores de problema" e querem mudar tudo: ferramentas de log, telemetria, monitoração, processos (Agile, Kanban, métricas, gerenciamento de projetos), boas práticas, arquitetura. "Pô, tá tudo errado nesse negócio."

Só que **quase nenhuma autonomia** existe para isso. Os problemas dos projetos não são superficiais; estão enraizados na cultura e nos processos da empresa e se repetem em todos os projetos. Por mais experiente que seja, ou mesmo virando gestor, muitas vezes você não tem poder de mudar. Quando fala com o usuário, ele pode responder: "quem é você na fila do pão para dizer como faço requisito? Faço projeto aqui há 20 anos." O dev está "na base da cadeia alimentar", na camada operacional; tática e estratégia são de outras pessoas. Se quiser mexer nisso, precisa subir a hierarquia, e ainda assim às vezes não alcança.

Pior: você sugere um processo/arquitetura, o time não adota (cultura de não fazer), dá problema, e **a bucha sobra para você** corrigir. Essa soma gera irritação e frustração, porque você sabe que podia ser melhor e não consegue mudar. É daí que se surta: querer mudar o que não está ao seu alcance.

**Na prática:**

1. **Entenda o jogo que você joga na empresa.** (Levou anos para entender.) Não é politicagem; é maturidade. Entenda a hierarquia e a dinâmica de interesses. Muitas vezes não é do interesse de alguém que o processo mude: em empresas fortemente waterfall, gerentes de projeto com cultura PMI que só fazem controle de projeto não querem Agile ("se mudar, quem perde o emprego? Quem garante que viram Scrum Master e a empresa não contrata gente de fora?"). Não é dizer qual é melhor; é entender que há interesses e que a conversa não basta: há hierarquia a respeitar, discussão que vai ao nível tático e estratégico. A gestão em geral quer **resultado** (respeitados limites éticos); quem se preocupa com o *como* é a camada tática/operacional; o gestor é responsável pelo resultado. Entender o jogo mostra o quanto você pode mexer e o quanto não pode; quem dá "pitaco maluco", se revolta e é demitido estava num jogo em que só perdia. Não é para calar a opinião, e sim saber até onde ir e qual jogo dá para ganhar.

2. **Reclame menos.** O autor reconhece que reclama muito. Mas reclamar "desopilar" é ilusão: você só aumenta e divide sua raiva; e, se prestar atenção, espera que o outro concorde, e quando contesta, você fica com mais raiva ("você é cego"). Não muda nada na situação; se reclamar ao chefe, pode mudar do jeito que você não quer ("laranja podre", status do emprego). Tenha ciência de **para quem** e **como** reclama. Quem reclama demais provavelmente faz de menos: vira "resmungão". Faça mais do que reclama.

3. **Pense no que você pode mudar.** Reclamar é terceirizar o problema ("a empresa tem que mudar"). Exemplo: teste. "Não existe cultura de teste, não me dão tempo, qualidade não é prioridade" é terceirizar a culpa: se seu trabalho é entregar com qualidade aceitável, testar é caminho que ajuda, e a empresa não precisa lhe dar um tempo específico. Ninguém vai mudar a arquitetura inteira de um software em produção (risco, decisão fora da sua alçada), mas dentro do seu código, do seu método, do seu fluxo de trabalho dá: de 8 h de cronograma, separar 2 h por vontade própria para teste unitário (6 h desenvolvimento + 2 h teste). No time: ligar análise do SonarQube na pipeline, rodar testes unitários na pipeline, criar processo de documentação ("quando sairmos de férias ninguém fica ligando um pro outro").

**Não subestime as pequenas mudanças:** uma pequena ação desencadeia outra e, no fim, gera mudança maior. E **quem resolve mais problemas ganha mais autonomia**: quem tem histórico de resolver é escutado; quem só reclama e faz sempre do mesmo jeito não é. De passo em passo, você pode ter mudado o que estava errado.

## Mantra 2 — Faça o melhor que você pode com o tempo que você tem

Ajuda no pensamento "nunca dá tempo de fazer nada direito, é sempre correria". Devs tendem a querer começar tudo do jeito mais perfeito: depois de um projeto de arquitetura ruim, no próximo estudam a melhor arquitetura do mundo; depois de sofrer com requisito, passam cinco meses só em análise; depois cinco semanas em cronograma. No começo o tempo parece infinito. Quando o prazo chega, nada saiu como devia (projeto gigante, arquitetura complexa, cronograma impossível sem saber o que fazer), e acaba-se começando "do jeito que dá". A correria volta igual, só mudou o tamanho da janela. Você sofre com a correria, com o que não conseguiu fazer, com a arquitetura que não ficou boa e com o medo de ser demitido. **Quanto mais tempo você tem, mais tempo você vai levar** (regra universal).

**Na prática:**

- **O tempo é o maior limitador de tudo, inclusive da procrastinação.** Coisas sem data não saem do papel: projeto de software, reforma, construir casa. Se você ficar "polindo a maçã", não come a maçã. Tempo parece jogar contra, mas ajuda a tirar do papel.
- **O código perfeito não existe**, só na sua cabeça. Você revisita código seu de seis meses atrás e acha uma porcaria; isso é normal, porque você evoluiu. Tenha uma visão do perfeito, mas saiba que não vai atingi-lo.
- **Entregue**, mesmo que ruim: "se não entregar, você vai pra rua". Resolve-se um problema de cada vez: não entregar leva à demissão agora; entregar código ruim talvez mais tarde, e talvez o código não esteja tão ruim quanto você acha. Não é fazer de qualquer jeito; é prioridade. Dentro do tempo, faça o melhor que puder. Pode ser fantástico ou uma droga *para você* sem ser uma droga para o projeto. Frase de um mentor: **"feliz, nunca satisfeito"**: fique feliz com as entregas, mas tudo pode melhorar (melhoria contínua); o perfeito só existe na sua cabeça.
- **Aprenda a priorizar.** Devs priorizam errado: na cabeça deles o cadastro vem antes da regra de negócio; para o negócio, a regra vem primeiro. Prioridade não sai da cabeça do dev: sai da conversa com o negócio e o usuário. É um dos conceitos de Agile mais "ditos entender" e mais esquecidos (priorização de backlog). Dá para cadastrar por script direto no banco e fazer uma tela mais ou menos; se você precisa da regra, faça a regra primeiro. É um dos maiores geradores de estresse: investe-se muito tempo no que o usuário não precisa, e às vezes o próprio usuário não sabe priorizar ("acho que na verdade precisava mais disso"). Faz parte do jogo.

## Mantra 3 — Complexidade e organização andam juntas

Para quando bate a sensação de "esse negócio não vai acabar nunca". Devs tendem a não valorizar organização: "organizar é papel do Scrum Master, do gerente, do tech lead; eu preciso escrever código". Mas "depois reclama que vai perder o emprego para a IA, que escreve código muito mais rápido"; **organizar também faz parte do trabalho**, e a pessoa é parte do que precisa ser organizado. Não se trata de organizar o time todo (lembre do mantra 1), e sim o **seu** trabalho.

**Analogia:** reunião de amigos em casa (traz uma cerveja, uma carne; se alguém não trazer, tudo bem) exige baixo planejamento. Uma festa de casamento (salão, data, buffet, flores, músicos, juiz de paz/padre, contratos, pagamentos, sincronização de vários fornecedores num único dia) exige muito: muitos contratam um organizador de casamentos. Um projeto de software é bem mais complexo que uma reunião de amigos. Trabalhar "organicamente" numa tarefa complexa gera desorganização e um estresse gigantesco, às vezes imperceptível.

**Analogia da casa:** casa bagunçada é estressante (tudo jogado, sensação de que está tudo errado, você não quer deitar no sofá); casa arrumada traz tranquilidade. No trabalho, sem organização você não sabe quanto falta, se está no prazo, se pode trabalhar menos, e pior: **não percebe o quanto já trabalhou** ("trabalhando, trabalhando, não fiz nada"). Organização mostra o que já foi entregue, tira o estresse e libera a mente.

**Na prática:**

- **Detalhe seu trabalho: primeiro nível macro, depois micro.** Mesmo uma tarefa pequena (a menos que seja uma linha de código): primeiro as macroetapas (botão na tela → front end → back end → fluxo todo), depois o micro (alterar este método, criar esta interface/classe, aplicar esta regra aqui e aquela ali). Uma funcionalidade gigante pode ser detalhada em pequenas tarefas.
- **Crie lista de tarefas para tudo** (mercado, material de reforma, saídas na rua; qual ordem). Crie o hábito mesmo que ache que "não funciona com listas" (pode ser preguiça ou nunca ter feito de verdade). A lista dá: (a) **passo a passo**, com ordem e sequência lógica, e o **poder da barra de progresso** (as barras no computador não existem à toa; tiram ansiedade; sem saber se andou pouco ou muito você fica ansioso); (b) o **poder do check**: olhar a lista e ver "eu já fiz isto" dá sensação de microvitória, produtividade, alívio e libera energia mental.

## Conclusão

Ansiedade (muita coisa para fazer), frustração (as coisas não acontecem), incapacidade, inutilidade: são sensações comuns a quem trabalha como dev, riscos ocupacionais. O objetivo não é mandar fazer autoajuda ou terapia (embora ajude muito), mas entender **por que** essas sensações aparecem e **reconhecê-las** quando chegam (estou frustrado, ansioso, me sentindo incapaz) para criar mecanismos de lidar com elas. A gente "surta" porque vê o problema, não entende por que acontece e não consegue se mexer. Não é um guia para evitar remédio tarja preta; é para **proteger a energia mental**, que a programação exige muito, e para trabalhar melhor.

Tudo que foi dito envolve **análise de requisitos** (detalhar atividades, entender o que fazer), **arquitetura** (dividir tarefas é o conceito de arquitetura na prática: limites e responsabilidades), **testes** (validar entregas, dar o "check" na tarefa) e **refatoração** (melhoria contínua: poder entregar "mais ou menos" agora com a segurança de melhorar depois, no código próprio ou no do colega). Esses quatro pilares estão ligados ao "dev que resolve" (conceito do autor, tratado em material próprio).
