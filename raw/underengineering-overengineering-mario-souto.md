# Under-Engineering vs Over-Engineering — Mário Souto

**Formato:** Transcrição de vídeo do YouTube (português, limpa e pontuada — transcrição automática, sem tradução necessária)
**Autor/canal citado na fala:** Mário Souto (nome do canal mencionado na fala soa como "canal da Absolut" — provável erro de transcrição automática, não confirmado)

---

Olá pessoal, eu sou Mário Souto, seja muito bem-vindo a mais um vídeo aqui do canal. No vídeo de hoje você verá um papo sobre *under-engineering* — basicamente a arte de fazer menos do que você deveria — versus fazer mais do que você deveria (*over-engineering*), e lidar com o sofrimento disso todos os dias.

Esse vídeo aqui começou com um tom de reclamação porque eu já passei por algumas dessas dores. Então vou pedir para você deixar o seu like para ver mais vídeos de depoimento sincero como esse aqui e a gente trocar uma ideia nos comentários.

## O ponto de partida: um tweet sobre os extremos

Para embasar esse vídeo, eu peguei um tweet dessa pessoa, um card, que fala de alguns extremos de desenvolvimento que dão errado — tanto de under-engineering quanto de over-engineering, basicamente a definição que eu falei: no under-engineering você normalmente vai fazer menos do que precisa.

## Exemplo prático: construir um formulário do zero ou usar uma lib pronta?

Um bom exemplo que eu consigo dar aqui — é uma discussão que até eu puxei esses dias — é tipo: você começa um projetinho novo na empresa, é só um formulário, você só precisa pegar um dado e mandar. Você pode criar toda a estrutura de manipular o formulário do zero, ou pegar bibliotecas prontas para fazer isso.

Quando você cai numa situação dessas, as pessoas vão olhar de forma diferente: umas vão falar "seu objetivo é simples, você pode fazer tudo do zero"; outras vão falar "mas você não sabe até onde esse projeto vai crescer, pode usar alguma ferramenta para te ajudar, algum framework do gênero".

Hoje em dia eu sou meio categórico na resposta: eu diria para você usar alguma coisa que tenha documentação e que não seja você que criou. Por exemplo, se você vai fazer um formulário: não faça ele puro, procure alguma lib que já exista que faça essa parte de gerenciamento de formulário. Se você for usar o React, procura pelo React Hook Form, por exemplo, ou até mesmo pelo Formik, que é uma outra lib popular.

Por quê? Porque normalmente, se você for criar o seu próprio jeito de fazer formulário, eu tenho certeza que, de todas as opções, você na hora vai estar criando um legado. "Ah, Mário, mas eu só tenho um campo que eu preciso validar" — mas eu vou dar um outro caso aqui: vamos partir do ponto que você só precisa fazer esse formulário do seu trabalho.

## O tweet: sinais de over-engineering e under-engineering

Voltando ao card que eu trouxe: ele coloca como sinais de over-engineering coisas como usar prematuramente microsserviços e micro-frontends, ignorar o YAGNI (a regra que eu conheço como "You Aren't Gonna Need It"), otimização prematura, apresentações excessivas, especulação de features — o que cai um pouco nesse papo que a gente tem aqui — e ter 100% de cobertura de teste.

Do lado de under-engineering, o card lista, entre outras coisas: tight coupling (fortemente acoplado), hardcode de valores, ausência de checks automatizados e de validação de erros, código copiado e colado sem estrutura, e falta de flexibilidade suficiente. Alguns termos do card ficaram difíceis de identificar com precisão na transcrição do áudio — deixo para os comentários quem souber complementar.

## "Beautiful screate" / suporte a navegador e polyfills

Um ponto do card que eu acho super importante — mesmo transcrito com imprecisão aqui — é a questão de suporte a navegador. Por mais que você esteja fazendo somente um formulário, você vai cair numa treta que eu já trouxe num vídeo anterior aqui do canal, sobre como começar com React em 2033 (piada): você fatalmente vai querer dar suporte a navegadores mais antigos, e se você fizer na unha, sem nenhuma estrutura de algum framework por trás, você provavelmente não vai ter estrutura de polyfill cobrindo as features de linguagem que você está usando no projeto — coisas como `structuredClone` e outras funções mais recentes. O `Array.prototype.map`, por exemplo, se não me engano não roda no IE10/IE11. Hoje o suporte a navegadores antigos é cada vez menor, mas ainda assim a gente não pode ignorar, porque é comum uma pessoa já querer usar recursos novos sem ter consciência do que está abrindo mão ao construir um projeto do zero.

