# Padrão de Projeto Decorator (Renato Augusto)

> Transcrição de vídeo em português sobre o padrão de projeto Decorator. Autor: Renato Augusto.

Fala pessoal, Renato Augusto aqui de novo, e dessa vez pra gente falar sobre o padrão de projeto **Decorator**, que é um dos meus padrões de projetos favoritos. É um padrão extremamente poderoso, muito flexível e versátil — você vai conseguir utilizá-lo em muitos contextos. E é um padrão que utiliza um conceito chamado **composição recursiva**, que muita gente não conhece, e isso traz uma flexibilidade absurda para dentro do seu código. A gente basicamente vai conseguir alterar uma classe, adicionar uma funcionalidade em tempo de execução, sem nem tocar nessa classe. Isso não é mágica, é apenas padrão de projeto. Então, pra gente não perder mais tempo, vamos pra tela e vamos entender como é que isso funciona.

## Propósito e categoria

Qual é o propósito por trás do padrão de projeto Decorator? Basicamente ele é um padrão na categoria dos **padrões de projeto estruturais** — a gente tem os criacionais, os estruturais e os comportamentais. Ele é conhecido por três nomes: **Decorator** (decorador, do inglês pro português), **invólucro** (a tradução correta — "envoltório" está errada) e **Wrapper**. Cuidado para não confundir: outros padrões de projeto também são conhecidos como Wrapper — o Adapter, por exemplo, também é conhecido como Wrapper. Mas em 99,9% dos casos ele é chamado de padrão de projeto Decorator.

O propósito desse padrão basicamente é o seguinte: a gente vai pegar os nossos objetos e adicionar novos comportamentos ao longo do tempo, conforme a necessidade for surgindo, **sem tocar no nosso objeto**. Porque todas as vezes que a gente modifica uma classe que já está em produção, já está rodando lá, a gente muito provavelmente vai trazer novos bugs, vai quebrar alguma coisa. Então nunca é bom modificar as nossas classes já existentes, porque isso fere o **Open/Closed Principle** (princípio aberto/fechado), que diz que as nossas classes têm que estar abertas para extensão e fechadas para modificação.

Esse padrão está ligado diretamente ao Open/Closed Principle: a gente não vai alterar a nossa classe, a gente vai adicionar novas funcionalidades sem nem tocar nela. A gente joga o nosso objeto dentro de um invólucro, dentro de outro objeto, para adicionar um comportamento sem alterar o objeto principal. E conforme forem surgindo novas features e novas demandas, a gente vai criando novos invólucros e jogando um dentro do outro — e isso é chamado de **composição recursiva**.

### Analogia com o mundo real

A gente tem o nosso personagem. Surgiu uma demanda: o personagem está com frio — o que a gente faz? Acopla um casaco nele, adiciona uma característica/comportamento novo. Depois chegou a chuva, uma nova demanda: a gente adiciona uma capa de chuva nele. Mas repare: a gente não altera o personagem principal, a gente adiciona novas funcionalidades sem alterá-lo diretamente. E a capa de chuva foi adicionada por cima do casaco, mas se eu quiser pegar o personagem e adicionar diretamente a capa de chuva sem passar pelo casaco, também consigo — **a gente não é obrigado a seguir uma ordem**.

Esse padrão tem muita similaridade com o **Chain of Responsibility** (cadeia de responsabilidades), outro pattern que traz um processo em cadeia para executar algumas coisas. Só que no Chain of Responsibility a gente precisa seguir uma ordem, e aqui a gente não precisa.

## Exemplo em código: Image Processor

A gente tem um diretório chamado `image_processor`, que seria um módulo dentro do nosso sistema. Vamos imaginar que estamos trabalhando numa aplicação em que o usuário consegue fazer upload de imagem e editar essa imagem posteriormente — um sisteminha de thumbnails, por exemplo, aquelas capinhas de imagem pro YouTube.

