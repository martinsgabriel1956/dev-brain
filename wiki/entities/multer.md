---
type: entity
title: "Multer"
aliases: ["multer", "multer diskStorage", "upload.single"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [nodejs, express, upload, multipart, biblioteca]
skill: lang-dynamic
status: stub
---

# Multer

Middleware do [[wiki/entities/express]] para receber [[wiki/concepts/multipart-form-data]]: separa os campos de texto em `req.body` e os arquivos em `req.file` (ou `req.files`). Pode gravar em disco (`diskStorage`), manter em memória (`memoryStorage`) ou usar um *storage engine* de terceiros (S3).

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]), com [[wiki/entities/diego-fernandes|Diego Fernandes]]:

- **Configuração:** `multer.diskStorage({ destination: path.resolve(__dirname, '..', '..', 'uploads'), filename })`.
- **Nome único:** o `filename` gera `${crypto.randomBytes(6).toString('hex')}-${file.originalname}` e chama `callback(null, fileName)`.
- **Na rota:** `routes.post('/points', upload.single('image'), ...)`; `upload.array('fotos')` serviria para vários arquivos.
- **No controller:** `request.file.filename` vira o campo `image` do ponto.
- **`fileFilter` e `limits`** (tipo e tamanho) ficam citados, "não vai dar tempo da gente implementar".

**O que faltou para produção:**

- **Limites e tipo:** `limits: { fileSize }` e `fileFilter` checando o tipo real (magic bytes), não só o `mimetype` enviado pelo cliente. Sem isso, cabe qualquer arquivo, inclusive HTML ou SVG com script servidos pelo `express.static` (XSS armazenado). Ver [[wiki/concepts/xss]] e [[wiki/concepts/upload-arbitrario-rce]].
- **Nome sanitizado:** o `preservePath: false` padrão já tira diretórios do `originalname` `[external]` (https://github.com/expressjs/multer#multeropts), mas acentos e espaços ainda quebram URLs.
- **Validar antes de gravar,** ou limpar os órfãos quando a validação ou a transação falha.
- **Fora do disco local:** num PaaS, o disco é efêmero ([[wiki/concepts/sistema-de-arquivos-efemero]]); em produção, o lugar é object storage ([[wiki/concepts/object-storage]]).

`[skill: lang-dynamic]` No Fastify, o equivalente é `@fastify/multipart`, com `limits` e streaming direto para o S3.

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: upload da imagem do ponto de coleta
