# Criptografia — de César aos Computadores Quânticos

Transcrição de vídeo (autor não identificado no material fornecido).

---

Imagina que você quer mandar uma mensagem super secreta pro seu amigo que mora do outro lado do mundo, e a única forma de mandar mensagem é por carta. Como que você faz para garantir que só ele vai ler essa mensagem? E se um carteiro resolver abrir no meio do caminho, ou pior, se alguém mudar a mensagem antes de chegar no destino?

Você promete: "responderei com criptografia". Mas vamos falar real: você realmente sabe como é que funciona essa tal criptografia? O que diz se o método é seguro ou não? É isso que eu vou explicar para vocês hoje.

## A Cifra de César

Mais de 2000 anos atrás, Júlio César tinha esse problema: ele precisava enviar ordens militares sem que o inimigo entendesse. E a solução dele foi simples: ele pegava cada letra do alfabeto e trocava por outra. Tipo, A vira D, B vira E, C vira F — fazia um shift no alfabeto.

Pode até parecer seguro, mas com o tempo as pessoas começaram a perceber que tinham poucas combinações possíveis, e com pouco de paciência qualquer um conseguia quebrar a mensagem. Essa é a cifra de César — o que muita gente acha que é a primeira criptografia, mas não é.

## A Cítala Espartana (Scytale)

Algumas centenas de anos antes, os espartanos já tinham sua própria criptografia, conhecida como Cítala (Scytale). Ela funcionava assim: primeiro você enrolava um pedaço de couro ao redor de um bastão. Aí você escrevia sua mensagem na fita em linha reta, e depois desenrolava a fita e preenchia os espaços vazios. Só alguém com o bastão do mesmo diâmetro conseguia enrolar a tira e ler a mensagem corretamente. E é isso que eles pensavam.

Mas a criptografia antigamente não era sobre matemática, era pura criatividade. E o legal de entender é que sempre teve o mesmo objetivo: garantir um canal seguro dentro de outro canal inerentemente inseguro.

## O que significa ser um canal seguro

Trocar informação de modo seguro é fazer com que a mensagem enviada ou recebida seja:

- **Confidencial** — ninguém além do esperado consegue entender.
- **Íntegra** — garantir que a mensagem não foi alterada.
- **Autêntica** — conseguir validar que quem te enviou a mensagem é realmente quem diz ser.

## A Cifra de Vigenère

Depois dessas criptografias apareceram outras ao longo do tempo, mas vamos pular para a próxima mais importante, mais de 1000 anos depois: por volta de 1500, a cifra de Vigenère.

Enquanto métodos antigos uma letra X era sempre trocada por uma letra Y (A sempre vai ser E, B sempre vai ser F), a cifra de Vigenère mudou isso: agora a letra A em algum momento pode ser substituída pela letra E, em outro momento pela letra K, e por aí vai.

Funciona assim: você tem a sua mensagem que quer encriptar, e precisa de uma chave secreta, geralmente do mesmo tamanho. Existe uma matriz com linhas e colunas que vão de A até Z. Procura-se a linha que tem a primeira letra da mensagem, e a coluna que tem a primeira letra da chave — onde elas se encontram é a primeira letra da cifra. Repete-se isso para cada letra da mensagem.

Para descriptografar é parecido: com a mensagem criptografada e a mesma chave, para cada letra da chave pega-se a linha onde ela aparece, procura-se nessa linha onde a letra da mensagem criptografada aparece, e olha-se para cima para encontrar a letra original.

A mesma chave secreta usada para criptografar é usada para descriptografar — isso é **criptografia simétrica**. Um fato curioso é que a cifra de Vigenère era conhecida como "a cifra indecifrável" por mais de 300 anos, até que descobriram que não era bem assim.

## A Máquina Enigma

Pulando mais alguns anos, para a época das guerras: a máquina Enigma foi a principal máquina de criptografia para comunicação da Alemanha durante a Segunda Guerra Mundial, e foi quebrada porque os operadores repetiam a chave — o que não pode de jeito nenhum.

## Criptografia Simétrica e Assimétrica

