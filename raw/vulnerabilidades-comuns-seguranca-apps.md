# O maior problema de segurança do seu app não tá na rede

> Transcrição de vídeo sobre vulnerabilidades comuns em aplicações web/SaaS e como corrigi-las.

O maior problema de segurança do seu app ou SaaS não tá na rede, nem em grandes exploits. Tá entre a cadeira e o monitor. O problema não é que seu código pode ser hackeado, é que você já deixou ele praticamente aberto.

Este vídeo mostra as vulnerabilidades mais comuns encontradas em aplicações reais e como corrigi-las. Depois desse vídeo, cometer esses erros não é mais descuido, é sabotagem.

O foco não é falar sobre grandes CVEs ou redes, ainda mais considerando que a aplicação provavelmente está hospedada na Vercel, Fly ou outra grande empresa que já oferece um certo tipo de proteção, e que o uso de ORM dificulta SQL injection e o uso de JSX dificulta XSS. Isso não significa que é impossível sofrer esses ataques, só que não é o escopo deste conteúdo — há infinitos materiais sobre essas vulnerabilidades específicas.

## Webhook mal configurado

Todo mundo gosta de webhook, mas a grande maioria usa sempre a mesma rota (`/api/webhook` ou `/api/hook`). Isso não está tecnicamente errado, mas qualquer um pode ficar chutando rotas possíveis de webhook até encontrar uma.

Se estiver mal configurado, um usuário mal-intencionado pode mandar uma mensagem para a rota fingindo ser o serviço de pagamento, confirmando uma compra que nunca aconteceu.

**Correção:** sempre usar uma assinatura secreta ao configurar um webhook.
- No Stripe: cabeçalho `Stripe-Signature`.
- No Mercado Pago: cabeçalho `X-Signature`.

O backend deve validar esse código para garantir que a requisição veio da fonte certa. Se um usuário mandar uma requisição direto pro webhook, a API deve reclamar que falta a assinatura.

## IDOR (Insecure Direct Object Reference)

Basicamente não verificar permissão ao acessar objetos via API.

Exemplo: um endpoint `GET /purchase/:id`. O usuário manda uma requisição `GET /purchase/123` e a API devolve os detalhes da compra. Mas e se a compra `123` não é dele? Parabéns, acabou de vazar os dados de outro usuário.

Outro erro clássico: um `PATCH /profile` onde o servidor recebe o `userId` no corpo da requisição. **Não façam isso.** O ID do usuário deve vir sempre da sessão, do JWT, do que for — nunca do body da requisição. Sempre validar quem está pedindo acesso antes de mostrar, editar ou excluir qualquer coisa.

## Exposição excessiva de dados (data exposure)

Imagine um marketplace onde é possível acessar um produto mandando uma requisição `GET` com o ID do produto. A API retorna os detalhes do produto e do vendedor — só que junto com nome e foto do vendedor, também vêm e-mail, CPF, telefone, endereço e senha criptografada.

Isso acontece porque, ao buscar o produto, a query também trouxe os dados do vendedor por inteiro, sem filtrar o que realmente devia ser enviado ao frontend.

**Correção:** enviar somente o que for realmente necessário para o frontend. Se só precisa do nome e da foto do vendedor, envie só isso. Não parta do princípio de "ah, o frontend só usa o que precisa" — proteja os dados na origem.

## Falta de rate limit / captcha

Não colocar rate limit ou captcha em certos lugares pode não ser uma vulnerabilidade direta, mas é uma das coisas que mais prejudica o produto.

- Uma API pública de `POST` sem limitação permite que um atacante automatize a criação de milhares de posts falsos, poluindo o banco de dados e degradando a experiência dos usuários. Armazenamento em banco é caro, então isso também custa dinheiro.
- Uma API de envio de e-mail sem limitação permite que um atacante exploda o limite de envios, gerando custo extra para conseguir voltar a enviar e-mails.
- Uma página de login sem proteção permite ataques de brute force para descobrir senhas.

