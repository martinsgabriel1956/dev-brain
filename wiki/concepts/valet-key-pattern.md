---
type: concept
title: "Valet Key Pattern"
aliases: ["valet key", "presigned url", "credencial temporária", "scoped token", "signed url"]
date_created: 2026-06-05
date_updated: 2026-06-05
source_count: 1
tags: [valet-key, presigned-url, s3, attack-surface, arquitetura-seguranca, least-privilege, upload, storage]
skill: tech-mentor-security
status: stable
---

# Valet Key Pattern

Padrão arquitetural que emite uma credencial temporária de escopo mínimo para que o cliente acesse um recurso externo diretamente — sem que a API principal precise intermediar o tráfego.

**Analogia:** você não entrega a chave da sua casa para quem vai estacionar o carro. Entrega só a chave da garagem, com validade de uma hora.

## Três Características da Valet Key

1. **Expira rapidamente** — credencial de curta duração (minutos, não horas)
2. **Escopo mínimo** — funciona apenas para um recurso específico (um arquivo, um bucket path)
3. **Não eleva privilégio** — não dá acesso à API ou ao sistema como um todo

## Fluxo

```
1. Cliente solicita acesso à API
2. API valida identidade + permissão do usuário
3. API gera credencial temporária (valet key) de escopo restrito
4. Cliente recebe a valet key
5. Cliente acessa o recurso diretamente com essa chave
6. Recurso valida a chave e permite a operação — sem passar pela API novamente
```

## Exemplos Práticos

- **AWS S3 Presigned URL** — URL com assinatura HMAC que permite upload/download de um objeto específico por N minutos
- **Azure SAS Token (Shared Access Signature)** — acesso temporário a Blob Storage
- **Google Cloud Signed URL** — acesso temporário a objetos no GCS

Ver também: [[concepts/media-upload-pattern]] — implementação do padrão para upload de mídia.

## Ganhos

- **Reduz carga da API:** a aplicação não precisa receber e repassar arquivos grandes (não vira proxy)
- **Reduz [[concepts/attack-surface]]:** token interceptado tem impacto limitado em tempo e escopo
- **Melhora performance:** cliente faz upload/download diretamente no storage — sem hop extra

## Relação com Least Privilege

A Valet Key é a implementação prática do [[concepts/defense-in-depth]] em credenciais: mesmo que vaze, não há escalada de privilégio possível.

## Key Sources

- [[sources/padroes-arquiteturais-seguranca-gatekeeper-valet-key-token-relay]]
