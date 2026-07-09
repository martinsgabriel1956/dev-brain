# 5 Princípios Que Me Mudaram Como Programador

> Transcrição de vídeo (inglês, traduzida) sobre por que alguns desenvolvedores nunca crescem mesmo depois de anos na área — um dos motivos é não entender os princípios subjacentes da programação. Não são teoria para aprender uma vez e esquecer; são o que de fato acelera o crescimento como programador.

---

## Princípio 1 — Boy Scout Rule (Regra do Escoteiro)

Vem dos escoteiros nos EUA: *"deixe o acampamento mais limpo do que você encontrou"*.

Uncle Bob popularizou esse conceito na comunidade de programação: a prática de deixar o código um pouco mais limpo do que você o encontrou, sempre que fizer uma mudança numa base de código existente.

A qualidade do código tende a degradar com o tempo — isso aumenta a dívida técnica. E dívida técnica se reduz com melhoria contínua, não importa o quão pequena.

**Exemplo:** você foi designado para mudar um valor dentro de uma função. Fez a mudança. Mas percebe que o nome das variáveis não está claro o suficiente. A maioria dos devs ignora isso e só comita o que foi pedido. Quem segue essa regra também melhora o nome da variável. Não é só sobre nomes — qualquer coisa que você perceber que pode ser melhorada, melhore. Esse gesto simples é extremamente valioso para a base de código a longo prazo.

---

## Princípio 2 — Evite Otimização Prematura

Não tente deixar seu código mais rápido antes que ele realmente precise ser rápido. Primeiro faça funcionar, só depois otimize se necessário.

> "Premature optimization is the root of all evil." — Donald Knuth

Programadores costumam desperdiçar a maior parte do tempo se preocupando com a velocidade de partes não-críticas do programa, porque foram condicionados a esse hábito de otimizar tudo.

Esse princípio não é contra otimizar — é sobre entender **o que** precisa ser otimizado e, principalmente, **quando** otimizar. Essa é a fraqueza de muitos desenvolvedores: já vi gente usando microsserviços com 100 usuários, ou adicionando cache para algo que nem precisava.

---

## Princípio 3 — Escreva Código Para Quem Vai Mantê-lo

Quando você escreve código, escreva de um jeito que o futuro desenvolvedor que vai mantê-lo (que pode ser você mesmo) não tenha dificuldade para entender e gerenciar.

O código que você escreve hoje será mantido por outra pessoa — ou por você no futuro. Se o único foco for "fazer funcionar" sem se importar com clareza, no futuro, ao voltar a esse código, você vai ter dificuldade de entender o que está acontecendo.

Duas implementações podem fazer exatamente a mesma coisa, mas uma é claramente preferível numa base de código real. A lição: sempre que você escrever ou gerar código com IA, garanta que ele seja fácil de entender e manter antes de comitar.

---

## Princípio 4 — YAGNI (You Aren't Gonna Need It)

Você não deveria construir algo que não precisa agora só porque *talvez* precise no futuro.

A maioria dos desenvolvedores tem o hábito de tentar prever o que vai precisar futuramente — mas, na maior parte das vezes, essa previsão nunca se concretiza, e só adiciona complexidade desnecessária ao projeto.

Lembre-se: se você está gastando tempo com algo que só *talvez* seja necessário no futuro, você está tirando tempo do que precisa *agora*.

---

## Princípio 5 — Faça a Coisa Mais Simples Que Poderia Funcionar

Diante de um problema, escolha sempre a solução mais simples que de fato resolve. Não fique pensando demais, não superengenheire — pergunte-se: qual é a coisa mais simples que resolve isso agora?

Essa ideia vem da Extreme Programming (XP), que ensina a construir algo simples primeiro e depois refatorar para algo melhor.

Muitos desenvolvedores não percebem, mas tentam construir a solução perfeita desde o início — o que acaba supercomplicando a solução. Com esse princípio você chega a um código funcional mais rápido, e mesmo que precise mudar depois, isso costuma ser mais fácil do que consertar um design complexo que já nasceu errado.

Como desenvolvedor, perceber quando você está superengenheirando algo é uma habilidade muito importante.

---

## Fechamento

Esses foram os cinco princípios de programação que você deveria começar a aplicar imediatamente. Existem outros que não foram cobertos neste vídeo — fica para uma segunda parte.
