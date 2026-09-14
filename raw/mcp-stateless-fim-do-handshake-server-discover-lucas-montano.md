# MCP Stateless: Fim do Handshake e Server Discover (Lucas Montano)

- **Tipo:** transcrição de vídeo do YouTube, colada diretamente pelo usuário no prompt
- **Autor (inferido pelo conteúdo):** Lucas Montano (auto-referência explícita no fechamento: "bota no YouTube aí Lucas Montano ou melhor Techfounder Lucas Montano"; cupom de patrocínio "Lucas Montano" para Hostinger, mesmo padrão recorrente de vídeos anteriores dele já na wiki)
- **Idioma original:** Português — sem necessidade de tradução
- **Tema:** mudança recente na especificação do Model Context Protocol (MCP) da Anthropic, que remove o handshake stateful do protocolo e o torna stateless no core, com um novo método obrigatório `server discover` e headers dedicados para roteamento de método/recurso

---

## Transcrição

Lembram quando lançaram o MCP e a gente entrou numas "noias" de que a gente não ia mais precisar implementar REST ou qualquer API request, que agora as IAs iam se comunicar umas com as outras todas através de MCP? Pois é, esse futuro não veio — ou talvez ele tenha demorado, assim como o QR Code demorou. Vocês lembram disso? O QR Code não era famoso quando lançaram, demorou muitos anos pra gente de fato começar a utilizar. Então precisou de várias iterações na tecnologia.

E a Anthropic, semana passada, divulgou uma mudança bem forte no MCP. Então, basicamente, para quem tem interesse sobre Model Context Protocol: a Anthropic tá matando o handshake do MCP. Obviamente, o teu servidor remoto agora é só um POST que roda em qualquer máquina. Uma das coisas mais complicadas que tinha para implementar o MCP e hospedar ele é que os MCPs eram **stateful** — stateful é quando uma aplicação armazena dados de contexto entre requests. Então tu tem múltiplos usuários fazendo requests e essa aplicação pode segurar alguns estados, por isso a gente fala que é stateful.

A mudança principal do MCP vem nisso agora: a especificação do protocolo passa a ser, no seu core, **stateless**, o que facilita pra gente fazer deploy e escalar em servidores remotos. Eu nem sei se a Anthropic tá utilizando isso, mas recentemente no Claude Desktop App eles divulgaram que agora tu consegue rodar aquelas tarefas do teu "cowork" na nuvem.

Então o que eu quero te mostrar nesse vídeo é falar um pouco dessa mudança e implementar o MCP com vocês. Vou fazer isso na minha VPS da Hostinger, que tá apoiando esse vídeo, onde eu hospedo a maioria dos meus projetos e onde também faço vários experimentos como esse, de testar uma nova tecnologia — porque, não sei tu, mas eu acredito que essa é a forma mais fácil que tem de aprender algo novo.

### Dados atualizados

MCP superou **400 milhões de downloads mensais** do SDK — quatro vezes mais que este ano — e hoje já é um padrão da indústria. O MCP tá se movendo de uma especificação de protocolo bidirecional e stateful para uma especificação mais simples, de request/response. Isso significa que os servidores MCP agora podem ser deployados **serverless** e também numa infraestrutura de edge. Isso simplifica a experiência de construir um MCP server para o cloud e escalar o uso dele.

E a adoção — como eu falei, o problema de qualquer nova tecnologia/protocolo é a velocidade com que as pessoas adotam. Vejo com bons olhos essa mudança. O Cloud [Claude] agora tem **950 MCP servers**, e MCP apps fazem com que o servidor consiga renderizar interfaces interativas. Inclusive eu tô a fim de lançar o MCP do meu app (PSUA) pro Cloud, porque os usuários vão conseguir, por exemplo, manipular suas sessões, buscar informações através desse MCP.

### Server Discover

Temos um novo método chamado **server discover**. O servidor é obrigado a implementar; o cliente só chama quando for necessário. Ele serve para anunciar, por exemplo, a versão, as capabilities que ele suporta, a identidade, e por aí vai. Se tu não chamar, ou mandar direto uma versão errada, o servidor te retorna um erro de versão.

### Por que isso importa para quem paga um servidor

"Remote MCP servers effectively become standard HTTP endpoints which scale cleanly with enterprise workloads." Basicamente, tu não tem mais aquelas sessões no protocolo de MCP, nem o "protocol-specified durable object". Antes, seguindo a especificação, tu precisava de uma camada de sessão — isso exigia um Redis da vida, sticky session, session store — e tudo isso é gasto, e muitas vezes te impede de rodar em determinadas infraestruturas.

