# Tecnologias que já foram hype (e ainda sustentam o mundo)

Transcrição de vídeo do canal de Bernardo Lobato. Limpa de erros de reconhecimento de fala (ASR) e formatada em Markdown — conteúdo original em português, sem necessidade de tradução.

## Abertura

Você já teve vontade de jogar todo o seu conhecimento fora para aprender o framework da moda que surgiu de ontem para hoje? Acha que se ficar dois dias sem acompanhar as tendências do mercado vai te defenestrar da nossa área para sempre? Então esse vídeo é para você.

No vídeo de hoje vamos falar de algumas tecnologias que já foram hype, mas hoje nem tanto — e ainda assim são as que fazem o mundo funcionar como a gente conhece. E tudo isso longe do hype. Então já tira a tarde inteira de hoje para debugar aquele documento WSDL, que o vídeo já vai começar.

Olá, dev. Eu sou Bernardo Lobato e hoje quero bater um papo um pouquinho mais leve. Se existe uma característica da nossa área que muda pouco é a velocidade com que as discussões mudam. Basta surgir uma nova tecnologia, uma nova arquitetura, uma nova ferramenta, para que boa parte da atenção da comunidade se volte imediatamente para ela. Isso é saudável até certo ponto. Durante algum tempo parece que aquele é o único caminho possível e que tudo que veio antes perdeu relevância, como se estivesse prestes a desaparecer — isso pelo menos no mainstream.

Com o passar dos anos, no entanto, a realidade costuma seguir um caminho diferente. Muitas das tecnologias que deixaram de aparecer em conferências, cursos e discussões nas redes sociais continuam presentes em sistemas importantes, movimentando aplicações críticas e recebendo manutenção diariamente em empresas gigantescas. Elas apenas ficaram em segundo plano, sem chamar tanta atenção, enquanto outras passaram a ocupar mais esse espaço do mainstream.

Nesse vídeo eu separei cinco exemplos de tecnologias que já foram consideradas ultrapassadas em diferentes momentos, mas que continuam desempenhando papel importante em empresas de todos os portes. Mais do que falar sobre cada uma delas, a ideia é mostrar que o ciclo de novidade da nossa área nem sempre acompanha o ritmo com que as tecnologias realmente deixam de ser utilizadas.

## 1. SOAP

A sigla, em inglês, para Simple Object Access Protocol, surgiu em 1998 em um movimento de empresas que começava a integrar sistemas distribuídos pela internet. O protocolo foi criado com forte participação da Microsoft e de outros pesquisadores, e alguns anos depois acabou sendo padronizado pelo W3C.

Naquele período ainda não existia um padrão amplamente aceito para comunicação entre aplicações desenvolvidas em plataformas diferentes, e cada fornecedor costumava implementar sua própria solução. Já aplicações diferentes mas na mesma plataforma, como Java, por exemplo, possuíam soluções próprias para interoperabilidade — quem lembra do Java RMI ou mesmo do CORBA?

O principal problema que o SOAP procurava resolver era justamente a interoperabilidade entre plataformas diferentes. Empresas precisavam conectar aplicações escritas em Java, C++, .NET e outras tecnologias sem depender de implementações específicas de cada fornecedor. Além disso, setores como bancos e seguradoras exigiam recursos relacionados a segurança, assinatura digital, criptografia, transações distribuídas e contratos bem definidos entre cliente e servidor. O ecossistema formado por especificações como WS-Security, WS-ReliableMessaging e WS-AtomicTransaction surgiu exatamente para atender essas necessidades.

Entre aproximadamente 2002 e 2008, o SOAP tornou-se praticamente o padrão para o desenvolvimento de serviços corporativos. Frameworks como Apache Axis, JAX-WS no Java, e o Windows Communication Foundation (WCF) da Microsoft ajudaram a consolidar sua adoção, enquanto o formato WSDL facilitava a geração automática de clientes e servidores.

A partir do início da década de 2010 o cenário começou a mudar. A expansão das aplicações web e dos smartphones aumentou a demanda por APIs mais leves e simples de consumir. O REST, aliado ao JSON, passou a atender boa parte desses cenários com uma complexidade muito menor. Para muitas aplicações, manter toda essa infraestrutura do SOAP simplesmente deixou de fazer sentido.

Mesmo assim, o SOAP continua bastante presente em ambientes corporativos. Bancos, seguradoras, operadoras de saúde e órgãos governamentais ainda mantêm milhares de serviços baseados nesse protocolo. Em vez de desaparecer, ele acabou se consolidando como uma tecnologia voltada para cenários em que contratos rígidos, interoperabilidade e requisitos avançados de segurança continuam sendo diferenciais importantíssimos. Para quem trabalha com ERP: o sistema de integração com as notas fiscais da Receita Federal, até hoje, é integrado através do protocolo SOAP.

## 2. XML

O XML — Extensible Markup Language — tornou-se uma recomendação oficial da W3C em 1998. Seu desenvolvimento foi coordenado por Jon Bosak, da Sun, juntamente com um grupo de especialistas que buscava criar um formato de dados simples, aberto e independente de plataformas. A ideia surgiu como uma alternativa mais flexível ao SGML — ou até mesmo como uma especificação em cima do SGML — preservando sua capacidade de representar documentos estruturados sem carregar toda a sua complexidade.

