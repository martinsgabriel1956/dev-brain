# Microsserviços: história, SOA/ESB, benefícios e desafios (Bernardo Lobato)

Fonte: transcrição de vídeo do YouTube, canal de Bernardo Lobato. Já em português — sem necessidade de tradução.

---

Você já precisou escalar uma parte do seu sistema, mas acabou percebendo que ia precisar escalar tudo junto, duplicando suas máquinas, duplicando seus bancos de dados e principalmente duplicando seus custos? Já trabalhou num projeto tão grande em que várias equipes atuavam ao mesmo tempo e quando dava algum problema no build era aquele Deus nos acuda e todo o time ficava parado? Já teve um bug, um erro em produção que, quando acontecia, tirava a solução inteira do ar? Então esse vídeo é para você. Já vai pedindo a pizza e se preparando para passar a madrugada inteira fazendo deploy em produção, que o vídeo já vai começar.

Olá devs, eu sou Bernardo Lobato e hoje a gente vai finalmente falar sobre essa que foi uma febre ali dentro dos times de desenvolvimento e de arquitetura de sistema dos últimos anos: os famosos microsserviços. Modularizar a aplicação, aumentar a coesão, diminuir o acoplamento são sonhos antigos dos desenvolvedores, e a gente consegue atingir boa parte dessas características com o uso dos microsserviços. É isso que a gente vai ver aqui hoje.

Porém, antes da gente mergulhar de cabeça nesse estilo arquitetural, para começar a entender do que se trata, de onde veio e para onde vai, vamos tentar entender um pouquinho o histórico, como surgiu esse modelo e a tomada de decisões que acabou levando ele a se tornar o queridinho ali dos desenvolvedores nos últimos anos.

## Origem histórica

Em 2005, um então desenvolvedor chamado Peter Rogers acabou usando o termo "microweb service" dentro de uma conferência chamada Web Services Edge. A ideia dele nesse artigo era apresentar serviços enxutos, pequenos, altamente independentes e com baixo acoplamento. Isso era uma certa inovação para a época, que estava acostumada com a utilização e a popularidade do modelo SOA, que reinava na época, principalmente em grandes empresas, em grandes corporações.

### O que é SOA

Aqui neste momento eu acho importante trazer um pouquinho do que é essa arquitetura SOA, para a gente poder entender como o microsserviço funcionaria ali como um contraponto a ela. SOA, ou Service Oriented Architecture, é um estilo arquitetural organizado em serviços independentes que se comunicam por interfaces bem definidas, normalmente através de um barramento de serviço. A ideia central aqui era usar esse barramento para que as aplicações pudessem conversar entre si de uma maneira ordenada e padronizada.

Nesse modelo, os serviços costumam ser mais robustos e genéricos, e costumam utilizar protocolos de comunicação mais pesados, como SOAP com XML. Existe também um componente central nesse modelo chamado ESB (Enterprise Service Bus). É através desse componente que todos os serviços se comunicam; além de centralizar os acessos, fornecia também recursos como roteamento de mensagens, segurança, monitoramento etc. É um componente bem robusto, que demanda mão de obra especializada e consome uma boa quantidade de recursos.

É importante ressaltar também que essa cultura do SOA foi muito forte dentro de soluções corporativas, e os ESBs mais conhecidos eram normalmente oferecidos por grandes fornecedores como IBM, Oracle, SAP etc. Essas ferramentas eram, e ainda são até hoje, muito populares e muito difundidas no mercado corporativo de grandes aplicações, e muitas empresas ainda seguem com muito sucesso esse estilo arquitetural. E só para constar, existem também ESBs de código aberto, bastante difundidos — um exemplo conhecido é o WSO2 ESB.

### A proposta de Peter Rogers como contraponto ao SOA

Dito isso, vamos voltar à apresentação do Peter Rogers. O que ele propunha na época era a diminuição do tamanho desses serviços, e também a adoção de um novo protocolo — ao invés de SOAP com XML, que é bem verboso, a utilização de REST, protocolo que já existia na época, porém não era tão difundido assim, principalmente em grandes empresas. O objetivo dele era tentar trazer alguma simplificação naquele modelo de SOA existente.

Acho que agora deu para ficar um pouco mais claro de onde esse nome "microsserviços" surgiu: era, de certa forma, uma oposição ao modelo vigente de SOA.

