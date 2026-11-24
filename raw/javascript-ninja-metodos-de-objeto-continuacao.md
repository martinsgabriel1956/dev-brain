# JavaScript Ninja: métodos de objeto (continuação) e desafio da semana 3

Voltamos então com um curso de JavaScript Ninja. Estamos na nossa terceira aula, falando sobre objetos. Meu nome é Fernando Daciuk, que nós estávamos falando no último vídeo sobre métodos de objeto, certo?

## Propriedade × método

Então, basicamente, método de objeto, como você viu, eles são funções que você usa como o valor da propriedade do objeto. Então sim, relembrando aquilo que nós tínhamos lá: objeto pessoa. Ele tem uma propriedade de nome, que recebe logo o nome, é uma propriedade, que eu tenho aqui um método andar, que é uma propriedade andar que recebe, no caso, de uma function. E quando eu tenho uma propriedade que recebe uma function, com o nome dessa propriedade se torna método.

Então, se eu chamar pessoa ponto o nome, que ele vai me retornar o nome. Isso é uma propriedade. Agora, se eu chamo uma pessoa ponto andar, andar está aqui, no caso, é uma função. Eu vou precisar invocar ela para ver o resultado dela. Ele vai retornar para mim com o pessoal andando. Significa que o andar, na verdade, é um método do objeto pessoa, certa?

Então essa diferença de propriedade [e] método, basicamente, olhando aqui, olhando aqui, porque a gente já viu sobre funções e variáveis. Quando você cria uma nova variável, vai mais largo a dois, por exemplo, isso aqui é uma variável, certo? É quando você cria uma função, funcional arroz, isso aqui é uma função. Então eu criei que uma variável, crio uma função.

Basicamente, quando você faz isso dentro de um objeto, objeto, ao invés de variável, você tem uma propriedade, que recebe um valor, e você tem um método quando você cria uma função aqui, ok?

Então meu objeto ponto propriedade, ele é basicamente como se fosse a minha variável, sobre como estar dentro do objeto. Ele nos chama a variável, de chama propriedade. E quando eu tenho o meu método, ele não se chama função, ele se chama método. Da função, e quando eu crio ela fora do objeto, como eu criar dentro do objeto, então ela acaba se tornando o método desse objeto.

Beleza, acho que ficou simples até aí. Agora pode... já pode participar do desafio dessa semana 3 agora, beleza?

## Desafio da semana 3

Então vamos lá, vou mostrar para vocês aqui no repositório. Está, aumentar um pouquinho aqui. Você podem ver que o desafio 3 já está aqui, está no repositório. Tem umas coisas bem legais aqui, está?

Uma coisa que eu queria comentar só aqui: estou pedindo para a gente, vai trabalhar bastante com o objeto e métodos e propriedades aqui nesse desafio, da criação de métodos, de criação de objetos e criação de propriedades no objeto.

Uma coisa que eu quero comentar aqui, basicamente, é que eu não deixei anotado porque eu queria comentar aqui no vídeo: e quando você tem esses retornos aqui, está. "Crie um método chamado o nome completo, que retorna a frase: Olá, meu nome é", nome e sobrenome, um ponto de exclamação.

O que acontece é que você vai retornar e isso aqui da pessoa que está dentro do parênteses, é isso que está entre colchetes aqui, só as variáveis, são as variáveis que você vai utilizar. No caso, que o nome vai ser a propriedade, o nome do teu objeto que você vai criar. Você vai ver no exercício do desafio que você vai fazer. E aqui vem seu sobrenome.

Então, sempre que tiver um nome assim, todo em maiúsculo, é com, entre, entre colchetes assim, significa que para você utilizar uma variável, está, aqui, para você concatenar essa string aqui. Como essa variável, essa propriedade, esse método, que, beleza? Eu sou pra você saber que tem um dos times que tem aqui, mas eu não deixei explícito falado ali.

## Atualizar o repositório

Então agora eu vou mostrar pra você. Vou mostrar mais uma vez, porque tem algumas pessoas que ainda estavam batendo um pouco cabeça pra poder fazer a atualização do repositório, pra poder ter o desafio 3 atualizado, como fazer o envio do desafio. Então eu vou mostrar que agora como a gente vai fazer para atualizar o repositório mais uma vez. Beleza, então tá.

A gente já tem forkado o repositório de vocês, já foram. Já estava tudo conta. Se já tenho challenge [1], challenge 2. Se você não tem ainda, assim, os vídeos anteriores que mostra como, como você vai fazer, como você criar o desafio, está nos vídeos anteriores, tem lá, então você pode assistir e lá vai mostrar.

