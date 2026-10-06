# Introdução à Arquitetura de Software: o que é e conceitos para decisões arquiteturais (Kiper Academy)

Transcrição de vídeo (pt-BR) introdutório de uma série sobre arquitetura backend, do canal da Kiper Academy (apresentador não identificado na transcrição). ASR bruto limpo, pontuado e organizado em seções; conteúdo técnico preservado, sem tradução (já estava em português). Pedidos finais de divulgação (comunidade, roadmap, aulas ao vivo) omitidos. Termos do ASR corrigidos pelo contexto: "Martin Faller/Follower" = Martin Fowler; "Doma" = DOMA (Domain-Oriented Microservice Architecture); "Servas" = serverless; "Versel" = Vercel; "Globaloplay" = Globoplay; "cash" = cache; "indepotência/depotência" = idempotência; "acoblada" = acoplada; "PICP" = provavelmente PicPay (incerto). Os links dos artigos da Shopify e da Uber estão na descrição do vídeo (não disponíveis aqui).

## Abertura

Introdução ao conceito de arquitetura de software, o que é na prática, e alguns conceitos que se deve ter em mente antes de tomar decisões arquiteturais para aplicações backend.

## O que é arquitetura de software

Definição formal: a **organização fundamental de um sistema**: seus principais componentes, as relações entre eles e os princípios que orientam sua construção e evolução. Como a definição é abstrata, o vídeo olha para o **papel** da arquitetura:

- **Dividir o sistema:** o que cada parte faz e quais são suas responsabilidades.
- **Definir a comunicação:** como as partes interagem e trocam informações.
- **Acomodar restrições:** orçamento, prazo, capacidade da equipe, tecnologias disponíveis.
- **Atender qualidades esperadas:** requisitos de segurança e desempenho (ex.: resposta da API com latência de 200 ms como requisito de negócio).
- **Tratar dados:** onde ficam armazenados, quem acessa, como manter consistência, como quebrar em entidades.

Não é preto no branco: autores diferentes dão definições diferentes. Martin Fowler (autor de *Refatoração* e de livros sobre design patterns e arquitetura): arquitetura é *"the shared understanding that the expert developers have of the system"*, ou seja, o **entendimento compartilhado** que os desenvolvedores especialistas têm do sistema (responsabilidades, comunicação, restrições).

## Por que se preocupar com arquitetura

A arquitetura influencia diretamente:

- **Custo de mudança:** tempo da equipe para alterar uma parte do sistema, e custo literal de manter a aplicação rodando (serviços e tecnologias escolhidos).
- **Desempenho:** tempo de resposta, escala, capacidade de lidar com novas requisições e milhões de dados/usuários.
- **Trabalho em equipe:** quantas equipes, quantas pessoas em cada, qual a responsabilidade de cada uma. A influência é mútua: a organização das equipes também influencia as decisões arquiteturais.
- **Complexidade:** um sistema bem dividido (responsabilidades, consistência de dados, comunicação assíncrona) pode ficar complexo demais. Isso dificulta o onboarding de novos desenvolvedores e a investigação de bugs: o bug pode ser só o **sintoma** de uma causa espalhada em outra parte da arquitetura.

Exemplos citados (artigos na descrição do vídeo): **Shopify** (transição de um monolito para microsserviços) e **Uber** (já tinha microsserviços, mas o sistema ficou caótico, com equipes trabalhando com mais de 50 microsserviços ao mesmo tempo; introduziu o **DOMA, Domain-Oriented Microservice Architecture**, microsserviços orientados a domínio, e reduziu a quantidade de microsserviços).

## Arquitetura de que? O problema de definir "aplicação"

Segundo Martin Fowler, as decisões importantes no desenvolvimento de software variam de acordo com a **escala do contexto** considerado. Uma escala comum é a **aplicação** (*application architecture*). Mas não há definição clara de aplicação; depende de quem olha:

- **Desenvolvedores:** um conjunto de código visto como unidade única (ex.: um repositório no GitHub).
- **Clientes:** toda a interface com a qual interagem, mesmo que por trás haja vários repositórios e APIs.
- **Detentores de orçamento (líderes/chefes):** uma iniciativa com verba única (ex.: R$ 100 mil destinados à parte de esportes do Globoplay; para eles a "aplicação" é a parte de esportes, não o Globoplay todo).

Exemplo do **Mercado Livre:** para o cliente, a home é uma única aplicação. Para o desenvolvedor, busca (serviço separado, regras, bancos e microsserviços próprios), banners (time de marketing), corredores (promoções, produtos do dia), carrinho e perfil podem ser, cada um, uma aplicação separada. Para o negócio, "Mercado Play" é uma coisa só, englobando o link na home, os banners de filmes e a plataforma em si. Conclusão: o contexto/limite da aplicação precisa estar **bem definido entre desenvolvedores e negócio** antes de decidir a arquitetura.

## Dimensões das decisões arquiteturais

- **Estrutural:** fronteira de execução da aplicação e formato de deploy. Ex.: microsserviço ou não, event-driven, serverless. Também infraestrutura: serviço hospedado na AWS, front na Vercel, API Gateway no meio, banco Aurora com read replica no Neon porque é mais barato.
- **Design do código:** fronteiras de responsabilidade e dependência *dentro* do código. Padrões como Clean Architecture, arquitetura hexagonal, arquitetura Onion (cebola) e MVC (Model-View-Controller). Às vezes uma decisão de design se combina com uma estrutural (ex.: quebrar o MVC em partes separadas).

