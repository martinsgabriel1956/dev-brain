---
type: source
title: "Upload e Download de Arquivos Gigantes: Object Storage, Presigned URLs, Multipart Upload e CDN (System Design para Entrevistas Tier S)"
aliases: ["upload de arquivos gigantes tier s", "upload de vídeo de 2 GB entrevista", "presigned url multipart cloudfront", "vídeo 5 série camaforte"]
date_created: 2026-10-30
date_updated: 2026-10-30
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/upload-download-arquivos-gigantes-presigned-url-multipart-tier-s.md
source_url: ""
author: "Pedro Camaforte"
date_published: ""
date_ingested: 2026-10-30
source_count: 0
tags: [system-design, entrevistas, upload, download, object-storage, amazon-s3, presigned-url, multipart-upload, cdn, cloudfront, egress, sqs, backend, infra, finops]
skill: tech-mentor-system-design
status: stable
---

# Upload e Download de Arquivos Gigantes: Object Storage, Presigned URLs, Multipart Upload e CDN

## TL;DR

Quinto vídeo da série Tier S de [[wiki/entities/pedro-camaforte]]. A tese: **numa entrevista sênior, o servidor de aplicação nunca deveria encostar no arquivo**. O vídeo parte da solução mais crua e evolui por eliminação. Guardar o binário no banco quebra queries, backup/restore e réplicas. Guardar no disco local quebra com [[wiki/concepts/auto-scaling]] e [[wiki/concepts/load-balancer]]. Um volume compartilhado funciona, mas exige um time de infra dedicado. Usar [[wiki/concepts/object-storage]] (S3) com o servidor no meio só repassa bytes. A resposta final é a [[wiki/concepts/presigned-url]]: o servidor só autoriza, gera a URL localmente via SDK, e o cliente sobe direto para o S3.

A regra de decisão é a seguinte. Abaixo de 100 MB, use PUT único. Acima disso, use [[wiki/concepts/multipart-upload]] com URLs numeradas por parte, upload paralelo, retomada via `uploadId` e prova de conclusão via ETags. Ao finalizar, um evento vai para o [[wiki/concepts/aws-sqs|SQS]] e um worker marca o upload como completo, o que fecha o gancho de [[wiki/concepts/processamento-assincrono]] do vídeo 3. Um cron job limpa uploads abandonados e finaliza uploads "órfãos" que já têm todas as partes.

No download, a URL pré-assinada vale para arquivos privados, com [[wiki/concepts/cdn]] ([[wiki/concepts/aws-cloudfront|CloudFront]]) na frente. O vídeo afirma que o ganho real da CDN é custo de [[wiki/concepts/custo-de-egress|egress]] ("economia de 90%"), mas **os próprios números do vídeo desmentem isso**: US$ 0,09 → US$ 0,085/GB dá cerca de 5,6%. Detalhes em Key Claims. Para validar arquivos, o vídeo propõe um [[wiki/concepts/bucket-de-quarentena]].

## Key Claims

- **Servidor como intermediário de bytes é red flag de entrevista sênior.** Receber o arquivo e repassá-lo ao S3 gasta memória e banda à toa, e uma falha em 99% obriga o usuário a recomeçar. A resposta esperada é cliente → S3 direto, com o servidor só gerenciando permissões. *Confiança: alta.* O mesmo fluxo já está em [[wiki/concepts/media-upload-pattern]] (caso WhatsApp) e em [skill: tech-mentor-system-design] `architecture-ops.md` ("server não é gargalo para uploads/downloads grandes"). → [[wiki/concepts/media-upload-pattern]], [[wiki/concepts/valet-key-pattern]]
- **Binário no banco é inviável em escala por três motivos.** (a) Queries como "últimos 10 vídeos" trafegam GBs de memória, I/O e banda. (b) Backup e restore passam de minutos para horas, o que pesa justamente numa emergência. (c) Cada [[wiki/concepts/read-replicas|réplica de leitura]] precisa copiar os vídeos inteiros. → [[wiki/concepts/read-replicas]]
- **Disco local é incompatível com servidores efêmeros.** O load balancer pode mandar o download para outro servidor, e o auto scaler pode destruir de madrugada o servidor que guardava o arquivo. É o argumento de [[wiki/concepts/stateless]] aplicado a arquivos. → [[wiki/concepts/stateless]], [[wiki/concepts/auto-scaling]]
- **Volume compartilhado (servidor central de arquivos) é uma solução legítima.** Muitas empresas pequenas e médias o usam por anos. O custo é virar dono da infra: um ponto único de falha, gargalo de I/O e um time dedicado. Próximo de [[wiki/concepts/nas-network-attached-storage]].
- **Object storage = blob storage.** *Blob* significa *binary large object*. O S3 não é o único (Google Cloud Storage e Azure Blob Storage também existem), mas é o termo padrão em entrevistas. → [[wiki/concepts/object-storage]], [[wiki/concepts/amazon-s3]]
- **A presigned URL é gerada localmente pelo servidor, sem chamar o S3.** O servidor usa o SDK e a credencial secreta. A URL carrega um tempo de expiração e `X-Amz-Signature`; o S3 recalcula a assinatura e nega a requisição se algo foi adulterado. *Confiança: alta* [external]: é o SigV4 de query string ([docs AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html)). A exceção é o `CreateMultipartUpload`, que exige uma chamada real ao S3, como a própria fonte descreve. → [[wiki/concepts/presigned-url]]
- **Antes do upload, o cliente envia nome, tipo e tamanho.** O servidor grava esses metadados com status `pendente`. O tamanho serve para calcular quantas URLs de parte gerar.
- **PUT único vai até 5 GB, mas a AWS recomenda multipart a partir de 100 MB.** *Confiança: alta*, bate com a documentação da AWS. → [[wiki/concepts/multipart-upload]]
- **Mecânica do multipart:**
  - O servidor pede um `uploadId` ao S3 e devolve um **array de URLs pré-assinadas numeradas**, uma por parte.
  - Cada parte tem no mínimo 5 MB; só a última pode ser menor (ex.: 101 MB → 20 × 5 MB + 1 MB).
  - As partes podem subir em paralelo.
  - Se a conexão cair, as partes já enviadas ficam no S3. O servidor pergunta quais partes o S3 já recebeu e o cliente retoma do ponto exato.
  - *Confiança: alta.* A API dessa consulta é `ListParts` [external].
