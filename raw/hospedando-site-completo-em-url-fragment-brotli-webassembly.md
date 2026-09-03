# Hospedando um site completo dentro de uma URL (fragment identifier + Brotli + WebAssembly)

Transcrição de vídeo (YouTube), autor: Michel Leonardo. Tema: gambiarra que hospeda um site HTML/CSS/JS completo inteiramente dentro do fragment identifier (`#`) de uma URL, sem servidor, usando compressão Brotli decodificada via WebAssembly (Go/TinyGo) no navegador.

## Transcrição

E se eu te falasse que dá para hospedar um site inteiro com HTML, CSS e tudo que você quiser direto na barra de endereços do seu navegador, sem pagar servidor, sem nuvem, sem nada? Parece doideira, né? Mas hoje a gente vai colocar um site completo dentro de um simples link de internet.

Tudo isso aconteceu porque eu tava sem ideia para vídeo, tava procurando alguma gambiarra nova para fazer pela internet. Até que eu achei o vídeo de um cara demonstrando como funciona um ataque XSS clássico, injetando o código direto no link. E foi aí que me veio a dúvida: até onde eu consigo levar uma vulnerabilidade dessa? Se o navegador aceita rodar um script escondido na URL, será que ele aceita renderizar uma página inteira?

Para quem não sabe o que é XSS: imagina uma cidade onde tem um robô que dá direções. As pessoas dessa cidade confiam cegamente nele. Você chega, escreve num papel para onde quer ir, entrega para ele, ele só repete em voz alta e aponta o caminho. Até que um dia um cara chamado Beto percebe uma falha: o robô não filtra o texto, ele só repete o que recebe. Aí Beto escreve um comando de JavaScript no papel usando as tags de `<script>` e manda para um coitado chamado Vítor. O Vítor entrega pro robô, que repete a ordem. O cérebro do Vítor, que age como um navegador, escuta aquilo — como a ordem tá dentro de uma tag `<script>`, ele não vê como texto, ele vê como comando. Ele obedece a ordem na hora e manda o dinheiro dele pro Beto.

Trazendo pro mundo real: o robô é um servidor web confiável. O atacante chega, injeta o código no link e manda pra vítima. O ataque vai no servidor e é refletido direto na tela. O navegador, confiando no site, roda o código sem pensar duas vezes. E é isso que chamamos de XSS reflexivo. Normalmente esse tipo de coisa acontece principalmente nos parâmetros da URL.

Foi aí que eu defini um objetivo: em vez de colocar um simples JavaScript, eu vou colocar um site inteiro dentro da própria URL.

### O problema do tamanho e a solução do fragment identifier

Quando usamos parâmetros de URL, eles vão pro servidor, e os servidores têm regras bem rígidas quanto ao tamanho do payload que vai nesses parâmetros. O Nginx, por exemplo, que é o mais famoso, não deixa passar de 4 a 8 KB, justamente para evitar ataques de DDoS. Para um site completo isso é muito pouco.

A solução tá no fragment identifier — aquela hashtag (`#`) que fica no final do link, que geralmente serve só para fazer a tela rolar até uma seção específica de um texto. Mas, por conta de como a web foi construída, tudo que vem depois desse hashtag nunca é enviado pro servidor. O navegador simplesmente não manda; fica tudo rodando localmente, só na sua máquina. E a melhor parte: navegadores modernos, tipo Firefox, aguentam até 2 MB de dados ali antes de dar algum erro. Isso é perfeito.

### Minificação com Go

Ter 2 MB não significa que dá pra simplesmente colar um HTML inteiro ali. O HTML não é compilado — o tamanho final depende de cada espaço em branco, quebra de linha, comentário inútil esquecido. Limpar isso na mão toda vez seria loucura, então automatizei com um script em Go usando a biblioteca `minify`: você passa o arquivo HTML e ela remove tudo que é inútil, resultando em uma única linha de código o mais leve possível.

### Compressão com Brotli

Para comprimir ainda mais, pesquisei o método de compactação mais forte e rápido para arquivos web hoje: Brotli.

Analogia: você é um chefe de cozinha com um caderno de receitas gigantesco e quer enviar pelo correio, mas isso custa caro e demora. Você contrata um organizador chamado Brotli para diminuir o caderno. Ele usa três truques:

1. **Carimbos**: Brotli já vem de fábrica sabendo os termos mais usados da internet; em vez de escrever tags do zero, substitui por um código minúsculo.
2. **Odeia repetições**: se o passo 3 diz "bata a massa" e o passo 8 também, ele risca o passo 8 e anota "volta 5 linhas e copia 3 palavras".
3. **Regra do menor apelido**: o que mais aparece ganha o símbolo menor (ex.: "farinha" vira um ponto); o que aparece pouco (ex.: "camarão") ganha um símbolo um pouco maior.