**Exemplo (sistema de pagamentos):**
- *Decisão estrutural:* a cobrança é um serviço com deploy independente e se comunica com pedidos por mensagens (ex.: um serviço de mensageria da AWS).
- *Decisão de design:* a regra de cobrança depende de uma **interface de pagamento** global; o **adapter** do provedor (PicPay, Itaú etc.) implementa essa interface. A cobrança não depende diretamente do provedor externo, só da interface; o adaptador é o "carinha do meio" que desacopla.

## Conceito 1: Stateful vs. Stateless

Uma instância (servidor/backend) é **stateful** quando a continuidade do atendimento depende do estado que ela conserva entre requisições; **stateless** quando não exige que a próxima requisição encontre aquele estado local na mesma instância.

- **Stateful:** o servidor guarda em memória informações dos clientes que já fizeram requisição (usuários logados, IPs, ações realizadas) e as usa conforme o usuário navega. Analogia: mostra-se a identidade ao segurança uma vez; da próxima vez ele diz "essa é a Fernanda, pode passar".
- **Stateless:** não exige estado prévio do cliente. O usuário se autentica uma vez (e-mail e senha), recebe um **token** e o apresenta em **toda requisição** (mostra o crachá de novo a cada vez); as únicas informações usadas são as do token.
- **Por que stateless (não é regra):** permite subir **várias instâncias** do mesmo backend, distribuir requisições entre elas e substituir uma que falhe sem interromper o atendimento. Pode-se subir 100 instâncias e depois reduzir para uma sem perder a continuidade.
- **Quando stateful faz sentido:** partida **multiplayer**, em que o servidor mantém o estado do jogador (posição, itens usados) em tempo real; só persistir em banco não adianta. O usuário precisa estar sempre conectado àquela mesma instância.
- Ao desenhar um sistema (ex.: pagamentos), a pergunta é: essa aplicação precisa ser stateful ou stateless?

## Conceito 2: Síncrono vs. assíncrono

Pergunta-guia: **o usuário precisa do resultado final agora ou pode recebê-lo depois?** Ou: consigo fazer tudo necessário agora para gerar o resultado?

- **Síncrono:** o front faz a requisição, o backend a mantém ativa, processa tudo (banco, cálculos) e devolve a resposta; o front espera.
- **Assíncrono:** o backend responde só "200 OK, recebi a requisição" e avisa depois quando estiver pronto. Faz sentido, por exemplo, ao consultar um serviço terceiro de verificação de identidade (CNH/CPF) que demora até 30 minutos: não dá para manter a conexão aberta (nem há timeout que aguente).
- O mesmo vale entre dois backends: ao chamar outra API, preciso da resposta naquele momento (aguardo e reajo ao retorno) ou posso seguir sem ela?

## Conceito 3: Acoplamento

Pergunta-guia: **se eu mudar o componente B, o que vou precisar mudar no componente A?**

Exemplo: sistema de escolas com dois backends/microsserviços, **matrícula** e **cobrança**. A matrícula só libera acesso ao curso depois que a cobrança confirma o pagamento. É uma **dependência de negócio**, ou seja, um **acoplamento legítimo**. O cuidado é restringir esse acoplamento ao **status** (matrícula confirmada porque o pagamento está confirmado; pendente porque o pagamento está pendente), sem que a matrícula interaja com detalhes internos da cobrança: consultar o banco da cobrança, manipular seus objetos, chamar serviços internos.

Exemplo do acoplamento **não saudável:** a cobrança troca o endereço de uma string única (`address`) para campos separados (`street`, `number`, bairro...) e, como a matrícula mexia diretamente nesses campos, é preciso alterar as classes da matrícula. A única dependência real era o status.

Critério para identificar acoplamento não saudável: um problema em uma parte da aplicação **impede outra parte diferente de funcionar**, mesmo sem nenhuma necessidade de negócio entre elas.

## Conceito 4: Idempotência

Pergunta-guia: **se essa requisição ou mensagem chegar duas vezes, o que acontece?** (ex.: a cobrança envia duas vezes a confirmação de pagamento para a matrícula.)

Uma operação **idempotente** permite repetir a mesma operação lógica **preservando o efeito esperado**. Solução comum: uma **chave de idempotência** (um ID/hash gerado, salvo e transitado entre os serviços); ao receber um evento duplicado com o mesmo ID, o receptor sabe que já processou e não reprocessa. **Não é bala de prata:** a implementação ainda precisa tratar **chamadas concorrentes** (duas chamadas ao mesmo tempo) e registrar o resultado de forma confiável.

## Conceito 5: Cache

Pergunta-guia: **quanta desatualização posso aceitar?** Ou seja, por quanto tempo a informação servida pode divergir da fonte de verdade?

O cache mantém uma **cópia** dos dados originais num servidor mais próximo do usuário/mais rápido. Reduz o **tempo de acesso** (ex.: 1 s caindo para 10 ms) e pode reduzir **custo** (cada requisição à origem custa mais). Em contrapartida, a informação é atualizada de tempos em tempos (a cada 1 min, 5 min, 1 h...), então pode haver momentos em que o usuário consulta algo desatualizado.

- **Não aceita desatualização:** saldo bancário. Cliente recebe um Pix de R$ 10 mil, abre o app, vê R$ 0 (cache), se desespera, acha que levou golpe; 5 minutos depois o cache atualiza.
- **Aceita desatualização:** post de blog. Se o autor editar o texto ou adicionar uma foto, o efeito final no leitor não é problemático.

## Encerramento

Vídeo introdutório de uma série sobre arquitetura no canal: cada tema será aprofundado e serão desenhadas arquiteturas de sistemas reais, com casos de empresas. Argumento de carreira: saber tomar boas decisões arquiteturais é diferencial de um bom profissional, em oposição a quem apenas executa a tarefa do Jira.
