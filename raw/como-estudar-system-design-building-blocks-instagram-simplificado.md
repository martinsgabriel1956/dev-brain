# Como Estudar System Design — Building Blocks e o Caso "Instagram Simplificado"

Fonte: transcrição de vídeo do YouTube (canal e autor não identificados na transcrição), sobre como estudar System Design por meio de um padrão de 5 etapas e de um caso prático ("Instagram simplificado"). Já em português — sem necessidade de tradução. Transcrição automática colada pelo usuário; foram adicionados apenas pontuação, parágrafos e títulos de seção, e o texto foi limpo de erros de reconhecimento de fala.

Termos corrigidos por contexto (transcrição automática): "Buing Blocks" → Building Blocks; "Hate Limiter" → Rate Limiter; "DDS e spam" → DDoS e spam; "heads" → hits (cache hit); "enginex" → Nginx; "Cloud Flare" → Cloudflare; "cáfico/CFC" → Kafka; "Rabit MQ/RTMQ/Ritmkill" → RabbitMQ; "sharing" → sharding; "post gress/post GR SQL" → PostgreSQL; "foto RL" → foto URL; "to many requests" → Too Many Requests; "expand" → spam; "attacks" → ataques; "desaclopar" → desacoplar; "Kill" (após "fila") → provável "Queue" (palavra da transcrição automática truncada); "eh/né" (hesitação) removidos em parte. Trechos ambíguos sinalizados no texto com [?]. Pedidos de like/compartilhamento/inscrição preservados por fidelidade, mas sem valor técnico.

---

## Abertura

O vídeo de hoje é sobre System Design: será que existe um padrão e, se existe, qual padrão posso adotar para escalar melhor o meu sistema ou suprir um gargalo que está acontecendo no meu back end? Mas antes de estudar ou verificar se existe de fato um padrão, não se esqueça de deixar o seu like, compartilhar este vídeo nas suas redes sociais e ativar o sininho de notificação para que o YouTube entregue mais vídeos como este. E, óbvio, deixe um comentário; sempre gosto de responder todo mundo, e é muito interessante ler a opinião de vocês. Agora, sem mais enrolação: pega o papel, pega o lápis e a caneta, e bora pra aula.

## Como estudar System Design

Primeiro: System Design é a habilidade de criar soluções escaláveis, resilientes e performáticas para sistemas de software. Não é sobre decorar padrões, e sim entender problemas reais e tomar decisões técnicas diante desses problemas.

O autor traz um padrão em etapas para estudar System Design:

1. Aprender os **blocos de construção** (*building blocks*).
2. Estudar **problemas reais** e pensar em como resolvê-los.
3. Projetar soluções **em camadas**: criar uma versão simplificada e depois levá-la à maior complexidade, utilizando os building blocks.
4. **Justificar cada decisão** com trade-offs claros.
5. **Comparar a sua solução com empresas reais**, com demandas reais que acontecem no mercado profissional.

## Etapa 1 — Os building blocks

É preciso aprender os componentes mais comuns e quais são os seus propósitos, não só a definição (por isso "blocos de construção"):

- **Load balancer** — distribuidor de carga entre instâncias; usado para evitar sobrecarga.
- **Rate limiter** — protege a API como um todo; contra DDoS e spam, uma espécie de filtro.
- **Cache** — o mais comum é o Redis; reduz a latência e a carga no banco de dados. (A transcrição menciona "heads" [?], provavelmente *cache hits*.)
- **Filas** — Kafka, SQS ou RabbitMQ; servem para desacoplar serviços e lidar com picos de informação.
- **Database** — a parte de persistência; depende dos padrões de leitura/escrita. SQL ou NoSQL.
- **CDN** — acelera a entrega do conteúdo estático.
- **Sharding** — divide os dados para escalar horizontalmente.

Depois de saber quais são os blocos, só se entende qual usar ao observar um problema real.

## Etapa 2 — O cenário: Instagram simplificado

