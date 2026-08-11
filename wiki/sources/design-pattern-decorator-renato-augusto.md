---
type: source
title: "Padrão de Projeto Decorator (Renato Augusto)"
aliases: ["decorator renato augusto", "image processor decorator", "composição recursiva decorator video"]
date_created: 2026-08-11
date_updated: 2026-08-11
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/design-pattern-decorator-renato-augusto.md
source_url: ""
author: "Renato Augusto"
date_published: ""
date_ingested: 2026-08-11
source_count: 0
tags: [design-patterns, structural, decorator, wrapper, composicao-recursiva, open-closed, solid, oop, chain-of-responsibility, backend]
skill: tech-mentor-backend
status: stable
---

# Padrão de Projeto Decorator (Renato Augusto)

## TL;DR

Vídeo didático em português sobre o [[wiki/concepts/decorator-pattern]], construído em torno de um exemplo prático de um módulo `ImageProcessor` de upload/edição de imagens. Um `BasicImageProcessor` faz o processamento básico (validar metadados, extensão, salvar em `uploads/`), e novas demandas — adicionar marca d'água e redimensionar — são atendidas criando decorators (`WatermarkImageProcessor`, `ResizeImageProcessor`) que envolvem o objeto anterior em vez de modificar a classe existente. O vídeo usa o exemplo para ensinar **composição recursiva** e ancorar o padrão no [[wiki/concepts/open-closed-principle]], além de contrastá-lo com o Chain of Responsibility.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| O Decorator é um padrão **estrutural** cujo propósito é adicionar comportamento a objetos sem alterar a classe original, envolvendo (wrapping) o objeto em outro objeto | Definição de abertura; três nomes citados: Decorator, invólucro e Wrapper | Alto |
| O padrão está diretamente ligado ao **Open/Closed Principle** — modificar uma classe já em produção introduz risco de bugs; a alternativa correta é estender via wrapping | Argumento central repetido a cada nova demanda (marca d'água, resize) | Alto |
| A técnica que dá flexibilidade ao padrão é a **composição recursiva**: cada decorator recebe no construtor uma instância da mesma interface e delega a ela antes de aplicar seu próprio comportamento | Construtor de `WatermarkImageProcessor` e `ResizeImageProcessor` recebe `ImageProcessorInterface`; `process` chama `imageProcessor.process(...)` e só depois decora | Alto |
| Diferente do Chain of Responsibility, a **ordem dos decorators não é obrigatória** — inverter a ordem dos wrappers ainda executa sem erro; e não é preciso aplicar todos | Demonstração invertendo `Watermark`/`Resize`; sugestão de `if` no Controller para aplicar a marca d'água condicionalmente | Alto |
| O que "manda" na execução é a **instância atual na variável + o método comum `process`** — todas as classes implementam a mesma interface, por isso são intercambiáveis e encadeáveis | Explicação do fluxo em cadeia: `Resize.process` → `Watermark.process` → `Basic.process` | Alto |
| Decorator tem forte similaridade com **Chain of Responsibility** e com o conceito de **Middleware** (usado por frameworks para validação de requisições HTTP) | Comparação explícita ao final | Médio — a equivalência com Middleware é uma aproximação didática, não uma citação formal |
| Cada decorator cria um **novo arquivo** em vez de sobrescrever o anterior, para não corromper o arquivo já existente em caso de falha | `watermarked_file.jpg` e `resized_file.jpg` criados além do `file.jpg` básico | Alto |

## Estrutura do Exemplo

```
ImageProcessorInterface { process(imagePath): string }

Cliente (Controller) monta a cadeia:
  imageProcessor = new BasicImageProcessor()
  imageProcessor = new WatermarkImageProcessor(imageProcessor, "marca")   // decora
  imageProcessor = new ResizeImageProcessor(imageProcessor, 100, 100)     // decora
  imageProcessor.process("/temp/file.jpg")

Execução em cadeia (composição recursiva):
  Resize.process → Watermark.process → Basic.process → (retorna caminho)
                 ← redimensiona       ← marca d'água  ←
```

Cada camada chama o `process` do objeto que envolve, pega o caminho retornado e aplica seu próprio comportamento em cima, gerando um novo arquivo (`file.jpg` → `watermarked_file.jpg` → `resized_file.jpg`).

## Relação com [[wiki/concepts/decorator-pattern]]

Esta fonte reforça e concretiza a página de conceito, que até então se apoiava sobretudo no exemplo de canais de notificação de [[wiki/sources/seis-design-patterns-mais-usados-na-pratica]]:

- Confirma a mecânica de **wrapping recursivo em runtime** com um exemplo diferente (processamento de imagens), reforçando que o decorator recebe o objeto decorado **externamente** via construtor — o mesmo traço que a página de conceito usa para distinguir Decorator de [[wiki/concepts/proxy-pattern]].
- Adiciona dois ângulos que a página ainda não cobria: o vínculo explícito com o **Open/Closed Principle** e o contraste com **Chain of Responsibility** (Decorator não exige ordem; Chain exige).

## Entidades Mencionadas

- [[wiki/entities/renato-augusto]] — autor/canal do vídeo

## Conceitos Relacionados

- [[wiki/concepts/decorator-pattern]]
- [[wiki/concepts/open-closed-principle]] — Open/Closed Principle como justificativa do padrão
- [[wiki/concepts/design-patterns]] — catálogo GoF; padrões estruturais
- [[wiki/concepts/proxy-pattern]] — outro wrapper estrutural, distinção por intenção

## Questões em Aberto

- O vídeo instancia as dependências diretamente no código cliente (sem container de injeção de dependência), o mesmo ponto de testabilidade deixado em aberto por outras fontes de padrões do mesmo autor ([[wiki/sources/design-pattern-facade-renato-augusto]]).
- A equiparação de Decorator a "Middleware" é apresentada como aproximação didática; não há citação de fonte primária (GoF) para esse mapeamento.

## Citações Preservadas

> "A gente basicamente vai conseguir alterar uma classe, adicionar uma funcionalidade em tempo de execução, sem nem tocar nessa classe. Isso não é mágica, é apenas padrão de projeto."

> "As nossas classes têm que estar abertas para extensão e fechadas para modificação."

> "O que manda é a instância atual que está na classe e o método `process` que você vai chamar, porque todas elas possuem esse método."
