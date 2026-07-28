# Pipeline de Renderização do Browser — da URL ao Pixel

> Transcrição de vídeo (áudio → texto), já em português. Reestruturada em markdown a partir de bloco único sem pontuação/seções, preservando o conteúdo técnico. Título original de trabalho: explicação de tudo que acontece entre digitar uma URL e a página aparecer na tela (~300ms), em seis etapas.

## Introdução

Você digita uma URL e aperta enter. Em 300 milissegundos a página aparece na tela. Mas entre o enter e o primeiro pixel, o browser passa por seis etapas diferentes. Este vídeo mostra cada uma delas.

## 1. Cache

Tudo começa com a URL. O browser precisa descobrir para onde mandar o pedido de dados — mas antes de tudo, ele checa o cache: se essa página já foi visitada e o cache ainda é válido, o browser pula tudo e usa a versão salva, sem precisar de rede nem espera.

Se não tem cache, aí sim começa a navegação.

## 2. DNS

O primeiro passo é o DNS. O browser pega o domínio (por exemplo `exemplo.com`) e pergunta pro servidor de DNS qual é o endereço IP correspondente. O DNS é como se fosse uma lista de contatos do celular: você tem o nome e precisa do número — o IP seria o número de celular. Quando recebe a resposta, o browser sabe para onde ir.

## 3. Conexão TCP

O próximo passo é abrir uma conexão TCP: o famoso handshake de três vias (three-way handshake), que são três mensagens só para estabelecer a conexão:

1. Browser manda **SYN**.
2. Servidor responde **SYN-ACK**.
3. Browser confirma com **ACK**.

## 4. TLS (se HTTPS)

Se o site usa HTTPS, tem mais uma etapa: o TLS. Browser e servidor negociam a criptografia trocando certificados e chaves, o que resulta em mais algumas viagens de ida e volta (round trips).

## 5. Request HTTP

Depois de tudo isso, só agora o browser manda o request HTTP — um `GET` pedindo o HTML da página. O servidor responde com um documento de texto em HTML.

## 6. Do HTML ao DOM

Esse arquivo de texto é só uma sequência de caracteres. Como o browser transforma isso numa página visual?

1. **Bytes → caracteres**: o HTML chega como bytes; o browser converte em caracteres usando a codificação declarada no documento (geralmente UTF-8).
2. **Tokenizer**: lê os caracteres e identifica cada pedaço — tags de abertura e fechamento, atributos, texto. Exemplo: ao encontrar `<div class="container">`, o tokenizer cria um token de abertura com o nome `div` e o atributo `class`.
3. **Nós e árvore**: cada token vira um nó, e esses nós são organizados numa árvore baseada na hierarquia de abertura/fechamento das tags. Essa árvore é o **DOM** (Document Object Model) — representação estruturada do documento inteiro. Cada tag vira um nó, cada texto vira um nó, cada atributo fica acessível.

**Parsing incremental**: o parser não espera o HTML inteiro chegar — ele começa a construir o DOM conforme os dados chegam. É por isso que páginas grandes renderizam de cima para baixo: o browser vai renderizando conforme os bytes chegam.

**Tolerância a erros**: o parser de HTML é tolerante. Se você esquecer de fechar uma tag, ele fecha para você. Se você colocar um `<div>` dentro de um `<p>`, ele reorganiza. O parsing de HTML nunca falha.

**Limitação do DOM**: o DOM sozinho não sabe como as coisas devem aparecer. Ele sabe o que existe, mas não a cor, o tamanho, nem a posição.

## 7. CSSOM

Para saber a aparência, o browser precisa de outra árvore. Enquanto o DOM está sendo construído, o browser encontra tags `<link>` e `<style>` com CSS. O CSS passa por um processo parecido: bytes → caracteres → tokens → nós → árvore. Essa árvore se chama **CSSOM** (CSS Object Model).

O CSSOM mapeia cada regra CSS para os elementos que ela afeta. Como o próprio nome do CSS diz, ele funciona em cascata: cada nó herda estilos do pai. Se o `body` tem `font-size: 16px`, todos os filhos herdam esse valor, a não ser que sobrescrevam.

**CSS bloqueia a renderização**: o browser não renderiza nada enquanto o CSSOM não estiver completo. Isso acontece porque, sem ele, o browser renderizaria o HTML cru sem estilo nenhum e depois teria que redesenhar tudo — experiência ruim para o usuário.

## 8. Render Tree

Com o DOM (estrutura) e o CSSOM (estilos) prontos, o próximo passo é combinar as duas. O browser passa pelo DOM e, para cada nó visível, consulta o CSSOM para encontrar os estilos computados. O resultado é a **render tree**.

