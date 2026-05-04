# Padrão de Projeto: Proxy

**Autor:** Renato Augusto  
**Fonte:** Transcrição de vídeo (YouTube)  
**Referência oficial:** https://refactoring.guru/pt-br/design-patterns/proxy  
**Categoria:** Padrões Estruturais

---

## O que é o Proxy?

O padrão Proxy serve como um **substituto ou espaço reservado para outro objeto**, permitindo controlar o acesso a ele. Com isso, é possível executar ações antes ou depois que uma requisição chega ao objeto original.

É como um **interceptador** entre o código cliente e o objeto real: o cliente nunca conversa diretamente com a classe alvo — ele passa pelo proxy primeiro.

> Similaridade com outros padrões: Facade, Adapter, Decorator — porém com **motivação diferente**. O Decorator decora em cadeia; o Proxy intercepta uma comunicação específica e adiciona uma camada no meio.

---

## Motivação

Imagine uma classe `ReportGenerator` que gera relatórios. Com o tempo, a lógica ficou pesada e passou a demorar 5 segundos por requisição. O front-end fica travado esperando.

**Onde colocar o cache?**

- No Controller? Viola SRP e insere regra de infraestrutura onde não deveria.
- No próprio `ReportGenerator`? Viola OCP — mexer em código em produção é arriscado.

**Solução:** criar uma classe `ReportGeneratorProxy` que encapsula o `ReportGenerator` real e adiciona a camada de cache sem tocar no código existente.

---

## Estrutura do Exemplo (Framework Web)

```
src/
  controllers/
    ReportGeneratorController   # código cliente — chama o proxy
  services/
    ReportGenerator             # classe real com lógica pesada
    ReportGeneratorProxy        # proxy com camada de cache
  repositories/
    ReportRepository            # acesso ao banco de dados
  entities/
    Report                      # entidade com atributo id
```

---

## Interface Compartilhada

Para o proxy funcionar, ambos (`ReportGenerator` e `ReportGeneratorProxy`) devem implementar a mesma interface:

```typescript
interface ReportGeneratorInterface {
  generate(report: Report): any[];
}
```

Isso garante que o Controller não precisa saber se está falando com o proxy ou com a classe real.

---

## Implementação do Proxy (com Cache)

```typescript
class ReportGeneratorProxy implements ReportGeneratorInterface {
  constructor(
    private reportGenerator: ReportGenerator,
    private cache: CacheInterface
  ) {}

  generate(report: Report): any[] {
    const cacheKey = `report_${report.id}`;

    return this.cache.get(cacheKey, () => {
      // Executa apenas se o cache estiver vazio ou expirado
      return this.reportGenerator.generate(report);
    }, { expiresIn: 3600 }); // expira em 1 hora
  }
}
```

**Fluxo:**
1. Proxy verifica se existe cache para `report_<id>`
2. Se existir → retorna do cache (resposta imediata)
3. Se não existir → chama `ReportGenerator.generate()` (5s), armazena no cache, retorna o resultado
4. Após 1 hora o cache expira e o ciclo se repete

---

## No Controller (código cliente)

```typescript
// Antes
const reportGenerator = new ReportGenerator(repository);

// Depois — apenas troca para o proxy
const reportGenerator = new ReportGeneratorProxy(
  new ReportGenerator(repository),
  cache
);

// O restante do código não muda
const reportData = reportGenerator.generate(report);
```

---

## Outros Casos de Uso do Proxy

| Caso | Descrição |
|---|---|
| **Cache** | Evita reprocessamento de operações custosas |
| **Controle de acesso** | Verifica permissões antes de delegar ao objeto real |
| **Log** | Registra chamadas sem poluir a classe original |
| **Lazy initialization** | Adia a criação de objetos pesados até o momento do uso |
| **Validação** | Verifica regras antes de repassar a requisição |

---

## Princípios Respeitados

- **SRP:** cache/log/validação ficam fora da classe de serviço e do controller
- **OCP:** a classe original não é modificada; cria-se algo novo
- **LSP:** o proxy implementa a mesma interface, podendo substituir o original

---

## Diferença do Decorator

| | Proxy | Decorator |
|---|---|---|
| **Propósito** | Controlar acesso / interceptar | Adicionar comportamento em cadeia |
| **Motivação** | Infraestrutura, segurança, cache | Extensão de funcionalidade |
| **Instanciação** | Geralmente cria internamente o objeto real | Recebe o objeto decorado externamente |

---

## Referências

- [Refactoring Guru — Proxy (PT-BR)](https://refactoring.guru/pt-br/design-patterns/proxy)
- Livro: *Padrões de Projeto* — Gang of Four (GoF)
