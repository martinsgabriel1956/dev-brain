# Vibe coding, .env exposto, IDOR, account takeover e RCE numa loja feita com IA

> Transcrição de vídeo (YouTube), canal de Geraldo Alcântara (pentester), sobre um pentest educacional em ambiente controlado contra uma loja fictícia ("Lucas") construída com ferramentas de vibe coding (Cursor, Lovable, Claude Code).

Você passou semanas construindo a sua loja com IA — Cursor, Lovable, Claude Code. Você descreveu o que queria e a IA construiu. Seus clientes confiaram em você, cadastraram nome, e-mail, dados de pagamento. Mas enquanto sua loja estava no ar, eu estava do outro lado. Em menos de 10 minutos eu tinha acesso a tudo. E hoje eu vou te mostrar o passo a passo.

Esse aqui é o Lucas — poderia muito bem ser você. 26 anos, designer, criador de conteúdo, passa os dias no Figma, no Lightroom, no Notion. Nos últimos dois anos foi acumulando ativos digitais: templates de apresentação para Notion, presets de foto para fotógrafos, packs de ícones para designers. Vendia tudo isso pelo Gumroad, mas cansou de pagar comissão, de não ter controle dos dados dos clientes e de depender sempre de plataforma de terceiro.

Aí veio a IA. Em uma semana o Lucas tinha sua própria loja: página de produto, checkout, entrega automática do arquivo, painel para ver as vendas — tudo com cara profissional. Postou no Twitter: "Larguei o Gumroad, minha loja tá no ar." Likes, retweets, elogios, e os primeiros clientes compraram, confiaram nele.

O que o Lucas não sabia é que a IA que construiu a loja dele nunca pensou em segurança uma única vez. E eu vou te mostrar isso agora.

Caso você não me conheça, meu nome é Geraldo Alcântara, sou pentester, e esse canal fala sobre cibersegurança e hacking.

Se você utiliza IA para gerar código, presta atenção nisso: pesquisadores encontraram 35 CVEs só em março desse ano relacionados a código gerado por IA — mais do que a somatória dos 7 meses anteriores. Além disso, segundo a Veracode, 45% das amostras de código gerado por IA têm vulnerabilidades contidas no OWASP Top 10. Se você tem qualquer produto no ar feito por IA e nunca fez um teste de segurança, é muito possível que você já tenha alguma dessas falhas nesse momento.

Antes de partir pro vídeo: tudo está sendo feito em um laboratório, em ambiente controlado. Se você quiser fazer seus próprios testes, lembre-se de sempre testar sistemas que você tem autorização para testar.

## A investigação

A loja que a IA fez pro Lucas é bonita, profissional — qualquer um colocaria o cartão de crédito ali. Com o Burp Suite aberto, capturando todas as requisições, o interessante não é apenas entender o que a aplicação faz, mas o que ela não protege.

Antes de mais nada, um teste que normalmente a IA não ajuda a proteger, e que é assustadoramente fácil de fazer: usar o dirsearch (ferramenta de brute force de diretórios/arquivos) para encontrar caminhos que a aplicação não está mostrando.

Em poucos minutos o dirsearch encontrou algo assustador: um arquivo `.env` exposto publicamente, acessível por qualquer usuário com um navegador. Dentro dele: secret key, chaves do Stripe, e um usuário de teste que o desenvolvedor criou para testar a aplicação e esqueceu de remover ao subir para produção.

### Login com credenciais vazadas

Com as credenciais do `.env`, login imediato na aplicação com o usuário de teste do desenvolvedor. Dentro, uma rota `/admin` aparece no output do dirsearch — mas o usuário de teste não tem acesso a ela, pelo menos não diretamente.

### IDOR nos pedidos