Agora vou mostrar como a gente vai fazer pra atualizar com o desafio 3. Então tenho aqui o meu repositório, aqui no meu terminal. Se você utiliza isso, você está utilizando o software mesmo do GitHub, recomendo que você utilize a linha de comando, nesse caso aqui, pra atualizar por aqui. Até onde eu vi, o software do... ele não suporta mais de um remote.

Então eu, por exemplo, adicionou remote, que significa o quê? A origem, o original, caso, ele vai ser um mero repositório principal, o meu repositório na minha conta. Então, por exemplo, eu tenho lá a minha conta fdaciuk barra curso de JavaScript Ninja. Então esse vai ser o original, se vai ser um repositório que eles estão usando, e o upstream vai ser um repositório do curso mesmo, que o da2k curso JavaScript, que é esse aqui.

Este repositório principal, o nome dele vai se chamar eu percebi. Na aula 2 eu mostrei como que ele não tinha remote, que está aí. Você precisa adicionar de Ilídio comando, porque não tem como, como você adicionar: ou você vai adicioná-lo manualmente, ou você vai adicionar pelo remote. É melhor que você faça pela linha de comando, porque assim você vai manter tudo atualizado, exatamente como evitar. Eu recomendo, é bem simples usar linha de comando.

Mais uma vez: se você tiver dúvidas, se você não souber como fazer, se tivesse batendo muito para fazer, você pode entrar em contato comigo, que eu vou te ajudar a fazer isso e deixar o repositório atualizado.

Então vamos lá. Se eu der um comando aqui, bem, eu vou... eu vou ver que eu tenho duas vezes aqui: eu tenho a grande master, que eu tenho challenge 2. Eu não tinha challenge 1 aqui, porque eu não baixei, tinha nenhum. Eu tinha 29, e eu não baixei ela, que eu tinha só a minha master e a tela de 2.

Então, primeira coisa que eu vou fazer, era coisa: eu preciso atualizar o meu repositório com o repositório principal. Então eu vou fazer: eu vou voltar pra master, vou dar um jeito de checar de master. Então vou voltar aqui pra branch.

Beleza, estando aqui novamente, mas eu tenho o meu challenge 1, monte challenge 2 e o... então aqui tá faltando três. Como que eu vou fazer para puxar o tirei 3? Eu vou dar o comando efetivo. Então eu percebi que ele vai fazer o quê? Ele vai baixar logo do repositório principal, repositório do curso, todas as branches que estão criadas lá no repositório, como eu só tinha, mas ele trouxe aqui. Ele fez a atualização, e ele fez a leitura e tal, e fez da atualização. Então trouxe aqui pra gente. Massa.

Está bem, agora tem como fazer: eu vou fazer um merge Down Tim, mas tem gente que tem o challenge três, que eu acabei de puxar pra cá, como repositório. Você pode ver que ainda tem só a challenge 1, tira de dois. Eu vou fazer um MBA master.

Então eu fiz aqui, e ele atualizou. Eu tinha 2, algumas alterações lá, e eu tinha três. Ele trouxe. Eu dei um comando para ele estar aqui, vai mostrar que eu tenho agora challenge [1], challenge dois. Ela instrui os três aqui na master, e então em branco, tá? Ele não... eles não estão preenchidos, tá bom?

Então, se você vê aqui, eu tinha challenge um, amigo, me olhe, está em branco. Ele não deve ter preenchido na marra. A mesma coisa: challenge dois, ele não deve ter preenchido, deve tá todo em branco aqui. Eu tinha challenge 3 também, certo? Então tá todo, ele tá todo em branco aqui, está preenchido.

## Branch do desafio e envio

Beleza, ainda falta colocar, adicionar as respostas. Agora, como que você vai fazer pra, pra criar o Tinder 3? Você não vai editar direto na master. Antes de você começar a editar, o que você vai fazer: checkout menos B challenge fácil 03. Ele vai criar uma branch chamada de aprendizado 3, está, com todos os arquivos que estavam na master, ou seja, baseado na master. Ele, o que eu tinha: challenge 1, 2, 3.

Só que agora estou na branch challenge 3, estão agora eu posso editar normalmente o meu arquivo do challenge 3, meu arquivo do desafio. Aí que eu vou fazer login aqui a declarar uma variável qualquer, que seja o objeto vazio. Eu vou criar aqui: var o objeto vai recebê-la, o meu objeto vazio.

Então você vai editar assim. Para não dar de cara pra você: você que vai fazer isso sozinho. Isso aqui eu quero ver vocês fazendo esse site.

Beleza, então vou começar a criar o objeto ali só para eu poder te mostrar que tem uma alteração. Fiz alteração aqui, vi 20. Ele vai me mostrar que ele alterou, ele modificou o meu challenge 3 pontos. Eu me dei conta de que tinha lá em três. E agora eu vou dar o seguinte ponto, vai adicionar, certo? Eu vou dar um clique aqui, ele adicionou, ficou gordinho, tá vendo? Ele adicionou. Tive. Ou seja, eu tenho alterações que para serem commitadas.