O usuário envia uma foto pela API, que armazena a foto em **disco local**. O banco de dados é o **PostgreSQL**, com uma tabela `users` e uma tabela chamada `profile_url`. (O autor reconhece que redes sociais geralmente trabalham com NoSQL, mas, hipoteticamente, o "Instagram simplificado" usa banco relacional.) Quando alguém acessa o perfil, a imagem é servida diretamente do back end.

Problemas identificados:

- O back end fica lento com muitos acessos.
- A imagem demora a carregar devido à latência alta.
- Picos de usuários derrubam o servidor.
- Ataques: alguém faz spam o tempo todo.

## Etapa 3 — Aplicando os building blocks

**Load balancer** (Nginx, AWS, entre outros).
- Problema: muitos acessos derrubando o back end.
- Decisão: adicionar múltiplas instâncias e balancear a carga.
- Quando usar: sempre que houver múltiplos servidores servindo a mesma API.

**CDN** (Cloudflare, AWS CloudFront, entre outros).
- Problema: imagem lenta para carregar.
- Quando usar: sempre que houver conteúdo estático — imagens, vídeos, arquivos.
- Decisão: salvar a imagem em um bucket (S3), gerar uma URL pública e servi-la via CDN.

**Cache** (Redis).
- Problema: evitar bater toda hora no banco para buscar o `profile_photo_url`.
- Quando usar: quando o mesmo dado é muito acessado e muda pouco.
- Decisão: armazenar `user_id` e `photo_url` em cache com **TTL de 5 minutos**, atualizando sempre que houver um upload novo.

**Rate limiter.**
- Problema: alguém fazendo 1.000 ou 10.000 uploads por segundo de imagem — "um problema muito sério".
- Quando usar: sempre que se expõem endpoints públicos, principalmente de escrita.
- Decisão: permitir 10 uploads por minuto por IP [?: a transcrição diz "fazer uma associação de imagens por IP" — provavelmente "associar/contar uploads por IP"]; se ultrapassar, retornar **429 Too Many Requests**. Algo simples que trata ataques.

**Fila** (Kafka ou RabbitMQ; o autor gosta do RabbitMQ por ser mais simplificado — o Kafka é muito grande, então depende do contexto).
- Problema: o upload pode ser lento e o usuário não deve esperar o processamento todo.
- Quando usar: quando o tempo de resposta não precisa ser síncrono.
- Decisão: após o upload, enviar uma mensagem à fila; um worker lê da fila e gera a miniatura da imagem — processo assíncrono. É mais ou menos como Instagram e Twitter fazem: ao enviar um vídeo mais demorado, o usuário continua usando a plataforma enquanto uma barra de progresso indica que o upload está sendo feito.

**Escalabilidade do banco de dados.**
- Problema: milhões de usuários acessando perfis.
- Decisão: várias **réplicas de leitura** do PostgreSQL; se for preciso escalar mais, **sharding por região**. Simples assim.

## Etapa 4 — Pensar como engenheiro

A pergunta não é "o que é um load balancer" — por mais que seja preciso conhecer os building blocks. A pergunta é: qual é o **gargalo atual** do meu sistema, o que posso resolver agora e qual é o **custo** dessa decisão. Sempre pensar em **latência**, **consistência**, **resiliência** e **custo**.

## Como treinar

Criar um cenário como o "Instagram simplificado". Por exemplo, um **YouTube simplificado** com funcionalidades básicas: o usuário faz upload [?: a transcrição diz "o pde"] de vídeo, assiste ao vídeo, há comentários, há a contagem de views e há recomendação de vídeo na home. A partir daí, treinar System Design sobre esse problema. A maior dica do autor: treinar com cenário real — quanto mais você exercita [?: a transcrição trunca "quanto mais você exer"] ... (frase interrompida, sem conclusão na transcrição).

## Fecho

Espero que vocês tenham gostado deste vídeo e, se gostou, curta e compartilha. E fui.