Hoje em dia a gente tem que proteger dados em escala industrial e governamental, então os algoritmos ficaram mais robustos, matematicamente confiáveis e, consequentemente, mais complicados. Precisa de um conhecimento teórico em matemática equivalente a algumas pós-graduações.

Atualmente existem dois tipos de criptografia: **simétrica** e **assimétrica** (também conhecida como criptografia de chave pública).

### Criptografia Simétrica — AES

Na criptografia simétrica, a mesma chave é usada para criptografar e descriptografar. É rápida, eficiente e mais simples do que a assimétrica.

Um exemplo é o **AES (Advanced Encryption Standard)**, um algoritmo de criptografia simétrica **por blocos** — diferente das criptografias por fluxo que criptografam byte a byte, a criptografia por bloco processa um grupo fixo de bits de uma vez só.

O AES pode usar chaves de 128, 192 e 256 bits, e dependendo do tamanho da chave o número de rodadas muda. Cada rodada serve para embaralhar e misturar ainda mais os dados: substituir bytes, rotacionar a linha da matriz, aplicar transformação matemática nas colunas. A cada rodada os dados ficam cada vez mais irreconhecíveis, e até hoje nenhuma vulnerabilidade foi encontrada no AES quando usado da forma certa. É usado desde Wi-Fi, criptografia de disco, até em VPNs.

**O problema da criptografia simétrica é a troca de chaves.** Como passar para uma pessoa uma chave secreta de forma segura? Por e-mail um invasor pode pegar; por mensagem pode vazar; pessoalmente é difícil de escalar para várias pessoas. Esse problema é chamado de **key distribution problem**.

### Criptografia Assimétrica — RSA

A ideia: e se tivesse duas chaves, uma pública que todo mundo pode ter e uma privada que só uma pessoa pode ter? Daí nasceu a criptografia assimétrica.

Um exemplo é o **RSA**, baseado na propriedade de números primos: fatorar números grandes em seus primos é extremamente difícil computacionalmente, e essa dificuldade é o que traz a segurança do RSA.

Funciona assim:
1. Escolhe-se dois números primos grandes, P e Q (precisam ser grandes para garantir segurança).
2. Calcula-se N = P × Q.
3. Calcula-se o totiente de Euler — função que conta quantos números menores que N são coprimos com N.
4. Escolhe-se um expoente público **e**, que precisa ser primo em relação ao totiente.
5. Calcula-se o expoente privado **d**.

A chave pública que todo mundo pode ter é (e, N), e a chave privada que só o dono pode ter é (d, N). Para criptografar, converte-se a mensagem para forma numérica e aplica-se a função com a chave pública. Para descriptografar é parecido, usando a chave privada.

## IND-CPA — Medindo Segurança

Um monte de cálculo e embaralhamento não significa necessariamente que um esquema é seguro. Um dos modelos mais comuns para medir segurança é o **IND-CPA** (indistinguibilidade sob ataque de texto escolhido — *Indistinguishability under Chosen Plaintext Attack*).

A ideia: um atacante pode mandar quantas mensagens diferentes ele quiser para serem criptografadas (o **chosen plaintext**, ele escolhe o texto original e vê como fica criptografado). A **indistinguibilidade** significa que, se um atacante criptografa duas mensagens diferentes do mesmo tamanho e recebe de volta só uma das cifras, ele não consegue identificar qual mensagem gerou aquela cifra. Um sistema é IND-CPA seguro se o atacante não consegue adivinhar qual foi a mensagem criptografada, com probabilidade melhor que a de um chute aleatório.

**Exemplo: a cifra de César não é IND-CPA segura.** Se um atacante pede para criptografar duas mensagens diferentes do mesmo tamanho e recebe a cifra, dá para descobrir qual mensagem gerou aquela cifra, porque a cifra de César sempre substitui o caractere X pelo mesmo Y. Por exemplo: se numa das mensagens candidatas a letra "E" aparece nas mesmas posições em que a letra "H" aparece na cifra, a correspondência de padrão de repetição de caracteres entrega qual foi a mensagem original.

## A Ameaça Quântica: Shor e Grover

