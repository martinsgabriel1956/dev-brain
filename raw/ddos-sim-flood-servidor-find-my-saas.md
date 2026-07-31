# Como um SYN Flood de 260 Milhões de Requests Derrubou meu SaaS

Transcrição de vídeo/áudio em português (canal "Mano Davin" — Davin, criador do Find My SaaS). Transcrição bruta original sem pontuação nem quebras de parágrafo; reorganizada em parágrafos e seções para leitura, sem alteração de conteúdo, gírias ou expressões do autor.

---

## O aviso

Eu tava na academia, no meio lá da minha malhação, do meu treino fofo, meu celular vibrou. Quando eu peguei o celular, cara, eu dei uma olhada e tinha uma notificação de instabilidade no meu servidor. Aí, alguns segundos depois, cara, eu tenho um amigo de cybersegurança, ele foi lá me mandou uma mensagem, falou assim: "O Find My SaaS tá fora do ar, cara?"

Aí do nada eu vou lá, abro o Estúdio do YouTube e eu vejo, cara, que tem uma porrada de gente comentando no meu último vídeo — aquele vídeo sobre vulnerabilidade — perguntando se eu tinha sido hackeado e tal, o que que tava acontecendo. Tava fora do ar, mano. Eu recebi 260 milhões de requests em um único dia e o meu servidor não morreu, ele foi assassinado.

*(Bloco promocional do canal — inscrição, notificações, lives às terças e quintas 10h, Instagram @manodeivin.)*

## O primeiro desespero

Primeira coisa que eu fiz, cara, foi largar a minha ginástica, largar o meu treino, a minha malhação, e abrir o SSH no meu celular — o primeiro desespero, gente. Aí eu tentei conectar, mano, e nada, o servidor não respondia. Eu falei: "cara, acabou", até minha força tava por diminuir. Peguei meus pesos e fui pra casa.

Cheguei aqui em casa, sentei em frente ao computador e falei: "porra, bora começar esse debug aqui." O bom é que era numa sexta-feira, boa e ruim, né — não tinha live nem nada, o trabalho tava de boa, falei: "deixa eu debugar essa parada."

## A fase de negação

Aí começa um estágio de negação absurda. Eu me recusava a aceitar que era um ataque DDoS. Sabe por quê? Porque eu tinha lá um firewallzinho configurado na moral, eu tinha um Cloudflare lá na frente de todos os domínios, tranquilinho, belezinha, tinha meu proxy certinho — na minha cabeça isso era praticamente impossível. Pensei: "ah, deve ser um pico de tráfego, deve ser algum processo engasgado, qualquer coisa menos um ataque."

Aí eu consigo entrar no meu servidor, dou um `htop`. Tinha um load average da máquina de 26 — e era uma máquina de 1 core (fiz até um upgrade depois, esqueci de mencionar: tinha uma máquina de 1 core, foi pra 2 cores). Imagina só bater 26 numa máquina de 2 cores. Tinha oito processos do `sched` rodando em paralelo, porque nenhum terminava nunca, e o scheduler ficava lá spawnando novos. Eu matei tudo na mão, o load caiu de 26 para 8. Falei: "beleza, resolvi essa bosta." Mas não tava resolvido, nem a pau.

## O bug do Traefik/Coolify

Enquanto eu tava matando os processos, o Coolify — que é basicamente o que eu uso pra gerenciar deploy — tinha atualizado o Traefik automaticamente. (Parênteses rápido: o Coolify é um projeto open source que qualquer um pode usar; a forma mais fácil de instalar é pela VPS da Hostinger, que tem um gerenciador com instalador que sobe o Coolify sozinho, sem copiar comando no terminal nem quebrar a cabeça com Docker na mão. Deixei tutoriais na descrição do vídeo original mostrando o deploy do Coolify usando a Hostinger, com cupom de desconto.)

Voltando pro caos: o Coolify tinha atualizado o Traefik automaticamente. O Traefik é o proxy reverso que roteia todo o tráfego das minhas aplicações. E a versão nova, a 3.6.16, tinha um bugzinho lindo: 35% de CPU constante mesmo sem nenhuma conexão, zero tráfego passando, e o troço queimando CPU igual minerador de Bitcoin. Imagina isso num servidor de 2 cores — você tira 35% de capacidade e o resto do serviço fica se empurrando no que sobra. E além do CPU, tinha memory leak: chegou a 4,7 GB de RAM em 40 minutos.

Eu ainda tava na fase de negação: "o problema é o Traefik, essa versão tá zoada pra caramba, vou fazer um downgrade e tudo volta ao normal." Mas o pior é que não era isso.

## O diagnóstico real: SYN flood

Eu rodei um `ss -s` — conexões TCP — e fiquei congelado: 34.000 conexões TCP no estado `CLOSE_WAIT`, 2.400 em `SYN_RECV` (aproximado — falado como "2400 FIN"), 30.000 sockets alocados no kernel. Isso tá longe de ser tráfego legítimo. Quem dera fosse — quem dera fosse esse sucesso todo pro Find My SaaS. Era um flood puro. A galera tava flodando, era SYN flood puro, isso que tava acontecendo.

Pra quem não sabe o que é um SYN flood: imagina que o servidor é a portaria de um prédio. Cada request que chega é uma pessoa nova que toca o interfone e fala "e aí, vim te visitar." O servidor vai lá, abre a porta e espera a pessoa entrar. O SYN flood é 70 milhões de pessoas tocando interfone ao mesmo tempo e ninguém entrando — o servidor fica lá de porta aberta esperando gente que nunca vai entrar, até travar tudo.

