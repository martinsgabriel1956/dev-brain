# Flex-basis: o tamanho base dos flex-itens (auto, 0 e valor fixo)

Então, pessoal, agora a gente vai conversar um pouco sobre flex-basis. Eu vou tentar explicar de maneira mais dinâmica e mais didática possível, mas, praticamente, o flex-basis, como o próprio nome já anuncia, ele quer definir uma unidade na base dos flex-itens, quer padronizar o tamanho do flex-item. E eu vou explicar para vocês como é que se dá isso para poder não confundir com o flex-grow que a gente acabou de estudar.

## De onde a gente parou: os flex-grows

Vamos tomar aqui como exemplo de onde a gente parou da última vez. A gente definiu o item 11 e o item 12 com flex-grows diferentes, onde esse aqui cresce o dobro desse que, por sua volta, cresce que nem o dobro dos outros. Então, todos estão crescendo iguais, menos o 11 e menos o 12. Então, quando quebra, o 12 sempre vai ocupar o dobro desse e, por conseguinte, o 11 sempre vai ser o dobro do 10 e dos outros, quando tiver essa quebra, onde ele sempre vai aproveitar o espaço que está disponível, porque, por padrão, ele vem com o stretch. Então, vamos lá.

## Flex-basis auto: o padrão

O que a gente pode identificar aqui é que o flex-basis, o valor padrão dele é auto. O que significa isso? O flex-basis automático meio que não está nem para o tamanho dos flex-itens. Então, como eu não defini tamanho fixo nos itens, se eu não definir tamanho fixo, ele vai ajustar de acordo com o conteúdo.

E você percebe que o conteúdo tem o mesmo tamanho. O item 2, item 3 e item 4 têm exatamente o mesmo tamanho, que é a palavra item e o algarismo. Se eu vir aqui, por exemplo, no item 1 e encher de número, se eu vir aqui no 5 e encher de número, eu tenho conteúdos diferentes. Como eu não estabeleci nenhum tamanho específico para o item, ele vai simplesmente se ajustar ao tamanho do conteúdo.

Por quê? Porque o meu tá flex-basis auto. O que quer dizer isso? Ele vai crescer sem se importar com o tamanho, a padronização ou a uniformidade dos flex-itens. Você percebe que esse está com um conteúdo maior, ele vai ficar maior. Esse está com um conteúdo menor, ele vai ficar menor.

## Não confundir com o flex-grow

Mas, Násser, como é o flex-grow? Lembra que o flex-grow não é diretamente ligado ao conteúdo. Ele é mais ligado ao padding. Você percebe que antes de fazer essa modificação, deixa eu voltar aqui, 1 e 5. Antes de fazer essa modificação, olha só o espaço do conteúdo para a nossa caixinha. Você está vendo que está a mínimo, tem praticamente nada nele. Quando eu vim aqui e aumentei o conteúdo, olha só, continuou do mesmo jeito. Então, os grows estão certinhos, não tem nada mudando aqui.

O 10, olha aqui o espaçamento. Está maior, porque quebrou. Deixa eu quebrar mais um item. Olha só o 9. O 9 e o 10 têm a quantidade de grow diferente. Como ele teve espaço para expandir, ele foi lá e expandiu. Mas, olha só, eles estão do mesmo tamanho. Não mudou. Deixa eu vir aqui no 9 e aumentar o conteúdo dele. Olha só, o grow do 9 e do 10 está exatamente o mesmo. Ele aumentou porque o conteúdo aumentou junto. E pelo fato do flex-basis estar no automático, ele não interessa para isso. Ele não tenta padronizar o tamanho dos flex-itens. Então, esse aqui é o primeiro valor e é o valor padrão.

## Flex-basis 0

Se eu mudo para flex-basis 0, agora ele vai começar a se importar. Ele meio que vai fazer conta matemática para poder deixar o mais próximo possível. Ou seja, ele vai fazer contas de acordo com o conteúdo que tem nesses itens. Vai tentar quebrar ao máximo, de forma a manter todos os flex-itens com o flex-basis 0 o mais próximo um dos outros.

