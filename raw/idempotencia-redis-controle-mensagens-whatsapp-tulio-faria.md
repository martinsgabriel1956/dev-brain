# Idempotência com Redis — Controle de Mensagens WhatsApp (Tulio Faria, DevPleno)

> Transcrição de vídeo do canal DevPleno, apresentado por Tulio Faria. Conteúdo original em português — sem necessidade de tradução.

Você sabe o que é idempotência? Nesse vídeo a gente vai falar sobre o conceito e eu vou te dar um exemplo prático de como que você pode implementar idempotência com Redis, e também aonde eu utilizei e aonde você pode utilizar em um sistema que você tenha ou tenha que desenvolver.

Olá! Aqui é o Tulio Faria do DevPleno e seja muito bem-vindo a mais um vídeo. Nesse vídeo a gente vai ter conceitos e código, mão na massa, então vai ser um vídeo bastante interessante pra gente explorar um pouquinho mais sobre o conceito de idempotência e também sobre a parte prática de como que você pode implementar isso no código.

Antes de começar o nosso vídeo, recados bastante importantes: tem alguns links aqui embaixo, tem a nossa loja de camiseta, a Usedev — as camisetas que eu uso aqui você consegue adquirir lá na nossa loja e ajuda a gente bastante também — e tem um link para um grupo no WhatsApp onde a gente está juntando as pessoas que têm interesse em criar um SaaS. A gente vai começar a colocar alguns conteúdos lá e em breve a gente vai ter uma mentoria também sobre SaaS, então basta clicar no link aqui embaixo para ficar sabendo mais.

E na verdade, a ideia desse vídeo veio exatamente quando eu estava executando o meu SaaS: a gente colocou uma funcionalidade nova e a gente precisou fazer um controle de idempotência. A gente vai começar falando o que é esse conceito e eu vou mostrar para vocês um pouco dos exemplos que a gente pode utilizar.

## O que é idempotência

Se a gente quebrar essa palavra que é muito legal, a gente tem "idem" e tem "potência" — idem de igual e potência de poder. Ele tem um poder, uma característica de ser igual. Qual é a ideia da idempotência? A gente pode falar que a característica também é de ser idempotente.

Inclusive tem na Mozilla uma definição: se a gente fizer várias requisições ou várias chamadas ou várias operações baseado em alguma característica, a intenção é que a gente não mude o estado final.

Você quer um exemplo prático disso? Quando você tenta passar na mesma maquininha várias vezes, o mesmo valor, você vai perceber que a maquininha vai negar os subsequentes. Por quê? Porque ela não sabe se aquilo realmente é uma falha na comunicação ou simplesmente você está tentando várias vezes mesmo. Geralmente a gente faz controle de idempotência quando a gente tem esse cenário: a gente não consegue exatamente saber se a mensagem chegou ou não.

Na Mozilla eles comentam exatamente dos métodos HTTP: o GET, o HEAD, o PUT e o DELETE são idempotentes. A ideia é que se você chamar com os mesmos parâmetros, mesma URL etc., ele não altere ali o estado do servidor. Lógico que o PUT e o DELETE alteram, mas principalmente o GET mantém — se você fizer um GET sempre em `/algum-recurso`, a intenção é que ele sempre retorne a mesma característica, o mesmo estado.

Porém, uma forma melhor que eu gosto de ver idempotência não é exatamente pelo método HTTP, porque se você não implementar corretamente cada verbo, pode ser que você não tenha idempotência implementada corretamente. A ideia aqui foi só trazer que existe esse termo.

## O cenário prático: SaaS + bot de WhatsApp

Vamos para a prática. Imagine que você tem dois sistemas, dois servidores, duas APIs etc. No meu caso, eu tenho o meu SaaS de um lado e um botzinho de WhatsApp do outro. O que acontece: as requisições que eu mando do meu SaaS para o bot precisam ser idempotentes. Por quê? Pode acontecer alguma coisa no meio dessa comunicação que me leve a mandar mais uma mensagem, porque eu não consegui ter a confirmação exatamente do WhatsApp de que a mensagem foi enviada.

Isso foi exatamente o cenário que aconteceu comigo: o meu SaaS precisa mandar uma mensagem no WhatsApp e muitas vezes demorava um pouco a mais, a gente dava timeout, mas a mensagem ia mesmo assim. Então como que você controla isso? Quando a gente consegue controlar essa idempotência, a gente pode retentar essa mensagem com segurança.

## Como resolver: identificar a característica única da requisição

O que é mais importante quando a gente tenta achar uma técnica de idempotência é descobrir qual a característica dessa requisição que faz com que essa mensagem seja identificada como única. Voltando ao exemplo da maquininha de cartão: o que poderia identificar aquilo como único? A mesma maquininha, o mesmo valor, o mesmo cartão de crédito — três características que, combinadas, identificam a requisição como a mesma. O grande trabalho na hora de definir idempotência é exatamente identificar quais características da requisição você vai usar para saber se ela é repetida ou não.

No caso do botzinho de WhatsApp, a gente usou: o telefone do destinatário + o tipo da mensagem + um hash da mensagem. Você pode combinar quais características, quais fatores, você vai levar em conta para saber se aquela mensagem é repetida ou não.

