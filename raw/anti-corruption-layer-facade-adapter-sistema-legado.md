# Anti-Corruption Layer: Facade/Adapter entre Sistema Novo e Sistema Legado

Transcrição de vídeo/aula (pt-BR, autor não identificado no trecho colado). ASR bruto limpo, pontuado e organizado em seções abaixo — conteúdo técnico preservado sem paráfrase adicional.

## O Objetivo do Padrão

Por que esse padrão existe? Qual é o objetivo dele?

Ele serve, na verdade, para a gente não estragar o outro código. Então eu tenho um código novo e um código legado. Para não ter uma quebra muito grande arquitetural, estrutural, dos dois lados — basicamente como que ele funciona: a gente vai ter aqui um componente que vai ser responsável por fazer a tradução de um subsistema para outro subsistema. Então eu faço a substituição gradativa, e tudo que precisaria ser incomum ali, que traria algum tipo de impacto para um dos nossos componentes, para uma das duas pontas, a gente leva para essa camadinha intermediária.

Basicamente falando, parece bem simples — mas falando em alto nível é isso. Depois a gente vai ver um pouquinho mais no detalhe, vocês vão ver que tem algumas complexidades extras aí.

## Relação com Facade e Adapter

Implementação de uma camada fachada ou um adaptador — isso aqui a gente tá falando, na verdade, do Design Patterns: o Facade ou o Adapter. Um dos dois patterns aqui, eles servem para isso. Eles vão ajudar a gente a resolver esse problema. Esses dois padrões ajudam a gente nesse ponto.

## Problema 1: Dependência

Os problemas que ele resolve, basicamente: dependência. E essa aqui acaba sendo uma dor de cabeça grande — não é a maior (sempre falo para vocês que integração é), mas a gente acaba tendo integrações aqui também. E a gente tem, aqui, questão de dependência, que é um problema para arquitetos. É um problema por quê: sempre que a gente tem dependência, quando eu mudo um ponto eu posso danificar outro, quebrar outro. E tem dependências que são escondidas, que a gente não consegue diagnosticar tão facilmente.

E aí, quando a gente tem dependências escondidas ali, é super complicado. Como que eu posso criar uma dependência escondida? Por um componente que eu faço uma chamada através de uma configuração que às vezes até está num banco de dados. Imagina que eu tenho, sei lá, um microsserviço que, em algum momento do meu código, eu chamo ele — eu tenho um GET ali de uma URL, e essa URL vem de um registro lá de uma config que tá em banco, ou que tá num arquivo de configuração (mais fácil um pouquinho), ou que está em memória, numa variável de ambiente.

Então eu poderia também criar uma dependência assim. E, com algumas linguagens que suportam, por exemplo, reflexão — como .NET, Java — você faz uma reflexão do componente e linca um com o outro ali. Dá até para implementar em tempo de execução, com reflexão. Aí você cria dependências que são "medidas" (mascaradas) que você não consegue facilmente perceber.

Então, na verdade, aqui, quando a gente tá falando do padrão, ele evita que a gente tenha uma dependência forte entre os objetos da versão nova com a versão anterior. Se eu tenho diretamente meu sistema antigo — como a gente viu lá no Strangler [Fig] — chamando os componentes novos, eu tenho uma dependência forte. Essa dependência forte é um problema.

Por que ela é um problema? Porque se eu mudar qualquer coisa no meu sistema de origem ou no de destino, eu tenho impacto direto no outro sistema. Se eu mexer no sistema origem, no tocante àquela requisição que eu faço para fazer a chamada pro microsserviço novo, eu quebro — a minha aplicação do lado de cá para de funcionar. E se é o sistema provedor que muda qualquer coisa, tanto relacionada à resposta quanto à assinatura da requisição, a gente também tem problemas — quebra a outra ponta.

Então uma dependência direta gera esse tipo de dor. Gera uma dor forte. É uma dor de cabeça bem grande pra gente também.

## Problema 2: Sistemas Legados (Múltiplos)

A gente falou de dependências; outro problema que ele resolve é problemas com sistemas legados. Não só um, mas talvez vários outros sistemas legados que precisavam ali se falar — a gente tem isso resolvido também. Quando a gente coloca uma camada de anticorrupção, os impactos: como diminui a dependência, a gente diminui também problemas nos sistemas de origem ali, os antigos, que tipicamente são os principais e vão ser por um bom tempo quando você começa esse processo.
