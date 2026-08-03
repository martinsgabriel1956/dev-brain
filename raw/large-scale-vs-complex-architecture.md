# Large Scale Architecture vs. Complex Architecture

> Transcrição de aula em português, já no idioma original (sem necessidade de tradução). Pontuação, paragrafação e alguns erros óbvios de transcrição automática (ex.: "chart" → "sharding", "as 401" → provavelmente "AS/400") foram corrigidos para legibilidade. Trechos genuinamente ambíguos ficam marcados como `[transcrição incerta]`.

Fala galera, beleza?

Nessa aula nós vamos falar sobre a definição de **Large Scale Architecture** e **Complex Architecture**. São dois termos que você pode ouvir e eles podem estar muito relacionados à sua arquitetura — ela pode ser tanto os dois quanto pode ser só um.

## Escalar

Quando a gente ouve "large scale architecture", a gente tá falando de uma arquitetura escalar. Fui até na definição das palavras — não achei "escala" como substantivo no sentido que eu queria, achei o verbo "escalar". Gostei muito dessa definição e também da de complexidade.

Escalar, basicamente, é a relação entre as diferentes dimensões de um desenho. Imagina que você tem uma imagem que é a sua arquitetura e você precisa expandi-la para aumentar o tamanho dos dados, o consumo da sua arquitetura. Como que você escala? Expande o seu banco de dados, expande os seus computes. E não é só uma questão de colocar um auto scale — não é uma questão simples assim. São muitos fatores que você precisa preparar, e vamos ver isso quando falarmos dos patterns.

São diversas camadas (layers) que você precisa escalar — não é só a computação, a base de dados também é outra. Tudo tem um limite, é finito. Uma base de dados não atende TPS infinito. Aí vêm questões de você aprender a usar sharding para aumentar a resiliência, mudar a forma como você armazena os dados, aumentar o TPS, diminuir o tempo de resposta (latência), enfim.

Então, quando a gente está falando de large scale, é uma arquitetura que **não necessariamente é complexa**. Ela está mais focada em ter capacidade e engenharia para atender aquela escala que a aplicação pode ter.

## Complexidade

Já a complexidade acontece em **todos** os tipos de arquitetura — pequenas ou não, com large scale ou não, para 100 usuários ou para 1 milhão de usuários. Isso é um pouco reflexo dos padrões escolhidos.

Claro que às vezes é inviável evitar. Tem momentos em que a complexidade da regra de negócio é complexa de fato. Quando a gente pega empresas grandes — enterprises que já estão no mercado há 50, 60, 70 anos —, temos um desafio muito grande: a complexidade de modernizar as aplicações enquanto se mantém o passado. Refatorar gradualmente.

Imagina uma empresa que começou num mainframe e, de repente, foi jogando workloads para um AS/400, depois para Linux, depois para Windows. Começa a virar um ambiente complexo. E aí tem uma dependência grande — você não conseguiu sair do mainframe, deixou três workloads lá, dois no AS/400, catorze no Linux, vinte e oito no Windows `[transcrição incerta quanto aos números exatos]`. Aí você começa a ter uma relação entre eles: eles têm que se comunicar, têm integração, têm uma forma de trocar dados. Você tem batch, tem online, tem transacional, e começa a virar uma bagunça. Geralmente a complexidade é algo presente nos ambientes enterprise.

Agora, empresas recentes — mesmo que grandes, tipo startups que deram um boom e cresceram do nada — podem ter complexidade, sim, mas não passaram pelo problema que muitas enterprises antigas passaram, que é ter uma coisa muito antiga e precisar adaptá-la para o novo modelo. A complexidade talvez seja menor nesse caso.

### Características de uma arquitetura complexa

- Diversas camadas, com componentes interdependentes (um depende do outro).
- Sistemas com tecnologia poliglota — Linux, Windows, outra versão X, outra Y, container, Java, e por aí vai.
- Muitos tipos de comunicação convivendo: SOAP, REST, mensageria assíncrona, batch — gerando aquela "bagunçinha".
- Regras de negócio bem complexas — geralmente porque a empresa precisa conviver com o passado: "eu atendia isso no passado, não posso desligar, não tenho como reescrever toda a aplicação e parar de entregar novas funcionalidades".
- Às vezes é só uma questão de **over thinking** — excesso de pensamento — que não simplifica as coisas e acaba gerando arquiteturas complexas por conta própria.

## Large Scale

Quando a gente fala de large scale, estamos falando de arquiteturas projetadas para suportar sistemas que operam em um nível extenso de volume de dados. Como eu falei, não é necessariamente complexa — pode ter algoritmos complexos, mas numa visão de alto nível a arquitetura em si é mais simples. Você pode, a nível de código, ter um sharding implementado, mas isso não é complexo no sentido "poliglota e tudo mais" da arquitetura complexa.

Large scale é caracterizada pela necessidade de **alta disponibilidade** — aplicações com picos, sistemas bancários, lojas virtuais, qualquer startup que precise disso. Geralmente utiliza, consciente ou inconscientemente, padrões de arquitetura — não tem como não usar. É comum, quando eu converso com empresas para entender as aplicações que elas têm, eu já perceber: "olha, você usou tal pattern" — e a partir disso já consigo inferir quais são os trade-offs e os problemas que provavelmente existem. Por exemplo: ele escolheu isso aqui, então provavelmente tem problema com observabilidade ou monitoração; ele escolheu aquilo, então não tem problema disso, mas vai ter problema daquilo, e assim por diante.

Geralmente envolve diferentes tecnologias de computing e storage engines de banco de dados — então existe uma complexidade, sim, mas não exatamente poliglota como na arquitetura complexa. Você começa a não usar só uma base de dados: talvez um S3 para armazenar objetos, um CDN, um Redis ou Memcached para chave-valor. Você precisa estar apto a responder a isso.

Aqui em large scale a gente fala de algo muito interessante: **dividir para conquistar**. Você divide em diversos pedaços para conseguir atender o número de usuários que pode aparecer.

Além do software que atende de fato o negócio e o usuário final, existe o que é chamado de **control plane** — os controladores da arquitetura. Por exemplo, num ambiente de sharding, você precisa mover um usuário de um shard para outro; isso exige uma camada de controle própria. Numa arquitetura complexa isso nem sempre existe, porque ela é complexa por natureza, não necessariamente por escala.

### Over-engineering

No large scale, é comum ver, de um lado, **over engineering** — "eu preciso de tanto, tanto, tanto" que a pessoa acaba colocando ferramental e tecnologia demais, fazendo mais engenharia do que precisava — e, do outro lado, o **over thinking** que já mencionei na complexidade.

## Como saber se uma arquitetura é complexa?

Qual é a métrica? Sinceramente, não sei — e não classifico arquiteturas como complexas ou não. Não sei se alguém classifica assim. Gostaria de ouvir a opinião de vocês nos comentários.

Eu diria que, dentro dos itens que eu falei, "arquitetura complexa" é muito relativo — o que é complexo para mim não é complexo para você. Não é um pattern, não é uma resposta sim/não, e nem valeria a pena montar um checklist com pontuação para isso. Poderia até fazer, mas não adianta muito: independente da classificação, os patterns vão te ajudar dos dois jeitos. E geralmente, quando é complexa, é porque estamos falando de enterprises, como eu falei.

Beleza, galera. Isso é o que eu tinha para falar nesse vídeo. É longo e importante, é fundamental, e espero que você tenha entendido. Voltamos a falar na próxima aula. Valeu!