### 2012: o nome se consolida

Já em 2012, um grupo de arquitetos acabou optando pelo nome "microsserviços" como um nome apropriado para arquiteturas de sistemas que usem essas características (e outras que serão discutidas mais adiante). Nesse mesmo ano, em 2012, na Polônia, houve a apresentação de um grande case que utilizava esse estilo: "Microservices — Java, the Unix Way". Essa apresentação trazia a ideia de que os serviços de uma aplicação deveriam seguir a mesma filosofia (ou uma filosofia parecida) do sistema operacional Unix, em que cada processo tinha uma única e pequena responsabilidade, e vários desses processos (ou serviços) podiam trabalhar em conjunto para resolver problemas maiores — ou seja, uma abordagem arquitetural em que a aplicação era dividida em serviços pequenos e independentes, e cada um resolvia um único problema de sua responsabilidade.

## Definição formal

Tendo essa base, vamos entender agora um pouco mais formalmente o que é e como funciona uma arquitetura em microsserviços. É uma arquitetura descentralizada na qual as funcionalidades são desacopladas e independentes, implementadas em serviços diferentes. Cada serviço deve implementar uma única funcionalidade, ou seja, deve ter uma e somente uma responsabilidade dentro de um contexto delimitado.

Na prática, para que uma implementação seja considerada um "serviço" independente dentro dessa arquitetura, ela deve cumprir três requisitos:

1. Deve ser uma aplicação **standalone** — deve funcionar sozinha.
2. Deve possuir um **deploy independente** — a entrega dessa aplicação não deve, em hipótese alguma, depender da entrega de outras aplicações.
3. Deve implementar uma **funcionalidade útil** dentro do domínio do problema que está sendo resolvido.

Com base nisso, dá para explorar outros assuntos relacionados para garantir que a implementação siga os melhores padrões de desenvolvimento e estabeleça uma comunicação eficiente entre esses serviços.

### Bounded context e comunicação exclusivamente via API

Os serviços dentro dessa arquitetura são fortemente inspirados no conceito de **bounded context** (contextos delimitados), conceito do DDD que visa delimitar os limites de maneira muito clara dentro de um subdomínio ou domínio de uma aplicação.

E também, por conta do baixo acoplamento e da independência entre esses serviços, é de extrema importância que eles sejam acessados somente via API — API de uma maneira genérica (não necessariamente REST, não necessariamente mensageria). O que isso quer dizer: nada de integração via banco de dados, nada de dois serviços acessando o mesmo banco de dados para se ter acesso aos dados de um serviço específico. Esses dados têm que estar exclusivamente disponibilizados via API. Então, se tem uma coisa a se levar desse vídeo, é isso: cada microsserviço tem o seu próprio banco de dados, e ninguém além dele pode acessar esse banco. (Nota do autor: no próximo vídeo dessa série ele explica por que isso, levado ao pé da letra sem cuidado, pode ser uma péssima ideia.)

## Exemplo: sistema de streaming (tipo Netflix/YouTube)

Como seria uma arquitetura de microsserviços com um sistema de streaming? Alguns serviços possíveis, em alto nível:

- **Autenticação e autorização** — gestão de login, perfis de usuário e permissões.
- **Catálogo** — informações de filmes, séries e metadados (gênero, sinopse, elenco etc.).
- **Recomendação** — sugestões personalizadas usando um algoritmo proprietário da empresa.
- **Streaming** — entrega de fato dos vídeos, adaptando qualidade conforme a conexão do usuário.
- **Pagamentos / assinatura**.
- **Histórico, notificações, upload** etc.

A ideia aqui não é detalhar uma implementação real, mas dar uma base de entendimento.

### Diferenciação de serviços: recomendação vs. streaming

Um serviço de **recomendações** com algoritmo proprietário é interessante de manter independente do restante do sistema, porque permite fazer alterações e experimentar nesse algoritmo com uma velocidade diferente da entrega dos outros componentes — mais agilidade para testar nuances diferentes, com um único deploy, sem comprometer o restante da arquitetura. Isso também permite manter um time focado especificamente na melhoria desse algoritmo.

