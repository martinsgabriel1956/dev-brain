# Refatoração: Pragmatic Programmer, Martin Fowler e a 2ª Edição de Refactoring

**Formato:** Transcrição de vídeo (YouTube)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-07-27
**Referência:** The Pragmatic Programmer; Refactoring (Martin Fowler, 2ª edição); palestra e entrevista de Martin Fowler (Thoughtworks)

---

## Introdução

E aí, galera, beleza? Esses dias eu estava vendo um capítulo do livro *Pragmatic Programmer* — que eu já falei aqui para vocês que eu tenho lido — e ele fala sobre refatoração. Então queria falar um pouquinho sobre refatoração.

Eu também vi uma palestra do Martin Fowler em que ele fala da 2ª edição do livro *Refactoring*, que lançou 20 anos depois da primeira edição. E, vindo para cá, eu estava escutando também uma entrevista do Martin Fowler com uma brasileira da Thoughtworks — a empresa que foi fundada também pelo Martin Fowler. Vou colocar os links da palestra e do bate-papo na descrição do vídeo.

## Essência vs. Acidente

Eu tenho falado para vocês aqui, pessoal, várias vezes, sobre a questão da diferença entre essência e acidente no desenvolvimento de software. Existem coisas que são problemas essenciais e fundamentais, e coisas que são mais acidentais. Essas coisas mais acidentais estão mais relacionadas com tecnologias, e essas tecnologias, a gente sabe, vêm e vão — hoje a gente está falando de Julia, ontem a gente falava de Go, PHP. São tecnologias que realmente vêm e vão. Mas os princípios fundamentais ficam.

Prova disso, pessoal, é esse livro do Martin Fowler, *Refactoring*, cuja primeira edição foi publicada há 20 anos. O *Pragmatic Programmer* também: a primeira edição dele foi publicada há 20 anos atrás. E hoje eu estou lendo a edição comemorativa de 20 anos. Ou seja: como esses caras tratam de problemas essenciais do desenvolvimento de software, esses livros ainda são relevantes.

Eu já falei várias vezes para vocês isso, e repito: um dos papéis deste canal é trazer para vocês princípios fundamentais que realmente não mudam e que realmente ajudam a desenvolver bom software.

## Por que Martin Fowler escreveu uma segunda edição

Uma das perguntas da brasileira para o Martin Fowler foi: por que ele fez uma segunda edição do livro *Refactoring*? E, de fato, o Martin Fowler respondeu o seguinte: que o *Refactoring* já era relevante há dez, vinte anos atrás, e ele resolveu editar uma nova versão principalmente porque o código parecia muito antigo — porque, de fato, a primeira versão foi escrita usando Java, que tinha lá umas coisas de Java que não se usam mais há mais de dez anos, como por exemplo a classe `Vector`, que não se utiliza mais há muito tempo.

Além desse motivo do código estar antigo e datado, ele também disse que algumas refatorações estavam muito atreladas à orientação a objetos. A gente sabe que refatoração não é uma coisa específica de um paradigma de programação — a programação orientada a objetos é onde ela é mais associada, mas ela vale para qualquer tipo de paradigma. Então ele reeditou o livro pensando nisso: usar uma linguagem mais nova, no caso JavaScript, e também desatrelar um pouco da orientação a objetos, porque refatoração serve para qualquer tipo de paradigma de programação.

## O novo exemplo: peças de teatro

Outra coisa bem legal do livro, pessoal, é que na primeira edição ele usava um exemplo de programação que era uma locadora de vídeos — ninguém mais usa fita de vídeo, e muitos de vocês nunca usaram isso. Então, de fato, ele trocou o exemplo. E olha só que legal o exemplo que ele está usando agora na segunda edição do livro: é um exemplo de um domínio mais permanente da atividade humana, que é o de peças de teatro.

Desde pelo menos a Grécia Antiga a gente tem peças de teatro. Então o novo exemplo que ele usa no livro é de peças de teatro e teatros que gerenciam peças de teatro. Não é legal isso, pessoal? Pensa só: como esse exemplo é muito mais permanente, isso faz com que essa edição valha por mais tempo do que a primeira edição, que tinha uma tecnologia de locação de fitas de vídeo que nem se utiliza mais.

Então, o Martin Fowler é realmente um desses mestres do desenvolvimento de software que eu falo para vocês que vale a pena seguir e aprender.

## A analogia da jardinagem

Mas, afinal, o que é isso, refatoração? Lá no livro *Pragmatic Programmer*, os autores usam uma analogia muito legal: muitas vezes o desenvolvimento de software é comparado com construção — construção de prédios. E eles dizem que essa analogia não é a mais adequada. Eles falam que uma analogia mais adequada é a da jardinagem, porque, de fato, quando você está desenvolvendo um jardim, o que acontece? Às vezes crescem plantas daninhas que você precisa arrancar; às vezes as próprias plantas boas começam a crescer demais, cresce um galho a mais, e você precisa ir lá e podar.

Então software é mais parecido com jardinagem, porque, de fato, o código é uma coisa viva, e com o tempo a gente tem essa questão do débito técnico. De fato, o código vai degradando — em inglês é *decaying* — porque ele vai degradando com o tempo. A refatoração é uma maneira de você manter o software saudável, porque você vai podando essas ervas daninhas, os galhos que vão saindo a mais, para deixar o código bem estruturado, bem bonito, para manter a qualidade do código.

## Definição de refatoração segundo Martin Fowler

Qual é a ideia do Martin Fowler de refatoração? É uma pequena alteração estrutural que não altera o comportamento do sistema. Então é uma mudança na estrutura interna do código que não altera o seu comportamento.

