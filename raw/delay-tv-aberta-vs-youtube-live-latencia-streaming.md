# Por que a Live do YouTube Chega Depois da TV Aberta? (Delay/Latência de Streaming)

Transcrição de vídeo/áudio em português. Já no idioma original — sem necessidade de tradução.

---

Você tá vendo um jogo da Copa do Mundo na Casé TV no YouTube e do nada um vizinho grita "gol", mas para você a bola ainda nem tinha entrado na área. Se o mesmo jogo tá passando na Globo pela TV aberta, o lance vai chegar muito antes. E por que que isso acontece? De onde vem esse delay? Vou te explicar o que acontece desde a câmera até chegar na sua tela.

Antes de comparar, precisamos separar a emissora do meio de transmissão. Você pode assistir a Globo por antena, por cabo, por satélite ou pela internet no Globoplay, e cada um vai funcionar de uma forma diferente. O foco aqui vai ser comparar a TV digital aberta recebida por antena com uma live que chega pelo YouTube.

A diferença entre o momento capturado pela câmera e o momento exibido para você se chama **latência**. E para entendermos essa latência, a gente começa no ponto que os dois tipos de transmissão têm em comum: nos dois casos a imagem tem que passar pela produção. A equipe vai escolher a câmera, vai adicionar a narração, coloca o placar e talvez segura alguns segundos para conseguir fazer o replay ou alguma outra operação. Depois eles vão ter que comprimir o vídeo, porque mandar cada quadro sem tratamento deixaria pesado demais. Só essa parte já vai adicionar um atraso na TV e também no YouTube.

Só que depois da compressão, os delays vão se acumulando de forma diferente para cada um deles.

## Na parte da internet

O produtor vai ter que enviar o vídeo para os servidores do YouTube. Quando o vídeo comprimido chega no YouTube, a plataforma processa e gera versões diferentes da mesma live — então uma pessoa pode estar vendo em 4K na TV enquanto uma outra tá vendo em 480p no celular. Esse processamento se chama **transcodificação**, e ele eleva um tempo, mas ele permite que a live funcione em vários dispositivos e conexões diferentes.

Com essas versões prontas, o YouTube ainda vai precisar organizar o vídeo para distribuir milhões de reproduções. Para fazer streaming pela internet, o vídeo inteiro tem que ser quebrado em partes menores. Um arquivo de controle vai informar quais segmentos já estão disponíveis e em qual ordem o player tem que buscar.

Depois vai entrar a **CDN**, que é uma rede de servidores distribuídos que aproxima fisicamente o conteúdo dos espectadores. A CDN vai reduzir a distância e dividir a carga, mas cada pessoa assistindo tem que pedir os dados pela própria conexão.

Para evitar que qualquer oscilação trave a imagem, o player vai ter que guardar parte desses dados antes de mostrar pro usuário. Pra isso, o **buffer** é usado para reservar uma parte pequena do vídeo que tá à frente do ponto que você tá assistindo, entre aspas, "ao vivo". Se a internet der uma oscilada por um momento, o player vai consumir essa reserva e a imagem vai continuar passando. Só que para criar essa margem, a reprodução necessariamente precisa ficar atrás do ponto mais recente da live.

O próprio YouTube explica na documentação deles que esse buffer de leitura antecipada é o principal causador da latência do streaming. Se diminuísse a reserva, o vídeo se aproximaria do "ao vivo", mas qualquer variação da rede do usuário travaria muito mais rápido para ele. Esse tradeoff entre estabilidade e atraso existe porque a internet entrega uma sessão diferente para cada pessoa.

## Na TV digital aberta

A emissora codifica e modula o sinal usando radiodifusão. A torre vai transmitir esse fluxo pela mesma faixa de rádio para toda a área de cobertura. A TV vai receber os bits pela antena, vai corrigir o que for possível, decodificar o áudio e o vídeo e mostrar a imagem.

A maior diferença é que ela não precisa pedir o próximo segmento a um servidor que nem no stream, e nem escolher uma qualidade dependendo da internet de cada um. Isso porque o mesmo sinal serve para todos os aparelhos com antena compatível — aí não precisa criar uma conexão separada para cada um. Por isso, a TV aberta precisa de muito menos buffer antes da reprodução.

É importante falar que a TV aberta também tem um delay: também tem a parte de produção, compressão, transmissão e decodificação, que gastam tempo. No YouTube ainda tem outras coisas, como upload até o servidor deles, a transcodificação, a publicação de segmentos e a distribuição pela CDN. Depois ainda tem a conexão de quem tá vendo, o buffer e o decoder do aparelho. Tudo somado dá o delay que você sente.

## O delay não é igual para todo mundo

Digamos que a primeira pessoa tem uma conexão estável: o player dela vai conseguir manter um buffer menor. A segunda pessoa tem uma oscilação na internet dela: o player dela vai ter que aumentar a distância para evitar que trave a transmissão. E digamos que a terceira pessoa pausou a live, voltou depois e continuou de onde parou. O aparelho, o navegador, a rede e a qualidade escolhida também vão mudar o quanto o vídeo fica armazenado. Por isso que duas pessoas na mesma live do YouTube podem ter delays diferentes.

Mas o produtor da live tem como escolher o quanto a plataforma tem que priorizar a estabilidade ou a interação. O YouTube oficialmente oferece alguns modos de latência: a normal, a baixa e a ultra baixa. Segundo a documentação deles, a maioria das pessoas fica abaixo de 10 segundos no modo de baixa latência; no modo de latência ultra baixa, a maioria vai ficar abaixo de cinco. Não dá para saber qual configuração cada canal, que nem a Casé TV, usa nas lives do YouTube.

Quanto menor a latência escolhida, menos vídeo o player consegue guardar como proteção. Por isso o YouTube deixa claro que reduzir o atraso vai aumentar a chance de buffering — principalmente quando o upload dos produtores pro YouTube ou a conexão da pessoa não é uma internet mais rápida. Isso vai ajudar quem tá assistindo, mas não consegue ajudar com todos esses processos que não têm nenhuma relação com a sua internet.

## O que você pode fazer para melhorar o delay

Uma conexão estável ajuda, evitando que o buffer cresça, e também deixar a qualidade no automático vai fazer a resolução diminuir antes de travar a transmissão. Só aumentar a velocidade da internet não vai garantir que a imagem fique sincronizada com a TV aberta — isso porque a transcodificação, os segmentos e o buffer da plataforma vão continuar atrapalhando.

Resumindo: só dá para reduzir o atraso local, porque você obviamente não vai conseguir controlar toda a cadeia de transmissão. Se você tá vendo a Globo pelo Globoplay, ela também tem que percorrer uma cadeia de stream pela internet similar à do YouTube. Se for TV a cabo ou via satélite, vão entrar os equipamentos e os buffers de cada operadora. E fora tudo isso, a Casé TV e a Globo podem receber feeds de produção diferentes, cada um com o próprio atraso antes da distribuição.

Agora, quando o vizinho gritar gol primeiro, você vai lembrar desse vídeo enquanto espera o gol chegar na sua tela.

É isso — se curtiu, se inscreve e deixa um like, que ajuda bastante o canal. Valeu!
