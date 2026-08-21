# Seedwork

> Tradução para português do bliki **"Seedwork"**, de Martin Fowler.
> Fonte: https://martinfowler.com/bliki/Seedwork.html
> Autor: Martin Fowler | Publicado em: 11 de setembro de 2003
> Tags originais: evolutionary design
> Tradução feita para fins de estudo.

---

Nos primeiros dias da Orientação a Objetos, os defensores do paradigma — eu incluído — dedicavam muita atenção a argumentar em favor do reuso. No início falávamos sobre reuso de classes individuais. Depois descobrimos que reusar classes isoladas, embora funcionasse em alguns casos, não funcionava tão bem em outros. Então passamos a investir em frameworks reutilizáveis, que nos davam aplicações parcialmente construídas com determinada funcionalidade.

No lado técnico, esse tipo de reuso foi um sucesso — basta olhar para as grandes bibliotecas disponíveis em ambientes como Java e .NET (e não apenas em OO, como demonstra o CPAN). Mas, particularmente no lado de negócio, esse reuso não apareceu com a mesma rapidez. E mesmo no lado técnico, muita gente sente que os frameworks com os quais lida são complexos demais para o seu propósito, e essa complexidade acaba dificultando que essas ferramentas sejam realmente úteis.

Um [weblog recente](http://www.artima.com/weblogs/viewpost.jsp?thread=8826) de Michael Feathers explorou essa questão, e a [discussão resultante](http://www.artima.com/forums/flat.jsp?forum=106&thread=8826) trouxe à tona uma noção alternativa: o **seedwork**. Um framework deveria ser uma aplicação parcialmente pronta que você estende de formas controladas para obter o que precisa. Um seedwork é uma funcionalidade mínima que você modifica como quiser para chegar ao que precisa. Isso significa, claro, que não há como receber atualizações comuns do seedwork — uma vez que você o expande, ele passa a ser seu. É o tipo de reuso por copiar-e-colar que muita gente, inclusive eu, costuma menosprezar.

Talvez eu não devesse ser tão desdenhoso assim. Frameworks e bibliotecas funcionam muito bem quando estão bem maduros ("bem temperados"). Mas conseguir um bom framework é muito difícil. Seedworks não são tão úteis quanto um bom framework, mas são mais fáceis de criar e de usar. A questão não é se eles são ideais, mas simplesmente se são úteis.

E mesmo o reuso maduro costuma ser um problema. Ainda não descobrimos de fato como lidar com bibliotecas compartilhadas que são atualizadas em cronogramas diferentes. Todos já reclamamos do "DLL-hell" da Microsoft. Só nesta semana meu sistema RedHat travou quando tentei instalar um software e descobri que minhas dependências de versão estavam todas bagunçadas (foi meio dia jogado no lixo). Talvez o sistema de versionamento do .NET resolva isso, mas até agora é fácil demais até para pessoas competentes se darem mal.

Percebi que o reuso (ou evitar duplicação) dentro de uma aplicação é essencial. Mas o reuso entre aplicações é muito mais difícil, principalmente porque um [ApplicationBoundary](/bliki/ApplicationBoundary.html) é, antes de tudo, uma construção social. Isso é mais uma evidência de que frameworks reutilizáveis são muito mais difíceis do que pensamos, e mais um motivo para considerarmos alternativas menos perfeitas — como os seedworks.
