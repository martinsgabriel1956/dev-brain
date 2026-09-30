# ICMP Browser: navegando na internet sem HTTP, usando o protocolo do ping (Go)

> **Origem:** transcrição de vídeo em português (brasileiro), colada pelo usuário em 2026-09-30. Autor: Michel Leonardo (o falante se apresenta ao final: "eu me chamo Michel Leonardo"). Título original do vídeo e data de publicação não informados; o título acima é descritivo.
>
> **Tratamento:** a transcrição original é corrida, sem pontuação, com termos corrompidos pelo reconhecimento de voz. Aqui foi limpa e dividida em seções, sem alterar o conteúdo. Já estava em português, então **não houve tradução**.
>
> **Termos corrompidos, corrigidos por contexto:**
> - "Golend" → **GoLand** (IDE da JetBrains); "Jet Brandins" → **JetBrains**
> - "ICMP" também aparece como "CMP", "SMP" e "MP" → ICMP
> - "1228" / "12 28" → **128** (tipo ICMPv6 Echo Request); "129" = Echo Reply (o texto original diz "Eco Request")
> - "10000 bytes" (MTU) → quase certamente **1500 bytes** (MTU típico de Ethernet); o áudio diz "por volta de 10000". **[incerto; correção por conhecimento externo]**
> - "fragmentação do Tel" → provavelmente **fragmentação do IP** **[incerto]**
> - "a RID é esse caos" → "a rede é esse caos"; "ORL" → URL; "lente dão" → **lentidão**; "SIO" etc. omitidos
> - "hype" (pedido final) = curtida/engajamento no celular
> - Trechos de patrocínio (JetBrains) e pedidos de like/inscrição/sorteio preservados de forma resumida.

---

## Abertura: o que é o "ICMP Browser"

O navegador mostrado **não usa HTTP**: ele roda sobre o protocolo mais simples da internet, criado para saber se um servidor está vivo ou morto (o **ping**). O autor transforma o ping num navegador, o **ICMP Browser**. Canal já havia feito um **codec de vídeo usando ICMP**. A ideia surgiu depois de ver no LinkedIn um post de alguém que rodou **Doom pelo DNS**; no banho veio a ideia de tentar algo parecido com ICMP: navegar na internet sem HTTP, só com ICMP.

## O que é o ICMP

- Protocolo cujo objetivo é **reportar erros na rede**. Se um dado não chega ao destino final, o ICMP gera o erro e avisa.
- Exemplo: se um pacote é grande demais para um roteador, ele descarta o pacote e manda de volta à fonte uma mensagem ICMP avisando do erro.
- Outro uso clássico: enviar um pacote ICMP a um servidor para saber se está vivo e quanto tempo a viagem leva. É o que o comando `ping` faz.

## Como usar isso para acessar a internet

Olhando a estrutura do pacote, no final há o **campo de dados**, onde dá para colocar "qualquer coisa" e enviar ao destino. O tamanho máximo do campo em **IPv6** é de **65 KB**. Parece que um pacote só levaria o site inteiro, mas existe o vilão: o **MTU** (unidade máxima de transmissão), o tamanho máximo que um pacote pode trafegar antes de ser dividido em várias partes. O limite fica em ~1500 bytes (áudio diz "10000"; ver correção acima) e pode ser menor conforme a rede.

Consequência (exemplo cotidiano: baixar arquivo pesado e falhar com uma oscilação): a **fragmentação**. Se o pacote gigante é dividido em três partes e **um** fragmento se perde (oscilação de Wi-Fi), o sistema operacional do destino **descarta os outros dois** que chegaram. E o ICMP, diferente do TCP, **não tem garantia de entrega nem retransmissão**: perde-se uma parte gigante do HTML por um lag minúsculo.

O autor poderia implementar lógica de entrega/retransmissão, mas considera **complexo demais** e escolhe o caminho fácil: **fatiar o HTML em pedaços menores e enviar tudo separadamente** para fugir do MTU. Talvez faça a versão com garantia em outro vídeo.

## Patrocínio (JetBrains)

