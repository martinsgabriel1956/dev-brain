# DevSecOps — Dicionário do Programador (Código Fonte TV)

> Transcrição de vídeo em português (quadro "Dicionário do Programador", canal Código Fonte TV), fornecida como texto corrido sem pontuação. Reescrita como Markdown estruturado em seções temáticas para leitura. Sem necessidade de tradução — fonte já em português. Patrocínio do vídeo pela HPE preservado integralmente, conforme regra de transcrever sem cortar conteúdo.

## Abertura

Contextualizando, DevSecOps é um termo que significa literalmente *Development, Security and Operations* — traduzindo para o nosso português tupiniquim, desenvolvimento, segurança e operações. É um conceito que aborda a cultura e automação de segurança através de uma responsabilidade compartilhada em todo o ciclo de vida do software.

Esse conceito foi utilizado primeiramente em 2012 pela Gartner, três anos após a proposta do termo DevOps, fomentado por Patrick Debois sobre os métodos para soluções de conflitos entre as áreas de desenvolvimento e operações. DevSecOps foi primeiramente tratado como "DevOpsSec", e foi pensado a fim de acrescentar segurança aos processos de DevOps.

Fica com a gente até o fim para entender mais a fundo sobre esse termo.

Olá, CDF! Seja bem-vindo a mais esse Dicionário do Programador, o quadro do Código Fonte TV, onde a cada vídeo destrinchamos um termo, uma tecnologia ou uma palavrinha desse incrível mundo da programação.

## As Origens do DevOps

Pois é, para começar a falar sobre DevSecOps, vamos voltar um pouco e entender melhor o que é DevOps. Apesar de já estar com 14 aninhos, o DevOps ainda assusta muita gente que se pergunta "que bicho é esse?".

Patrick Debois, intitulado por ele mesmo no Twitter como "59% DevOps advice, público, orador público, consultor DevOps", fundador do blog *Jedi* (acrônimo para *Just Enough Documented Information* — informações documentadas apenas o suficiente), já deixava explícito o movimento ágil entre desenvolvimento e infraestrutura, que vinha propondo desde 2008. Nas próprias palavras de Patrick:

> "Muitas vezes me parece que a comunidade é conhecida apenas nos círculos de desenvolvimento, enquanto a ideia já se aplica a outras seções da empresa. Muitas dessas técnicas podem ser aplicadas a vendas ágeis, interface do usuário ágil e infraestrutura ágil — eles estão se referindo à possibilidade de um movimento ágil em torno de processos de infraestrutura e aplicações. Pena que ninguém além de mim se interessou."

Coincidência do destino ou não, em 2009 Patrick teve conhecimento de uma palestra da Velocity onde dois funcionários da Flickr apresentaram um tema intitulado "10+ Deploys por Dia: Cooperação entre Desenvolvedores e Operações no Flickr". Após essa saga em busca de compreensão a respeito do movimento que estava propondo, Patrick se torna o padrinho do conceito DevOps e cria o primeiro DevOps Day, em Gante, na Bélgica, no ano de 2009.

## Segmento patrocinado — HPE

Para nos ajudar a tratar desse tema de operações e segurança, temos o prazer de contar com nossa parceira HPE, que tem uma linha de software capaz de entregar soluções em nuvem para empresas. E você aí pensando ainda em servidores e impressoras — saiba que a HPE passou por várias transformações muito interessantes.

Você conhece o HPE Ezmeral? É uma plataforma com diversas ferramentas de análise e machine learning, feita para que as equipes de dados possam se concentrar na criação de valor a partir dos dados, e não em infraestrutura. Um dos seus pilares é o HPE Ezmeral Runtime, uma solução para modernização de apps e orquestração de containers. Com ele é possível trabalhar de forma unificada, podendo automatizar e gerenciar todos os clusters implantados, estejam eles hospedados em nuvens públicas, on-premise ou na borda. A HPE abstrai os detalhes de cada interface de gerenciamento dos provedores e disponibiliza tudo de forma centralizada.

Você pode conhecer a fundo as soluções da HPE e realizar treinamentos gratuitos através do link que está na descrição.

## De DevOps a DevSecOps

Você está agora se perguntando onde entra o DevSecOps nisso tudo. Assim como um filho não nasce sem uma mãe, DevSecOps provavelmente não existiria se a cultura DevOps não tivesse sido tão difundida.

