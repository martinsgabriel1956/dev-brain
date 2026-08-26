# Armazenamento Seguro de Senhas: Hashing, Salting e Peppering

> Transcrição de vídeo. Patrocínio inicial (cadeira SF, cupom "galego") removido do corpo do texto por ser publicidade, não conteúdo técnico.

Esse vídeo tem dois objetivos, e apenas dois objetivos. O primeiro é servir de introdução ao armazenamento de senhas. Eu não sou um expert em criptografia, não sou um expert em cybersegurança, não sou um expert em autenticação — por isso estou fornecendo apenas uma introdução, e o objetivo explícito dela é prevenir que você cometa erros monumentais na hora de armazenar as senhas no seu aplicativo.

Vamos falar hoje sobre o que é hashing, o que é salting, o que é peppering, e como geralmente é recomendado utilizar esses três conceitos em conjunto para armazenar senhas. Ao entender isso, muitos de vocês vão perceber que estavam fazendo da maneira errada e podem começar a fazer da maneira certa. E espero que isso também faça vocês darem mais valor a outros métodos, como usar multifactor authentication ou usar alguém que providencia esse serviço para você — um Cognito ou algo nesse sentido.

## O Modelo de Ameaça: Duas Formas de Atacar Senhas

A primeiríssima coisa que precisamos entender sobre senhas é isto: supondo que você armazena no seu banco de dados o ID do usuário, o e-mail e a senha, isso tem dois problemas — duas ameaças que precisamos entender para saber como evitá-las.

Existem dois modelos de ameaça: o ataque **online** e o ataque **offline**.

**Ataque online**: um atacante tentando adivinhar a senha vai testar todas as senhas possíveis, uma atrás da outra, até o login ser bem-sucedido. Hashing, salting e peppering não necessariamente previnem esse ataque — afinal, se o usuário ficar testando várias senhas, alguma hora o login funciona.

**Ataque offline**: alguém conseguiu acessar o seu banco de dados de alguma maneira — as informações vazaram. Se as senhas estivessem em texto plano no banco, o atacante já tem a senha para aquele aplicativo — e, como as pessoas reutilizam senhas, possivelmente também para várias outras aplicações.

## Defendendo Contra o Ataque Online

No ataque online, existem várias formas de evitar que o atacante fique testando todas as senhas possíveis até obter sucesso:

- **Rate limit** na frente da aplicação — não deixar um usuário fazer 10.000 requests em paralelo tentando fazer login. Pode ser baseado em dispositivo, em IP, ou no próprio usuário (ex.: bloquear a conta depois de 5 tentativas erradas).
- **MFA (Multifactor Authentication)** — o código do autenticador, ou um código enviado por WhatsApp/e-mail depois que a senha for acertada, garante que é realmente o dono da conta e não alguém que só adivinhou a senha.

Um conjunto de todas essas coisas — rate limit, bloqueio de conta após tentativas, MFA — bem implementado cobre 99,99% dos casos de ataque online.

## Defendendo Contra o Ataque Offline

Aqui o cenário é mais complexo: o atacante tem acesso ao banco de dados, conseguiu efetivamente o dump das senhas. Mesmo nesse caso, MFA ainda pode salvar. Mas também é possível fazer com que o acesso à senha não seja garantia de conseguir logar, mesmo sem MFA.

### Nunca Armazenar Senha em Texto Plano

Isso está errado em todas as circunstâncias, sem exceção.

### Hashing

Uma função de hash aplicada a um input sempre produz o mesmo output — e o caminho é de mão única: dado o hash, não dá para deduzir a senha original. Mas a mesma senha, com os mesmos parâmetros, sempre produz o mesmo hash.

Ao invés de armazenar a senha, armazenamos o **password hash** — o resultado de passar a senha pela função de hashing.

### Brute Force

Mesmo com hashing, o atacante pode tentar adivinhar a senha por força bruta: testar sistematicamente candidatas e comparar o hash resultante. Isso costuma ser feito de forma refinada:

1. Primeiro, as senhas mais comuns do planeta (existe uma tabela de senhas super comuns).
2. Depois, ataque de dicionário — testar todas as palavras de um dicionário.
3. Depois, geração algorítmica de todas as combinações possíveis.

O tamanho do espaço de busca cresce rapidamente: com 26 letras minúsculas e senha de 8 caracteres, são 26⁸ combinações. Adicionar maiúsculas leva a 52; adicionar dígitos (0–9), a 62; adicionar caracteres especiais aumenta ainda mais. É por isso que sites exigem senha com minúscula, maiúscula, número e caractere especial — para aumentar esse número e tornar o ataque computacionalmente mais caro. (Essa exigência é um pouco controversa, mas o motivo é esse.)

Mesmo assim, computadores atuais fazem trilhões de cálculos por segundo. Por isso, além de exigir senhas com espaço de busca grande, usamos propositalmente uma **função de hash lenta**. Quando usamos um hashmap dentro de uma linguagem de programação, queremos que o cálculo seja o mais rápido possível; quando guardamos uma senha, queremos o oposto — que o cálculo seja lento e caro, tanto em CPU quanto em memória, para tornar o ataque de força bruta economicamente inviável.

