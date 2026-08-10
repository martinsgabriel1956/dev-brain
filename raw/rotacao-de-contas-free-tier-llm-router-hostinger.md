# Achei um "Esquema Illuminati" pra Rodar Cloud Code de Graça

Eu achei um esquema Illuminati para poder rodar o Cloud Code de graça, paizão. Porra, tô muito feliz, mano. Essa semana um amigo me apresentou o **Nine Router** — basicamente ele é um proxy onde você consegue plugar vários providers: Gemini, Cloud Code, Cursor, OpenRouter, tem um monte de ferramenta chinesa, e ele consegue pegar os modelos da própria Anthropic também.

E tem um recursozinho interessante nele, meu jogador: você consegue colocar algumas contas free tier nele. Por exemplo, eu posso ter três contas do Gemini, posso ter, por exemplo, três contas da Anthropic. E ele tem um esquema que, quando acaba o token de uma, ele joga pra outra; acabou de outra, ele joga pra outra. É praticamente uma "disqueteira" para nós que somos velhos. E isso não é pirataria, tá? Isso pode ser imoral, mas não é nada ilegal.

No vídeo de hoje eu vou te mostrar isso na prática. Mas antes de continuar, já sabe, né, cara: já deixa o like, se inscreve no canal, ativa a notificação pra não perder nenhum conteúdo neste canalzinho — isso aqui é um boteco de tecnologia. E você que já é inscrito, dá uma olhada aqui embaixo se você continua inscrito, porque o YouTube está derrubando as inscrições.

## O que é o Nine Router

Como eu já adiantei, basicamente o Nine Router é um proxy local — um proxy que você instala na sua máquina, instala numa VPS, instala onde você quiser — onde ele vai gerar, por exemplo, uma chave de API, uma URL bonitinha, e ele é totalmente compatível, por exemplo, com a API da Anthropic e a API da OpenAI. Então é plug and play: você vai plugar lá, cara, e a parada já vai funcionar de cara.

E tem muito provider compatível — eu tenho uma lista aqui: Cloud, Copilot, Gemini CLI, Cursor, Codex, Llama, Qwen, Kiro, OpenRouter. Tem muita opção de graça.

### Instalação via Hostinger (implantação com um clique)

Vou fazer o setup aqui nesse exato momento pra gente rodar isso na prática, porque não tem muito lenga-lenga. Vou aqui na "implantação com um clique", pesquiso "Nine Router", coloco a senha do meu dashboard, clico em "implantar", espero um pouquinho e já vai tá pronto.

E pronto — já tá aqui, mano, já tá funcionando, já com login e senha. Não tem muito mistério pra instalar.

## Providers e o esquema de rotação de contas free tier

Se a gente vier aqui na lateral, na aba de providers, a gente tem: Cloud Code, Antigravity (sem limite), e alguns free tier providers, se é que você me entende. Tem o OpenCode Free, o Opener (já conectado), o Ollama Cloud — tá tudo aqui.

Basicamente você conecta, por exemplo, o Kiro AI, que tem vários planos free tier, e ele tem todo o esquema de rotação: tá esgotando o token dessa conta, vamos pra próxima; tá esgotando dessa, vamos pra próxima. Ele faz essa rotação e você fica tranquilo. Por exemplo, se você tem duas contas do Cloud, você não precisa esperar os seus tokens acabarem — pode colocar duas contas, por exemplo, uma da empresa e uma pessoal, e ele vai rotacionando. Você não precisa esperar aquele ciclo de "ah, vou ter que esperar 4 horas" — não, mano, ele já resolve isso também.

A instalação é muito simples graças à Hostinger, que é parceira desse canal. Se você quiser testar, rodar na sua máquina, deixei um linkzinho na descrição — se usar o cupom "Devin" você ainda vai ter desconto. Eu tenho aqui minha máquina de laboratório, tenho a máquina dos meus SaaS rodando na Docker — a galera sabe que ela te atende desde o MVP até produção mesmo, até você escalar o seu produto. Então usa meu cupom, você vai ajudar a fortalecer pra caramba o canal.

