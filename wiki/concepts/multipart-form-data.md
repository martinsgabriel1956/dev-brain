---
type: concept
title: "multipart/form-data"
aliases: ["multipart form data", "FormData", "form-data", "upload multipart"]
date_created: 2026-11-16
date_updated: 2026-11-16
source_count: 1
tags: [http, upload, formularios, api]
skill: lang-dynamic
status: stub
---

# multipart/form-data

Formato de corpo HTTP em que cada campo vai numa "parte" separada por um *boundary*, com seus próprios cabeçalhos. Por isso aceita texto e arquivos binários na mesma requisição. É o que um `<form enctype="multipart/form-data">` envia, e o que o `FormData` do navegador produz.

No Ecoleta ([[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]): "infelizmente o JSON não suporta arquivos". O cadastro de ponto passa a ir como multipart, montado campo a campo no Insomnia e, no React, com `const data = new FormData(); data.append('name', name); ... data.append('image', selectedFile)`. No servidor, o [[wiki/entities/multer]] separa campos e arquivo.

**Consequências:**

- **Tudo chega como texto:** arrays viram `items=1,2,6` (`join`/`split`), e números viram strings, que precisam de conversão e [[wiki/concepts/validacao-de-entrada]].
- **Não defina o `Content-Type` à mão** ao enviar `FormData` com fetch ou Axios: o cliente gera o *boundary* sozinho.
- **Alternativas:** para arquivos grandes, upload direto para object storage com URL assinada, e só o JSON dos dados para a API ([[wiki/concepts/media-upload-pattern]]). Não confundir com o [[wiki/concepts/multipart-upload]] do S3, que divide um arquivo em partes.

Relacionado: [[wiki/concepts/formulario-html]], [[wiki/concepts/json]].

## Key sources

- [[wiki/sources/nlw-1-diego-fernandes-dia-5-upload-validacao-github-deploy-ecoleta]]: cadastro de ponto com imagem