Com a evolução em realizar processos colaborativos, manter ambientes estáveis, performados e resilientes, surgiram também alguns problemas em relação à qualidade dessas entregas — com equipes e até setores inteiros de segurança nas organizações. Ficou perceptível para todos que somente entregar de forma ágil e escalável não era o suficiente. A segurança como setor separado dos demais não poderia mais continuar em silos, considerando uma cultura de colaboração e responsabilidade distribuídas.

Então se agrega ao conceito o termo, ficando "DevOpsSec" inicialmente, até se compreender que os processos de segurança não estavam mais restritos a uma camada da aplicação ou da infraestrutura, mas ao todo organizacional — mudança por parte das equipes de desenvolvimento e infraestrutura. Ficou claro que não era apenas uma mudança em relação às ferramentas utilizadas, mas a cultura com que se produzia infra e código, trazendo para o ciclo de desenvolvimento e operações as camadas necessárias de segurança durante todo o processo.

Assim como as organizações precisaram realizar uma transformação cultural na virada de chave para os processos ágeis relacionados a DevOps, agora mais do que nunca precisariam enfrentar a grande vilã: a falta de segurança.

## O Manifesto DevSecOps

O Manifesto DevSecOps já deixa muito claro a urgência em atacar o problema da forma mais rápida possível, por meio da "segurança como código":

> "Sabemos que devemos adaptar nossos caminhos rapidamente e promover a inovação para garantir que os problemas de segurança e privacidade dos dados não sejam deixados para trás porque demoramos muito para mudar. Como sabemos, a quantidade de hackers, vírus de toda a natureza, são problemas que não podem ser deixados para resolver da noite para o dia. Os ataques cibernéticos são hostis e crescem a cada dia, gerando grandes prejuízos em diversos setores, desde grandes marcas a sites e sistemas governamentais."

Mas o que podemos então fazer diante de tamanha hostilidade e agressividade? O Manifesto DevSecOps é uma carta curta e direta sobre as ações que devem ser tomadas:

> "Não vamos simplesmente confiar em scanners e relatórios para melhorar a segurança — atacaremos produtos e serviços como alguém de fora para ajudá-lo a defender o que você criou. Não vamos esperar que nossas organizações sejam vítimas de erros e invasores. Não nos contentaremos em encontrar o que já é conhecido; em vez disso, procuraremos por anomalias ainda não detectadas."

Praticamente uma declaração de guerra para quem ousasse se aproximar. Numa época em que se desenvolviam somente sistemas monolíticos, onde os ciclos de desenvolvimento duravam meses e até mesmo anos, a segurança era completamente isolada. Atualmente, para garantir a eficácia em ciclos cada vez mais rápidos e frequentes, a segurança precisa fazer parte de todo o processo.

## O Que Defender

Mas afinal, o que realmente é preciso defender? Eu te digo: os dados, os containers, os clusters, a cloud. Defender, nesse caso, não é um ato passivo, mas uma ação ativa de proteção para o ciclo de vida da aplicação.

Porém, mesmo com todo o fluxo mapeado e defendido ativamente, ainda é possível ocorrerem brechas de segurança que podem ocasionar riscos. Como devemos reagir diante de brechas de segurança? Existem frameworks e normas — o conjunto de regras, como ITIL, COBIT, ISO 27001 — e compliance, que para as empresas representam estarem em conformidade com as leis, padrões éticos, regulamentos internos e externos.

Para reagir a falhas de segurança, é importante implementar processos ágeis, regras adequadas e boas práticas que estejam alinhadas com toda a implementação técnica nos fluxos de vida do desenvolvimento.

## DevSecOps no Ciclo de Desenvolvimento

Depois de muita história, entendemos que DevSecOps precisa fazer parte de todo o ciclo de desenvolvimento — é necessário incorporar segurança em todo o fluxo de trabalho, e não somente no final do ciclo e de forma isolada.

Vamos então a uma comparação. Em um contexto geral, as fases de fluxo do DevOps incluem: planejamento, código, build, teste, release, deploy, operação e monitoramento. Para DevSecOps, algumas ferramentas e tecnologias podem fazer parte do ciclo contínuo, para cada fase especificamente. Podemos citar aqui as seguintes ferramentas (a lista de ferramentas mudou muito rápido nos últimos anos e continua mudando):