Já o serviço de **streaming** tem grande oportunidade para escalabilidade, por ser (a princípio) o que mais consome recursos de todo o ambiente. Isso permite pensar numa stack diferenciada, com uma linguagem de programação mais otimizada para vídeo ou arquivos brutos — independência até na stack e na tecnologia utilizada, focando em eficiência de código sem comprometer o restante da arquitetura.

## Benefícios

- **Independência de serviços**, gerando baixo acoplamento (aplicações standalone).
- **Manutenibilidade** — cada desenvolvedor foca no escopo do seu serviço, não na solução inteira.
- **Escalabilidade** — serviços menores que consomem poucos recursos podem ser escalados individualmente conforme a demanda específica, sem precisar escalar (e pagar por) o restante do sistema.
- **Resiliência** — quando uma parte do sistema é comprometida por um erro em produção, não necessariamente a solução inteira se degrada; aquele pedaço de funcionalidade pode ser contornado para que a arquitetura inteira não caia por um único problema.
- **Independência tecnológica** — cada serviço pode ter sua própria stack (linguagem, banco de dados) conforme o que aquele serviço precisa entregar.
- **Equipes independentes** — múltiplos times, cada um focado em um microsserviço ou grupo pequeno de microsserviços, reduzindo o escopo de onboarding e a curva de aprendizado (sem "onboarding de uma semana" só para conseguir buildar o projeto pela primeira vez).

## Desafios

- **Aumento da complexidade de infraestrutura** — não é só codar e entregar; é preciso ter rotinas de monitoramento, alguém acompanhando CI/CD etc.
- **Problemas "resolvidos" no monolito reaparecem de forma distribuída** — comunicação entre serviços, rede de computadores, latência, largura de banda, tamanho de dados transferidos, circuit breakers etc.
- **Dados distribuídos e consistência eventual** — cada serviço tem sua própria base de dados; é preciso lidar com o fato de que as bases, em todo o ecossistema, podem eventualmente não estar consistentes naquele momento — é preciso de estratégias para replicar o que foi produzido num serviço para os outros serviços interessados naqueles dados.
- **Curso de operação (custo)** — componentes separados, se mal dosados/mal estudados, podem levar a um custo financeiro maior do que numa aplicação monolítica (ressalva do autor: isso é caso a caso — também existem monolitos que consomem recursos "infinitos"; depende do fit da arquitetura com quem está desenvolvendo).
- **Capacitação do time (desafio pouco falado)** — o modelo não é intuitivo, principalmente para quem já trabalha num modelo tradicional de monolito. É muito fácil, num processo de migração (ou mesmo num desenvolvimento novo), implementar só parte das estratégias de descentralização — por pressão de prazo, desconhecimento do time ou falha na gestão técnica — parando mais ou menos no meio do caminho, e aí abrir mão de características importantes (como compartilhar banco de dados ou compartilhar bibliotecas de código para evitar duplicação). Isso pode ser desastroso para o projeto.

Segundo o autor, essa é a grande diferença entre projetos que têm chance de dar certo e projetos que vão fracassar e precisar ser reescritos num futuro não muito longo (ou até imediatamente, conforme o projeto vai ficando mais complexo). Dica: se você quer treinar esse modelo, comece com projetos mais simples, embarque o time nessa empreitada e aprendam juntos, ou capacite o time se você já tem mais experiência. O importante é todo mundo entender que está no mesmo barco, entender as motivações, e não cada um seguir seu próprio padrão — fadando o sistema ao fracasso.

## Quando não vale a pena (ainda)

Se você está começando um projeto pequeno que precisa entregar valor rápido, ir para a rua rápido, ou um MVP que ainda precisa ser validado, talvez a complexidade não se pague. Nesse caso, o monolito bem feito, bem desenhado, bem estruturado e com responsabilidades que possam ser quebradas no futuro de maneira pouco traumática pode ser a melhor opção para o sistema que está nascendo.

## Vídeos relacionados citados pelo autor

- Um vídeo sobre **vertical slices**, como ponto de partida para quem está pensando em migrar de um sistema monolito para um sistema mais distribuído.
- Um vídeo sobre **bounded context** (DDD), que ajuda a definir o escopo de um serviço dentro de uma arquitetura orientada a microsserviços e mapear os serviços que serão disponibilizados pelo sistema.
