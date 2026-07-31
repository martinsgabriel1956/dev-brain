> Transcrição de vídeo/áudio em português (Lucas Badico), já no idioma original — sem necessidade de tradução. Transcrição bruta reorganizada em parágrafos e seções para legibilidade; conteúdo verbal preservado, sem paráfrase de substância.

# Golang Profissional: Por Que "Código Fofo" Não Existe em Go

Porque a real é que código fofo no Go tá perdido. E aí, pronto pra aprender Golang? Tu tá empolgado pra aprender Golang comigo essa semana, que bonitinho, ele tá empolgado. Mas claro que ele tá empolgado pra aprender uma linguagem nova — todo mundo se empolga pra aprender uma linguagem nova. Mas deixa eu te falar, senta direito um pouquinho na cadeira que eu vou lançar três dicas brabas sobre como é a realidade de codar Golang profissionalmente, e que eu não vejo a galera que produz conteúdo falar muito — porque a real é que código fofo no Go tá perdido.

Olá, eu sou Lucas Badico, dev, mentor e apaixonado por programação. Programando em Golang profissionalmente há praticamente 5 anos hoje, mas nesse momento há 3 meses exclusivamente como programador — ou seja, eu deixei os meus cargos de liderança e gestão. Estou simplesmente codando em Golang das 10 da manhã até às 10 da noite alguns dias — tá bem da hora, bem puxado, mas bem gostoso. E eu tô aqui pra te falar como tem sido e o que você pode esperar dessa carreira, dessa realidade de ser dev Golang.

Se fôssemos resumir esse vídeo, o resumo seria: Golang não é pra código fofo.

## Dica 1 — Não existe grande framework em Go

A primeira coisa que o "código fofo" busca são grandes frameworks que vão resolver a vida dele, vão dizer exatamente como ele tem que codar. Quem acompanhou as minhas lives construindo meu sistema sabe que em Golang não tem isso. Você tem recomendações, boas práticas da comunidade, mas você nem tem uma grande lib que todo mundo usa — como é o Rails no caso do Ruby, ou como Express no caso do Node — e você não tem também a prática da comunidade definitiva. Você tem recomendações: tem pessoas que usam de uma forma, pessoas que usam de outra forma, tem empresas que vão usar uma coisa, outras empresas vão usar outra coisa.

Então não existe um grande framework para Golang. A verdade é que Go desestimula grandes frameworks. Existe um ditado que diz que é melhor repetir um pouquinho de código do que acoplar a uma grande biblioteca. Então é muito comum você repetir código, você escrever. E vamos pra segunda dica.

## Dica 2 — 80% das suas dependências vão ser a standard library

A segunda dica é: 80% das suas dependências vão ser a standard library. Você vai ter apenas um pequeno percentual de dependências que são de fora da standard library, de pacotes bem estabelecidos — mas eles têm que ser coisas pequenas no seu projeto. E o jeito que a gente trabalha em Go faz com que a gente dependa muito pouco deles. Normalmente esses pacotes vão ser como o gRPC, o RM, o driver do seu banco de dados — esse tipo de coisa. Porque o resto você vai criar: ah, autenticação, você vai criar o interceptor de autenticação; ah, o logger, você vai criar o interceptor de log. Você não vai importar essas coisas, você vai codar essas coisas. E é uma coisa boa, porque se você vai codar essas coisas, você vai aprender como que elas funcionam. Eu amo esse tipo de coisa.

Um exemplo muito bom dessa questão de que a standard library atende quase 100% do que a gente precisa é o pacote `http`. O `net/http` do Go fez com que a gente não precisasse de 80% dos pacotes de HTTP servers que estão por aí, porque ele implementou o recurso que a gente mais precisava, que era o multiplex. Então no Go, no `net/http`, você não precisa mais ter algo como Express (pra quem é de Node) — os 80% daquelas libs que atendiam ao requisito de multiplex deixam de existir, porque agora você tem isso direto na standard library. E essa tendência é cada vez maior: pacotes de erros que eram muito usados foram incorporados à standard library, foi feita uma versão deles pra standard library.

