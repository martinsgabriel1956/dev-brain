Nessa aula nós vamos falar sobre o ciclo de mudança de uma arquitetura.

Como eu falei já no vídeo anterior, uma mudança de arquitetura requer que você esteja muito alinhado com o negócio. É o que acontece: quando você for implementar uma arquitetura — por exemplo, definir que vai usar um Event Sourcing, ou uma arquitetura de coreografia, ou uma arquitetura de orquestração, ou um CDC, ou um Transaction Outbox, enfim, independente de qual — existe um ciclo, um período de convívio com as versões.

Então é muito importante que você seja assertivo, porque o trabalho leva um tempo. E se você perceber no meio do caminho que esse caminho não é o certo, claro, é legal que você vai trocar — que bom que você percebeu — mas isso vai fazer com que você perca muito tempo para conseguir fazer uma entrega de valor de fato para o negócio.

Então, num ciclo bem breve, qual é a ideia aqui?

Primeiro você faz uma avaliação do seu AS-IS. Você precisa entender de fato 100% não só a tecnologia, mas sim as regras de negócio. Você tem que pegar todos os pontos-chave dos problemas que você tem, das necessidades, o que não tá funcionando bem, o que tá funcionando bem. Você tem que entender 100% o seu AS-IS.

Depois você começa a pensar nos seus objetivos — vamos definir um futuro da sua aplicação, o que é muito chamado de TO-BE. Aí você desenha o seu TO-BE.

É claro que desenhar não vai compilar. Você precisa ir para o próximo passo, que não é fazer uma migração, mas sim executar uma prova de conceito, muito conhecida como POC, onde você faz uma versão bem mínima — não é nem mínima, na verdade é um teste mesmo, uma prova de conceito — onde você consegue simular se aquilo realmente funcionaria como você acha.

Você faz essa POC e ela funciona muito bem, mas aí você tem que começar a fazer testes nessa POC para de fato confirmar que aquilo te atenderia. Vamos supor que funciona muito bem, e ali você tem uma quantidade de 10.000 transações por segundo esperadas. Imagine que você tem 10.000, aí você faz uma POC testando só 500 conexões/transações por segundo — isso é válido? Talvez você estivesse falando de mudar a base de dados: será que, se você botar ali 10.000 TPS, aquela arquitetura que você fez na base de dados vai atender a sua necessidade? Talvez não. Então teste tudo: se é 10.000, teste pelo menos 10.000. Entenda o que muda ao rodar 1.000, 5.000, 10.000 e, se possível, 15.000 — como seria aquele comportamento? Você não precisa testar 100%. Não estou falando de fazer um MVP, porque o MVP vem depois dos testes.

Então, funcionaram os testes, deu sucesso: agora você vai começar a trabalhar numa migração. E para fazer uma migração, você precisa começar pequeno. Existem outros padrões de coexistência entre dois ambientes: você está lá com o seu TO-BE, que é o sistema A, e tem o seu sistema B (o legado). Existem algumas formas de fazer essa migração, e você tem que conviver com os dois. Existem padrões que ajudam nisso, tanto na reescrita, na decomposição de um serviço, como também na comunicação entre eles — para evitar que um afete o outro, porque eles vão continuar tendo que conversar. Enfim, existem muitos outros padrões.

Quando você finaliza, a ideia é que você entregue pequenos resultados. Vai existir todo um planejamento da migração oficial, você realiza sua migração, finaliza, e isso vai virar o seu novo AS-IS. E aí vira um trabalho, um fluxo contínuo de melhoria de arquitetura.

Beleza, galera? Bom, é isso que eu tinha para falar nesse vídeo, e vamos ao próximo. Valeu!