No fim, um livro de 1000 páginas vira um bloquinho de 150 páginas.

### O problema: sem servidor, sem header de compressão

O motor de descompressão nativo do navegador só é ativado quando o servidor manda o arquivo junto com o header HTTP `Content-Encoding: br`, avisando que o conteúdo está comprimido em Brotli. Mas nesse projeto não existe servidor enviando nada — só um link e o computador com o site. Ou seja: temos o pacote comprimido em mãos, mas o navegador se recusa a descomprimir sem o header.

### Por que não dá para descomprimir com JavaScript puro

Solução aparente: escrever o próprio descompressor de Brotli para rodar no link. Mas JavaScript puro tem problemas:

- JavaScript roda numa única thread — a matemática de descompressão do Brotli é densa; um site grande comprimido trava o navegador (aba "não responde").
- Codificação de URL: colocar os bytes crus do Brotli direto na barra faz o navegador converter símbolos especiais, e cada byte pode virar 3 bytes.

Solução: **WebAssembly** para rodar o algoritmo de descompressão, e **Base64URL** para resolver a codificação da URL.

### Base64 / Base64URL

Imagine uma foto e um correio que só aceita cartas em texto. Base64 é a máquina que desmonta os bytes e transforma tudo num bloco de caracteres comuns. Problema: Base64 usa `+`, `/` e `=`, que na URL são caracteres de comando/estrutura e quebram o link. A solução é **Base64URL**: mesma ideia, mas troca `+`/`/` por `-`/`_` e descarta o `=`.

### WebAssembly (Wasm)

Analogia: o navegador é um restaurante muito movimentado; JavaScript é o gerente — ótimo para anotar pedidos e arrumar mesas, mas se mandarem ele esculpir uma estátua de gelo em tempo real (rodar a matemática do Brotli), ele trava tudo. O Wasm não é um funcionário, é um manual de instruções pré-compilado em baixo nível: o navegador entrega direto pra CPU executar, sem tradução, então é muito mais rápido.

### Gerando o Wasm com TinyGo

É possível gerar Wasm a partir do próprio Go usando **TinyGo**, um compilador feito para rodar Go em ambientes bizarros (Arduino, Wasm). A documentação é ruim; o autor encontrou salvação num guia de blog escrito por "Artur C" depois de muitas horas tentando.

A peça-chave é a biblioteca **syscall/js**, que permite Go e JavaScript se comunicarem:

- A função de descompressão Brotli é escrita em Go e empacotada de forma que o JavaScript consiga chamá-la; todo o trabalho pesado roda isolado ali dentro, sem travar o navegador.
- `js.Global()` acessa o objeto `window` do navegador (escopo global da página) e registra a função lá, com o nome `decoder`. Na prática: abrir o console e chamar `window.decoder` passando o Base64 gigante devolve o site inteiro.
- No fim do programa Go é necessário um `select{}` vazio para bloquear a thread principal — sem isso o programa fecha e o JavaScript nunca mais consegue chamar a função depois.

Depois disso, basta rodar o comando do TinyGo para compilar o script em Wasm e colocar o resultado na pasta da página HTML. É preciso incluir também o arquivo `wasm_exec.js` (runtime/glue code) do próprio TinyGo, que funciona como um intérprete/tradutor entre o navegador e o binário Wasm gerado a partir do Go — sem ele o navegador não sabe o que fazer com o `.wasm`.

### O limite de 2 MB e a solução "multi-CD"

O fragment identifier aguenta até uns 2 MB. A solução, inspirada em jogos antigos que pediam para trocar de CD (tipo GTA), foi: quando o payload gerado passa de 2 MB, o script que gera a URL corta o código ali mesmo e coloca uma marcação de identificação (parte 1, parte 2, etc.), gerando vários links. No lado da página web, uma lógica de JavaScript pega todas as URLs separadas, junta as peças como um quebra-cabeça e monta o site completo na memória — basicamente uma "URL multipart".

### A página HTML final

A página usa HTML, CSS e JavaScript. Primeiro importa o script base do TinyGo (`wasm_exec.js`). O JavaScript lê o fragment identifier (tudo depois do `#`) contendo o texto em Base64. Faz uma checagem: se o payload tiver mais de uma parte (por causa do limite de 2 MB), pede para colar o próximo link. Com todas as partes reunidas, junta tudo e envia pro WebAssembly, que descomprime e devolve o HTML original, que é inserido direto na página.

### Teste final

Pegando uma página de exemplo, rodando o script (minificação + Brotli + Base64URL), copiando o texto gigante gerado e colando na URL depois do `#`, o site aparece renderizado na tela — a gambiarra funciona.

---

Autor do vídeo: Michel Leonardo. Crédito citado no vídeo: guia sobre TinyGo + Wasm por "Artur C" (blog não identificado com URL específica na fala).
