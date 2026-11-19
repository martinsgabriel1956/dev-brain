# Relatório do Google PageSpeed: os principais avisos de diagnóstico

Opa, fala pessoal, sejam bem-vindos a mais uma aula onde a gente vai dar mais uma olhadinha no que que o PageSpeed Insights ele dá pra gente, né? Então, essa aula aqui vai ser um pouquinho mais rapidinha porque, literalmente, nós vamos bater em teclas das quais eu já falei, né? Eu só vou estar comprovando pra vocês o que que o Google tá querendo dizer pra gente, tá?

## Imagens

Basicamente, olha só. Disponibilize imagens em formato de última geração. Traduzindo, ele quer em WebP, ele não quer em PNG e JPEG. Sempre que ele der um probleminha, ele vai te dar aqui uma breve descrição e um link pra poder você ler mais sobre isso, tá? Mas ele basicamente vai falar, ó, WebP ou AVIF costuma ter uma compensação melhor, por favor, transforme todas essas imagens que você vai ganhar em desempenho, porque tá pesado, né? Você pode ganhar muito desempenho nesse sentido porque as imagens vão ficar mais leves.

Defina um tamanho adequado para as imagens, que foi aquela conversa que a gente teve nas aulas passadas. Olha, eu detectei que aqui é uma resolução muito grande, que tá sendo carregada pro celular sem necessidade. Tá com uma resolução, sei lá, 4K num celular de resolução 320p, entendeu? Sem necessidade. Então, ele vai reclamar disso também.

## Recursos que impedem a renderização

Elimine recursos que impedem a renderização. Então, basicamente, isso aqui é quando tem algum JavaScript que não tá sendo utilizado, que ele verificou que estão bloqueando a primeira exibição da sua página, né? Então, não está contribuindo de forma direta pra primeira exibição. Lembra que ele leva muito em consideração a primeira exibição do seu website, né?

E aí ele fala, ó, por favor, inclua somente um JavaScript, um CSS que seja crítico, ou seja, que coloque lá no render de forma crítica para primeiro carregamento. Se não for crítico, você joga esse JavaScript lá pra baixo, tá? E, né, ajude aí na renderização pra que ele não seja carregado de forma primeira, porque ele não está contribuindo com nada, né? Basicamente, é isso.

## Payloads, texto visível e DOM

Evite payloads de rede muito grandes, ou seja, quando tem arquivos muito grandes lá embaixo. Então, coloquei alguns vídeos, mais algumas fotos. Você tá vendo que as áreas mais vermelhas são fotos e vídeos, tá? Sempre assim.

Garanta que o texto continue visível. Então, um probleminha aqui de acessibilidade.

Evite DOMs muito grandes. Então, quando você está carregando, por exemplo, páginas onde tem muitos elementos na DOM, geralmente quando a gente utiliza de muitos ícones dentro de uma página, ele reclama disso aqui, né? Porque você está com, sei lá, um SVG que está com mil camadas de gradiente, de muita coisa. Ele vê aquele tanto de elementos na árvore DOM e ele reclama também, tá?

## A regra do 80-20

Então, pessoal, esses são os principais pontos de crítica. Ah, Násser, eu tenho mais dúvidas. Por favor, vem aqui, dê uma lida, mas eu garanto pra você que se você realizar as práticas que a gente está conversando aqui, vai ficar quase nada, né? Desses limpinhos aqui que tudo a gente consegue resolver. Beleza, pessoal? Então, é isso.

E até a próxima aula, a gente vai falar um pouquinho mais agora sobre os artigos. Nós vamos bater em alguns pontos dos artigos aqui que eles costumam não agregar tanto. Porque o que acontece? Se a gente for aplicar aquela regra do 80-20, eu vou repetir isso na próxima aula, você consegue resolver 80% das coisas fazendo 20%. Grande parte disso é mídia, que é o que a gente já conversou até aqui.

Tem outras práticas que a gente pode conversar sobre melhorar o desempenho da sua página? Podemos. Só que, tipo assim, vai melhorar quanto? Ah, 30 milissegundos. São poucos milissegundos, entendeu? A gente vai muito numa nuância, a gente vai muito ali no osso que chega um ponto que você fazer esse tanto de coisa não vale a pena mais, porque o ganho que você vai ter é pouco, tá? Os principais que mais fazem a diferença, a gente já conversou, beleza? Mas é interessante a gente estar dando uma olhada nos outros para poder entender, mas saber pesar essas características.

Beleza, pessoal? Então, falou, até a próxima!
