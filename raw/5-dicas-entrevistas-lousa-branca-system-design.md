# 5 Dicas para Passar em Entrevistas de Lousa Branca / System Design

Transcrição de vídeo em português (canal Full Cycle, apresentador Wesley Willians). Sem áudio original em inglês; transcrição bruta reformatada em Markdown, sem alteração de conteúdo, apenas organizada em seções e com pontuação corrigida para legibilidade.

## Introdução

Vídeo sobre como se sair bem nas entrevistas de "lousa branca" (whiteboard) ou system design que grandes empresas costumam aplicar — o momento em que perguntam coisas como "como você faria um Twitter", "como você desenvolveria um Facebook", "como você cria um encurtador de URL". É nesse momento que o candidato mostra conhecimento de arquitetura de software e de solução, maturidade no desenvolvimento de tecnologias e o repertório acumulado na carreira que ajuda a criar um sistema escalável, com alta disponibilidade etc.

O vídeo também promove o MBA em Arquitetura Full Cycle, com menção a mentores como Uncle Bob, Robert "Justos" (referência a Robert C. Martin), Vaughn Vernon e Bernardinho.

## Contexto da entrevista

Quando o candidato chega nessa etapa, já passou pelo RH e por alguma entrevista técnica básica ou desafio de código. Na sessão de lousa branca / system design, o time de tecnologia dá um "case" e o candidato precisa destrinchar diversos aspectos dele. Importante: **system design é uma coisa, design system é outra** — no vídeo fala-se de system design.

## Dica 1 — Gerencie o tempo

Essas sessões costumam durar entre 40 e 50 minutos. O tempo é um fator importantíssimo e deve ser monitorado o tempo todo, porque é fácil não conseguir chegar ao fim da sessão. Uma recomendação direta: **não saia desenhando nada de cara** — vão faltar elementos, e a impressão passada é a de alguém fazendo um monte de coisa sem perguntar nada antes.

## Dica 2 — Não tenha medo de perguntar / comece pelos requisitos

É esperado que o problema apresentado não venha com todos os elementos necessários para resolvê-lo. Por exemplo, ao receber "como eu desenvolvo um encurtador de URL", é preciso perguntar coisas como quantos acessos esse sistema vai ter, quantas pessoas vão gerar URLs encurtadas — só fazendo essa pergunta já se sabe se o sistema é para 10 pessoas ou para 1 milhão.

A dica central aqui é **começar pelos requisitos**. Todo sistema tem funcionalidades "core" (essenciais) e funcionalidades auxiliares. Pergunte aos entrevistadores quais são as funcionalidades core — é nelas que o foco de desenvolvimento da solução deve estar. As funcionalidades auxiliares ficam para depois, se sobrar tempo.

## Dica 3 — Plano de capacidade

O entrevistador espera que o candidato crie um plano de capacidade, fazendo cálculos básicos como:

- Quantas requisições por segundo ou por minuto o sistema vai receber.
- Quais são os picos de acesso e as requisições esperadas nesses picos.
- Qual banda é necessária para a aplicação funcionar.
- Quanto se vai gastar em disco para armazenar dados por dia, por ano, para 5 anos.
- Qual será o *replication factor* em disco — quantas cópias das informações serão mantidas.

Trazer esses cálculos como resposta sinaliza ao entrevistador que o candidato se preocupa em entender requisitos e em criar um plano de capacidade real.

## Dica 4 — Modelagem de dados e de API

Este ponto é um pouco mais "tricky": o candidato precisa mostrar que sabe modelar banco de dados, mas a ideia não é fazer uma modelagem complexa — é mostrar repertório sobre dados. Partes do sistema podem usar um RDBMS, outras um banco chave-valor, outras um banco focado em busca (search), por exemplo. Isso demonstra o repertório de como o candidato trabalha com diferentes tipos de banco de dados.

Junto com isso, é preciso trabalhar a modelagem da API: colocar os principais endpoints e até chamadas internas entre sistemas, mostrando que o candidato sabe o que é um request, um response, os principais códigos de retorno, e qual protocolo será usado (HTTP, gRPC etc.). Esses itens ajudam o entrevistador a perceber que o candidato sabe do que está falando.

## Dica 5 — O desenho na lousa (system design propriamente dito)

Só nesse momento é que o candidato começa a fazer os desenhos na lousa branca — não que a modelagem de dados, o plano de capacidade e os cálculos anteriores não sejam registrados por escrito, mas o desenho, as chamadas e os casos de uso ficam para essa etapa. É aqui que os entrevistadores avaliam o repertório do candidato e, principalmente, se o que está sendo desenhado tem relação com o que foi dito antes de chegar a esse desenho. Esse é considerado um dos pontos mais importantes da sessão.

## Dica extra — Nunca minta sobre tecnologias que você não domina

Nunca, jamais, coloque no desenho tecnologias com as quais você não teve experiência real. Depois da sessão de system design, os entrevistadores começam a perguntar detalhes do porquê daquela escolha de tecnologia, e vão descendo o nível de profundidade da pergunta para calibrar o conhecimento real do candidato.

Exemplo dado: se o candidato diz que usaria o Prometheus como gerenciador de métricas, o entrevistador pode perguntar como funciona o sistema de alarmes do Prometheus, que tipo de banco de dados ele usa, quais são as quatro formas de gerar informação para consulta, como fazer determinada consulta em PromQL etc.

A recomendação é: coloque apenas tecnologias que você domina. Se quiser citar uma tecnologia que não domina totalmente, faça um disclaimer explícito — algo como "estou colocando essa tecnologia porque no time em que trabalhei o pessoal utilizou isso, mas eu, pessoalmente, não tenho um conhecimento profundo sobre ela".

## Sobre lidar com "não sei"

Esses tipos de entrevista são estressantes e todas têm um objetivo em comum: fazer o candidato, em algum momento, dizer "não sei" — não interessa quem seja o candidato, o entrevistador vai descendo o nível de dificuldade das perguntas até encontrar esse limite. Isso é esperado e normal; o problema é fingir que sabe tudo.

Quando não souber algo, a recomendação é dizer diretamente: "eu não sei, e eu gostaria muito de aprender sobre isso — pelo que percebi, vocês trabalham bastante com isso, então seria muito bacana ter a chance de me aprofundar nesses temas aqui." Não tente "sabonetear" (enrolar) tentando falar um monte de coisa para escapar da pergunta — quem entrevista está acostumado a perceber isso, e a impressão final fica pior ainda.

## Fechamento

Recomendação geral: se acostumar com esse tipo de sessão e buscar exemplos de system design na internet. Novo convite para o MBA em Arquitetura Full Cycle, que tem disciplinas focadas em system design.
