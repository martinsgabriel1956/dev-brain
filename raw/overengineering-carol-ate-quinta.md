# Over-Engineering: Quando o Código Bonito Vira um Problema

**Canal:** Até Quinta (Carol)
**Tema:** Over-engineering na programação
**Data de captura:** 2026-04-29

---

## Transcrição

Você com certeza já ouviu falar de código limpo, arquitetura limpa, convenções, design patterns — aquilo que vai tornar o seu código bonito, abstrato, complexo, digno de uma obra de arte para qualquer um botar defeito. Mas aí o tempo vai passando e você entende que o programador que aumenta complexidade sem necessidade acaba cometendo um erro muito grave na programação. É o que a gente chama de **over-engineering**.

Infelizmente, um fenômeno que acontece é que programadores, à medida que ganham experiência, acabam pensando em soluções complexas demais para problemas simples. Não foi diferente comigo. Aconteceu comigo também. Mas todo mundo sabe que isso pode ser tão prejudicial quanto a boa e velha gambiarra. Muitas vezes o seu código bonito pode ser pior do que o código feio.

Uma das coisas mais fantásticas da programação é que não tem jeito certo de programar. Você tem várias possibilidades para resolver o mesmo problema — várias abordagens, arquitetura, design patterns. O que vai guiar a solução são os requisitos do projeto, do seu time, do negócio em que você está inserido. Você pensa qual é a melhor solução naquele sentido. E sim, muitas vezes chegar nessa definição é algo complexo e nebuloso.

---

## Sobre a apresentadora

Carol — engenheira de software sênior com mais de 12 anos de mercado. Canal "Até Quinta".

---

## O fenômeno do over-engineering

### Iniciantes pensam simples

Quando a gente está começando, tem pouco conhecimento. Como você está adquirindo esse conhecimento, você não tem muito background para tomar decisões. Iniciantes acabam limitados pelo próprio conhecimento e pensam em soluções o mais simples possível para os problemas.

Isso muda com o tempo. Lá na frente, pensar simples é uma das coisas mais difíceis na programação — quando você tem bagagem e conhecimento, é difícil tirar o viés de tudo que você aprendeu.

### KISS — Keep It Simple

Já ouviu falar desse tema? Pensar simples é um dos bons princípios da programação. Quer dizer basicamente que você deve evitar aumentar a complexidade de uma solução desnecessariamente. Parece simples pensar simples, mas não é. À medida que você adquire conhecimento, é muito difícil eliminar complexidades desnecessárias.

Quando a gente fala em evitar complexidade desnecessária, é evitar aquela complexidade que vai prejudicar a manutenção do software sem agregar valor.

---

## A história do Pedro

Pedro é iniciante, conseguiu seu primeiro emprego, ainda aprendendo. Toda vez que ele escreve um código, é revisado por programadores mais experientes — uma tonelada de comentários com referências e boas práticas. Ele entende que precisa melhorar.

Meio que sem querer, ele começa a pensar que o simples não é o suficiente. Luta com a síndrome do impostor. Olha para o código do sênior e fala: "Nossa, um dia eu quero fazer aquilo ali."

Pedro começa a estudar — arquitetura, abstração, paradigmas, design patterns. Realmente importante. Começa a melhorar o código, torná-lo mais abstrato. Só que isso evolui de uma forma que Pedro começa a colocar o ego acima da solução.

Ao invés de tomar uma decisão baseada em requisitos do projeto, ele começa a experimentar soluções novas e a abstrair demais para que fique bonito e abstrato. Começa a pensar: "E se esse código que eu estou usando aqui para caldo de cana um dia fosse utilizado para fritar pastel?"

E aí a gente cria aquelas bizarrices abstratas que acabam dificultando de forma tremenda a manutenção do projeto.

---

## O problema do ego na engenharia

Isso já aconteceu com muitas pessoas — com a maioria. É muito comum no meio da programação. Até você ganhar experiência para entender que aumentar complexidade, mesmo pensando no futuro, vai te fazer sofrer lá na frente.

Quando a gente pensa em uma solução de engenharia, a gente tem que ponderar muito a questão da necessidade. Vamos supor que você queria uma solução extremamente complexa e robusta onde outros desenvolvedores sem aquele conhecimento específico teriam dificuldade para entender. O que vai acontecer é que as pessoas que vão trabalhar nesse projeto vão criar gambiarras para forçar comportamentos — simplesmente porque não têm o conhecimento daquilo que foi implementado.

Por isso é muito importante pensar também a nível de time — aquilo que você está implementando. É isso que faz projetos virarem: você tem um padrão de projeto, chega outra pessoa, sugere outro padrão, você tem metade do projeto em um padrão e metade em outro, com gambiarras conectando os dois.

---

## Código feio vs. código bonito

Algumas semanas atrás rolava uma thread no LinkedIn onde as pessoas falavam sobre um caso de um código feio que performava melhor do que um código bonito — por conta das camadas a mais de abstração, a performance era prejudicada em milissegundos. Muitas pessoas usaram esse argumento para defender o código feio.

Tudo bem que esses termos são relativos — código feio, código bonito. O que estamos falando aqui: uma solução ruim, uma gambiarra que vai dar problema, ou um código simples? Há uma diferença enorme.

A gente não pode usar esse argumento para defender o código feio, para defender a falta de conhecimento. É muito importante ter conhecimento, entender as possibilidades, e saber ponderar isso na hora certa. A questão dos milissegundos, na prática, muitas vezes não afeta nada — e você ganha na questão da manutenção e qualidade do código.

---

## Comentários relevantes do LinkedIn

**Marcelo:**
> "Over-engineering, em minha opinião, atrapalha quase tanto quanto o código bagunçado. Assim como gambiarra, excesso de abstrações confunde muitas pessoas e acaba abrindo espaço para código com funcionalidade duplicada — justamente por conta do dev com menos contexto não conseguir lidar com o excesso de abstrações."

**Danilo Furtado:**
> "O quanto eu já vi códigos em empresas com MVP mais clínica que era tão abstrato e tão genérico... PQP. Era muito difícil a manutenção, até mesmo entender para que servia aquela classe, aquele código."

**Gabi Ferreira (criador de conteúdo):**
> "Como quase toda pergunta que se faz para dev deve ser: 'depende'. Código feio, código bonito, abstrato — pode ser a melhor opção ou pior, dependendo do contexto."

---

## Dica para freelancers iniciantes (HTML/CSS)

Pergunta do Johnny: qual tipo de freela indicaria para quem está com apenas HTML e CSS?

- Algumas freelances pedem apenas o front-end: pegar o design e transformar em HTML/CSS.
- Plataforma Fiverr tem muito esse tipo de serviço — pesquise "HTML CSS JavaScript".
- Outros projetos em outras plataformas freelancer: landing pages, sites estáticos que não precisam de nada dinâmico.
- **Dica diferenciada:** entre em contato com agências de publicidade. Poucas pessoas fazem isso — todo mundo vai para as plataformas online. Você consegue gerar contato mais direto e ir atrás das agências criar esse relacionamento.

---

## Patrocinador

**Cubes Academy** — curso de desenvolvimento de software, agora no formato noturno:
- Metodologia estruturada: técnica + direcionamento de carreira.
- Aulas gravadas + mentorias ao vivo.
- Programa de residência de software (experiência de mercado desde o início).
- Link na descrição do vídeo com cupom de desconto.

---

## Próximos vídeos mencionados

1. "10 verdades que você precisa saber antes de se tornar um programador."
2. Indicação de canal de games do YouTube.