### Patrocínio — Hostinger

[Bloco patrocinado] Para fazer esse deploy vou usar a Hostinger, parceira do canal. Tenho um plano **KVM2**, o mais popular deles. Junto da infraestrutura pra construir teu projeto, tu conta com proteção contra DDoS, firewall alimentado por IA, snapshots em tempo real e backup semanal automático, caso precise de rollback. Se teu projeto roda em Docker, tu consegue fazer o deploy dele numa VPS da Hostinger com facilidade — eles têm Docker Manager gratuito incluso. Escolhe o melhor plano de VPS na Hostinger e implanta teu app Docker. Link com desconto na descrição; cupom **Lucas Montano** dá 10% de desconto extra do que já tem no site.

### Headers: método e recurso obrigatórios

Agora todo POST é obrigado a dizer uma única coisa no header: qual método ele é e qual recurso ele quer. Pensa no que o teu proxy conseguia fazer antes: chegava um POST nele, esse POST chegava lá no `/mcp` e pedia uma única coisa — por exemplo, "me lista as tools", que é basicamente o que a gente espera que o MCP devolva para um agente: quais são as ferramentas que ele tá expondo. Isso podia segurar tua conexão uns 40 segundos — na verdade, "list tools" deveria levar milissegundos, não deveria nem levar segundos. Só que o teu Nginx não tinha como saber isso sem abrir o body, porque não sabia se alguém tava pedindo para listar as tools ou para rodar uma tool. E rodar uma tool pode envolver chamadas externas — por exemplo, já criei um MCP onde tu consegue autenticar via OAuth no Google; dentro do PSUA a gente aceita anexação de documentos vindos do Google Drive, e pra isso eu usei o MCP para integrar essa parte de requisição de autenticação.

Então toda vez que eu batia no Nginx, basicamente não dava pra saber se estava pedindo para listar as ferramentas ou para de fato rodar uma tool. Isso tem impacto forte porque as regras de, por exemplo, rate limit de API, tinham que ser únicas. Digamos que tu quer permitir que o cliente bata no teu MCP e pergunte quais são as tools a cada 3 segundos — tudo bem. Mas tu não quer que ele chame, por exemplo, uma tool de autenticação a cada 3 segundos; tu quer um timeout e um rate limit diferente, porque ninguém vai autenticar a cada 3 segundos se não estiver tentando hackear uma conta. Antigamente isso não era possível; agora isso tá tudo no header — tu tem um MCP request header e consegue passar pra ele o método e qual recurso tu quer. É outra tecnicidade que muda bastante a forma de implementar teus MCPs agora.

### A comanda do restaurante: estado na mão do cliente

Outra frase importante do changelog da Anthropic: "Servers that need cross-call state should use explicit, server-minted handles passed as ordinary tool arguments."

Traduzindo pro nosso dia a dia: imagina que tu chega no bar ou no restaurante e o garçom te entrega uma comanda com um número (eu já trabalhei de garçom, sei disso). Tu sai com aquela comanda, e qualquer garçom do bar consegue vir te atender, porque o teu estado tá na tua mão, no número da tua comanda — não tá na memória do garçom. Não é "aquele gurizão de camisa preta... deixa eu ver aqui nos meus pedidos, é o número três" — não, a comanda tá comigo, com o número três, e qualquer garçom pode vir marcar na minha comanda o que eu estou consumindo.

Então o estado agora tá na mão do cliente, não mais com o garçom (que seria o teu MCP). Era isso que a sessão stateful do MCP impedia antes: só o garçom que te atendeu primeiro sabia quem tu era. Agora, imagina que tu tem um MCP hospedado numa serverless function e pode chamar ele diversas vezes — ele não tá te amarrando nem fazendo handshake pra manter uma conexão contigo. Toda vez que tu chama, tu passa a tua comanda e ele sabe quem tu é. Ele não precisa manter uma sessão sobre ti.

O servidor faz o "cunhamento" (mintagem) da tua comanda — um número — e devolve isso como um argumento normal na próxima chamada que fizer. O estado da tua sessão sai da parte de transporte do protocolo e vira só mais um dado.

### Implicação de segurança da comanda

Claro que aí tem uma mudança de segurança, porque agora a comanda passa pela mão do cliente. Se ela for um número simples, o cliente pode trocar o número ou "comprar na conta" de outro cliente. Por isso agora a gente precisa **assinar** a comanda — não preciso ensinar isso porque é pra isso que um protocolo serve. No site `modelcontextprotocol`, buscando por "multi-round trip requests", tem a seção "server requirements", que explica: servers **must** treat request state as untrusted input; servers **must** protect its integrity.

