# Order e align-self: mudar a ordem e o alinhamento de um flex-item

Então, pessoal, vamos continuar. Agora a gente vai conversar sobre as duas últimas propriedades dos flex-itens antes de a gente partir para a prática, que é a propriedade order e a propriedade align-self, que a gente vai trabalhar nessa aula de maneira bem simples.

## Order: para que serve

Essa propriedade aqui é muito simples, mas também muito funcional, que literalmente modifica a ordem dos flex-itens. E quando é que eu preciso desse tipo de funcionalidade?

Vamos supor que eu estou no modelo desktop, onde eu tenho uma ilustração e depois o texto. E no modelo desktop, essa ordem é interessante, eu ter a ilustração primeiro aparecendo, por exemplo, na parte esquerda e o texto depois. Talvez, quando eu passar para o mobile e não modificar a ordem, vai continuar dessa mesma forma. Vai aparecer a ilustração primeiro e o texto depois. Só que no mobile, às vezes, como vai aparecer uma ilustração e o texto depois? Às vezes é melhor aparecer primeiro o texto explicando e depois a ilustração vem e ajuda. Em determinados casos, é interessante que você saiba modificar a ordem dos elementos.

## Order: como funciona

Então, literalmente, ele leva no intuitivo. Então, o order zero vem configurado para que, quando está com o order zero, que é o valor padrão, apareça a ordem que está no HTML. Essa é a regra básica. Se no HTML está o item um, dois e três, vai aparecer um, dois e três. A gente vai tratar disso na prática.

E, se você quiser mudar a ordem, você aplica a ordem em número em todos os itens, onde, por exemplo, o azul foi o que eu apliquei primeiro. Então, quando eu apliquei, ele vem aqui primeiro, o verdinho em segundo e o vermelho em terceiro. Então, esse esquema aqui ilustra bem o que eu estou querendo dizer.

Então, eu vou aplicar um order diferente para cada. Vamos supor que eu quero que você apareça em segundo: eu quero que o um apareça em segundo, o dois apareça em primeiro, o três continua aparecendo em terceiro e o quatro continua aparecendo em quarto. Então, só vai inverter o primeiro e o segundo. Quando você quebra, da mesma forma.

Vamos supor que agora eu quero que o quatro vire o primeiro e o dois virem o quarto. O quarto ficou em primeiro, o dois ficou por último e, quando eu quebro, ele segue essa mesma ordem. Basicamente, é bem simples isso, mas é funcional quando a gente está tratando de melhorar a responsividade e o flow das informações, o fluxo de informações.

## Align-self

Por último, a última propriedade é o align-self. O align-self vai trazer as mesmas características de quando a gente está falando sobre flex-item. Inclusive, ele traz justamente os mesmos valores, flex-start, flex-end, center, onde, quando eu aplicava essas propriedades lá no container, ele meio que aplicava a todos os flex-itens. Então, todos seguiam o mesmo padrão. Se você quiser que algum dos itens saia desse padrão, você aplica o align-self.

Vamos ver aqui alguns exemplos para a gente mostrar para vocês. Eu vou primeiro tirar do stretch, então eu vou aplicar no container o flex-start. Vamos ver. Vamos definir aqui um minimum-height, min-height de 50 pixels, para poderem ficarem... O max-height, aliás. Max-height, para poderem ficarem pequenos assim, para podermos ilustrar da melhor forma possível, onde agora a gente vai aplicar, por exemplo, o align-self.

Eu quero que o item 1, por exemplo, fique no centro, então center, e os outros continuem do mesmo jeito. Deixa eu apagar aqui. Por padrão, eles vão ficar no flex-start, então é o primeiro item que vai ficar no center, então eu baixei para o center. Vamos supor que eu quero que ele fique agora na parte de baixo, na parte de cima: flex-start vai subir, flex-end vai descer.

Então, você pode aplicar as mesmíssimas propriedades que a gente viu lá no flex-end, então dá para fazer o stretch, eu quero que só ele complete a coisa toda. O que está ficando? É porque eu coloquei o minimum-height aqui para todos, e eu posso vir aqui e modificar, então, center, e aí você consegue verificar essas diferenças aqui, o baseline.

Então, é literalmente aplicar os estilos de alinhamento que a gente já conhecia, só que para itens específicos. Agora, a gente vai partir para uma parte mais prática, aplicando todos os conceitos que a gente viu aqui para poder fixar.