## Configurando o Cloud Code pra usar o Nine Router

Eu particularmente gosto de rodar ele usando o OpenRouter, gosto muito do OpenRouter. Só que tem uma galera que já tá acostumada, por exemplo, com a usabilidade do Cloud Code — eu até entendo que é muito boa, principalmente porque você já tem os atalhos, já sabe onde tudo funciona. Então eu sei que migrar de CLI, de ferramenta de desenvolvimento, é muito complexo. Então vamos pro Cloud Code.

A primeira coisa que você precisa fazer dentro do seu Nine Router é ir no menu **Endpoint and Key**. Ele basicamente já vai gerar uma URL pra você — a minha URL da Hostinger — e você vai gerar uma chave de API ali. Pode criar uma chave. Eu já vou copiar — lógico que isso é uma API temporária, então pode ser que vaze; se vazar não tem problema, porque ela vai ser deletada antes que os script kiddies fiquem de olho aí pra querer me foder. Mas fica tranquilo, o pai tá vacinado.

Uma vez copiado isso, você pode simplesmente vir aqui em **Claude settings** — no `claude-settings.json` — e simplesmente colar essa linha aqui, onde eu passo a minha `ANTHROPIC_BASE_URL` e passo a minha chave. Fica tranquilo que tá tudo certo.

Então eu não loguei, não fiz nada. Vou entrar aqui na minha pasta `barra-app`, tenho aqui meu Ruby on Rails API. Se eu chamar o Claude aqui, ele fala que ele "tá com o Rico", mas na real ele tá com outro esquema — que eu já vou te mostrar como faz essa configuração — mas ele já tá plugado na minha ferramenta. Se eu der um "oi" aqui, já vai me responder: "Pronto, como posso ajudar você?" — e em hora nenhuma fiz login com ele.

### Mapeando modelos

Uma parada interessante é que eu consigo, por exemplo, mapear o modelo que o meu Cloud Code tá usando lá — esse Haiku 4.5. Então eu posso simplesmente vir aqui e adicionar os modelos que eu quero usar. Por exemplo, eu tenho aqui o OpenRouter, tô usando o GLM 5.2. Então, enquanto o meu Cloud Code tá conectado no Haiku 4.5, eu mapeei o GLM 5.2 — mas eu posso simplesmente mapear com outros modelos.

Se você tiver usando o Kiro, que tem um free tier muito generoso, você consegue usar o próprio modelo da Anthropic, se quiser, e o OpenRouter também. A vantagem do Kiro é que você usa meio que de graça enquanto é free tier — como eu já estourei a minha cota, não consigo nem testar. Mas eu tenho outra parada interessante: o **MiMo Code Free**, que é da Xiaomi, tem esse modelo MiMo. Então também posso selecionar esse modelo pra adicionar no meu combo.

Eu consigo ordenar esse combo de modo que ele faça o esquema de "tá acabando os tokens dessa conta, vamos pra próxima". Ele consegue fazer isso, e você ainda consegue fazer o teste: se falhar a chamada do GLM 5.2, ele vai tentar o próximo. Ele tem essa configuração chamada **try in order**, que vai tentar na ordem — falhou esse, vai pro próximo; falhou esse, vai pro próximo — pra fazer a rotação. E ele tem também a opção "penalize" (ou algo do tipo), que confesso que não sei direito o que seria — acho que tem um esquema de "julgamento" ali. Mas vamos pegar o mais simples, que é o **fallback**, que funciona uma maravilha.

## Painel de uso e custo

Outra coisa muito interessante nele é que você tem todo o controle de uso. Olha só, dos testes que acabei de fazer aqui: quantos tokens de input, quanto de output, quanto gastei de estimativa — gastei $7,14 nos testes que eu tava fazendo. Ele mostra tudo que tá acontecendo, que eu usei GLM 5.2, e se, por exemplo, ele começar a chamar o MiMo, já mostra a distribuição — ele tem todo esse mapa aqui. Achei incrível isso.

