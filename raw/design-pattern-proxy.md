# Padrão de Projeto: Proxy

**Autor:** Renato Augusto
**Formato:** Transcrição de vídeo (canal no YouTube)
**Categoria do padrão:** Estrutural (GoF)
**Idioma original:** Português (BR)
**Data de transcrição:** 2026-06-05

---

## Introdução

O padrão Proxy é agnóstico de linguagem e framework — o conceito arquitetural se aplica em qualquer stack. Tem similaridade visual com Facade, Adapter e Decorator, mas com motivação completamente diferente.

---

## O que é o Proxy

O Proxy serve como **substituto ou espaço reservado para outro objeto**, permitindo controlar o acesso a ele. Em vez do código cliente conversar diretamente com a classe alvo, ele passa por um intermediário — o Proxy.

```
Cliente → Proxy → Objeto Real
```

Esse intermediário pode:
- Adicionar funcionalidades (cache, log, validação)
- Fazer verificações antes ou depois da chamada
- Atrasar a inicialização do objeto real (lazy initialization)
- Controlar permissões de acesso

> **Resumo em uma frase:** o Proxy intercepta a comunicação entre cliente e objeto, adicionando uma camada no meio sem modificar nenhum dos dois.

---

## Motivação — O Problema

Imagine um gerador de relatórios numa aplicação web:

```
GET /reports/:id
→ Controller busca o Report no repositório
→ Passa o Report para ReportGenerator.generate()
→ Retorna os dados ao front-end
```

Com o crescimento do sistema, a lógica ficou pesada. A operação passou a levar **5 segundos** para retornar — tempo inaceitável para o usuário.

**Solução óbvia (errada):** implementar cache direto no Controller ou na classe de serviço.

**Por que é errado:**
- Controller não deve conter regras de negócio ou infraestrutura
- Jogar cache no `ReportGenerator` viola o **Single Responsibility Principle** e o **Open/Closed Principle**
- Modificar código que já está em produção é arriscado

**Solução correta:** criar um Proxy.

---

## Estrutura do Projeto de Exemplo

```
src/
  controllers/
    ReportGeneratorController   # código cliente — chama o proxy
  services/
    ReportGenerator             # classe real com lógica pesada
    ReportGeneratorProxy        # proxy com camada de cache
  repositories/
    ReportRepository            # acesso ao banco de dados (Data Mapper pattern)
  entities/
    Report                      # entidade com atributo id
```

---

## Implementação Passo a Passo

### 1. Criar a Interface

Para que o Proxy possa se passar pelo objeto original, ambos devem implementar a mesma interface:

```typescript
interface IReportGenerator {
  generate(report: Report): any[];
}
```

### 2. Fazer a Classe Original Implementar a Interface

```typescript
class ReportGenerator implements IReportGenerator {
  generate(report: Report): any[] {
    // lógica pesada aqui — simula 5 segundos
    sleep(5000);
    return ['conteúdo do relatório'];
  }
}
```

### 3. Criar o Proxy

```typescript
class ReportGeneratorProxy implements IReportGenerator {
  constructor(
    private reportGenerator: ReportGenerator,
    private cache: CacheInterface
  ) {}

  generate(report: Report): any[] {
    const cacheKey = `report_${report.id}`;

    return this.cache.get(cacheKey, () => {
      // expira após 1 hora
      // só executa quando o cache está vazio ou expirado
      return this.reportGenerator.generate(report);
    }, { expiresIn: 3600 });
  }
}
```

**O que acontece em cada chamada:**

| Situação | Comportamento |
|---|---|
| Primeira chamada (cache vazio) | Executa `ReportGenerator.generate()`, armazena no cache, retorna |
| Chamadas seguintes (cache válido) | Retorna do cache imediatamente — `ReportGenerator` não é chamado |
| Após 1 hora (cache expirado) | Executa novamente, atualiza o cache |

### 4. Substituir no Controller

```typescript
// antes
const reportGenerator = new ReportGenerator();

// depois — única mudança no Controller
const reportGenerator = new ReportGeneratorProxy(
  new ReportGenerator(),
  cache
);

// a chamada permanece idêntica — Controller não sabe que é um Proxy
const reportData = reportGenerator.generate(report);
```

---

## Por que Funciona — O Princípio

O Controller é o **código cliente**. Ele só sabe que está lidando com algo que implementa `IReportGenerator`. Não sabe — e não precisa saber — se é o objeto real ou um Proxy.

Isso é possível porque:
1. Proxy e objeto real compartilham a mesma interface
2. O Controller depende da abstração (interface), não da implementação concreta

---

## Outras Aplicações do Proxy

Além de cache, o mesmo padrão se aplica a:

| Uso | O que o Proxy faz |
|---|---|
| **Cache** | Armazena resultado e evita reprocessamento |
| **Controle de acesso** | Verifica permissão do usuário antes de delegar |
| **Log** | Registra chamadas antes/depois de executar |
| **Lazy initialization** | Adia criação de objetos pesados até o primeiro uso |
| **Validação** | Valida entrada antes de passar ao objeto real |
| **Rate limiting** | Controla frequência de chamadas ao objeto real |

---

## Diferença entre Proxy e Decorator

Visualmente são parecidos — ambos encapsulam um objeto e delegam chamadas. A diferença está na **motivação**:

| | Proxy | Decorator |
|---|---|---|
| **Propósito** | Controlar acesso / interceptar comunicação | Adicionar comportamento em cadeia |
| **Quem conhece quem** | Proxy conhece a classe concreta | Decorator conhece a interface |
| **Composição** | Geralmente uma camada única | Pode ser encadeado (decorator de decorator) |
| **Exemplo** | Cache, auth, log de acesso | Adicionar funcionalidades incrementais |

> Cache não é regra de negócio do `ReportGenerator` — é infraestrutura. Por isso vai no Proxy, não no Decorator.

---

## Princípios SOLID Respeitados

- **SRP (Single Responsibility):** cada classe tem uma responsabilidade — `ReportGenerator` gera, `ReportGeneratorProxy` gerencia cache
- **OCP (Open/Closed):** código existente não é modificado, apenas estendido com nova classe
- **LSP (Liskov Substitution):** Proxy implementa a mesma interface e pode substituir o original sem o cliente perceber

---

## Resumo

O Proxy é um interceptador. Cria-se uma classe que:
1. Implementa a mesma interface do objeto real
2. Recebe o objeto real no construtor
3. Adiciona a lógica necessária (cache, auth, log) antes ou depois de delegar

O código cliente não sabe — e não precisa saber — se está falando com o objeto real ou com o Proxy.

---

## Referências

- Livro GoF — *Padrões de Projeto: Soluções Reutilizáveis de Software Orientado a Objetos*
- [Refactoring.Guru — Proxy Pattern](https://refactoring.guru/design-patterns/proxy)