- **ETags são a prova de conclusão.** O S3 devolve uma ETag por parte. Para concluir, o cliente envia ao servidor o array ordenado de ETags, e o S3 valida tudo antes de montar o objeto. Isso impede que um cliente "declare" um upload concluído sem ter enviado as partes. *Nota [external]:* para o browser ler o header `ETag` da resposta, o CORS do bucket precisa expor esse header (`ExposeHeaders: ["ETag"]`). A fonte não menciona isso.
- **A conclusão dispara evento → SQS → worker.** O worker atualiza o status do upload para completo. O mesmo vale para o PUT único. É a mesma cola event-driven de [skill: tech-mentor-system-design] `system-design-cases.md`, onde, no pipeline de upload do YouTube, `S3 event → SQS → Transcoding Workers`. → [[wiki/concepts/aws-sqs]], [[wiki/concepts/processamento-assincrono]]
- **O cron job tem duas funções.** (1) Limpar uploads abandonados para não pagar armazenamento de partes órfãs. (2) Finalizar uploads pendentes há mais de 24h cujas partes já estão todas no S3: o cliente enviou tudo, mas caiu antes de avisar, e o usuário pode receber um e-mail. *Nota [external]:* para a função (1), o S3 tem uma regra nativa de lifecycle, `AbortIncompleteMultipartUpload` ([docs AWS](https://docs.aws.amazon.com/AmazonS3/latest/userguide/mpu-abort-incomplete-mpu-lifecycle-config.html)), que dispensa o cron. O cron continua necessário para a função (2).
- **O limite do multipart é 50 TB por objeto.** *Confiança: alta*, confirmado pelo [anúncio AWS de 02/12/2025](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-s3-maximum-object-size-50-tb/) [external]. O limite real é ≈ 48,8 TiB (10.000 partes × 5 GiB). **Isso contradiz [[wiki/concepts/amazon-s3]]**, que dizia "objetos até 5 TB" (valor anterior a dez/2025); a página foi atualizada.
- **Durabilidade do S3.** A fonte diz "9,99999" (ASR truncado). O valor oficial é 99,999999999% (11 noves), já registrado em [[wiki/concepts/amazon-s3]].
- **Download privado:** o usuário pede o arquivo pelo ID → o servidor checa a permissão → o banco devolve a **S3 key** (o path) → o servidor gera a presigned URL de GET → o S3 faz o stream. Arquivos públicos não precisam de URL assinada. *Confiança: alta*, idêntico ao exemplo `getDownloadUrl` de [skill: tech-mentor-system-design] `architecture-ops.md`, inclusive o "verificar autorização ANTES de gerar a URL".
- **CDN na frente do S3:**
  - **Latência:** do Japão até um S3 nos EUA, cai de ~500 ms para ~10–20 ms.
  - **Custo, segundo a fonte:** egress S3 → internet a US$ 0,09/GB; S3 → CloudFront gratuito; CloudFront → usuário a US$ 0,085/GB; "economia de 90%".
  - **⚠️ Contradição interna:** pelos próprios números do vídeo, a economia é (0,09 − 0,085) / 0,09 ≈ **5,6%**, não 90%. Os preços em si conferem [external, fontes secundárias: [awsfundamentals](https://awsfundamentals.com/blog/amazon-cloudfront-pricing), [redresscompliance](https://redresscompliance.com/aws-cloudfront-vs-direct-egress-cost.html)].
  - **De onde vem o ganho real de custo:** do cache hit, que evita GETs e leituras repetidas na origem; do free tier do CloudFront (1 TB/mês); e de faixas de volume e planos flat-rate mais baratos.
  - *Recomendação para entrevista:* cite "S3 → CloudFront é gratuito e o cache derruba requisições à origem", não o "90%". → [[wiki/concepts/custo-de-egress]], [[wiki/concepts/aws-cloudfront]], [[wiki/concepts/cdn]]
- **Framework de decisão:** < 100 MB → PUT pré-assinado; ≥ 100 MB → multipart pré-assinado (até 50 TB); acesso frequente → CDN.
- **Red flags de entrevista:**
  - Usar multipart para arquivos de 10–15 MB ("decorou que tem que fazer chunk").
  - Passar o arquivo pelo servidor.
  - → [[wiki/concepts/entrevista-system-design]]
- **Validação com bucket de quarentena.** O upload cai num bucket temporário, uma máquina isolada o escaneia (malware pode "explodir" ali sem dano) e só depois o arquivo vai para o bucket final. → [[wiki/concepts/bucket-de-quarentena]], [[wiki/concepts/upload-arbitrario-rce]], [[wiki/concepts/sandbox]]

## Entities

[[wiki/entities/pedro-camaforte]] · [[wiki/entities/aws]]

## Concepts

[[wiki/concepts/object-storage]] · [[wiki/concepts/presigned-url]] · [[wiki/concepts/multipart-upload]] · [[wiki/concepts/custo-de-egress]] · [[wiki/concepts/bucket-de-quarentena]] · [[wiki/concepts/media-upload-pattern]] · [[wiki/concepts/valet-key-pattern]] · [[wiki/concepts/amazon-s3]] · [[wiki/concepts/aws-cloudfront]] · [[wiki/concepts/cdn]] · [[wiki/concepts/aws-sqs]] · [[wiki/concepts/processamento-assincrono]] · [[wiki/concepts/auto-scaling]] · [[wiki/concepts/stateless]] · [[wiki/concepts/read-replicas]] · [[wiki/concepts/upload-arbitrario-rce]] · [[wiki/concepts/entrevista-system-design]] · [[wiki/concepts/finops]]

## Conexão com outras fontes

Este é o vídeo 5 da série que já tem na wiki o vídeo 1 ([[wiki/sources/escalar-leituras-banco-de-dados-entrevista-tier-s]]), o 6 ([[wiki/sources/race-condition-locking-pessimista-otimista-reservations-tier-s]], anunciado no fim deste vídeo) e o 7 ([[wiki/sources/como-se-comportar-na-entrevista-de-system-design-tier-s]]). O vídeo 1 já colocava a CDN como último degrau da escada de leitura, específica para arquivos estáticos. Este vídeo detalha esse degrau para arquivos grandes e acrescenta o argumento de custo.

O fluxo de presigned URL já aparecia de forma resumida em [[wiki/sources/case-whatsapp]] (via [[wiki/concepts/media-upload-pattern]]) e como padrão de segurança em [[wiki/sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]] ([[wiki/concepts/valet-key-pattern]]). Esta fonte acrescenta o multipart, a retomada, as ETags, o cron de reconciliação e o download. O caso do Instagram simplificado ([[wiki/sources/como-estudar-system-design-building-blocks-instagram-simplificado]]) usava bucket com URL **pública** + CDN; aqui o caso é **privado**, com URL de GET assinada.

## Open Questions

- **"Economia de 90%" com CloudFront.** É um erro numérico da fonte: pelos preços citados, a diferença por GB é ~5,6%. Não está claro qual artigo o autor leu. O ganho real vem do cache e do free tier.
- **O tamanho declarado não é imposto.** Uma presigned URL de PUT não limita o tamanho enviado, a menos que o `Content-Length` entre na assinatura. Um cliente pode declarar 10 MB e enviar 5 GB. O fluxo da fonte não fecha essa brecha. Alternativas [external]: presigned **POST** com política `content-length-range`, ou validação do tamanho real no evento de conclusão.
- **Vídeo 3 da série (processamento assíncrono)** ainda não foi ingerido. Esta fonte diz que fecha "o ponto deixado aberto" lá, sem detalhar qual era.
- **Quarentena.** A fonte não diz como o arquivo sai da quarentena nem quem escaneia. Opções [external]: worker disparado por evento do S3, ou o GuardDuty Malware Protection for S3. Também não diz o que o usuário vê enquanto o arquivo está em validação (status `PROCESSING`).
- **Alternativa padronizada de upload retomável.** O protocolo **tus** ([skill: tech-mentor-system-design] `architecture-ops.md`) não é mencionado. A skill observa que o multipart do S3 "não tem protocolo padronizado para retomar do browser"; a retomada descrita pela fonte é orquestrada pelo próprio servidor.

## Raw Quotes

> "A resposta é até quase que contraintuitiva, porque o seu servidor nunca nem deveria encostar nesse arquivo."

> "O próprio servidor, através de um SDK do S3 e de uma variável de ambiente que ele vai ter lá dentro, uma secret, ele consegue sozinho, independentemente, gerar essa URL e já devolver direto pro usuário."

> "Porém, não é porque a gente pode que a gente deve fazer isso."

> "Ó, tá aqui a prova, todas as tags que o próprio S3 gerou. Então eu não posso forjar uma ETag."

> "Não: se o upload do arquivo é pequeno, se esse arquivo é pequeno, você pode fazer o upload direto. A própria Amazon recomenda que você faça isso."
