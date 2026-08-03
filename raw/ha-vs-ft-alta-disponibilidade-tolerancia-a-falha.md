# HA vs FT — Alta Disponibilidade vs Tolerância a Falha

Nessa aula vamos falar sobre a diferença de HA e FT, que é High Availability ou Fault Tolerance, ou alta disponibilidade ou tolerância a falha. O nome já diz um pouquinho né?

Mas vamos começar com alta disponibilidade. Abstrai aqui o tipo de tecnologia. Não estamos entrando nesse detalhe por hora, porém, a ideia do alta disponibilidade é que ele é altamente disponível. Eu não estou dizendo que ele pode tolerar ou ter uma indisponibilidade sem que ninguém perceba, né? Então o sistema conta disponibilidade. Ele existe uma indisponibilidade, Ele só é a alta disponibilidade, né? Então, talvez ele seja 95% de disponível, mas não 99,9 ou quase próximo dos 100%. Que seja, quantos novos você tem e enfim.

Então imagina, você tem 100 ali, 100 TPS, né? Transações por segundo, um monte de usuário conectando ele passa ali para uma camada que seja qual seja ela, né, E ele cai uma porcentagem dos usuários numa. Num datacenter que seja um DC um e também um DC dois, né? Então tem os dois datacenters. E o que acontece? Eu vou ter 50/50 em cada um deles, mas a minha base de dados. Note que ela é um Failover, então mesmo que o meus servidores aqui eu tenha ele 100% igual, não disponível, não é 100% igual ao mesmo dado a mesma versão, os dois rodando ali na versão dois.

O que acontece é que a base de dados não é, como você pode ver aqui, a minha base de dados 1 Ela está fazendo um failover se necessário, então aqui ela seria uma base primária e aqui a minha secundária. Então, durante um problema, o que acontece é que existe uma indisponibilidade para eu fazer esse switch de carga, Então geralmente isso acontece. Você vê ambientes que você tem cluster, ai eu tenho aquele cluster, né meu, meu Suse Cluster, Redhat Cluster, meu MySQL Cluster. Não estou falando de um, de um, de algumas. Não estou falando de clonar ali, de outros mecanismos.

Existem formas de você fazer uma alta disponibilidade, mas vamos dizer assim, um sistema de tolerância falha. Aí ele já tolera. Toleraria, né? A falha.

Então, nesse exemplo que eu dei, o datacenter 2 caiu. Existe uma indisponibilidade até ele fazer um failover para outra, para para o outro lado do datacenter. Já que nesse outro exemplo todos os servidores, né? Note que eu tenho até mais servidores aqui, que seja, Então tenho mais servidores aqui. Eles são todos iguais. Como você pode ver, server A, server A, server A, server A e o que acontece é que eu tenho alguma forma aonde eu persisto. Os mesmos dados nesse DB 1 que eu persisto aqui e aí ele existe um clone para o outro lado né, Que seria um Failover.

Então mesmo que eu tenha uma indisponibilidade nesse datacenter, o que acontece é que ainda vou continuar operando porque eu tenho uma réplica ali. Então um dos nós de fato, ele faz um failover para um outro datacenter. Porém, eu tinha um outro que estava ativo lá.

O problema é que quando a gente começa a falar de tolerância a falha, a gente começa a pensar em aumento de custo, né? Por isso que eu coloquei aqui tolerância à falha. O custo é bem superior, então tem que ver. Muitos negócios fazem bastante sentido. E existe também engenharias que precisam ser feitas ou a seleção da base de dados também precisa ser feita nesse exemplo, que ela de fato faça com que você consiga tolerar essa falha.

Eu não estou falando que é 100% de disponibilidade aqui, tá, pessoal? Mas se o usuário estava ali fazendo naquele momento, escrevendo uma coisa nessa base de dados e esse datacenter venha cair, com certeza Ele receberia um erro, mas quando ele tentasse de novo, ele já ia cair para o outro lado e o banco de dados estaria ali em pé.

Então essa é a principal diferença. Note, quando a gente fala de tolerância, falhas, o custo com certeza é bem superior, porque o tipo de tecnologia que você vai ter que ter, ela é superior e a gente vai falar bastante sobre isso. Nos padrões, quando a gente realmente começar a falar dos padrões.

Beleza, pessoal? Então é isso aí e até o próximo vídeo. Valeu!
