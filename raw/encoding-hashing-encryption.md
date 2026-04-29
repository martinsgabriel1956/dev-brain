# Encoding vs Hashing vs Encryption — Qual a Diferença?

**Canal:** ByteByteGo (tradução livre)
**Tema:** Fundamentos de segurança e representação de dados
**Data de captura:** 2026-04-29

---

## Transcrição (traduzida)

Pense na última vez que você pesquisou algo no Google. Se você olhar para a barra do navegador, verá algo assim. Se olhar com atenção, os espaços são substituídos por `%20` e o ponto de interrogação por `%3F`. O navegador transformou sua query em algo diferente.

Por quê? Porque URLs só aceitam um conjunto limitado de caracteres. Nesse conjunto, caracteres como espaço (` `) não são válidos. Mas eles ainda precisam ser transmitidos — então são convertidos para algo que pertence ao conjunto permitido.

Esse tipo de transformação de dados de uma forma para outra, com o propósito de armazenamento ou transmissão, é chamado de **encoding**. E assim como no exemplo anterior, dados podem ser codificados de muitas outras formas. Por exemplo, o texto `hello` pode ser convertido para binário, hexadecimal ou base64.

O encoding não se limita à transmissão de dados — tem outros usos. Por exemplo, no frontend com CSS, você já viu os códigos de cor com valores RGB. Esses valores normalmente são escritos em hexadecimal pela sua natureza compacta. Em decimal, o mesmo valor ficaria muito mais longo. Da mesma forma, em HTML, você pode ter visto a tag `<img>` referenciar uma URL onde a imagem reside. Para imagens leves, é possível incorporá-las diretamente no formato base64 via HTML ou CSS — economizando uma requisição de rede.

O ponto central aqui é que **encoding é reversível**. Qualquer pessoa que vê `%20` consegue decodificá-lo de volta para um espaço. Trata-se de representação de dados, não de segurança.

---

## Hashing

Falando em segurança — toda vez que você cria uma conta online, sua senha nunca é armazenada em texto puro. Em vez disso, ela é convertida em uma string de comprimento fixo que pode parecer algo assim. A partir dessa string, é impossível reconstruir a senha original.

Esse tipo de transformação é possível por meio de um processo chamado **hashing**. Hashing é o processo de converter dados em outra forma irreversível, usando um algoritmo de hashing que executa operações matemáticas complexas por baixo dos panos.

Então, quando você faz login, a senha que você digita é hasheada novamente e comparada com o hash armazenado no sistema. Se forem iguais, o login é bem-sucedido.

Hashing é definido por três características principais:

1. **É unidirecional.** Não é possível reverter um hash para obter a entrada original.
2. **É determinístico.** A mesma entrada sempre produz o mesmo hash.
3. **É de comprimento fixo.** Não importa o tamanho da sua senha — o hash sempre terá o mesmo tamanho.

Hashing não se aplica apenas a senhas. Em downloads de arquivos, por exemplo: se o arquivo baixado estiver corrompido, seu hash será diferente do arquivo original. Se estiver íntegro, o hash será idêntico.

---

## Encryption

E se você precisar de uma transformação unidirecional que seja bidirecional — mas apenas para pessoas ou sistemas selecionados? É aí que entra a **encryption** (criptografia).

Imagine que você tem um documento secreto no seu computador. Qualquer pessoa com acesso à sua máquina pode abri-lo e lê-lo. A criptografia oferece uma forma de transformar esse documento em algo que só pode ser revertido com o uso de uma **chave**. Quem tem a chave acessa os dados. Quem tentar abrir sem a chave verá apenas gibberish.

### Exemplo histórico: Cifra de César

Júlio César usava uma técnica básica de criptografia para proteger mensagens militares — hoje conhecida como **Caesar Cipher** ou Shift Cipher. A ideia: deslocar cada letra da mensagem por um número fixo de posições no alfabeto.

Digamos que o deslocamento seja 3. A palavra `HELLO`:

```
H → K
E → H
L → O
L → O
O → R
```

Resultado: `KHOOD`. Para quem intercepta sem saber o deslocamento, parece sem sentido. Mas o destinatário que sabe que cada letra foi deslocada por 3 pode simplesmente reverter o deslocamento e decifrar a mensagem de volta para `HELLO`.

Esse tipo de criptografia é trivialmente quebrável hoje com computadores modernos, mas ilustra perfeitamente a ideia central: a mensagem só é legível para quem tem a chave.

### Criptografia moderna

A criptografia moderna usa algoritmos matemáticos complexos projetados para ser inquebrável por força bruta — pelo menos com os computadores atuais. A computação quântica pode mudar isso, mas é tema para outro vídeo.

O WhatsApp, por exemplo: toda mensagem que você envia é criptografada no seu dispositivo antes mesmo de sair do seu celular. Se alguém tentar espionar a rede, verá apenas ruído ininteligível. Somente a pessoa com quem você está trocando mensagens — que possui a chave de decriptação correspondente — consegue transformar esse ruído em palavras reais.

---

## Resumo comparativo

| | Encoding | Hashing | Encryption |
|---|---|---|---|
| **Propósito** | Representação / transmissão | Verificação de integridade | Confidencialidade |
| **Reversível?** | Sim, por qualquer um | Não | Sim, mas só com a chave |
| **Exemplos** | UTF-8, binário, hex, base64 | MD5, SHA-256, bcrypt | AES, RSA, E2E (WhatsApp) |
| **Uso típico** | URLs, imagens inline, CSS | Senhas, integridade de arquivos | Mensagens, documentos sensíveis |

**Encoding** é como traduzir dados para outro formato para que computadores possam armazená-los ou transmiti-los corretamente. Não é sobre sigilo — é sobre estrutura e legibilidade. Totalmente reversível.

**Hashing** pega seus dados e os passa por uma "fórmula" especial para criar um código único de comprimento fixo. Esse código não revela os dados originais e não pode ser revertido. Por isso é ideal para armazenar senhas com segurança ou verificar integridade de arquivos.

**Encryption** é sobre confidencialidade. Transforma seus dados em algo ilegível — mas temporariamente, porque, diferente do hashing, é reversível desde que você tenha a chave correta. É assim que apps de mensagens como o WhatsApp protegem suas conversas até dos próprios servidores.
