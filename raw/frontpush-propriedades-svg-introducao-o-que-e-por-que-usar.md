# Introdução às propriedades SVG: o que é o SVG e por que usar

Opa, fala pessoal, vamos iniciar o módulo de propriedades dos SVGs.

Eu acredito que muita gente estava ansiosa por esse módulo para poder a gente conhecer um pouco mais sobre as ilustrações vetorizadas de que eu tanto falo, de que eu sempre falei que muitas das minhas criações são com base em SVGs e vai completar demais os módulos anteriores, que o módulo anterior a gente discorreu sobre as principais propriedades do CSS para poder a gente manipular os elementos e os SVGs vão completar esse combo para poder a gente começar literalmente a animar.

Então essa aula aqui é introdutória no sentido de eu explicar o que é o SVG antes da gente começar de uma forma um pouco mais conceitual e explicar os motivos de por que usar para você também conscientizar outras pessoas para poder utilizar esse queridinho que ajuda tanto a gente ter desempenho no sentido dele ser mais leve, vocês vão ver isso aí, na prática, além dele ser manipulável, da gente conseguir utilizar as tags, aliás, as propriedades de animação do CSS para poder tornar possível o motion em ilustrações também.

## O que é o SVG

Primeira coisa, o que é o SVG? Ele significa Scalable Vector Graphics, como eu já disse para vocês também, ele é uma imagem vetorial, então são ilustrações, só que tem esse porém aqui, ele é vetorial no formato XML que suporta animações.

Eu vou abrir um SVG para vocês e vou mostrar a estrutura para vocês entenderem como é que se dá isso aqui, então o cabo aqui que eu vou mostrar na prática, mas acredite em mim que ele é literalmente código, é um documento XML, se vocês não sabem o que é XML, basta vir aqui do Google Doc XML, você vai ver que é uma linguagem de marcação, assim como o PHP. Olha só, isso aqui é um XML, está vendo? Então você vai ver que ele também é composto por tags e olha só, basicamente é só código, por isso que torna ele tão vantajoso, porque ele é mais leve que uma imagem normal, ele não é um PNG, um JPG, ele é uma imagem vetorial que traz uma qualidade muito superior justamente por ser vetor, porque ele é formado por coordenadas, por esses vetores.

E pelo fato dele ser adimensional, a dimensão é simplesmente a que eu dou para ele, então facilmente eu consigo aplicar um SVG em telas maiores ou em telas menores e olha só, mais leve, está certo? E a gente está utilizando código no processo e vocês vão ver quando eu abrir um SVG e começar a explicar todos esses conceitos para vocês.

## Um espelho do Figma

Então a gente vê aquelas primeiras perguntas, por que a gente usa, o que dá para fazer com o SVG e sempre pense da pessoal como um espelho do Figma, por que eu estou falando isso? Por isso que o Motion e o UI Design se encaixam tão bem e vocês também vão perceber isso ao longo das próximas aulas, onde eu vou estar sempre demonstrando, mas olha só, eu vou mostrar aqui nessas aulas bônus como a gente faz esses elementos, elementos de sombra, por exemplo, esses ícones aqui e literalmente tudo que eu faço aqui no Figma é meio que um espelho do que se pode ser feito com um SVG, porque se eu clicar aqui nesse frame e vir aqui no modo de export, eu vou ver que tem opções, o PNG, o JPG, o SVG e o PDF, são as quatro principais formas da gente exportar qualquer tipo de imagem.

Ou são as quatro principais que rondam na web, com certeza são essas aqui, principalmente PNG, JPG e SVG e quando você aperta aqui em exportar para SVG e a gente dá o export, deixa eu salvar aqui na minha área de trabalho mesmo, você vai ver que é o mesmo elemento, ele não muda em nada, é um espelho de fato.

Olha só, isso aqui é um arquivo SVG que é exatamente isso aqui que eu criei no Figma, então vocês vão perceber que tem, por exemplo, propriedades que tem no Figma e não necessariamente tem no CSS, como por exemplo, uma manipulação melhor de bordas ou então criação de elementos em perspectiva feita de forma mais fácil, colocar as bordas, colocar os efeitos, então literalmente tudo que eu coloco aqui com relação a efeito, layer blur, background blur, inner shadow, todas as propriedades e efeitos que a gente consegue colocar aqui, a gente também consegue fazer no SVG, por isso que você saber o Figma e fazer o estudo do SVG é um encaixe tão perfeito.

Então quando eu fiz o export aqui, eu tenho um arquivo, ele é um arquivo SVG, deixa eu ver se ele está responsivo, ele não está responsivo porque ele exporta com algumas características que vocês vão ver, mas tem como deixar ele responsivo também, ou seja, fluido para poder pegar o tamanho de um div pai e torná-lo parte integrante da nossa interface e inclusive, todo o meu site é feito com SVGs, até pouco tempo atrás, eu falo pouco tempo atrás, uns dois anos ou até um ano, eu ainda utilizava imagens, mas quando eu comecei a estudar e buscar mais conhecimento sobre SVG, eu vejo que só tem vantagens para poder até deixar o meu site mais performático e pelo fato dele ter elementos separados, a gente vai entender a estrutura dele, vocês vão ver isso na prática, vai dar para ver que dá para manipular cada um dos elementos, então por que eu uso?

