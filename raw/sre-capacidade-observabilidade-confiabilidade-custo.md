# SRE: Planejamento de Capacidade, Observabilidade, Custo, Release Engineering, Segurança e Confiabilidade

> Transcrição de aula/vídeo em português. Sem necessidade de tradução. Pontuação e paragrafação corrigidas para legibilidade; erros óbvios de transcrição automática corrigidos silenciosamente (ex. "web engineering" → "site reliability engineering", "traceability"/"trace" mantidos conforme dito). Autor/canal não identificado na transcrição fornecida.

Você tem a capacidade de ter todo esse planejamento funcional e te atendendo. Perfeito! Resolvido. Você já tem aí um planejamento de capacidade que atenda a questão de hardware. Então você não vai ter esse tipo de problema.

Outro ponto que você precisa ter é observar tudo o que acontece na sua arquitetura, desde o nível da aplicação até o nível de infraestrutura. Você tem que entender um fluxo. Então, se alguém falou que está tendo um problema — "tá muito lento" — qual é o fluxo todo? Qual é a jornada? Qual é a traceability? Qual o trace daquela chamada? Então você tem que ter isso: observar a visão completa.

Além dessa observação que eu falei, você precisa ter os alarmes, as métricas, notificações. Você precisa entender que algo está a acontecer. Você tem que prevenir o planejamento de capacidade — ele vai se basear muito nos dados da observação para entender qual o tamanho e como ele vai se planejar referente à capacidade.

Ao mesmo tempo, isso vai depender muito da empresa, mas de forma geral, quando você olha para custo, muitas vezes acha que é gasto — e isso tem mudado bastante com o aumento considerável de equipamentos de tecnologia, sendo de fato o core da empresa, com dados e tudo mais. Mas há a otimização de custo, que está extremamente ligada ao planejamento de capacidade e à observabilidade, porque é onde você vai reduzir os custos.

Não é só aí, né? Quando a gente fala de otimização de custo, estamos falando de otimizar mesmo o custo. Mas tem coisas que não são tão visíveis — por exemplo, você melhora, você otimiza o custo às vezes gastando mais em tecnologia, porque você para de ter um problema na entrega do seu produto. Uma loja virtual, 1h fora do ar, você perde R$ 1 milhão; porém, colocando o dobro de recurso que você tem lá — então você tinha dez servidores, colocar 20 custa 100 mil a mais — a gente tá falando que você tá ganhando na verdade 900 mil. Você tá deixando de perder. Então isso é bem importante.

Outro ponto é o dia a dia, a operação de tudo isso. Então, como ele vai ver a observabilidade, como ele vai fazer o planejamento de capacidade, inclusive ter a visão da otimização de custo na operação. Como ele vai saber que existe um Release Engineer e a capacidade de fazer um deployment da aplicação? Vai ter um módulo em que eu falo de todos os tipos de deployment que você poderia usar para minimizar o impacto da sua aplicação. Então, Release Engineering é a engenharia de entrega de novas versões — como que você vai fazer isso, gradual ou não.

E aí, segurança está em tudo — em tudo. Segurança, basicamente, é o sucesso de fato: você tem que estar seguro contra diversas coisas.

E o outro ponto é a confiabilidade. O que seria a confiabilidade? Ela é praticamente tudo, né? Ela é o ato de você estar ali confiável, digamos assim. Então vou fazer um zoom nessa questão da confiabilidade para a gente entender um pouquinho mais o que tá incluso nela.

A confiabilidade é a capacidade de você ter uma consistência dos seus dados. A durabilidade: saber que depois que você persistiu aquele dado, você não vai perder mais. Você ter tolerância a falhas — então ela meio que cobre todos aqueles outros itens. Você tem previsibilidade do que vai acontecer — a questão da habilidade, você tem que ser previsível para entregar uma boa confiabilidade. Você tem que ter disponibilidade dos seus recursos sempre que o usuário quer — disponibilidade aqui não é só estar up ou não, mas sim você ter a capacidade, o recurso de CPU e memória, para atender aquele determinado usuário.

Legal, então confiabilidade vai muito além. Eu não vou me aprofundar muito aqui, isso é tema de outro curso, mas eu queria trazer essa visão do que de fato é considerado sucesso na visão de um SRE — Site Reliability Engineer — que é um role que garante o sucesso de fato do software junto com o time de desenvolvimento.

Beleza, galera. Bom, então era isso que eu tinha para falar nesta aula. Até a próxima. Valeu!
