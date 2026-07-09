# Tipos de Deploy

Hoje a gente vai falar sobre os diferentes tipos de deploy. A gente vai começar esse vídeo diferenciando deploy de release, porque são 100 coisas diferentes — é importante notar essa diferença. A gente vai falar sobre deploy manual, deploy automático, vamos falar sobre os três principais tipos — quatro, na verdade, principais tipos — e mais alguns outros menos conhecidos. Vamos falar sobre Recreate, Rolling, Blue/Green e Canary. E de onde vem o nome do termo Canary: é uma alusão a levar canários para minas, para mineração.

Antes disso, quando você for fazer algum tipo de deploy, eu recomendo que você faça na parceira do canal, a HostGator, que tá patrocinando o vídeo de hoje. A HostGator tem várias soluções interessantes, faz muito sentido usar eles — questões de hospedagem de site e tal, a gente já mostrou aqui no canal também, eu usando, e foi bem legal. Tem o OpenClaw pré-instalado, você consegue uma VPS com OpenClaw para rodar de maneira muito fácil, a instalação é super simples e funciona super bem. Eu gosto bastante da VPS deles, o preço é muito competitivo, em reais, para você ter servidores no Brasil — a latência para seus usuários vai ser provavelmente muito baixa — e você consegue customização completa. Você pode escolher diversos tipos de VPS: uma máquina mais crua para você configurar, ou um sistema operacional com um painel (tipo cPanel), ou já pré-configurada para rodar OpenClaw ou N8N, ou uma com Docker, que facilita muito para você subir os seus serviços. Se você tá planejando hospedar um projeto pessoal, um site, um portfólio, recomendo ver as soluções da HostGator — link na descrição, avisa que veio do canal e ganha uma oferta especial. Já vi gente hospedando SaaS que fatura R$20-30 mil nessas VPSs pagando um custo baixíssimo.

Vamos lá que esse vídeo vai ser bem legal.

## Deploy vs. Release

Primeiro eu quero te explicar qual que é a diferença de deploy e release. Para muitas empresas, digamos, um pouco menos maduras, é a mesma coisa — mas não precisa ser.

Imagina que na esquerda você tem sua codebase, hospedada tipo no GitHub, e na direita você tem sua VPS (vamos imaginar a VPS da HostGator). Seu código vai estar duplicado dentro da VPS. Só que pode ter, por exemplo, uma feature nova, partes novas do código que ainda não estão ativadas — imagina que isso está escondido atrás de uma feature flag. Seus usuários estão mandando tráfego pro servidor, mas essas linhas de código novas que você escreveu não estão rodando, estão escondidas atrás de uma feature flag. Nenhum usuário está vendo essa release.

Alternativamente, sem pensar em feature flag: você pode ter duas instâncias rodando, uma com código antigo, outra com código novo. Você fez o deploy — o código está na máquina, está no servidor — mas todo o tráfego do usuário ainda está rodando no código e nas features antigas. Então você consegue fazer um deploy sem fazer um release: lançar o código para a máquina sem que esse código afete os usuários. Isso é importante notar.

## Deploy Manual vs. Deploy Automático

A primeira maneira mais simples de fazer deploy, e a primeira que você deve aprender, é o deploy manual: mover o código pra máquina onde ele vai poder ser executado e entregar valor pros usuários. É você atualizar o servidor com código novo.

A diferença entre deploy manual e automático é que no manual, quando você chegar numa versão que quer fazer o deploy (você foi incrementando o GitHub, fez um commit, outro commit, uma branch, deu merge na main, chegou no commit tal e falou "gostei dessa versão, vamos puxar pro servidor"), você faz isso manualmente. Existem diferentes maneiras de fazer o deploy. Geralmente quem faz deploy manual: dá SSH na máquina (VPS ou servidor), puxa o código (`git pull` ou `git clone`), sobe a aplicação (`npm start`, simplificando). Já trabalhei em lugares que faziam isso com FileZilla — uma gambiarra tremenda. Já trabalhei em lugares em que rodava um script shell na própria máquina que conectava no servidor (e precisava estar na VPN).