Além de doutor em matemática, agora seria preciso ser doutor em física quântica. Em 2025 já existem computadores quânticos rápidos, o que pode ser considerado uma ameaça para os sistemas de criptografia atuais.

- **Algoritmo de Shor**: algoritmo quântico capaz de resolver o problema da fatoração de inteiros em tempo polinomial, ou seja, de forma eficiente. Isso é uma ameaça gigantesca para criptografias baseadas na dificuldade de fatoração de inteiros, como o RSA — um computador quântico pode quebrar esse algoritmo em minutos.
- **Algoritmo de Grover**: dá uma aceleração quadrática para busca em dados não ordenados. Não quebra diretamente uma criptografia simétrica, mas pode acelerar bastante um ataque de força bruta.

Hoje isso não é um problema prático (ninguém tem um computador quântico poderoso em casa), mas levanta uma ameaça do tipo **"colha agora, decifre depois"** (harvest now, decrypt later): a ideia é coletar dados criptografados hoje, armazená-los, e esperar ter um computador quântico poderoso o suficiente para decifrá-los depois.

## Hashing

Diferente da criptografia que pode ser criptografada e descriptografada, o **hash é unilateral** — é praticamente impossível reverter um valor de hash para encontrar a entrada original. Mesmo trocando só uma pequena coisa na entrada, o resultado final é totalmente diferente. Essa técnica é usada para verificação de integridade de arquivos, blockchain, assinatura digital e, principalmente, armazenamento de senhas.

### O Problema do Hash Determinístico em Senhas

MD5 e SHA-256 foram e ainda são muito usados para armazenar senhas, mas isso não é seguro: esses métodos são **determinísticos** — não importa quantas vezes você passa o mesmo input, o resultado sempre vai ser o mesmo (o MD5 de "123456" sempre vai ser o mesmo hash).

Isso é um problema porque atacantes, ao longo de muitos anos, construíram bancos de dados de bilhões de senhas e seus hashes correspondentes — isso é chamado de **rainbow table**. A partir de um hash, alguém consegue descobrir a entrada original consultando essas tabelas.

### Salt e Pepper

Para resolver esse problema entra o conceito de **salt**: um valor aleatório adicionado junto da senha antes de gerar o hash. Em vez de fazer hash direto de "123456", adiciona-se algo aleatório antes e só então gera-se o hash. Isso torna as rainbow tables inúteis, porque cada hash resultante agora depende também do salt.

Além disso, existe o conceito de **pepper**: enquanto o salt é aleatório (e armazenado junto ao hash), o pepper é fixo e secreto (guardado à parte, por exemplo em variável de ambiente do servidor). O hash final é a concatenação do salt, da senha e do pepper.

**Nunca use algoritmos determinísticos como MD5 para senhas.** Use BCrypt ou Argon2, que são as melhores opções atualmente.

### BCrypt

O BCrypt é baseado no algoritmo Blowfish, especificamente uma variante chamada EKS-Blowfish (Expensive Key Schedule Blowfish). Ele faz com que o hash seja **lento de propósito**, dificultando muito ataques de força bruta. Para gerar o hash de uma senha, tem-se a senha, um salt aleatório e um fator de custo que define quantas iterações vão ser feitas — e é aí que entra o EKS-Blowfish, misturando o salt e a senha várias vezes.

Uma curiosidade: o algoritmo do BCrypt só faz o hash dos 72 primeiros caracteres da senha — se a senha passada tiver mais que isso, o excesso é literalmente ignorado.

### Argon2

O Argon2 é o mais indicado atualmente, mais especificamente o **Argon2id**. Foi feito para consumir bastante memória RAM e ser resistente a ataques paralelos (GPU). Funciona em três fases:

1. Concatena a senha e o salt e aplica uma função de hash inicial.
2. Preenche uma matriz — primeiro com acessos previsíveis (evita ataque side-channel), depois com acessos aleatórios (bloqueia ataques de GPU).
3. Mistura os últimos blocos e gera o hash final numa única string.

---

Vídeo cobre os pontos mais importantes sobre criptografia hoje em dia, com bastante conteúdo resumido e omitido — o tema é muito maior do que um vídeo de 10 minutos.