O problema que o XML procurava resolver era relativamente claro: empresas precisavam trocar informações entre sistemas completamente diferentes, muitas vezes desenvolvidos por fornecedores distintos e utilizando tecnologias incompatíveis. Era necessário um formato que pudesse representar dados de maneira estruturada, validável, e suficientemente genérica para atender desde documentos até integrações corporativas.

A sua popularização aconteceu principalmente entre o final da década de 1990 e toda a década de 2000. Nesse período, praticamente toda a tecnologia corporativa adotou o XML de alguma forma. O protocolo SOAP, inclusive, utilizava XML como formato de mensagens. O Maven, bastante utilizado no Java, adotou o pom.xml para descrição de projetos. O Apache Ant utilizava o build.xml. Tecnologias como JAXB, DOM, SAX, XSD e XSLT formaram um enorme ecossistema para manipulação e validação de documentos, enquanto diversos padrões industriais passaram a utilizar XML como formato oficial para troca de dados.

Com o crescimento das aplicações web, principalmente após a popularização do Ajax e dos dispositivos móveis, formatos mais compactos passaram a ganhar espaço. O JSON oferecia menor volume de dados, era mais fácil de manipular em JavaScript e exigia menos processamento para serialização e deserialização. Para APIs modernas, essas características acabaram tornando o JSON dominante.

Ainda assim, o XML permanece extremamente presente em diversos setores. Além do SOAP, ele continua sendo utilizado em documentos do Microsoft Office, projetos Java, arquivos de configuração, nota fiscal eletrônica e inúmeros padrões internacionais. Sua presença diminuiu principalmente nas APIs públicas voltadas para aplicações web, mas continua sendo uma tecnologia importante sempre que padronização, validação e interoperabilidade são requisitos fundamentais.

## 3. ESB (Enterprise Service Bus)

O conceito de Enterprise Service Bus surgiu no início dos anos 2000 como uma evolução das soluções tradicionais de integração empresarial. A ideia foi fortemente influenciada pelos padrões descritos por autores como Gregor Hohpe e Bobby Woolf em *Enterprise Integration Patterns*, embora diversos fornecedores também tenham desenvolvido suas próprias plataformas. Ao longo do tempo, empresas como IBM, Oracle e Tibco foram responsáveis por transformar esse conceito em produtos amplamente utilizados por grandes empresas do mercado.

O problema enfrentado pelas grandes organizações era relativamente comum: ao longo dos anos, empresas acumulavam dezenas ou até centenas de aplicações diferentes, incluindo ERP, CRM, sistemas legados, bancos de dados, aplicações desenvolvidas internamente e até soluções adquiridas de terceiros. Fazer cada sistema conversar diretamente com todos os demais criava uma arquitetura extremamente difícil de manter.

O ESB surgiu justamente para centralizar essa comunicação, oferecendo recursos como transformação de mensagens, roteamento, orquestração de serviços, monitoramento e adaptação entre protocolos diferentes. Inclusive, muitos dos serviços SOAP comentados acima eram publicados e orquestrados em plataformas de ESB, que atuavam como um barramento central para integrar dezenas ou centenas de sistemas diferentes.

A popularização dessa estrutura ocorreu aproximadamente entre 2004 e 2015. Plataformas como MuleSoft, IBM Integration Bus e Oracle Service Bus tornaram-se referências em projetos de integração corporativa, sendo amplamente adotadas por bancos, seguradoras, empresas de telecomunicações e órgãos governamentais.

O cenário começou a mudar com a consolidação da computação em nuvem, da arquitetura orientada a eventos e da economia das APIs. Em muitos projetos, as equipes passaram a preferir integrações mais distribuídas, utilizando API REST, mensageria e plataformas como Kafka, em vez de concentrar boa parte da lógica de integração em um barramento central. Essa mudança reduziu significativamente o entusiasmo em torno dos ESBs, principalmente em projetos novos.

Apesar disso, eles continuam desempenhando papel importante em organizações que possuem um grande legado tecnológico. Empresas que passaram décadas construindo seus sistemas dificilmente substituem sua infraestrutura de integração de uma vez só. Nesses ambientes, soluções como MuleSoft e IBM Integration Bus continuam sendo utilizadas para conectar aplicações desenvolvidas em épocas diferentes, preservando investimentos realizados ao longo de muitos anos.

## 4. jQuery

O jQuery foi criado em 2006 pelo desenvolvedor americano John Resig, em uma época em que o desenvolvimento para a web era significativamente mais trabalhoso do que é hoje. Os navegadores implementavam JavaScript e o DOM de maneiras diferentes, fazendo com que uma funcionalidade que funcionava, por exemplo, no Firefox, apresentasse problemas no Internet Explorer e em outros navegadores. Além disso, tarefas relativamente simples — como selecionar elementos da página, manipular HTML ou realizar uma requisição Ajax — exigiam muito código e um bom conhecimento das diferenças entre cada navegador.

