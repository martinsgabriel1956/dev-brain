# Por que programadores têm os melhores prompts: a IA não virou o jogo, ampliou a distância (transcrição)

> Transcrição de vídeo (PT-BR), limpa de erros de ASR; sem tradução (já em português). Autoria inferida pela autorreferência "Balta" (comentários de público citados no fim) e pelo contexto de cursos de C#/.NET. Trechos ASR ambíguos marcados com `[?]`. O vídeo resume um post do LinkedIn do autor e um artigo (link na descrição, não identificado na transcrição) sobre prompting dos modelos Claude.

Há um tempo atrás eu postei no meu LinkedIn algo sobre prompts e programador, e esse foi um dos posts mais comentados do ano. Vou deixar o link na descrição. Quero resumir o que falei sobre IA, programação, prompts e por que os programadores tendem a ter os melhores prompts.

## A IA não dá poder a ninguém: só ajuda quem já sabe o que quer

A IA não dá poder para ninguém, só ajuda quem já sabe o que quer. Se você coloca um gerador de vídeo como o Veo 3 (ou qualquer outro) na minha mão, eu não consigo criar um vídeo legal, pelo menos até agora, porque meus prompts são vagos: não sei o que pedir em termos de criação de vídeo, não sei como é feita uma boa composição. O mesmo vale para qualquer área. Qualquer pessoa pode pedir uma landing page ao Claude, mas se ela vai ficar boa e vender é outra história: envolve marketing e outros itens.

O problema é que quem não tem essa noção vai queimar tempo, dinheiro e muito token, porque há um desperdício enorme na geração de conteúdo que parece bom mas é só "uma cara bonita enfeitando um sonho ruim".

## O artigo: parece sobre agentes, mas é sobre contexto

O artigo (na descrição) fala principalmente da família de modelos Claude (a transcrição cita "família CCO `[?]`", Fable, Opus e outros), mas a ideia vale para todos os modelos. Parece falar de agentes, mas no fundo fala de **contexto**, "a máxima da IA". Muita gente espera que a IA adivinhe o que precisa ser feito; ela entrega muita coisa ruim e a pessoa conclui "a IA não funciona para mim", quando na verdade ela é que não sabe pedir. O autor destrincha em quatro partes.

### 1. Tamanho do prompt

Dá muita discussão: prompt grande e específico ou pequeno e genérico?

- **Específico demais:** a IA sempre segue o que você escreve, mesmo que ela conheça uma solução melhor. Ela não vai implementar a melhor.
- **Vago demais:** ela alucina; preenche com o que acredita ser bom. Exemplo: "cria uma API de produtos". Com CQRS? Repository pattern? Minimal API ou controllers MVC? Autenticação ou não? Com Identity? Há milhões de formas; se você não informa, o modelo responde com o que ele "tem em mente", treinado com dados da internet.

Analogia: construir um sistema é como construir uma casa. Na sua rua há casa térrea, sobrado, com subsolo, garagem na frente, garagem no fundo. Qual é a melhor? Depende do que você precisa. Você precisa saber o que quer para a IA poder ajudar. É por isso que o autor acha difícil o sonho de "negócio criar o sistema inteiro com IA".

### 2. Saber o que você quer (falso positivo e o "não sei que não sei")

Dois itens: (a) o **falso positivo**, achar que está certo mas está errado; (b) o pior, **nem saber que está errado**, ou nem saber que algo melhor existe. Você pede para mudar a rota, pede algo diferente, mas nem sabe que aquilo não funciona ou que havia algo melhor no meio do caminho.

"Nem o melhor modelo, nem o modelo mais top vai ajudar quando você não sabe o que quer." Nenhum modelo, sênior ou profissional consegue ajudar; isso não é problema da IA, é **problema de clareza**. Talvez seja preciso voltar ao papel e caneta, enumerar o que se quer, e só então pedir. É como pedir ao seu time: "meu time não me entrega", mas será que você pede de forma clara, ou cada hora pede uma coisa diferente?

### 3. Ambiguidade

A ambiguidade acontece no desenvolvimento normal, com a gente e com a IA. Se a IA se perde por 20–30 minutos, tudo bem: dá para ver no prompt que ela tenta uma coisa, volta, tenta outra e acaba com a solução. Mas **se a IA se perde por dois dias**, você já tem uma dívida técnica imensa e provavelmente queimou muitos tokens. É o pior cenário: ela se perde **mas não sabe que se perdeu**, continua confiante, entregando o que você não queria.

