---
title: "Atrofia cognitiva, IA e a síndrome do pânico de esquecer programar"
type: transcript
date_ingested: 2026-07-03
---

# Atrofia cognitiva, IA e a síndrome do pânico de esquecer programar

Transcrição de vídeo (falado, PT-BR original — sem necessidade de tradução).

---

Eu quero falar sobre esse pânico geral que os programadores estão tendo de não conseguir usar os seus "mega brain" para programar, achando que nunca mais vão conseguir escrever um código manualmente. Peguei alguns papers aqui que estão dizendo que o dev tá sim perdendo a capacidade de codar, que estão basicamente esquecendo a sintaxe básica. Eu acho que isso é uma baboseira, é uma estupidez. E venho aqui falar de experiência própria: fiquei 3 anos sem escrever código, zero, e depois voltei pro meu melhor momento da carreira. Então é por isso que, quando eu vejo esses tipos de estudos, eu não fico preocupado, porque já aconteceu comigo — já fiquei 3 anos sem escrever código e depois foi a primeira vez que eu consegui uma vaga na gringa. Mas quem sou eu, né? Vamos ver esses papers acadêmicos de 2026, saindo agora essa semana, fresquinho, que medem essa tal atrofia do teu "mega braindin".

O que os autores estão falando é o seguinte: eles propõem que ter uma assistência de IA não causa só o que eles chamam de *disuse atrophy* — que seria esquecer porque tu parou de usar — mas causa uma atrofia cognitiva, um *cognitive offloading*. Tu delega a parte cognitiva pro teu cérebro, e o teu cérebro reorganiza as informações da forma maleável que ele é, e essas conexões viram meio que uma via única: tu para de fazer as conexões que antes tu fazia.

Tem outro paper: **"The Instrumental Dissolution of Typing: Why AI Challenges the Keyboard Era in Knowledge Work"**. Aqui não é só sobre programador, é sobre parar de digitar em geral. O argumento é que digitar código vai virar basicamente a mesma coisa que aconteceu quando a gente esqueceu de escrever à mão — uma skill que tu pratica na escola mas que ninguém usa profissionalmente. O que esses estudos debatem é se a infraestrutura mental que sustenta essa skill vai sumir junto ou não.

Depois tem alguns depoimentos surgindo — um no Reddit de alguém reclamando do seu senior engineer, mais pessoal: o autor conta que começou a perder a habilidade de codar. É um dev sênior, 15 anos de carreira, falando que perdeu a capacidade de escrever um `for` loop sem pedir pro Claude.

Na verdade, eu digo o seguinte: a gente já tinha esquecido como fazer algumas coisas perguntando pro Google. Acho que é sempre o mesmo debate — a gente tá sempre debatendo as mesmas coisas. Antigamente a gente falava que esquecia das coisas que procurava no Google. Lembro do início desse canal: uma das coisas que mais recebi comentário agradecendo foi minha transparência em falar que minha capacidade como dev vem da forma que eu consigo buscar no Google. Eu falava direto aqui, há 6 anos atrás, que a melhor habilidade que tu pode desenvolver é fazer uma boa pesquisa no Google, que tu não precisava memorizar as coisas. E parece que a gente tá repetindo essas mesmas coisas, como se isso importasse.

Mas tem uma diferença que a literatura aponta: entre quem usa IA já tendo um histórico, uma base sólida, anos de prática — levou anos pra desenvolver aquela habilidade e começou a usar IA depois — versus quem nunca teve essa base. No primeiro caso, mesmo esquecendo temporariamente, tu acaba lembrando depois, é como andar de bicicleta ou de skate. Agora, se tu nunca teve isso, obviamente não vai lembrar — tu não consegue lembrar do que nunca aprendeu.

### O post do Reddit

> "Meus engenheiros seniors pararam de pensar por si mesmos. 3 anos nesta empresa, eu realmente gostava da minha equipe. Nosso tech lead costumava ser o cara que passava horas elaborando projetos de sistema complexos num quadro branco, explicando cada custo-benefício e garantindo que todos entendessem o porquê das decisões. Na última terça, ele enviou um PR com a descrição: 'fluxo de autenticação refatorado com base na saída do ChatGPT'."

Isso tá virando meio que uma prática de mercado. E o pior não é quando um dev gera um ticket que o GPT escreveu e depois resolve ele com IA. O pior é quando alguém *fora do time*, uma pessoa não técnica, gera esse ticket porque aprendeu a conectar o repositório do projeto no Claude. Aí tu tem tickets no backlog vindo com detalhamento técnico escrito por uma IA, planejado por alguém não técnico — como se essa pessoa fosse um analista de sistemas de 2002.

Continuando o post:

> "Eu pedi que ele me explicasse as alterações e ele me olhou como se eu tivesse pedido para ele recitar o código de memória. 'É só colar no ChatGPT e pedir pra ele explicar.' Este é um engenheiro sênior, um cara que eu admirava."

Será que isso é atrofia? Será que é só preguiça? Será que a gente tá sendo sobrecarregado com mais tarefas e não tem mais tempo de ensinar alguém mais júnior o que tá criando? Ou será que de fato a pessoa nem entendeu o que criou, porque quem escreveu o código foi a IA?

Já estão surgindo outras skills pra isso — tipo usar a IA como um "GRE"/vestibular sobre o PR que a própria IA criou, pra validar entendimento (vou gravar um vídeo sobre isso). Mas aqui o foco é: será que a gente tá atrofiando? Será que eu ainda sei o que é uma VPS, como conectar nela por SSH, qual a melhor VPS pra hospedar meus projetos?

*(Trecho publicitário sobre Hostinger/VPS omitido — não é conteúdo técnico relevante.)*

### O teste de 12 questões

Peguei um teste de 10–12 questões de "fundamentos" pra ver se a gente ainda consegue resolver, sugerindo 20–60 minutos pra tentar. Exemplos:

- **Escrever um `for` loop com índice, sem autocomplete.** Testei em Kotlin no terminal, sem indentação nem autocomplete. Cheguei perto (`for (i in lista.indices) println("$i: ${lista[i]}")`), mas travei em detalhes tipo se é `size`, `length` ou `lastIndex`. Isso eu já não escrevo de cabeça há anos, e não tem nada a ver com IA — tem a ver com dependência do LSP e autocomplete da IDE, que existe desde muito antes de LLMs (plugins de autocomplete de linha já existiam desde ~2008, antes do Copilot).
- **Inverter uma string com dois ponteiros, sem `.reverse()`.**
- **Tratar erro 401 e 500 com try/catch separados.** A sintaxe importa pouco — a questão real é entender *o que* é 401 (não autorizado) e 500 (erro interno do servidor), e o que fazer em cada situação.
- **Escrever um regex de cabeça.** Ninguém memoriza regex — sempre se usou builders/playgrounds online.
- **Resolver conflito de merge via linha de comando (git puro).** Aqui houve um "leapfrog": fui de resolver merge conflicts via CLI pra usar IA, explicando o que está conflitando. Antes, resolver um conflito exigia entender os dois diffs (branch A vs branch B) e por que cada lado modificou aquela linha, decidindo se aceita um lado, o outro, ou funde os dois porque são regras de negócio diferentes coexistindo na mesma linha. Hoje a IDE (Android Studio) já resolvia boa parte disso "magicamente"; com IA dá pra puxar o diff + a descrição do PR como contexto extra pra decidir o merge com mais informação — a IA não escreve o código por você aqui, ela acelera a busca de contexto.

Conclusão: não dá pra ter medo de não estar codando tudo na mão. A IA já ganhou esse jogo — mesmo que a bolha estoure (falando de valuation, IPO da Anthropic etc.), ainda vamos ter modelos locais rodando autocomplete de graça. Decorar como fazer um `for` com índice é bobagem; isso já tinha sido resolvido antes da IA, só com autocomplete de linha.

### A exceção: quem aprendeu a programar nos últimos 18 meses

Aqui sim há um caso diferente: o dev que aprendeu a programar já com Claude Code do lado desde o início, que nunca soube fazer um `for` loop sem autocomplete. O impacto de uma eventual "IA ficar mais cara" vai ser totalmente diferente pra essa pessoa do que pra quem já programa há 10, 15, 20 anos. O medo de quem começou há 18 meses é justo.

Recomendação pra esse público: focar em **conhecimento perene**, não em escrever sintaxe manualmente. Exemplos de conhecimento perene:

- Quais são as principais causas de um erro 401 e de um erro 500.
- Como debugar uma falha que só acontece em produção, não no ambiente de dev.
- Como fazer catch de um erro e propagá-lo até a interface com uma mensagem adequada (hierarquia de exceptions em OO, subir a exceção pela stack de chamadas até a função de entrada).
- O que é uma stack call.

Sintaxe não importa — escrever código já foi resolvido há muito tempo, independente de IA, pelas ferramentas modernas de desenvolvimento.

### Paralelo com escrita e leitura

Assim como os artigos falam sobre escrever à mão (skill de escola, não usada profissionalmente), o maior problema do brasileiro não é a falta de escrita — é a interpretação de texto, a capacidade de ter clareza no pensamento. Escrever é a ferramenta que leva a essa clareza; ler é a ferramenta que leva a melhor interpretação. Usando IA ou não pra resolver problemas complexos, tu ainda tá escrevendo (o prompt) e lendo (a resposta gerada). Não estamos eliminando essas habilidades humanas — só mudando a forma como são exercitadas.