Então muitas das coisas que você vai precisar no seu dia a dia estão na standard library. Você tem que conhecer a standard library. E lembra: não tem um framework na standard library. Não existe um framework — existem várias ferramentas, pedaços do que o seu sistema precisa, que você vai juntar, e você vai ter então a sua versão do que o sistema precisa. Então lembra: repetir é melhor do que acoplar. Repita isso nos comentários pra dar aquela força no engajamento.

## Dica 3 — Go exige que você sente e escreva bastante (e a questão dos genéricos)

E a última dica braba é: se tem uma linguagem que vai exigir que você sente a bunda na cadeira e code, é Golang. Tem a questão da filosofia de que um pouco de repetição é melhor do que muito acoplamento. Mas por muito tempo o Go não tinha genéricos. O que genéricos dão? Digamos que você tem que fazer uma função que é um mapper, uma high order function que pega outra função e pega vários tipos de itens que vai iterar sobre esses itens. Antigamente você não tinha como fazer um mapper genérico, porque não existiam genéricos — você tinha que fazer uma versão desse mapper pra cada tipo de item, pra cada tipo de lista.

Hoje em dia você já consegue fazer, mas a filosofia de você escrever bastante continua enraizada no Go, e a gente continua preferindo escrever do que ter um genérico super inteligente que resolve tudo pra gente. O genérico a gente está usando tem muito caso de uso, mas são coisas muito pequenas, são um pedaço que você precisa que seja inteligente pra trocar o tipo — coisas muito inócuas.

Por exemplo, o meu handler é uma repetição atrás de repetição — isso não é só porque é o meu projeto, em todo projeto grande de Golang você vai ter isso: vai ter o handler que é uma repetição atrás de repetição das mesmas funções. A gente prefere escrever do que ter algo genérico muito inteligente que pode quebrar se algo mudar — quebra tudo. Então pra gente é muito mais estável dessa forma.

Quando o Go faz isso — quando os criadores da linguagem, os mantenedores que estão lá em cima decidindo as features, decidem isso — eles escolhem tirar a engenharia da programação e fazer com que a programação de grandes sistemas volte a ser programação, volte a ser algo divertido. Por quê? Porque é simples. Você mesmo, no início... então você tá começando — o meu curso, meu curso começa no dia 25, provavelmente um dia depois do lançamento desse vídeo. No meu curso você vai aprender o básico da linguagem, e com esse básico você vai poder assistir as minhas lives e entender o que eu tô fazendo nas lives, porque são ferramentas básicas sendo repetidas e repetidas e repetidas.

Isso é muito bom, afasta gente que quer coisa mágica. Você não vai ter nada mágico com Go. Se você quer algo mágico, vai pra Elixir, vai pra Ruby on Rails, vai pra Laravel — mas não tem nada mágico em Go. É muita repetição, e isso é algo muito bom: faz com que a sua carreira seja tranquila se você se dedicar, e faz com que cada hora que você gasta codando você tá de fato evoluindo as suas habilidades em Go, porque não tem nada escondido no Go.

## Fechamento

Então cara, é isso — se prepara. Se você quer mesmo entrar de cabeça no Go, se prepara pra escrever muito, pra codar bastante, porque é isso que o Go te convida a fazer.

Se você quer aprender, já falei bastante do meu curso, mas vou deixar aqui a última chamada: você quer aprender Golang do dia 25 de novembro ao dia 29, de segunda a sexta, eu vou estar ensinando Golang aqui pra vocês. Vou ensinar um ABC, o básico, e vou mostrar como você sobe uma API bem simples usando a standard library, pra você conseguir brincar com o Postman que eu ensinei no último curso e a sua própria API.

Beleza, então esse fica o convite. E se você não sabe ainda o que é API, não sabe usar o Postman, te convido a correr assistir o curso de Postman, que vai estar aqui, ou assistir o último vídeo que eu falo sobre o Go, que vai estar aqui. Obrigado, e até o curso — te vejo lá.
