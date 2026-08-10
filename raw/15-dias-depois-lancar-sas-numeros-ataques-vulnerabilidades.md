# 15 Dias Depois de Lançar Meu SaaS: Números, Ataques e Vulnerabilidades

*Transcrição de vídeo do YouTube, canal Mano Davin/Mano Deivin ("Boteco de Tecnologia"). Texto reorganizado em parágrafos e seções a partir da transcrição bruta falada, sem alteração de conteúdo ou tradução (já em português).*

## As três descobertas

Quinze dias depois de lançar meu SaaS, o Find My SaaS, eu descobri três coisas.

A primeira é que o projeto vai ser usado desde que funcione. Essa é uma primeira descoberta, porque toda vez você fica com aquela ideia de "vou lançar, ninguém vai mexer, ninguém tá nem aí pro projeto" — e a galera usa. Foi maneiro.

A segunda coisa que eu aprendi foi o seguinte: sempre vai ter alguém tentando hackear o que você faz. Sempre. Não adianta falar "ah, sou solo, projeto pequeno" — se você mostrou para alguém, vai ter sempre um script kiddie, vai ter alguém estudando cibersegurança que vai te usar como exemplo, pode ter certeza. E se você tiver visibilidade — eu tenho um canal no YouTube com uma visibilidade boa — mais ataques você recebe. A gente teve o caso do nosso amigo Abraham, que lançou o Cinema Hub dele e dançou. Então quanto mais visibilidade você tem, mais ataques você recebe. Eu aposto que o Antônio Real Oficial deve receber ataque pra caramba, porque ele tá sempre ativo no X, sempre ativo na comunidade — não precisa nem ter canal no YouTube.

A terceira coisa que você tem que se preparar é que sempre vai ter uma galera que nunca construiu nada, nunca lançou nada, talvez nem seja programador, e essa galera vai estar te ensinando a escalar, te falando uma porrada de feature, tudo que você "tem que fazer". Vai ter uma galera que do nada vira especialista de produto. É foda. A gente tem que tomar cuidado com esses especialistas em PowerPoint. Aconteceu isso também no meu projeto.

Hoje eu quero te mostrar exatamente o que aconteceu em 15 dias: quantos usuários apareceram, qual foi o crescimento, os ataques que ele sofreu, as vulnerabilidades encontradas e, principalmente, dinheiro — porque no final disso, pouca gente mostra número de SaaS. Lembrando: não tô aqui pra vender curso, a galera já me conhece. Se você caiu aqui de paraquedas: não sou vendedor de curso, não tô querendo te vender nada, só compartilhando uma experiência. Não é um SaaS "faturei 100 mil" — faturei uma merreca, mas essa merreca pra mim tá bom, e eu vou falar no final do vídeo.

## Sobre o canal

Se você tá chegando agora: se inscreve no canal, deixa o like, ativa a notificação. Aqui a gente chama de Boteco de Tecnologia — a gente faz resenha. O conteúdo principal são as lives, terça e quinta-feira às 10h, puro suco de resenha sobre mercado e projeto. Segue também no Instagram, @manodeivin, onde a resenha continua.

Contexto: este vídeo é a parte 2 do vídeo em que eu lancei o SaaS. É basicamente um marketplace de outros SaaS — eu brinco que é o "mercadão de Madureira do SaaS". A funcionalidade é pouquíssima, de propósito: você cadastra um SaaS e recebe upvote. Não tem downvote, não tem nada além disso. O endereço é findmysas.com. Como eu monetizo: você pode dar boost tanto no seu SaaS quanto no SaaS de alguém que você acha maneiro — por exemplo, gostei do SaaS do Antônio Real Oficial, pago pra ele ficar em destaque por alguns dias. A ideia é ser um espírito de comunidade: serve tanto pra quem quer contratar outro SaaS quanto pra quem chega pra dar upvote no SaaS de um amigo e acaba descobrindo outros projetos maneiros e contratando. Isso tá funcionando — virou um ecossistema muito maneiro.

## A infraestrutura: uma VPS só

Antes de continuar, uma parada que incomoda muita gente quando a gente fala de lançar SaaS: esse SaaS inteiro roda numa VPS só, da Hostinger. A máquina tem **1 núcleo de processamento, 4 GB de RAM e 50 GB de armazenamento**. De forma simples e enxuta: sem Kubernetes, sem arquitetura de microsserviço, sem multicloud com nome bonitinho, sem arquitetura event-driven. É um monolito rodando ali. Não precisei de milhares de serviços, só uma VPS — e mesmo assim aguentou.

Tem muita gente paranoica que acha "não vai escalar, não vai aguentar". Calma, os números aí embaixo mostram: tivemos mais de 230 mil requisições, isso com ataque incluso, e a aplicação continua de pé. A galera da velha guarda acha que se você não tem uma arquitetura com 15 camadas de infra você não deveria nem subir nada — "como você não tá usando o serviço A, B e C?" Não, cara. A real é que às vezes uma VPS bem configurada resolve o seu problema.