O legal é que o Martin Fowler fala que essa alteração é tão pequena que, isoladamente, ela não vale a pena — "poxa, para que eu vou fazer isso?" — mas, como você faz muitas pequenas alterações, aí sim, no conjunto, vale a pena fazer a refatoração. Mas uma refatoração sozinha é uma coisa tão pequena que parece ridícula, que não vale a pena fazer, como por exemplo você mudar o nome de uma variável. Quando você muda o nome da variável, você muda a estrutura do código, mas não altera o seu comportamento.

Então refatoração, como uma coisa pequena, é comparável a cortar a grama, a podar os excessos das plantas — é uma atividade que você precisa fazer no dia a dia, e não somente esporadicamente.

## Quando fazer refatoração — as duas motivações de Fowler

Quando que eu faço refatoração? O Martin Fowler dá dois exemplos, dois tipos de motivações para você fazer refatoração:

1. **Quando você entende melhor o código.** A ideia é: você entendeu melhor o código, e agora você vai colocar de volta esse entendimento no código.
2. **Quando você quer fazer alguma alteração** e essa alteração vai ser difícil do jeito que o código está agora. Então você refatora para facilitar a modificação.

A ideia do Martin Fowler é que você fique alternando entre adicionar funcionalidades novas no sistema — adicionar features — e refatorar o sistema. Então você fica nesse jogo de adicionar features e refatorar, adicionar features e refatorar. Com isso, você mantém a saúde do sistema enquanto ele cresce.

## As seis situações do Pragmatic Programmer

Os autores do *Pragmatic Programmer* também dão outras seis situações em que é interessante você refatorar o código:

1. **Duplicação.** Quando você acha alguma duplicação — lembra lá daquele princípio DRY, *don't repeat yourself* — é uma boa hora de você refatorar o código.
2. **Falta de ortogonalidade (acoplamento).** Quando você acha um código que não está ortogonal, ou seja, muito acoplado, e você quer desacoplar, vale a pena fazer refatoração nesse caso também, para tirar o acoplamento.
3. **Conhecimento desatualizado.** Quando o seu conhecimento ficou desatualizado — você aprendeu uma coisa nova sobre o sistema, sobre os requisitos — isso requer refatoração no código para espelhar o conhecimento novo.
4. **Mudança de prioridades no uso real.** Quando o sistema passa a ser utilizado por pessoas reais, e algumas coisas que você achava que não eram muito importantes passam a ser mais importantes, e coisas que você achava que eram importantes passam a ser menos importantes — esse tipo de situação também vale a pena você refatorar o código, para refletir a importância dessas partes.
5. **Melhoria de performance.** Quando você percebe uma possível melhoria de performance e precisa dessa melhoria, você refatora o código para manter o comportamento que ele tem, mas com melhor performance.
6. **Quando um teste passa.** Parece um pouco engraçado, mas é a melhor situação para alterar o seu código: quando você tem um teste passando para aquele trecho do código. Quando você tem um teste passando, você tem muito mais confiança para alterar o código, porque você pode rodar o teste de novo e ver se o código continua com o comportamento que deveria ter — é o chamado teste de regressão.

## O sacrifício da refatoração

Na verdade, refatoração não é uma coisa muito gostosa — a gente sabe que alterar código é uma coisa meio dolorosa. Então refatoração exige uma gerência desse sofrimento. Vale a pena enfrentar esse sofrimento, fazer esse sacrifício, para que seu código fique um pouquinho melhor a cada vez. Como você faz isso várias vezes, nas pequenas coisas que a gente vai melhorando, com bastante tempo a gente vai ter um código bem bonito, bem estruturado.

Então a dica dos autores do *Pragmatic Programmer* é: refatore cedo e refatore com frequência. E, de fato, pessoal, eu já falei aqui sobre entropia de software — essa questão do software degradando com o tempo. Se você refatora, você diminui a chance do seu sistema degradar com o tempo.

## As três dicas de Martin Fowler para refatorar bem

Refatoração é uma coisa que deve ser feita de forma lenta, deliberada e com cuidado. O Martin Fowler dá três dicas aqui para que a refatoração traga mais benefícios do que danos ao seu sistema:

1. **Não misture adicionar funcionalidade com refatorar.** Tem a ver com aquilo que eu falei para vocês: adiciona funcionalidade, faz refatoração; adiciona funcionalidade, faz refatoração. Não tenta fazer as duas coisas ao mesmo tempo. Primeiro você adiciona a feature, depois você refatora. Isso segue também aquele princípio do TDD: primeiro faz funcionar, depois refatora para ficar bem estruturado.
2. **Sempre tenha testes para suas refatorações, e rode-os com frequência.** Quanto antes você pegar um defeito que foi causado por uma reestruturação, melhor — mais fácil de rastrear e consertar o problema.
3. **Tome passos pequenos** — os *baby steps*. Primeiro renomeia uma variável, depois move esse atributo de uma classe para outra, depois quebra o método em dois. Nunca tenta fazer várias refatorações ao mesmo tempo — isso pode ser perigoso. Com esses passos pequenos e deliberados, você pode ir rodando os testes sempre, evitando assim o debugging prolongado.

## Encerramento

Galera, obviamente eu quero falar mais sobre refatoração mais para frente, mas fica aí algumas dicas e a definição de refatoração para vocês procurarem saber mais e adotarem essa prática no dia a dia. Hoje em dia, com essas IDEs mais modernas, você tem muita facilidade para fazer refatoração, porque muitas delas são automatizáveis — então ajuda muito também você ter uma IDE poderosa para fazer vários tipos de refatoração.

Então, a próxima vez que você ver um código que não está bom, retruca, gerencia — vale a pena aceitar essa dor agora do que ter que cuidar de uma dor muito maior mais para frente. Então: refatore cedo e com frequência.

É isso aí, galera. Fiquem com Deus e até o próximo vídeo.