Outra coisa importante: a questão do tempo. No cenário que a gente estava resolvendo, a gente não manda mais uma mensagem para o mesmo telefone, do mesmo tipo, que bata o hash, com uma frequência menor do que 5 minutos. Ou seja: se chegar mais de uma mensagem com tudo igual dentro de 5 minutos, a gente considera que é a mesma mensagem e não manda de novo. Esse foi o controle que a gente fez.

Outras formas, em outros lugares: você pode ter algum ID — por exemplo, um ID de pagamento no Stripe — que já indica se aquilo é idempotente ou não. Vários serviços já fazem esse controle prontos (ex.: Stripe garante que, dado o mesmo ID, você não vai ter dados duplicados nem cobrar no cartão mais de uma vez). O bot de WhatsApp usado aqui não é a API oficial, então foi preciso montar esse controle manualmente.

Resumindo o conceito: idempotência é a característica de usar algum parâmetro da requisição (ou da chamada de uma função) para saber se ela está sendo repetida — e, se estiver, não alterar o estado do serviço, do servidor, nem mandar de novo a mensagem/e-mail.

### Outro exemplo real: limite de SMS por usuário

Um outro exemplo bastante interessante — já usado no trabalho do autor — é controlar quantas mensagens SMS um usuário pode receber. Também usa-se idempotência para isso: existe uma métrica para não mandar muitas mensagens para o mesmo usuário (principalmente usuários americanos, que usam mais SMS), e esse controle é feito com um controle de idempotência para não floodar a mesma pessoa.

## Implementação prática com Redis (Node.js / ioredis)

Existem algumas maneiras de implementar isso no código:

- **Upsert no banco de dados** (`INSERT ... ON CONFLICT`) — se houver colisão em dados específicos, você escolhe rejeitar ou atualizar o dado.
- **Controle via Redis**, útil principalmente para sistemas distribuídos — dois serviços em que um precisa chamar o outro. O controle pode ficar tanto em quem chama quanto em quem recebe a mensagem; em ambos os casos funciona.

Exemplo demonstrado no vídeo (`pnpm init` + `ioredis`, Redis rodando localmente via Docker):

```javascript
const Redis = require("ioredis");
const redis = new Redis();

async function sendSms(phone, message) {
  // chave de idempotência combinando telefone + mensagem
  const idempotencyKey = `idempotency-key:${phone}-${message}`;
  // (poderia usar um hash SHA-256 da mensagem para compactar a chave)

  const sent = await redis.set(idempotencyKey, "1", "EX", 60, "GET");
  // "EX 60": expira em 60s — critério de quanto tempo a requisição é considerada "a mesma"
  // "GET": faz um GET antes do SET — retorna o valor anterior (ou null se não existia)

  if (!sent) {
    console.log("send sms...");
    // envia a mensagem de verdade
  } else {
    // já foi enviado dentro da janela — não reenviar
  }
}

sendSms("11999999999", "Sua mensagem A");
sendSms("11999999999", "Sua mensagem A"); // repetida — não envia (mesmo hash, dentro da janela)
sendSms("11999999999", "Sua mensagem B"); // mensagem diferente — envia
sendSms("11999999999", "Sua mensagem B"); // repetida — não envia
```

O comando central é `redis.set(key, value, "EX", ttlSeconds, "GET")`: o Redis tenta fazer o `SET`, mas com a flag `GET` ele retorna o valor anterior da chave antes de sobrescrever (equivalente a um `GET` seguido de `SET`, atômico). Se o retorno (`sent`) for falso/nulo, quer dizer que a chave não existia ainda — logo a mensagem não tinha sido enviada, e pode ser enviada agora. Se já existir valor, a mensagem já foi enviada dentro da janela de tempo definida pelo `EX`, e o envio é ignorado.

No teste demonstrado: a 1ª chamada envia a mensagem; a 2ª chamada (mesmo telefone + mesma mensagem) não envia, pois já tinha sido enviada; a 3ª chamada (mensagem diferente) envia novamente, porque o hash mudou; a 4ª chamada (repetição da 3ª) não envia. Esperando mais de 1 minuto (o TTL configurado), o ciclo se repete — a mesma combinação volta a ser aceita. Disparando tudo em sequência rápida, todas as mensagens subsequentes dentro da janela são negadas.

## Casos de uso adicionais mencionados

- **Reprocessamento de lote (batch):** se um lote de processamento falhar no meio e precisar recomeçar do zero, a chave de idempotência garante que mensagens já enviadas não sejam duplicadas para o usuário ao reprocessar o lote inteiro.
- **Bot de WhatsApp não-oficial instável:** o bot usado pelo autor não é a API oficial do WhatsApp e é relativamente instável — mensagens às vezes chegavam ao destinatário mesmo quando a confirmação da requisição falhava (timeout). O controle de idempotência garante que, mesmo com retries motivados por esses timeouts, o usuário final receba a mensagem só uma vez (evita "flood" no aparelho do usuário).

## Fechamento

O vídeo encerra reforçando os pontos de call-to-action (like, comentários, grupo de mentoria sobre SaaS) já mencionados na abertura.
