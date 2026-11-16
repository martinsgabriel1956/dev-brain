# Representação da cor em códigos: HSB, hexadecimal e RGB

Então, pessoal, conforme a gente tinha conversado, agora a gente vai partir para a parte mais prática, que é a representação da cor em códigos, para a gente entender um pouco de como ela é composta, de como ela é escrita em hexadecimal, que é muito importante a gente saber RGB e hexadecimal quando a gente for estudar também programação para o desenvolvedor.

Depois a gente vê a diferença de RGB para CMYK, então sem mais delongas, vamos começar.

## HSB

Deixa eu fazer um frame bem simples aqui para poder a gente tratar disso e a primeira coisa é que quando eu desenho determinada forma, sempre você vai vir no fill em preenchimento e ele vai te abrir essa caixinha de diálogo aqui.

Essa caixinha é muito comum em toda e qualquer ferramenta de prototipagem, então não precisa ficar preocupado, esse aqui só tem no Figma, geralmente todos têm e é exatamente a mesma coisa.

A primeira coisa é a gente entender como é composta a cor e acredito que o modo mais fácil de explicar de antemão é no modo HSB. Tem outros modos, a gente vai passear por eles, mas vamos começar pelo HSB, onde o H significa hue, matiz, o S saturação e o B de brightness, brilho.

O hue é a matiz que varia de 0 até 359 e vocês vão entender o que é de 0 a 359, que tem aquela ideia do círculo cromático, 360 graus, é mais ou menos isso, a saturação que vai de 0 a 100 e o brilho vai de 0 a 100.

Então, nesse quadradinho aqui, a gente percebe que o hue varia aqui. Se eu vir aqui e mudar para o modo HSB, você vai ver que ele está aqui, 360 e 0, onde ele vai e volta no mesmo ponto, ou seja, isso aqui é um círculo, onde eu passeio por todo o espectro visível que a gente acabou de conversar na aula passada.

Se eu pegar esse meu cursor e fizer variações da esquerda para a direita, percebe que esse número 72, 73 não está variando quando eu faço variações da esquerda para a direita, ou seja, está mudando a saturação. E quando eu tenho uma cor mais saturada, você percebe que a saturação está medindo a presença daquela cor. Quando eu saturo ela ao máximo, ela fica como se fosse mais pura e quando eu saturo ao mínimo, ela vai tender a escala de cinza. Então saturação é o quê? A presença de determinada cor no objeto.

Enquanto o brilho, eu vario de cima para baixo, está vendo? Então, quando eu baixo o brilho no 0, eu tenho o preto puro. Quando eu vou no brilho ao máximo, eu tenho a cor um pouquinho mais estourada, com o brilho no máximo. E quando eu subo os dois, eu vou ter aquela cor pura, que eu sempre indico não utilizar, porque esse tipo de cor aqui a gente não acha na natureza.

Então, a cor é composta desses três componentes, se é que podemos dizer assim, que vai auxiliar a gente quando estiver compondo a paleta de cores ou variação de cores.

## Hexadecimal

Com relação a como a gente constrói ela em hexadecimal e em RGB, vamos lá, porque esse modo HSB é mais utilizado para a gente compor as cores com a paleta de cores e tudo, mas quando passa para o ambiente de desenvolvimento, na maioria das vezes vai encontrar o hexadecimal e o modo RGB, que também é o modo CSS, só que com opacidade, que a gente vai chegar lá, mas continua sendo RGB.

Então, quando eu falo de hexadecimal, olha só, qual é essa cor? É 8FF00. Então deixa eu escrever aqui essa cor, então é 8F, vamos aumentar aqui, e a gente vai entender por que ela é composta dessa forma. Então venho aqui, Ctrl+C, Ctrl+V. Então o que essa forma diz para a gente?

Primeiro, que sempre é acompanhado de um hashtag, onde eu posso decompor em RRGGBB, os dois próximos é a cor verde e os dois próximos é a cor azul. E aqui, coincidentemente, o azul está zerado, está 00, o verde está no máximo, ou seja, está FF, e o vermelho também tem um pouco de vermelho, tem caráter 8. Mas eu não estou entendendo nada disso, o que significa ser hexadecimal?