Essa parte de build é o ponto que eu trouxe do formulário: vale mais a pena não construir do zero e usar alguma ferramenta que já resolve isso. O mesmo vale para CSS — usa o Tailwind CSS, por exemplo, em vez de reinventar.

## Novidade tecnológica: cuidado ao introduzir sem necessidade

Calma, respira: se na empresa que você trabalha não existe uma tecnologia padrão para fazer interface (como Vue, React ou algo do gênero), aí faz sentido você escolher uma, só pelo ponto de ficar padronizado e qualquer pessoa conseguir usar fácil. Mas se já existe um padrão, prefira usar combinações de ferramentas que já têm referência e exemplos prontos — como o próprio Next.js, que já traz exemplos de setup — do que criar tudo do zero. Criando tudo do zero, fatalmente vai dar errado em algum ponto e você não vai ter nenhuma referência para se apoiar.

## Under-engineering é mais comum que over-engineering

Quero trazer um ponto: essa parte de under-engineering é, na minha visão, mais comum nos projetos do que over-engineering. A gente fala de over-engineering quando o projeto é mais complexo, mas até um projeto simples — até mesmo esse formulário que você está fazendo — se você faz tudo na mão, uma hora pode ser que alguém sobrescreva algo nesse projeto sem que você saiba, ou tenha algum bug em produção enquanto você está fora de casa, e a outra pessoa não consiga gerar um novo build/deploy.

### Exemplo pessoal: projeto DevSoltinho (Discord)

Hoje eu tô construindo um projeto que se chama DevSoltinho, que faz parte de um Discord que eu mantenho com a galera (link na descrição para você participar). Esse projeto está hospedado na Vercel. Qualquer pessoa que faz parte do time — eu pago a versão Pro da Vercel para poder usar times — poderia vir aqui, pegar uma versão antiga do deploy e fazer um redeploy. Só de usar uma ferramenta que me dá essa estrutura, mesmo sem eu ter programado isso, por cerca de $20/mês eu tenho um pipeline de deploy previsível funcionando, o que me permite controlar meus ambientes de deploy considerando a quantidade de coisas que tenho — vale muito a pena no meu caso.

Além da Vercel para deploy, uso o Supabase como serviço de banco de dados. Um dos pontos que quero trazer nesse vídeo é a importância de automatizar processos que dão trabalho. Se você está com dificuldade de mexer em alguma parte da infraestrutura ("back Angel", possivelmente "backend" mal transcrito), vale a pena conversar com o time sobre usar uma solução mais pronta, "de caixinha", que você consegue plugar — mas já pensando em como você sai dela também, e não confiando cegamente na estrutura só porque ela existe. Se você for subir um banco do zero, provavelmente não vai saber configurá-lo direito, e o mesmo vale para outras peças de infra.

Sempre que a gente está criando tudo do zero, a gente perde muito tempo — e vai ter que reconstruir depois. Se você puder ter uma parte pronta, com a melhor qualidade possível, isso ajuda bastante.

## Code review

Se você tiver sozinho no projeto, realmente não vai ter review — mas é importante ter a cultura de code review no time. Eu já fiz uma live aqui no canal sobre isso, vale a pena dar uma olhada.

Coisas que aparecem em review e se relacionam com essa discussão de under/over-engineering:
- ter tipos genéricos demais (`any` no TypeScript) em vez de tipos específicos;
- não ter tipos robustos no código, especialmente ao trabalhar com classes numa linguagem mais orientada a objetos — ficar passando muito tipo primitivo de um lado para o outro em vez de usar um enum, por exemplo, com os tipos de pagamento que você tem, ao invés de passar como string.

## Hardcode e variáveis de ambiente