Dentro do `image_processor` a gente tem uma **interface** (`ImageProcessorInterface`) e uma classe concreta (`BasicImageProcessor`) que a implementa. Na interface a gente tem apenas um método `process`, que recebe o `imagePath` (o caminho da imagem que vamos processar) e retorna uma string (o novo caminho onde a imagem processada está armazenada).

A classe concreta `BasicImageProcessor` implementa a interface. No método `process`, ela recebe o caminho da imagem. O código cliente, quando chamar essa classe concreta, vai ter que passar o caminho de uma imagem. Aqui dentro, fazendo uma pequena simulação (não faz sentido criar código real, traria poluição visual), a gente teria a lógica para o processamento básico dessa imagem. Por fim, a gente cria um novo caminho para a imagem processada, salva a imagem nesse caminho (dentro do diretório `uploads`) e retorna esse `newImagePath`.

Esse processamento básico poderia ser, por exemplo: a verificação dos metadados da imagem (para ver se tem conteúdo malicioso), a verificação da extensão do arquivo (se é JPEG, para ver se o cara não está tentando passar um PDF ali dentro) e, por fim, salvar o arquivo dentro de um diretório novo.

### Código cliente e o fluxo de upload

O nosso código cliente pega o caminho de um arquivo que supostamente acabou de chegar no servidor. Quando o usuário no front-end faz upload de uma imagem, essa imagem inicialmente vai para um diretório temporário (`/temp`). É ali que a gente pega a imagem e faz algum tratamento nela ou a salva em outro diretório. No exemplo, o `imagePath` é `/temp/file.jpg` (fictício). A gente simula que o Controller pegou essa imagem no `/temp` e vai jogar para ser processada dentro do `image_processor`, que processa a imagem e salva dentro do `uploads`.

### Nova demanda: marca d'água

Chegou uma nova demanda: o usuário não quer mais só o processamento básico, ele precisa adicionar uma **marca d'água** na imagem (o textinho dele, o texto da marca/empresa, pra que as pessoas não possam roubar a imagem dele).

A gente é sempre inclinado a fazer a coisa errada: alterar a classe padrão que já está em produção. Isso não faz sentido e fere o Open/Closed Principle. O interessante é sempre adicionar novas funcionalidades sem tocar na nossa classe — e é aí que entra o Decorator.

Em vez de adicionar um método novo ou um construtor no `BasicImageProcessor`, a gente cria uma classe que vai **envolver** o `BasicImageProcessor`, e essa classe nova conterá a funcionalidade de adicionar a marca d'água:

```
class WatermarkImageProcessor implements ImageProcessorInterface {
    constructor(imageProcessor: ImageProcessorInterface, watermark: string)

    process(imagePath):
        processedImagePath = imageProcessor.process(imagePath)  // delega para o objeto envolvido
        // lógica para abrir a imagem, adicionar a marca d'água (watermark)
        // cria um NOVO arquivo (watermarkedFile), não sobrescreve o existente
        return watermarkedFilePath
}
```

Essa classe `WatermarkImageProcessor` é o **decorator** — ela decora a classe raiz `BasicImageProcessor`. No construtor ela recebe um `ImageProcessorInterface` (que vai ser a instância do `BasicImageProcessor` jogada aqui dentro) e o texto da marca d'água. No `process`, ela primeiro chama `imageProcessor.process(imagePath)` — o `BasicImageProcessor` processa o caminho que chegou e retorna o novo caminho —, e só então a gente adiciona a funcionalidade de decoração: abre a imagem no caminho retornado, adiciona a marca d'água e **cria um novo arquivo** (para não quebrar o arquivo já existente caso dê algum problema), retornando o caminho do novo arquivo.

### Montando a cadeia no código cliente

No código cliente (que representaria um Controller num MVC), a gente instancia o `BasicImageProcessor` e, se a marca d'água foi solicitada, sobrescreve a variável com uma instância do `WatermarkImageProcessor`, jogando o `BasicImageProcessor` para dentro:

```
imageProcessor = new BasicImageProcessor()
imageProcessor = new WatermarkImageProcessor(imageProcessor, "texto da marca")
result = imageProcessor.process("/temp/file.jpg")
```

