# HMAC: Garantindo Integridade de Mensagem em Local-First (Pergunta de Entrevista de System Design)

> Transcrição de vídeo. Formatada em Markdown para ingest na wiki, sem alteração de conteúdo ou opinião do autor. Já estava em português, sem necessidade de tradução; fala corrida (ASR, sem pontuação) foi limpa de repetições e organizada em seções para leitura, sem alterar o conteúdo técnico.

O autor descreve esta como uma das perguntas de entrevista de system design com menor taxa de acerto — nível médio/avançado, envolvendo segurança e criptografia, tema pouco comum nesse tipo de entrevista.

## O problema

Cenário: um `cart service` computa o valor final de um carrinho — aplica descontos, calcula preço unitário e total — e gera um payload com ID do produto, quantidade, preço unitário e preço total. Esse payload é enviado para um ambiente local do usuário (um app). O servidor **não quer armazenar** esse carrinho calculado (evitar custo de storage), mas precisa **garantir que o preço que o usuário está vendo localmente é o mesmo que será recebido de volta** quando o carrinho for enviado para fechamento.

Isso é o padrão conhecido como **local-first**: o dado local no cliente é tratado como dado real, fidedigno, sem precisar ser persistido no servidor.

A pergunta central: como garantir **integridade da mensagem sem armazená-la no servidor**?

## Tentativa 1: criptografar o payload

Resposta comum e incompleta: criptografar o dado inteiro antes de mandar para o cliente. Isso garante consistência — na volta, o servidor decripta e confirma que é o mesmo dado — mas **quebra a exibição**: se o payload está criptografado, o cliente não consegue descriptografar e não consegue mostrar o preço ao usuário. Criptografia resolve confidencialidade/consistência, mas ao custo de perder a legibilidade na ponta que precisa exibir o dado.

## Tentativa 2: chave assimétrica (assinatura digital)

Segunda resposta comum: usar par de chaves pública/privada — assinar com a chave privada do servidor, o cliente verifica com a chave pública (ou o inverso). Isso resolveria o problema de integridade sem impedir a exibição do payload em claro.

**Problema**: algoritmos de chave assimétrica (ex.: RSA) são **computacionalmente muito mais custosos** que criptografia simétrica ou hashing. Em alto volume, esse custo penaliza a aplicação. Por isso o autor não recomendaria chave assimétrica para esse cenário.

## Tentativa 3: secret + mensagem concatenados, hash simples

Terceira ideia comum: manter um segredo (`secret`) no servidor, concatenar `secret + mensagem` e gerar um hash (ex.: MD5) desse resultado, mandando o hash como header HTTP junto com o payload no corpo (body).

Essa é o caminho certo na direção certa, mas **não é suficiente**: segundo especialistas em segurança (o autor se declara não-especialista, citando o consenso da área), essa abordagem de "hash(secret + mensagem)" é fácil de burlar. Com tempo e poder computacional, é possível explorar o padrão interno do algoritmo de hash e fazer **extensão de mensagem** (mensagem original + dados extras) preservando o mesmo hash — porque o segredo fica no início da concatenação, e os algoritmos de hash processam por blocos, expondo esse padrão. Simplesmente concatenar um segredo na frente da mensagem não gera entropia suficiente para tornar a mensagem seguticamente segura.

## A solução: HMAC (Hash-based Message Authentication Code)

HMAC é o padrão (definido em RFC, ver RFC 2104) que resolve exatamente esse problema com baixo overhead computacional — muito mais barato que chave assimétrica — mantendo a garantia de integridade.

### A ideia central

Em vez de simplesmente concatenar um segredo com a mensagem, o HMAC **deriva duas chaves a partir da mesma chave secreta**: uma chave interna (`ipad` — inner pad) e uma chave externa (`opad` — outer pad).

- **Pad interno**: byte `0x36`, repetido até o tamanho do bloco do algoritmo de hash (64 bytes para MD5/SHA-1).
- **Pad externo**: byte `0x5C`, repetido até o mesmo tamanho de bloco.

Esses dois bytes (`0x36` e `0x5C`) foram escolhidos pelos pesquisadores do paper original por serem "os mais distantes" entre si em termos de bits — minimizam a chance de colisão e maximizam a entropia entre chave interna e chave externa.

