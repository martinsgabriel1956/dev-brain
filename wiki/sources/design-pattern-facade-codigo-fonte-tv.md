---
type: source
title: "Facade: Padrão de Projeto na Prática, com TypeScript (Código Fonte TV)"
aliases: ["facade codigo fonte tv", "client facade lgpd", "remove conta facade video"]
date_created: 2026-08-18
date_updated: 2026-08-18
source_file: /home/gabriel-martins/Documentos/dev-brain/raw/design-pattern-facade-codigo-fonte-tv.md
source_url: ""
author: "Código Fonte TV"
date_published: ""
date_ingested: 2026-08-18
source_count: 0
tags: [design-patterns, structural, facade, solid, srp, ocp, dependency-injection, lgpd, typescript, oop, video]
skill: tech-mentor-backend
status: stable
---

# Facade: Padrão de Projeto na Prática, com TypeScript (Código Fonte TV)

## TL;DR

Segundo episódio da minissérie "mão no código" de padrões de projeto do canal [[wiki/entities/codigo-fonte-tv]] (depois de Strategy), sobre o padrão [[wiki/concepts/facade-pattern]]. Constrói um `ClientFacade` em TypeScript que encapsula a remoção de conta de um cliente (Avatar, Documentos, Histórico de Acesso), motivada por um cenário de exclusão de dados sob **LGPD**. Diferente da fonte [[wiki/sources/design-pattern-facade-renato-augusto]] — que defende que o Facade não fere o SRP — este vídeo assume abertamente que sua implementação viola OCP, DIP/acoplamento e SRP, e usa isso para argumentar que o Facade é um padrão controverso: útil quando a complexidade do cliente é grande demais, mas não gratuito.

## Key Claims

| Claim | Evidence | Confidence |
|---|---|---|
| Um subsistema é um conjunto de serviços que, juntos, executam operações complexas e que o Facade existe para simplificar do ponto de vista de quem consome | Exemplo: Avatar pode usar S3 ou Google Drive, e-mail para comunicação, histórico de acesso via outro serviço — cada um tratado como subsistema independente | Alto |
| Facade não impede acesso direto ao subsistema, só oferece um caminho mais simples | Afirmação explícita: "ele não encapsula de forma a evitar o acesso diretamente [aos serviços]" — diferente de encapsulamento que bloqueia acesso | Alto |
| Remover dados de um cliente sob LGPD não é um loop trivial de `remove()` em cada serviço — pode haver regra de negócio no meio (ex.: histórico de acesso tem retenção legal obrigatória) | Motivação central do exemplo: a lei exige remoção de dados a pedido do titular, mas certos dados (histórico de acesso) podem precisar ser retidos por obrigação legal | Médio — o vídeo não cita o artigo específico da LGPD, é usado como motivação narrativa |
| A implementação apresentada quebra OCP, porque depende de implementações concretas dos serviços em vez de interfaces — adicionar um canal novo (SMS, além de e-mail) exige abrir a classe e alterar o método existente | Exemplo hipotético de adicionar envio de SMS ao fluxo de remoção, comparado ao custo de repetir essa alteração em vários pontos | Alto |
| Instanciar os serviços diretamente no construtor do Facade (em vez de injetá-los) acopla o Facade fortemente às implementações concretas; a alternativa (DI completa) devolve a complexidade para o código cliente, que teria que montar e passar todos os serviços | Comparação explícita entre as duas abordagens no vídeo, sem resolver a tensão — apresentada como trade-off real, não como erro a corrigir | Alto |
| Na opinião do autor, a implementação quebra SRP "bonito", porque o método `removeConta` faz mais do que uma única coisa deveria fazer — mesmo reconhecendo que outros defendem que orquestração pura não quebra SRP | Posição pessoal do autor, contrastada explicitamente com a visão contrária ("tem gente que defende que não quebra") | Médio — é uma opinião declarada como tal, não uma prova formal |
| Facade pode ser implementado como classe com construtor (estado + instância) ou como método estático que recebe o objeto a operar como parâmetro — a segunda forma evita re-instanciar o Facade a cada chamada, mas não resolve a tensão de acoplamento/manutenção | Duas variações de código mostradas: `new ClientFacade(cliente).removeConta()` vs. `ClientFacade.removeConta(cliente)` | Alto |
| Facade pode ser composto em cadeia — uma fachada (ex.: `ClienteComunicacao`) pode existir dentro de outra fachada, decidindo internamente entre e-mail e SMS | Exemplo hipotético mencionado ao final, sem implementação de código | Médio |
| Uso de Facade é controverso: há quem o trate como anti-pattern por ferir SOLID; o autor pondera que os princípios devem ser respeitados ao máximo, mas aceita Facade como solução de compensação quando a complexidade do lado cliente é grande demais | Conclusão explícita do vídeo, convite aberto para debate nos comentários | Alto |

## Estrutura do Exemplo

```
Cliente (ação de botão) → ClientFacade.removeConta()
                              ├─ AvatarService.remove(cliente)
                              ├─ DocumentService.remove(cliente)
                              └─ AccessHistoryService.remove(cliente)
```

```typescript
class ClientFacade {
  private cliente: Cliente;
  private avatarService: AvatarService;
  private documentService: DocumentService;
  private accessHistoryService: AccessHistoryService;

  constructor(cliente: Cliente) {
    this.cliente = cliente;
    this.avatarService = new AvatarService();
    this.documentService = new DocumentService();
    this.accessHistoryService = new AccessHistoryService();
  }

  removeConta() {
    this.avatarService.remove(this.cliente);
    this.documentService.remove(this.cliente);
    this.accessHistoryService.remove(this.cliente);
  }
}
```

Variação estática:

```typescript
class ClientFacade {
  static removeConta(cliente: Cliente) {
    new AvatarService().remove(cliente);
    new DocumentService().remove(cliente);
    new AccessHistoryService().remove(cliente);
  }
}
```

## Relação com [[wiki/concepts/facade-pattern]]

- Confirma o caso de uso "reduzir acoplamento entre o cliente e um subsistema de múltiplos serviços", já documentado na página de conceito a partir de [[wiki/sources/design-pattern-facade]] e [[wiki/sources/design-pattern-facade-renato-augusto]].
- Adiciona um exemplo motivacional novo — **compliance/LGPD** — ao lado do exemplo de e-commerce da fonte de Renato Augusto, reforçando que a orquestração escondida por uma Facade frequentemente carrega regra de negócio real (ordem, exceções), não é só "chamar vários métodos".
- **Diverge da fonte de Renato Augusto** na avaliação sobre SRP — ver contradição registrada em [[wiki/questions/facade-fere-srp-video-comparison]].

## Entidades Mencionadas

- [[wiki/entities/codigo-fonte-tv]] — autor/canal do vídeo, segundo episódio da minissérie de design patterns (depois de Strategy)

## Questões em Aberto

- O vídeo não resolve a tensão entre acoplamento (serviços instanciados direto no construtor) e a alternativa de DI completa (que devolve a complexidade de montagem para o cliente) — apenas expõe o trade-off. Ponto que [[wiki/sources/design-pattern-facade-renato-augusto]] também deixa aberto, no mesmo formato de implementação (construtor com `new` direto).
- Não há aprofundamento em como testar um `ClientFacade` que instancia suas próprias dependências — mesma lacuna já registrada em [[wiki/sources/design-pattern-facade]].
- Contradição direta com [[wiki/sources/design-pattern-facade-renato-augusto]] sobre se o Facade fere o SRP — registrada em [[wiki/questions/facade-fere-srp-video-comparison]].