O deploy automático segue uma série de regras — geralmente você tem uma pipeline que é "triggada" quando algo acontece. O mais comum: quando você faz merge de algo na main, fechou um pull request pra main com código atualizado, existe uma pipeline que vai rodar alguns scripts — pode muito bem ser um simples SSH pro servidor e um `git pull` + `npm start`. A pipeline pode reproduzir exatamente aquilo que você faz manualmente. A diferença entre deploy automático e manual não é o que está sendo feito, é qual o trigger/gatilho que causa esse deploy.

Atualmente as empresas mais organizadas têm visto que deploy automático é melhor — é menos propenso a erro humano, essa é a grande vantagem. Como é "triggado" baseado em alguma regra, é difícil esquecer de fazer um deploy, e você pode reforçar proteções adicionais (ex: "se os testes não passaram, o deploy não acontece"). Hoje existem diversas ferramentas para pipeline — muito comum usar uma combinação de GitHub Actions mais algum outro ferramental (Docker, Kubernetes, Jenkins, etc.). O número de ferramentas aqui é gigantesco, então não dá pra generalizar — pode ser GitHub Actions, pode ser GitLab com uma ferramenta externa monitorando a branch main, funciona perfeitamente bem.

## Tipos de Deploy

### Recreate

É o mais comum — se você não pensou muito sobre o que está fazendo, provavelmente está fazendo um Recreate. Dentro do servidor você tem uma instância da aplicação rodando (ex: Node/Express ou FastAPI). O Recreate é a forma mais simples e óbvia: você tem a V1 rodando, quer passar pra V2. Você dá shutdown na instância (desliga), e dá start na V2 (sobe o código novo, `npm start`).

O que acontece: os usuários estavam enviando requests pro servidor. Em algum momento você desliga um e sobe o outro — e enquanto o start está acontecendo (não é instantâneo, mesmo que rápido), os requests são perdidos. Se você estava servindo na porta 3000, desligou o que ocupava a porta, subiu outro na mesma porta — nesse meio tempo, entre desligar e subir, os requests foram perdidos. Os usuários vão experienciar downtime.

Antigamente esse tipo de deploy era super comum: janela de manutenção ("o site vai ficar em manutenção das 9 às 10 da noite"), você acessava o servidor às 9, baixava código novo, deletava o antigo, criava a build, subia, e vida que segue. Hoje em dia não é mais tão comum.

### Rolling Deployment

Imagina que numa máquina você tem várias instâncias da aplicação rodando, ou várias máquinas/servidores (um cluster). O Rolling substitui uma por uma: se você tem quatro instâncias e dropa uma, ainda consegue servir os usuários sem problema — e aí você pode adicionar V2 no lugar. Você vai ter, por exemplo, três instâncias rodando V1 e uma rodando V2, depois deleta outra V1 e sobe V2, e assim vai "rolando".

A grande dificuldade do Rolling: (1) alguns usuários vão cair na V1, outros na V2 — inevitável por um curto período, então é importante que V1 e V2 sejam absolutamente compatíveis com o que o usuário espera; (2) mais importante ainda, as requisições vão pro banco de dados, e é muito importante ter compatibilidade também com o banco. Se você vai fazer uma migração no banco e subir V2, lembre que V1 vai continuar rodando por um tempo, então precisa estar compatível.

### Blue/Green Deployment

Um dos meus favoritos. O Blue é a V1, e todo o tráfego é mandado pra V1. Em paralelo você sobe a Green (V2), deploya, bota pra rodar, tudo certo para receber usuários. Você faz testes na Green — stress test, teste de carga, acessa e vê se está funcionando — e quando estiver tudo pronto, você simplesmente direciona o tráfego dos usuários pra Green.

Vantagens do Blue/Green: na prática não existe downtime — é só o tempo de mudar o tráfego de um lado pro outro. E na prática, você vai ter Blue e Green rodando em paralelo, então se por acaso precisar de um hotfix/rollback (já aconteceu comigo — fiz um deploy que causou o servidor ficar inacessível por uns 10-15 minutos), em Blue/Green você simplesmente redireciona o tráfego de volta pra Blue. Muito bom. A grande vantagem do Blue/Green é esse rollback facilitado. O custo: por um período você tem que ter as duas versões rodando em paralelo — é um setup um pouco complexo em termos de infra e ops.