- **Planejamento e análise:** Jira, Trello, ThreatModeler, Risk, Kanboard, WhiteSource, WeCan
- **Build:** Jenkins, Cube (provável referência a Kubernetes/CI), OWASP ZAP, Arachni, Husky, SQLMap, Liquibase, Talend
- **Deploy:** certificados TLS e DRM, Falcon, TripWire
- **Operações:** Prometheus, Zabbix, Suricata, OSSEC, Docker Bench for Security, Clair, IsNorth, New Relic

E a Alexlog (referência não totalmente clara na fala — provável menção à OWASP Foundation), uma fundação sem fins lucrativos que trabalha para melhorar a segurança do software, apresenta um guideline DevSecOps que demonstra como podemos implantar e promover a cultura de segurança através da abordagem *shift-left testing*, onde os testes passam a ser realizados no início dos estágios, e não somente no final das cascatas, ficando dessa forma integrado em todo o ciclo. Isso ajuda qualquer empresa que tenha pipeline de desenvolvimento a traçar uma perspectiva de segurança durante todo o processo.

A análise de segurança deve considerar todo o ciclo, do planejamento ao deploy. Aqui estão alguns termos que se utilizam para essas verificações:

- **Secret scanning:** escaneia os repositórios para encontrar possíveis vazamentos de credenciais
- **SCA (Software Composition Analysis):** análise de composição de software
- **IAST (Interactive Application Security Testing):** testes interativos de segurança de aplicativos

Vemos que, a cada etapa do ciclo, é primordial que a segurança seja implementada. Diferente de uma pipeline puramente DevOps, onde os testes de conformidade são realizados de forma isolada, muitas vezes através de consultorias e testes sem considerar todas as etapas do ciclo.

## Pessoas, Não Só Ferramentas

É importante frisar que ferramentas não são somente o conjunto de tecnologias utilizadas para gerar mais segurança aos processos, mas são também pessoas, times, equipes que devem ter participação ativa na segurança dos sistemas. O ser humano é parte do sistema, não somente na sua utilização, como também na sua criação.

Segurança contínua: constantes atualizações são realizadas todos os dias em linguagens de programação, frameworks, bibliotecas, sistemas operacionais — e tudo isso nos leva ao movimento ativo em relação à segurança. Como diz o DevSecOps: pessoas verificam ferramentas, e ferramentas verificam pessoas. Confie, mas verifique.

## Mercado de Trabalho

Como todos nós sabemos, o mercado de tecnologia está com um nível altíssimo de demanda para profissionais que atuam em cloud e segurança, e a demanda por profissionais deve continuar aumentando cada vez mais. Segundo pesquisa da Brasscom, até 2025 o mercado iria gerar cerca de 565 mil vagas em tecnologia — dessas, em torno de 125 mil somente de cloud e segurança, podendo agregar profissionais que tenham conhecimento dos dois mundos: o nosso tão falado aqui, DevSecOps.

Atualmente, no LinkedIn, 5 mil vagas com o termo DevSecOps para trabalho remoto.

## Encerramento

Sabendo que nem toda empresa trabalha da mesma forma, é importante salientar que existem diversas práticas de segurança que podem ser adotadas para o seu ambiente especificamente. Tudo que foi falado até agora são conceitos e boas práticas testadas e validadas nas organizações.

Caso você ainda não tenha nem sequer pensado sobre a segurança da sua aplicação, talvez seja um momento de começar a entender o quão importante ela é, para que você tenha um ambiente de desenvolvimento saudável e se prepare para escalar o seu tão sonhado projeto da maneira mais segura possível.

DevSecOps é uma cultura, um cargo, boas práticas para segurança, métodos ágeis de desenvolvimento, colaboração entre equipes, confiabilidade — é tudo isso e um pouco mais, uma combinação de filosofia, culturas e práticas consolidadas de segurança. Com o que abordamos hoje, podemos sentir o gostinho de uma pequena parte de tudo que é possível realizar com essa cultura, cada vez mais presente no nosso cotidiano — se é que ela já não estava por aí.

Nos conta através dos comentários se esse vídeo te ajudou, e também se deixamos algum assunto de lado — afinal, falar de segurança é sempre um grande desafio.

Aproveitamos para deixar um agradecimento especial ao Rafael Botelho, um super profissional DevOps que nos ajudou na construção desse conteúdo. Vamos deixar o link do canal e das redes do Rafael na descrição — vale a pena você conhecer o seu conteúdo.

Não esqueça também de deixar seu like e de conferir todas as ferramentas e treinamentos da HPE disponíveis no link que está na descrição. Nós vamos ficando por aqui, e então, até o próximo vídeo. Tchau, tchau!