Causas: falta de revisão humana (não olhar o código gerado, não dizer "não era isso que pedi"); tentar forçar a continuação de conversas. O autor já mostrou em lives o quão ruim é tentar recuperar contexto: **respondeu errado/não entendeu → descarte aquele contexto, crie outro, comece uma conversa nova de cabeça limpa.**

A IA desenvolve muito rápido. O que levava uma semana com o time para fazer uma besteira, hoje se faz em 20 minutos. Ela não cria só código bom rápido; cria **código ruim rápido** e **toma decisão errada rápido**. Antes errar levava 3–4 semanas; hoje, 20 minutos, e às vezes já foi para produção.

### 4. O especialista sempre leva vantagem

O ponto mais importante. O especialista conhece o que está pedindo e sabe o que fazer. Se existisse uma IA mágica que criasse carros de Fórmula 1, o autor (zero em mecânica) não saberia pedir para otimizar; um engenheiro da McLaren a usaria para um avanço enorme na performance. Na nossa área: quem tem boa base de performance e baixo nível (otimização de memória, como as coisas funcionam) fará bom uso da IA; quem trabalha mais com APIs, na camada acima, não conseguirá otimizar tanto a API porque não sabe o que pedir.

**Os melhores usuários de IA têm poucas zonas de desconhecimento.** Quanto mais você conhece, melhor o prompt; quanto mais mitiga os dois pontos do item 2 (não saber que está errado / não saber que algo existe), melhores os prompts. Ao criar uma arquitetura, o autor já sabe qual quer, por quê, a motivação e o que pode dar errado; a IA vira "só um parceiro": ele guia, dá instruções, e ela serve de base de apoio para bater papo e trocar ideias sobre o projeto.

## Tese: a IA não virou o jogo, ampliou a distância

Na visão do autor, "a IA não virou o jogo, só ampliou a distância": quem sabe pouco continua sabendo pouco e entregando pouco; quem sabe muito entrega com mais capacidade e velocidade. Se você usa IA e não consegue entregar muito, ainda tem muita coisa a estudar. Resumo: **quem sabe pouco ficou mais rápido, só que na direção errada.**

## Fundamentos e teoria nunca foram tão importantes

A prática, a escrita de código, a IA faz: converte C# para qualquer linguagem e vice-versa em minutos, e a cada dia melhor. O que sobra para nós são **fundamentos**: C#, orientação a objetos, acesso a dados, performance, banco de dados, ASP.NET e como a web funciona, deployment, Docker, nuvem, mensageria, CQRS, arquitetura, DDD. É o que se estuda há muito tempo; design patterns, por exemplo, são de 1994 e ainda se estudam. **Fundamentos não mudam.**

Quem coloca muita mão na massa e pouca teoria (muita gente acha teoria chata) tem problema: sem teoria hoje não se consegue conversar com a IA. "Quero uma API igual a tal API", mas por que aquela API funciona, por que é boa nesse cenário? Você só manda replicar; qualquer pessoa vai conseguir fazer isso daqui para frente, não é diferencial. É a sensação de seguir muitos tutoriais: você faz um CRUD, vai bem, acha que aprendeu; no mundo real pedem uma tela master-detail e você não sabe fazer, porque não tem teoria nem fundamento.

Por isso boa parte dos conteúdos do autor (cursos) são bem teóricos: a prática vocês descobrem sozinhos, codando. A necessidade é entender o *porquê* de cada situação; sabendo isso, você implementa sua arquitetura do seu jeito. No sistema novo que o autor tem rodando, a arquitetura é "um mix": pedaços de uma e de outra, do jeito deles. Não é porque se criou uma Clean Architecture que se deve seguir sempre aquele modelo: existe um conjunto de princípios que tornam a arquitetura boa, e sabendo os fundamentos você cria a sua.

## Analogia final: construção civil

Criar uma casa nunca é a mesma casa. Você aprendeu a fazer uma casa térrea, mas não um sobrado; não aprendeu fundação nem alicerce, a base de como as coisas funcionam. Com frameworks, o alicerce já vem pronto: você só "subiu o muro", nunca fez um alicerce nem mexeu na fundação. Por isso falta base, e é preciso resolver isso o quanto antes, "porque daqui pra frente subir muro é a IA que vai fazer".

Encerramento: o autor pede opinião nos comentários. (Citações de público: "Pô, Balta, os cursos têm bastante fundamento, bastante teoria".)
