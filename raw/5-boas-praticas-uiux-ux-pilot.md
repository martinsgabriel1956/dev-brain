# 5 boas práticas de UI/UX (com Cursor e UX Pilot)

## Introdução

Nesse vídeo nós vamos ver cinco boas práticas de UI/UX que vão fazer você sair de resultados como essa página aqui para ir para essa página daqui. Essas técnicas que a gente vai ver ao longo do vídeo são técnicas fáceis de aplicar nos seus prompts e também quando você tiver desenvolvendo as suas próprias interfaces.

Para quem tem um background mais de design — ou seja, quem fez alguma graduação ou algum curso mais técnico, mais aprofundado — talvez já conheça esses conceitos. Mas os desenvolvedores, tanto front-end quanto principalmente os back-end, eu tenho certeza que não conhecem todos esses tópicos que a gente vai discutir aqui. E só aplicando essas pequenas mudanças já vão fazer com que vocês construam interfaces muito mais amigáveis pros usuários e que cumpram o objetivo daquela página — às vezes conversão, às vezes fazer com que as pessoas entendam a mensagem que vocês querem passar — e, claro, interfaces mais atrativas.

## Contexto: como as duas interfaces foram criadas

Eu já estou aqui com as duas interfaces que a gente vai comparar pra gente conseguir extrair os conceitos de UI e de UX que diferenciam uma da outra.

A primeira coisa que eu quero dar pra vocês é um contexto de como eu criei essa interface inicial. Essa interface eu criei através do Cursor: fui simplesmente lá no meu Cursor e fiz um prompt bem curto, ele gerou um plano e eu pedi para ele implementar. Nada muito rebuscado a nível de boas práticas de front-end ou de design — fiz um prompt padrão, que normalmente é o que a gente faz no dia a dia quando tá mais corrido. Ele implementou aquela tela que a gente estava visualizando: uma landing page para coletar usuários interessados em ter acesso a cursos gratuitos.

Depois peguei esse mesmo conceito e fiz uma segunda versão pelo **UX Pilot**, uma ferramenta que eu tenho usado bastante (já comentei em outros vídeos do canal). Uso o UX Pilot para primeiro fazer o conceito de UI/UX e, quando termino esse conceito, exporto isso pro Figma. Lá no Figma, uso o MCP do Figma para implementar com Cursor / Claude Code.

Para essa segunda interface, visualmente mais atrativa, mais profissional e mais amigável pros olhos do usuário, utilizei as técnicas que vamos aprender neste vídeo.

## 1. Hierarquia visual

Na primeira versão da landing page, pela hierarquia dos elementos em tela não tem um fluxo específico que o olho percorre. Quando eu olho para essa tela, a primeira coisa que me chama atenção é o texto grande, mas depois eu jogo o olho pro formulário ("Escreva-se gratuitamente"), depois pro "ver cursos disponíveis", depois pro "quero me inscrever". A hierarquia visual dos elementos não foi pensada da melhor forma para explicar o que o usuário tem que fazer na tela e passar a informação pro usuário.

Isso acontece porque a hierarquia deveria ter sido pensada com fontes, pesos, cores e posicionamento que fizessem com que os elementos mais importantes chamassem mais atenção e, subsequentemente, os outros elementos fossem chamando a atenção do usuário. O que acontece nessa primeira versão é que os dois botões de CTA estão com o mesmo peso na hierarquia visual — mesmo tamanho, ambos com cores chamativas, mesmo tamanho de fonte. Isso já causa confusão no cérebro: qual é o botão principal? Para onde meu olho deve ir?

Outra coisa: o texto "Escreva-se gratuitamente", apesar de menor que o título, ainda está muito grande e em bold, o que acaba chamando a atenção do usuário direto pro formulário. Às vezes, antes de pedir pro usuário se inscrever, era melhor apresentar outros dados que o convencessem (quantos cursos disponíveis, horas de conteúdo, quais cursos tem — JavaScript, TypeScript etc.) — mas esses dados estão meio escondidos embaixo.