## Os números (Google Analytics)

Peguei aqui o Google Analytics compartilhado — não é conversa fiada, é build in public. Período: últimos 15 dias (gravando em 6 de abril).

- **12.000 usuários ativos / novos usuários**
- **Tempo médio de engajamento: 1 minuto e 43 segundos** (KPI que quero melhorar num próximo passo)
- **178.000 eventos** (cada clique numa página conta como evento)

Nas páginas e telas, os SaaS em destaque na home são os que compraram boost: Jet Cloud, Frub, Riva Pay, Flurinara (Dev The Alert em inglês), entre outros. Dá pra observar a hipótese de que mais visibilidade gera mais clique: por exemplo o Flurinara teve 2.316 acessos e 1.886 usuários que clicaram — e a galera tem dado feedback de que está fechando negócio através da plataforma, o que confirma o ecossistema entre comunidade e comunidade (não é um "Product Hunt", é "entre nós").

Tivemos alguns picos de acesso — um deles bateu na semana anterior, numa sexta-feira, coincidindo com um vídeo novo no canal.

### Origem do tráfego

- **Tráfego orgânico via vídeo (YouTube)**: ~46% — maior fonte
- **Direto**: 19% (3.756 sessões)
- **Busca orgânica**: 14%
- **Referral**: parcela relevante — provavelmente galera que cadastra o SaaS e compartilha o link pedindo upvote (1.976 sessões nessa categoria)
- **Redes sociais (X, LinkedIn, Instagram)**: 7,9% — foi a menor fonte, mesmo com posts nos três
- Outras categorias menores não identificadas com clareza no relatório (ex.: "Organic Shopping")

Nada manipulado, nada pago — tráfego totalmente orgânico.

### Cadastros

Até o momento da gravação (6 de abril, 10h40): **746 SaaS cadastrados**. Desses, 100 foram subidos como mock/estático no lançamento, então o número real de produtos cadastrados organicamente é **646**.

## Dinheiro

No vídeo anterior a meta declarada era R$ 2.000/mês — o suficiente pra cobrir os custos baixos da VPS e assinar o Claude Code (a grande dor era "quero grana pra assinar o Claude Code Max"). O que sobrasse iria para a obra da chácara.

A realidade veio diferente. Usando o **List MRR** (produto de um amigo, que lista faturamento via chave de leitura do Stripe — nunca uma chave de escrita, mesmo confiando no dono da ferramenta, porque não dá pra saber se os dados vão vazar) é possível ver o ranking de faturamento: tem gente faturando mais de R$ 4 milhões, outro caso (André Dev) já faturou R$ 87.000 com produtos de SaaS.

O Find My SaaS aparece no ranking com **R$ 4.819,00 de faturamento em 15 dias**. Não foi um caso "Abraham" (que declarou R$ 200.000), não foi um produto do Thiago Finch — foi um projeto humilde lançado pra comunidade.

Isso não significa largar o emprego de dev. Motivos:

1. **Efeito novidade** — a galera contrata, experimenta e conhece agora; esse efeito tende a cair nos próximos meses, e o valor atual provavelmente não é sustentável tal como está.
2. **Bagagem de produto/startup** — não há emoção desproporcional com o número: ele superou a expectativa (mais que dobrou), mas isso é tratado com cautela.
3. **Sem funil, sem tráfego pago, sem "copy milagrosa", sem curso de lançamento** — o único esforço de marketing foi falar do projeto nas lives.

O ponto mais importante não é o valor, é o comportamento: gente comprando SaaS através da plataforma, descobrindo soluções que nem o próprio autor conhecia (ex.: um "Duolingo pra dev", ferramentas de monitoramento em tempo real, uma ferramenta que previne chargeback com notificação no WhatsApp a cada compra). Ao mesmo tempo, muita gente descobriu o Find My SaaS. Quando entra dinheiro dos dois lados, o experimento vira produto — "produto de comunidade, produto da humildade".

## Os ataques

Junto com o dinheiro vieram os ataques: mais de 234.000 requisições, boa parte suspeita de DDoS malicioso — **157 tentativas maliciosas bloqueadas segundo o Cloudflare**. Não é só bot: tem gente testando no limite, tipo "vamos ver se derruba". Toda vez que o projeto é citado na live, em menos de 5 segundos o gráfico do Cloudflare dispara com tentativas de DDoS.

Isso já era esperado, porque a máquina mínima (1 núcleo, 4 GB) foi escolhida de propósito, para descobrir se o MVP aguenta porrada. Apesar de tentar tratar as vulnerabilidades, deu muito medo — inclusive foi essa uma das razões para manter o SaaS com o menor número possível de informações/features: medo de vazamento de dado. Até o momento do vídeo, nenhum vazamento ocorreu.