### Normalização da chave

A chave secreta precisa ser ajustada para o tamanho do bloco do algoritmo (64 bytes, no caso de MD5/SHA-1):

- Se a chave for **menor** que o tamanho do bloco, ela é completada com padding de zeros.
- Se for **maior**, ela é reduzida aplicando hash sobre ela mesma (o resultado do hash já cabe no tamanho do bloco).

Com a chave normalizada no tamanho do bloco, dá para fazer XOR (`shore`/`xor` na fala transcrita) entre a chave e cada pad, obtendo a chave interna e a chave externa.

### As duas etapas de hash

```
chave_interna = chave_normalizada XOR ipad (0x36 repetido)
chave_externa = chave_normalizada XOR opad (0x5C repetido)

hash_1 = Hash(chave_interna || mensagem)        # etapa 1 — equivalente ao "hash(secret+msg)" ingênuo, mas com a chave já com padding
hash_final = Hash(chave_externa || hash_1)      # etapa 2 — HMAC propriamente dito
```

A etapa 1 sozinha é essencialmente a abordagem ingênua do passo anterior (concatenar segredo + mensagem e fazer hash) — mas usando a chave com padding, não a chave crua. A diferença decisiva é a **etapa 2**: em vez de concatenar diretamente com a mensagem original, o HMAC concatena a chave externa com o **hash resultante da etapa 1**. Isso dificulta bastante o ataque de extensão de mensagem, porque o atacante não está mais manipulando a mensagem original diretamente — está lidando com um hash intermediário protegido por uma segunda chave derivada.

O `hash_final` é o HMAC, enviado no header da requisição junto com o payload (body) em claro.

### Fluxo completo na prática

1. Servidor calcula o carrinho, gera o payload (body) e o HMAC do payload (header) usando seu `secret`.
2. Servidor manda body + header (HMAC) para o cliente — **nada é persistido no servidor**.
3. Cliente exibe o payload normalmente (está em claro, não criptografado).
4. Quando o cliente reenvia o carrinho para fechamento, ele reenvia o mesmo body e o mesmo header HMAC recebido.
5. Só o servidor tem o `secret` — ele recalcula o HMAC (chave interna, chave externa, duas etapas de hash) sobre o body recebido e compara com o header recebido.
6. Se os dois HMACs baterem, o servidor tem garantia de que o payload não foi alterado desde que ele mesmo o gerou — sem precisar ter armazenado nada.

### Por que verificar algo que o próprio servidor gerou?

A pergunta que surge: por que gerar um payload e depois validar o mesmo payload que você mesmo gerou? A resposta é o ganho de **não precisar armazenar** o carrinho. Em um e-commerce com milhões de carrinhos sendo criados e alterados continuamente, o custo de armazenamento e de busca (lookup) é real:

- Banco relacional: precisaria de índice em memória sobre milhões de registros — custo computacional alto.
- Banco não-relacional (ex.: DynamoDB): também tem custo de leitura/escrita por lookup.

Ao jogar esse estado para o cliente (local-first) e usar HMAC só para validar integridade na volta, o servidor **elimina o custo de storage e de descarte de carrinho** (não precisa expirar/limpar carrinhos abandonados, porque eles nunca foram persistidos).

### Exemplo em Go (estrutura do algoritmo)

O autor apresenta um exemplo em Go ilustrando os passos: definição do tamanho de bloco conforme o algoritmo de hash (SHA vs MD5, ambos 64 bytes conforme a RFC), as constantes de pad interno (`0x36`) e externo (`0x5C`) definidas pela RFC, normalização (padding) da chave, e as duas etapas de hash (interno, depois externo) até chegar no HMAC final.

## Conclusão

Para o cenário de local-first com necessidade de garantir integridade de mensagem sem persistir o dado, a resposta mais aderente é **HMAC**: um hash duplo, usando chave interna e chave externa derivadas da mesma chave secreta via padding com bytes escolhidos para maximizar distância/entropia entre as duas derivações — garantindo integridade com overhead computacional baixo comparado a chaves assimétricas.

O autor recomenda a leitura da RFC do HMAC (curta) para quem quiser entender a origem dos bytes de padding e como o esquema garante segurança.