## Densidade de pixels

Densidade de pixels, como eu já disse para vocês, ele é dimensional, basta eu esticar ele que ele não vai pixelar que nenhuma imagem, por exemplo, deixa eu dar um exemplo aqui no meu próprio website, onde a única parte que tem imagem é essa aqui, está vendo? Ela é uma imagem, se eu vir aqui, começar a dar zoom, aquele exemplo básico, olha só como ele vai começar a pixelar, está vendo? Ele vai começar a perder qualidade, viu aí?

Agora, se eu pegar esse mesmo exemplo aqui, que eu acabei de abrir e começar a dar zoom, vocês vão perceber, pessoal, não interessa o zoom que eu der, ele vai continuar em uma definição perfeita, então olha só como o uso do SVG melhora a performance do browser, otimiza, principalmente hoje que a gente está precisando de tecnologias que facilitem a gente construir interfaces que sejam responsivas e o uso da imagem nunca vai sumir, então é muito interessante, é muito vantajoso a gente ter esse tipo de recurso para poder a gente construir nossas interfaces e não ficar se preocupando em, por exemplo, ficar exportando vários tamanhos de imagens para poder ajustar um ao mobile, o outro ao desktop e o outro ao tablet, porque para poder conseguir performance nessa questão, eu tenho que exportar vários tamanhos, por isso que nessa opção aqui, quando você seleciona PNG, tem essa variação aqui de um X onde eu posso exportar ela menor do tamanho original ou então duas vezes o tamanho original, um e meio vezes o tamanho original e etc.

Então pensando nisso também, tem elementos que, por exemplo, a imagem, o JPG e o PNG, eles não vão desaparecer e para poder tornar o mais performático possível, eu tenho que carregar imagens menores em mobile e imagens maiores em desktop para poder se adequar à tela e é uma preocupação que eu não preciso ter quando eu trabalho com SVGs.

## Integração com a ferramenta de prototipagem

Integração total com a ferramenta de prototipagem, você percebe que muito se explica com o espelho do Figma, o SVG, vocês vão perceber isso com o decorrer das aulas de tudo, vocês vão entender isso aqui na prática, a gente vai conseguir manipular com tudo que foi feito lá de CSS, que eu falei lá no módulo anterior, nós vamos conseguir fazer com cada elemento específico, você percebe?

Se eu der um Ctrl-Shift-G aqui nesse ícone, percebe que tem um balãozinho, ele é um vetor, ele é um elemento, ele é um elemento separado, ao passo que esse background aqui é um outro elemento e esse cara aqui atrás é a união de vários outros elementos, está vendo? E aí, quando eu exporto ele para SVG, eles vão de maneira separada para o código e se eles vão de maneira separada, eu consigo manipular eles de forma individual com o CSS.

Então, suas vantagens até agora, dá para aplicar efeitos e filtros, aquele efeito de Liquid Motion, a gente se dá aplicando alguns efeitos do SVG, então ele é performático e possui árvore no DOM, o que é isso? Eu posso manipular ele com JavaScript também, então olha só o tanto de vantagens que se tem a utilizar SVGs.

## Propriedades específicas

Tem propriedades específicas que a gente vai estudar ao longo do curso, por exemplo, a propriedade de stroke dos elementos, tem muitas propriedades aqui para poder ele deixar redondinho nas pontas, deixa eu fazer aqui uma retinha só para vocês entenderem, se eu vir aqui e colocar a propriedade de stroke, deixa eu aumentar aqui, está vendo que ele é quadradinho, tem as propriedades para poder deixar ele redondo nas pontas, então é da dash array, que é colocar, por exemplo, 5 e 10, deixa eu colocar 20 e 10, vou aumentar esse valor aqui, porque como ele está round, você não enxerga direito, mas 40, 70, então olha só o tanto de propriedade que a gente vai conseguir manipular com o SVG, que é com bordas, que dá mais liberdade que as próprias propriedades do CSS.

Então tem propriedades do CSS que eles compartilham, tem propriedades que são só do SVG e a gente também vai tentar estudar a maioria delas, a grande maioria delas para conseguir efeitos legais, o SVG também é chamado meio que o Photoshop da web.

## Desvantagens e próxima aula

Então até agora, pessoal, eu não disse nenhuma desvantagem, porque o SVG tem algumas poucas, mas existem também, porque ele precisa estar no estilo inline para poder ter todas essas vantagens, mas isso é coisa da próxima aula, onde eu vou falar para vocês como é que a gente utiliza, como é que a gente insere o SVG nas nossas páginas HTML, beleza? Então até a próxima.