## "Token Saver": comprimindo output, contexto e prompts

Essa parte aqui confesso que é polêmica, e é exatamente o que eu quero testar. Ele tem uma funcionalidade chamada **Token Saver**. O que isso faz: basicamente economiza token pra você.

- **Compress output** — já vem ligado por padrão. Basicamente enxuga a saída de comandos tipo `git diff`, `grep`, `ls` antes de mandar pro modelo, resolvendo aquele problema de agente queimando token à toa só pra ler "ruído" de comando. Achei uma parada maneira.
- **Compress** (segunda opção) — faz uma compactação de toda a conversa quando você tá numa sessão muito longa, resolvendo aquele problema do Cloud Code ficar "esquecendo" todo o contexto quando você tá no finalzinho da janela e ela acaba estourando.
- **Caveman** (terceira opção) — a gente já falou aqui no canal daquela skill do "homem das cavernas", que faz o modelo falar de forma mais econômica, tipo homem das cavernas, e resolve as paradas — te economiza token pra caramba. Você consegue selecionar se quer light, full ou ultra. Por padrão você não precisa de skill nenhuma pra isso; toda vez que você tiver plugado no seu Nine Router, ele controla isso pelo dashboard.
- **Lazy senior dev** (última opção) — basicamente é o espírito do programador sênior preguiçoso, que tenta não abstrair tanto, não precisa escrever tanto código pra aquilo — é basicamente o "sênior cansado", que tem muita preguiça. Acho maravilhoso.

### Teste ao vivo: com e sem Token Saver

Quero mostrar na prática, ao vivo: eu testei e vou falar pra você que, pro que eu uso, não foi tão legal assim — mas talvez, testando seu caso de uso, pode ser que funcione pra você.

Com o Cloud Code aberto, sem nenhuma opção de Token Saver habilitada, colei um prompt do meu "Mega Brain" pedindo pra criar uma aplicação em Ruby on Rails 7 — basicamente um CRUD de locadora (a gente que é velho já ama isso), só uma API com SQLite, mas tem que rodar os testes e tem que funcionar. Rodei o Mega Brain e ele finalizou a tarefa, tudo rodando, testes passando: três exemplos, zero falhas.

Fui ver o uso pra poder comparar com os outros módulos: gastamos **$0,81**, 705 mil tokens de input, 4.800 de output, 748,8 mil de leitura de cache.

Agora vamos ativar a primeira opção — o **compress output**, a ferramenta de compressão de output, que segundo ele diminui de 60% a 90% dos tokens. Apaguei a locadora gerada sem o compress ativado, e fiz a mesma coisa de novo com ele ativado. Rodei o Mega Brain e... levou **7 minutos**. Era exatamente isso que eu queria mostrar: no resultado, gastou bem mais — olha a quantidade de tokens: **2,2 milhões de tokens de input**, 12.800 de output, **2,6 milhões de leitura de cache**. Coloca lado a lado um com o outro só pra ver o absurdo que é isso.

O que eu quero trazer com isso: pra mim, que sou programador Ruby on Rails, isso não funcionou. E pra não prolongar muito o vídeo, testei o Caveman também — não funcionou, acabou gastando muito mais token. Testei todas aquelas flags e, pra mim, não foi tão legal, não gostei muito. Mas pode ser que pro seu caso de uso funcione.

## Sessão longa "infinita" e fallback silencioso

Tem outras coisas que confesso que achei bem interessantes. A gente sabe que, quando tá programando e a janela de contexto vai enchendo, perto do final ele começa a "delirar", dar resposta errada pra caramba. Ele tem um recurso, que já é padrão, de uma sessão muito mais longa — te dá um contexto muito maior, como se você tivesse uma janela de contexto infinita. E, por mais que faça aquela troca de modelo que comentei, o contexto acaba migrando de modelo pra modelo. Isso o OpenCode também faz, que acho maravilhoso. Mas se você gosta do Cloud Code, cara, você consegue fazer isso também com o Cloud Code.