Na segunda versão, o texto que chama mais atenção é o título ("Aprenda mais e melhor suas habilidades"). Em seguida, "Comece a aprender agora". Depois, os números: 50.000 usuários ativos, 200 cursos, avaliação média. A hierarquia visual faz o olho ir muito mais para os elementos importantes, e há apenas um CTA — não dois. O problema de ter dois CTAs é que a ação do usuário se dispersa: alguns clicam em "ver cursos disponíveis", outros em "quero me inscrever". Como "ver cursos disponíveis" é uma ação mais fácil que preencher um formulário, o número de inscrições cai, porque esse CTA concorrente acaba capturando a atenção que iria para o formulário.

### Padrões de leitura da tela

Além do tamanho, cor e fonte, o **posicionamento em tela** importa — existem dois padrões de visualização, conforme um artigo sobre o tema:

- **Padrão Z**: mais usado ao visualizar páginas com mais elementos e menos texto (um app, um site). O usuário percorre da esquerda pra direita a partir do topo, desce pela diagonal até a parte inferior esquerda, e finaliza a leitura novamente da direita pra esquerda. É o padrão aplicado na segunda versão da landing page.
- **Padrão F**: mais usado em blogs e páginas com muito texto. O usuário primeiro escaneia todo o conteúdo em formato de F, sem ler de fato, e depois volta para ler o que interessou.

Para a landing page (mais elementos, menos texto), o padrão Z é o adequado.

### Aplicando no UX Pilot

Peguei a página gerada pela IA no Cursor, trouxe um print como referência no UX Pilot ("attach image with context") e usei o seguinte prompt:

> "Refatore o layout aplicando a lei da hierarquia visual. Estabeleça o título 1 como ponto focal usando um peso de fonte extra bold de contraste máximo. Formulário deve ser o ponto focal secundário, use tamanhos de fontes e pesos diferentes, garantindo que a ação do CTA seja visualmente dominante sobre todo o resto."

Na primeira iteração o texto ainda ficou grande e havia dois CTAs. Pedi para reduzir o texto e remover um dos CTAs, e o resultado ficou bem melhor. Importante: quando um print é usado como referência, a IA tende a herdar cores, fontes e estilo daquele print — por isso, para gerar a versão final (mais elegante), não usei a página antiga como referência em nenhum momento, apenas fiz prompts sucessivos.

## 2. Lei da proximidade (Gestalt)

Esse princípio de Gestalt diz que, dependendo da distância entre elementos (e de cores e formas), a gente pode visualizá-los como um grupo ou não. Exemplo clássico: três fileiras de bolinhas com a mesma distância são percebidas como um único grupo. Se a terceira fileira for afastada das demais, passamos a perceber duas fileiras como um grupo e a terceira como outro grupo separado. O mesmo vale para cores diferentes — bolinhas de cores distintas são percebidas como grupos distintos.

Essa lei é usada, por exemplo, em logos: no logo da Unilever, cada ícone (cenoura, flor, peixe etc.) é um desenho independente, mas juntos, em zoom out, formam a letra U — um grupo único.

Isso importa porque, dependendo de como a tela é montada, os usuários vão enxergar elementos como um grupo. Por exemplo, ao dar scroll e ver números de métricas juntos, o cérebro já entende isso como uma seção. Mas para atrelar um dado a outro elemento (por exemplo, um fato a uma promessa), eles precisam estar próximos — do contrário, o cérebro não os processa como parte da mesma coisa.

Na segunda versão da interface, os números (150 cursos gratuitos, +2.000 horas de conteúdo, etc.) foram aproximados do texto "Aprenda programação de graça", para que o usuário processe isso como uma unidade única: a promessa e a prova social juntas. Na primeira versão, esses números estavam soltos, sem conexão visual clara com o argumento principal.

### Aplicando no UX Pilot

Prompt utilizado, aplicado apenas na seção específica selecionada:

> "Aplique a lei de proximidade de Gestalt. Agrupe visualmente as estatísticas de prova social logo abaixo do título principal, reduzindo o gap entre eles para que sejam percebidos como uma única unidade de valor. Aumente o espaço/margem entre esse bloco e o formulário para separar claramente a promessa (o que ele vai aprender de graça) da ação (o que ele precisa fazer para alcançar aquela promessa)."

