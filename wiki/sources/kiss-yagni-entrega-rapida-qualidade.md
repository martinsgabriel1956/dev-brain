---
type: source
title: "Como Entregar Seus Projetos Mais Rápido e Com Mais Qualidade — KISS e YAGNI"
aliases: ["kiss e yagni entrega rapida qualidade", "dois princípios para entregar mais rápido"]
date_created: 2026-07-19
date_updated: 2026-07-19
source_count: 0
tags: [kiss, yagni, principios, over-engineering, qualidade, entrega, idempotencia]
skill: tech-mentor-backend
source_file: /home/nemomartins/Documentos/new/dev-study/raw/kiss-yagni-entrega-rapida-qualidade.md
source_url: ""
author: "Everton Oliveira"
date_published: ""
date_ingested: "2026-07-19"
status: stable
---

# Como Entregar Seus Projetos Mais Rápido e Com Mais Qualidade — KISS e YAGNI

## TL;DR

Vídeo de Everton Oliveira (engenheiro de software sênior) apresentando KISS e YAGNI como os dois princípios que resolvem o dilema central da entrega de software: velocidade vs. qualidade. Traz origem do KISS (Marinha dos EUA), um exemplo de refatoração de uma validação de reprocessamento de transferência usando KISS, e um exemplo clássico de over-implementação de métodos de repositório violando YAGNI.

---

## Reivindicações Principais

**Claim:** KISS foi criado e usado pela primeira vez pela Marinha dos Estados Unidos.
**Evidência:** Afirmação direta do autor, sem citação de fonte primária ou data.
**Confiança:** Média — origem militar do KISS é amplamente repetida na indústria como folclore técnico, mas a atribuição específica à Marinha dos EUA não é verificada nesta fonte nem documentada com data/contexto (a origem exata é disputada; atribuições comuns incluem Kelly Johnson, engenheiro da Lockheed Skunk Works, década de 1960). Já registrado como lacuna aberta — ver Questões em Aberto.

**Claim:** KISS se aplica também a testes — testes unitários de baixo valor podem/devem ser removidos em favor de testes focados no núcleo do problema.
**Evidência:** Argumento qualitativo do autor, sem exemplo de código.
**Confiança:** Média-alta — coerente com [[wiki/concepts/criterios-de-bom-teste]] e com a crítica a cobertura por cobertura já presente em [[wiki/sources/teste-unitario-integracao-e2e-opiniao]], mas é uma aplicação nova do KISS não coberta antes na wiki (KISS até aqui só estava ligado a arquitetura/design, não a estratégia de testes).

**Claim:** Uma cadeia de `if`s de validação de status pode ser simplificada para uma checagem de pertencimento a uma lista de status permitidos, com retorno antecipado — exemplo prático de KISS aplicado.
**Evidência:** Exemplo de refatoração descrito (não mostrado em código na transcrição, apenas narrado): lógica que decide se uma transferência pode ser reprocessada, dado seu status.
**Confiança:** Alta como técnica (é um refactor padrão, coerente com [[wiki/concepts/idempotencia]] no aspecto de "verificar se uma operação pode ser reexecutada com segurança"), mas o exemplo real não foi capturado em código pela transcrição — apenas a descrição verbal do antes/depois.

**Claim:** YAGNI foi apresentado no livro *Extreme Programming*, de autoria de Ronald (Ron) Jeffries.
**Evidência:** Afirmação direta do autor.
**Confiança:** Baixa — **contradiz** o que já está documentado em [[wiki/entities/kent-beck]]: o livro fundador do YAGNI/XP é *Extreme Programming Explained* (1999), de **Kent Beck**. Ron Jeffries é coautor da criação da Extreme Programming (junto com Beck e Ward Cunningham, no [[wiki/entities/c3-project|projeto C3]]) e escreveu obras próprias sobre XP, mas a atribuição de autoria do livro citado nesta fonte a Jeffries em vez de Beck parece um erro do autor do vídeo. Ver Questões em Aberto.

**Claim:** Implementar preventivamente todos os métodos possíveis de um repositório (get, insert, update, delete) quando a feature em questão só precisa de um subconjunto é uma violação típica de YAGNI — aumenta tempo de entrega e gera código morto.
**Evidência:** Exemplo ilustrativo dado pelo autor (sem código real).
**Confiança:** Alta — coincide exatamente com o exemplo já documentado em [[wiki/concepts/yagni]] ("interface para cada repositório com uma única implementação... mappers em todas as direções").

**Claim:** Interfaces mais simples geram maior retenção de usuário — extensão do KISS para UX/front-end.
**Evidência:** Argumento qualitativo, sem dado quantitativo ou estudo citado.
**Confiança:** Baixa-média — plausível e alinhado ao senso comum de UX, mas sem evidência empírica citada na fonte; ângulo novo que a wiki não tinha para KISS (até então só arquitetura/código/testes).

---

## Conceitos Abordados

- [[wiki/concepts/kiss]]
- [[wiki/concepts/yagni]]
- [[wiki/concepts/idempotencia]] — exemplo de refatoração é uma checagem de reprocessamento seguro, adjacente mas não idêntico ao padrão de Idempotency Key
- [[wiki/concepts/over-engineering]]

## Entidades

- [[wiki/entities/everton-oliveira]]
- [[wiki/entities/kent-beck]] — autoria do livro de XP citado (com ressalva de possível erro do autor do vídeo)
- [[wiki/entities/c3-project]] — origem da Extreme Programming, contexto de Ron Jeffries

## Questões em Aberto

- **Atribuição do livro *Extreme Programming* a Ronald Jeffries** em vez de Kent Beck — provável imprecisão do autor do vídeo. *Extreme Programming Explained* (1999) é de Kent Beck; Ron Jeffries é cocriador da metodologia e coautor de outras obras sobre XP, mas não do livro fundador citado. Não corrigido na fonte (raw/ é imutável); a wiki reflete a atribuição correta via [[wiki/entities/kent-beck]].
- **Origem exata do KISS na Marinha dos EUA** não é datada nem referenciada com fonte primária — vale checar em ingestão futura (a atribuição alternativa mais comum na literatura de engenharia é a Kelly Johnson, Lockheed Skunk Works).
- Exemplos de código (refatoração da validação de transferência e dos métodos do repositório) foram narrados verbalmente no vídeo, não mostrados em texto — a transcrição em áudio não captura o código exibido na tela.
- Autor/canal do vídeo não teve URL ou data de publicação fornecidos junto com a transcrição.

## Raw Quotes

> "KISS... foi criado pela Marinha dos Estados Unidos, foi utilizado pela primeira vez nesse contexto da Marinha, e o objetivo dele é manter as coisas o mais simples possível."

> "YAGNI... que é você não precisará disso... foi apresentado nesse livro Extreme [Programming] do Ronald Jeffries."

> "Você só faça implementações daquilo que for necessário para aquele momento."