Agora `imageProcessor` é uma instância do `WatermarkImageProcessor` e, dentro dele, tem uma instância do `BasicImageProcessor`. Ao rodar, são criados dois arquivos: `file.jpg` (do processamento básico) e `watermarked_file.jpg` (com a marca d'água). A gente instancia a classe, joga a instância do `BasicImageProcessor` para dentro do `WatermarkImageProcessor`; quando `process` é chamado, o `WatermarkImageProcessor` manda o `BasicImageProcessor` executar em cima do caminho que chegou, pega o retorno, abre o arquivo, adiciona a marca d'água, cria um novo arquivo e retorna o caminho.

### Nova demanda: redimensionar

Chegou mais uma demanda: o usuário quer **redimensionar** a imagem (passar uma altura e uma largura). De novo, a gente seria instigado a ir na classe `BasicImageProcessor` e carregar o construtor/método `process` de propriedades — não faz sentido. Vamos criar mais um decorator, o `ResizeImageProcessor`:

```
class ResizeImageProcessor implements ImageProcessorInterface {
    constructor(imageProcessor: ImageProcessorInterface, height: int, width: int)

    process(imagePath):
        processedImagePath = imageProcessor.process(imagePath)
        // lógica para redimensionar de acordo com height/width
        // cria um novo arquivo (resizedFile)
        return resizedFilePath
}
```

No código cliente:

```
imageProcessor = new BasicImageProcessor()
imageProcessor = new WatermarkImageProcessor(imageProcessor, "texto da marca")
imageProcessor = new ResizeImageProcessor(imageProcessor, 100, 100)
result = imageProcessor.process("/temp/file.jpg")
```

Ao rodar, são criados três arquivos: `file.jpg` (básico), `watermarked_file.jpg` (marca d'água) e `resized_file.jpg` (redimensionado). O arquivo redimensionado já tem a marca d'água e o processamento básico — a gente está **somando funcionalidades**.

## Composição recursiva e execução em cadeia

O fluxo: a gente tinha um `BasicImageProcessor`; adicionou o decorator de marca d'água; e por fim o de resize. O `ResizeImageProcessor` recebeu uma instância do `WatermarkImageProcessor`, que já tinha uma instância do `BasicImageProcessor`. Quando a execução chega na linha do `process`, o `ResizeImageProcessor` chama o `process` do `WatermarkImageProcessor`, que antes de executar a própria lógica chama o `process` do `BasicImageProcessor`. No final das contas, isso é uma **execução em cadeia** — muito parecido com o Chain of Responsibility. Esse padrão também tem outros nomes como **Middleware**, e alguns frameworks o utilizam principalmente para validação de requisições HTTP.

A diferença: no Chain of Responsibility a gente precisa seguir uma ordem; aqui não. Se eu inverter a ordem dos decorators (trocar um pelo outro), ainda assim consigo executar — ele recria todos os arquivos, sem erro. A gente também **não é obrigado a implementar todos** os decorators. Se, lá no front-end, a gente permitiu que o usuário optasse por adicionar a marca d'água ou não, num Controller a gente faria um `if`: se o parâmetro da marca d'água foi passado, a gente instancia o `WatermarkImageProcessor` e passa a instância anterior para dentro; senão, o `imageProcessor` continua sendo o resize (ou o básico).

O que manda é a **instância atual** que está na variável e o método `process` que a gente chama — porque todas as classes possuem esse método (implementam a mesma interface). Você vai criar novos objetos que encapsulam objetos anteriores e ir adicionando funcionalidades ao longo do tempo, podendo trocar a ordem tranquilamente.

## Fechamento

É um padrão simples e muito poderoso. No começo é um pouco complicado por conta da composição recursiva, mas é tranquilo de implementar. Por fim, o autor recomenda o livro **Padrões de Projeto** (o catálogo oficial do GoF), que muda a percepção sobre orientação a objetos e ensina todos os design patterns do GoF.