Outro recurso que eu curti muito é o **fallback silencioso**. A gente sabe que alguns modelos chineses, principalmente quando a gente tá usando conta free — essas continhas que a gente vai fazendo pra testar — começam a dar erro do nada, pra caramba. O fallback silencioso é o seguinte: ele fez a chamada nesse modelo, esse modelo deu problema, ele vai pro próximo; o próximo deu problema, ele vai pro próximo. Ele vai testando vários modelos, e o contexto acaba sendo compartilhado entre os modelos. Isso, mano, é lindo.

## Um contraponto sincero: cuidado com contas free tier

Agora sendo bem sincero, falando sério: a gente fica muito emocionado com essa parada de jogar várias contas de free tier, mas, na prática, pra usar no dia a dia de trabalho, talvez isso não seja uma parada tão OK, porque a gente sabe que o Gemini CLI e o próprio Cloud Code têm meio que um detector pra saber se você tá usando alguma ferramenta assim, e acaba bloqueando seu acesso — e você acaba perdendo a conta. Você pode plugar várias ferramentas chinesas e fazer essas contas free tier e tal, mas tem que tomar muito cuidado com isso.

Pra você que é estudante, tá fazendo projeto paralelo, tá com pouca grana pra torrar nisso, acho que vale a pena. Agora, na prática, pra você que trabalha no dia a dia, sendo bem sincero, eu não confiaria 100% — mas pra brincar, testar uma coisa ou outra, vale muito a pena, principalmente pra testar esse monte de modelo chinês que foi lançado sem gastar um centavo.

E antes que a galera fale "pô, paizão, mas você tá usando uma parada paga" — calma, calma, porque tem o Cloud Code e tem os modelos da Anthropic; você tá usando a ferramenta de graça, porque a ferramenta tem um "lockin" que você só pode usar com modelos Anthropic, e o que eu acabei de fazer aqui foi usar modelos chineses — o GLM 5.2, mais conhecido como "o Fable Killer", que é o concorrente que quase empata com o Fable — usando a ferramenta. Lógico que tem uns bugzinhos, se você observar tem umas mensagens de erro ali, mas nada que incomode, é só ignorar. E é isso: a gente consegue quebrar o "lockin" do Cloud Code.

## Fechamento

Se você quiser testar, testa na Hostinger, não precisa instalar na sua máquina — joga na Hostinger. Assim como pra mim é legal, porque eu testo aqui no meu Mac, testo também no meu PC — tenho um PC que uso pra fazer umas lives, faço alguns projetos, testo nele, tenho umas máquinas em Linux que consigo plugar nela. A grande vantagem é ter tudo centralizado — acho que isso de estar centralizado é maravilhoso, consigo ter um controle muito melhor de tudo que tô usando, tudo que tô gastando. Mas se você quiser testar, usa meu cupom "Devin" na Hostinger, deixei o link na descrição, você vai ajudar pra caramba o canal.

E se você não é inscrito, se inscreve no canal, deixa o like, ativa a notificação pra não perder nenhum vídeo. E ainda falando sobre ferramentas: dá uma olhada nessa recomendação que eu fiz — testei aquela do PewDiePie, aquele youtuber famoso, que lançou uma ferramenta pra você poder usar no seu dia a dia e quebrar esse lockin de ter todos seus dados com as empresas, como a OpenAI e a Anthropic — os seus dados passam a ser 100% seus.

Estamos juntos, forte abraço, até o próximo vídeo, valeu!

---

**Nota de transcrição:** o nome do produto foi ouvido foneticamente como "Nine Router" (possivelmente grafado de outra forma pelo fabricante — não confirmado nesta transcrição). Pontuação, acentuação e cortes de repetição (efeitos de reconhecimento de fala) foram normalizados; o conteúdo e a ordem dos argumentos foram preservados.