Dica extra: em vez de escrever os prompts na mão, vale usar uma IA de texto (ChatGPT, Claude etc.) para ajudar a redigir o prompt a partir de um print e da explicação da lei que se quer aplicar, e depois adaptar o resultado antes de colar no UX Pilot. Selecionar apenas a seção que se quer alterar (em vez da tela inteira) permite iterar em partes específicas sem perder o que já ficou bom em outras seções.

## 3. Affordance

Affordance em UX é uma propriedade visual ou interativa de um elemento que sugere como ele deve ser utilizado, guiando o usuário através das ações de forma intuitiva. Exemplos:

- Um botão num certo estilo sugere que deve ser clicado (e muda de estilo ao ser pressionado).
- Um switch sugere que deve ser "flipado" para ligar/desligar.
- Uma bolinha sobre uma linha sugere que deve ser arrastada (slider).
- Um campo de texto com um cursor piscando sugere que se deve clicar e digitar.
- Um ícone de microfone sugere entrada por voz.

O mesmo se aplica a elementos físicos: um botão de controle remoto sugere clique; um switch físico sugere puxar; um botão giratório sugere girar para aumentar/diminuir. Tudo isso melhora a experiência porque o usuário não precisa de uma curva de aprendizado — o próprio elemento já indica como deve ser usado.

Na interface do exemplo, os inputs indicam claramente que podem ser clicados (contorno ao focar) e os botões têm cursor pointer e hover. Um erro muito comum em interfaces geradas por IA é a ausência de cursor pointer em botões, ausência de hover/glow, e ausência de sublinhado em links — pequenos detalhes que, quando faltam, causam confusão sobre o que é clicável.

Na versão gerada no UX Pilot, foi adicionada uma setinha no CTA, que não é estritamente necessária para indicar clicabilidade (o botão já deixa isso claro), mas reforça a sensação de continuidade: preencher o formulário leva à próxima etapa (acesso aos cursos gratuitos).

## 4. Interface como máquina de estados

Todo elemento ou componente em tela que tenha interação com o usuário, ou que mude de estado, deve ser pensado como uma máquina de estados — como se aprende na faculdade. O elemento começa em um estado e sofre transições por interação do usuário ou por eventos do sistema (chegada de novo dado, atualização, etc.).

Isso importa porque é muito comum acessar interfaces que buscam dados sem exibir nenhum estado de loading — o usuário clica, tudo fica parado, e de repente aparece o resultado. Esse estado de loading teria sido mapeado se a máquina de estados do componente tivesse sido pensada.

Exemplo de máquina de estados de um formulário:
- **Estado inicial**: incompleto — botão desabilitado (disabled).
- **Estado preenchido**: botão habilitado (enabled); pode haver indicação visual de progresso.
- **Estado de loading**: ao clicar em "se inscrever".
- A partir do loading, o fluxo pode ir para **estado de erro** (mostrar mensagem de erro) ou **estado de sucesso** (mostrar confirmação).

Não é necessário desenhar um diagrama de estados formal para cada componente simples, mas é importante ter esse raciocínio em mente ao pedir para a IA gerar a interface — pedindo explicitamente que ela preveja esses estados possíveis. Para componentes complexos, com muitos estados possíveis (idle, loading, sucesso, erro, parcialmente preenchido etc.), vale um trabalho mais minucioso, já que cada estado bloqueia coisas diferentes em tela.

Um problema comum é um componente ocupar mais de um estado ao mesmo tempo — por exemplo, mostrar erro e sucesso simultaneamente, algo que, numa máquina de estados bem desenhada, nunca poderia coexistir (ou está no estágio que pode dar erro depois de carregar, ou está carregando e só depois mostra erro ou sucesso, nunca os dois).

## Wireframes e considerações finais

Além de gerar interfaces completas, o UX Pilot também permite gerar **wireframes**: em vez do desenho completo da tela, ele gera apenas os blocos e o posicionamento dos elementos, servindo de base para trabalhar em cima.

O UX Pilot é uma ferramenta completa para quem quer criar designs de forma mais elegante e profissional, entregando uma experiência melhor pros usuários. No final, dá para exportar tudo pro Figma e conectar com a IA de desenvolvimento preferida via MCP do Figma (por exemplo, Cursor ou Claude Code). A ferramenta tem créditos gratuitos disponíveis para testes (wireframes, UIs completas, fluxos inteiros).
