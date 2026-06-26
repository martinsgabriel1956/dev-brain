# 4 Hábitos Ruins de Programador

> Transcrição/adaptação de vídeo. Autor do artigo de referência: **Dano** — artigo: *"For Web Da Nec"*

---

## Introdução

Você não é um programador ruim — você pode **ter hábitos** de um programador ruim. Há uma diferença fundamental entre *ser* algo e *estar* algo. Quando alguém escreve "eu não sou um bom programador", o problema está na formulação: você pode estar num nível ruim de desenvolvimento, assim como pode estar cansado — não *ser* cansado.

O cérebro, o pedaço de carne mais sofisticado do planeta, frequentemente se depara com duas escolhas:

- Uma que pode gerar progresso, mas com desconforto garantido.
- Outra que não gera progresso, mas garante conforto.

---

## Hábito Ruim #1 — Falar "Sim" para Tudo

Tentar ajudar a todos é uma postura louvável, mas uma promessa é uma dívida. Assumir dívidas de forma descontrolada tem um custo alto: o tempo estoura e os juros são caríssimos. Mesmo que você consiga dar conta, sua performance e produtividade como programador caem — você é constantemente interrompido.

Esse comportamento é comum ao entrar numa empresa nova: querer mostrar que você "serve para alguma coisa". O problema aparece quando você vira uma espécie de dependência — as pessoas ficam viciadas em sua opinião antes de qualquer decisão ou risco.

**Exemplo prático:** Se alguém pede para você revisar um e-mail arriscado antes de enviá-lo, ao revisar você divide a culpa se der errado e divide o crédito se der certo. Mas se a pessoa assumir 100% do risco e 100% do retorno, ela cresce muito mais.

Ao aniquilar o risco das outras pessoas o tempo todo, você também inibe o surgimento de novos líderes.

> *"Quando disser sim para outros, certifique-se de não estar dizendo não para si mesmo."* — Paulo Coelho

**Atenção:** calibre o nível de senioridade com o nível de risco. Não deixe alguém inexperiente tomar decisões críticas sem supervisão (ex: queries em banco de produção sem WHERE).

---

## Hábito Ruim #2 — Sua Definição de "Pronto" Não É Pronto

Programação tem uma característica importante: digitar código é apenas uma das milhares de tarefas de um programador. A diferença entre quem entendeu isso e quem não entendeu é visível.

Acreditar que rodar o código e marcar como "finalizado" é estar pronto é, provavelmente, estar muito longe disso. Perguntas que indicam que algo realmente não está pronto:

- Você olhou para o código de forma crítica?
- Outro desenvolvedor conseguiria entender isso facilmente?
- Você refatorou o que estava confuso?
- A alteração tem reflexo na documentação?
- Na revisão, você focou em regras de negócio ou só em estilo?
- Você testou além do caminho feliz?

O que foi entregado era um rascunho, não a entrega final.

---

## Hábito Ruim #3 — Não Testar o Próprio Código

Testar apenas o caminho feliz de uma implementação é tão ingênuo quanto concordar com a própria opinião sem questionamento.

- Escreva testes automatizados — comece o quanto antes para ganhar prática e velocidade.
- Garanta o comportamento das coisas funcionando **e** garanta o comportamento quando elas deveriam retornar erros.
- Ser enganado pelo próprio teste dói, mas é um aprendizado valioso.

Mesmo que sua empresa tenha uma pessoa dedicada a QA, isso não transfere a responsabilidade de você testar o que escreve.

---

## Hábito Ruim #4 — Fazer Commits/PRs Gigantescos

A sensação ao revisar um pull request gigantesco é ruim: você não sabe quando vai terminar, e nem dá vontade de começar.

Um padrão comum e problemático:

1. Você faz um commit que quebra um teste.
2. Num commit seguinte, você corrige o teste.

**O que fazer:** No mesmo commit, faça a alteração do código **e** a alteração que faz o teste passar. Transforme cada commit numa unidade de alteração funcional — não num diário de mudanças.

Commits bem modelados são mais valiosos, mais fáceis de revisar e mais fáceis de reverter.

---

## Síntese

Todos esses hábitos estão conectados: corrigi-los torna você um programador melhor, com menos fricção, e como consequência — mais rápido e mais valioso.