Três coisas importantes ficam garantidas nessa assinatura: **quem é o dono**, o **prazo de validade** e **para que ela foi emitida**.
- Quem é o dono garante que a comanda de uma pessoa não vai parar na mão de outra.
- Prazo de validade garante que uma comanda de ontem não abre uma conta hoje.
- Para que foi emitida importa porque, sem isso, se tu emitiu uma comanda para fazer checkout num e-commerce, por exemplo, tu não pode usar ela para adicionar item no carrinho — senão estarias gerando assinaturas iguais para propósitos diferentes. Na documentação chamam isso de identificar a requisição que originou o pedido.

### Como o servidor pergunta algo ao usuário sem segurar a conexão

Se não tem handshake e não tem conexão aberta, como o servidor pergunta algo pro usuário? Isso deveria exigir um stream aberto, certo? É a parte de "multi-round trip requests": o cliente chama o servidor passando ID e parâmetros da requisição; o servidor precisa de mais informação e pede essa informação adicional; o cliente busca a informação e manda os parâmetros de novo; quando o servidor tem informação suficiente, ele volta com resultado para aquele ID. Ele não segura mais a conexão, mas pode responder "preciso de mais informação, tu não me mandou tudo que preciso". Cada uma dessas idas é um request diferente — o primeiro request "morre", tem ID um, o segundo tem ID dois. É um simples POST stateless.

E se falhar? Tu manda de novo — só faz o retry.

### Impacto no SDK e na facilidade de implementação

Lembra dos 400 milhões de downloads do SDK que citei no início? Tu pode usar o MCP TypeScript SDK, mas agora que é só um POST — um request e um response — dá pra fazer manualmente num único arquivo. Ficou ainda mais fácil criar um MCP. Tu não precisa esperar uma nova versão do SDK (quando eu escrevia o roteiro desse vídeo ainda nem tinha saído) — dá pra implementar esse MCP stateless na mão, num único arquivo.

Outras formas de começar: no GitHub da Hostinger tem o "Remote MCP Server", mostrando como criar um SEO checker para rodar remotamente no teu site. Também dá pra usar o Meta MCP, que instala com um clique na Hostinger e, dentro dele, tem diversos MCPs — é basicamente um MCP Server Proxy.

### Resumo das seis mudanças

1. **O handshake acabou** — não precisa mais manter uma conexão; toda request agora descreve o que ela quer por si só.
2. **Server discover** passou a ser obrigatório do lado do servidor, mas opcional do lado do cliente.
3. **Dois headers novos** — deixam o Nginx, gateway ou rate limiter trabalharem sem precisar abrir o body; tools diferentes podem ter configurações diferentes.
4. Ao invés de estado mantido pelo servidor, agora tu tem **comandas na mão do cliente** — cada request virou um request único.
5. Ainda tem **interatividade** entre servidor e cliente, porque o servidor pode retornar pedindo mais informação (multi-round trip).
6. Se algo falhar, um **retry** teu cai em qualquer nova instância da tua function.

Além disso: como tu não precisa mais manter sessão, tu **pode** manter se quiser (Redis, sticky session, session store) — mas não é mais obrigatório pela especificação. Isso garante que dá pra implementar um round robin "burro" numa VPS, sem precisar de mais nada. E esse era o objetivo desde o começo dessa modificação da Anthropic.

### Fechamento

O que eu quero que tu leve desse vídeo: sei que muitos de vocês não acreditam em MCP, assim como eu também fui descrente do QR Code. Hoje ando pelas ruas vendo QR code em tudo, até em transmissão de TV (ex.: Casé TV transmitindo a Copa com QR code na tela) — e a gente achava que essa ideia nunca ia funcionar.

O MCP nasceu parecendo uma ideia complexa demais: mantendo conexão viva entre client e servidor, tendo que ter todo o estado no transporte, uma máquina cuidando de um cliente. Agora essa complexidade vai embora — ele fica atrás de um load balancer, bota um round robin burro na tua VPS, e o agente serve as chamadas para as ferramentas que o cliente precisa. É a mesma correção que a web já fez há 20 anos. É incrível como a gente continua cometendo os mesmos erros toda vez que lança um novo protocolo ou tecnologia.

Comenta aí: tu já criou um MCP? Quer mais vídeos técnicos como esse, ou eu volto a falar de hype de IA e empreendedorismo? Bota no YouTube aí Lucas Montano — ou melhor, Techfounder Lucas Montano, que eu tô postando uns vídeos sobre essa jornada de empreender de novo no digital. Um forte abraço, não esquece de se hidratar, e eu te vejo no próximo vídeo.