Então, se eu vir aqui em salvar, ele quebrou esse texto aqui para poder deixá-lo o mais curto possível. Como esse aqui é um string inteiro, ele não conseguiu quebrar de novo. Mas se eu vir esse aqui e desse um espaço, ele ia quebrar de novo. O que ele está tentando é deixar todos os flex-itens o mais próximo, o mais uniforme possível um dos outros.

Então, ele meio que vai pegar um valor e vai fazer suas próprias contas matemáticas e tentar quebrar cada um deles, se é possível que quebre, de forma que agora eles tenham mais ou menos o mesmo tamanho. Por mais que esse aqui tenha um conteúdo muito maior em relação ao item 2, a discrepância entre eles diminuiu. Não estou mudando nenhuma propriedade de flex-grow, ela está exatamente a mesma.

## Flex-basis com valor fixo

E uma coisa legal de a gente observar também é que outra propriedade do flex-basis é quando eu deixo um valor fixo. Vamos supor que eu venho aqui e deixo 100 pixels. O que eu estou dizendo para ele? A base dos meus flex-itens é de 100 pixels, ou seja, é o mínimo que você pode ir. Eu quero que você se esforce para deixar todos os meus flex-itens com um mínimo de 100 pixels.

Então, quando eu venho aqui e salvo, está vendo que ele vai quebrar bem mais. E você percebe que agora o tamanho deles está importando já com relação ao flex-basis, porque eu falei para ele: o mínimo de largura dos meus flex-itens eu quero de 100. Se eu aumentar isso aqui, por exemplo, para 200, todo mundo vai aumentar igual, porque eu quero uma base de 200. E a gente começa a entender bem mais como a gente consegue controlar o tamanho dos cards e como eles conseguem variar em vários tamanhos de tela.

## Flex-basis e flex-grow juntos

Então, olha só o tanto que ele é inteligente: ele vai deixar com um mínimo de 200. Não quer dizer que aqui tem 200, ele dividiu de forma que os flex-itens como um todo respeitem o flex-grow. Então dá para perceber que o 12 é maior que o 11, que porventura é maior que o 10, que é o grow 1, que é aplicado para todo o resto. A gente percebe essa diferença aqui, então ele continua respeitando o grow, só que ele respeita meio que ponderando agora as duas propriedades, porque o que eu disse? A base tem que ser no mínimo de 200 pixels.

Então, quando eu estiver diminuindo, ele vai tentar ajustar, tentar, tentar e manter todas as particularidades que eu disse. Pode perceber que mesmo ele na iminência de trocar, o 12 ainda está maior, ele não está totalmente alinhado, assim como o 11 também não está totalmente alinhado, e a diferença do 10 para o 11 é proporcional, assim como do 11 para o 12 é proporcional, por mais que a diferença aqui seja mínima, mínima, mínima. Vamos supor que aqui tem 4 pixels, aqui tem 2 pixels e aqui tem 1 ou 0 pixels.

Então, você está vendo que ele está muito próximo e tentando respeitar tudo que a gente estabeleceu para ele, mas vai chegar um momento que ele não vai mais conseguir manter a base de 200, aí vai quebrar, e ele vai manter isso até o 200 de novo, até quebrar novamente. Então, se eu vir aqui em inspecionar, vou aumentar essa parte aqui, olha só, então ele está aqui, ele vai tentar, tentar, tentar. Lembre-se que a base minha é de 200 pixels: quando alcançar o 200 e ele não conseguir respeitar mais, ele vai quebrar novamente.

Então, é assim que funciona o flex-basis com relação ao flex-grow. Então, é um conceito um pouco mais complexo, digamos assim, que eu aconselho fortemente a vocês treinarem, para vocês estudarem mais sobre isso, buscarem mais referências tanto na W3C como em maiores exemplos, e para poder tirar essas dúvidas e mais outras que podem surgir na nossa cabeça. A gente vai fazer sempre mais exemplos para a gente estar aprendendo mais sobre essa propriedade, mas eu espero que eu tenha sido o mais claro possível na explicação dela.