## O número que quebrou

Um número que eu não tava preparado emocionalmente pra ver: o dashboard do Cloudflare dos últimos 30 dias mostrava um pico de 260 milhões de requests num único dia. Pra ter uma base: num dia normal, o Find My SaaS recebia de 200 a 400 mil requests — isso já era considerado ataque normal/regular. Só que nesse dia, uma única pessoa mandou 70 milhões de requests de uma vez só.

É como se nos outros dias a galera tivesse jogando pedrinha na janela do Find My SaaS, e chegou um camarada e simplesmente jogou um caminhão de entulho, descarregou na sala. O load bateu 88 numa máquina de 2 cores — o ideal é ficar abaixo de 2. O SSH parou de responder, perdi acesso ao servidor, o servidor reiniciou sozinho (provavelmente um watchdog do kernel). A aplicação do Find My SaaS atingiu o limite de file descriptors — o número máximo de arquivos e conexões que pode abrir ao mesmo tempo — e entrou num loop de falha absurdo. Tentei `docker restart` no container, não respondia. "Fodeu, fodeu."

O atacante gastou muito mais dinheiro provisionando o DDoS do que eu recebo de faturamento no Find My SaaS no mês inteiro.

## A hipótese do IP vazado (e a surpresa)

Eu tinha uma hipótese forte durante o debug inteiro: talvez o IP real do meu servidor tinha vazado. Fazia sentido — se o atacante sabe o IP real, manda o tráfego direto pra ele e ignora o Cloudflare completamente. É tipo ter um segurança na porta do bar e o bandido entrar pela janela.

Fui olhar o dashboard do Cloudflare pra confirmar essa hipótese, e a resposta me quebrou: os ataques vieram *pelo* Cloudflare. O tráfego não foi direto no IP. E o pior: o modo **Under Attack** — a feature que o Cloudflare tem exatamente pra esse tipo de situação — tava desativado. Eu tinha um escudo e ele tava desligado, e eu não sabia.

O Traefik bugado recebia essas conexões do Cloudflare e distribuía pras aplicações; com o bug de CPU e memory leak, ele não conseguia processar nenhum tráfego legítimo, e ainda por cima 70 milhões de requests maliciosas chegando de uma vez. O servidor virou uma panela de pressão sem válvula de escape.

## As tentativas que falharam

- Downgrade do Traefik pra versão anterior: não resolveu — a versão 3.3 também apresentou memory leak naquele setup.
- Regra de firewall no Docker: insuficiente pro SYN flood.
- Reiniciar o container da aplicação: o container tava tão travado que não respondia nem ao `SIGTERM`.

Depois de umas 6 horas batendo cabeça (eu e o Claude Code tentando achar a solução), a decisão final foi: desistir de ressuscitar o servidor. Provisionei uma VPS nova do zero na Hostinger, rodando só o Find My SaaS, e fiz o desvio de tráfego pra lá. Aprendizado: às vezes, em engenharia de software, é melhor aceitar que o paciente morreu e refazer o paciente do que tentar ressuscitar um defunto.

## A filosofia do servidor novo

O servidor novo subiu com filosofia diferente. Da primeira vez eu só subia tudo e configurava a segurança meio por cima; dessa vez, primeiro a infraestrutura defensiva, depois o serviço. A sequência: firewall no boot, Docker depois, e o Proxy por último.

### Checklist do que mudou

1. **Auto-update de proxy em produção** — nunca mais travei a versão do Traefik. O Coolify, por padrão, atualiza o Traefik toda semana; parece conveniente até vir uma versão bugada que sobe sozinha e derruba tudo.
2. **Under Attack Mode no Cloudflare** — precisa estar ativado, ou pelo menos configurado pra ativar automaticamente. Eu tinha esse recurso disponível e simplesmente não tinha ativado.
3. **IP novo — o IP antigo tá queimado** — mesmo atrás do Cloudflare, o IP real do servidor pode aparecer em registro de DNS histórico, e um atacante consegue achar. Existem ferramentas de segurança que permitem descobrir isso em segundos (descoberta feita depois do incidente).
4. **Limite de file descriptors no container configurado explicitamente** — o default do Docker é baixo demais; configurar `65000` soft/hard.
5. **SYN cookies habilitados no kernel** — isso faz o kernel não alocar memória pra conexão TCP até o handshake terminar. Se o handshake nunca termina (como no SYN flood), a memória não é alocada — simples e eficiente.
6. **Monitoramento** — não tinha nenhum alerta pra RAM do proxy, pra contagem de processos acumulados, pra sockets TCP. Se tivesse, teria visto o problema uns 20 minutos antes de perder o acesso ao SSH.

## Fechamento

Segurança não é o que você sabe, é o que você configura — e eu não tinha configurado o básico no meu próprio servidor. Esse foi o preço da aula: 6 horas fora do ar, 260 milhões de requests, um servidor reconstruído do zero.

*(Fechamento do vídeo: pergunta pros comentários se o IP real do servidor do espectador tá exposto; recomendação de amigos de cybersegurança pra checagem de segurança, link na descrição; chamada pra outro vídeo do canal sobre um check de vulnerabilidade que achou 15 vazamentos no mesmo SaaS; CTA de inscrição/notificação/lives; publieditorial de cadeira ergonômica Elements para home office.)*