Navegando pela área do usuário: produtos, pedidos. Abrindo um pedido: nome do cliente, e-mail, endereço, produto comprado, token de download. O ID do pedido na URL é um número simples e sequencial — adivinhando outro ID, acesso direto aos dados de pedido de outro cliente (nome, e-mail, endereço, token de download), sem nenhuma verificação de que aquele pedido pertence ao usuário autenticado. Um IDOR (Insecure Direct Object Reference) clássico.

### A chave de integração no perfil

Na aba de perfil do usuário de teste: nome, e-mail, telefone, data de cadastro, e uma "chave de integração". A aplicação usa essa chave para autenticar via `POST /api/login`, retornando um cookie de sessão. O ID do usuário na URL do perfil também é um número simples — nesse caso, o número 7.

Trocando o ID de 7 para 1 na URL do perfil: outro IDOR, expondo o perfil (e a chave de integração) de outro usuário, "Carlos". Usando a chave de integração do Carlos no endpoint de autenticação, a aplicação retorna um cookie válido — login efetivo como Carlos, sem senha, sem MFA. Um account takeover completo, usando apenas a numeração sequencial de outro endpoint já vulnerável.

### Escalando para admin via força bruta no Burp Intruder

O perfil do Carlos mostra `role: user`. Em vez de repetir a enumeração manualmente usuário por usuário, a etapa é automatizada com o Burp Intruder: a requisição `GET /profile` é enviada ao Intruder, o ID na URL é marcado como payload, e um payload set numérico de 1 a 15 é configurado. Cada resposta é inspecionada com "Grep - Extract" para capturar o valor do campo `role`.

A varredura mostra `role: user` para a maioria dos IDs, `404 Not Found` para IDs inexistentes — e um ID (o 6) sem o valor `user` no grep. A resposta completa desse perfil revela a conta do próprio Lucas, dono da loja, com `role: admin`.

Usando a chave de integração do perfil do Lucas (ID 6) no mesmo endpoint de autenticação, a aplicação gera um cookie de sessão de administrador. Login completo como administrador do sistema — a partir de um `.env` exposto, sem nenhuma senha quebrada.

### Painel administrativo e RCE via upload de plugin

No painel admin: receita da loja, dados de todos os usuários, e uma aba de plugins com a opção de instalar um plugin próprio. Fazendo upload de um plugin malicioso e executando a instalação, o resultado é remote code execution (RCE) — comandos executados diretamente no servidor (`ls`, `pwd`, leitura de `/etc/passwd` confirmando acesso ao sistema de arquivos do host).

Em menos de 10 minutos, a partir de um único arquivo `.env` exposto, a cadeia completa (credenciais vazadas → IDOR em pedidos → IDOR em perfil/account takeover → escalonamento para admin via enumeração de IDs → RCE via upload de plugin sem validação) deu controle total sobre a loja do Lucas.

## Como se proteger

1. **Nunca exponha um arquivo `.env` publicamente.** Configure o servidor para bloquear acesso a qualquer arquivo que comece com ponto.
2. **IDOR:** antes de retornar qualquer dado, a aplicação precisa verificar no backend se o usuário autenticado tem permissão sobre aquele recurso específico — nunca confiar no ID vindo direto da requisição sem checar contra a sessão ativa. Vale para pedidos, perfil, download, ou qualquer outro recurso.
3. **Upload restrito** (o vetor do RCE): validar o MIME type no backend, não só no frontend; restringir extensões aceitas ao estritamente necessário (ex.: apenas JPG/PNG para fotos); salvar arquivos fora de diretórios públicos do servidor; nunca executar dinamicamente arquivos vindos de usuários.
4. **Ter um dev ou alguém de segurança envolvido** no processo de vibe coding é o caminho mais seguro para atingir maturidade de segurança razoável. Alternativas complementares: rodar um scanner como o OWASP ZAP e levar os achados de volta para a IA corrigir; rodar análise estática de código; pedir para a própria IA revisar o código em busca de brechas de segurança.
5. **Nunca commitar credenciais no repositório** — usar `.gitignore` desde o primeiro commit.

O Lucas é fictício, mas os erros que ele cometeu são reais.
