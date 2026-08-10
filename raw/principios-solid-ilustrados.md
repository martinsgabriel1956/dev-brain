# Princípios SOLID Ilustrados

> Transcrição de vídeo (português) sobre um artigo que ilustra os cinco princípios SOLID com desenhos simples de robôs. O vídeo mistura as ilustrações da autora original com a interpretação pessoal do apresentador, incluindo o "efeito dominó" entre os princípios — como um força o comportamento do outro — e onde a comunidade diverge sobre os limites de cada um.

---

## Contexto

A autora do post publicou um artigo chamado "The SOLID Principles in Pictures", ilustrando cada princípio com um robozinho em uma versão errada e uma versão certa. O apresentador usa essas ilustrações como fio condutor, conectando cada uma a um modelo mental próprio e a exemplos práticos de código (processador de pagamentos, ORM, extensões de navegador).

---

## S — Single Responsibility Principle

Uma classe, componente, entidade ou função deve ter uma única responsabilidade.

**Ilustração errada:** um robô que é ao mesmo tempo chefe de cozinha, jardineiro, pintor e motorista — faz tudo.

**Ilustração certa:** para cada responsabilidade do sistema existe uma entidade especializada apenas naquilo, e a melhor possível naquele assunto.

### Por que separar responsabilidades

- Reaproveitamento de código mais fácil.
- Refatoração mais fácil.
- Testes automatizados mais fáceis.
- Menos bugs — e quando ocorrem, são mais fáceis de isolar e consertar.
- Permite implementar coisas novas sem precisar carregar o programa inteiro na cabeça: cada responsabilidade fica isolada, então você presta atenção só naquele pedaço até fechar e passar para o próximo.

### Analogia: manchar roupa na máquina de lavar

Numa máquina de lavar (o "componente"), basta uma meia vermelha para manchar todas as roupas claras. Em software acoplado, basta um componente no lugar errado para manchar o comportamento de todos os outros.

**Exemplo:** um sistema de cadastro e login acoplados numa mesma entidade "usuário". Uma alteração no fluxo de cadastro pode quebrar o login de quem já está cadastrado — mesmo que essas pessoas não tenham mais nada a ver com o processo de cadastro. A solução é ter duas "máquinas de lavar" separadas: uma só com peças de cadastro, outra só com peças de login.

### Dica prática para achar o limite da responsabilidade

Tente colocar no nome da função ou do componente tudo que ele está fazendo. Se o nome fica bizarro (ex.: `registrationAndImagingConfirmationAndAuthentication`), essa entidade provavelmente tem responsabilidade demais. Para quem está começando, é normal "manchar a roupa" algumas vezes — é assim que se aprende a identificar onde as responsabilidades se misturam. Só cuidado para não cair no design prematuro tentando separar tudo demais antes de precisar.

---

## O — Open/Closed Principle

Classes, entidades ou funções devem estar abertas para extensão, mas fechadas para modificação.

**Ilustração errada:** um robô fala "eu sei cortar" segurando uma faquinha; depois fala "agora eu sei pintar", só que a faquinha sumiu e virou um rolo de pintura — ele perdeu a capacidade anterior para ganhar a nova.

**Ilustração certa:** o mesmo robô mantém a faquinha numa mão e, ao aprender a pintar, segura as duas ferramentas ao mesmo tempo — "agora eu sei cortar e pintar".

A versão errada representa o caso em que, para cada novo requisito, você precisa modificar a entidade existente — geralmente adicionando mais um `if`, mais um caminho novo dentro do código. O comportamento antigo não desaparece, só se acumula em cima do código antigo, e cada novo requisito gera mais uma condicional, dificultando cada vez mais a manutenção.

### Exemplo — processador de pagamentos

Uma abstração `processarPagamento` recebe um objeto de cartão, valida os campos (número, vencimento, nome), consulta um serviço de antifraude e realiza a cobrança. Funciona bem para cartão de crédito e, por serem campos parecidos, também para cartão de débito sem mudanças.

Quando chega o requisito de processar boleto — campos completamente diferentes, sem o mesmo fluxo de antifraude — a saída rápida (e errada) é abrir a classe base `processarPagamento`, hoje fechada, e adicionar um novo `if` para tratar boleto como caso especial. A cada novo método de pagamento (ex.: pontos de fidelidade), seria necessário voltar a mexer nessa classe base, e a regra de negócio específica de cada produto passaria a "manchar" o processador genérico.

**Solução:** a abstração base não deveria conhecer os campos específicos de cada produto financeiro. No limite, ela apenas recebe um objeto de pagamento/instrução e pede para esse objeto se validar, depois se cobrar — sem saber os detalhes de implementação. Se todo objeto injetado respeitar essa mesma interface, a classe base de processamento nunca mais precisa ser modificada quando surgir um novo método de pagamento.

### Outro exemplo — ORM

Um ORM relaciona propriedades de um objeto com colunas de tabela usando os mesmos métodos genéricos (salvar, atualizar, deletar), independentemente do banco usado. Sem tocar no código-fonte do ORM, é possível estendê-lo para funcionar com um novo banco (MySQL, Postgres etc.) sem alterar a camada de abstração principal — embora, no limite, até essa abstração tenha um teto de generalização.

