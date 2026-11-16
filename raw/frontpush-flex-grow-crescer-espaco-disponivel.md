# Flex-grow: quanto cada flex-item cresce no espaço disponível

Então, pessoal, agora nós vamos progredir na parte do Flexbox. Até agora, a gente entendeu como é que funcionam todas as propriedades sobre flex-container. Mais uma vez, reiterando, na metade do nosso estudo dos fundamentos do Flexbox: a gente vai passar por todas as propriedades e depois vai ter alguns projetinhos práticos para poder a gente aplicar tudo que a gente está vendo aqui, certo?

Então, lembre que são dois pilares: tem as propriedades do flex-container, que a gente já encerrou. Agora, a gente vai começar sobre a propriedade dos flex-items, ou seja, ao invés de aplicar as propriedades no flex-container, eu vou aplicar no flex-items e ver como é que eu posso conseguir diversas configurações.

## O que é o flex-grow

O flex-grow, pelo próprio inglês, a gente vê que grow vem de crescimento, então ele define a habilidade de um flex-item crescer. Quanto ele vai crescer com relação ao outro? O número padrão que vem aqui no flex-grow é zero. E aí, quanto maior o número, maior em proporção ele vai crescer, e aí a gente vai entender, com base em exemplos, como é que ele cresce.

## Preparando a demo

Então, vamos lá mais uma vez, vamos aqui para o nosso esqueminha. Vou deixar flex-start, está certo? Vou deixar flex-start, para ele ficar colado aqui, mas o que acontece? Eu vou tirar esse padding, só para poder enfatizar para vocês como se dá o processo. Então, vou vir aqui, vou comentar, eu tirei o padding, vou colocar ele no modo row, normal, beleza, está aí.

Percebe que agora, como ele não tem um padding, ele está com o como stretch, ele vem em padrão stretch, que é completando todo o espaço vazio. Vamos supor que eu venha aqui e aumente o height para 700. Opa, o Num Lock estava desligado, foi mal, galera. Olha só, ele vai lá, completa, ele está no modo stretch, padrão, poder completar ao máximo.

## Flex-grow igual para todos

A primeira coisa que eu tenho que aplicar agora é o flex-grow. E eu vou aplicar para todos. Você sabe que o flex-grow, por padrão, vem em 0. Então, se eu vir aqui e aplicar 0, não vai mudar absolutamente nada. Se eu aplicar flex-grow 1, vamos ver o que acontece. Olha só, não vai mudar também nada. Flex-grow 2, nada. Flex-grow 3, nada. Flex-grow 10, nada.

Aí você pergunta assim: por quê? O que está acontecendo? Não estou entendendo nada. Ah, porque não tinha quebrado. Então, quando quebra, o que acontece? O que a gente consegue perceber aqui? Que o que realmente aumenta no flex-grow é a distância do conteúdo para a borda, de forma que preencha o container como um todo.

Então, como todos os flex-items têm justamente o mesmo tamanho como o flex-grow, eles vão crescer de forma justamente igual. Então, eu colocar um flex-grow 50, não vai mudar nada. Está todo mundo crescendo exatamente igual. Então, se eu colocar 1, 2, qualquer coisa aqui, não vai mudar nada. A grande sacada do flex-grow é quando eu tenho flex-grows diferentes. Como eu estou aplicando 1 para todos os itens, você não vai ver diferença nenhuma.

## Flex-grows diferentes

Então, vamos deixar só esses quatro aqui, para a gente verificar. Vou ter que deixar 8, volta. Vamos deixar 8 para a gente ver essa diferença. Está aqui, 8 flex-items, onde eu vou lá e quero quebrar. Por que ele não está quebrando? Porque eu tenho uma outra propriedade chamada flex-basis, que eu vou ter que explicar depois, que facilitaria a gente a saber dela agora. Então vou deixar com 12 mesmo para poder quebrar.

Vamos supor que todo está com flex-grow 1 e eu quero no 12 vir aqui e aplicar um style de flex-grow 4. Vamos ver como funciona. Agora sim, só no item 12, ele está crescendo mais que os outros.

Então, olha o que acontece: o espaço dentre esses está igualzinho, enquanto o 12 está 4 vezes maior. Se esse está crescendo com proporção de 1, os outros estão todos crescendo com proporção de 1. O do 12 está crescendo com proporção de 4, então é assim que a gente percebe a diferença do flex-grow.

Se eu colocar, por exemplo, no 11 o flex-grow 2, você percebe que ele aumentou. Ele sempre vai aumentar conforme o espaço que ele tem disponível. Quando ele está aqui, como não quebrou, não tem nada que aumentar. O grow não é necessariamente aumentar, é aumentar quando está disponível. Quando quebra que ele fica disponível.

O 12 tem maior prioridade que o 11, que porventura tem maior que o 10, que o 10 já é o flex-grow 1 normal. Você percebe que esse é o dobro desse, que é o dobro desse: 1, 2, 4. É assim que funciona o sistema flex-grow.