### Canary

Pode ser implementado de diferentes maneiras. A ideia: um certo percentual de usuários vê a versão nova (quase como beta testers), e a maioria vê a versão antiga. Pode ser feito com duas instâncias tipo Blue/Green, com 5% dos usuários vendo a versão nova e 95% a antiga. Se tudo estiver dando certo, aumenta para 25/75, e vai aumentando até 100% na versão nova.

Existe uma maneira que não é mais Canary deployment, é mais um release — o que a Meta gosta de chamar de "massive rollout at massive scale" — em que você segrega usuários em grupos e mostra determinadas features escondidas atrás de feature flags para alguns usuários. Isso é possível, mas aí não é Canary deployment, é mais um Canary release (release através de feature flag). O jeito mais tradicional é falar de instâncias diferentes mesmo.

Vantagem do Canary: quando você tem 5% dos usuários vendo, se existir um bug, ele afeta só 5% — você consegue pegar o bug e voltar pra versão antiga (rollback) tranquilamente. Desvantagem: o setup é complexo, precisa da compatibilidade novamente entre ambas as versões (pelo menos com o banco de dados), e pode ser difícil de debugar quando 5% dos usuários reportam um problema e os outros 95% não — pode ficar obscuro. Canary é sobre reduzir risco, usando um percentual pequeno de usuários.

### A/B Deployment

Existe algo quase igual ao Canary que é o deployment do tipo A/B: percentuais dos usuários veem uma feature, percentuais veem outra. Isso não é para reduzir risco técnico, é para ver se, por exemplo, um checkout novo vende mais. Se vender mais, migra pra versão nova; se não vender mais, esquece ela.

### Shadow Deployment

Muito bacana. 100% dos usuários fazem requisições pra V1. A sacada: você sobe uma V2 que nenhum usuário está vendo, e esses mesmos requests são duplicados/replicados na V2. A versão nova também processa esse tráfego, para você ver se não vai dar bug, se responde corretamente as requests, monitorar tempo de resposta, ver se está gerando erro novo no Sentry. Você valida a V2 com clones do tráfego real — mede exatamente como os usuários usam a aplicação, para ver se a nova versão é capaz de lidar com o tráfego 100% real. Excelente, mas é um dos mais complicados de fazer, e um dos mais caros. Para sistemas com side effects (ex: enviar e-mails) fica mais complicado — tem que resolver a questão do banco de dados também: duplicar o banco, ou mockar o banco de dados? São questões complexas.

Esses são basicamente os principais tipos de deployment que existem.

## Continuous Deployment

É mais um conceito que pode utilizar essas diferentes estratégias: todas as mudanças que passam nos testes vão sendo continuamente enviadas — toda alteração de código que passa nos testes é deployada continuamente. Como esse deploy vai acontecer depende da estratégia adotada — pode ser qualquer uma dessas, mas geralmente se parece mais com Rolling (acredito que seja o mais comum).

## Serverless

Quando você faz deploy em ambiente serverless, muitas vezes você não está administrando esse tipo de coisa diretamente. Quando você deploya numa cloud que fornece um serviço serverless, a cloud vai basicamente, em algum momento, "flipar" um direcionamento e mandar as requisições pra versão nova do serviço — quase como se fosse um Recreate instantâneo, ou um Blue/Green. Claro, você pode configurar uma pipeline que faz isso de forma diferente (A/B, Canary) — nada impede implementar essas coisas no serverless. Mas geralmente quem tem serviços simples usando serverless está fazendo um deploy estilo Recreate mesmo, e fazer rollback pra uma versão antiga também costuma ser rápido em serverless.

---

Sobre tipos de deploy, era isso. Se você quiser, comenta qual desses você quer ver na prática — pretendo fazer um vídeo mostrando Blue/Green deployment com a VPS da HostGator.