### Modelo mental: plugins de navegador

Uma extensão de navegador acrescenta funcionalidades novas sem que ninguém precise alterar o binário do navegador — porque a extensão respeita um contrato (interface) previamente estabelecido e se encaixa nele. O navegador está **aberto** para novas funcionalidades (extensões) mas **fechado** (o binário não muda).

---

## O Efeito Dominó (S + O + L + I + D)

O apresentador propõe pensar nos cinco princípios como peças de dominó: um força o comportamento do outro, para o bem ou para o mal. No exemplo do processador de pagamentos, resolver o Open/Closed exigiu, na prática, aplicar também Liskov Substitution e Dependency Inversion via injeção de dependência — cada implementação de pagamento é livre para fazer o que quiser internamente, desde que respeite a interface esperada (isso pode ser feito também com um design pattern observador, sem injeção de dependência formal).

Robert C. Martin (1996) descreveu que o uso rigoroso conjunto do Open/Closed e do Liskov Substitution pode ser generalizado em um princípio à parte: o Dependency Inversion Principle.

---

## L — Liskov Substitution Principle

Se uma subclasse é criada por herança a partir de uma classe base, um objeto dessa subclasse deve conseguir substituir um objeto da classe base sem quebrar o programa.

**Ilustração errada:** um robô "pai" sabe fazer café; o robô "filho" (criado por herança) não está disponível, e quando pedem café a ele, o filho responde "eu não sei fazer café, mas aqui está uma água".

**Ilustração certa:** pedem café ao robô filho e ele entrega, inclusive um cappuccino.

### Onde o princípio costuma confundir

A dúvida comum é: por que eu substituiria a classe pai por uma subclasse, se isso não parece a evolução natural do software? A resposta proposta no vídeo é que o valor real do princípio está em forçar a pensar no **nível certo de abstração** da hierarquia de herança.

### Exemplo clássico — ave, pica-pau e pinguim

Uma classe `Ave` implementa `bicar()` e `voar()`. A subclasse `PicaPau` herda os dois métodos sem problema — ambos fazem sentido. Uma função genérica que executa os métodos de qualquer `Ave` funciona normalmente com um `PicaPau`.

Ao criar a subclasse `Pinguim`, o método `bicar()` continua funcionando, mas `voar()` lança uma exceção — o pinguim não voa. Isso quebra o Liskov Substitution: a subclasse não pode substituir a classe base sem quebrar o comportamento esperado.

**Conclusão prática:** se toda subclasse nova exige lançar uma exceção ou "lutar" contra o que ela herdou, é sinal de que a abstração da classe base está errada — e insistir nela tem efeito destrutivo na evolução do sistema. O princípio empurra a pensar no que a classe pai deveria realmente fornecer de comum para todas as subclasses, o que por sua vez ajuda a respeitar Open/Closed — principalmente ao programar contra interfaces, já que a classe base processa qualquer objeto injetado sem conhecer detalhes de implementação, dando liberdade total para novas implementações (o mesmo exemplo do processador de pagamentos serve aqui).

---

## I — Interface Segregation Principle

Clientes não devem ser forçados a depender de métodos que não usam. "Cliente" aqui é a classe forçada a implementar uma interface com métodos que não fazem sentido para ela.

**Ilustração errada:** dois robôs recebem a mesma lista de exercícios — girar ao redor, rotacionar os braços, mexer as antenas. Um dos robôs não tem antena, mas precisa implementar o método mesmo assim (normalmente com uma implementação vazia ou que lança exceção).

**Ilustração certa:** os exercícios (interfaces) são segregados — quem pode girar, gira; quem pode rotacionar os braços, rotaciona; quem tem antena, mexe na antena. Cada robô só implementa o que de fato faz sentido para ele.

Esse princípio é interpretado no vídeo como um reflexo dos três primeiros (SRP, OCP, LSP) aplicado especificamente a interfaces, dando ainda mais flexibilidade ao design.

---

## D — Dependency Inversion Principle

Um módulo não deve depender diretamente de detalhes de implementação de outro módulo — deve existir uma abstração (ex.: uma interface) entre eles.

**Ilustração errada:** um robô diz "eu corto pizza usando o meu braço cortador de pizza" — a ferramenta está fundida ao usuário, como "mãos de tesoura" (Edward Mãos de Tesoura), impossível de trocar.

**Ilustração certa:** o robô diz que corta pizza com qualquer ferramenta que for injetada nele — o braço tem um "soquete" (interface), e qualquer ferramenta que respeite esse soquete pode ser encaixada e usada.

---

## Conteúdos extras citados no vídeo

- Vídeo do próprio canal sobre o design pattern mais usado pelo apresentador (envolve injeção de dependência), incluindo testes automatizados e arquitetura de software, em JavaScript puro mas aplicável a qualquer linguagem.
- Recomendação de um vídeo do canal "código fonte TV" para SOLID em Java.
- Recomendação de um vídeo do canal "Rocketseat" para SOLID em TypeScript.