Pausa: a **JetBrains** agora é parceira oficial do canal (o autor usa suas IDEs todo dia). Todos os meses o canal sorteia uma licença de um ano de qualquer produto; regras na descrição e no comentário fixado.

## Código: servidor ICMP em Go (o lado que responde)

- Ferramenta: **GoLand**, com a **biblioteca oficial de ICMP do Go**.
- Primeiro passo: subir um **servidor ICMP**, que recebe os pings e devolve a resposta. O autor decidiu usar **IPv6**, então precisa informar isso ao abrir o listener.
- Depois, um **loop** que lê mensagens da rede.

**Primeiro problema:** começaram a chegar vários pacotes ICMP "do nada", sem ter enviado ping. "A rede é esse caos": era tráfego de erro de roteador e lixo. Era preciso filtrar.

**Solução:** existem vários **tipos de ICMP**; o tipo é definido pelo **primeiro byte**. O único que importa é o tipo **128, Echo Request** (o mesmo que o `ping` usa). Importa porque quem envia esse tipo **fica esperando uma resposta**, e é nessa resposta que o autor manda o HTML da página.

Depois de filtrar: ler o pacote ICMP e validar se o usuário enviou um **link no campo de dados**. Se sim, **baixa o HTML** da página para enviar de volta.

## "Acabamos de criar um proxy"

O autor explica: imagine querer acessar um site que espiona o seu computador. Para não se expor, você "contrata" o computador de outra pessoa: em vez de ir direto, manda o link a esse PC, que acessa, pega o conteúdo e devolve só a resposta, **sem vazar seu IP ou identidade**. Foi isso que fizeram, só que em vez de HTTP, usando ICMP.

## Fatiamento e protocolo próprio dentro do campo de dados

Depois de baixar o conteúdo, dividir em **pacotes de 1024 bytes** e enviar cada pedaço como resposta. Dois problemas, ao analisar de novo a estrutura do ICMP (só há espaço para **ID**, **número de sequência** e **dados**):

1. Como quem recebe sabe **quantos pacotes existem no total** para saber quando terminou?
2. Nada garante que milhares de pacotes chegam **na ordem certa**. Como reordenar?

**Solução (1):** os **primeiros 4 bytes do campo de dados** de cada pacote indicam o **total de pedaços**; o resto do espaço é preenchido com o HTML baixado.

## Lado cliente: receber e remontar

- Inicia-se outro **servidor ICMP** do lado que recebe o site, que agora escuta respostas do tipo **129 (Echo Reply)**, a resposta do ping com o endereço do site.
- Ao chegar a resposta, lê os 4 bytes iniciais (total de pedaços).
- Os pacotes chegam **fora de ordem**. Solução (2): como o total é conhecido, cria-se um **array desse tamanho** e cada pedaço é guardado na posição certa (pela sequência). O autor admite que **não é o método mais eficiente**, mas serve para um experimento.

## Mostrar no navegador: web server em Go + templates

- Com o HTML em mãos e ordenado, falta jogar na tela do navegador comum. Sobe-se um **web server simples em Go**.
- Segredo: o Go tem **sistema de templates nativo** "absurdamente bom": pega dados vindos do código Go e coloca direto na tela, **evitando criar uma API** só para enviar os dados da página.
- Template: uma caixa de texto onde a pessoa digita o link; ao apertar Enter, a página aparece.

## Teste final

Liga o servidor proxy, liga o servidor web, abre o navegador comum, digita uma URL: **funcionou**. Navegou pela internet usando um dos protocolos mais simples da rede.

## Limitações e próximos passos

- Rodou **localmente**, mas nada impede colocar num servidor real e navegar de qualquer lugar. Foi um dos motivos de usar **IPv6**: é fácil ter esse tipo de endereço liberado num servidor.
- É uma **prova de conceito**, com muitas limitações: **não baixa imagens** da página, **nem fontes**, e há o problema da **lentidão**.

## Encerramento

Pede like/inscrição ("hype" no celular). O código completo do proxy está na descrição. Lembra do sorteio JetBrains. Assina: **Michel Leonardo**, "e te vejo na próxima gambiarra".