Com uma senha longa (16–24 caracteres, com minúscula, maiúscula, número e caractere especial) e uma função hash computacionalmente cara, o tempo estimado para quebrar por força bruta, no poder de computação atual, é medido em bilhões de anos.

Sobre computação quântica: já existem testes com computadores de mais de mil qubits, mas também já existem algoritmos de hashing não quebrados por computação quântica. Hoje, um dos algoritmos mais recomendados é a família **Argon2**, especificamente o **Argon2id**.

### Salting

Hashing sozinho ainda tem um problema: a mesma senha, com os mesmos parâmetros, sempre gera o mesmo hash. Se Alice e Bob tiverem a mesma senha, o hash armazenado será idêntico — o que possibilita um **ataque de senhas pré-computadas**: o atacante mantém uma tabela de hashes já calculados e o que cada um mapeia. Isso também revela que dois usuários compartilham a mesma senha — e um vazamento de outra aplicação mais fraca (ex.: um provedor de e-mail antigo que faliu) pode permitir deduzir a senha de outra pessoa pelo hash idêntico.

A solução: adicionar um número aleatório — o **salt** — antes de fazer o hash. Bob tem salt "123", Alice tem salt "456"; mesmo com a senha "1234" para ambos, o hash resultante é diferente. O salt é armazenado junto ao password hash, por usuário, no mesmo banco de dados — não precisa ser secreto. Mesmo que o atacante tenha acesso ao resto do banco e ao salt, o ataque de senhas pré-computadas continua inviável, porque ele precisaria recalcular tudo de novo especificamente para aquele salt.

O salt deve ser gerado por uma lib (geralmente a mesma lib que faz o hashing), não implementado manualmente, e deve ser: aleatório, grande e único por usuário. Se o salt for o mesmo entre dois usuários, ainda dá para identificar que eles têm a mesma senha.

Com hash + salt, a senha fica muito difícil de ser quebrada: o ataque demora bilhões de anos e não há lookup reverso possível, já que o salt é único por usuário e por aplicação.

### Peppering

Ainda existe um cenário em que o atacante tem hash, salt e sabe qual algoritmo foi usado (ex.: Argon2id) — se a senha do usuário for relativamente fraca (ex.: 8 caracteres), ainda pode ser possível quebrar. A técnica de **peppering** adiciona um segundo salt secreto, que o atacante não tem acesso porque **não fica armazenado no banco de dados** — se o banco vazar, o pepper continua protegido.

O pepper é opcional e um pouco controverso. Geralmente é um valor único por aplicação (não por usuário), secreto, armazenado em local diferente do banco — tipicamente um secrets manager (AWS Secrets Manager, Google Secrets Manager).

Combinando hash + salt + pepper corretamente, hoje em dia isso torna um ataque offline impossível, mesmo com acesso total ao banco de dados — dado que a senha é minimamente longa.

**Por que pepper é controverso**: errar com salt/hash na tabela é relativamente contido. Errar com o pepper no secrets manager — perder o valor, fazer um deploy errado, trocar a senha do secrets manager por engano — invalida **todas** as senhas do aplicativo de uma vez, para 100% dos usuários, sem possibilidade de reconstrução. Todo mundo precisaria criar senha nova. Por isso é considerado arriscado.

## Recomendações Práticas

A implementação correta de tudo isso é difícil, exige experiência e muito cuidado. Três recomendações fortes, em ordem crescente de terceirização:

1. **Use libs consagradas.** Não invente sua própria lib, hash ou salt. Use Argon2, siga a documentação, implemente do jeito padrão de mercado.
2. **Use um framework de mais alto nível**, como **Better Auth**, que cuida da parte de armazenamento e hashing por você. Faz sentido especialmente para quem é solo founder de um SaaS — desenvolvedores não são necessariamente bons em segurança, então às vezes é melhor confiar em algo já testado.
3. **Terceirize completamente com um identity provider** — **Clerk** (ficou muito popular recentemente), **Auth0**, **Cognito** (AWS), entre outros. Toda a parte de login é feita pelo provedor; você não lida com essa dor de cabeça.

Existe ainda a opção de nem ter senha: login via **Magic Link** por e-mail, ou autenticação social (Google, GitHub). Para SaaS B2C, o autor prefere pessoalmente não lidar com senha — login via Google/GitHub elimina boa parte dessa dor de cabeça (opinião pessoal).

## Conclusão

Muitas aplicações do mundo real estão vulneráveis nesse sentido — senha em plaintext ou com criptografia antiga/fraca. Vale verificar se o algoritmo usado no seu produto (ou na empresa onde você trabalha) é compatível com o estado da arte atual — existem algoritmos recomendados, menos recomendados, e algoritmos já considerados facilmente quebráveis.

Este vídeo é introdutório: o objetivo é ensinar pelo menos o que **não** fazer, mesmo que fazer certo, na prática, seja mais difícil do que essa introdução cobre.