Agora vou mandar um git commit menos. Vou colocar a mensagem challenge 0 3. Então eu fiz o meu commit. Beleza, feito o meu commit, agora vou fazer um push origin challenge 03. Vou fazer o original, e o meu repositório, está, não é o repositório do curso, é o meu, ou o seu, aí, nesse caso, tá, o seu diálogo e origem. E você, as alterações que você tem que ir pra tua chamada challenge 3. Quando você faz isso, ele vai automaticamente enviá-la para o GitHub. Que você olhar aqui: não tenho que challenge um, tirei do Estado, e agora subi challenge 3. Se atualizar aqui no repositório, vai ver que eu tenho aqui.

Eu sou mineira, mas eu tenho que boa gente challenge três. Eu não tinha nem de três. Agora eu tenho, mostrei as três linhas aqui, está estreando bem certinho aqui. E como tem um monte terá somente a gente querendo ligar, pediu pra fazer o pull request. Por enquanto, o normal é exatamente igual às outras tantas vezes que a gente reconhece, que está exatamente igual. Clique aqui, incompleto, e por enquanto chegou. Se não der, você vem direto, então reconhecido aqui, faz aquela alteração, como mostrei no vídeo anterior, pra você atualizar 20 março, como faz aqui na minha frente.

Mas eu não tenho challenge, challenge três, que você vai fazer. Já nem um pouco de até meia-noite, ela instrui volta pra master, master, mas status, e você vai dar um git push origin. Agora você vai enviar toda a gente mas até lá pro repositório de origem. Ok. Beleza, agora sim, agora pra ter os três atualizados aqui. Ótimo. Então mandei para branch master e mandei pra gente.

## Uma branch por desafio

Tinha gente querendo atualizar challenge dois, o que além de ficar só com o desafio 2. Então, assim, a ideia é que cada desafio seu, no caso aqui na minha, a gente tenha ficado nesse repositório do curso. A ideia é que em cada época a gente que você tem aqui, ela fique com o seu, o seu desafio, e a gente marca, ela fica sempre com os desafios em branco.

A master vai ficar sempre atualizada com o repositório principal. E se eu mudar aqui, por exemplo, challenge três, eu vir aqui na pasta challenge três, eu vou ver que eu tenho me interessava aqui, está. Mas se olhar na master, essa alteração não existe. Ok.

Então, ideia, essa ideia que você tem em cada doente o seu desafio separado. Os desafios vão ficar bem sem parar disso e vão ficar organizados aqui.

## Encerramento

Então esse desafio vai ser bem bacana. Eu espero que você goste bastante, porque ele vai te levar a aprender a utilizar os objetos de uma forma bem legal. A gente vai falar muito sobre objetos. O objeto é uma das partes mais importantes do JavaScript, para não dizer mais. O mais importante é objeto de funções, são, assim, as partes mais importantes. A gente vai falar muito ainda dentro do nosso curso, a gente vai fazer muita coisa com eles ainda.

Então, basicamente, a ideia: você aprende bastante, para aprender bem como funcionam os objetos, aprender bem como funciona as funções. É assim que vai conseguir chegar no nível Ninja de forma rápida, e você vai ter um aprendizado excelente.

Então, assim, era isso que eu queria mostrar. Fizemos aqui o desafio da semana 3. Se você tiver alguma dúvida, já sabe: entre em contato comigo, responde o email do curso que eu mando toda semana com o link do vídeo. Você pode abrir mais cedo o vídeo. Se você tiver uma dúvida, e uma dúvida que talvez possa ser de outras pessoas, é até melhor que você abra uma issue no GitHub também, que pode ajudar outras pessoas também. Outras pessoas estão fazendo curso, talvez podem ter a mesma dúvida. Aí a gente fica respondida ao lado da tela. Se você tiver alguma dúvida, pode abri-la.

E se você não conseguir resolver um exercício todo, porque você tem alguma dúvida, alguma coisa, [a] gente travou, não tem problema. Manda o poder com este exercício pela metade mesmo, ou até onde você conseguiu fazer, e pergunta no próprio reconhece a sua dúvida. Está lá, eu vou te ajudar, responder para que você responda ele certinho.

Ainda não é... ainda não chegamos, né, na hora da prova. Ainda não estamos fazendo os desafios, que é praticamente uma prova onde você vai treinar os seus conhecimentos. Mas se você tiver dúvidas, você tem que tirar a dúvida. Pergunte sempre, que o ninja de verdade lhe perguntou se ele tem tudo. Ele pergunta, e para que as dúvidas sejam sanadas e você aprende de verdade.

Beleza, então finalizamos aqui 3, e até a próxima semana.