**Correção:** implementar captcha, rate limit ou outros mecanismos em lugares sensíveis ou caros.

## Mass assignment (atribuição em massa)

Em uma rota `PATCH` que altera informações de um objeto (ex: `username`, descrição de um produto), essa vulnerabilidade permite alterar qualquer propriedade do objeto — não só o campo pretendido. Assim, além de alterar o nome de usuário, o usuário também consegue alterar o próprio cargo para `administrador` (ou qualquer outra propriedade sensível).

**Correção:** definir explicitamente quais campos podem ser alterados via cada rota (allowlist de campos), nunca aceitar o objeto inteiro.

## TOCTOU (Time of Check to Time of Use)

Vulnerabilidade causada por um intervalo de tempo entre verificar uma condição (o *check*) e usar o resultado (o *use*).

Exemplo clássico: você tem R$ 100 na conta e pede para sacar os R$ 100. O programa verifica se você tem o dinheiro e, se tiver, faz o saque. Mas se você mandar várias requisições ao mesmo tempo (o delay de rede naturalmente já gera esse efeito), a função é executada várias vezes em paralelo, todas passam pelo *check* de saldo antes que qualquer *use* (saque) seja processado — resultando em múltiplos saques com apenas R$ 100 de saldo.

Isso vale para vários cenários: like em uma publicação, compra de tickets, etc.

**Correção:** travar os recursos críticos enquanto estão sendo usados. Pode-se usar semáforos, sistema de filas, mas o mais comum são **transactions no banco de dados**, garantindo que o check e o use aconteçam de forma atômica — a operação acontece por completo ou não acontece nada.

## Confiar no frontend

Muita gente acha que validar só no frontend já é suficiente — afinal, se o botão está desabilitado, a requisição nunca seria enviada; se o frontend diz que você tem R$ 10 disponíveis, você só pode sacar R$ 10, porque "foi o servidor que informou isso ao front". Não é bem assim: qualquer regra que está no frontend pode ser ignorada ou manipulada pelo usuário, principalmente em aplicações CSR.

### Demonstração (exemplo com uma plataforma de apostas)

1. A tela mostra "saque indisponível" — isso é uma renderização condicional.
2. Localizando no código a condição que decide entre "saque indisponível" e o botão de resgatar.
3. Um breakpoint é colocado nessa condição e a página é recarregada.
4. Via código no debugger, as variáveis do frontend são alteradas manualmente: o `amount`/`grossAmount` é modificado e uma flag é forçada para `true`, liberando o botão de saque na interface — mesmo sem saldo real.
5. Ao clicar em "sacar com PIX", a requisição vai para o backend, mas como o backend valida server-side o que foi realmente creditado (não confia no que o frontend envia), a requisição falha.

Isso mostra que toda renderização condicional do lado do cliente pode ser falsificada.

### Outro exemplo: e-commerce

Se o preço é calculado no frontend e enviado ao backend, um atacante pode interceptar a requisição e alterar o preço para, por exemplo, 50 centavos.

**Correção:** o backend precisa ter controle total sobre valores sensíveis — nunca confiar em preço, saldo ou permissões vindas do cliente. Sempre recalcular no servidor e comparar/validar antes de processar. Se o sistema depende só do frontend para segurança, alguém vai burlar.

## Considerações finais

Segurança 100% não existe e nunca vai existir. Todo programa usado para criar ou hospedar um app foi feito por seres humanos, e humanos erram — pode ser um bug no seu código, no framework, no banco de dados ou no sistema operacional. Mesmo com código perfeito, nada impede uma invasão física ao servidor, o roubo de credenciais de um funcionário do provedor de hospedagem, ou um phishing bem-sucedido.

Segurança é um jogo infinito. O objetivo não é estar 100% seguro, mas dificultar ao máximo o ataque e reduzir os danos caso algo dê errado.