A render tree só tem nós visíveis:
- Tudo com `display: none` fica de fora.
- O `<head>` inteiro fica de fora.
- Tags `<script>` ficam de fora.
- Diferença importante: `visibility: hidden` **entra** na render tree — o elemento é invisível, mas ainda ocupa espaço.

## 9. Layout (Reflow)

Com a render tree pronta, vem o **layout**, também chamado de **reflow**. É aqui que o browser calcula a geometria de cada elemento: posição X e Y, largura e altura.

Pensa no **box model**: cada elemento é uma caixa com content, padding, border e margin. O browser calcula o tamanho final de cada caixa levando em conta o fluxo do documento — um `width: 50%` vira um número em pixels, uma margem `auto` é calculada com base no espaço disponível. Unidades relativas viram absolutas.

O layout é recursivo: o tamanho de um pai depende dos filhos, e a posição dos filhos depende do pai. O browser resolve isso de cima para baixo (passando as restrições de largura) e de baixo para cima (acumulando as alturas).

## 10. Paint

Agora que o browser sabe exatamente onde cada caixa vai ficar e qual o tamanho dela, falta transformar isso em pixels na tela. O **paint** transforma a render tree em pixels. O browser percorre cada nó e gera instruções de pintura — algo como "desenhe um retângulo azul na posição 10,20 com largura 250 e altura 50 pixels". Cada nó vira uma ou mais instruções dessas.

O browser não pinta tudo numa superfície só — ele divide a página em **camadas** (layers). Elementos com `transform`, `opacity` ou `will-change` geralmente ganham camada própria, porque mover uma camada é muito mais barato do que repintar tudo.

## 11. Composite

Depois de pintar cada camada, vem o **composite**. A GPU pega todas as camadas, aplica as transformações e combina elas na ordem certa. Por isso animações com `transform`/`opacity` são performáticas: elas só mexem no compositing, sem recalcular layout nem repintar.

Até esse ponto o browser já fez tudo e a página aparece na tela — mas tem um elemento que pode interromper esse processo inteiro: o **JavaScript**.

## 12. JavaScript e o Parser

Quando o parser de HTML encontra uma tag `<script>`, ele para — para de construir o DOM para executar o script. Isso acontece porque o JavaScript pode modificar o DOM: `document.write` insere HTML novo no meio do parsing, `appendChild` adiciona um nó filho, `removeChild` remove. O parser não tem como saber o que o script vai fazer, então ele espera.

**Preload scanner**: enquanto o parser principal está parado, o browser usa um recurso chamado preload scanner — um parser mais leve que escaneia o HTML adiante procurando recursos para baixar (imagens, stylesheets). Ele não constrói o DOM, mas adianta o processo, começando downloads em paralelo.

**Cadeia de bloqueios CSS → JS → HTML**: se o script acessa estilos computados (ex.: `getComputedStyle`), o browser precisa garantir que o CSSOM esteja atualizado. Então o CSS que ainda está carregando bloqueia o JavaScript, que bloqueia o parsing do HTML. Ou seja: CSS bloqueia JS, que bloqueia HTML — uma cadeia de bloqueios.

**`async` e `defer`**: dois atributos resolvem esse problema.
- `async`: o browser baixa o script em paralelo e executa assim que termina o download, sem garantia de ordem de execução.
- `defer`: o browser também baixa em paralelo, mas só executa depois que o DOM está completo, e na ordem em que aparece no HTML. Na maioria dos casos, `defer` é o mais usado — o script roda depois do DOM pronto, sem bloquear o parsing.

**Eventos importantes**:
- `DOMContentLoaded`: dispara quando o HTML foi parseado e os scripts com `defer` executaram.
- `load`: só dispara quando tudo carregou — imagens, fontes, iframes, tudo.

## 13. Reflow/Repaint Disparados por JavaScript

Quando JavaScript modifica o DOM ou o CSSOM, o browser pode precisar refazer partes do pipeline:
- Mudar a **largura** de um elemento → causa **reflow**.
- Mudar a **cor** → causa só **repaint**.
- Mudar o **transform** → vai direto pro **composite**.

Quanto mais "acima" no pipeline a mudança acontece, mais trabalho o browser precisa refazer.

## 14. Por Que as Otimizações Funcionam

Conhecendo o pipeline inteiro, dá para entender por que certas otimizações funcionam — cada uma ataca uma etapa específica:

- **Minificar HTML/CSS** → reduz o tempo de parsing.
- **Usar `defer` nos scripts** → evita o bloqueio do parser.
- **Manter o CSS raso** (seletores simples, pouca profundidade) → acelera o layout.
- **Usar `transform`/`opacity` em vez de `top`/`left`** → pula direto pro compositing, sem layout nem paint.