## O pentest e a vulnerabilidade crítica

Durante uma live, com o dashboard de monitoramento aberto ao lado, um inscrito do canal mandou um relatório de pentest — **Márcio Mendes**. Vários outros também mandaram e-mails com vulnerabilidades pontuais, mas o relatório do Márcio foi o mais relevante: **12 vulnerabilidades encontradas, incluindo uma crítica**.

A vulnerabilidade crítica: o **login via Google OAuth aceitava parâmetros extras na URL** sem validação — ou seja, era possível montar um link malicioso que pedia permissões (escopos) além do que o Find My SaaS normalmente solicita (que é só e-mail, nome e foto do usuário). O fluxo não tinha checagem sobre o que estava sendo passado via URL. Um atacante poderia:

1. Pegar a URL legítima de login do Find My SaaS.
2. Adicionar parâmetros de permissão extra.
3. Embutir esse link modificado num SaaS de terceiro malicioso.
4. Quando a vítima clicasse e aceitasse as permissões, o token de autenticação vazava pela URL — permitindo ao atacante capturar esse token e autenticar-se usando as credenciais/API keys da vítima.

Segundo a explicação recebida, o erro técnico de fundo não era exatamente "do lado" da aplicação — era confiar demais no input do usuário (e, por extensão, confiar que ninguém tentaria manipular a URL). Não houve vazamento nem exploração real registrada — foi identificado via pentest responsável antes de qualquer exploração maliciosa conhecida. As vulnerabilidades relatadas, incluindo a crítica, já foram corrigidas.

## "Especialistas de PowerPoint" e o ruído de feedback

Enquanto isso, apareceu algo mais perigoso do que as vulnerabilidades técnicas: as ideias. Gente do nada virando especialista, mandando mensagem no LinkedIn, feedback por e-mail, DM no Instagram, sugerindo "faz um sistema de afiliado", "faz um split de pagamento", "cria uma comissão sobre venda" — tentando transformar um CRUD simples de listagem de SaaS num TCC.

O exemplo mais absurdo: alguém mandou um e-mail longo sugerindo reescrever o projeto em TypeScript, com a justificativa de que Ruby é "fracamente tipado" e deveria ser trocado por uma linguagem "fortemente tipada". Resposta: se fosse trocar de stack por tipagem forte, a escolha nunca seria TypeScript — seria algo como Java. Não dá pra trocar de stack só porque alguém acha "legal". Esse tipo de escuta indiscriminada é perigosa: se você escutasse todo mundo, o projeto nunca teria existido.

Feedback é um presente — você aceita ou não. É preciso ter objetivos e KPIs mentais próprios e filtrar: o feedback de quem nunca lançou nada, talvez nem programador, e acha que o que aprendeu num curso é a verdade absoluta, é descartável. O feedback que importa é o uso real, o dinheiro entrando, o usuário dizendo "tô fazendo venda com isso".

## Filosofia por trás: execução, não arquitetura

O projeto não é sobre stack ou arquitetura vistosa — é sobre execução. A abordagem segue os conceitos do livro *A Startup Enxuta* (Lean Startup) na prática: construir rápido, colocar no ar, medir, ajustar — sem esperar nada perfeito e sem tentar prever todos os casos possíveis. Isso não significa lançar sem nenhum cuidado: é preciso conhecimento suficiente para entregar algo minimamente seguro, ciente dos riscos que se está correndo e com um plano pra mitigá-los.

Recomendação para quem está fazendo vibe coding sem saber programar: mesmo sem contratar um dev, contrate um pentester antes de lançar — ao menos alguns problemas serão resolvidos antes de virarem incidente. Cita-se de novo o caso do Abraham, que deixou o `.env` visível publicamente e teve a base de dados inteira exportada por terceiros — o tipo de falha que tira o cliente todo de uma vez.

Ao entregar algo minimamente OK, na forma mais "raiz" de MVP, vem tudo junto: crescimento, bug, crítica, ataque — mas também o que importa, que é feedback real, uso real, dinheiro entrando.

## Próximos passos

Criar um backlog guiado por métrica: aumentar cadastro (medir tempo de cadastro e taxa de desistência), aumentar retenção (hoje em 1min43s no Google Analytics) e aumentar receita — sem ilusão, sem pressa, sem querer virar milionário e sem a intenção de, depois, vender curso ou mentoria em cima disso. O objetivo é gerar renda suficiente para reinvestir em ferramentas (como o Claude Code Max) e criar outros produtos, testando o caminho de se tornar indie hacker.

## Encerramento

Agradecimento a Márcio Mendes pelo pentest. Convite para quem precisar de recomendação de pentester entrar em contato por e-mail (contato@manodeivin.com.br). Chamada para o cupom de desconto na Hostinger (link na descrição/comentário fixado), referência ao vídeo anterior (parte 1) sobre a construção do SaaS, e convite para as lives de terça e quinta-feira às 10h.