Significa que hexa vem de 6, o Brasil vai ser hexa, então ele remete ao número 6, decimal ao número 10, então eu tenho que ter, nesse sistema, 16 algarismos, se é que eu posso dizer assim, para poder compor o meu sistema. E quais são os meus 16 algarismos?

Vamos lá, 1, 2, 3, 4, 5, 6, 7, 8, 9, e aí eu não posso colocar o 10, porque o 10 é um algarismo diferente, ele não é esse bem um algarismo, ele é o conjunto de dois algarismos, que é o 1 e o 0. Então o que eles fizeram? "Ah, vamos colocar a letra", então A, B, C, D, E, F, ou seja, o A representa 10, o B 11, o C 12, D 13, 14, 15. "Ah, mas tem que dar 16", é porque tem o 0 aqui atrás.

Então esse aqui é o sistema hexadecimal, porque ele tem 16 algarismos para poder representar ele, por isso que é da letra A até a letra F, e do algarismo do 0 até o 9, e aí eu componho as cores nesse sentido. O que quer dizer?

Quer dizer que essa cor verde tem um pouquinho de vermelho, mas o quanto de vermelho, sabendo que todas as cores vão de 0 até 255, então eu posso colocar de 0 até 255 de vermelho, 0 até 255 de verde e 0 até 255 de azul.

E aí vamos começar a compor essa cor aqui. Vamos supor, eu tenho 8 e F compondo o vermelho, então eu tenho 8 na primeira posição, lembrando que eu tenho duas posições, então deixa eu colocar aqui posição 1, aqui embaixo posição 2. Então no vermelho eu tenho o 8 ocupando a primeira posição e o F ocupando a segunda posição. O que isso significa para mim, qual é a conta que eu tenho que fazer?

Se a minha base é hexadecimal, o sistema é o quê? Na base 16. Como ele está na primeira posição, eu tenho que multiplicar por 16 elevado à primeira posição, e esse aqui é chamado a posição 0, então o outro elevado à posição 0. Então esse aqui posição 1, esse aqui posição 0, porque você faz da direita para a esquerda, então na verdade o F está na posição 0. Sempre desmembra em posição 0, posição 1, posição 0, posição 1, posição 0, posição 1.

E aí eu faço F, que o quê? Significa 16 no nosso sistema, vezes o quê? 16 elevado a 0. Quanto que é 16 elevado à primeira? É o próprio número 16. Então como é que eu faço essa conta? 8 vezes 16. Então vamos lá, 8 vezes 16, o que vai dar quanto?

Deixa eu abrir aqui a calculadora, vamos lá, 8 vezes 16 vai dar 128. Então 128 na primeira posição do vermelho, enquanto aqui eu tenho o F, que é o quê? 16 vezes 16 elevado a 0, que é 1, que é igual a 16. Ou seja, o número que está compondo a minha componente vermelha, que é o red, está sendo o quê? 128 mais 16.

Então é essa conta e vocês não vão precisar fazer ela, mas eu preciso explicar uma vez para vocês entenderem. E aí a gente volta lá, 128 mais 16 dá 144, ou seja, o valor de vermelho nessa cor aqui é 144.

## RGB e o modo CSS

Enquanto a cor verde, eu nem preciso fazer a conta, porque percebe que é FF, ou seja, é máximo, então no G é 255. E no Blue eu também não preciso fazer conta, porque aqui ele está zerado, tanto na primeira posição como na última. Então o número que corresponde essa cor em RGB é 144, 255 e 0.

Se a gente vier aqui e simplesmente mudar para RGB, olha só, 143, 255 e 0, que é justamente essa conta que se faz. Então a gente representa as cores dessa forma. Na maioria das vezes vocês vão ver ou o modo RGB ou o modo hexadecimal quando a gente estiver programando, então são esses os principais, HSB na hora de compor.

E também é muito utilizado o modo CSS, que é o modo RGB normal, normalíssimo, só que o A indica o caráter alfa, que é o quanto transparente é essa cor, que você também consegue aplicar.

Então essa é a aula um pouquinho mais prática para poder a gente entender como é composta a cor com relação aos códigos. Tudo bem?
