# Style Guide na prática (parte 2): o que documentar para o desenvolvedor

Então, pessoal, na parte dois da prática aqui do guia de estilo, a gente está meio que aprendendo a configurar alguns padrões para poder a gente ter consistência tanto no Figma, tanto na documentação, que esse é o objetivo do style guide, onde na última aula a gente viu como é que a gente adiciona, por exemplo, estilos de texto, de cor e de efeito. São esses três os principais e tem como você aplicar de N formas e com o decorrer dos projetos a gente vai voltar nesse tópico novamente.

Mas o que eu queria destacar aqui nessa aula de forma bem rápida é com relação à documentação, pessoal. O que acontece? Vamos analisar, eu como desenvolvedor, vamos analisar aqui, por exemplo, os cards com relação aos efeitos que a gente acabou de aplicar. Desculpa ele ter travado, mas com os efeitos que a gente acabou de criar aqui. Então, vamos supor que eu estou criando esse card e eu preciso passar quais são essas informações desse card para o desenvolvedor, quais são as informações que realmente são importantes.

Por exemplo, o linear-gradient, qual é a orientação, qual é a inclinação, quantas camadas de box-shadow têm, como é que se cria esse efeito. Então, aqueles que são mais relacionados a design mesmo, que é um refino das cores ou então de sombras, são sempre muito importantes de você colocar na descrição. Sempre, sempre, sempre.

## Posicionamento e dimensões

Com relação a elementos de posicionamento, nem tanto, porque o posicionamento do Figma automático aqui, eu acho que não condiz muito com a realidade, não é assim que a gente aplica quando a gente está codando. Vamos supor, se eu vir aqui e clicar em inspect, ele vai dizer para mim o width e o height, beleza. Se eu der algum tipo de arquivo para ele, eu consigo estabelecer esse tipo de tamanho para ele, não tem problema nenhum.

Com relação ao botão, esse tipo de dimensão é importante, então faço questão de deixar claro qual o tamanho que eu quero e muitas vezes eu posso até estabelecer o padding. Não necessariamente eu preciso estabelecer o tamanho fixo total, porque depende do conteúdo do texto, se o conteúdo aqui estiver maior, pode ser maior, mas eu posso muito bem vir aqui em design e estabelecer, por exemplo, eu quero um padding de 16 pixels sempre, então vou de 32, precisa muito pouco. Vamos colocar aqui, 36.

Vamos colocar esse padding aqui como padrão dos botões, a proposta está muito errada, então o botão deveria ser aqui, botão e você coloca 16 de um lado e 16 do outro, 36 aliás, eu quero aumentar um pouquinho, eu quero 40, eu quero 48, tem aqui, 48, faz o alinhamento ali, faz o alinhamento, beleza, o picola até o final.

Indicando para ele que você quer um text-button, um padding aqui de um lado e de outro de 48 pixels e aí você consegue estabelecer isso, mas eu vou deixar conforme estava antes, também estou editando o arquivo, podendo bagunçar ele todo e eu passar para vocês com mais consistência depois, mas com relação a cards, esse tamanho também você pode especificar, traçando uma setinha de um lado e uma setinha do outro, uma linha guia para poder estabelecer esse tamanho.

## Border-radius e cor

Com relação ao border-radius, super importante, porque o border-radius varia de acordo com o tamanho do card, porque se eu manter, por exemplo, um border-radius fixo, olha só, se eu manter um border-radius fixo para um card pequeno, olha só o que ele vira, se eu manter um border-radius fixo para um card muito grande, meio que ele não faz sentido porque perde a identidade dele ter esse arredondadinho aqui, está vendo?

Então, o border-radius precisa ser relativo, conforme o tamanho do card, então é sempre bom você estabelecer quais os tamanhos do card que você está colocando e, juntamente, com o tamanho do border-radius, então aqui é o 38 pixels, a cor é muito simples de você aplicar, é a principal que estou colocando aqui, que a proposta eu ainda não coloquei, ainda estou editando, mas eu irei colocar a cor tanto em CSS, que é o RGBA, muito comum de utilizar, tanto como hexadecimal, esses dois são os mais utilizados.

## Box-shadow

Isso é muito importante, porque isso para o desenvolvedor é muito complicado dizer quais são as sombras do CSS, então não deixe de vir aqui e copiar sempre esse box-shadow, ele já criou o box-shadow com o RGBA certinho, com as opacidades, está vendo? Já muito bem colocadas com a cor correta e com as camadas corretas, porque lembra desse estilo que a gente acabou de aplicar aqui, ele tem mais de uma camada, ele tem quatro camadas de drop-shadow para poder dar esse efeito.

E é muito difícil de você não passar esse tipo de informação, então basta você vir em inspect, copia e cola, Ctrl-C, Ctrl-V, e você vir no box-shadow, copia aqui dentro, você documentou e sempre deixa ele um pouco mais brando assim, para poder dar essa hierarquia. Para poder ficar bem leve, onde ele simplesmente quer aplicar o box-shadow desse modo aqui, no modo normal, você vir aqui, box-shadow, ele só vir aqui, copia e cola, ou seja, no PDF que você esteja exportando, então com relação ao estilo em si, o Figma acerta muito.

## Gradiente

Então, em um gradiente desse, tem como eu aplicar esse gradiente de forma nativa no CSS3, utilizando essa propriedade aqui, o background-linear-gradient, só que tem a inclinação, que está em 220 deg, e onde começa ou termina determinada cor, você percebe que aqui, 14,43% é onde começa essa cor e 85% é onde começa essa cor, então tem os limites do background-linear, desse comando aqui, então é muito importante você copiar esse background-linear, ou então mostrar como ele busca esse tipo de informação no arquivo que você está passando, e se ele tiver informação ou conhecimento no Figma, ele consegue tirar essas informações do próprio documento.

## Position, flexbox e grid

O que não dá para levar muito em consideração é o position, porque a gente não utiliza isso aqui quando a gente está codando, é muito difícil a gente utilizar o position para poder layoutar, não estou falando que é impossível, mas tendo o flexbox e o grid, é muito difícil de utilizar essas informações aqui, então elas quase sempre são totalmente descartadas quando a gente fala de layout. Quando a gente fala de design, de sombra, de cores, de linear, esses são sempre aspectos muito importantes da gente deixar documentado nesse sentido aqui.

## Estados: normal, hover e clicável

Então quando você for criar os módulos, cria o modo normal, cria o modo hover, quando você passa o mouse e cria o modo clicável, que quando você clica é o que ele fica, então eu sempre costumo criar esses três módulos no card, da mesma forma para os ícones, da mesma forma que eu penso aqui para os inputs, eu tenho que deixar o modo quando ele está inativo, quando eu passo o mouse em cima, quando eu deixo e clico, eu tenho que deixar muito bem claro quais são esses estados, quais são as características de design que mudam de um para o outro, qual é esse verde, esse verde eu já deixei especificado aqui.

Então você percebe que é um mapa de design, é o mapa que traduz o design para o CSS da melhor forma possível, então esses detalhes é importante sempre estar destacado, acredito que é isso, efeito de sombra é, acredito que é isso e eu vou enfatizar isso nos projetos quando a gente estiver desenvolvendo, de verdade, principalmente do Nubank que vai servir de case para poder a gente demonstrar tudo isso, beleza galera? Até a próxima.