O principal objetivo do jQuery era justamente eliminar essa complexidade. Seu famoso lema, "write less, do more", refletia bem essa proposta. Em vez de obrigar o desenvolvedor a lidar com as particularidades de cada navegador, a biblioteca ofereceu uma API única e muito mais simples para manipulação de DOM, tratamento de eventos, animações e comunicação assíncrona com o servidor.

Sua popularização aconteceu de forma extremamente rápida entre 2007 e 2013. Em poucos anos, praticamente todo projeto web acabava utilizando jQuery. O crescimento foi impulsionado também por um enorme ecossistema de plugins e ferramentas, como jQuery UI, jQuery Mobile, DataTables, e também pelas primeiras versões do Bootstrap, que utilizavam jQuery como dependência obrigatória.

A partir de meados da década de 2010 o cenário começou a mudar. Os navegadores passaram a seguir os padrões da web com muito mais consistência, reduzindo a necessidade de bibliotecas de compatibilidade. Ao mesmo tempo, muitos recursos disponíveis somente via jQuery acabaram sendo introduzidos na própria linguagem JavaScript, que evoluiu bastante com o ECMAScript 2015 (ES6), dependendo cada vez menos dessas bibliotecas externas. Paralelamente, frameworks como AngularJS, Angular 2, React e Vue introduziram uma forma completamente diferente de construir interfaces, baseada em componentes e gerenciamento de estado, reduzindo ainda mais o espaço ocupado pelo jQuery.

Mesmo assim, a biblioteca continua extremamente presente em aplicações corporativas, sistemas internos, portais desenvolvidos ao longo da última década e diversos produtos comerciais. Hoje ela é dificilmente escolhida para novos projetos, principalmente os da moda, mas continua sendo uma das bibliotecas mais utilizadas na história da web e permanece com manutenção ativa, recebendo correções e atualizações até os dias de hoje — seu último release estável foi publicado em 17 de janeiro de 2026.

## 5. COBOL

O COBOL é uma das linguagens de programação mais antigas ainda em uso. Seu desenvolvimento começou em 1959, sob orientação de um consórcio formado por representantes da indústria e do governo dos Estados Unidos. O objetivo do COBOL era resolver um problema bastante específico da época: computadores estavam deixando de ser utilizados apenas para cálculos científicos e começavam a automatizar atividades administrativas de grandes empresas. Era então necessário criar uma linguagem capaz de representar regras de negócio, processamento de registros, operações financeiras e relatórios de forma legível e relativamente independente do fabricante do hardware — algo incomum naquele período.

Sua popularização ocorreu principalmente entre as décadas de 1960 e 1980. Bancos, seguradoras, empresas de telecomunicações, companhias aéreas e órgãos governamentais adotaram o COBOL em larga escala para construir seus sistemas centrais. Ao longo desse período, tecnologias como o mainframe IBM System/360, além de compiladores como IBM Enterprise COBOL e Micro Focus COBOL, tornaram-se parte fundamental do ecossistema.

A partir dos anos 1990, linguagens como Java, C# e C++ passaram a dominar o desenvolvimento de novas aplicações corporativas. Além disso, a expansão da internet, das interfaces gráficas e da computação distribuída deslocou boa parte do desenvolvimento para plataformas mais modernas, reduzindo significativamente o número de novos projetos escritos em COBOL.

Entretanto, a realidade do mercado continua bastante diferente da percepção criada ao longo dos anos. Grande parte do sistema financeiro mundial executa aplicações escritas em COBOL, responsáveis por processar milhões de transações diariamente. Em vez de substituir esses sistemas integralmente, muitas organizações optam por modernizar sua arquitetura, expondo funcionalidades por meio de APIs, filas de mensagens e novos serviços, enquanto o núcleo da lógica de negócio permanece o mesmo, em COBOL. O resultado é uma tecnologia que praticamente desapareceu das discussões sobre novos projetos, mas continua sustentando algumas das aplicações mais críticas e confiáveis da indústria atual. Boa parte da infraestrutura do sistema financeiro brasileiro — inclusive os sistemas que dão suporte ao Pix — depende de aplicações escritas em COBOL.

Um dado que pode chamar a atenção: o COBOL continua evoluindo até hoje. A versão mais recente do padrão oficial da linguagem foi publicada em 2023, mais de 60 anos após a criação da linguagem em 1959. Hoje ela possui recursos como orientação a objetos, tipos de dados definidos pelo usuário e suporte a caracteres Unicode.

## Encerramento

Cinco tecnologias, cinco histórias diferentes, mas com um fio condutor em comum: nenhuma delas morreu de verdade. Elas só saíram um pouco das notícias. Fica um recado e uma reflexão: a indústria de tecnologia é obcecada com o novo, mas o que realmente sustenta o mundo na maior parte do tempo é o que já está rodando há décadas, sem holofote nenhum. Às vezes o mais relevante é o que nunca parou de funcionar.

Da próxima vez que você sentir aquela ansiedade de "preciso aprender o framework que saiu nos últimos 15 minutos", lembre desse vídeo. O SOAP ainda está rodando desde 98. Ele está lá, tranquilo. Você também pode ficar por um tempo.