Essa parte de hardcode é um ponto super importante. Por exemplo, no meu projeto, na camada de acesso ao banco de dados, os valores de configuração (mesmo os que eu consigo trocar fácil, como chaves públicas que vão para o navegador) estão todos como variáveis de ambiente. Configurando essas variáveis de ambiente direto no painel da Vercel (nas settings do ambiente), eu consigo, sem precisar mexer no código, mudar um valor e disparar um novo deploy da aplicação, que vai carregar esse valor novo. Isso inclui, por exemplo, a chave da OpenAI que eu uso para outro vídeo recente do canal.

O que eu tento trazer aqui é como, na prática, algumas dessas coisas acabam entrando no seu código. Eu sei que às vezes você está num projeto mais corrido e quer fazer mais rápido — mas o "mais rápido" é muito relativo: ele é mais rápido no momento em que você está fazendo, porque pode ser que daqui a três dias dê um problema, e você vai pagar por esse "mais rápido" que fez três dias atrás. É aí que a gente começa a cair na questão de débito técnico.

## Acoplamento (tight coupling)

Um dos pontos que o card trazia era tight coupling — você estar fortemente acoplado no seu código, o sistema muito emaranhado. No meu projeto, por exemplo, tenho muito claro a parte de banco de dados e a parte de autenticação — coloquei todos os tipos de autenticação num arquivo só, mas eu poderia quebrar isso um pouco mais. O ponto importante que eu tentei seguir: se esse arquivo é o arquivo de login, eu evito colocar coisas de criar conta junto — a parte de criação de conta deveria estar numa parte separada, tipo "account creation". É um pouco filosófico isso; conforme você vai trabalhando nos projetos, você vai vendo que existe uma separação natural das coisas, mas é importante pensar nessa questão de acoplamento — e isso é algo que você só desenvolve praticando e codando mesmo, não tem muito como fugir disso.

## Copiar e colar, flexibilidade e falta de validação

Sobre ficar copiando e colando código: em alguns casos faz sentido, não vou entrar muito nesse detalhe aqui. Sobre "flexibilidade suficiente" e "não ter checks automatizados e validação de erros" — eu colocaria isso muito na conta do próprio ambiente de CI.

## CI: lint e testes automatizados

Se você for olhar a versão que eu tenho pronta e a que fiz nesse projeto, eu uso GitHub Actions, e não é difícil ter suporte de teste e lint. No repositório, na pasta `.github`, tenho os workflows: um workflow de lint e um workflow de teste — são cerca de 31 linhas para rodar o lint e o teste automatizado.

Para isso aparecer como check obrigatório no pull request, eu vou nas settings do repositório, na parte de branches, e adiciono uma regra de proteção para a minha branch principal, exigindo pull request antes de fazer merge de código, e exigindo que os checks de status passem. O nome que passei no GitHub Actions (lint e teste) é o que aparece ali como obrigatório. Só de configurar isso uma vez e salvar, da próxima vez que eu abrir um PR essa estrutura já aparece.

## Fechamento: onde pegar exemplos de setup

O ponto que quero trazer com tudo isso: qualidade é uma coisa que você pode ter no seu projeto sem estar fazendo de menos (under-engineering) ou fazendo de mais (over-engineering) — você tem uma base, um caminho mínimo para trabalhar. E acho que o setup é a parte mais difícil.

Então, no final, eu quero te dar um caminho de onde você pode pegar alguns exemplos de setup que eu fiz para você copiar e trazer para o seu projeto. Por exemplo, no meu projeto, na parte web, tenho um arquivo `.eslintrc` que importa a configuração de lint base do projeto. No seu projeto, você vai precisar ter um arquivo de configuração de lint parecido, e um comando para rodar o lint — copiando essa estrutura, o lint vai funcionar. O meu setup de testes funciona não só para web, mas também para app, para extensão de navegador, entre outros.

Espero que esse vídeo tenha feito sentido para você, espero que você reflita sobre o quanto você tem feito dessas duas coisas (under-engineering e over-engineering) nos últimos projetos que trabalhou. A gente se vê no próximo vídeo, aqui fica o meu abraço, valeu, falou, e fui.
